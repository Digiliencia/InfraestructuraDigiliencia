# Plantilla de Excel para IGM y ROI – Integrada con GQM + PRAGMATIC

## 1. Estructura propuesta del libro

Hojas recomendadas:

1. `Métricas_TRIKE` – catálogo de métricas (T, R, I, K, E), con códigos, definiciones y scores PRAGMATIC. [web:39][web:45]
2. `Datos_Brutos` – datos recolectados (por organización, sector, año...).
3. `IGM` – cálculo de subíndices y del Índice Global de Madurez.
4. `ROI` – estimaciones de retorno de inversión basadas en costes e impactos.
5. `Parametros` – pesos, umbrales, criterios PRAGMATIC y configuraciones.

## 2. Hoja `Métricas_TRIKE`

Columnas sugeridas:

- Código (p.ej. T1.1.a, R1.1.a, etc.).
- Nombre corto.
- Descripción detallada.
- Dimensión TRIKE (T/R/I/K/E).
- Tipo de dato (entero, porcentaje, monetario, etc.).
- Fuente (ENCUESTA, CSIRT, REGULADOR, MERCADO...).
- Scores PRAGMATIC (P, R, A, G, S, Pr, O, I, Rn).
- Meta-score PRAGMATIC (media o ponderación definida en `Parametros`). [web:45]

## 3. Hoja `Datos_Brutos`

Una fila por combinación relevante (p.ej. año–sector–tipo de entidad o, en estudios micro, por organización). Columnas típicas:

- Año.
- Sector.
- Tipo de entidad (esencial/importante/otra).
- Tamaño (micro, pyme, gran empresa, administración...).
- Valores de cada métrica (T1.1.a, T1.1.b, ..., E1.3.a).

## 4. Hoja `IGM`

### 4.1 Cálculo de subíndices por dimensión TRIKE

Para cada fila (p.ej. sector–año):

- `T_index = FUNCIÓN(T1.1.a_norm, T1.1.b_norm, T1.2.a_norm, T1.2.b_norm, T1.3.a_norm, T1.3.b_norm)`
- `R_index = FUNCIÓN(R1.1.a_norm, R1.2.a_norm, R1.3.a_norm, R1.3.b_norm)`
- `I_index = FUNCIÓN(I1.1.a_norm, I1.2.a_norm, I1.2.b_norm, I1.3.a_norm, I1.3.b_norm)`
- `K_index = FUNCIÓN(K1.1.a_norm, K1.2.a_norm, K1.3.a_norm, K1.3.b_norm)`
- `E_index = FUNCIÓN(E1.1.a_norm, E1.2.a_norm, E1.2.b_norm, E1.3.a_norm)`

Donde cada métrica se normaliza (si procede) a una escala 0–100, y la función puede ser una media simple o ponderada con pesos definidos en `Parametros` (posiblemente ajustados según meta-score PRAGMATIC para privilegiar métricas de mayor calidad). [web:45]

### 4.2 Cálculo del Índice Global de Madurez (IGM)

En `Parametros`, definir pesos de cada dimensión (wT, wR, wI, wK, wE).  

Fórmula general:

- `IGM = (wT*T_index + wR*R_index + wI*I_index + wK*K_index + wE*E_index) / (wT + wR + wI + wK + wE)`

Puede incorporarse un factor de calidad basado en PRAGMATIC:

- `IGM_ajustado = IGM * (1 - alpha*(1 - MetaScore_PRAGMATIC_global))`

donde `MetaScore_PRAGMATIC_global` refleja la calidad media de las métricas utilizadas y `alpha` ajusta la penalización por baja calidad.

## 5. Hoja `ROI`

Integrar los elementos clásicos de ROI con métricas de impacto (I1.2.a, I1.2.b) y riesgo (R1.1.a):

Variables de entrada por fila (sector/organización):

- `Coste_CS`: gasto anual en ciberseguridad.
- `Incidentes_previos`, `Coste_inc_previos`.
- `Incidentes_actuales`, `Coste_inc_actuales`.

Indicadores:

- `Reducción_incidentes = Incidentes_previos - Incidentes_actuales`
- `Reducción_coste = Coste_inc_previos - Coste_inc_actuales`

ROI básico:

- `ROI_CS = (Reducción_coste - Coste_CS) / Coste_CS`

Escenarios:

- Escenario 0: situación actual.
- Escenario 1: mejora en T y K (mejor detección/anticipación).
- Escenario 2: mejora en R e I (mejor gestión del riesgo e impacto).

## 6. Visualizaciones

- Gráficos radar para T/R/I/K/E.
- Líneas de tiempo para IGM por sector.
- Gráficos de dispersión (IGM vs. ROI_CS).

La integración de GQM + PRAGMATIC en la hoja `Métricas_TRIKE` permite justificar por qué se usan unas métricas y no otras en los paneles de alto nivel. [web:38][web:45]

---