# 🎯 PLANTILLA DE REPORTE EJECUTIVO GQM + PRAGMATIC
## Cómo Explicar al Consejo que las Métricas No Son Caprichos del CISO
#### Versión 1.0 — Abril 2026

---

> *"El objetivo no es mostrar muchas métricas, sino pocas métricas que expliquen muchas cosas."*

---

## 1. PROPÓSITO DE LA PLANTILLA

Esta plantilla de presentación (PowerPoint / Slides) traduce el marco GQM + PRAGMATIC a una narrativa ejecutiva comprensible para Alta Dirección y Consejo:

- Explica **qué objetivos** se persiguen (Goal).  
- Muestra **qué preguntas** se formulan para comprobar si se cumplen (Question).  
- Enseña **qué métricas** se han seleccionado y por qué son especialmente buenas (Metric + PRAGMATIC).  
- Conecta todo ello con decisiones de inversión, riesgos regulatorios y retorno económico.

**Formato recomendado:** PowerPoint 365 / Google Slides  
**Número de diapositivas nucleares:** 14 + apéndices técnicos

---

## 2. ESTRUCTURA PROPUESTA DE LA PRESENTACIÓN

### Slide 1 — Portada

**Título:** `Marco de Métricas MSS basado en GQM + PRAGMATIC`  
**Subtítulo:** `De los objetivos nacionales a los logs del SOC`  
**Elementos:** Logo, nombre del ponente, fecha, clasificación (Confidencial)

---

### Slide 2 — Por qué Estamos Hablando de Métricas

**Objetivo:** Dar contexto sin abrumar.

Elementos clave:

- Crecimiento de incidentes (datos INCIBE/ENISA)
- Entrada en vigor de NIS2/DORA/ENS
- Inversión creciente en ciberseguridad

**Mensaje central:** *"Si vamos a invertir más, debemos medir mejor."*

---

### Slide 3 — De los Objetivos a las Métricas: GQM en una Mirada

**Visual:** Diagrama simple en tres niveles:

```
OBJETIVO (GOAL) → PREGUNTAS (QUESTION) → MÉTRICAS (METRIC)

Ejemplo:
Goal: Reducir impacto de incidentes críticos.
Question: ¿En cuánto tiempo los detectamos y los contenemos?
Metric: MTTD, MTTC, MTTR.
```

**Nota de orador:** Explicar que ninguna métrica existe "porque sí": todas cuelgan de un objetivo explícito.

---

### Slide 4 — Cómo Elegimos las Métricas: PRAGMATIC

**Visual:** Tabla sencilla con las 9 letras y breve definición.

| Letra | Criterio | Pregunta clave |
|-------|----------|----------------|
| P | Predictive | ¿Nos dice algo útil sobre el futuro a tiempo de actuar? |
| R | Relevant | ¿Le importa esta métrica a quien decide? |
| A | Actionable | ¿Sugiere qué hacer, no solo qué ha pasado? |
| G | Genuine | ¿Se basa en datos reales, no cosméticos? |
| M | Meaningful | ¿Se entiende sin intérprete simultáneo? |
| A | Accurate | ¿Es lo bastante exacta para la decisión? |
| T | Timely | ¿Llega a tiempo para influir? |
| I | Independent | ¿No está sesgada por incentivos extraños? |
| C | Cheap | ¿Cuesta menos de lo que vale? |

**Mensaje:** *"No todo lo que podemos medir merece ser medido."*[cite:130][cite:131][cite:136][cite:142]

---

### Slide 5 — Cadena Completa: Objetivo Nacional → Organización → MSS → Métrica

**Visual:** Cadena tipo GQM+Strategies[cite:129][cite:138].

```
OBJETIVO NACIONAL
  "Reducir el impacto de incidentes graves en infraestructuras esenciales"
        ↓
OBJETIVO ORGANIZACIÓN
  "Reducir incidentes críticos un 30% en 3 años"
        ↓
OBJETIVO MSS
  "MTTD < 1h y MTTR < 24h en incidentes críticos"
        ↓
PREGUNTAS
  "¿Cuál es nuestro MTTD actual? ¿Cumplimos RTO?"
        ↓
MÉTRICAS
  MTTD, MTTR, % incidentes dentro de RTO
```

**Mensaje:** Cada gráfico del dashboard debe poder recorrerse hacia arriba por esta cadena.

---

### Slide 6 — Nuestro Catálogo de Métricas MSS Seleccionadas

**Visual:** Tabla resumen con 8–10 métricas clave y su PRAGMATIC total.

| Métrica | Objetivo GQM | PRAGMATIC /90 | Nivel prioridad |
|---------|--------------|---------------|-----------------|
| MTTD | G-DR1 | 76 | Muy Alta |
| MTTR | G-DR3 | 72 | Muy Alta |
| ACR | G-CV1 | 70 | Muy Alta |
| % MFA | G-GOV1 | 74 | Muy Alta |
| Tiempo remediación CVEs críticas | G-CV2 | 72 | Muy Alta |
| ROSI MSS | G-FIN1 | 69 | Muy Alta |
| Compliance ENS/NIS2 | G-GOV2/G-GOV3 | 67 | Alta |

**Nota:** Mencionar que las puntuaciones PRAGMATIC vienen del trabajo técnico en `MSS-PRAGMATIC-matriz-completa.md`.

---

### Slide 7 — "Radar" PRAGMATIC de una Métrica Emblemática (MTTD)

**Visual:** Gráfico radar 9-ejes (uno por criterio PRAGMATIC) para MTTD.

- Mostrar claramente que MTTD puntúa muy alto en P, R, A, M, T y C.

**Mensaje:** *"Aquí vemos por qué MTTD es una métrica estrella: predice, importa, mueve acciones y cuesta poco medirla."*

---

### Slide 8 — Ejemplo 1: Cómo MTTD Afecta a NIS2 y al Negocio

**Visual:** Línea de tiempo con NIS2 Art. 23 (24h/72h) y nuestro MTTD actual.

Texto sugerido:

- "MTTD actual: 4h → margen razonable para notificar en 24h"  
- "Objetivo: MTTD 1h → margen holgado y menor daño operativo"  

**Mensaje:** A menor MTTD, menor probabilidad de sanciones y menor impacto de incidentes.

---

### Slide 9 — Ejemplo 2: % MFA vs. Riesgo de Compromiso de Cuentas

**Visual:** Barras comparando % MFA actual vs. objetivo, con referencia a NIS2.

- "Hoy: 62% de cuentas con MFA"  
- "Objetivo 12 meses: 95%"  
- "Obligación explícita en NIS2 Art. 21.2 j)."

**Mensaje:** *"Esta métrica no es estética técnica: es la diferencia entre cumplimiento e incumplimiento regulatorio."*

---

### Slide 10 — Ejemplo 3: ROSI de MSS — Métrica económica

**Visual:** Gráfico de barras ALE_sin_controles vs. ALE_con_controles, con ROSI.

- "Pérdidas anuales esperadas sin MSS: X M€"  
- "Pérdidas anuales esperadas con MSS: Y M€"  
- "ROSI: Z%"  

**Mensaje:** *"Esta métrica responde a la pregunta favorita del CFO: '¿Qué retorno tiene todo esto?'"*

---

### Slide 11 — Cómo se Construye el IGM-MSS

**Visual:** Diagrama en capas:

```
CAPA 1: Métricas individuales (MTTD, ACR, MFA, CVEs, etc.)
CAPA 2: Puntuación PRAGMATIC (peso de cada métrica)
CAPA 3: Pilares (Gobernanza, Detección, Cumplimiento, Resiliencia, Tecnología)
CAPA 4: Índice IGM-MSS (0–100)
```

**Mensaje:** El índice no es una media arbitraria, sino una agregación ponderada por calidad de métrica.

---

### Slide 12 — Resultados Actuales y Brechas Prioritarias

**Visual:**

- Gauge con IGM-MSS actual.  
- Gráfico de barras con pilares y comparación con benchmark.  
- Lista Top 5 brechas con relación explícita a métricas (ej. MTTD demasiado alto, % MFA bajo, ACR insuficiente, etc.).

---

### Slide 13 — Hoja de Ruta: Mejorar Métricas es Mejorar la Organización

**Visual:** Roadmap 12–24 meses.

Para cada línea de acción:

- Métrica objetivo (ej. MTTD, % MFA, tiempo remediación CVEs).
- Valor actual → valor objetivo.  
- Acciones para cerrar brecha.  
- Relación con normativa (NIS2/ENS/DORA).

---

### Slide 14 — Decisiones que Solicitamos Hoy

Estructurada en 3 bloques:

1. **Inversión** (basada en ROSI y ALE).  
2. **Cambios contractuales MSS** (incorporar métricas al SLA).  
3. **Cambios organizativos** (formación, procesos, recursos).

Cada decisión se ancla explícitamente en una métrica GQM + PRAGMATIC.

---

## 3. APÉNDICES PARA AUDIENCIAS TÉCNICAS

- **Apéndice A:** Tabla completa GQM (Goals–Questions–Metrics) por dominio (Gobernanza, Detección, Cumplimiento, etc.).  
- **Apéndice B:** Matriz PRAGMATIC completa para todas las métricas candidatas.  
- **Apéndice C:** Mapeo GQM–Normativa (NIS2, ENS, DORA).  
- **Apéndice D:** Detalle de la plantilla Excel (estructuras de hojas y fórmulas clave).  

---

## 4. RECOMENDACIONES DE DISEÑO GRÁFICO

- **Colores:** reaprovechar paleta del kit MSS previo (azules, verdes para fortalezas, ámbar/rojos para brechas).  
- **Tipografía:** Inter / Calibri, títulos ≥28 pt, cuerpo 16–18 pt, cifras clave 40–50 pt.  
- **Regla de oro:** máximo 3 ideas por slide, máximo 1 gráfico complejo.

---

*Plantilla de Reporte Ejecutivo GQM + PRAGMATIC — Versión 1.0 · Abril 2026*