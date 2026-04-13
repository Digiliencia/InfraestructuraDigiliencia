<?php
/*
Plugin Name: Digiliencia - Descargar Conversación
Description: Añade un botón al chatbot para imprimir o guardar la conversación como PDF.
Version: 1.0
*/

if (!defined('ABSPATH')) exit;

class Digiliencia_Descargar_Conversacion {

  public function __construct() {
    // Endpoint para mostrar la conversación imprimible
    add_action('init', [$this, 'registrar_endpoint']);
    add_action('template_redirect', [$this, 'mostrar_pagina_impresion']);

    // Inyectar el botón en el chatbot (ambos hooks para mayor compatibilidad)
    add_action('wp_footer', [$this, 'inyectar_boton']);
    add_action('wp_head',   [$this, 'inyectar_boton']);
  }

  /* ================= ENDPOINT ================= */

  public function registrar_endpoint() {
    add_rewrite_rule(
      '^descargar-conversacion/?$',
      'index.php?digiliencia_descarga=1',
      'top'
    );
    add_rewrite_tag('%digiliencia_descarga%', '1');
  }

  public function mostrar_pagina_impresion() {
    if (!get_query_var('digiliencia_descarga')) return;

    $chat_id = sanitize_text_field($_GET['chatId'] ?? '');
    if (empty($chat_id)) {
      wp_die('No se ha indicado ninguna conversación.');
    }

    $mensajes = $this->obtener_mensajes($chat_id);
    if (empty($mensajes)) {
      wp_die('No se ha encontrado la conversación o está vacía.');
    }

    $this->renderizar_pagina($mensajes, $chat_id);
    exit;
  }

  /* ================= OBTENER MENSAJES ================= */

  private function obtener_mensajes($chat_id) {
    global $wpdb;

    // AI Engine guarda las conversaciones en mwai_messages (o similar)
    // Intentamos primero con la tabla estándar de AI Engine Pro
    $tabla_messages = $wpdb->prefix . 'mwai_messages';
    $tabla_chats    = $wpdb->prefix . 'mwai_chats';

    // Verificar qué tablas existen
    $existe_messages = $wpdb->get_var("SHOW TABLES LIKE '$tabla_messages'");
    $existe_chats    = $wpdb->get_var("SHOW TABLES LIKE '$tabla_chats'");

    if ($existe_chats && $existe_messages) {
      // Estructura con tablas separadas
      $chat = $wpdb->get_row($wpdb->prepare(
        "SELECT * FROM $tabla_chats WHERE chatId = %s LIMIT 1",
        $chat_id
      ));

      if (!$chat) return [];

      $mensajes = $wpdb->get_results($wpdb->prepare(
        "SELECT role, content, created_at FROM $tabla_messages
         WHERE chatId = %s ORDER BY created_at ASC",
        $chat_id
      ));

      return $mensajes ?: [];
    }

    // Fallback: AI Engine guarda debates como posts o en mwai_discussions
    $tabla_discussions = $wpdb->prefix . 'mwai_discussions';
    $existe_discussions = $wpdb->get_var("SHOW TABLES LIKE '$tabla_discussions'");

    if ($existe_discussions) {
      $row = $wpdb->get_row($wpdb->prepare(
        "SELECT * FROM $tabla_discussions WHERE chatId = %s LIMIT 1",
        $chat_id
      ));

      if (!$row) return [];

      // Los mensajes suelen estar serializados en un campo JSON
      $data = json_decode($row->messages ?? $row->content ?? '', true);
      if (is_array($data)) {
        $result = [];
        foreach ($data as $m) {
          $obj = new stdClass();
          $obj->role    = $m['role'] ?? 'user';
          $obj->content = $m['content'] ?? '';
          $result[] = $obj;
        }
        return $result;
      }
    }

    // Último fallback: buscar en wp_options (debates de AI Engine)
    $debates = get_option('mwai_discussions', []);
    foreach ($debates as $debate) {
      if (($debate['chatId'] ?? '') === $chat_id) {
        $result = [];
        foreach ($debate['messages'] ?? [] as $m) {
          $obj = new stdClass();
          $obj->role    = $m['role'] ?? 'user';
          $obj->content = $m['content'] ?? '';
          $result[] = $obj;
        }
        return $result;
      }
    }

    return [];
  }

  /* ================= RENDERIZAR PÁGINA ================= */

  private function renderizar_pagina($mensajes, $chat_id) {
    $titulo = get_bloginfo('name') . ' — Conversación';
    $fecha  = date_i18n('d/m/Y H:i');
    ?>
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title><?php echo esc_html($titulo); ?></title>
      <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }

        body {
          font-family: Arial, sans-serif;
          font-size: 14px;
          color: #222;
          background: #f5f5f5;
          padding: 20px;
        }

        .contenedor {
          max-width: 760px;
          margin: 0 auto;
          background: #fff;
          border-radius: 8px;
          padding: 32px;
          box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        }

        .cabecera {
          display: flex;
          justify-content: space-between;
          align-items: flex-start;
          border-bottom: 2px solid #c0392b;
          padding-bottom: 16px;
          margin-bottom: 24px;
        }

        .cabecera h1 {
          font-size: 18px;
          color: #c0392b;
          font-weight: bold;
        }

        .cabecera .meta {
          font-size: 12px;
          color: #888;
          text-align: right;
        }

        .mensaje {
          margin-bottom: 16px;
          padding: 12px 16px;
          border-radius: 8px;
          line-height: 1.6;
        }

        .mensaje.usuario {
          background: #c0392b;
          color: #fff;
          margin-left: 60px;
        }

        .mensaje.asistente {
          background: #f0f0f0;
          color: #222;
          margin-right: 60px;
        }

        .mensaje .rol {
          font-size: 11px;
          font-weight: bold;
          text-transform: uppercase;
          letter-spacing: 0.5px;
          margin-bottom: 6px;
          opacity: 0.7;
        }

        .mensaje.usuario .rol { color: rgba(255,255,255,0.8); }
        .mensaje.asistente .rol { color: #888; }

        .pie {
          margin-top: 32px;
          padding-top: 16px;
          border-top: 1px solid #eee;
          font-size: 11px;
          color: #aaa;
          text-align: center;
        }

        .btn-imprimir {
          display: inline-block;
          margin: 0 auto 24px;
          padding: 10px 24px;
          background: #c0392b;
          color: #fff;
          border: none;
          border-radius: 6px;
          font-size: 14px;
          cursor: pointer;
          font-family: Arial, sans-serif;
          text-decoration: none;
        }

        .btn-imprimir:hover { background: #a93226; }

        .acciones {
          text-align: center;
          margin-bottom: 24px;
        }

        @media print {
          body { background: #fff; padding: 0; }
          .contenedor { box-shadow: none; padding: 0; }
          .acciones { display: none; }
        }
      </style>
    </head>
    <body>
      <div class="contenedor">
        <div class="cabecera">
          <h1><?php echo esc_html(get_bloginfo('name')); ?> — Conversación</h1>
          <div class="meta">
            <?php echo esc_html($fecha); ?><br>
            <small>ID: <?php echo esc_html(substr($chat_id, 0, 8)); ?>...</small>
          </div>
        </div>

        <div class="acciones">
          <button class="btn-imprimir" onclick="window.print()">
            🖨️ Guardar como PDF / Imprimir
          </button>
        </div>

        <?php foreach ($mensajes as $m) :
          $rol     = $m->role ?? 'user';
          $content = $m->content ?? '';
          if (empty(trim($content))) continue;
          $es_usuario   = in_array($rol, ['user', 'human']);
          $clase        = $es_usuario ? 'usuario' : 'asistente';
          $etiqueta     = $es_usuario ? 'Tú' : 'Asistente';
        ?>
        <div class="mensaje <?php echo $clase; ?>">
          <div class="rol"><?php echo esc_html($etiqueta); ?></div>
          <?php echo nl2br(esc_html($content)); ?>
        </div>
        <?php endforeach; ?>

        <div class="pie">
          Conversación exportada desde <?php echo esc_html(get_bloginfo('name')); ?> · <?php echo esc_html($fecha); ?>
        </div>
      </div>
    </body>
    </html>
    <?php
  }

  /* ================= BOTÓN EN EL CHATBOT ================= */

  public function inyectar_boton() {
    ?>
    <style>
      /* Ocultar el botón de descarga roto de AI Engine Pro */
      .mwai-download-button { display: none !important; }

      .dgc-btn-descargar {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 32px;
        height: 32px;
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 8px;
        cursor: pointer;
        color: rgba(255,255,255,0.85);
        opacity: 0.8;
        transition: all 0.2s;
        padding: 0;
        flex-shrink: 0;
      }
      .dgc-btn-descargar:hover {
        opacity: 1;
        background: rgba(255,255,255,0.2);
      }
      .dgc-btn-descargar svg { width: 16px; height: 16px; }
    </style>
    <script>
    (function() {
      console.log('[Digiliencia] Script de descarga cargado OK');

      function limpiarTexto(el) {
        var clon = el.cloneNode(true);
        // Convertir emojis de WordPress (img.emoji) a su caracter unicode
        clon.querySelectorAll('img.emoji').forEach(function(img) {
          var emoji = document.createTextNode(img.getAttribute('alt') || '');
          img.parentNode.replaceChild(emoji, img);
        });
        // Quitar SVGs e imágenes que no sean emoji (avatares, iconos)
        clon.querySelectorAll('svg, img').forEach(function(s) { s.remove(); });
        // Quitar elementos de UI del chat
        clon.querySelectorAll('.mwai-reply-actions, .mwai-copy-button, .mwai-download-button, .mwai-name, .mwai-avatar').forEach(function(e) { e.remove(); });
        return clon.innerHTML;
      }

      function descargarConversacion() {
        var convEl = document.querySelector('#dgcBot .mwai-conversation');
        if (!convEl) {
          alert('No hay conversación activa en pantalla.');
          return;
        }

        var mensajes = [];
        convEl.querySelectorAll('.mwai-reply').forEach(function(reply) {
          var esAI   = reply.classList.contains('mwai-ai');
          var textEl = reply.querySelector('.mwai-text');
          if (!textEl) return;
          mensajes.push({ rol: esAI ? 'ai' : 'user', html: limpiarTexto(textEl) });
        });

        if (mensajes.length === 0) {
          alert('La conversación está vacía.');
          return;
        }

        var fecha = new Date().toLocaleDateString('es-ES', {
          day: '2-digit', month: '2-digit', year: 'numeric',
          hour: '2-digit', minute: '2-digit'
        });

        var htmlMensajes = '';
        mensajes.forEach(function(m) {
          if (m.rol === 'user') {
            htmlMensajes +=
              '<div class="msg msg-user">' +
                '<span class="quien">T\u00fa</span>' +
                '<div class="texto">' + m.html + '</div>' +
              '</div>';
          } else {
            htmlMensajes +=
              '<div class="msg msg-ai">' +
                '<span class="quien">CyberSegurIA</span>' +
                '<div class="texto">' + m.html + '</div>' +
              '</div>';
          }
        });

        var estilos =
          '@page { size:A4; margin:2cm 2.5cm; }' +
          '* { box-sizing:border-box; margin:0; padding:0; }' +
          'body { font-family:Georgia,"Times New Roman",serif; font-size:13pt; color:#111; background:#fff; line-height:1.6; }' +
          'h1 { font-size:18pt; font-weight:bold; color:#c0392b; margin-bottom:4px; }' +
          '.meta { font-size:10pt; color:#888; margin-bottom:28px; border-bottom:1px solid #ddd; padding-bottom:14px; }' +
          '.msg { margin-bottom:22px; }' +
          '.quien { display:block; font-size:9pt; font-weight:bold; text-transform:uppercase; letter-spacing:.6px; color:#888; margin-bottom:5px; }' +
          '.msg-user .quien { color:#c0392b; }' +
          '.texto { line-height:1.75; }' +
          '.msg-user .texto { color:#333; font-style:italic; }' +
          'h3 { font-size:13pt; margin:14px 0 7px; }' +
          'ul,ol { padding-left:22px; margin:8px 0; }' +
          'li { margin-bottom:4px; }' +
          'strong { font-weight:bold; }' +
          'code { font-family:monospace; background:#f4f4f4; padding:1px 5px; border-radius:2px; font-size:11pt; }' +
          'a { color:#c0392b; }' +
          'table { border-collapse:collapse; width:100%; margin:12px 0; font-size:11pt; }' +
          'th,td { border:1px solid #ddd; padding:7px 11px; text-align:left; }' +
          'th { background:#f5f5f5; }' +
          '.pie { margin-top:36px; padding-top:14px; border-top:1px solid #eee; font-size:9pt; color:#aaa; }' +
          'svg { display:none !important; }' +
          'img { display:none !important; }';

        var contenido =
          '<h1>CyberSegurIA \u2014 Conversaci\u00f3n</h1>' +
          '<p class="meta">Digiliencia.org &nbsp;&middot;&nbsp; ' + fecha + '</p>' +
          htmlMensajes +
          '<div class="pie">Generado por CyberSegurIA &middot; digiliencia.org &middot; ' + fecha + '</div>';

        // Imprimir desde iframe oculto — sin abrir nueva pestaña
        var iframe = document.getElementById('dgc-print-frame');
        if (iframe) { iframe.parentNode.removeChild(iframe); }
        iframe = document.createElement('iframe');
        iframe.id = 'dgc-print-frame';
        iframe.style.cssText = 'position:fixed;width:0;height:0;border:0;left:-9999px;top:-9999px;';
        document.body.appendChild(iframe);

        var doc = iframe.contentDocument || iframe.contentWindow.document;
        doc.open();
        doc.write('<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>Conversaci\u00f3n \u2014 CyberSegurIA</title><style>' + estilos + '</style></head><body>' + contenido + '</body></html>');
        doc.close();

        setTimeout(function() {
          try {
            iframe.contentWindow.focus();
            iframe.contentWindow.print();
          } catch(e) {
            console.error('[Digiliencia] Error al imprimir:', e);
          }
        }, 300);
      }

      function inyectarBoton() {
        // Buscar el contenedor derecho del header del chat
        var headerRight = document.querySelector('.dgc-header-right');
        if (!headerRight) {
          console.log('[Digiliencia] .dgc-header-right no encontrado aún');
          return;
        }
        if (headerRight.querySelector('.dgc-btn-descargar')) return; // ya existe

        console.log('[Digiliencia] Inyectando botón en .dgc-header-right');

        var btn = document.createElement('button');
        btn.className = 'dgc-btn-descargar';
        btn.title = 'Descargar / Imprimir conversación';
        btn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>';
        btn.addEventListener('click', descargarConversacion);

        // Insertar antes del logo (último elemento) para que quede junto al status
        var logo = headerRight.querySelector('.dgc-logo-img');
        if (logo) {
          headerRight.insertBefore(btn, logo);
        } else {
          headerRight.appendChild(btn);
        }
      }

      // ── Parche botón copiar de AI Engine Pro ──────────────────────────
      // mwai solo enlaza el clic al último mensaje renderizado.
      // Con delegación de eventos capturamos el clic en cualquier botón
      // de copiar y obtenemos el texto del mensaje más cercano.
      document.addEventListener('click', function(e) {
        var btn = e.target.closest('.mwai-copy-button');
        if (!btn) return;

        // Buscar el .mwai-text del reply que contiene este botón
        var reply = btn.closest('.mwai-reply');
        if (!reply) return;
        var textEl = reply.querySelector('.mwai-text');
        if (!textEl) return;

        var texto = textEl.innerText || textEl.textContent || '';
        if (!texto.trim()) return;

        // Prevenir que mwai ejecute su propio handler roto
        e.stopImmediatePropagation();

        navigator.clipboard.writeText(texto.trim()).then(function() {
          // Feedback visual: cambiar el icono brevemente a un tick
          var svgOrig = btn.innerHTML;
          btn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>';
          setTimeout(function() { btn.innerHTML = svgOrig; }, 1500);
        }).catch(function() {
          // Fallback para navegadores sin clipboard API
          var ta = document.createElement('textarea');
          ta.value = texto.trim();
          ta.style.cssText = 'position:fixed;left:-9999px;top:-9999px;';
          document.body.appendChild(ta);
          ta.select();
          document.execCommand('copy');
          document.body.removeChild(ta);
        });
      }, true); // useCapture:true para interceptar antes que mwai

      function iniciar() {
        inyectarBoton();
        var obs = new MutationObserver(function() { inyectarBoton(); });
        obs.observe(document.body, { childList: true, subtree: true });
      }

      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', iniciar);
      } else {
        iniciar();
      }
    })();
    </script>
    <?php
  }
}

new Digiliencia_Descargar_Conversacion();
