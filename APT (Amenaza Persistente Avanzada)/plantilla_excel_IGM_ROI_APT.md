# (e) Plantilla de Excel para Cálculo de IGM y ROI

La siguiente descripción permite implementar una hoja de cálculo en Excel (o equivalente) para calcular el Índice Global de Madurez (IGM) y el ROI de ciberseguridad a partir de las respuestas de la encuesta.

## 1. Estructura general del libro

Se recomiendan al menos tres hojas:

1. **"Respuestas"**: registro de respuestas por organización.
2. **"Puntuaciones"**: transformación de respuestas en puntuaciones numéricas.
3. **"IGM_ROI"**: cálculo de índices, agregados y métricas financieras.

## 2. Hoja "Respuestas"

Columnas sugeridas:

- A: ID_Organización
- B: Sector
- C: Tamaño
- D: Ámbito
- E: Fecha_respuesta
- F–AZ: Preg_1, Preg_2, ..., Preg_42

Cada fila corresponde a una organización.

## 3. Hoja "Puntuaciones"

- Replicar las columnas ID_Organización, Sector, etc.
- Para cada pregunta, definir una columna de **puntuación numérica** (por ejemplo, P6, P7, ..., P41) según las reglas de mapeo.

### 3.1. Ejemplos de reglas de puntuación

- Pregunta 6 (estrategia formal):
  - Máximo órgano de gobierno: 3
  - Dirección intermedia: 2
  - En elaboración: 1
  - Prácticas dispersas / no existe: 0

- Preguntas 13, 22, 27 (escalas 0–3): la puntuación es directamente el valor seleccionado.

- Pregunta 15 (integración con continuidad): 3, 2, 1, 0 según grado.

Implementar estas reglas con funciones **SI()** o **BUSCARV()**.

## 4. Cálculo de subíndices por bloque

En la hoja "IGM_ROI":

Para cada bloque *b*, crear un rango con las puntuaciones de sus preguntas. Por ejemplo:

- Bloque Gobernanza (B_GOV): P6, P7, P8, P9, P10.
- Bloque Riesgo (B_RISK): P11, P12, P13.1–13.6, P14, P15.
- etc.

Calcular:

`IGM_GOV = PROMEDIO(P6;P7;P8;P9;P10) / 3`

(si todas las preguntas están en escala 0–3; si alguna no lo está, normalizar previamente).

Repetir para cada bloque.

## 5. Cálculo del IGM global

Definir pesos (por defecto, iguales):

- Peso_GOV, Peso_RISK, Peso_VECT, Peso_DET, Peso_RESP, Peso_CULT, Peso_INV, Peso_COLAB, Peso_FUTURO.

Calcular:

`IGM_global = SUMAPRODUCTO({IGM_GOV;IGM_RISK;IGM_VECT;...}; {Peso_GOV;Peso_RISK;Peso_VECT;...})`

Asegurarse de que la suma de pesos es 1.

## 6. Cálculo del ROI de ciberseguridad

En la hoja "IGM_ROI", añadir columnas:

- INV (inversión anual en ciberseguridad).
- PLA_0 (pérdida esperada anual antes de mejoras).
- PLA_1 (pérdida esperada anual después de mejoras).

Fórmula:

`ROI_ciber = (PLA_0 - PLA_1 - INV) / INV`

Para escenarios, se pueden crear columnas PLA_1_Esc1, PLA_1_Esc2… y calcular ROIs alternativos.

## 7. Visualizaciones sugeridas

- Gráfico radar de subíndices de bloque (IGM por dimensión).
- Gráfico de dispersión IGM_global vs. número de incidentes.
- Gráfico de barras inversión (% TI) vs. IGM_global.

Estas representaciones facilitan el uso del libro como soporte para reportes ejecutivos.