# Plantilla de Excel para IGM y ROI alineada con GQM + FAIR

## 1. Objetivo

Esta plantilla extiende la anterior hoja de cálculo de IGM/ROI, incorporando referencias GQM y facilitando la conexión con indicadores nacionales (PAE‑S, IECtrl‑S).

## 2. Hojas propuestas

1. **Objetivos_GQM**: recoge las metas (Goals) y preguntas (Questions) a las que responden los escenarios y controles.
2. **Escenarios_FAIR**: contiene parámetros FAIR por escenario (LEF, LM, ALE, percentiles).
3. **Controles_FAIRCAM**: detalla controles, costes y efecto esperado sobre LEF y LM.
4. **Calculos_IGM_ROI**: calcula Delta_ALE, IGM y ROI.
5. **Vinculo_Indicadores_Nacionales**: agrega resultados para alimentar PAE‑S, IECtrl‑S, etc.

## 3. Hoja “Objetivos_GQM”

Columnas sugeridas:

- A: ID_Goal
- B: Descripcion_Goal
- C: Horizonte_Temporal
- D: Indicadores_Asociados (PAE‑S, IFEP‑S, etc.)
- E: ID_Question
- F: Descripcion_Question
- G: Escenarios_Asociados (IDs de escenarios en Escenarios_FAIR)

## 4. Hoja “Escenarios_FAIR”

Columnas sugeridas:

- A: ID_Escenario
- B: Sector
- C: Activo_Clave
- D: Tipo_Escenario (IT/OT/Datos personales/…) 
- E: LEF_Base
- F: LEF_Post
- G: LM_Base
- H: LM_Post
- I: ALE_Base
- J: ALE_Post
- K: P95_Base
- L: P95_Post
- M: ID_Goal
- N: ID_Question

## 5. Hoja “Controles_FAIRCAM”

Columnas sugeridas:

- A: ID_Control
- B: Nombre_Control
- C: Tipo_Control
- D: Sector
- E: Coste_CAPEX_Anualizado
- F: Coste_OPEX_Anual
- G: Reduccion_LEF_Estimada (%)
- H: Reduccion_LM_Estimada (%)
- I: Escenarios_Afectados (lista ID_Escenario)
- J: Fuente_Estimacion

## 6. Hoja “Calculos_IGM_ROI”

Para cada combinación Escenario–Control:

- A: ID_Escenario
- B: ID_Control
- C: ALE_Base
- D: ALE_Post
- E: Delta_ALE = C – D
- F: Coste_Total_Control = CAPEX_Anualizado + OPEX_Anual
- G: IGM = Delta_ALE / ALE_Base
- H: ROI_Anual = (Delta_ALE – Coste_Total_Control) / Coste_Total_Control

## 7. Hoja “Vinculo_Indicadores_Nacionales”

Agregaciones por sector y país:

- A: Sector
- B: ALE_Total_Base = suma ALE_Base
- C: ALE_Total_Post = suma ALE_Post
- D: PAE_Sector = ALE_Total_Base (o Post, según escenario)
- E: IECtrl_S = (ALE_Total_Base – ALE_Total_Post) / ALE_Total_Base
- F: Contribucion_a_PAE_Nacional (como % del total)

Esta estructura permite que, a partir de datos organizativos, se alimenten directamente indicadores FAIR nacionales.