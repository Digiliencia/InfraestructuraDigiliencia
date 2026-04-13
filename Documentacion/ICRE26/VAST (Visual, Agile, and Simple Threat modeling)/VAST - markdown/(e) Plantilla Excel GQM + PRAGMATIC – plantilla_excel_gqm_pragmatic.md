# Plantilla de Excel para GQM + PRAGMATIC, IGM y ROI

Esta plantilla extiende la hoja de cálculo anterior (IGM y ROI) para incorporar:

- Relación explícita de cada métrica con sus objetivos GQM.
- Puntuación PRAGMATIC por métrica.

## 1. Hojas recomendadas

1. `Respuestas` – Datos brutos de la encuesta.
2. `Puntuaciones` – Puntos por pregunta y bloque (como en el IGM anterior).
3. `GQM_Metricas` – Catálogo de métricas GQM.
4. `PRAGMATIC` – Puntuaciones PRAGMATIC por métrica.
5. `IGM` – Cálculo de índice global de madurez.
6. `ROI` – Cálculo de retorno de inversión.
7. `Parametros` – Pesos, correspondencias, referencias.

## 2. Hoja `GQM_Metricas`

Columnas sugeridas:

- `Codigo_Metrica` (ej.: G1.M1)
- `Objetivo_G` (ej.: G1)
- `Pregunta_Q` (ej.: G1.Q1)
- `Descripcion`
- `Definicion_Formal`
- `Unidad`
- `Fuente_Datos`
- `Periodicidad`

Cada fila describe una métrica según el marco GQM.

## 3. Hoja `PRAGMATIC`

Columnas sugeridas:

- `Codigo_Metrica`
- `P_Predictiva`
- `R_Relevante`
- `A_Accionable`
- `G_Genuina`
- `M_Significativa`
- `P2_Precisa`
- `O_Oportuna`
- `I_Independiente`
- `C_Rentable`
- `PRAGMATIC_Score`

Fórmula para `PRAGMATIC_Score`:

```excel
= PROMEDIO(P_Predictiva; R_Relevante; A_Accionable; G_Genuina; M_Significativa; P2_Precisa; O_Oportuna; I_Independiente; C_Rentable)
```

Opcionalmente, se puede añadir:

- `Peso_PRAGMATIC` para ponderar la importancia relativa de la métrica en el IGM.

## 4. Integración con `IGM`

En la hoja `IGM`:

- Para cada bloque (GOV, INV, THR, etc.) se puede crear una versión ponderada por la calidad PRAGMATIC de las métricas subyacentes.

Ejemplo conceptual:

- `THR_Score = SUMA(Metrica_THR_i * Peso_PRAGMATIC_i)`

De este modo, las métricas mejor evaluadas (más robustas) influyen más en el índice.

## 5. Relación con ROI

Se pueden utilizar algunas métricas GQM como variables explicativas en el análisis de ROI, por ejemplo:

- Ver si mejoras en G2.M3 (tiempo de remediación) se correlacionan con reducción de pérdidas por incidentes.
- Estudiar si la adopción de modelado de amenazas (G1.M1–M3) se asocia a menor frecuencia de incidentes críticos.

Este análisis se haría mediante gráficos y análisis estadísticos adicionales, fuera del alcance de la plantilla básica pero facilitados por la estructura clara de datos.