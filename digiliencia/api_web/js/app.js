/**
 * app.js
 * Main orchestrator for the Digiliencia web interface.
 *
 * Responsibilities:
 *  - Initialises the application on DOMContentLoaded.
 *  - Checks the API health and token state on startup.
 *  - Wires all event listeners (forms, buttons, custom events).
 *  - Delegates to auth.js, conversations.js, and chat.js.
 */

import { isAuthenticated, healthCheck } from './api.js';
import { login, register, logout, deleteUser, getCurrentEmail } from './auth.js';
import {
  loadConversations,
  loadTemplates,
  handleCreateConversation,
  clearActiveConversation,
} from './conversations.js';
import {
  openConversation,
  clearChatPanel,
  handleSendMessage,
  loadModels,
  setSelectedModel,
  resetChatState,
} from './chat.js';
import {
  setAppVisible,
  setUserInfo,
  showAuthModal,
  switchAuthTab,
  showNewChatModal,
  hideNewChatModal,
  showToast,
} from './ui.js';

// ── Entry point ───────────────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', init);

async function init() {
  _initTheme();
  _wireEventListeners();
  await _bootstrap();
}

// ── Theme Management ──────────────────────────────────────────────────────────

function _initTheme() {
  try {
    const savedTheme = localStorage.getItem('digiliencia_theme');
    const isDark = savedTheme === 'dark';
    
    if (isDark) {
      document.documentElement.setAttribute('data-theme', 'dark');
    } else {
      document.documentElement.removeAttribute('data-theme');
    }
    
    _updateThemeIcon(isDark);
    console.log('[Theme] Initialized theme:', isDark ? 'dark' : 'light');
  } catch (err) {
    console.error('[Theme] Failed to initialize theme:', err);
  }
}

function _toggleTheme() {
  try {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newIsDark = currentTheme !== 'dark';
    
    console.log('[Theme] Toggling to:', newIsDark ? 'dark' : 'light');

    if (newIsDark) {
      document.documentElement.setAttribute('data-theme', 'dark');
      localStorage.setItem('digiliencia_theme', 'dark');
    } else {
      document.documentElement.removeAttribute('data-theme');
      localStorage.setItem('digiliencia_theme', 'light');
    }
    
    _updateThemeIcon(newIsDark);
  } catch (err) {
    console.error('[Theme] Failed to toggle theme:', err);
  }
}

function _updateThemeIcon(isDark) {
  const iconMoon = document.getElementById('icon-moon');
  const iconSun = document.getElementById('icon-sun');
  
  if (iconMoon && iconSun) {
    if (isDark) {
      iconMoon.style.display = 'none';
      iconSun.style.display = 'block';
    } else {
      iconMoon.style.display = 'block';
      iconSun.style.display = 'none';
    }
  }
}

// ── Bootstrap ─────────────────────────────────────────────────────────────────

/**
 * Checks health, restores session if a token exists, otherwise shows auth.
 */
async function _bootstrap() {
  // Health check (non-blocking UI)
  const health = await healthCheck();
  if (!health.ok) {
    showToast('No se puede conectar al servidor. Algunas funciones pueden no estar disponibles.', 'warning', 6000);
  }

  if (isAuthenticated()) {
    const email = getCurrentEmail() ?? 'Usuario';
    setUserInfo(email);
    setAppVisible(true);
    await _onLogin();
  } else {
    setAppVisible(false);
  }
}

// ── Post-login setup ──────────────────────────────────────────────────────────

/**
 * Called after a successful login (or on restore).
 * Loads models and conversations in parallel.
 */
async function _onLogin() {
  await Promise.all([loadModels(), loadConversations()]);
}

// ── Event wiring ──────────────────────────────────────────────────────────────

function _wireEventListeners() {
  // ── Auth tabs ─────────────────────────────────────────────────
  document.querySelectorAll('.auth-tab').forEach(tab => {
    tab.addEventListener('click', () => switchAuthTab(tab.dataset.tab));
  });

  // ── Theme toggle ──────────────────────────────────────────────
  document.getElementById('btn-theme-toggle')?.addEventListener('click', _toggleTheme);

  // ── Login form ────────────────────────────────────────────────
  const loginForm = document.getElementById('login-form');
  loginForm?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('login-email').value.trim();
    const password = document.getElementById('login-password').value;
    const btn = loginForm.querySelector('button[type="submit"]');
    const ok = await login(email, password, btn);
    if (ok) await _onLogin();
  });

  // ── Register form ─────────────────────────────────────────────
  const registerForm = document.getElementById('register-form');
  registerForm?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('register-email').value.trim();
    const password = document.getElementById('register-password').value;
    const btn = registerForm.querySelector('button[type="submit"]');
    const ok = await register(email, password, btn);
    if (ok) await _onLogin();
  });

  // ── Logout button ─────────────────────────────────────────────
  document.getElementById('btn-logout')?.addEventListener('click', async () => {
    await logout();
    resetChatState();
    clearActiveConversation();
  });

  // ── Delete user button ────────────────────────────────────────
  document.getElementById('btn-delete-user')?.addEventListener('click', async () => {
    await deleteUser();
    resetChatState();
    clearActiveConversation();
  });

  // ── New chat button ───────────────────────────────────────────
  document.getElementById('btn-new-chat')?.addEventListener('click', async () => {
    await loadTemplates();
    showNewChatModal();
  });

  // ── New chat form submission ───────────────────────────────────
  const newChatForm = document.getElementById('new-chat-form');
  newChatForm?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const title = document.getElementById('new-chat-title').value;
    const templateId = document.getElementById('new-chat-template').value;
    const btn = newChatForm.querySelector('button[type="submit"]');
    const ok = await handleCreateConversation(title, templateId, btn);
    if (ok) hideNewChatModal();
  });

  // ── New chat modal cancel ─────────────────────────────────────
  document.getElementById('new-chat-cancel')?.addEventListener('click', hideNewChatModal);

  // Close modal on overlay click
  document.getElementById('new-chat-modal')?.addEventListener('click', (e) => {
    if (e.target.id === 'new-chat-modal') hideNewChatModal();
  });

  // ── Model selector ────────────────────────────────────────────
  document.getElementById('model-select')?.addEventListener('change', (e) => {
    setSelectedModel(e.target.value);
  });

  // ── Message input / send ──────────────────────────────────────
  const messageInput = document.getElementById('message-input');
  const sendBtn = document.getElementById('btn-send');

  sendBtn?.addEventListener('click', async () => {
    const content = messageInput?.value ?? '';
    await handleSendMessage(content);
  });

  messageInput?.addEventListener('keydown', async (e) => {
    // Send on Enter (without Shift)
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      const content = messageInput.value;
      await handleSendMessage(content);
    }
  });

  // Auto-resize textarea
  messageInput?.addEventListener('input', () => {
    messageInput.style.height = 'auto';
    messageInput.style.height = `${Math.min(messageInput.scrollHeight, 180)}px`;
  });

  // ── Conversation events ───────────────────────────────────────
  document.addEventListener('conversation:selected', (e) => {
    openConversation(e.detail.conversation);
  });

  document.addEventListener('conversation:cleared', () => {
    clearChatPanel();
  });

  // ── Auth events ───────────────────────────────────────────────
  document.addEventListener('auth:logout', () => {
    // Nothing extra — already handled by each auth function
  });
}
