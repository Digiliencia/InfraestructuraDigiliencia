# Plantilla de Excel para Cálculo de Índice Global de Madurez (IGM) y ROI

> Esta plantilla está pensada para implementarse en Excel (o equivalente) a partir de las respuestas de la encuesta.

## 1. Estructura de hojas

### Hoja 1 – `Respuestas`

Columnas sugeridas:

- A: ID_Organización  
- B: Sector  
- C: Tamaño  
- D: Pregunta  
- E: Respuesta_Texto  
- F: Respuesta_Valor (0–4)  

Cada fila representa una respuesta a una pregunta para una organización.

### Hoja 2 – `Preguntas_Ponderaciones`

Columnas:

- A: Pregunta  
- B: Pilar_GCI (Legal / Technical / Organizational / Capacity / Cooperation)  
- C: Peso_Pilar (ej. 1)  
- D: Peso_Pregunta_en_Pilar (ej. 1)  
- E: Nivel_0_Valor_Mín  
- F: Nivel_1_Valor_Máx  
- G: Nivel_2_Valor_Máx  
- H: Nivel_3_Valor_Máx  
- I: Nivel_4_Valor_Máx  

Aquí se define qué preguntas pertenecen a qué pilar y cómo se traducen las puntuaciones a niveles de madurez.

### Hoja 3 – `IGM_Por_Org`

Columnas:

- A: ID_Organización  
- B: Sector  
- C: Tamaño  
- D: Legal_Score  
- E: Technical_Score  
- F: Organizational_Score  
- G: Capacity_Score  
- H: Cooperation_Score  
- I: IGM_Global (media ponderada)  
- J: Legal_Level (0–4)  
- K: Technical_Level (0–4)  
- L: Organizational_Level (0–4)  
- M: Capacity_Level (0–4)  
- N: Cooperation_Level (0–4)  

Cálculos (ejemplo de fórmulas):

- Para cada pilar, sumar los `Respuesta_Valor` de las preguntas asociadas y dividir entre el máximo posible (normalización).  
- `IGM_Global` = promedio de los cinco pilares (o ponderación personalizada).  

### Hoja 4 – `ROI`

Columnas:

- A: ID_Organización  
- B: Año  
- C: Presupuesto_TI_Total  
- D: Presupuesto_Ciberseguridad  
- E: Incidentes_Mayores (nº/año)  
- F: Coste_Incidentes (estimado, €/año)  
- G: Tiempo_Indisponibilidad_Total (horas/año)  
- H: Valor_Indisponibilidad (€/hora)  
- I: Coste_Indisponibilidad (Fórmula = G * H)  
- J: Coste_Total_Riesgo (F + I)  
- K: IGM_Global (vinculado a Hoja 3)  
- L: Indicador_ROI (ver abajo)

## 2. Cálculo del IGM (Índice Global de Madurez)

Ejemplo de cálculo por pilar (en Excel, pseudofórmulas):

1. En `Respuestas`, asignar a cada respuesta un valor de 0 (mínima madurez) a 4 (máxima).  
2. En `IGM_Por_Org`, para el pilar Legal:
   - `Legal_Score` = SUMA de valores de respuestas de preguntas marcadas como Legal / número de preguntas Legal.  
3. Repetir por pilar.  
4. `IGM_Global` = PROMEDIO(Legal_Score:Cooperation_Score).

## 3. Cálculo de un indicador de ROI

No existe un ROI “oficial” de ciberseguridad, pero se propone un indicador práctico:

- Definir, para cada organización y año:  
  - `Presupuesto_Ciberseguridad` = D  
  - `Coste_Total_Riesgo` = J (suma de costes de incidentes e indisponibilidad).  

- **Indicador_ROI** (orientativo) podría definirse como:

  \[
  \text{ROI\_Ciber} = \frac{\text{Coste\_Total\_Riesgo\_Referencia} - \text{Coste\_Total\_Riesgo\_Año}}{\text{Presupuesto\_Ciberseguridad\_Año}}
  \]

  Donde `Coste_Total_Riesgo_Referencia` puede ser:  
  - El coste medio de incidentes de años previos.  
  - Una estimación basada en benchmarks sectoriales.  

En Excel, si:

- `Coste_Total_Riesgo_Ref` está en columna M,  
- `Coste_Total_Riesgo_Año` en J,  
- `Presupuesto_Ciberseguridad_Año` en D,  

entonces:

- `Indicador_ROI` = `(M - J) / D`

## 4. Visualizaciones recomendadas

En Excel o BI:

- Radar de madurez (5 pilares) por organización.  
- Gráfico de barras comparando IGM por sector.  
- Diagrama de dispersión: `IGM_Global` vs. `Presupuesto_Ciberseguridad` (% TI).  
- Evolución temporal: `Coste_Total_Riesgo` y `Presupuesto_Ciberseguridad` por año.  

Estas visualizaciones permiten relacionar inversión, madurez y impacto, reforzando la lógica de “digital trust” que se observa en las encuestas globales de ciberseguridad.[web:34][web:41]  