<?php
/*
Plugin Name: AI Engine - Digiliencia Adapter PRO
Description: Conecta AI Engine Pro con la API personalizada de Digiliencia (SCAYLE).
Version: 1.2
*/

if (!defined('ABSPATH')) exit;

class Mwai_Digiliencia_Adapter {

  private $email    = 'manuel@gmail.com';
  private $password = 'Manuel1*';
  private $model_id = '0815bd64-392d-4b57-ae43-8a671adfe95f'; // qwen3:32b

  public function __construct() {
    add_filter('mwai_chatbot_takeover', [$this, 'handle_request'], 10, 2);
  }

  /* ================= JWT ================= */

  private function get_token($force = false) {

    if (!$force) {
      $token = get_transient('digiliencia_jwt');
      if ($token) return $token;
    }

    $response = wp_remote_post(
      'https://api.digiliencia.org/api/auth/login',
      [
        'timeout' => 30,
        'headers' => ['Content-Type' => 'application/json'],
        'body'    => json_encode([
          'email'    => $this->email,
          'password' => $this->password
        ])
      ]
    );

    if (is_wp_error($response)) return false;

    $body = json_decode(wp_remote_retrieve_body($response), true);
    if (empty($body['access_token'])) return false;

    // Token dura ~1 año, guardamos por 11 meses para renovar con margen
    set_transient('digiliencia_jwt', $body['access_token'], 11 * 30 * DAY_IN_SECONDS);

    return $body['access_token'];
  }

  /* ================= CHAT ID ================= */

  private function get_external_chat_id($mwaiChatId, $token, $firstMessage = null) {

    $saved = get_option('digiliencia_chat_' . $mwaiChatId);
    if ($saved) return $saved;

    // Generar título obligatorio
    if (!empty($firstMessage)) {
      $title = mb_substr(trim($firstMessage), 0, 60);
    } else {
      $title = 'Conversación ' . current_time('Y-m-d H:i:s');
    }

    $chat = wp_remote_request(
      'https://api.digiliencia.org/api/chats',
      [
        'method'  => 'PATCH',
        'timeout' => 30,
        'headers' => [
          'Authorization' => 'Bearer ' . $token,
          'Content-Type'  => 'application/json'
        ],
        'body' => json_encode([
          'title' => $title
        ])
      ]
    );

    if (is_wp_error($chat)) return false;

    $body    = json_decode(wp_remote_retrieve_body($chat), true);
    $chat_id = $body['id'] ?? null;

    if ($chat_id) {
      update_option('digiliencia_chat_' . $mwaiChatId, $chat_id);
    }

    return $chat_id;
  }

  /* ================= REQUEST ================= */

  public function handle_request($reply, $query) {

    $token = $this->get_token();
    if (!$token) return "Authentication error.";

    $external_chat_id = $this->get_external_chat_id(
      $query->chatId,
      $token,
      $query->message
    );

    // Si no se pudo crear el chat → token expirado → renovar y reintentar
    if (!$external_chat_id) {
      $token = $this->get_token(true);
      if (!$token) return "Re-authentication failed.";
      $external_chat_id = $this->get_external_chat_id(
        $query->chatId,
        $token,
        $query->message
      );
    }

    if (!$external_chat_id) return "Chat creation error.";

    $response = $this->send_message($external_chat_id, $query->message, $token);

    // Si 401 en el envío → renovar token y reintentar
    if ($response === 401) {
      $token = $this->get_token(true);
      if (!$token) return "Re-authentication failed.";
      $response = $this->send_message($external_chat_id, $query->message, $token);
    }

    if (is_string($response)) return $response;

    return "Unexpected API error.";
  }

  private function send_message($chat_id, $message, $token) {

    $response = wp_remote_request(
      "https://api.digiliencia.org/api/chats/{$chat_id}",
      [
        'method'  => 'PATCH',
        'timeout' => 600,
        'headers' => [
          'Authorization' => 'Bearer ' . $token,
          'Content-Type'  => 'application/json'
        ],
        'body' => json_encode([
          'content'  => $message,
          'model_id' => $this->model_id
        ])
      ]
    );

    if (is_wp_error($response)) return "Message send error.";

    $code = wp_remote_retrieve_response_code($response);
    if ($code === 401) return 401;

    $body = json_decode(wp_remote_retrieve_body($response), true);

    if (!empty($body['text'])) {
      return $body['text'];
    }

    return "Invalid AI response.";
  }
}

new Mwai_Digiliencia_Adapter();
