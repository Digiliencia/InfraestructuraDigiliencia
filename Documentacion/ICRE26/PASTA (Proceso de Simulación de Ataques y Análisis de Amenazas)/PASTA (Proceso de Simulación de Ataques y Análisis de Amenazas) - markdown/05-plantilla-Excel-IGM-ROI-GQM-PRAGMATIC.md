# Plantilla de Excel – IGM y ROI basados en GQM + PRAGMATIC
## Integración de métricas PASTA+STRIDE a nivel organización/sector

### 1. Estructura propuesta de hojas

1. `CATALOGO_METRICAS`  
2. `PONDERACIONES_PRAGMATIC`  
3. `DATOS_ORGANIZACIONES`  
4. `CALCULO_IGM`  
5. `CALCULO_ROI`  
6. `PARAMETROS`  
7. `GLOSARIO`

### 2. Hoja `CATALOGO_METRICAS`

Columnas sugeridas:

- `ID_Metrica` (ej. M1.1, M4.1)  
- `Nombre_Corto`  
- `Descripcion`  
- `Objetivo_GQM` (G1, G2, G3, G4)  
- `Fuente_Datos` (encuesta, registro de incidentes, etc.)  
- `Unidad` (% , nº incidentes, horas, etc.)  

Registrar aquí las métricas priorizadas tras evaluación PRAGMATIC.[web:50][web:52][web:58]

### 3. Hoja `PONDERACIONES_PRAGMATIC`

Columnas:

- `ID_Metrica`  
- `P` `R` `A` `G` `M` `C` `T` `I` `$` (1–5)  
- `Score_PRAGMATIC` (p.ej. suma o media de los 9 criterios)  
- `Peso_en_IGM` (0–1)

Reglas sugeridas:

- Normalizar `Score_PRAGMATIC` para convertirlo en peso inicial.  
- Ajustar manualmente pesos en `Peso_en_IGM` para reflejar prioridades estratégicas (por ejemplo, dar peso extra a M4.1 y M5.3).  

### 4. Hoja `DATOS_ORGANIZACIONES`

Formato con cada fila = una organización (o una organización-año):

- `ID_Org`  
- `Sector`  
- `Ano`  
- Columnas para cada métrica seleccionada: `M1_1`, `M1_2`, `M1_3`, `M2_1_S`, etc.  

Valores numéricos en las unidades definidas (porcentaje, número, horas).

### 5. Hoja `CALCULO_IGM`

Objetivo: producir un Índice Global de Madurez (IGM) por organización.

Pasos:

1. Normalizar cada métrica a escala 0–100.  
   - p.ej. para M1.1 (porcentaje) se puede usar directo: `M1_1_norm = MIN(100, MAX(0, M1_1))`.  
   - para MTTR (M4.1) conviene transformar: menor MTTR = mejor puntuación; por ejemplo:  
     `M4_1_norm = MAX(0, MIN(100, 100 * (1 – (MTTR / MTTR_objetivo_max))))`.

2. Calcular score parcial de cada métrica:  
   `Score_Metrica = Valor_Normalizado * Peso_en_IGM`.

3. Sumar para obtener IGM por organización:

```text
IGM = SUMA(Score_Metrica para todas las métricas seleccionadas)
```

Opcional:  
– Desglosar por objetivos G1–G4 creando sub-índices `IGM_G1`, `IGM_G2`, etc., usando sólo métricas asignadas a cada objetivo.

### 6. Hoja `CALCULO_ROI`

Objetivo: aproximar un ROI a partir de:

- Cambios en IGM (y, por extensión, en riesgo estimado).  
- Inversión en capacidades relacionadas (modelado de amenazas, simulaciones, etc.).[web:51]

Columnas por organización:

- `IGM_Baseline` (año 0)  
- `IGM_Actual` (año n)  
- `Delta_IGM` = `IGM_Actual – IGM_Baseline`  
- `Riesgo_Anual_Baseline` (€)  
- `Coef_Reduccion_Riesgo_por_IGM` (parámetro, p.ej. 0,02 por cada punto de IGM)  
- `Riesgo_Anual_Actual` = `Riesgo_Anual_Baseline * (1 – Coef * Delta_IGM)` (con límites 0–Riesgo_Baseline)  
- `Inversion_Total` en periodo (€)  
- `Ahorro_Anual_Estimado` = `Riesgo_Anual_Baseline – Riesgo_Anual_Actual`  
- `ROI` (%) = `(Ahorro_Anual_Estimado – Inversion_Total) / Inversion_Total * 100`

Advertencias:

- El coeficiente de reducción de riesgo por punto de IGM es una hipótesis que debe calibrarse con datos históricos y literatura de riesgo.[web:48][web:49][web:54]  
- La estimación de “Riesgo_Anual_Baseline” debe basarse, idealmente, en escenarios PASTA y métodos de riesgo (por ejemplo, L * I, pérdidas anualizadas, etc.).[web:18][web:48]

### 7. Hoja `PARAMETROS`

Incluir:

- Listado de sectores y sus MTTR objetivo máximos (por ejemplo, salud < X horas, energía < Y horas, etc.).  
- Coeficientes de reducción de riesgo por Delta_IGM, por sector.  
- Pesos globales por objetivo G1–G4 si se quieren índices específicos.

### 8. Hoja `GLOSARIO`

Definir:

- IGM, G1–G4.  
- Cada métrica M1–M5.  
- PRAGMATIC y su propósito.  
- Limitaciones: sesgos de datos, dependencia de auto-reporte, etc.

Con esta plantilla, Excel se convierte en algo más que una tabla infinita: se convierte en una calculadora disciplinada que respeta los objetivos, se hace las preguntas adecuadas y no se enamora de cualquier métrica que pase por delante.