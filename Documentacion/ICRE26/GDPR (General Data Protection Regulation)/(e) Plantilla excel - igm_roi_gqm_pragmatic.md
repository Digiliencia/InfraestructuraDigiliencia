# Plantilla de Excel – IGM y ROI (versión GQM + PRAGMATIC)

Este archivo complementa la plantilla anterior de IGM/ROI, integrando el marco
GQM y las calificaciones PRAGMATIC. [web:12][web:23][web:27]

## 1. Hojas sugeridas

- `Respuestas_Encuesta` – Respuestas a la encuesta organizacional.
- `Métricas` – Cálculo de cada métrica Mx.y a partir de respuestas.
- `PRAGMATIC` – Puntuación de calidad de cada métrica.
- `IGM` – Índice Global de Madurez por bloques y global.
- `ROI` – Análisis de retorno de inversión por iniciativas.

## 2. Hoja `Métricas`

Columnas recomendadas:

- `A`: ID Métrica (M1.1, M1.2, etc.).
- `B`: Descripción.
- `C`: Objetivo GQM (G1–G5).
- `D`: Fórmula de cálculo (referencia a `Respuestas_Encuesta`).
- `E`: Valor actual.
- `F`: Valor objetivo (meta).
- `G`: Brecha (en términos coherentes con cada métrica).

Ejemplos de lógica:

- M1.1 (Nº de brechas notificadas/año): se toma directamente de la pregunta
  de encuesta o de datos reales del registro de incidentes.
- M2.1 (% de datos cifrados en reposo): promedio ponderado de respuestas por
  sistemas/entornos, o % real obtenido de inventario de activos.
- M3.1 (MTTR-detección): media de tiempos de detección registrados.

## 3. Hoja `PRAGMATIC`

Columnas:

- `A`: ID Métrica.
- `B`: P (Predictivo).
- `C`: R (Relevante).
- `D`: A (Accionable).
- `E`: G (Genuino).
- `F`: M (Significativo).
- `G`: P2 (Preciso).
- `H`: T (Oportuno).
- `I`: I (Independiente).
- `J`: C (Rentable).
- `K`: Suma PRAGMATIC.
- `L`: PRAGMATIC medio (K / 9).

Fórmulas típicas:

- `K2 = SUMA(B2:J2)`
- `L2 = K2/9`

Se recomienda resaltar en rojo métricas con `L < 1,5` para identificar
indicadores de baja calidad que convendría revisar o eliminar.

## 4. Integración con `IGM`

En la hoja `IGM`:

1. Definir bloques (por ejemplo, G1–G5 o bloques temáticos: Resultados,
   Controles, Operación, Terceros, Cultura/ROI).
2. Para cada bloque, seleccionar solo métricas con `PRAGMATIC medio >= umbral`
   (por ejemplo, 1,5).
3. Calcular una media ponderada por bloque:
   - Peso de cada métrica dentro del bloque,
   - o simple media si se desea simplicidad.

Ejemplo de columnas:

- `A`: Bloque.
- `B`: IGM_Bloque (media de métricas seleccionadas).
- `C`: Peso del bloque en IGM global.
- `D`: Contribución al IGM global (`=B*C`).

IGM global: suma de las contribuciones de todos los bloques.

## 5. Integración con `ROI`

En la hoja `ROI`, para cada iniciativa:

- listar las métricas Mx.y que se espera mejorar (por ejemplo, M2.3, M3.1, M3.3),
- indicar valor actual (columna `E` de `Métricas`) y valor objetivo (columna `F`),
- traducir la variación de la métrica en reducción de probabilidad o impacto
  de incidentes, apoyándose en supuestos documentados. [web:12]

Estructura típica de tabla:

- `A`: ID iniciativa.
- `B`: Descripción.
- `C`: Métricas afectadas (lista Mx.y).
- `D`: Coste total iniciativa (CAPEX+OPEX).
- `E`: Reducción estimada de probabilidad (%) y/o impacto (€).
- `F`: Ahorro anual esperado (€).
- `G`: Horizonte (años).
- `H`: Ahorro total horizonte (`=F*G`).
- `I`: ROI (`=(H-D)/D`).

Así, la narrativa de ROI se asienta en métricas que han superado el filtro
PRAGMATIC y se conectan explícitamente con objetivos GQM.

## 6. Notas prácticas

- Mantener una hoja `Supuestos` donde se documentan fuentes de probabilidades,
  impactos y valores objetivo.
- Versionar el libro (v1, v2…) cuando se ajustan objetivos o métricas.
- Revisar anualmente el conjunto de métricas con baja puntuación PRAGMATIC
  para mejorarlas o sustituirlas.