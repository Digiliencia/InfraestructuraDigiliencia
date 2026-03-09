/**
 * chat.js
 * Chat interaction module for the Digiliencia web interface.
 *
 * Responsibilities:
 *  - Renders message history (user vs AI discriminated by order_number parity).
 *  - Loads available AI models and manages model selection.
 *  - Handles sending messages (optimistic UI, blocks input while waiting).
 *  - Manages the chat panel empty state (no conversation selected).
 *  - Listens for conversation:selected / conversation:cleared events.
 *
 * NOTE on user/AI discrimination:
 *  The backend saves BOTH user and AI messages with model_id = payload.model_id
 *  (see api/routers/chats.py, line 208). Therefore model_id is NOT a reliable
 *  discriminator. The API itself uses order_number parity internally:
 *    odd  order_number → USER message
 *    even order_number → AI message
 *  We adopt the same convention here.
 */

import { sendMessage, getModels, getConversation } from './api.js';
import { showToast, scrollToBottom, formatMessageContent, escapeHtml } from './ui.js';

// ── State ─────────────────────────────────────────────────────────────────────

/** Currently selected conversation ID. */
let _currentChatId = null;

/** Currently selected AI model ID. */
let _selectedModelId = null;

/** Cached model list. */
let _models = null;

// ── Initialisation ────────────────────────────────────────────────────────────

/**
 * Loads available AI models and populates the model dropdown.
 * Should be called once on login.
 */
export async function loadModels() {
  const select = document.getElementById('model-select');
  if (!select) return;

  if (_models) {
    _populateModelSelect(select, _models);
    return;
  }

  const result = await getModels();
  if (result.ok && result.data?.models?.length) {
    _models = result.data.models;
    _populateModelSelect(select, _models);
  } else {
    select.innerHTML = '<option value="">Sin modelos disponibles</option>';
  }
}

function _populateModelSelect(select, models) {
  select.innerHTML = '';
  models.forEach((m, i) => {
    const opt = document.createElement('option');
    opt.value = m.id;
    opt.textContent = m.name;
    if (i === 0) { opt.selected = true; _selectedModelId = m.id; }
    select.appendChild(opt);
  });
}

/**
 * Updates the selected model when the dropdown changes.
 * @param {string} modelId
 */
export function setSelectedModel(modelId) {
  _selectedModelId = modelId;
}

// ── Conversation loading ──────────────────────────────────────────────────────

/**
 * Loads a full conversation object into the chat panel.
 * Called when conversation:selected is dispatched.
 *
 * @param {{id: string, title: string, messages: Message[]}} conversation
 */
export function openConversation(conversation) {
  _currentChatId = conversation.id;

  // Update header title
  const titleEl = document.getElementById('chat-title');
  if (titleEl) titleEl.textContent = conversation.title;

  // Show/hide empty-state vs message area
  _showChatPanel(true);

  renderMessages(conversation.messages ?? []);
}

/**
 * Renders an array of messages into the chat panel.
 * @param {Message[]} messages
 */
export function renderMessages(messages) {
  const container = document.getElementById('messages-container');
  if (!container) return;

  container.innerHTML = '';

  if (!messages.length) {
    container.innerHTML = '<div class="messages__empty">Aún no hay mensajes. ¡Escribe algo!</div>';
    return;
  }

  messages.forEach(msg => {
    const bubble = _buildBubble(msg);
    container.appendChild(bubble);
  });

  scrollToBottom(container);
}

/**
 * Builds a single message bubble element.
 *
 * User/AI discrimination uses order_number parity:
 *   odd  → user message
 *   even → AI message
 *
 * IMPORTANT: model_id cannot be used — the backend stores the same model_id
 * on both user and AI messages (see api/routers/chats.py line 208).
 *
 * @param {{id: string, order_number: number, content: string}} msg
 * @param {boolean} [forceUser]  - If true the bubble is always rendered as user.
 * @returns {HTMLElement}
 */
function _buildBubble(msg, forceUser = false) {
  // Odd order_number = user message; even = AI message.
  // For optimistic bubbles order_number may be absent — treat as user.
  const isUser = forceUser || msg.order_number == null || msg.order_number % 2 !== 0;
  const div = document.createElement('div');
  div.className = `message ${isUser ? 'message--user' : 'message--ai'}`;
  div.dataset.id = msg.id;

  div.innerHTML = `
    <div class="message__avatar" aria-hidden="true">
      ${isUser
        ? '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 12c2.7 0 4.8-2.1 4.8-4.8S14.7 2.4 12 2.4 7.2 4.5 7.2 7.2 9.3 12 12 12zm0 2.4c-3.2 0-9.6 1.6-9.6 4.8v2.4h19.2v-2.4c0-3.2-6.4-4.8-9.6-4.8z"/></svg>'
        : '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm1 14H11v-2h2v2zm0-4H11V7h2v5z"/></svg>'
      }
    </div>
    <div class="message__content">
      <span class="message__role">${isUser ? 'Tú' : 'Asistente'}</span>
      <div class="message__text">${formatMessageContent(msg.content)}</div>
    </div>`;

  return div;
}

/** Builds a temporary typing indicator bubble. */
function _buildTypingIndicator() {
  const div = document.createElement('div');
  div.className = 'message message--ai message--typing';
  div.id = 'typing-indicator';
  div.innerHTML = `
    <div class="message__avatar" aria-hidden="true">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm1 14H11v-2h2v2zm0-4H11V7h2v5z"/></svg>
    </div>
    <div class="message__content">
      <span class="message__role">Asistente</span>
      <div class="typing-dots"><span></span><span></span><span></span></div>
    </div>`;
  return div;
}

// ── Send message ──────────────────────────────────────────────────────────────

// ── Input blocking state ──────────────────────────────────────────────────────

/** True while waiting for an AI response — prevents sending another message. */
let _isBusy = false;

/**
 * Enables or disables the chat input area during AI processing.
 * @param {boolean} busy
 */
function _setChatBusy(busy) {
  _isBusy = busy;
  const input = document.getElementById('message-input');
  const sendBtn = document.getElementById('btn-send');
  if (input) {
    input.disabled = busy;
    input.placeholder = busy
      ? 'Esperando respuesta del asistente…'
      : 'Escribe tu mensaje… (Enter para enviar, Shift+Enter para nueva línea)';
  }
  if (sendBtn) sendBtn.disabled = busy;
}

// ── Send message ──────────────────────────────────────────────────────────────

/**
 * Sends a user message and displays the AI response.
 * The input is disabled for the entire duration of the request.
 *
 * @param {string} content  - The user's message text.
 */
export async function handleSendMessage(content) {
  if (!content.trim()) return;
  if (_isBusy) {
    showToast('Espera a que el asistente termine de responder', 'warning');
    return;
  }
  if (!_currentChatId) {
    showToast('Selecciona o crea una conversación primero', 'warning');
    return;
  }
  if (!_selectedModelId) {
    showToast('Selecciona un modelo de IA', 'warning');
    return;
  }

  const container = document.getElementById('messages-container');
  const input = document.getElementById('message-input');

  // Optimistic: append user bubble immediately (forceUser=true, no order_number yet)
  const optimisticMsg = { id: `opt-${Date.now()}`, content };
  container?.appendChild(_buildBubble(optimisticMsg, /*forceUser=*/true));

  // Show typing indicator
  container?.appendChild(_buildTypingIndicator());
  scrollToBottom(container);

  // Clear input and lock the whole input area
  if (input) { input.value = ''; input.style.height = 'auto'; }
  _setChatBusy(true);

  const result = await sendMessage(_currentChatId, content, _selectedModelId);

  // Remove typing indicator and restore input
  document.getElementById('typing-indicator')?.remove();
  _setChatBusy(false);
  if (input) input.focus();

  if (!result.ok) {
    // Remove the optimistic bubble on failure
    container?.querySelector('[data-id^="opt-"]')?.remove();
    showToast(_parseSendError(result), 'error');
    return;
  }

  // Reload the full conversation from server (authoritative history with correct order_numbers)
  const refreshed = await getConversation(_currentChatId);
  if (refreshed.ok && refreshed.data?.messages) {
    renderMessages(refreshed.data.messages);
  } else {
    // Fallback: render optimistic AI bubble as even order_number
    const aiMsg = { order_number: 2, content: result.data?.text ?? '' };
    container?.appendChild(_buildBubble(aiMsg));
    scrollToBottom(container);
  }
}

// ── Panel state ───────────────────────────────────────────────────────────────

/** Shows or hides the active chat panel vs the empty placeholder. */
function _showChatPanel(visible) {
  document.getElementById('chat-empty')?.classList.toggle('chat-empty--hidden', visible);
  document.getElementById('chat-active')?.classList.toggle('chat-active--hidden', !visible);
}

/** Resets the chat panel to the empty state (no conversation). */
export function clearChatPanel() {
  _currentChatId = null;
  _showChatPanel(false);
  const titleEl = document.getElementById('chat-title');
  if (titleEl) titleEl.textContent = '';
  const container = document.getElementById('messages-container');
  if (container) container.innerHTML = '';
}

/** Clears model cache (call on logout). */
export function resetChatState() {
  _currentChatId = null;
  _selectedModelId = null;
  _models = null;
  clearChatPanel();
}

// ── Error parsing ─────────────────────────────────────────────────────────────

function _parseSendError(result) {
  if (result.status === 0) return 'Error de red. No se pudo enviar el mensaje.';
  if (result.status === 404) return 'La conversación no existe o fue eliminada.';
  if (result.status === 409) return 'El chat está ocupado. Espera un momento.';
  return `Error al enviar el mensaje (${result.status}).`;
}
