/**
 * api.js
 * Low-level API client for the Digiliencia backend.
 *
 * Responsibilities:
 *  - Manages BASE_URL configuration.
 *  - Attaches the JWT Bearer token to every authenticated request.
 *  - Provides one typed function per API endpoint (mirrors api_cli behaviour).
 *  - Persists the token in localStorage between page reloads.
 */

// ── Configuration ────────────────────────────────────────────────────────────

/** Default API base URL. Use relative /api since Nginx proxies it. */
const BASE_URL = '/api';

/** localStorage key used to persist the JWT token. */
const TOKEN_KEY = 'digiliencia_token';

// ── Token helpers ─────────────────────────────────────────────────────────────

/** Returns the stored JWT token, or null if none. */
export function getToken() {
  return localStorage.getItem(TOKEN_KEY);
}

/** Saves a JWT token to localStorage. */
export function setToken(token) {
  localStorage.setItem(TOKEN_KEY, token);
}

/** Removes the JWT token from localStorage. */
export function clearToken() {
  localStorage.removeItem(TOKEN_KEY);
}

/** Returns true if a token is currently stored. */
export function isAuthenticated() {
  return Boolean(getToken());
}

// ── Core fetch wrapper ──────────────────────────────────────────────────────

/**
 * Makes an HTTP request to the API.
 *
 * @param {string} method   - HTTP verb ('GET', 'POST', 'PATCH', 'DELETE').
 * @param {string} path     - API path (e.g. '/auth/login').
 * @param {object|null} body - JSON body payload (omit for GET/DELETE).
 * @param {boolean} auth    - Whether to attach the Bearer token.
 * @returns {Promise<{ok: boolean, status: number, data: any}>}
 */
async function request(method, path, body = null, auth = true) {
  const headers = { 'Content-Type': 'application/json' };

  if (auth) {
    const token = getToken();
    if (token) headers['Authorization'] = `Bearer ${token}`;
  }

  const options = { method, headers };
  if (body !== null) options.body = JSON.stringify(body);

  let response;
  try {
    response = await fetch(`${BASE_URL}${path}`, options);
  } catch (networkError) {
    return { ok: false, status: 0, data: null, error: `Network error: ${networkError.message}` };
  }

  // Parse body only if there is content
  let data = null;
  const contentType = response.headers.get('content-type') || '';
  if (contentType.includes('application/json') && response.status !== 204) {
    try { data = await response.json(); } catch { data = null; }
  }

  return { ok: response.ok, status: response.status, data };
}

// ── Health ────────────────────────────────────────────────────────────────────

/**
 * GET /health
 * @returns {Promise<{ok: boolean, status: string}>}
 */
export async function healthCheck() {
  return request('GET', '/health', null, false);
}

// ── Authentication ────────────────────────────────────────────────────────────

/**
 * POST /auth/login
 * Authenticates a user. Stores the returned JWT token on success.
 *
 * @param {string} email
 * @param {string} password
 * @returns {Promise<{ok: boolean, status: number, data: any}>}
 */
export async function apiLogin(email, password) {
  const result = await request('POST', '/auth/login', { email, password }, false);
  if (result.ok && result.data?.access_token) {
    setToken(result.data.access_token);
  }
  return result;
}

/**
 * POST /auth/register
 * Registers a new user account.
 *
 * @param {string} email
 * @param {string} password
 * @returns {Promise<{ok: boolean, status: number, data: any}>}
 */
export async function apiRegister(email, password) {
  return request('POST', '/auth/register', { email, password }, false);
}

/**
 * POST /users/me (used by CLI for logout notification)
 * Clears the local JWT token regardless of server response.
 *
 * @returns {Promise<void>}
 */
export async function apiLogout() {
  try { await request('POST', '/users/me'); } catch { /* ignore */ }
  clearToken();
}

/**
 * DELETE /users/me
 * Permanently deletes the current user account and clears the token.
 *
 * @returns {Promise<{ok: boolean, status: number, data: any}>}
 */
export async function apiDeleteUser() {
  const result = await request('DELETE', '/users/me');
  if (result.ok) clearToken();
  return result;
}

// ── Conversations ─────────────────────────────────────────────────────────────

/**
 * GET /chats/conversations
 * Returns all conversations for the authenticated user.
 *
 * @returns {Promise<{ok: boolean, data: {conversations: ConversationSummary[]}}>}
 */
export async function getConversations() {
  return request('GET', '/chats/conversations');
}

/**
 * PATCH /chats
 * Creates a new conversation.
 *
 * @param {string} title        - Display title for the chat.
 * @param {string} ai_prompt_id - UUID of the AI template/prompt.
 * @returns {Promise<{ok: boolean, status: number, data: ConversationSummary}>}
 */
export async function createConversation(title, ai_prompt_id) {
  return request('PATCH', '/chats', { title, ai_prompt_id });
}

/**
 * GET /chats/{id}
 * Returns the full conversation including message history.
 *
 * @param {string} chatId
 * @returns {Promise<{ok: boolean, data: ConversationFull}>}
 */
export async function getConversation(chatId) {
  return request('GET', `/chats/${chatId}`);
}

/**
 * PATCH /chats/{id}
 * Sends a user message and returns the AI response.
 *
 * NOTE: This call uses NO timeout — the chatbot model can take a long time
 * to generate a response. This mirrors the CLI behaviour (timeout=10000s).
 * fetch() has no built-in timeout by default; we explicitly avoid adding one
 * here so slow models are never aborted on the client side.
 *
 * @param {string} chatId
 * @param {string} content   - The user's message text.
 * @param {string} model_id  - UUID of the AI model to use.
 * @returns {Promise<{ok: boolean, data: {text: string}}>}
 */
export async function sendMessage(chatId, content, model_id) {
  // Use a dedicated fetch call without any AbortSignal so the browser
  // never cancels this request, regardless of how long the model takes.
  const headers = { 'Content-Type': 'application/json' };
  const token = getToken();
  if (token) headers['Authorization'] = `Bearer ${token}`;

  let response;
  try {
    response = await fetch(`${BASE_URL}/chats/${chatId}`, {
      method: 'PATCH',
      headers,
      body: JSON.stringify({ content, model_id }),
      // No signal → no timeout → waits indefinitely for the AI response
    });
  } catch (networkError) {
    return { ok: false, status: 0, data: null, error: `Network error: ${networkError.message}` };
  }

  let data = null;
  const contentType = response.headers.get('content-type') || '';
  if (contentType.includes('application/json') && response.status !== 204) {
    try { data = await response.json(); } catch { data = null; }
  }

  return { ok: response.ok, status: response.status, data };
}

/**
 * DELETE /chats/{id}
 * Deletes a conversation.
 *
 * @param {string} chatId
 * @returns {Promise<{ok: boolean, status: number}>}
 */
export async function deleteConversation(chatId) {
  return request('DELETE', `/chats/${chatId}`);
}

// ── Templates ─────────────────────────────────────────────────────────────────

/**
 * GET /chats/templates
 * Returns all available AI prompt templates.
 *
 * @returns {Promise<{ok: boolean, data: {templates: TemplateSummary[]}}>}
 */
export async function getTemplates() {
  return request('GET', '/chats/templates');
}

// ── Models ────────────────────────────────────────────────────────────────────

/**
 * GET /chats/models
 * Returns all available AI models.
 *
 * @returns {Promise<{ok: boolean, data: {models: ModelSummary[]}}>}
 */
export async function getModels() {
  return request('GET', '/chats/models');
}
