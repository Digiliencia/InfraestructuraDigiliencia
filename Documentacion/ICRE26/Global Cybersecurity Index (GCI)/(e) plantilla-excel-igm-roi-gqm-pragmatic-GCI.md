# Plantilla de Excel para Cálculo de IGM y ROI Integrando GQM + PRAGMATIC

> Esta plantilla define las hojas y cálculos necesarios para:  
> 1) Transformar respuestas de encuesta en un Índice Global de Madurez (IGM) alineado con GCI y GQM.  
> 2) Relacionar la madurez con inversión y costes para derivar indicadores de ROI.  

## 1. Hojas propuestas

### Hoja 1 – `Respuestas`

Columnas:

- A: ID_Organización  
- B: Sector  
- C: Tamaño  
- D: Pregunta_ID (p.ej. Q2.1.3)  
- E: Pilar_GCI (L/T/O/C/Co)  
- F: Goal_ID (G1.1, G2.1, etc.)  
- G: Respuesta_Texto  
- H: Respuesta_Valor (0–4)  

Cada fila = una respuesta a una pregunta de la encuesta.

### Hoja 2 – `Preguntas_Metricas`

Columnas:

- A: Pregunta_ID  
- B: Métrica_ID (M2.1.3, etc.)  
- C: Descripción_Métrica  
- D: Tipo_Métrica (directa/derivada)  
- E: Peso_en_Pilar (0–1)  
- F: Peso_en_Goal (0–1)  

### Hoja 3 – `Pilares_IGM`

Columnas (una fila por organización):

- A: ID_Organización  
- B: Sector  
- C: Tamaño  
- D: Legal_Score  
- E: Technical_Score  
- F: Organizational_Score  
- G: Capacity_Score  
- H: Cooperation_Score  
- I: IGM_Global  

Cálculos orientativos:

- `Legal_Score` = PROMEDIO de `Respuesta_Valor` para Pregunta_ID con Pilar_GCI = "L".  
- Igual para el resto de pilares.  
- `IGM_Global` = PROMEDIO(D:H) o promedio ponderado si se ajustan pesos por pilar.

### Hoja 4 – `PRAGMATIC_Metricas`

Columnas:

- A: Métrica_ID  
- B: P (Predictivo, 1–5)  
- C: R (Relevante, 1–5)  
- D: A (Accionable, 1–5)  
- E: G (Genuino, 1–5)  
- F: M (Significativo, 1–5)  
- G: Ac (Preciso, 1–5)  
- H: T (Oportuno, 1–5)  
- I: I (Independiente, 1–5)  
- J: C (Rentable, 1–5)  
- K: Puntuación_Media_PRAGMATIC (PROMEDIO(B:J))  

Uso sugerido:

- Filtrar métricas con Puntuación_Media_PRAGMATIC ≥ 3,5 para priorizar su uso en cuadros de mando.

### Hoja 5 – `ROI_Ciber`

Columnas:

- A: ID_Organización  
- B: Año  
- C: Presupuesto_TI_Total  
- D: Presupuesto_Ciberseguridad  
- E: %_TI_en_Ciber (D/C)  
- F: IGM_Global (vinculado a `Pilares_IGM`)  
- G: Coste_Incidentes (€/año)  
- H: Coste_Indisponibilidad (€/año)  
- I: Coste_Total_Riesgo (G + H)  
- J: Coste_Total_Riesgo_Referencia (media de años anteriores o benchmark)  
- K: ROI_Ciber  

Fórmula sugerida para ROI_Ciber:

\[
\text{ROI\_Ciber} = \frac{\text{Coste\_Total\_Riesgo\_Referencia} - \text{Coste\_Total\_Riesgo}}{\text{Presupuesto\_Ciberseguridad}}
\]

En Excel, si:

- `Coste_Total_Riesgo_Referencia` en J2  
- `Coste_Total_Riesgo` en I2  
- `Presupuesto_Ciberseguridad` en D2  

entonces:

- `ROI_Ciber` (K2) = `(J2 - I2) / D2`

### Hoja 6 – `Dashboards`

- Gráficos radar por organización (5 pilares).  
- Gráficos de barras: IGM por sector.  
- Dispersión: `IGM_Global` vs `%_TI_en_Ciber`.  
- Tendencias: `Coste_Total_Riesgo` vs. `IGM_Global` por año.  

## 2. Integración con GQM

Las columnas `Goal_ID` y `Pilar_GCI` permiten:

- Analizar la contribución de cada métrica a objetivos concretos (ej. G2.1).  
- Agrupar resultados no solo por pilar, sino por objetivos nacionales/sectoriales.  

Ejemplo:

- Tabla dinámica que muestre, por Goal_ID, la media de IGM de las métricas asociadas.  

## 3. Integración con PRAGMATIC

La hoja `PRAGMATIC_Metricas` se usa para:

- Filtrar las métricas **recomendadas** (alta puntuación PRAGMATIC).  
- Documentar por qué se elige una métrica y no otra cuando hay redundancias.  

En cuadros de mando, se puede:

- Usar iconos o colores que indiquen el nivel PRAGMATIC de cada métrica clave.  

## 4. Buenas prácticas de implementación

- Validar fórmulas con un conjunto reducido de organizaciones piloto.  
- Mantener un diccionario de datos (fuente, periodicidad, responsable de cada métrica).  
- Revisar el catálogo de métricas cada 1–2 años a la luz de cambios normativos y de GCI.[web:20][web:40][web:41]  