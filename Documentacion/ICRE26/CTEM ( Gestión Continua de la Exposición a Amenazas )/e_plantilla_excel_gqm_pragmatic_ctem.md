# (e) Plantilla de Excel para IGM y ROI basada en métricas GQM + PRAGMATIC

Esta plantilla extiende la anterior plantilla de IGM/ROI incorporando explícitamente las métricas M1.x–M6.x definidas en el marco GQM.

## 1. Hojas recomendadas

1. `Respuestas_Org`: respuestas por organización (incluye campos específicos para M1.x–M6.x donde aplique).
2. `Metricas_CTEM`: cálculo de cada métrica M1.x–M6.x a partir de datos brutos.
3. `Ponderaciones_IGM`: pesos de preguntas/indicadores por eje de madurez.
4. `IGM_CTEM`: cálculo del índice de madurez por eje y global.
5. `ROI_CTEM`: cálculo del ROI usando incidentes, costes y métricas de exposición.
6. `PRAGMATIC_Scores`: tabla con puntuaciones PRAGMATIC por métrica.
7. `Parametros`: constantes, supuestos y valores por defecto.

## 2. Hoja "Respuestas_Org"

Contendrá:

- `ID_Org`, `Sector`, `Tamano`, `Pais`.
- Variables de base: número de activos críticos, exposiciones críticas, incidentes, etc.
- Valores declarados o derivados necesarios para calcular M1.1–M6.3.

## 3. Hoja "Metricas_CTEM"

Columnas sugeridas:

- `ID_Org`
- `M1_1`, `M1_2`, `M1_3`, ..., `M6_3`

Ejemplos de cálculo:

- `M1_1 = Activos_Criticos_Inventariados / Activos_Criticos_Estimados`
- `M1_2 = Activos_Criticos_Con_Descubrimiento_Continuo / Activos_Criticos_Inventariados`
- `M3_1 = Expos_Criticas_Cerradas_SLA / Expos_Criticas_Totales`
- `M3_2 = PROMEDIO(Dias_Remediacion_Expos_Criticas)`
- `M3_3 = Indice_Exposicion_Mes_Actual - Indice_Exposicion_Mes_Anterior`

Los datos fuente pueden venir de sistemas CTEM, inventarios, herramientas de tickets o de la propia encuesta.

## 4. Hoja "Ponderaciones_IGM"

Añadir columnas:

- `Metrica` (M1.1, M1.2, ...).
- `Descripcion`.
- `Eje_Madurez` (Gobernanza, Superficie, Validacion, Movilizacion, Resultados, Normativo).
- `Peso_Eje` (0–1 dentro de cada eje).
- `Peso_Global` (peso relativo de cada eje dentro del IGM global).
- `Max_Vlr` (valor objetivo o máximo de referencia para normalizar).

La normalización típica:

`Metrica_Normalizada = MIN( Valor_Org / Max_Vlr ; 1 )`

## 5. Hoja "IGM_CTEM"

Para cada organización:

- Calcular `Punt_Eje_X = SUMA( Metrica_Normalizada_i * Peso_Eje_i )` por eje.
- Normalizar cada eje a escala 0–5:

`Madurez_Eje_X = Punt_Eje_X * 5`

(si los pesos del eje suman 1).

- Calcular `IGM_Global = SUMA( Madurez_Eje_X * Peso_Global_X )`.

Se pueden añadir columnas:

- `Nivel_Madurez` (Bajo/Medio/Alto según umbrales de `Parametros`).
- `Ranking_Sectorial`.

## 6. Hoja "PRAGMATIC_Scores"

Incluir la tabla de la matriz PRAGMATIC con columnas adicionales:

- `Score_Total` (suma P+R+...+T).
- `Incluir_en_IGM` (Sí/No).
- `Comentario_Local`.

Opciones:

- Filtrar métricas con `Score_Total` inferior a un umbral para que no influyan en el IGM.
- Visualizar un gráfico de barras de calidad de métricas.

## 7. Hoja "ROI_CTEM"

Variables de entrada por organización:

- `Incidentes_Graves_Antes`, `Incidentes_Graves_Despues`.
- `Coste_Medio_Incidente`.
- `Coste_Anual_CTEM`.
- `Periodo` (años).
- Opcionalmente, `Reduccion_MTTR_Servicio`, `Coste_Hora_Interrupcion`.

Cálculos:

- `Incidentes_Evitados = MAX( Incidentes_Graves_Antes - Incidentes_Graves_Despues ; 0 )`
- `Perdidas_Evitadas = Incidentes_Evitados * Coste_Medio_Incidente`
- `Horas_Evitadas = Reduccion_MTTR_Servicio * Incidentes_Graves_Despues`
- `Coste_Interrupcion_Evitado = Horas_Evitadas * Coste_Hora_Interrupcion`
- `Beneficio_Total_CTEM = Perdidas_Evitadas + Coste_Interrupcion_Evitado`
- `Coste_Total_Programa = Coste_Anual_CTEM * Periodo`
- `ROI_CTEM = (Beneficio_Total_CTEM - Coste_Total_Programa) / Coste_Total_Programa`
- `ROI_% = ROI_CTEM * 100`

Se pueden usar las métricas M3.1, M3.2 y M5.3 para estimar cómo la mejora de madurez CTEM se relaciona con las variaciones en incidentes y tiempos de recuperación.

## 8. Hoja "Parametros"

Variables recomendadas:

- `Umbral_IGM_Alto`, `Umbral_IGM_Medio`, `Umbral_IGM_Bajo`.
- `Umbral_Score_PRAGMATIC_Min`.
- Valores de referencia de `Max_Vlr` para cada métrica.
- Costes medios por incidente y por hora de interrupción, por sector.

Con este diseño, la hoja de cálculo se convierte en la columna vertebral numérica que conecta datos CTEM de bajo nivel con índices de madurez y argumentos económicos a nivel organizativo y nacional.