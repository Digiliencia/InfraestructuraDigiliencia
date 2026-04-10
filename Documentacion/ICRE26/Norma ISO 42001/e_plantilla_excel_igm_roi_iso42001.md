# (e) Plantilla de Excel para cálculo de IGM y ROI (descripción)

## 1. Estructura general del fichero Excel

Se recomienda un libro de Excel con al menos cinco hojas:

1. `Catalogo_Preguntas`: listado de preguntas, bloques, códigos y pesos.
2. `Respuestas`: registro de respuestas para cada organización (o unidad) encuestada.
3. `Calculos_IGM`: procesamiento de respuestas y cálculo de índices.
4. `Calculos_ROI`: consolidación de costes, beneficios e indicadores de incidentes.
5. `Dashboard`: visualización de resultados mediante tablas y gráficos.

## 2. Hoja `Catalogo_Preguntas`

Columnas sugeridas:
- A: Código de pregunta (ej. B2_1, B4_3, etc.).
- B: Bloque (1–10).
- C: Descripción corta de la pregunta.
- D: Ponderación dentro del bloque (0–1), si se desea diferenciar preguntas.
- E: Número de opciones de respuesta.
- F–J: Texto de cada opción de respuesta (para referencia).
- K–O: Valor numérico asignado a cada opción (0–3 o 0–4).

Esta hoja sirve como diccionario central. El mantenimiento del catálogo aquí permite adaptar la encuesta sin reescribir fórmulas.

## 3. Hoja `Respuestas`

Filas:
- Una fila por organización o unidad evaluada.

Columnas:
- A: Identificador de la organización.
- B: Sector.
- C: Tamaño.
- D: País.
- E en adelante: Una columna por pregunta (mismo código que en `Catalogo_Preguntas`).

Las celdas de respuestas pueden contener el número de opción elegida (1, 2, 3, 4, …) o directamente el valor numérico correspondiente, según se prefiera. Otra opción es usar validación de datos con listas desplegables basadas en las opciones de `Catalogo_Preguntas`.

## 4. Hoja `Calculos_IGM`

### 4.1. Conversión de respuestas en puntuaciones

Para cada celda de respuesta, se utiliza una fórmula de búsqueda (por ejemplo, BUSCARV o INDICE/COINCIDIR) que, a partir del código de pregunta y la opción escogida, obtiene el valor numérico definido en `Catalogo_Preguntas`.

Se puede organizar la hoja de modo que:
- Cada fila represente una organización.
- Cada bloque tenga un rango dedicado donde se calculan las medias de sus preguntas.

### 4.2. Cálculo de puntuación por bloque

Para cada bloque:
- Calcular la media simple o ponderada de las puntuaciones de sus preguntas.
- Normalizarla a una escala de 0–1 dividiendo entre la puntuación máxima posible.

Por ejemplo, si un bloque tiene preguntas con máximo 3 puntos, la puntuación normalizada del bloque será:

`Puntuacion_Bloque = (SUMA(Puntuaciones_Preguntas) / (Número_Preguntas × 3))`

### 4.3. Aplicación de pesos de bloque

En una tabla aparte de la misma hoja, definir los pesos de cada bloque (suma total = 1). El IGM global se calcula como:

`IGM = 100 × SUMAPRODUCTO(Puntuaciones_Bloque_Normalizadas; Pesos_Bloque)`

Los subíndices se calculan de forma análoga, agrupando bloques (por ejemplo, Gobernanza = bloques 1–3, Monitorización = bloques 6–7, etc.).

## 5. Hoja `Calculos_ROI`

### 5.1. Entradas de costes

Columnas de ejemplo:
- Costes de personal dedicados al AIMS.
- Costes de herramientas (monitorización, pruebas de seguridad, automatización).
- Costes de consultoría, certificación y auditoría.
- Costes de formación y sensibilización.

### 5.2. Entradas de beneficios

Columnas de ejemplo:
- Número de incidentes de IA antes de la implantación (periodo base).
- Número de incidentes de IA después de la implantación.
- Coste medio estimado por incidente.
- Reducción en tiempos de respuesta y recuperación.
- Costes evitados por sanciones o litigios no producidos (estimados).

### 5.3. Cálculo de beneficios netos

Se puede estimar un “beneficio anual atribuible al AIMS” como:

`Beneficio = (Incidentes_Base – Incidentes_Actuales) × Coste_Medio_Incidente + Otros_Beneficios_Cuantificados`

El ROI se obtiene con la fórmula:

`ROI = (Beneficio – Costes_Anuales_AIMS) / Costes_Anuales_AIMS`

Se recomienda representar también el ROI acumulado a varios años, especialmente cuando los costes de implantación inicial son significativos.

## 6. Hoja `Dashboard`

Incluir gráficos y tablas tales como:
- Gráfico de barras con IGM por organización o unidad.
- Gráfico radar con subíndices por bloque.
- Serie temporal de IGM si se repite la encuesta.
- Gráfico de dispersión entre IGM y número de incidentes.
- Indicadores clave (IGM global, ROI estimado, bloques más débiles).

El objetivo es que el comité de riesgos o el consejo de administración pueda captar en una sola diapositiva dónde se está bien, dónde se está mal y cuánto cuesta mejorar.
