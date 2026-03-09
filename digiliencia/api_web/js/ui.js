/**
 * ui.js
 * DOM utilities and UI components for the Digiliencia web interface.
 *
 * Responsibilities:
 *  - Toast notifications (success / error / info)
 *  - Modal show/hide helpers (auth, new-chat, confirm)
 *  - Loading states on buttons
 *  - Scroll helpers
 *  - General DOM utilities
 */

// ── Toast notifications ───────────────────────────────────────────────────────

let _toastTimer = null;

/**
 * Shows a temporary toast notification.
 *
 * @param {string} message   - Text to display.
 * @param {'success'|'error'|'info'|'warning'} type
 * @param {number} duration  - Milliseconds before auto-dismiss (default 3500).
 */
export function showToast(message, type = 'info', duration = 3500) {
  const container = document.getElementById('toast-container');
  if (!container) return;

  // Clear any existing toast
  if (_toastTimer) { clearTimeout(_toastTimer); _toastTimer = null; }

  const icons = { success: '✓', error: '✕', info: 'ℹ', warning: '⚠' };
  container.innerHTML = `
    <div class="toast toast--${type}">
      <span class="toast__icon">${icons[type] ?? icons.info}</span>
      <span class="toast__message">${escapeHtml(message)}</span>
      <button class="toast__close" aria-label="Cerrar">✕</button>
    </div>`;

  const toast = container.querySelector('.toast');
  container.classList.add('toast-container--visible');

  // Close button
  toast.querySelector('.toast__close').addEventListener('click', () => dismissToast());

  // Auto-dismiss
  _toastTimer = setTimeout(dismissToast, duration);
}

function dismissToast() {
  const container = document.getElementById('toast-container');
  if (!container) return;
  container.classList.remove('toast-container--visible');
  if (_toastTimer) { clearTimeout(_toastTimer); _toastTimer = null; }
}

// ── Auth modal ────────────────────────────────────────────────────────────────

/** Shows the login/register overlay. */
export function showAuthModal() {
  const overlay = document.getElementById('auth-overlay');
  if (overlay) {
    overlay.classList.add('auth-overlay--visible');
    // Focus first input
    const firstInput = overlay.querySelector('input');
    if (firstInput) setTimeout(() => firstInput.focus(), 100);
  }
}

/** Hides the login/register overlay. */
export function hideAuthModal() {
  const overlay = document.getElementById('auth-overlay');
  if (overlay) overlay.classList.remove('auth-overlay--visible');
}

/**
 * Activates the given auth tab ('login' | 'register').
 * @param {'login'|'register'} tabName
 */
export function switchAuthTab(tabName) {
  document.querySelectorAll('.auth-tab').forEach(tab => {
    tab.classList.toggle('auth-tab--active', tab.dataset.tab === tabName);
  });
  document.querySelectorAll('.auth-panel').forEach(panel => {
    panel.classList.toggle('auth-panel--active', panel.id === `panel-${tabName}`);
  });
}

// ── New-chat modal ────────────────────────────────────────────────────────────

/** Shows the new-conversation creation modal. */
export function showNewChatModal() {
  const modal = document.getElementById('new-chat-modal');
  if (modal) {
    modal.classList.add('modal--visible');
    const titleInput = document.getElementById('new-chat-title');
    if (titleInput) setTimeout(() => titleInput.focus(), 100);
  }
}

/** Hides the new-conversation creation modal. */
export function hideNewChatModal() {
  const modal = document.getElementById('new-chat-modal');
  if (modal) {
    modal.classList.remove('modal--visible');
    // Reset form
    const form = modal.querySelector('form');
    if (form) form.reset();
  }
}

// ── Confirm dialog ────────────────────────────────────────────────────────────

/**
 * Shows a native-style confirm dialog (non-blocking, Promise-based).
 * Replaced the blocking `confirm()` for better UX.
 *
 * @param {string} message
 * @returns {Promise<boolean>}
 */
export function showConfirm(message) {
  return new Promise(resolve => {
    const modal = document.getElementById('confirm-modal');
    const text = document.getElementById('confirm-text');
    const btnOk = document.getElementById('confirm-ok');
    const btnCancel = document.getElementById('confirm-cancel');
    if (!modal || !text || !btnOk || !btnCancel) {
      resolve(window.confirm(message)); // fallback
      return;
    }

    text.textContent = message;
    modal.classList.add('modal--visible');

    function cleanup(result) {
      modal.classList.remove('modal--visible');
      btnOk.removeEventListener('click', onOk);
      btnCancel.removeEventListener('click', onCancel);
      resolve(result);
    }
    const onOk = () => cleanup(true);
    const onCancel = () => cleanup(false);
    btnOk.addEventListener('click', onOk);
    btnCancel.addEventListener('click', onCancel);
  });
}

// ── Loading state ─────────────────────────────────────────────────────────────

/**
 * Enables or disables the loading spinner on a button element.
 *
 * @param {HTMLButtonElement} element
 * @param {boolean} loading
 */
export function setLoading(element, loading) {
  if (!element) return;
  if (loading) {
    element.dataset.originalText = element.innerHTML;
    element.innerHTML = `<span class="spinner"></span>`;
    element.disabled = true;
  } else {
    element.innerHTML = element.dataset.originalText ?? element.innerHTML;
    element.disabled = false;
  }
}

// ── Scroll ────────────────────────────────────────────────────────────────────

/**
 * Scrolls an element to its bottom.
 * @param {HTMLElement} container
 */
export function scrollToBottom(container) {
  if (container) container.scrollTop = container.scrollHeight;
}

// ── DOM utilities ─────────────────────────────────────────────────────────────

/**
 * Escapes HTML special characters for simple strings (like toast messages).
 * For message contents, DOMPurify is used instead.
 * @param {string} str
 * @returns {string}
 */
export function escapeHtml(str) {
  if (typeof str !== 'string') return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

/**
 * Formats a message content string by parsing Markdown and sanitizing the output.
 * Uses marked.js and DOMPurify (injected via CDN in index.html).
 *
 * @param {string} content
 * @returns {string} HTML string
 */
export function formatMessageContent(content) {
  if (!content) return '';
  
  try {
    // 1. Parse markdown
    const rawHtml = window.marked ? window.marked.parse(content) : escapeHtml(content);
    
    // 2. Sanitize to prevent XSS
    return window.DOMPurify ? window.DOMPurify.sanitize(rawHtml) : rawHtml;
  } catch (e) {
    console.error('Error parsing markdown:', e);
    return escapeHtml(content);
  }
}

/**
 * Sets the visibility of the main app layout vs the auth overlay.
 * @param {boolean} loggedIn
 */
export function setAppVisible(loggedIn) {
  const app = document.getElementById('app');
  const auth = document.getElementById('auth-overlay');
  if (loggedIn) {
    app?.classList.remove('app--hidden');
    auth?.classList.remove('auth-overlay--visible');
  } else {
    app?.classList.add('app--hidden');
    auth?.classList.add('auth-overlay--visible');
  }
}

/**
 * Updates the user display name in the header.
 * @param {string} email
 */
export function setUserInfo(email) {
  const el = document.getElementById('user-email');
  if (el) el.textContent = email;
}

/**
 * Clears the user display name.
 */
export function clearUserInfo() {
  const el = document.getElementById('user-email');
  if (el) el.textContent = '';
}
