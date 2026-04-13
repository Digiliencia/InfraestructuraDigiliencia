# Plantilla de Excel para IGM y ROI basada en GQM + PRAGMATIC

## 1. Estructura del libro

Se recomienda un libro con las siguientes hojas:

1. **Respuestas_Encuesta**: datos de organizaciones (incluyendo respuestas a preguntas GQM relevantes).
2. **Codificacion_Metricas**: mapeo de respuestas a valores numéricos para cada métrica.
3. **Calculo_Metricas**: cálculo por organización de M1.1–M5.3 y otras métricas derivadas.
4. **PRAGMATIC**: puntuaciones de cada métrica en criterios PRAGMATIC y pesos resultantes.
5. **IGM**: cálculo del Indicador Global de Madurez agregando métricas ponderadas.
6. **ROI**: estimación de retorno de la inversión en modelado de amenazas.
7. **Resumen**: visualizaciones y tablas para reportes ejecutivos.

## 2. Hoja «Respuestas_Encuesta»

Columnas principales:

- `ID_Organizacion`, `Sector`, `Tamano`, `Ambito_Geografico`.
- Variables que permitan calcular las métricas:
  - Número de amenazas por categoría STRIDE, por sistema.
  - Indicadores de presencia de categorías ENISA.
  - Número de amenazas nuevas vs. catálogo base.
  - Número de amenazas por equipo para escenarios comparables.
  - Nº amenazas descartadas tras poda.
  - Horas por rol y sesión.
  - Nº amenazas con control, con registro de riesgo, con parámetros de continuidad.
  - Fechas de eventos clave (publicación ENISA TL, actualización de modelos, etc.). [web:13][web:7]

## 3. Hoja «Codificacion_Metricas»

Contendrá:

- Definiciones de cada métrica (M1.1–M5.3) y fórmula textual.
- Asignación de rangos a categorías cualitativas cuando proceda (por ejemplo, nivel de uso de datos ENISA: No/Parcial/Intensivo → 0/0,5/1).

## 4. Hoja «Calculo_Metricas»

Para cada organización, filas con las siguientes columnas calculadas:

- `M1_1_Cobertura_STRIDE`, `M1_2_Cobertura_ENISA`, `M1_3_Tasa_Nuevas`.
- `M2_1_Varianza_Inter`, `M2_2_Porc_Descartadas`, `M2_3_Solapamiento`.
- `M3_1_Esfuerzo_Sesion`, `M3_2_Esfuerzo_Amenaza_Util`, `M3_3_Esfuerzo_Relativo`.
- `M4_1_Porc_Con_Control`, `M4_2_Tiempo_Registro_Riesgo`, `M4_3_Porc_RTO_RPO`.
- `M5_1_Mapeo_ENISA`, `M5_2_Uso_Datos_ENISA`, `M5_3_Tiempo_Reaccion_ENISA`.

Las fórmulas pueden implementarse con referencias a columnas de «Respuestas_Encuesta» utilizando funciones como SUMA, PROMEDIO, VAR.P, etc.

## 5. Hoja «PRAGMATIC»

Estructura sugerida:

- Columnas: `Metrica`, `P`, `R`, `A`, `G`, `M`, `Pr`, `T`, `I`, `C`, `Puntuacion_Global`, `Peso_Normalizado`.
- `Puntuacion_Global`: media simple o ponderada de los 9 criterios.
- `Peso_Normalizado`: puntuación global de la métrica dividida por la suma de todas las puntuaciones globales, para usar como peso relativo en el IGM.

Ejemplo de fórmula:

- `Puntuacion_Global = PROMEDIO(P:C)` (si las columnas P–C contienen los 9 criterios).
- `Peso_Normalizado = Puntuacion_Global / SUMA(Puntuacion_Global_de_todas_las_metricas)`.

## 6. Hoja «IGM»

Para cada organización:

1. Multiplicar cada métrica Mx.y por su `Peso_Normalizado` procedente de la hoja «PRAGMATIC».
2. Sumar los productos para obtener un IGM en escala 0–1.
3. Escalar a 0–100: `IGM_100 = IGM * 100`.

También pueden calcularse sub-índices por objetivo (G1–G5) agrupando métricas correspondientes y recalculando pesos internos.

## 7. Hoja «ROI»

Columnas sugeridas:

- `Coste_Modelado_Anual`.
- `Reduccion_Incidentes` (o cambio en tasa de incidentes relevantes).
- `Coste_Medio_Incidente`.
- `Prob_Contribucion_Modelado` (P_Incidente_Evitado).

Fórmulas básicas:

- `Beneficio_Bruto = Reduccion_Incidentes * Coste_Medio_Incidente * Prob_Contribucion_Modelado`.
- `ROI = (Beneficio_Bruto - Coste_Modelado_Anual) / Coste_Modelado_Anual`.

En un análisis más fino, puede explorarse la relación entre IGM y ROI estimado mediante gráficos de dispersión, para evidenciar (o refutar, según el caso) la correlación entre madurez de modelado de amenazas y beneficios económicos.

## 8. Hoja «Resumen»

Debe incluir:

- Distribuciones de IGM por sector, tamaño, ámbito geográfico.
- Sub-índices por objetivo G1–G5.
- Relación entre IGM y ROI (gráfico de dispersión o burbujas).
- Resumen de métricas top según PRAGMATIC (las más influyentes en el IGM).