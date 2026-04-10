# 📘 README — KIT DE ENCUESTA LINDDUN/LIINE4DU 2025–2026
## Guía de Inicio Rápido y Descripción del Kit Completo
### Versión 1.0 · Abril 2026 · Español

---

> *"Todo gran viaje comienza con un README. Y toda gran política de privacidad, con una pregunta honesta sobre la situación de partida."*

---

## 🎯 ¿QUÉ ES ESTE KIT?

El **Kit de Encuesta LINDDUN/LIINE4DU 2025–2026** es un instrumento de diagnóstico de madurez en privacidad y protección de datos personales diseñado específicamente para organizaciones que operan bajo el marco regulatorio español y europeo.

Está basado en el marco **LINDDUN** (*Linking, Identifying, Non-repudiation, Detecting, Data Disclosure, Unawareness, Non-compliance*) desarrollado por KU Leuven/DistriNet, y en su adaptación española **LIINE4DU 1.0** publicada por la Agencia Española de Protección de Datos en octubre de 2024.

El kit permite a cualquier organización —independientemente de su tamaño o sector— realizar un diagnóstico estructurado de su nivel de madurez en privacidad, identificar brechas regulatorias, priorizar inversiones y comunicar los resultados a la Alta Dirección de forma rigurosa y persuasiva.

---

## 📦 CONTENIDO DEL KIT

El kit está compuesto por **7 documentos** en formato Markdown (`.md`), diseñados para trabajar de forma complementaria:

---

### 📋 (a) `encuesta-LINDDUN.md`
**Modelo de Encuesta Integral**

El documento principal del kit. Contiene:
- 42 ítems puntuables organizados en 10 módulos temáticos
- Módulo 0 de perfil organizacional (6 ítems contextuales)
- Sección de preguntas abiertas y valoración final
- Escala de respuesta descriptiva A–E con tono irónico-constructivo
- Cobertura de todos los indicadores LINDDUN + LIINE4DU:
  - M1: Linking (Vinculación)
  - M2: Identifying (Identificabilidad)
  - M3: Non-repudiation (No Repudio)
  - M4: Detecting (Detección)
  - M5: Data Disclosure (Divulgación de Datos)
  - M6: Unawareness (Desconocimiento)
  - M7: Non-compliance (Incumplimiento)
  - M8: Inaccuracy + Exclusion (LIINE4DU)
  - M9: Gobernanza
  - M10: Tecnología e IA

**Uso recomendado**: Aplicar en sesión colaborativa multidisciplinar (DPO + CISO + Legal + Negocio). Tiempo estimado: 45–90 minutos.

---

### 📐 (b) `guia-metodologica-LINDDUN.md`
**Guía Metodológica Detallada**

El manual del facilitador. Contiene:
- Fundamentos teóricos: LINDDUN, LIINE4DU y el modelo de madurez de 5 niveles
- Diseño de la encuesta: estructura modular, tipos de ítem y sistema de ponderación
- **Fórmula completa del IGM** (Índice de Madurez Global) con pesos por módulo
- Protocolo de administración: antes, durante y después de la sesión
- Requisitos del facilitador y modalidades de aplicación (4 opciones)
- Análisis e interpretación: cuantitativo, cualitativo, patrones de respuesta
- Niveles mínimos de IGM recomendados por sector
- Limitaciones metodológicas y notas de validez
- Marco normativo de referencia completo

**Uso recomendado**: Leer íntegramente antes de aplicar la encuesta. Especialmente importante para facilitadores externos.

---

### 📖 (c) `narrativa-LINDDUN.md`
**Narrativa Explicativa**

El "por qué" del kit, en formato de ensayo. Contiene:
- Contextualización del estado de la privacidad en España en 2026
- Análisis del caso AENA como paradigma del cumplimiento de papel
- LINDDUN como lenguaje común organizacional
- Justificación metodológica: por qué una encuesta y no una auditoría
- Reflexión sobre el tono irónico-constructivo de la encuesta
- El contexto post-AI Act y sus implicaciones prácticas
- Epílogo filosófico sobre la privacidad como opción ética

**Uso recomendado**: Distribuir como material introductorio a los participantes antes de la sesión de encuesta. También útil para presentar el proyecto a la Alta Dirección.

---

### 🗺️ (d) `mapeo-normativo-LINDDUN.md`
**Mapeo Detallado de Requisitos Normativos**

La "biblia jurídica" del kit. Contiene:
- Tabla completa de todas las preguntas (P0.1 a P10.4)
- Por cada pregunta: artículo RGPD, AI Act, NIS2, ENS, LIINE4DU y norma ISO aplicables
- Indicación del nivel de riesgo regulatorio si la respuesta es A o B
- Tabla resumen de ítems con sanción máxima aplicable (en €)
- Referencia a casos reales (AENA, TikTok) como ilustración del riesgo

**Uso recomendado**: Para el DPO/Legal al revisar resultados de la encuesta. También útil como checklist de cumplimiento regulatorio y para la preparación de EIPDs.

---

### 📊 (e) `plantilla-IGM-ROI-LINDDUN.md`
**Especificación de la Plantilla Excel IGM + ROI**

El manual de implementación de la calculadora. Contiene:
- Estructura de 8 hojas del libro Excel (CONFIG, RESPUESTAS, IGM_CALCULO, RADAR_CHART, ROI_PRIVACIDAD, BENCHMARKING, PLAN_MEJORA, NOTAS_AUDITORIA)
- Especificación completa de cada hoja: columnas, fórmulas, formatos condicionales
- Fórmulas Excel listas para copiar e implementar (SUMAPRODUCTO, SI, COINCIDIR, etc.)
- Calculadora de ROI: CNC (Coste de No Cumplimiento) vs. IC (Inversión en Cumplimiento)
- Generador automático de Plan de Mejora basado en respuestas
- Instrucciones de implementación en Excel, Google Sheets y LibreOffice Calc

**Uso recomendado**: El área de Sistemas/TI implementa la plantilla siguiendo la especificación. El DPO la completa con las respuestas de la encuesta. El reporte se genera automáticamente.

---

### 📑 (f) `reporte-ejecutivo-PPT-LINDDUN.md`
**Especificación del Reporte Ejecutivo en PowerPoint**

El manual de presentación para la Alta Dirección. Contiene:
- Especificaciones completas de diseño: paleta de colores HEX, tipografía, formato 16:9
- 18 diapositivas + 4 de apéndice, con contenido y diseño especificados
- Diapositivas clave: Portada, Resumen Ejecutivo, Radar Chart, Fortalezas y Áreas Críticas, Análisis por indicador LINDDUN, ROI Iceberg, Plan de Acción Priorizado, Benchmarking Sectorial
- Instrucciones de vinculación con el libro Excel (datos en tiempo real)
- Instrucciones de exportación a PDF para distribución

**Uso recomendado**: Presentar al Comité de Dirección o Consejo de Administración en los 15 días siguientes al diagnóstico. Actualizar trimestralmente con el seguimiento del Plan de Mejora.

---

### 📘 (g) `README-LINDDUN.md`
**Este documento**

La guía de inicio rápido del kit completo. Contiene la descripción de todos los archivos, el flujo de trabajo recomendado, los requisitos de aplicación y las referencias bibliográficas.

---

## 🔄 FLUJO DE TRABAJO RECOMENDADO

```
FASE 0 — PREPARACIÓN (1–2 semanas antes)
   ├─ Leer narrativa-LINDDUN.md (todo el equipo participante)
   ├─ Leer guia-metodologica-LINDDUN.md (facilitador + DPO)
   ├─ Designar facilitador y participantes (DPO, CISO, CTO, Legal, Negocio)
   ├─ Implementar plantilla-IGM-ROI-LINDDUN.md en Excel/Sheets
   └─ Recopilar evidencias documentales (Registro de Actividades, EIPDs, etc.)

FASE 1 — APLICACIÓN (sesión de 45–90 minutos)
   ├─ Completar encuesta-LINDDUN.md en sesión colaborativa
   ├─ Registrar evidencias en Hoja 8 (NOTAS_AUDITORIA) del Excel
   └─ Documentar desacuerdos entre participantes (son señales de mejora)

FASE 2 — ANÁLISIS (1–3 días tras la sesión)
   ├─ Introducir respuestas en Hoja 2 (RESPUESTAS) del Excel
   ├─ Revisar cálculo automático del IGM (Hoja 3)
   ├─ Contrastar con mapeo-normativo-LINDDUN.md los ítems A/B
   └─ Revisar Plan de Mejora generado automáticamente (Hoja 7)

FASE 3 — COMUNICACIÓN (1 semana tras el análisis)
   ├─ Elaborar presentación siguiendo reporte-ejecutivo-PPT-LINDDUN.md
   ├─ Presentar al Comité de Dirección o equivalente
   ├─ Obtener aprobación del Plan de Mejora con presupuesto asignado
   └─ Programar seguimiento trimestral y próximo diagnóstico anual

FASE 4 — IMPLEMENTACIÓN Y SEGUIMIENTO (12 meses)
   ├─ Ejecutar acciones del Plan de Mejora por prioridad
   ├─ Actualizar estado en Hoja 7 (PLAN_MEJORA) del Excel
   ├─ Reportar avance trimestral al Comité de Dirección
   └─ Repetir el diagnóstico completo al año siguiente
```

---

## 👥 PERFILES DE USUARIO

| Perfil | Documentos principales | Uso |
|--------|------------------------|-----|
| **DPO / Delegado de Protección de Datos** | Todos | Coordinación completa del diagnóstico |
| **CISO** | (a)(b)(d)(e) | Análisis de módulos técnicos (M1–M5, M10) |
| **CTO / Director de Sistemas** | (a)(b)(e)(f) | Módulos M10, M5; implementación Excel |
| **Director/a Legal / Compliance** | (a)(b)(d) | Análisis normativo; mapeo de riesgos regulatorios |
| **Alta Dirección / Consejo** | (c)(f) | Narrativa + Presentación ejecutiva |
| **Consultor/a externo/a** | Todos | Facilitación de la sesión + análisis de resultados |
| **Responsable de área de negocio** | (a)(c) | Participación en la encuesta + comprensión del contexto |

---

## ⚙️ REQUISITOS TÉCNICOS

### Para aplicar la encuesta:
- Editor Markdown (VS Code, Typora, Obsidian, Notion) o cualquier editor de texto
- Alternativamente: convertir el `.md` a Word/PDF con Pandoc o a formulario online con Typeform/Microsoft Forms

### Para la plantilla Excel:
- Microsoft Excel 365 o 2021 (recomendado para funciones dinámicas)
- Microsoft Excel 2019 (compatible con adaptaciones menores)
- Google Sheets (compatible, con limitaciones en gráfico radar)
- LibreOffice Calc 7.x (compatible con adaptaciones en fórmulas de formato condicional)

### Para el reporte ejecutivo:
- Microsoft PowerPoint 365 o 2021 (recomendado)
- LibreOffice Impress 7.x (compatible)
- Google Slides (compatible con adaptaciones de diseño)

### Conversión de Markdown a otros formatos:
```bash
# Convertir a Word (requiere Pandoc instalado)
pandoc encuesta-LINDDUN.md -o encuesta-LINDDUN.docx

# Convertir a PDF
pandoc encuesta-LINDDUN.md -o encuesta-LINDDUN.pdf --pdf-engine=wkhtmltopdf

# Convertir a HTML
pandoc encuesta-LINDDUN.md -o encuesta-LINDDUN.html
```

---

## 📚 MARCO NORMATIVO Y REFERENCIAS

### Normativa aplicable:
- **RGPD**: Reglamento (UE) 2016/679, arts. 5, 7, 13–22, 24–25, 28, 30, 32–35, 37–39, 44–49
- **LOPDGDD**: Ley Orgánica 3/2018, arts. 7, 12–18, 22, 34, 37–41, 87–91
- **AI Act**: Reglamento (UE) 2024/1689, prohibiciones vigentes desde feb. 2025
- **NIS2**: Directiva (UE) 2022/2555, transpuesta en España por Ley 11/2022
- **ENS**: Real Decreto 311/2022

### Marcos técnicos de referencia:
- **LINDDUN** (KU Leuven/DistriNet): linddun.org
- **LIINE4DU 1.0** (AEPD, octubre 2024): aepd.es
- **NIST Privacy Framework 1.0** (2020) / NIST CSF 2.0 (2024)
- **ISO/IEC 27001:2022** + ISO/IEC 27701:2019 + ISO/IEC 42001:2023
- **EDPB Report: AI Privacy Risks & Mitigations – LLMs** (abril 2025)

### Publicaciones académicas clave (2025):
- Langthaler et al., "Evaluating the Efficacy of LINDDUN GO for Privacy Threat Modeling for Local Renewable Energy Communities", ICISSP 2025
- KU Leuven DistriNet, "LINDDUN MAESTRO", Software & Systems Modeling, nov. 2025
- ENISA Threat Landscape 2025

---

## 🆓 LICENCIA Y REUTILIZACIÓN

Este kit se distribuye bajo **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

Puede utilizarse, adaptarse y distribuirse libremente con la siguiente atribución:

> *Kit de Encuesta LINDDUN/LIINE4DU 2025–2026. Basado en el marco LINDDUN de KU Leuven/DistriNet y LIINE4DU 1.0 de la AEPD. Versión 1.0, Abril 2026.*

Para adaptaciones sectoriales (sanidad, educación, sector financiero, sector público), se recomienda consultar las guías sectoriales de la AEPD y ajustar los pesos de los módulos IGM según el perfil de riesgo específico.

---

## 📞 SOPORTE Y ACTUALIZACIÓN

Este kit se revisará anualmente para incorporar:
- Nuevas obligaciones del AI Act según el calendario de implementación (2025–2027)
- Actualizaciones de LINDDUN Maestro y las herramientas de KU Leuven
- Nuevas guías y resoluciones de la AEPD
- Jurisprudencia sancionadora relevante del año anterior
- Datos actualizados de benchmarking sectorial

Para reportar errores, proponer mejoras o solicitar adaptaciones sectoriales:
- Contactar con el DPO de su organización para coordinar la adaptación
- Consultar la documentación actualizada en linddun.org y aepd.es

---

## ⚡ INICIO RÁPIDO (TL;DR)

¿Tiene 5 minutos? Siga estos 4 pasos:

1. **Lea** `narrativa-LINDDUN.md` para entender el propósito del kit.
2. **Convoque** a su DPO, CISO y director legal para una sesión de 90 minutos.
3. **Complete** `encuesta-LINDDUN.md` en la sesión, marcando la opción más honesta.
4. **Implemente** `plantilla-IGM-ROI-LINDDUN.md` en Excel y calcule su IGM.

En 90 minutos sabrá exactamente dónde está su organización en materia de privacidad. Y, lo que es más importante, sabrá adónde tiene que ir.

---

*"La privacidad no es un destino: es una dirección de viaje. Este kit es la brújula."*

---

**Kit de Encuesta LINDDUN/LIINE4DU 2025–2026**  
Versión 1.0 — Abril 2026  
Basado en LINDDUN © KU Leuven/DistriNet | LIINE4DU 1.0 © AEPD  
Distribuido bajo CC BY 4.0
