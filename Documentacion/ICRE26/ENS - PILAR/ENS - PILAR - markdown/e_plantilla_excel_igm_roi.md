# Plantilla Excel para Cálculo de IGM y ROI de Seguridad (PILAR–ENS)

> Descripción estructurada para implementar una hoja de cálculo que consolide las respuestas de la encuesta, calcule el Índice Global de Madurez (IGM) y sirva de base para estimar el ROI de las inversiones en seguridad.

---

## 1. Estructura general del libro

Se recomienda crear al menos cuatro hojas:

1. `RespuestasEncuesta`  
2. `MapeoPreguntas`  
3. `CalculoIGM`  
4. `ROI_Seguridad`

---

## 2. Hoja `RespuestasEncuesta`

Columnas sugeridas:

- A: Nº pregunta (ej. 2.1, 5.3, 9.1)  
- B: Descripción breve de la pregunta  
- C: Respuesta seleccionada (texto)  
- D: Valor numérico asociado (0–100)  
- E: Comentarios adicionales (opcional)

Las celdas de la columna C pueden implementarse con listas desplegables, y la columna D se calcularía mediante tablas de búsqueda (por ejemplo, usando `BUSCARV` o `XLOOKUP`) apoyadas en la hoja `MapeoPreguntas`.

---

## 3. Hoja `MapeoPreguntas`

Para cada pregunta:

- A: Nº pregunta  
- B: Tipo de escala (L0–L5, 1–5, binaria, etc.)  
- C–G: Correspondencia entre opciones de respuesta y valor numérico (0–100)  
- H: Dimensión IGM asociada (1 a 5)  
- I: Peso relativo de la pregunta dentro de la dimensión  

Ejemplo de fila para una pregunta de madurez L0–L5:

- A: 5.4  
- B: L0–L5  
- C: L0 → 0  
- D: L1 → 10  
- E: L2 → 50  
- F: L3 → 80  
- G: L4 → 90; L5 → 100  
- H: 3 (Madurez de salvaguardas y controles)  
- I: 1 (peso relativo dentro de la dimensión)

Esta hoja actúa como “tabla de verdad” de la encuesta.

---

## 4. Hoja `CalculoIGM`

Secciones principales:

### 4.1 Cálculo de valor por pregunta

Para cada pregunta, se toma el valor numérico de `RespuestasEncuesta!D` y se asigna a la dimensión correspondiente usando el mapeo de `MapeoPreguntas`.

### 4.2 Cálculo de cada dimensión

Para la dimensión \(i\):

- Calcular la suma ponderada de los valores de sus preguntas.  
- Dividir por la suma de los pesos de esas preguntas.

Ejemplo (en pseudofórmula Excel):

- `Dim1 = SUMPRODUCT(ValoresDim1; PesosDim1) / SUM(PesosDim1)`

Repetir para las cinco dimensiones.

### 4.3 Cálculo del IGM

Crear celdas:

- `IGM_D1` a `IGM_D5` (valores 0–100)  
- `Peso_D1` a `Peso_D5` (por defecto 0,2 cada uno, pero configurables)

El IGM se calcula como:

- `IGM_Total = SUMPRODUCT(IGM_D1:IGM_D5; Peso_D1:Peso_D5)`

Se recomienda añadir gráficos de radar o barras para visualizar dimensiones.

---

## 5. Hoja `ROI_Seguridad`

La hoja de ROI debe unir:

- Inversiones realizadas o planificadas.  
- Impacto esperado en el IGM o en dimensiones concretas.  
- Reducción estimada de riesgo (pérdida esperada).  
- Fórmulas de retorno de la inversión.

### 5.1 Tabla de inversiones

Columnas:

- A: Proyecto / medida (ej. “Segmentación de red por dominios”)  
- B: Coste total (CAPEX + OPEX periodo considerado)  
- C: Dimensiones IGM impactadas (ej. 2 y 3)  
- D: Incremento esperado en IGM por dimensión (en puntos)  
- E: Reducción estimada de pérdidas anuales (en euros)  
- F: Periodo de análisis (años)  
- G: ROI %  
- H: Payback (años)

Ejemplo de fórmula de ROI:

- `ROI % = (Beneficio_Neto / Coste) * 100`  
- Donde `Beneficio_Neto = Reducción de pérdidas en el periodo – Coste`.

### 5.2 Escenarios

Se pueden crear rangos de celdas para:

- Escenario conservador, medio y optimista.  
- Variar el incremento esperado de IGM o la reducción de pérdidas.

Gráficos recomendados:

- Barras comparando coste vs. beneficio estimado por proyecto.  
- Dispersión entre incremento de IGM y ROI.

---

## 6. Buenas prácticas para uso del Excel

- Proteger las hojas de mapeo y cálculo para evitar modificaciones accidentales.  
- Documentar en una hoja adicional (`Documentación`) los supuestos principales (por ejemplo, cómo se estima la reducción de pérdidas).  
- Versionar el fichero (v1, v2, …) para mantener trazabilidad de cambios.  
- Usar rangos con nombre para fórmulas complejas.

---

Esta plantilla no pretende agotar todas las posibilidades, pero sí proporcionar una estructura robusta para que la organización pueda:

- Consolidar los resultados de la encuesta.  
- Calcular y seguir el IGM en el tiempo.  
- Vincular inversiones en seguridad con mejoras de madurez y reducción de riesgo.