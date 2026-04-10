# (e) Plantilla de Excel para cálculo de IGM y ROI

Se propone una hoja de cálculo con las siguientes pestañas:

## Hoja 1 – "Respuestas"

Columnas:
- A: ID de pregunta (ej. 2.1, 2.2, ...).
- B: Bloque (Gobernanza, Riesgos, etc.).
- C: Descripción breve.
- D: Respuesta seleccionada (texto).
- E: Puntuación asignada (0–100).

Cada fila corresponde a una pregunta respondida en el cuestionario.

## Hoja 2 – "Ponderaciones"

Columnas:
- A: Bloque.
- B: Peso (%) en el IGM.

Ejemplo de filas:
- Gobernanza (CC1) – 15.
- Riesgos y monitorización (CC3–CC4) – 20.
- Controles técnicos (CC5–CC8) – 30.
- TSC (disponibilidad, integridad, confidencialidad, privacidad) – 20.
- Proveedores e IA – 10.
- Percepción y recursos – 5.

## Hoja 3 – "Cálculos IGM"

Columnas:
- A: Bloque.
- B: Puntuación media del bloque (calculada a partir de la hoja "Respuestas").
- C: Peso (%) desde "Ponderaciones".
- D: Puntuación ponderada (B * C / 100).

En una celda adicional:
- IGM = SUMA de la columna D.

Ejemplo en Excel:
- Suponiendo que las filas 2 a 7 de la columna D contienen las puntuaciones ponderadas:
  - Celda D8: `=SUMA(D2:D7)`

## Hoja 4 – "ROI Ciberseguridad"

Columnas:
- A: Concepto.
- B: Valor antes de inversión.
- C: Valor después de inversión.
- D: Comentarios.

Filas recomendadas:
- Frecuencia anual esperada de incidentes significativos.
- Impacto económico medio por incidente.
- Pérdida anual esperada (Frecuencia x Impacto).
- Coste anual de la inversión en ciberseguridad.
- Pérdida anual esperada después de las inversiones.
- Beneficio anual esperado (Pérdida antes – Pérdida después).
- ROI (%) = (Beneficio – Coste) / Coste * 100.

Ejemplo de fórmula de ROI en Excel:
- Si:
  - Pérdida antes está en B5.
  - Pérdida después está en C5.
  - Coste anual está en B6.
- Entonces:
  - Beneficio (celda B7): `=B5-C5`
  - ROI % (celda B8): `=(B7-B6)/B6*100`

Esta plantilla permite que un analista traduzca los resultados cualitativos de madurez en decisiones de inversión cuantificadas y defendibles ante dirección.