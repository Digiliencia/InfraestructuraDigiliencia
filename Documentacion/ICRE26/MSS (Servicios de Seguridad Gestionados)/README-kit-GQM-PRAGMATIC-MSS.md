# 📁 README — KIT GQM + PRAGMATIC PARA INDICADORES MSS
## Cómo Adoptar un Sistema de Métricas con Objetivo, Pregunta y Conciencia
#### Versión 1.0 — Abril 2026

---

> *"Si el dashboard es un escaparate, este kit es el taller: aquí se diseñan, afinan y, cuando toca, se retiran las métricas que no dan la talla."*

---

## 1. ¿QUÉ ES ESTE KIT?

El **Kit GQM + PRAGMATIC para Indicadores MSS** es un conjunto de artefactos metodológicos diseñados para:

- Alinear métricas de Servicios de Seguridad Gestionados (MSS) con **objetivos estratégicos nacionales y organizativos** mediante el enfoque **Goal–Question–Metric (GQM)**[cite:129][cite:138][cite:141].  
- Evaluar la **calidad y utilidad real** de cada métrica usando el metamarco **PRAGMATIC Security Metrics** (Predictive, Relevant, Actionable, Genuine, Meaningful, Accurate, Timely, Independent, Cheap)[cite:130][cite:131][cite:136][cite:139].

Está pensado para organizaciones españolas (públicas y privadas) que operan bajo NIS2, ENS, DORA e ISO 27001 y que utilizan MSS/MDR/XDR, ya sea con proveedores externos o capacidades SOC internas.

---

## 2. CONTENIDO DEL KIT

| Archivo | Descripción | Uso principal |
|---------|-------------|---------------|
| `MSS-GQM-PRAGMATIC-marco.md` | Marco integrativo GQM + PRAGMATIC aplicado a indicadores MSS | Referencia conceptual para CISO, Riesgos y arquitectura |
| `MSS-PRAGMATIC-matriz-completa.md` | Matriz completa de evaluación PRAGMATIC para métricas clave (MTTD, MTTR, ACR, ROSI, etc.) | Selección y priorización de métricas |
| `MSS-GQM-PRAGMATIC-narrativa.md` | Narrativa explicativa para explicar el enfoque a stakeholders no técnicos | Comunicación interna / evangelización |
| `MSS-GQM-mapeo-normativo.md` | Mapeo detallado GQM (Goals/Questions/Metrics) ↔ Encuesta MSS ↔ NIS2/ENS/DORA | Compliance, auditoría, diseño de SLAs |
| `MSS-GQM-PRAGMATIC-plantilla-igm-roi.md` | Diseño de plantilla Excel para IGM-MSS y ROSI con pesos PRAGMATIC | Implementación en hoja de cálculo |
| `MSS-GQM-PRAGMATIC-reporte-ejecutivo-ppt.md` | Plantilla de reporte ejecutivo para explicar métricas GQM + PRAGMATIC al Consejo | Presentaciones a Alta Dirección |
| `README-kit-encuesta-mss.md` | README original del Kit de Encuesta MSS (opcionalmente complementario) | Contexto general MSS |

---

## 3. PARA QUIÉN ES ESTE KIT

### Perfiles objetivo

- **CISOs y responsables de seguridad:** que necesitan defender ante la dirección por qué ciertas métricas son imprescindibles y otras son ruido.  
- **Equipos de Riesgos / CRO / actuarios:** que quieren conectar métricas técnicas con modelos de ALE/ROSI.  
- **Responsables de Cumplimiento / Legal:** que requieren trazabilidad entre métricas y artículos específicos de NIS2/ENS/DORA.  
- **Arquitectos de seguridad y líderes de SOC/MSSP:** que deben diseñar y operar cuadros de mando útiles.  
- **Consultores y auditores:** que buscan un marco coherente, no solo una lista de KPIs.

### Cuándo utilizarlo

- Al diseñar o revisar el cuadro de mando de seguridad.  
- Al renegociar contratos con MSSPs (definición de SLAs e indicadores).  
- Antes de auditorías formales ENS, NIS2 o ISO 27001.  
- Al justificar inversiones en ciberseguridad ante CFO/Consejo (usando IGM + ROSI).  
- Al planificar la transición hacia métricas para amenazas emergentes (IA, PQC, OT/ICS).

---

## 4. FLUJO DE TRABAJO RECOMENDADO

### Paso 1 — Entender el marco (GQM + PRAGMATIC)

1. Leer `MSS-GQM-PRAGMATIC-marco.md` para comprender cómo se conectan objetivos, preguntas y métricas.  
2. Leer `MSS-GQM-PRAGMATIC-narrativa.md` para una versión más literaria útil para convencer a otros.

### Paso 2 — Seleccionar métricas candidatas

1. Partir del inventario de métricas MSS existente (lo que hoy aparece en el dashboard).  
2. Contrastar ese inventario con las métricas propuestas y evaluadas en `MSS-PRAGMATIC-matriz-completa.md`.  
3. Eliminar métricas que no cuelgan claramente de ningún Goal GQM relevante.  
4. Proponer métricas nuevas donde haya objetivos sin indicadores.

### Paso 3 — Ajustar GQM a la realidad de la organización

1. Usar `MSS-GQM-mapeo-normativo.md` para:
   - Conectar los objetivos estratégicos de la organización con Goals GQM.  
   - Ver qué preguntas GQM y métricas están ya reflejadas en la Encuesta MSS.  
   - Identificar lagunas regulatorias (objetivos normativos sin métricas asociadas).

### Paso 4 — Implementar la plantilla Excel

1. Implementar el diseño descrito en `MSS-GQM-PRAGMATIC-plantilla-igm-roi.md` en Excel / LibreOffice / Sheets.  
2. Volcar resultados de la Encuesta MSS en `H1_Respuestas_Encuesta`.  
3. Cargar el mapeo GQM desde `H2_GQM_Mapeo` y las puntuaciones PRAGMATIC desde `H3_Puntuaciones_PRAGMATIC`.  
4. Validar con un conjunto de datos piloto.

### Paso 5 — Preparar el reporte ejecutivo

1. Adaptar la estructura de `MSS-GQM-PRAGMATIC-reporte-ejecutivo-ppt.md` a la realidad de la organización.  
2. Reemplazar ejemplos por valores reales de IGM-MSS, MTTD, ACR, %MFA, ROSI, etc.  
3. Ensayar el relato para que cada gráfico responda explícitamente a:  
   - ¿Qué objetivo persigue?  
   - ¿Qué pregunta contesta?  
   - ¿Qué decisión permite?

---

## 5. RELACIÓN CON EL KIT DE ENCUESTA MSS ORIGINAL

Este kit está diseñado para funcionar de forma **complementaria** al **Kit de Encuesta MSS**:

- La Encuesta MSS recoge datos de madurez organizativa y percepciones.  
- El Kit GQM + PRAGMATIC articula y filtra las métricas que se derivan de esos datos.  
- Juntos, permiten calcular un IGM-MSS sólido y traducirlo a decisiones de negocio y cumplimiento.

En la práctica:

- Las columnas de GQM en la hoja `Respuestas_Encuesta` referencian el mapeo de `MSS-GQM-mapeo-normativo.md`.  
- La ponderación de métricas en el IGM-MSS se toma de `MSS-PRAGMATIC-matriz-completa.md`.  
- El reporte ejecutivo usa ambas cosas para construir una narrativa creíble.

---

## 6. REQUISITOS TÉCNICOS

- **Markdown:** cualquier editor/visor (VS Code, Obsidian, GitHub, etc.).  
- **Hoja de cálculo:** Excel 365/2019+, LibreOffice 7.x o Google Sheets.  
- **Presentaciones:** PowerPoint 365, Google Slides o equivalente compatible.

Para convertir los `.md` a PDF o DOCX se recomienda **Pandoc** o exportadores integrados en editores Markdown.

---

## 7. REFERENCIAS CLAVE

- Basili, V., Caldiera, G., Rombach, H. — *The Goal Question Metric Approach*[cite:129][cite:132][cite:138][cite:141].  
- Brotby, W., Hinson, G. — *PRAGMATIC Security Metrics: Applying Metametrics to Information Security*[cite:130][cite:131][cite:136][cite:142].  
- *Getting Started with Security Metrics* — Security Metametrics[cite:136].  
- "The Smart Approach to Selecting Good Cyber Security Metrics" (2024)[cite:139].  
- ENISA — *Threat Landscape*, *MSS Market Analysis* y *ECSMAF V3.0*.  
- INCIBE — *Balance de Ciberseguridad* (España).  
- Directiva NIS2, ENS RD 311/2022, DORA, ISO/IEC 27001:2022, NIST CSF 2.0.

---

## 8. ADVERTENCIA Y BUENAS PRÁCTICAS

- Este kit **no sustituye** auditorías formales ni asesoramiento legal.  
- La puntuación PRAGMATIC es contextual: debe revisarse al menos cada 12–18 meses.  
- Transparencia ante el Consejo: documentar supuestos, fuentes de datos y limitaciones.

Regla de oro: *"Métrica que no pueda explicarse en 30 segundos a un directivo no técnico y relacionarse con una decisión concreta, métrica candidata a jubilación anticipada."*

---

*README — Kit GQM + PRAGMATIC para Indicadores MSS · Versión 1.0 · Abril 2026*