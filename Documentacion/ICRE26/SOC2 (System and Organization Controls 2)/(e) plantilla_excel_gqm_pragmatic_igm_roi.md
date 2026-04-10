# (e) Plantilla de Excel GQM + PRAGMATIC + IGM/ROI (estructura)

Se propone una hoja de cálculo ampliada con pestañas para capturar la cadena GQM y la evaluación PRAGMATIC, e integrarlas con el cálculo de IGM y ROI.

## Hoja 1 – "Métricas_GQM"

Columnas:
- A: ID de métrica (M1.1, M2.1, ...).
- B: Objetivo (G1, G2...).
- C: Pregunta asociada.
- D: Descripción de la métrica.
- E: Unidad de medida.
- F: Fuente de datos.
- G: Frecuencia de medición.

## Hoja 2 – "Datos_Métricas"

Columnas:
- A: ID de métrica.
- B: Periodo (mes, trimestre, año).
- C: Valor medido.
- D: Meta u objetivo.
- E: Desviación (C–D).
- F: Comentarios.

## Hoja 3 – "PRAGMATIC"

Columnas:
- A: ID de métrica.
- B: P – Predictivo (0–3).
- C: R – Relevante (0–3).
- D: A – Accionable (0–3).
- E: G – Genuino (0–3).
- F: M – Significativo (0–3).
- G: P – Preciso (0–3).
- H: T – Oportuno (0–3).
- I: I – Independiente (0–3).
- J: C – Rentable (0–3).
- K: Total PRAGMATIC (suma B:J).

Ejemplo de fórmula para K2:
- `=SUMA(B2:J2)`

## Hoja 4 – "IGM_Bloques"

Columnas:
- A: Bloque (Gobernanza, Riesgos, Controles técnicos, etc.).
- B: Puntuación media del bloque (derivada de las métricas seleccionadas para el bloque).
- C: Peso (%) del bloque en el IGM.
- D: Puntuación ponderada (B * C / 100).

En una celda adicional:
- IGM = SUMA de la columna D.

Ejemplo:
- Si D2:D7 contienen puntuaciones ponderadas, en D8:
  - `=SUMA(D2:D7)`

## Hoja 5 – "ROI_Ciberseguridad"

Columnas:
- A: Concepto.
- B: Valor antes de inversión.
- C: Valor después de inversión.
- D: Comentarios.

Filas recomendadas:
- Frecuencia anual esperada de incidentes significativos.
- Impacto económico medio por incidente.
- Pérdida anual esperada antes (Frecuencia x Impacto).
- Pérdida anual esperada después (con controles mejorados).
- Coste anual de la inversión en ciberseguridad.
- Beneficio anual esperado (Pérdida antes – Pérdida después).
- ROI (%) = (Beneficio – Coste) / Coste * 100.

Ejemplo de fórmulas:
- Si Pérdida antes está en B3 y Pérdida después en C3, Coste en B4:
  - Beneficio (B5): `=B3-C3`
  - ROI % (B6): `=(B5-B4)/B4*100`

La lógica recomendada es usar para el cálculo del IGM y, cuando aplique, para el ROI, sólo métricas que superen un umbral mínimo PRAGMATIC (por ejemplo, ≥ 18/27), reforzando así la calidad del cuadro de mando.