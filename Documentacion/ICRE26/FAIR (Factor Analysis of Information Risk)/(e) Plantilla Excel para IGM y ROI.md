# Plantilla de Excel para cálculo de IGM y ROI de controles basados en FAIR

## 1. Objetivo de la plantilla

Esta plantilla está diseñada para que una organización pueda calcular, de forma sencilla pero rigurosa, el impacto económico de la mejora de controles de seguridad (IGM: Índice de Ganancia en Mitigación) y el retorno de la inversión (ROI) utilizando resultados de modelos FAIR.

## 2. Estructura de hojas

Se recomienda estructurar el archivo Excel en las siguientes hojas:

1. **Entrada_Escenarios**: definición de escenarios de riesgo antes y después de controles.
2. **Parametros_Controles**: detalle de controles, costes y efectos esperados.
3. **Calculos_FAIR**: derivación de pérdidas esperadas y diferenciales.
4. **Indicadores_IGM_ROI**: síntesis de métricas para decisión.
5. **Resumen_Graficos**: tablas dinámicas y gráficos para reporte.

## 3. Hoja “Entrada_Escenarios”

Columnas sugeridas:

- A: ID_Escenario
- B: Descripción_Escenario
- C: Activo_Afectado
- D: Dominio (IT/OT/Datos personales/Nube/Terceros)
- E: ALE_Base (pérdida anual esperada antes de mejorar controles)
- F: ALE_Post (pérdida anual esperada después de mejorar controles)
- G: Percentil_95_Base
- H: Percentil_95_Post
- I: Supuestos_Principales (texto breve)

Las columnas E–H pueden alimentarse desde modelos FAIR internos o desde simulaciones (por ejemplo, exportadas desde herramientas especializadas).

## 4. Hoja “Parametros_Controles”

Columnas sugeridas:

- A: ID_Control
- B: Nombre_Control
- C: Tipo_Control (Prevención/Detección/Respuesta/Recuperación)
- D: Dominio (IT/OT/…)
- E: Coste_Inicial (CAPEX)
- F: Coste_Operativo_Anual (OPEX)
- G: Vida_Util_Años
- H: Escenarios_Afectados (lista de ID_Escenario)
- I: Reducción_LEF_Estimada (%)
- J: Reducción_LM_Estimada (%)
- K: Fuente_Estimación (experto/datos/modelo)

Estas columnas permiten vincular controles con escenarios y documentar supuestos de reducción de frecuencia y magnitud.

## 5. Hoja “Calculos_FAIR”

Columnas sugeridas (resultado por combinación Escenario–Control):

- A: ID_Escenario
- B: ID_Control
- C: ALE_Base
- D: ALE_Post
- E: Delta_ALE (E = C – D)
- F: Percentil_95_Base
- G: Percentil_95_Post
- H: Delta_Percentil_95 (H = F – G)

En esta hoja pueden calcularse también:

- I: Coste_Total_Control = Coste_Inicial prorrateado por año + Coste_Operativo_Anual.
- J: Años_Amortizacion = Coste_Total_Control / Delta_ALE.

## 6. Hoja “Indicadores_IGM_ROI”

Se propone definir:

- IGM (Índice de Ganancia en Mitigación) = Delta_ALE / ALE_Base.
- ROI_Anual = (Delta_ALE – Coste_Total_Control) / Coste_Total_Control.

Columnas sugeridas por control:

- A: ID_Control
- B: Nombre_Control
- C: ALE_Total_Base (suma de ALE_Base en escenarios afectados)
- D: ALE_Total_Post
- E: Delta_ALE_Total
- F: Coste_Total_Anual_Control
- G: IGM = E / C
- H: ROI_Anual = (E – F) / F

## 7. Hoja “Resumen_Graficos”

Incluir, al menos:

- Tabla de controles ordenados por Delta_ALE_Total.
- Gráfico de barras con IGM por control.
- Gráfico de burbujas (Coste_Total vs Delta_ALE_Total, tamaño = IGM).

## 8. Notas de uso

- Los valores ALE_Base y ALE_Post deben provenir de análisis FAIR consistentes (misma metodología, supuestos comparables).
- Siempre que sea posible, documente la fuente de cada estimación en columnas de texto (para evitar que los números floten sin contexto).
- Revise periódicamente la coherencia entre las reducciones estimadas de LEF/LM y los datos reales de incidentes.