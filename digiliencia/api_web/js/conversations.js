/**
 * conversations.js
 * Conversation management for the Digiliencia web interface.
 *
 * Responsibilities:
 *  - Loads and renders the conversation list in the sidebar.
 *  - Handles conversation creation (with title + template selection).
 *  - Handles conversation selection (loads message history).
 *  - Handles conversation deletion.
 *  - Dispatches custom events so chat.js can react to selection changes.
 */

import {
  getConversations,
  createConversation,
  deleteConversation,
  getConversation,
  getTemplates,
} from './api.js';
import { showToast, setLoading, showConfirm, escapeHtml } from './ui.js';

// ── State ─────────────────────────────────────────────────────────────────────

/** Currently selected conversation ID. */
let _activeConversationId = null;

/** Cached template list (fetched once per session). */
let _templates = null;

// ── Template loader ───────────────────────────────────────────────────────────

/**
 * Loads and caches the available AI templates.
 * Populates the template <select> in the new-chat modal.
 *
 * @returns {Promise<Array>} The templates array.
 */
export async function loadTemplates() {
  const select = document.getElementById('new-chat-template');
  if (!select) return [];

  if (_templates) {
    _populateTemplateSelect(select, _templates);
    return _templates;
  }

  const result = await getTemplates();
  if (result.ok && result.data?.templates) {
    _templates = result.data.templates;
    _populateTemplateSelect(select, _templates);
    return _templates;
  }

  showToast('No se pudieron cargar las plantillas', 'error');
  return [];
}

function _populateTemplateSelect(select, templates) {
  select.innerHTML = '';
  if (!templates.length) {
    select.innerHTML = '<option value="">Sin plantillas disponibles</option>';
    return;
  }
  templates.forEach(t => {
    const opt = document.createElement('option');
    opt.value = t.id;
    opt.textContent = `${t.name} — ${t.description}`;
    select.appendChild(opt);
  });
}

// ── Conversation list ─────────────────────────────────────────────────────────

/**
 * Fetches all conversations and renders them in the sidebar.
 */
export async function loadConversations() {
  const list = document.getElementById('conversation-list');
  if (!list) return;

  list.innerHTML = '<li class="conversation-list__loading">Cargando...</li>';

  const result = await getConversations();

  if (!result.ok) {
    list.innerHTML = '<li class="conversation-list__empty">Error al cargar conversaciones.</li>';
    return;
  }

  const conversations = result.data?.conversations ?? [];

  if (!conversations.length) {
    list.innerHTML = '<li class="conversation-list__empty">No hay conversaciones. ¡Crea una nueva!</li>';
    return;
  }

  // Load templates for display (name lookup)
  let templateMap = {};
  if (!_templates) await loadTemplates();
  if (_templates) templateMap = Object.fromEntries(_templates.map(t => [t.id, t.name]));

  list.innerHTML = '';
  conversations.forEach(conv => {
    const templateName = templateMap[conv.ai_prompt_id] ?? 'Plantilla desconocida';
    const li = _buildConversationItem(conv, templateName);
    list.appendChild(li);
  });

  // Re-apply active state if there is a currently selected conversation
  if (_activeConversationId) {
    _setActiveListItem(_activeConversationId);
  }
}

/**
 * Builds a sidebar list item element for a conversation.
 */
function _buildConversationItem(conv, templateName) {
  const li = document.createElement('li');
  li.className = 'conversation-item';
  li.dataset.id = conv.id;
  li.setAttribute('role', 'button');
  li.setAttribute('tabindex', '0');
  li.setAttribute('aria-label', `Conversación: ${conv.title}`);

  li.innerHTML = `
    <div class="conversation-item__body">
      <span class="conversation-item__title">${escapeHtml(conv.title)}</span>
      <span class="conversation-item__meta">${escapeHtml(templateName)}</span>
    </div>
    <button class="conversation-item__delete" data-id="${conv.id}" aria-label="Eliminar conversación" title="Eliminar">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <polyline points="3 6 5 6 21 6"/><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"/>
        <path d="M10 11v6M14 11v6"/><path d="M9 6V4h6v2"/>
      </svg>
    </button>`;

  // Select on click
  li.addEventListener('click', (e) => {
    if (!e.target.closest('.conversation-item__delete')) {
      selectConversation(conv.id);
    }
  });
  li.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') selectConversation(conv.id);
  });

  // Delete button
  li.querySelector('.conversation-item__delete').addEventListener('click', async (e) => {
    e.stopPropagation();
    await handleDeleteConversation(conv.id, conv.title);
  });

  return li;
}

// ── Select conversation ───────────────────────────────────────────────────────

/**
 * Selects a conversation, loads its full history, and notifies the chat module.
 *
 * @param {string} conversationId
 */
export async function selectConversation(conversationId) {
  _activeConversationId = conversationId;
  _setActiveListItem(conversationId);

  const result = await getConversation(conversationId);
  if (!result.ok) {
    showToast(`Error al cargar la conversación (${result.status})`, 'error');
    return;
  }

  // Notify the chat module
  document.dispatchEvent(new CustomEvent('conversation:selected', {
    detail: { conversation: result.data }
  }));
}

/** Marks the given list item as active and unmarks the rest. */
function _setActiveListItem(conversationId) {
  document.querySelectorAll('.conversation-item').forEach(el => {
    el.classList.toggle('conversation-item--active', el.dataset.id === conversationId);
  });
}

// ── Create conversation ───────────────────────────────────────────────────────

/**
 * Creates a new conversation from the new-chat form data.
 *
 * @param {string} title
 * @param {string} templateId  - UUID of the selected AI template.
 * @param {HTMLButtonElement} submitBtn
 * @returns {Promise<boolean>}
 */
export async function handleCreateConversation(title, templateId, submitBtn = null) {
  if (!title.trim()) { showToast('El título no puede estar vacío', 'warning'); return false; }
  if (!templateId)   { showToast('Selecciona una plantilla', 'warning'); return false; }

  setLoading(submitBtn, true);
  const result = await createConversation(title.trim(), templateId);
  setLoading(submitBtn, false);

  if (result.ok) {
    showToast('Conversación creada', 'success');
    await loadConversations();
    // Auto-select the new conversation
    if (result.data?.id) await selectConversation(result.data.id);
    return true;
  }

  showToast(`Error al crear la conversación (${result.status})`, 'error');
  return false;
}

// ── Delete conversation ───────────────────────────────────────────────────────

/**
 * Deletes a conversation after confirmation.
 *
 * @param {string} conversationId
 * @param {string} title
 */
export async function handleDeleteConversation(conversationId, title) {
  const confirmed = await showConfirm(`¿Eliminar la conversación "${title}"?`);
  if (!confirmed) return;

  const result = await deleteConversation(conversationId);

  if (result.ok || result.status === 204) {
    showToast('Conversación eliminada', 'success');

    // If the deleted conversation was active, clear the chat panel
    if (_activeConversationId === conversationId) {
      _activeConversationId = null;
      document.dispatchEvent(new CustomEvent('conversation:cleared'));
    }

    await loadConversations();
  } else {
    showToast(`Error al eliminar la conversación (${result.status})`, 'error');
  }
}

/** Returns the currently active conversation ID. */
export function getActiveConversationId() {
  return _activeConversationId;
}

/** Clears the active selection (e.g. after logout). */
export function clearActiveConversation() {
  _activeConversationId = null;
  _templates = null;
  const list = document.getElementById('conversation-list');
  if (list) list.innerHTML = '';
}
