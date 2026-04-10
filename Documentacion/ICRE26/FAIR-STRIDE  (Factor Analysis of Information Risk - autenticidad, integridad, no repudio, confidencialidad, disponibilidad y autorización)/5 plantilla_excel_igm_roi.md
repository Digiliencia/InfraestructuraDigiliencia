# Plantilla de Excel para cálculo de IGM y ROI

## 1. Estructura general del libro

Se propone un libro de Excel con, al menos, las siguientes hojas:

- `Respuestas`: captura detallada de las respuestas a la encuesta.
- `Ponderaciones`: tabla de asignación de valores numéricos y pesos por pregunta.
- `IGM`: cálculo del Índice Global de Madurez y subíndices.
- `ROI`: modelo de cálculo de retorno de la inversión en iniciativas FAIR‑STRIDE.
- `Gráficos`: representaciones visuales para el reporte ejecutivo.

## 2. Hoja «Respuestas»

Columnas sugeridas:

- `Org_ID`: identificador de la organización o unidad.
- `Fecha`: fecha de cumplimentación de la encuesta.
- `Pregunta`: código de la pregunta (ej. 3.1, 5.4.2, etc.).
- `Respuesta`: código de la respuesta elegida (ej. A, B, C, D).
- `Valor`: valor numérico asociado a la respuesta (se completará mediante búsqueda).

Cada fila representa la respuesta de una organización a una pregunta concreta. Para múltiples organizaciones, se agregan filas; para comparaciones temporales, se diferencian por fecha.

## 3. Hoja «Ponderaciones»

Columnas sugeridas:

- `Pregunta`: código de la pregunta.
- `Respuesta`: código de la respuesta (A, B, C, etc., mapeadas a las opciones reales).
- `Valor`: puntuación base (por ejemplo, de 0 a 4).
- `Dominio`: categoría de madurez (FAIR, STRIDE, Autenticidad, Integridad, etc.).
- `Peso`: peso relativo de la pregunta en el cálculo del subíndice del dominio.

Ejemplo de escala de valores:

- Opción que refleja máxima madurez: `Valor = 4`.
- Opción alta madurez: `Valor = 3`.
- Opción intermedia: `Valor = 2`.
- Opción baja: `Valor = 1`.
- Opción que describe ausencia de práctica: `Valor = 0`.

## 4. Hoja «IGM»

En esta hoja se calculan:

- Subíndices por dominio: `IGM_Dominio = (Σ Valor * Peso) / (Σ Peso)` para todas las preguntas asociadas a cada dominio.
- Índice Global de Madurez (IGM): media ponderada de los subíndices por dominio.

Ejemplo de fórmula (en pseudocódigo de Excel):

- Supongamos que en `Respuestas!A:E` están las columnas mencionadas y en `Ponderaciones!A:E` las ponderaciones.
- Usar `BUSCARV` o `ÍNDICE`/`COINCIDIR` para trasladar `Valor` y `Peso` a la hoja `Respuestas`.
- En `IGM`, para un dominio concreto:
  - `IGM_Autenticidad = SUMIFS(Respuestas!Valor*Respuestas!Peso, Respuestas!Dominio, "Autenticidad") / SUMIFS(Respuestas!Peso, Respuestas!Dominio, "Autenticidad")` (adaptando la fórmula a Excel con columnas auxiliares).

El IGM global puede ser la media ponderada de los subíndices, con pesos por dominio si se desea enfatizar unos sobre otros.

## 5. Hoja «ROI»

El objetivo de esta hoja es conectar cambios en el IGM con estimaciones de reducción de pérdida anual esperada, usando principios FAIR.

Columnas sugeridas para una tabla de iniciativas:

- `Iniciativa_ID`: identificador de la iniciativa (ej. «ZT‑Segmentación‑Red»).
- `Dominio_Principal`: dominio FAIR‑STRIDE al que se dirige (ej. Disponibilidad, Autorización).
- `Coste_Inicial`: inversión inicial estimada.
- `Coste_Anual`: costes de operación y mantenimiento.
- `Pérdida_Actual`: pérdida anual esperada antes de la iniciativa (media o percentil elegido).
- `Pérdida_Prevista`: pérdida anual esperada después de la iniciativa.
- `Reducción_Pérdida`: `=Pérdida_Actual - Pérdida_Prevista`.
- `Horizonte_Anios`: horizonte temporal analizado (por ejemplo, 3 años).
- `Beneficio_Total`: `=Reducción_Pérdida * Horizonte_Anios`.
- `Coste_Total`: `=Coste_Inicial + Coste_Anual * Horizonte_Anios`.
- `ROI_%`: `=(Beneficio_Total - Coste_Total) / Coste_Total`.
- `Payback_Anios`: `=Coste_Total / Reducción_Pérdida` (si Reducción_Pérdida > 0).

La plantilla puede incluir, además, escenarios de sensibilidad usando diferentes percentiles de pérdida (p. ej., 50, 90, 95) y gráficos que muestren la evolución del perfil de riesgo antes y después de la iniciativa.

## 6. Hoja «Gráficos»

Se recomienda incluir:

- Gráfico de barras del IGM y subíndices por dominio.
- Serie temporal del IGM para la organización (si hay varias mediciones en el tiempo).
- Gráficos de dispersión que relacionen el IGM con métricas de incidentes reales (número de incidentes, coste total, etc.).
- Gráficos de barras apiladas para mostrar el impacto relativo de distintas iniciativas en la reducción de pérdida.

Estos gráficos alimentarán el reporte ejecutivo que se describe en la plantilla de PowerPoint.