# CyberSegurIA — Aportación Universidad de Salamanca

Esta carpeta contiene la aportación de la **Fundación General de la Universidad de Salamanca** al proyecto Marco Digiliencia, dentro del repositorio InfrastructuraDigiliencia.

🌐 **Web:** [digiliencia.org](https://digiliencia.org)

---

## Descripción

CyberSegurIA es el asistente inteligente de ciberseguridad desarrollado sobre WordPress e integrado con la API SCAYLE de la Universidad de León. Permite a cualquier ciudadano consultar dudas sobre ciberseguridad de forma gratuita y sin necesidad de registro, a través de digiliencia.org.

---

## Estructura de esta carpeta

```
CyberSegurIA-USAL/
│
├── web/
│   ├── bloque-chat.html                          ← Bloque HTML del chatbot (insertar en WordPress)
│   └── digiliencia-chat.css                      ← Estilos de la interfaz
│
├── plugins/
│   ├── ai-engine-digiliencia-adapter.php         ← Plugin adaptador WordPress–API SCAYLE
│   └── digiliencia-descargar-conversacion.php    ← Plugin de descarga de conversaciones en PDF
│
└── documentacion/
    ├── guia-usuario-cyberseguria.docx            ← Guía de uso para el usuario final
    ├── memoria-general-cyberseguria.docx         ← Memoria técnica del proyecto
    └── documento-informativo-cyberseguria.docx   ← Documento informativo institucional
```

---

## Cómo funciona

1. El usuario accede a digiliencia.org y escribe una pregunta en el chat.
2. AI Engine Pro captura el mensaje y lo pasa al plugin adaptador.
3. El plugin se autentica en la API SCAYLE con un usuario de servicio y reenvía el mensaje.
4. La API procesa la consulta con el modelo LLM y devuelve la respuesta.
5. La respuesta se muestra al usuario en el chat.

---

## Tecnologías

- **WordPress** + plugin AI Engine Pro
- **PHP** — plugins personalizados para la integración
- **API REST SCAYLE** — sistema de IA de la Universidad de León
- **Ollama** + modelos LLM locales (qwen3:32b en producción)
- **JavaScript / CSS / HTML** — interfaz del chatbot

---

## Equipo

- José Francisco Adserias Vistué
- Javier Barrientos Montes
- Manuel Blanco Cuadrado
- Yuliana Vanessa Morales Trejos
- Luis Antonio Peña Deobarro

**Fundación General de la Universidad de Salamanca**

---

## Contacto

Para más información sobre el proyecto: [digiliencia.org](https://digiliencia.org)
