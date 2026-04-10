# 📊 PLANTILLA EXCEL PARA IGM-MSS Y ROI BASADA EN GQM + PRAGMATIC
## Arquitectura de Hoja de Cálculo Integrada con Objetivos, Preguntas y Métricas
#### Versión 1.0 — Abril 2026

---

> *"Una hoja de cálculo bien diseñada es la novela realista de la organización: si se lee con atención, cuenta exactamente quién manda, qué se teme y qué se finge."*

---

## 1. PROPÓSITO DE LA PLANTILLA

Esta plantilla Excel extiende la anterior **Plantilla IGM-MSS y ROSI** incorporando explícitamente:

- El **marco GQM** (Goal–Question–Metric) para asegurar trazabilidad desde objetivos a métricas[cite:129][cite:138][cite:141].  
- La **puntuación PRAGMATIC** de cada métrica, para seleccionar y ponderar indicadores de acuerdo con su utilidad práctica[cite:130][cite:131][cite:136][cite:139].

**Archivo recomendado:** `MSS_GQM_PRAGMATIC_IGM_ROSI_v1.0.xlsx`  
**Número de hojas:** 10

---

## 2. LISTADO DE HOJAS

1. `H1_Respuestas_Encuesta`  
2. `H2_GQM_Mapeo`  
3. `H3_Puntuaciones_PRAGMATIC`  
4. `H4_IGM_Cálculo`  
5. `H5_ROSI_Cálculo`  
6. `H6_Benchmark_Sectorial`  
7. `H7_Dashboard`  
8. `H8_Plan_Mejora`  
9. `H9_Histórico`  
10. `H10_Parametrización`  

---

## 3. HOJA H1 — «Respuestas_Encuesta»

Estructura casi idéntica a la plantilla previa, con dos columnas nuevas para GQM:

| Col | Campo | Tipo |
|-----|-------|------|
| A | Pregunta_ID (P1.1, P3.2…) | Texto |
| B | Texto_Pregunta | Texto |
| C | Bloque (B0–B12) | Texto |
| D | Respuesta_Código (1–7) | Número |
| E | Respuesta_Texto | Texto (BUSCARV) |
| F | Puntuación (0–4) | Número (BUSCARV) |
| G | Pilar_IGM (P-I…P-V) | Texto |
| H | Peso_Pregunta (0–1) | % |
| I | Goal_GQM_ID (G-DR1, G-CV2…) | Texto (BUSCARV desde H2) |
| J | Question_GQM_ID (Q-DR1.1…) | Texto (BUSCARV desde H2) |
| K | Obligatoria (S/N) | Texto |
| L | Respondida (S/N) | Fórmula |

Ejemplo de fórmula en **L5**:

```excel
=SI(ESBLANCO(D5),"N","S")
```

---

## 4. HOJA H2 — «GQM_Mapeo»

Contiene el mapeo entre preguntas de la encuesta, objetivos y preguntas GQM, y métricas asociadas (resumen del documento `MSS-GQM-mapeo-normativo.md`).

| Col | Campo |
|-----|-------|
| A | Goal_GQM_ID (G-DR1, G-CV1…) |
| B | Goal_Descripción |
| C | Question_GQM_ID (Q-DR1.1…) |
| D | Question_Descripción |
| E | Metric_ID (M-DR1.1…) |
| F | Metric_Nombre (MTTD, MTTR, ACR, etc.) |
| G | Pregunta_ID_Encuesta (P3.2, P6.3…) |
| H | Artículo_NIS2_Clave |
| I | Artículo_ENS_Clave |
| J | Artículo_DORA_Clave |

**Uso en H1:**

- En `I5` (Goal_GQM_ID):

```excel
=BUSCARV(A5,H2_GQM_Mapeo!G:J,1,FALSO)
```

- En `J5` (Question_GQM_ID):

```excel
=BUSCARV(A5,H2_GQM_Mapeo!G:J,2,FALSO)
```

---

## 5. HOJA H3 — «Puntuaciones_PRAGMATIC»

Alberga la puntuación PRAGMATIC de cada métrica técnica relevante.

| Col | Campo |
|-----|-------|
| A | Metric_ID (M-DR1.1, M-CV2.1…) |
| B | Metric_Nombre (MTTD, ACR, ROSI…) |
| C | P_Predictive (0–10) |
| D | R_Relevant (0–10) |
| E | A_Actionable (0–10) |
| F | G_Genuine (0–10) |
| G | M_Meaningful (0–10) |
| H | A_Accurate (0–10) |
| I | T_Timely (0–10) |
| J | I_Independent (0–10) |
| K | C_Cheap (0–10) |
| L | PRAGMATIC_Total |
| M | PRAGMATIC_Media |
| N | PRAGMATIC_Peso (0–1) |

**Fórmulas clave:**

```excel
// Total y media
L2 = SUMA(C2:K2)
M2 = PROMEDIO(C2:K2)

// Peso basado en total (normalización respecto de la métrica máxima)
N2 = L2 / MAX($L$2:$L$20)
```

**Ejemplos de valores:** (tomados de `MSS-PRAGMATIC-matriz-completa.md`)

- MTTD → L ≈ 76, M ≈ 8,4  
- ACR → L ≈ 70, M ≈ 7,8  
- ROSI → L ≈ 69, M ≈ 7,7

---

## 6. HOJA H4 — «IGM_Cálculo» (con peso PRAGMATIC)

La lógica del IGM-MSS se refuerza con un peso adicional derivado de la puntuación PRAGMATIC de cada métrica.

### 6.1. Cálculo del score de cada métrica

Se crea una tabla intermedia por métrica:

| Métrica | Metric_ID | Pilar | Valor_Normalizado | Peso_PRAGMATIC | Score_Métrica |
|---------|-----------|-------|-------------------|----------------|--------------|
| MTTD | M-DR1.1 | P-II | 0–1 | N (H3) | Valor × Peso |
| MTTR | M-DR3.1 | P-II/P-IV | … | … | … |
| ACR | M-CV1.1 | P-II/P-V | … | … | … |

**Ejemplo de normalización (columna Valor_Normalizado):**

```excel
// Suponiendo que "mejor" es menor (p.ej. MTTD, MTTR)
Valor_Normalizado = 1 - (Valor_Actual / Umbral_Máximo_Aceptable)

// Suponiendo que "mejor" es mayor (p.ej. % MFA, ACR)
Valor_Normalizado = Valor_Actual / Umbral_Óptimo
```

Los umbrales se definen en `H10_Parametrización`.

**Score_Métrica:**

```excel
Score_Metrica = MAX(0,MIN(1,Valor_Normalizado)) * Peso_PRAGMATIC
```

### 6.2. Cálculo por pilar


a) Sumar los `Score_Métrica` de todas las métricas asociadas a cada pilar.  

```excel
Score_Pilar_I = SUMAR.SI(Tabla_Métricas[Pilar],"P-I",Tabla_Métricas[Score_Métrica])
...
```

b) Normalizar cada pilar a escala 0–100 y aplicar peso de pilar:

```excel
Pilar_I_Pct = Score_Pilar_I / MAX_Pilar_I * 100
Pilar_I_Ponderado = Pilar_I_Pct * Peso_Pilar_I

// Pesos de pilar (recomendados):
Peso_Pilar_I = 0,20
Peso_Pilar_II = 0,25
Peso_Pilar_III = 0,20
Peso_Pilar_IV = 0,15
Peso_Pilar_V = 0,20
```

### 6.3. IGM-MSS Total

```excel
IGM_MSS = Pilar_I_Ponderado + Pilar_II_Ponderado + Pilar_III_Ponderado + Pilar_IV_Ponderado + Pilar_V_Ponderado
```

---

## 7. HOJA H5 — «ROSI_Cálculo» (idéntica a la plantilla previa, con enlace a PRAGMATIC)

La lógica actuarial se mantiene (AV, EF, ARO, ALE, ROSI) pero se añade una columna de **Calidad de Métrica** basada en PRAGMATIC para documentar la confianza en los resultados.

| Variable | Símbolo | Métrica base | PRAGMATIC_Total | Confianza (Alta/Media/Baja) |
|----------|---------|--------------|-----------------|----------------------------|
| ALE_sin_controles | — | ALE (M-FIN1.1) | L (H3) | Derivada de PRAGMATIC de inputs |
| ALE_con_controles | — | ALE (M-FIN1.2) | L (H3) | … |
| ROSI | — | M-FIN1.3 | 69 | Alta |

**Regla sugerida:** Si la media PRAGMATIC de las métricas que alimentan el modelo es <7, el informe de ROSI debe marcarse con un asterisco de cautela metodológica.

---

## 8. HOJAS H6–H9 (Benchmark, Dashboard, Plan, Histórico)

Se heredan de la plantilla previa con los siguientes ajustes:

- **Dashboard:** incluir visual de PRAGMATIC_Total por métrica (barras), para mostrar qué métricas son estructuralmente mejores.  
- **Plan de Mejora:** introducir un factor `Impacto_Métrica` derivado de PRAGMATIC: métricas con alta puntuación en P y R tienen mayor peso en la priorización.  
- **Histórico:** registrar no solo la evolución del IGM-MSS, sino también cambios en supuestos/umbral de normalización (para transparencia).

---

## 9. HOJA H10 — «Parametrización»

Contiene:

- Umbrales de normalización por métrica (p.ej. MTTD_Óptimo, MTTD_Aceptable, MTTD_Inaceptable).  
- Pesos de pilares y métricas.  
- Tabla de traducción de IGM-MSS a niveles (1–5) con descripciones textuales.

Ejemplo de tabla de umbrales:

| Métrica | Mejor_Cuanto | Óptimo | Aceptable | Inaceptable |
|---------|--------------|--------|-----------|-------------|
| MTTD (min) | Menor | ≤15 | ≤60 | >60 |
| MTTR (h) | Menor | ≤24 | ≤72 | >72 |
| ACR (%) | Mayor | ≥95 | ≥80 | <80 |
| % MFA | Mayor | ≥95 | ≥80 | <80 |

---

## 10. RECOMENDACIONES DE IMPLEMENTACIÓN

1. **Crear primero H2 y H3:** sin el mapeo GQM ni la matriz PRAGMATIC, el IGM-MSS sería un índice huérfano de teoría.  
2. **Separar claramente datos observados de supuestos:** por ejemplo, registrar los valores de ARO y EF en celdas de color distinto.  
3. **Documentar en comentarios de celda el origen de cada conjunto de datos:** encuestas internas, logs, informes MSS, estimaciones expertas.  
4. **Versionar la plantilla:** registrar cambios en pesos de pilares o umbrales.  
5. **Validar fórmulas con un piloto:** aplicar la plantilla a un caso real y revisar resultados con CISO, Riesgos y Financias.

---

*Plantilla Excel GQM + PRAGMATIC para IGM-MSS y ROSI — Versión 1.0 · Abril 2026*  
*Basada en: GQM (Basili & Weiss)[cite:129][cite:138][cite:141], PRAGMATIC Security Metrics[cite:130][cite:131][cite:136][cite:142], CAS Cyber Risk Papers, ENISA MSS 2025, ECSMAF V3.0.*
