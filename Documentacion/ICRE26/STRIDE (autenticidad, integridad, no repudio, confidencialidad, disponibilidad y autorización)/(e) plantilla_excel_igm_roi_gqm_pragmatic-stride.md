# Plantilla de Excel para IGM y ROI basada en GQM + PRAGMATIC

Esta plantilla complementa la anterior (Encuesta STRIDE) introduciendo explícitamente las métricas GQM y su evaluación PRAGMATIC.

## 1. Hojas recomendadas

1. `Indicadores_GQM`: catálogo de métricas con definición técnica y mapeo STRIDE.
2. `Datos_Metricas`: valores de métricas por período (mes, trimestre, año).
3. `PRAGMATIC`: puntuaciones de criterios PRAGMATIC por métrica.
4. `IGM_STRIDE`: cálculo de índices por categoría y global.
5. `ROI`: análisis de costes y beneficios de controles asociados a métricas clave.
6. `Dashboard`: resumen visual para dirección.

## 2. Hoja “Indicadores_GQM”

Columnas sugeridas:

- `ID_Metrica` (ejemplo: S1, T2, D1...).
- `STRIDE` (S, T, R, I, D, E, GOV, MET).
- `Objetivo_GQM` (G-O-S, G-O-T...).
- `Pregunta`.
- `Metrica` (nombre corto).
- `Definicion` (resumen técnico).
- `Unidad` (%, horas, número, índice 0–1...).
- `Fuente_Datos` (SIEM, IAM, CMDB, herramientas OT, etc.).

## 3. Hoja “Datos_Metricas”

Filas: una por combinación `ID_Metrica` + período (por ejemplo, año o trimestre).

Columnas típicas:

- `Periodo` (ej. 2025-Q4, 2026-Q1...).
- `Valor` (dato numérico).
- `Umbral_Objetivo` (valor deseado).
- `Umbral_Alerta` (valor que dispara atención especial).

Ejemplo: para S1 (% accesos críticos con MFA), `Umbral_Objetivo` podría ser 0,9 (90 %), `Umbral_Alerta` 0,6.

## 4. Hoja “PRAGMATIC”

Usando la matriz de referencia, incluir:

- Columnas: `ID_Metrica`, `P`, `R`, `A`, `G`, `M`, `Prc`, `O`, `I`, `C`, `Puntuacion_Total`.
- `Puntuacion_Total` puede ser la suma o la media de los nueve criterios.

Esto permite priorizar la implementación de métricas:

- Métricas con puntuación total alta → candidatas prioritarias.
- Métricas con puntuación baja → reconsiderar o rediseñar.

## 5. Hoja “IGM_STRIDE”

### 5.1. Cálculo de puntuaciones por métrica

Se pueden normalizar los valores para que todas las métricas se sitúen entre 0 y 1 respecto a sus objetivos. Ejemplo general:

- Para métricas de tipo “más es mejor” (ej. % MFA):  
  `Score = MIN(Valor / Umbral_Objetivo, 1)`.

- Para métricas de tipo “menos es mejor” (ej. horas de indisponibilidad):  
  `Score = MIN(Umbral_Objetivo / Valor, 1)`.

### 5.2. Ponderación por categoría STRIDE y PRAGMATIC

- Definir un peso base por métrica (p.ej. igualitario o según criticidad).
- Multiplicar dicho peso por un factor basado en la puntuación PRAGMATIC (por ejemplo, `1 + Puntuacion_Total / 27`).

De este modo, métricas más “PRAGMATIC” aportan más al índice final.

### 5.3. Índices por categoría y global

Para cada categoría STRIDE (S, T, R, I, D, E, GOV, MET):

- `Score_Categoria = SUMA(Score_metrica * Peso_metrica) / SUMA(Peso_metrica)`.

El índice global IGM-STRIDE se calcula como media (simple o ponderada) de las categorías.

## 6. Hoja “ROI”

Similar a la plantilla anterior, pero vinculando controles a métricas específicas:

- `Control` (ej. despliegue PAM, mejora TLS, logging inmutable...).
- `Metricas_Asociadas` (lista de IDs: E1, R2, etc.).
- `Coste_Anual`, `Riesgo_Inicial`, `Riesgo_Residual`, `Beneficio_Anual`, `ROI`.

La conexión GQM ayuda a justificar inversiones: cada control puede mostrarse como “palanca” explícita sobre métricas y objetivos.

## 7. Hoja “Dashboard”

Elementos recomendados:

- Gráfico radar de índices STRIDE por período.
- Barras comparando valores actuales vs. objetivos por métrica clave.
- Tabla top‑5 métricas con mayor brecha frente a objetivo.
- Tabla top‑5 controles con mejor ROI estimado.

El resultado es un cuadro de mando donde se ve cómo los objetivos nacionales y organizativos (GQM) se encarnan en métricas concretas cuya calidad ha sido contrastada (PRAGMATIC).