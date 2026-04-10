# Plantilla de Excel para cálculo de IGM y ROI Zero Trust (versión GQM + PRAGMATIC)

Esta plantilla extiende la versión anterior, incorporando referencias a objetivos GQM y puntuaciones PRAGMATIC por métrica.

## 1. Hojas recomendadas

- `Respuestas` – datos crudos por organización (encuesta).  
- `Ponderaciones` – pesos por pregunta y por pilar.  
- `IGM` – cálculo del Índice Global de Madurez.  
- `ROI` – cálculo del retorno de la inversión.  
- `M_GQM` – catálogo de métricas GQM (M1.1, M2.2, etc.).  
- `PRAGMATIC` – puntuaciones PRAGMATIC por métrica.  
- `Diccionario` – descripción de campos y escalas.

## 2. Hoja `M_GQM`

Columnas sugeridas:

- `ID_Metrica` (ej.: M1.1, M2.2).  
- `Descripcion` ("# usuarios con MFA en sistemas críticos").  
- `Pilar` (Identidad, Dispositivos, Red, Aplicaciones, Datos, Transversal).  
- `Objetivo_GQM` (referencia breve, ej.: G1).  
- `Formula` (texto pseudocódigo: numerador/denominador).  
- `Unidad` (% / días / horas / nº).  
- `Fuente_Datos` (IAM, EDR, SIEM, CMDB, etc.).

## 3. Hoja `PRAGMATIC`

Para cada `ID_Metrica`, incluir columnas:

- `Predictivo_P` (0–3).  
- `Relevante_R` (0–3).  
- `Accionable_A` (0–3).  
- `Genuino_G` (0–3).  
- `Significativo_M` (0–3).  
- `Preciso_P` (0–3).  
- `Oportuno_T` (0–3).  
- `Independiente_I` (0–3).  
- `Rentable_C` (0–3).  
- `Score_Total` (suma o media de los nueve criterios).  

Esto permite filtrar y priorizar métricas con mayor `Score_Total`.

## 4. Hoja `Respuestas`

Igual que en la plantilla básica, pero se recomienda añadir:

- Columnas que ya calculen algunas métricas técnicas (MTTD, MTTR, % MFA, etc.) si se dispone de datos brutos.  
- Identificadores de organización y de sector para análisis segmentado.

## 5. Hoja `IGM`

### 5.1. Puntuación por pilar

- Para cada pilar, usar `SUMAPRODUCTO` entre las respuestas codificadas (0–4) de las preguntas asignadas y los pesos definidos en `Ponderaciones`.  
- Normalizar cada pilar a una escala 0–4 o 0–5.

### 5.2. IGM total 0–100

- `IGM_Raw` = suma de (Score_pilar × Peso_pilar).  
- `IGM_0_100` = `IGM_Raw * 25` (si los pilares están en 0–4 y suman peso 1).

### 5.3. Enlace con métricas GQM

- Opcionalmente, crear columnas que combinen respuestas de la encuesta para aproximar métricas GQM (ej.: codificar respuestas de MFA para derivar M1.1 en tramos porcentuales).

## 6. Hoja `ROI`

Similar a la plantilla básica, con posibilidad de:

- Incorporar como variables explicativas el IGM y algunas métricas GQM (M1.1, M6.2, M6.3).  
- Analizar correlaciones entre madurez y coste de incidentes.

## 7. Hoja `Diccionario`

Debe documentar:

- Cada campo de `Respuestas`, `M_GQM`, `PRAGMATIC`, `IGM`, `ROI`.  
- Referencia a objetivo GQM y pilar.  
- Relación con normas (ENS, NIS2, DORA, etc.).

El objetivo es que cualquier analista externo pueda entender cómo se calculan el IGM y las métricas derivadas sin necesidad de descifrar jeroglíficos internos.