# Plantilla para Cálculo de IGM y ROI en Ciberseguridad

Este documento describe la estructura recomendada de la hoja de cálculo (Excel o equivalente) para calcular el Índice Global de Madurez (IGM) y estimar el ROI de inversiones en ciberseguridad a partir de las respuestas de la encuesta.

## 1. Estructura general de la hoja

Se recomiendan al menos cuatro hojas:

1. `Datos_Encuesta` – Respuestas codificadas por organización.  
2. `Ponderaciones` – Tabla de mapeo pregunta → dimensión → peso.  
3. `IGM_Resultados` – Cálculo de subíndices e IGM global.  
4. `ROI` – Cálculos de coste, pérdida esperada y ROI.

## 2. Hoja “Datos_Encuesta”

Columnas sugeridas:

- A: ID_Organización  
- B: Sector  
- C: Tamaño  
- D–ZZ: Variables codificadas (P1_1_1, P1_1_2, etc.)

Ejemplo de codificación:

- P1_1_1: 0–4 según nivel de madurez elegido.  
- P3_1_1_ENS: 0/1 si ENS aplicable.  
- P4_1_2_MFA_TOTAL: 0–4 según cobertura MFA.

## 3. Hoja “Ponderaciones”

Columnas:

- Pregunta_ID  
- Dimensión (IG_GOB, IG_RIESGO, etc.)  
- Peso_en_dimensión (0–1)  
- Peso_global (para análisis alternativos)

Ejemplo:

| Pregunta_ID | Dimensión | Peso_en_dimensión |
|-------------|-----------|-------------------|
| P1_1_1      | IG_GOB    | 0,15              |
| P1_2_1      | IG_GOB    | 0,10              |
| P2_1_1      | IG_RIESGO | 0,15              |

La suma de pesos por dimensión debe ser 1.

## 4. Hoja “IGM_Resultados”

Para cada organización:

1. Calcular subíndices por dimensión como media ponderada de las preguntas asociadas.  
2. Normalizar subíndices a escala 0–100.  
3. Calcular IGM como suma ponderada de subíndices.

Ejemplo Fórmulas (pseudocódigo Excel):

- `IG_GOB = SUMPRODUCT(Respuestas_GOB; Pesos_GOB) / SUM(Pesos_GOB)`  
- `IG_GOB_Norm = IG_GOB * (100 / Valor_Maximo_GOB)`  
- `IGM = IG_GOB_Norm * 0,2 + IG_RIESGO_Norm * 0,2 + ...`

## 5. Hoja “ROI”

### 5.1. Variables básicas

Por organización:

- `Coste_Ciberseguridad_Anual` – Gasto anual en ciberseguridad.  
- `Coste_TIC_Anual` – Gasto anual total TIC.  
- `%_Ciber_vs_TIC` – Calculado.  
- `IGM_Anterior` – Madurez en año t‑1 (si se dispone).  
- `IGM_Actual` – Madurez en año t.  
- `ALE_Anterior` – Pérdida anual esperada estimada antes.  
- `ALE_Actual` – Pérdida anual esperada estimada después.

### 5.2. Modelo simple de ROI

Se propone un modelo de ROI basado en la reducción de pérdida esperada:

- `Beneficio = ALE_Anterior – ALE_Actual`  
- `Inversión = Coste_Ciberseguridad_Anual` (o incremento respecto a t‑1)  
- `ROI = (Beneficio – Inversión) / Inversión`

Los valores de ALE pueden estimarse:

- A partir de modelos internos de riesgo, si existen.  
- Mediante supuestos prudentes basados en histórico de incidentes y en variación del IGM.

### 5.3. Enfoque pragmático

Si no se dispone de ALE, se pueden utilizar aproximaciones:

- Estimar una curva que relacione IGM con probabilidad de incidentes graves.  
- Utilizar benchmarks sectoriales como referencia.  
- Plantear escenarios (optimista, conservador, pesimista) para exploración de sensibilidad.

El Excel debe permitir ajustar estos parámetros sin necesidad de invocar a ningún oráculo estadístico.

## 6. Visualizaciones recomendadas

En hojas adicionales, generar gráficos:

- Dispersión IGM vs. % presupuesto TIC en ciberseguridad.  
- Barras comparando subíndices por sector.  
- Evolución temporal del IGM para organizaciones con datos de varios años.  
- Diagrama de burbujas: criticidad vs. madurez vs. tamaño de organización.

Estas visualizaciones facilitan la conversación con la alta dirección y con reguladores sin necesidad de llevarles todos los detalles técnicos.
