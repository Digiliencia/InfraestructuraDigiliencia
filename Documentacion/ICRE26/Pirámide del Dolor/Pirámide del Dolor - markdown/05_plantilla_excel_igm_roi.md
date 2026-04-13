# Plantilla de Excel para Cálculo de IGM y ROI
## Índice Global de Madurez (IGM) y Retorno de la Inversión (ROI) de Detección Basada en la Pirámide del Dolor

Esta plantilla está pensada para implementarse en una hoja de cálculo (Excel, LibreOffice, etc.) a partir de las respuestas de la encuesta. No pretende ser un modelo financiero exhaustivo, sino una herramienta pragmática para convertir la narrativa de la Pirámide del Dolor en números manejables.

---

## 1. Estructura general de la hoja

Se recomienda un libro de Excel con las siguientes hojas:

1. `Datos_Encuesta` – codificación de respuestas.  
2. `Ponderaciones` – pesos por pregunta y nivel de la Pirámide.  
3. `IGM` – cálculo del Índice Global de Madurez y subíndices.  
4. `ROI` – estimación de beneficios vs costes.  
5. `Resumen` – vista ejecutiva (para alimentar el PowerPoint).

---

## 2. Hoja `Datos_Encuesta`

Columnas sugeridas (fila 1 como cabecera):

- A: ID_Organización  
- B: Sector  
- C: Tamaño (categoría)  
- D: País / Región (si procede)  
- E…: Una columna por pregunta de la encuesta (P2_1, P2_2, … P9_4)

Codificación de respuestas:

- Para cada opción de respuesta, asignar un valor numérico de madurez (0, 1, 2, 3, …) acordado previamente.  
- Ejemplo: en P5_4 (“¿Dispone de métricas de cobertura ATT&CK?”)  
  - “No, no se dispone” → 0  
  - “Se ha intentado, pero sin sistematización” → 1  
  - “Parcialmente” → 2  
  - “Sí, métricas cuantificadas” → 3

Es recomendable mantener una tabla auxiliar de correspondencia respuesta → valor.

---

## 3. Hoja `Ponderaciones`

Objetivo: asignar a cada pregunta un peso y una vinculación a uno o varios niveles de la Pirámide del Dolor.

Columnas sugeridas:

- A: ID_Pregunta (ej. P3_1)  
- B: Bloque (3 – IoC bajo nivel, etc.)  
- C: Nivel_Piramide (IoC_bajo, Artefactos, TTP, Gobernanza)  
- D: Peso_Pregunta (0–1, o 0–100)  
- E: Comentario

Ejemplo de filas:

- P3_1 → Bloque 3, Nivel IoC_bajo, Peso 0,5  
- P4_1 → Bloque 4, Nivel Artefactos, Peso 0,8  
- P5_4 → Bloque 5, Nivel TTP, Peso 1,0  
- P6_1 → Bloque 6, Nivel Gobernanza, Peso 0,7  

Las ponderaciones pueden ajustarse según prioridades (por ejemplo, dar más peso a TTP en sectores críticos).

---

## 4. Hoja `IGM` – Índice Global de Madurez

### 4.1 Cálculo de subíndices por nivel de la Pirámide

Para cada organización (fila), calcular:

- **IGM_IoC** – Madurez en indicadores de bajo nivel.  
- **IGM_Artefactos** – Madurez en detecciones basadas en artefactos de red/host.  
- **IGM_TTP** – Madurez en TTP y comportamiento.  
- **IGM_Gobernanza** – Madurez en métricas y gobernanza.

Esquema de fórmula genérica (ejemplo, en pseudofórmula):

IGM_IoC =  
\[
\frac{\sum (Valor_Respuesta_Pi * Peso_Pi) \text{ para todas las Pi de nivel IoC}}{\sum Peso_Pi \text{ para todas las Pi de nivel IoC}}
\]

En Excel, asumiendo que:

- Las respuestas numéricas están en la hoja `Datos_Encuesta`.  
- Las ponderaciones y niveles están en `Ponderaciones`.

Puede implementarse con funciones como `SUMPRODUCT` y rangos filtrados por nivel (mediante tablas dinámicas o columnas auxiliares).

### 4.2 Normalización

Se recomienda normalizar cada subíndice a una escala 0–100:

IGM_IoC_Normalizado = (IGM_IoC / Valor_Máximo_Potencial_IoC) * 100

Donde `Valor_Máximo_Potencial_IoC` es el máximo teórico (por ejemplo, 3 si la escala de cada pregunta va de 0 a 3, ponderado por pesos).

Repetir para Artefactos, TTP y Gobernanza.

### 4.3 Cálculo del IGM global

Definir un peso relativo para cada subíndice, por ejemplo:

- IoC_bajo: 20%  
- Artefactos: 30%  
- TTP: 30%  
- Gobernanza: 20%

IGM_Global =  
= IGM_IoC_N * 0,2 + IGM_Artefactos_N * 0,3 + IGM_TTP_N * 0,3 + IGM_Gobernanza_N * 0,2

Los pesos pueden modificarse, pero es deseable reflejar cierta preferencia por capas superiores de la Pirámide.

---

## 5. Hoja `ROI` – Estimación de Retorno de la Inversión

La idea aquí no es construir un modelo financiero perfecto, sino vincular la mejora en detecciones de alto nivel con beneficios tangibles.

### 5.1 Datos de entrada

Columnas sugeridas:

- Coste_Anual_SOC (en moneda local)  
- Coste_Anual_Herramientas (licencias, servicios gestionados)  
- Coste_Anual_Incidentes (histórico estimado: pérdida de negocio, recuperación, multas, etc.)  
- Número_Medio_Incidentes_Graves_Año  
- Tiempo_Medio_Analista_por_Incidente (horas)  
- Costo_Hora_Analista

### 5.2 Variables derivadas

- Coste_Operativo_Analistas = Número_Medio_Incidentes_Graves_Año * Tiempo_Medio_Analista_por_Incidente * Costo_Hora_Analista  
- Coste_Total_Actual = Coste_Anual_SOC + Coste_Anual_Herramientas + Coste_Operativo_Analistas + Coste_Anual_Incidentes

### 5.3 Impacto de la mejora en TTP / niveles altos

Suponga:

- Mejora_TTP = incremento en puntos del subíndice IGM_TTP (por ejemplo, de 40 a 60).  
- Reducción_Porcentual_Incidentes = factor estimado (ej. 20%).  
- Reducción_Porcentual_Tiempo_Analista = factor estimado (ej. 15%).

Variables:

- Nuevos_Incidentes_Graves_Año = Número_Medio_Incidentes_Graves_Año * (1 – Reducción_Porcentual_Incidentes)  
- Nuevo_Tiempo_Medio_Analista = Tiempo_Medio_Analista_por_Incidente * (1 – Reducción_Porcentual_Tiempo_Analista)  
- Nuevo_Coste_Operativo_Analistas = Nuevos_Incidentes_Graves_Año * Nuevo_Tiempo_Medio_Analista * Costo_Hora_Analista  
- Nuevo_Coste_Anual_Incidentes = Coste_Anual_Incidentes * (1 – Reducción_Porcentual_Incidentes)  
- Coste_Total_Nuevo = Coste_Anual_SOC + Coste_Anual_Herramientas + Nuevo_Coste_Operativo_Analistas + Nuevo_Coste_Anual_Incidentes

### 5.4 Cálculo de ROI

Si el esfuerzo para mejorar TTP implica una inversión adicional (por ejemplo, un nuevo proyecto de detección avanzada):

- Inversión_Adicional_Anual (columna específica).  

Entonces:

- Ahorro_Anual = Coste_Total_Actual – Coste_Total_Nuevo  
- ROI = (Ahorro_Anual – Inversión_Adicional_Anual) / Inversión_Adicional_Anual

El ROI puede expresarse en porcentaje:

- ROI_% = ROI * 100

Se recomienda jugar con escenarios (pesimista, conservador, optimista) variando los factores de reducción de incidentes y tiempo de analista.

---

## 6. Hoja `Resumen`

Incluir gráficos y tablas clave:

- Radar o barras con los subíndices IGM (IoC, Artefactos, TTP, Gobernanza).  
- Evolución temporal si se repite la encuesta.  
- Comparación con sector (si hay datos agregados).  
- Gráfico del ROI estimado vs escenario “no hacer nada”.

Esta hoja será la fuente principal para construir el Reporte Ejecutivo en PowerPoint.

---

## 7. Buenas prácticas al usar la plantilla

- No atribuir a las cifras una precisión que no tienen: es un modelo de decisión, no de contabilidad.  
- Documentar los supuestos utilizados (por ejemplo, estimaciones de reducción de incidentes).  
- Revisar anualmente las ponderaciones y los factores de impacto, para reflejar cambios en la amenaza y el entorno regulatorio.

Si, después de todo, el ROI sale negativo, quizá no sea que la detección avanzada no compense, sino que los datos de partida subestiman el coste real de cada incidente. Eso, en sí mismo, ya es un hallazgo.