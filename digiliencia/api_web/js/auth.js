/**
 * auth.js
 * Authentication layer for the Digiliencia web interface.
 *
 * Responsibilities:
 *  - Wraps api.js calls for login, register, logout and account deletion.
 *  - Dispatches custom DOM events so the app can react to auth state changes.
 *  - Translates HTTP error codes into user-friendly messages.
 */

import { apiLogin, apiRegister, apiLogout, apiDeleteUser } from './api.js';
import { showToast, setLoading, setAppVisible, setUserInfo, clearUserInfo, showConfirm } from './ui.js';

// ── Internal state ────────────────────────────────────────────────────────────

/** Stores the last authenticated email (for display purposes). */
let _currentEmail = null;

// ── Public helpers ────────────────────────────────────────────────────────────

/** Returns the currently logged-in user's email, or null. */
export function getCurrentEmail() {
  return _currentEmail ?? localStorage.getItem('digiliencia_email');
}

// ── Login ──────────────────────────────────────────────────────────────────────

/**
 * Handles the login form submission.
 *
 * @param {string} email
 * @param {string} password
 * @param {HTMLButtonElement} submitBtn - The submit button (for loading state).
 * @returns {Promise<boolean>} True on success.
 */
export async function login(email, password, submitBtn = null) {
  setLoading(submitBtn, true);

  const result = await apiLogin(email, password);

  setLoading(submitBtn, false);

  if (result.ok) {
    _currentEmail = email;
    localStorage.setItem('digiliencia_email', email);
    setUserInfo(email);
    setAppVisible(true);
    document.dispatchEvent(new CustomEvent('auth:login', { detail: { email } }));
    showToast('Sesión iniciada correctamente', 'success');
    return true;
  }

  const msg = _parseAuthError(result, 'login');
  showToast(msg, 'error');
  return false;
}

// ── Register ──────────────────────────────────────────────────────────────────

/**
 * Handles the registration form submission.
 * Auto-logs in after successful registration (mirrors CLI behaviour).
 *
 * @param {string} email
 * @param {string} password
 * @param {HTMLButtonElement} submitBtn
 * @returns {Promise<boolean>} True on success.
 */
export async function register(email, password, submitBtn = null) {
  setLoading(submitBtn, true);

  const result = await apiRegister(email, password);

  if (result.ok) {
    // Auto-login
    const loginResult = await apiLogin(email, password);
    setLoading(submitBtn, false);

    if (loginResult.ok) {
      _currentEmail = email;
      localStorage.setItem('digiliencia_email', email);
      setUserInfo(email);
      setAppVisible(true);
      document.dispatchEvent(new CustomEvent('auth:login', { detail: { email } }));
      showToast('Cuenta creada e sesión iniciada correctamente', 'success');
      return true;
    }

    showToast('Registro correcto pero el inicio de sesión falló. Por favor inicia sesión manualmente.', 'warning');
    return false;
  }

  setLoading(submitBtn, false);
  const msg = _parseAuthError(result, 'register');
  showToast(msg, 'error');
  return false;
}

// ── Logout ────────────────────────────────────────────────────────────────────

/**
 * Logs out the current user.
 */
export async function logout() {
  await apiLogout();
  _currentEmail = null;
  localStorage.removeItem('digiliencia_email');
  clearUserInfo();
  setAppVisible(false);
  document.dispatchEvent(new CustomEvent('auth:logout'));
  showToast('Sesión cerrada', 'info');
}

// ── Delete user ───────────────────────────────────────────────────────────────

/**
 * Permanently deletes the current user account after confirmation.
 */
export async function deleteUser() {
  const confirmed = await showConfirm('¿Estás seguro de que deseas eliminar tu cuenta? Esta acción es irreversible.');
  if (!confirmed) return;

  const result = await apiDeleteUser();
  if (result.ok) {
    _currentEmail = null;
    localStorage.removeItem('digiliencia_email');
    clearUserInfo();
    setAppVisible(false);
    document.dispatchEvent(new CustomEvent('auth:logout'));
    showToast('Cuenta eliminada correctamente', 'success');
  } else if (result.status === 401) {
    showToast('No autorizado. Por favor inicia sesión de nuevo.', 'error');
  } else {
    showToast(`Error al eliminar la cuenta (${result.status})`, 'error');
  }
}

// ── Error parsing ─────────────────────────────────────────────────────────────

/**
 * Translates an API error response into a user-friendly string.
 *
 * @param {{status: number, data: any}} result
 * @param {'login'|'register'} context
 * @returns {string}
 */
function _parseAuthError(result, context) {
  const { status, data } = result;

  if (status === 0) return 'No se pudo conectar al servidor. Verifica la conexión.';

  if (context === 'login') {
    if (status === 401) return 'Email o contraseña incorrectos.';
    if (status === 422) {
      const detail = data?.detail;
      if (Array.isArray(detail) && detail.length > 0) {
        return `Error de validación: ${detail[0].msg}`;
      }
    }
    return `Error al iniciar sesión (${status}).`;
  }

  if (context === 'register') {
    if (status === 400) {
      const detail = data?.detail;
      if (typeof detail === 'string') return `Registro fallido: ${detail}`;
      if (typeof detail === 'object' && detail?.reason) return `Registro fallido: ${detail.reason}`;
    }
    if (status === 422) {
      const detail = data?.detail;
      if (Array.isArray(detail) && detail.length > 0) {
        const err = detail[0];
        const field = err.loc?.at(-1) ?? 'campo';
        return `Error en ${field}: ${err.msg}`;
      }
    }
    return `Error al registrarse (${status}).`;
  }

  return `Error inesperado (${status}).`;
}
