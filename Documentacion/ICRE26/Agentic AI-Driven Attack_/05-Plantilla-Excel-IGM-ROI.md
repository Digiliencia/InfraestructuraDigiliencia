# Plantilla de Excel para cálculo de IGM y ROI de Agentic IA

## 1. Estructura de la hoja “Respuestas”

Columnas sugeridas:

- A: Nº de pregunta  
- B: Dimensión (Gobernanza, Métricas, etc.)  
- C: Respuesta seleccionada (texto)  
- D: Puntuación (0–4)  
- E: Comentarios cualitativos  

Cada fila corresponde a una pregunta de la encuesta.

## 2. Hoja “Ponderaciones”

Columnas:

- A: Dimensión  
- B: Peso (%)  

Ejemplo de pesos (personalizable):

- Uso de Agentic IA – 10  
- Gobernanza – 20  
- Datos y memoria – 15  
- Métricas Agentic – 20  
- SOC – 15  
- Cumplimiento – 10  
- Cultura – 5  
- Incidentes / Estrategia – 5  

## 3. Hoja “IGM”

### 3.1. Cálculo de IGM por dimensión

Supongamos:

- En “Respuestas”, columna B contiene la dimensión, columna D la puntuación.  
- En “Ponderaciones”, columna A la dimensión, columna B el peso.

Para cada dimensión (por ejemplo, “Gobernanza”), se puede calcular:

- Promedio de puntuación:  
  - `=PROMEDIO.SI(Respuestas!$B:$B;"Gobernanza";Respuestas!$D:$D)`

- IGM parcial ponderado:  
  - Si el peso está en `Ponderaciones!B2`:  
  - `=PROMEDIO.SI(Respuestas!$B:$B;"Gobernanza";Respuestas!$D:$D) * Ponderaciones!B2 / 4`

> Nota: Se divide por 4 porque 4 es el nivel máximo de madurez.

### 3.2. IGM global

En una celda (por ejemplo, `IGM!B10`):

- `=SUMA(IGM!B2:IGM!B9)`

Esta fórmula suma los IGM parciales ponderados de todas las dimensiones.

## 4. Hoja “ROI”

### 4.1. Variables sugeridas

Columnas:

- A: Concepto  
- B: Valor antes de Agentic IA  
- C: Valor después de Agentic IA  
- D: Diferencia  
- E: Valor monetario estimado  

Filas de ejemplo:

- F1: MTTT medio (minutos).  
- F2: TTC medio para incidentes Agentic (minutos).  
- F3: Nº anual de incidentes de seguridad.  
- F4: Nº anual de incidentes evitados (estimados).  
- F5: Coste medio de incidente (€).  
- F6: Horas mensuales ahorradas en triage de alertas.  
- F7: Coste/hora del analista (€).  

### 4.2. Fórmulas de ejemplo

- Diferencia:  
  - `D2 = B2 - C2` (reducción de MTTT).  
- Ahorro anual por reducción de incidentes:  
  - `E4 = D4 * F5` (incidentes evitados × coste medio).  
- Ahorro anual por automatización de triage:  
  - `E6 = D6 * F7 * 12` (horas ahorradas × coste/hora × 12 meses).  

- ROI anual aproximado (en €):  
  - Si en `E10` se suman todos los ahorros (`=SUMA(E4:E9)`), y en `E11` se recogen los costes anuales de plataformas y proyectos de Agentic IA:  
  - `ROI = E10 - E11`  

Opcional: crear una celda de ROI (%):  
- `=SI(E11>0; (E10 - E11) / E11; "")`

## 5. Hoja “Dashboard”

Incluir gráficos de:

- IGM global y por dimensión (barras).  
- Evolución temporal (si se repite la encuesta).  
- ROI anual en € y %.  

La plantilla puede replicarse para varias organizaciones, permitiendo comparativas sectoriales.
