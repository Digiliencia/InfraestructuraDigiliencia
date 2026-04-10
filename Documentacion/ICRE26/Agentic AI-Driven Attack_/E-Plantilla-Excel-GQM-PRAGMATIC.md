# Plantilla de Excel para GQM + PRAGMATIC aplicado a Agentic IA

## 1. Hoja “GQM-Metricas”

Columnas sugeridas:

- A: Métrica (UAR, PAR, PED, etc.).  
- B: Objetivo GQM (resumen).  
- C: Preguntas clave (lista breve).  
- D: Definición de la métrica (fórmula).  
- E: Unidad.  
- F: Fuente de datos.  
- G: Frecuencia de cálculo.  
- H: Responsable.  

## 2. Hoja “PRAGMATIC-Score”

Columnas:

- A: Métrica.  
- B: P Predictiva (1–5).  
- C: R Relevante (1–5).  
- D: A Accionable (1–5).  
- E: G Genuina (1–5).  
- F: M Significativa (1–5).  
- G: P Precisa (1–5).  
- H: T Oportuna (1–5).  
- I: I Independiente (1–5).  
- J: C Rentable (1–5).  
- K: Score total.  
- L: Comentario.

### 2.1. Fórmula para Score PRAGMATIC

Si las puntuaciones están en B2:J2, en K2 puede utilizarse:

- `=PROMEDIO(B2:J2)`

Para ponderaciones distintas por criterio, sustituir por una suma ponderada.

## 3. Hoja “IGM-Agentic”

Objetivo: derivar un **IGM especializado en métricas Agentic IA**, opcionalmente integrado con el IGM global de ciberseguridad.

Columnas sugeridas:

- A: Métrica.  
- B: Peso en el IGM Agentic (0–1).  
- C: Nivel de implantación (0–4) – similar a madurez: inexistente, ad hoc, definido, gestionado, optimizado.  
- D: Score PRAGMATIC (referencia a “PRAGMATIC-Score”).  
- E: Índice combinado métrica (por ejemplo, C * D).  

### 3.1. Fórmulas de ejemplo

- Índice combinado por métrica (fila 2):  
  - `=C2 * D2`  
- IGM Agentic global (en una celda, por ejemplo E20):  
  - `=SUMAPRODUCTO(B2:B11;E2:E11) / SUMA(B2:B11)`

## 4. Hoja “ROI-Agentic”

Permite centrar el ROI en mejoras atribuibles a métricas Agentic (UAR, TTC, etc.).

Columnas:

- A: Métrica / efecto (UAR, TTC, etc.).  
- B: Situación “antes” (valor medio).  
- C: Situación “después”.  
- D: Mejora (Δ).  
- E: Traducción económica (€, si aplica).  

Ejemplo:

- Reducción de UAR → disminución esperada de incidentes graves.  
- Reducción de TTC → menos tiempo de indisponibilidad.  

Cálculo simplificado de ROI anual:

- Celda E20 (suma de beneficios): `=SUMA(E2:E10)`  
- Celda E21 (coste anual de iniciativas Agentic IA): valor introducido.  
- Celda E22 (ROI €): `=E20 - E21`  
- Celda E23 (ROI %): `=SI(E21>0;(E20-E21)/E21;"")`

## 5. Hoja “Dashboard-Agentic”

Incluir:

- Gráfico de barras con Score PRAGMATIC por métrica.  
- IGM Agentic global.  
- Evolución temporal de 2–3 métricas clave (por ejemplo, UAR, TTC, False Positive Reduction Rate).
