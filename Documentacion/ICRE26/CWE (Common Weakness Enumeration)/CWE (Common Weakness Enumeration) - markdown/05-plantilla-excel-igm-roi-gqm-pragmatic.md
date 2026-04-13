# Plantilla de Excel para Cálculo de IGM y ROI Integrando GQM + PRAGMATIC

Esta plantilla extiende la hoja de cálculo del IGM (Índice de Gestión de Debilidades) y ROI, incorporando explícitamente la trazabilidad GQM y la evaluación PRAGMATIC de las métricas. [web:24][web:29][web:21]

## 1. Estructura propuesta del libro

Hojas mínimas recomendadas:

1. `Diccionario_Metricas`  
2. `Datos_Encuesta`  
3. `Calculo_IGM`  
4. `Calculo_PRAGMATIC`  
5. `Calculo_ROI`  

---

## 2. Hoja `Diccionario_Metricas`

Columnas sugeridas:

- `ID_Metrica` – Ej. M1.1, M2.1, etc.  
- `Nombre_Corto` – “% vulns CWE Top25”, “Tiempo remediación CWE”, etc.  
- `Descripcion` – Definición exacta de la métrica.  
- `Meta_GQM` – G1, G2, G3, G4.  
- `Pregunta_GQM` – G1Q1, G2Q2, etc.  
- `Unidad` – %, días, índice 0–100, número absoluto, etc.  
- `Fuente_Datos` – CSIRT nacional, encuesta, inventario herramientas, etc.  
- `Escala` – 0–1, 0–100, días, etc.  

Opcionalmente, se pueden añadir:

- `Peso_IGM` – Peso relativo en el cálculo del índice (si se integran varias métricas).  
- `Notas` – Suposiciones, excepciones, etc.

---

## 3. Hoja `Datos_Encuesta`

Similar a la plantilla anterior, pero añadiendo columnas que luego alimenten métricas GQM:

- `ID_Org`  
- `Sector`  
- `Tamano`  
- Respuestas codificadas a las preguntas de la encuesta (ver kit anterior), en particular aquellas que sirven para construir M4.3, M4.4, M8.1, M8.2, etc.  

Para métricas de tipo “nacional” basadas en datos agregados (por ejemplo, M1.1, M2.1, M2.2, M3.1), se pueden usar registros sintéticos o trasladar directamente los resultados agregados a la hoja `Calculo_IGM`.

---

## 4. Hoja `Calculo_IGM`

### 4.1. Diseño

Por filas, se recomienda:

- Una fila por organización (para métricas organizativas).  
- Una fila adicional para “agregados nacionales/sectoriales” (para métricas provenientes de CSIRT, NVD, etc.).

Columnas:

- `ID_Org`  
- Métricas normalizadas (ej. `M1_1_norm`, `M3_1_norm`, etc.)  
- `IGM` – resultado como suma ponderada de métricas normalizadas.  
- `IGM_100` – escala 0–100.

### 4.2. Normalización

Ejemplos:

- Métrica en porcentaje (0–100): `M_norm = M / 100`.  
- Métrica en días (donde menos es mejor):  
  - Definir rango razonable (ej. 0–90 días).  
  - `M_norm = 1 – MIN(M, 90) / 90`.  

### 4.3. Cálculo

Si se usa un subconjunto de métricas para el IGM:

- `IGM = Σ (M_i_norm * Peso_i)`  
- Verificar que `Σ Peso_i = 1`.  

---

## 5. Hoja `Calculo_PRAGMATIC`

Esta hoja permite puntuar cada métrica según los criterios PRAGMATIC y, si se desea, derivar un índice de “calidad de métrica”.

Columnas:

- `ID_Metrica`  
- `P` (0–3)  
- `R` (0–3)  
- `A` (0–3)  
- `G` (0–3)  
- `M` (0–3)  
- `A2` (0–3)  
- `T` (0–3)  
- `I` (0–3)  
- `C` (0–3)  
- `Score_PRAGMATIC` = suma de los nueve criterios (máx. 27).  

Esto permite, por ejemplo:

- Ordenar las métricas por `Score_PRAGMATIC` para seleccionar las más “sanas”. [web:21][web:26]  
- Visualizar la contribución de cada criterio mediante gráficos radar o similares.  

---

## 6. Hoja `Calculo_ROI`

Igual que en la plantilla previa, pero integrando GQM:

Columnas básicas:

- `ID_Org`  
- `IGM_Antes`  
- `IGM_Despues`  
- `Coste_Anual_Incidentes_Antes`  
- `Coste_Anual_Incidentes_Despues`  
- `Inversion`  
- `Ahorro_Anual` = `Coste_Anual_Incidentes_Antes – Coste_Anual_Incidentes_Despues`  
- `ROI` = (`Ahorro_Anual – Inversion`) / `Inversion`  

Columnas opcionales:

- `M3_1_Antes`, `M3_1_Despues` (tiempo de remediación por CWE)  
- `M1_1_Antes`, `M1_1_Despues` (% de vulnerabilidades Top 25)  

Esto permite estudiar, por ejemplo, si una mejora de 10 puntos en IGM se corresponde con un descenso significativo en tiempo de remediación y coste de incidentes, lo que da respaldo económico a las decisiones de inversión.

---

## 7. Visualizaciones recomendadas

En el propio Excel se pueden preparar gráficos listos para exportar a la plantilla de PowerPoint:

- Gráfico de barras: IGM medio por sector.  
- Diagrama de dispersión: IGM vs coste anual de incidentes.  
- Gráfico de líneas: evolución de M1.1 (Top 25) y M3.1 (tiempo de remediación) a lo largo del tiempo.  
- Radar PRAGMATIC por métrica o por grupo de métricas.

---

## 8. Consideraciones finales

La plantilla no pretende ser una cárcel para analistas, sino un esqueleto razonable: permite desde un uso ligero hasta modelos bastante sofisticados. Lo importante es que cada celda con un número lleve detrás una narrativa clara: qué meta nacional sirve, qué pregunta responde y qué tan buena es la métrica según PRAGMATIC.