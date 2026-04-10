# Plantilla de Excel para cálculo de IGM y ROI con GQM + PRAGMATIC

## 1. Estructura propuesta del libro

Hojas recomendadas:

- `Métricas`: registro de valores de métricas FAIR‑STRIDE para cada organización/sector.
- `GQM`: definición de objetivos y preguntas asociadas a las métricas.
- `PRAGMATIC`: puntuación de calidad de cada métrica.
- `IGM`: cálculo de Índice Global de Madurez y subíndices.
- `ROI`: análisis de retorno de la inversión en iniciativas.
- `Dashboards`: gráficos y tablas para reportes.

## 2. Hoja «Métricas»

Columnas sugeridas:

- `Entidad_ID`: organización, sector o ámbito territorial.
- `Fecha`: periodo de referencia (año, semestre, trimestre).
- `Métrica_ID`: código (A1, A2, I1, C2, etc.).
- `Valor`: valor numérico de la métrica (ej. 12 incidentes, 3.5M€, 87 %).
- `Unidad`: unidades (nº, €, %, horas, etc.).
- `Dominio`: Autenticidad, Integridad, etc.
- `Goal_ID`: referencia al objetivo GQM principal.
- `Fuente_Datos`: sistema o proceso de donde se extrae la métrica.

## 3. Hoja «GQM»

Columnas:

- `Goal_ID`: identificador del objetivo (ej. G_AUT_01).
- `Nivel`: Nacional / Sectorial / Organizativo.
- `Descripción_Goal`: texto del objetivo.
- `Question_ID`: identificador de la pregunta (ej. Q_AUT_01).
- `Descripción_Pregunta`: texto de la pregunta.
- `Métrica_ID`: código asociado (puede haber varias métricas por pregunta).
- `Peso_Goal`: peso relativo del objetivo en el IGM.
- `Peso_Métrica`: peso de la métrica dentro del objetivo.

## 4. Hoja «PRAGMATIC»

Columnas:

- `Métrica_ID`
- `Predictivo` (0‑5)
- `Relevante` (0‑5)
- `Accionable` (0‑5)
- `Genuino` (0‑5)
- `Significativo` (0‑5)
- `Preciso` (0‑5)
- `Oportuno` (0‑5)
- `Independiente` (0‑5)
- `Rentable` (0‑5)
- `Score_Medio`: media simple o ponderada de los nueve criterios.
- `Comentarios`: notas sobre puntos fuertes y débiles.

Se puede definir una regla de negocio: sólo las métricas con `Score_Medio ≥ X` se usan en el IGM, o se asignan pesos mayores a métricas con mejor perfil PRAGMATIC.

## 5. Hoja «IGM»

Objetivo: calcular índices de madurez y, opcionalmente, de “calidad métrica”.

### 5.1 Cálculo de subíndices por dominio

Para cada `Entidad_ID` y `Dominio`:

- Traer desde `Métricas` los valores de métricas activas (las que cumplen umbral PRAGMATIC).
- A cada métrica se le asocia un `Peso_Métrica` (desde `GQM`) y opcionalmente un factor basado en `Score_Medio` PRAGMATIC (por ejemplo, multiplicar por `Score_Medio / 5`).

Ejemplo de fórmula conceptual:

- `Score_Métrica_Normalizada = f(Valor)` (si es necesario normalizar a escala 0‑4).
- `Score_Ajustado = Score_Métrica_Normalizada * (Score_Medio / 5)`.
- `Subíndice_Dominio = Σ(Score_Ajustado * Peso_Métrica) / Σ(Peso_Métrica)`.

### 5.2 Índice Global de Madurez (IGM)

- `IGM = Σ(Subíndice_Dominio * Peso_Dominio) / Σ(Peso_Dominio)`.

Peso_Dominio puede definirse a nivel nacional (por ejemplo, dar más peso a Disponibilidad y Confidencialidad para ciertos sectores).

## 6. Hoja «ROI»

Tabla de iniciativas (similar a la plantilla anterior, extendida con GQM):

Columnas:

- `Iniciativa_ID`
- `Descripción`
- `Dominio_Principal`
- `Goals_Asociados` (lista de `Goal_ID`)
- `Coste_Inicial`
- `Coste_Anual`
- `Pérdida_Actual` (media/p90 FAIR antes de la iniciativa)
- `Pérdida_Prevista`
- `Reducción_Pérdida`
- `Horizonte_Anios`
- `Beneficio_Total`
- `Coste_Total`
- `ROI_%`
- `Payback_Anios`
- `Impacto_IGM_Estimado` (cambio de subíndice/dominio y del IGM)

Así, cada iniciativa puede justificarse tanto por su impacto en riesgo económico como por su contribución a la madurez medida por el IGM.

## 7. Hoja «Dashboards»

Elementos recomendados:

- Gráfico del IGM y subíndices por dominio, para cada entidad y periodo.
- Gráficos que comparen métricas económicas FAIR con niveles de controles (por ejemplo, pérdidas por suplantación vs. % MFA).
- Mapas de calor que muestren, por sector o territorio, IGM y principales gaps PRAGMATIC.
- Vistas específicas para reguladores (visión macro) y para organizaciones (visión micro).