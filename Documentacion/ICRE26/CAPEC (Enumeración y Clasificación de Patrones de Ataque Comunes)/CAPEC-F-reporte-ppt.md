# 📽️ PLANTILLA DE REPORTE EJECUTIVO EN POWERPOINT
## Estructura, Contenido y Diseño de las 18+6 Diapositivas
### Kit de Encuesta CAPEC-ESP · Documento F · Versión 1.0 · Abril 2026

---

> *«Una diapositiva es el espacio donde la complejidad técnica negocia su rendición ante la atención directiva. Que la rendición sea digna.»*

---

## ESPECIFICACIONES GENERALES

| Parámetro | Valor |
|---|---|
| **Formato de archivo** | CAPEC-ESP-Reporte-Ejecutivo-v1.0.pptx |
| **Dimensiones** | 16:9 (33,87 cm × 19,05 cm) |
| **Total de diapositivas** | 18 principales + 6 de respaldo (backup) |
| **Audiencias objetivo** | Consejo de Administración / Comité de Dirección / Regulador / Técnico |
| **Tiempo de presentación** | 25–30 min (formato completo) / 12–15 min (formato abreviado) |

---

## PALETA DE COLORES INSTITUCIONAL

| Uso | Color | HEX | RGB |
|---|---|---|---|
| Fondo principal | Blanco institucional | #FFFFFF | 255, 255, 255 |
| Color primario (cabeceras, énfasis) | Azul CAPEC | #003366 | 0, 51, 102 |
| Color secundario (gráficas, accents) | Azul INCIBE | #0055A4 | 0, 85, 164 |
| Alerta crítica | Rojo ciberseguridad | #CC0000 | 204, 0, 0 |
| Advertencia | Naranja gestión de riesgos | #FF6600 | 255, 102, 0 |
| Positivo / OK | Verde madurez | #008000 | 0, 128, 0 |
| Neutro / datos | Gris institucional | #666666 | 102, 102, 102 |
| Fondo secciones | Azul muy claro | #E8F0F8 | 232, 240, 248 |

## TIPOGRAFÍA

| Elemento | Fuente | Tamaño | Peso |
|---|---|---|---|
| Título de diapositiva | Calibri | 32 pt | Bold |
| Subtítulo | Calibri | 22 pt | Regular |
| Texto de cuerpo | Calibri | 18 pt | Regular |
| Notas para el ponente | Calibri | 12 pt | Regular |
| Etiquetas de gráficas | Calibri | 14 pt | Regular |
| Leyendas de figura | Calibri | 11 pt | Italic |

---

## ESTRUCTURA COMPLETA DE DIAPOSITIVAS

---

### DIAPOSITIVA 01 — PORTADA

**Layout:** Fondo azul CAPEC con overlay geométrico
**Contenido:**
- Logo de la organización (posición superior derecha)
- Título principal: "**Estado de Madurez CAPEC en [Nombre Organización]**"
- Subtítulo: "Índice Global de Madurez CAPEC-ESP · Informe Ejecutivo 2026"
- Número de IGM-CAPEC resaltado en grande: **[X.XX / 5.00]** con barra de color
- Nivel de madurez: **"NIVEL [N] — [ETIQUETA]"**
- Fecha: Abril 2026
- "CONFIDENCIAL" en marca de agua

**Nota para ponente:** *Comenzar con el número. El IGM-CAPEC es el headline. Si la audiencia retiene un solo dato de esta presentación, que sea ese.*

---

### DIAPOSITIVA 02 — AGENDA

**Layout:** Lista con iconos sectoriales
**Contenido:**
1. Contexto regulatorio y de amenazas (2 min)
2. Metodología y alcance del estudio (2 min)
3. Resultados: IGM-CAPEC y sub-índices (8 min)
4. Análisis por dominio de ataque (5 min)
5. Amenazas emergentes: brechas detectadas (5 min)
6. Posición comparativa sectorial (3 min)
7. Plan de acción priorizado (5 min)
8. Preguntas y discusión

---

### DIAPOSITIVA 03 — CONTEXTO: EL PANORAMA DE AMENAZAS 2025

**Layout:** Split 50/50 con datos y titular
**Lado izquierdo (datos):**
- 122.223 incidentes en España (2025, INCIBE, +26%)
- 4.ª posición en objetivos gubernamentales europeos (ENISA)
- +1.265% en phishing generado con IA (2024)
- ×2 incidentes de cadena de suministro de software (2025)

**Lado derecho (visual):**
- Mapa de Europa con intensidad de amenaza por país
- Leyenda: "España — Alta exposición"

**Mensaje clave (destacado):** *"El adversario ha acelerado. La pregunta es: ¿hemos acelerado nosotros al mismo ritmo?"*

**Nota para ponente:** *Calibrar la reacción de la audiencia. Si no conocían estas cifras, el resto de la presentación encontrará terreno abonado. Si ya las conocen, esta diapositiva valida el nivel de la audiencia y permite avanzar rápido.*

---

### DIAPOSITIVA 04 — CONTEXTO: EL ECOSISTEMA REGULATORIO

**Layout:** Diagrama de timeline con hitos regulatorios
**Contenido:**
- Timeline: NIS2 vigente → Transposición española LCyGC → ENS RD 311/2022 → DORA en vigor (Ene 2025) → CNC anunciado (Oct 2025)
- Cuadro de obligaciones: Art. 21.2 NIS2 en forma de checklist visual
- Cuadro de sanciones: NIS2 (hasta 2% facturación global) vs. DORA (variable)

**Mensaje clave:** *"El regulador ha pasado de murmurar a gritar. Y CAPEC es la taxonomía que da contenido técnico a cada uno de los requisitos que NIS2 exige."*

---

### DIAPOSITIVA 05 — QUÉ ES CAPEC Y POR QUÉ LO MEDIMOS

**Layout:** Definición + comparativa visual ATT&CK vs. CAPEC
**Contenido:**
- Definición en una línea: *"El catálogo de los patrones que los adversarios repiten. No los atacantes concretos, sino sus métodos recurrentes."*
- Tabla de 2×2:
  | | Quién ataca | Cómo ataca |
  |---|---|---|
  | Ataque pasado | Threat Intel / OSINT | **ATT&CK** |
  | Ataque futuro | No predecible | **CAPEC** |
- CAPEC v3.9: 559 patrones, 9 mecanismos, 6 dominios

---

### DIAPOSITIVA 06 — METODOLOGÍA DEL ESTUDIO

**Layout:** Infografía de proceso en 4 fases
**Contenido:**
- Fase 1: Instrumento — 50 preguntas, 11 secciones, validación GQM + panel expertos
- Fase 2: Muestra — n=400 organizaciones, estratificado por sector y tamaño
- Fase 3: Análisis — AFC, Alpha Cronbach, regresión múltiple, clustering
- Fase 4: Output — IGM-CAPEC, benchmarks sectoriales, recomendaciones de política

---

### DIAPOSITIVA 07 — EL IGM-CAPEC: ARQUITECTURA DEL ÍNDICE

**Layout:** Diagrama circular con los 5 sub-índices y pesos
**Contenido:**
- Diagrama: IGM-CAPEC en el centro
- 5 segmentos con sus pesos:
  - IGC: 25% — Gestión del Conocimiento
  - ICM: 20% — Cobertura de Métricas
  - IAR: 20% — Alineación Regulatoria
  - IRD: 20% — Resiliencia Digital
  - IBE: 15% — Brecha Emergente
- Fórmula visible: `IGM = 0,25·IGC + 0,20·ICM + 0,20·IAR + 0,20·IRD + 0,15·IBE`

---

### DIAPOSITIVA 08 — RESULTADOS: IGM-CAPEC GLOBAL [ORGANIZACIÓN]

**Layout:** Dashboard de una sola métrica, impacto visual máximo
**Contenido:**
- Gauge/dial central con el valor IGM-CAPEC: **[0.XX]**
- Escala de colores del dial: rojo (0–0.40) → naranja (0.40–0.60) → verde (0.60–1.00)
- Indicador de posición: "Nivel [N] de 5: [ETIQUETA]"
- Comparativa:
  - vs. Media del sector: **[diferencia +/-]**
  - vs. Benchmark europeo: **[referencia ENISA/sectorial]**
  - vs. Objetivo 12 meses: **[gap a cubrir]**

**Nota:** *Esta diapositiva debe verse desde 5 metros de distancia. Si el número no se lee, la diapositiva ha fallado.*

---

### DIAPOSITIVA 09 — RESULTADOS: LOS 5 SUB-ÍNDICES

**Layout:** Gráfico de radar (spider) con overlay de benchmark
**Contenido:**
- Gráfico de araña con 5 ejes (IGC, ICM, IAR, IRD, IBE)
- Línea azul oscuro: resultado de la organización
- Línea gris punteada: media sectorial
- Línea verde punteada: líderes sectoriales (percentil 75)
- Tabla de apoyo debajo:

| Sub-índice | Score | vs. Sector | Estado |
|---|---|---|---|
| IGC | [X.XX] | [+/-X] | 🟢/🟡/🔴 |
| ICM | [X.XX] | [+/-X] | 🟢/🟡/🔴 |
| IAR | [X.XX] | [+/-X] | 🟢/🟡/🔴 |
| IRD | [X.XX] | [+/-X] | 🟢/🟡/🔴 |
| IBE | [X.XX] | [+/-X] | 🟢/🟡/🔴 |

---

### DIAPOSITIVA 10 — MADUREZ POR DOMINIO CAPEC

**Layout:** Barras horizontales con semáforo
**Contenido:**
- 7 barras horizontales (una por dominio CAPEC) con valores de 0 a 5
- Línea vertical en x=3.0 (umbral mínimo NIS2/ENS recomendado)
- Colores por barra: rojo (<2.0), naranja (2.0–3.0), amarillo (3.0–4.0), verde (>4.0)
- Etiqueta en cada barra: nombre del dominio + score + patrones CAPEC más relevantes

**Dominios mostrados:**
1. Software — score: [X.X]
2. Hardware — score: [X.X]
3. Comunicaciones — score: [X.X]
4. Cadena de Suministro — score: [X.X]
5. Ingeniería Social — score: [X.X]
6. Seguridad Física — score: [X.X]
7. ICS/OT — score: [X.X]

---

### DIAPOSITIVA 11 — AMENAZAS EMERGENTES: IA ADVERSARIAL

**Layout:** Tabla de impacto con iconografía de IA
**Contenido:**
- Tabla de los 6 tipos de ataque adversarial evaluados (NIST AI 100-2e2025):
  - Evasion, Poisoning, Extraction, Backdoor, Prompt Injection, Shadow AI Exfiltration
- Para cada uno: score actual de control (1–4) + gap vs. recomendación
- Destacado en rojo: "Prompt Injection: sin control formal en [X]% de organizaciones"
- Cita NIST AI 100-2e2025 en el pie de la diapositiva

---

### DIAPOSITIVA 12 — AMENAZAS EMERGENTES: CADENA DE SUMINISTRO

**Layout:** Diagrama de la cadena con vectores de ataque señalados
**Contenido:**
- Diagrama: Desarrollo → Build → Repositorios → Distribución → Producción
- Marcas de vulnerabilidad en cada eslabón con el CAPEC-ID correspondiente
- Porcentaje de organizaciones sin SBOM: [X%] (dato del estudio)
- Porcentaje con incidente confirmado de supply chain (últimos 24 meses): [X%]

---

### DIAPOSITIVA 13 — AMENAZAS EMERGENTES: AMENAZA CUÁNTICA

**Layout:** Timeline de la amenaza + estado de preparación
**Contenido:**
- Timeline: Hoy → CRQC esperado 2030–2035 → Retrodesciframiento de tráfico capturado hoy
- Estado de preparación de la organización: escala 1–5 (posicionar)
- NIST PQC: ML-KEM, ML-DSA, SLH-DSA (publicados 2024)
- Dato impacto: "67% de organizaciones ya han sufrido compromisos HNDL detectados"
- Recomendación inmediata: iniciar inventario criptográfico

---

### DIAPOSITIVA 14 — POSICIÓN COMPARATIVA SECTORIAL

**Layout:** Beeswarm o dot plot con la posición de la organización
**Contenido:**
- Distribución de IGM-CAPEC de todas las organizaciones del sector (puntos)
- Posición de la organización destacada en azul oscuro
- Percentil de la organización: **Percentil [XX]** — "Está por encima/debajo del [XX]% del sector"
- Top 5 brechas diferenciales respecto a líderes sectoriales (percentil 75)

---

### DIAPOSITIVA 15 — ANÁLISIS DE CUMPLIMIENTO REGULATORIO

**Layout:** Tabla de estado por marco normativo
**Contenido:**

| Marco | Artículos clave evaluados | Estado | Gaps identificados | Sanción máxima |
|---|---|---|---|---|
| NIS2 | Art. 21.2 (a–j) | 🟡 Parcial | [X] de 10 sub-requisitos | 2% facturación global |
| ENS | Medidas Nivel [ENS] | 🟡 En desarrollo | [X] controles pendientes | Inhabilitación servicios |
| DORA | Art. 5, 8, 9, 11, 26, 28 | 🔴 Crítico | [X] requisitos sin cubrir | Variable |
| RGPD | Art. 25, 32, 35 | 🟢 Adecuado | Menor | 4% facturación global |

---

### DIAPOSITIVA 16 — ROSI: EL ARGUMENTO FINANCIERO

**Layout:** Tres KPI grandes + gráfica de comparación

**KPI 1:** Inversión anual en ciberseguridad
- Valor: **[XXX.XXX] EUR**

**KPI 2:** ROSI calculado
- Valor: **[XXX]%**
- Subtítulo: "Por cada euro invertido, se evitan [X.X] euros de pérdida esperada"

**KPI 3:** Sanciones regulatorias potenciales evitadas
- Valor: **[X.X M] EUR**

**Gráfica:** Barras comparando ALE sin controles vs. ALE con controles actuales vs. ALE con controles objetivo

---

### DIAPOSITIVA 17 — PLAN DE ACCIÓN PRIORIZADO

**Layout:** Tabla de acción 90 días / 6 meses / 12 meses

| Prioridad | Brecha | Acción | Responsable | Plazo | Coste est. |
|---|---|---|---|---|---|
| 🔴 CRÍTICA | [Dominio con menor IGM] | [Acción específica] | CISO | 30 días | [EUR] |
| 🔴 CRÍTICA | Sin SBOM / Supply Chain | Implementar SCA | DevSecOps | 60 días | [EUR] |
| 🟡 ALTA | Sin política IA generativa | Redactar y aprobar política | CISO + Jurídico | 30 días | [EUR] |
| 🟡 ALTA | Sin inventario criptográfico | Iniciar auditoría PQC | Arquitectura | 90 días | [EUR] |
| 🟢 MEDIA | Formación técnica CAPEC | Programa de formación | RRHH + CISO | 6 meses | [EUR] |

---

### DIAPOSITIVA 18 — CONCLUSIONES Y PRÓXIMOS PASOS

**Layout:** 3 recuadros de mensaje clave
**Contenido:**

**Recuadro 1 — Dónde estamos:**
- IGM-CAPEC: [X.XX] — Nivel [N]
- Posición sectorial: Percentil [XX]
- Mayor brecha: Dominio [X] (score: [X.X])

**Recuadro 2 — El riesgo de no actuar:**
- Exposición regulatoria estimada: [X.X M] EUR en sanciones potenciales
- Coste de incidente del sector vs. coste de control: ratio [X:1]

**Recuadro 3 — La decisión necesaria:**
- Aprobación del presupuesto adicional: [X EUR] para acciones críticas
- Nombramiento del responsable del programa de mejora CAPEC
- Fecha de revisión: [próximo trimestre]

---

## DIAPOSITIVAS DE RESPALDO (BACKUP) — PARA PREGUNTAS EN PROFUNDIDAD

### BACKUP 01 — Taxonomía completa CAPEC v3.9
Los 9 mecanismos de ataque y los 559 patrones organizados por dominio y nivel de abstracción.

### BACKUP 02 — Metodología GQM detallada
Diagrama Goal–Question–Metric completo con los 5 sub-índices y sus ítems de encuesta correspondientes.

### BACKUP 03 — Detalle del cálculo IGM-CAPEC
Fórmulas, pesos y criterios de codificación de cada subíndice para auditores y técnicos que quieran verificar el modelo.

### BACKUP 04 — Mapeo normativo completo
Tabla de mapeo pregunta ↔ requisito normativo (extracto del Documento D del kit).

### BACKUP 05 — Análisis detallado de brechas en IA adversarial
Detalle de los 6 tipos de ataque adversarial con referencias NIST AI 100-2e2025 y recomendaciones de mitigación por tipo.

### BACKUP 06 — Glosario de términos CAPEC
Definición de los términos clave del catálogo CAPEC: Likelihood_Of_Attack, Typical_Severity, Susceptibility Indicators, Execution Flow, Abstraction Levels.

---

## ADAPTACIONES POR AUDIENCIA

### Versión Consejo de Administración (12 slides)
Eliminar: 06 (metodología), 11-13 (detalles técnicos emergentes)
Mantener: 03, 04, 08, 09, 10 (resumida), 14, 16, 17, 18
Énfasis: ROSI, sanciones, posición sectorial, decisión de inversión

### Versión Regulador / Auditor (15 slides)
Incluir: todas las diapositivas técnicas
Añadir: backup 03 y 04 como parte del flujo principal
Énfasis: cumplimiento normativo, gaps identificados, plan de remediación con fechas

### Versión Equipo Técnico / CISO (18 slides + todos los backup)
Presentación completa con todos los backups
Énfasis: métricas técnicas, patrones CAPEC específicos, plan de acción con detalles de implementación

---

*Kit de Encuesta CAPEC-ESP · Documento F: Plantilla PowerPoint Ejecutivo · Versión 1.0 · Abril 2026*
