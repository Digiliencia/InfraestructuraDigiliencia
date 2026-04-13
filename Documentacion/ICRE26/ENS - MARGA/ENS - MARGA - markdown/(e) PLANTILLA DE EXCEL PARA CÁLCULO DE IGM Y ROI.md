# (e) PLANTILLA DE EXCEL PARA CÁLCULO DE IGM Y ROI (DESCRIPCIÓN EN MARKDOWN)

## 1. Estructura general del libro de Excel

Se propone un libro con las siguientes hojas:

1. `Datos_Encuesta` – captura estructurada de las respuestas.  
2. `Codificacion` – tabla de correspondencia entre respuestas y valores numéricos.  
3. `IGM_Calculo` – cálculo del Índice Global de Madurez (IGM) y subíndices.  
4. `ROI_Calculo` – estimaciones de riesgo, pérdidas evitadas y ROI.  
5. `Reportes` – tablas y gráficos resumen para uso ejecutivo.

---

## 2. Hoja `Datos_Encuesta`

Columnas sugeridas (una fila por organización encuestada):

- `ID_Org` – identificador anónimo de la organización.  
- `Sector` – sector (de la pregunta 2).  
- `Tamano` – tamaño (pregunta 3).  
- `Tipo_Entidad` – tipo (pregunta 1).  
- `P5` ... `P57` – columnas que recogen la opción marcada en cada pregunta.

Ejemplo de codificación textual:

- `P5 = "Doc_Formal_Aprobado"`  
- `P27 = "7_30_dias"`  
- etc.

---

## 3. Hoja `Codificacion`

En esta hoja se definen tablas de equivalencia, por ejemplo:

### 3.1. Ejemplo de codificación de madurez (0–4)

| Pregunta | Opción de respuesta                                 | Código numérico |
|----------|-----------------------------------------------------|-----------------|
| P5       | No                                                  | 0               |
| P5       | En elaboración                                      | 1               |
| P5       | Sí, parcial                                         | 2               |
| P5       | Sí, formalmente documentado y aprobado              | 3               |

El mismo esquema puede ampliarse a una escala 0–4 o 0–5 según la granularidad deseada. Las tablas se usan en `IGM_Calculo` mediante funciones de búsqueda (BUSCARV/XLOOKUP).

### 3.2. Codificación de tiempos (MTTD, MTTR)

| Pregunta | Respuesta        | Código (puntuación) |
|----------|------------------|---------------------|
| P30/P31  | Semanas          | 0                   |
| P30/P31  | Días             | 1                   |
| P30/P31  | Horas            | 2                   |
| P30/P31  | Minutos          | 3                   |

---

## 4. Hoja `IGM_Calculo`

### 4.1. Subíndices de madurez

Para cada bloque se define un subíndice entre 0 y 100, calculado a partir de las preguntas relevantes:

- `Gov_ENS` – Gobernanza ENS y adecuación (P5–P13).  
- `Riesgo_Indicadores` – Riesgos e indicadores (P14–P19).  
- `Ciberresiliencia_IMC` – Uso del modelo IMC (P20–P25).  
- `Operacion` – Eficacia operativa (P26–P34).  
- `Arquitectura_ZT` – Zero Trust (P35–P39).  
- `Cultura_Formacion` – Formación y concienciación (P40–P42).  
- `Continuidad` – Continuidad y recuperación (P43–P45).  
- `Economia_Riesgo` – Riesgo económico, IGM y ROI (P46–P51).

Para cada subíndice:

```text
Subindice = (SUMA de puntuaciones codificadas / Puntuación máxima posible) * 100
```

### 4.2. Índice Global de Madurez (IGM)

Se propone una fórmula ponderada (ajustable):

```text
IGM = 0,15 * Gov_ENS
    + 0,15 * Riesgo_Indicadores
    + 0,15 * Ciberresiliencia_IMC
    + 0,15 * Operacion
    + 0,10 * Arquitectura_ZT
    + 0,10 * Cultura_Formacion
    + 0,10 * Continuidad
    + 0,10 * Economia_Riesgo
```

Las ponderaciones reflejan que gobernanza, riesgos, ciberresiliencia y operación son pilares ligeramente superiores, sin despreciar cultura, arquitectura y economía. Pueden adaptarse a escenarios sectoriales.

### 4.3. Clasificación por niveles

Con el IGM (0–100) se pueden definir rangos, por ejemplo:

- 0–25: Nivel I – Inicial  
- 26–50: Nivel II – Básico  
- 51–70: Nivel III – Intermedio  
- 71–85: Nivel IV – Avanzado  
- 86–100: Nivel V – Optimizado

Esta clasificación es útil para gráficos y comparaciones.

---

## 5. Hoja `ROI_Calculo`

### 5.1. Variables de entrada

Añadir a `Datos_Encuesta` o replicar en esta hoja:

- `Presupuesto_TI_Total` – gasto anual TI estimado.  
- `Presupuesto_Ciberseguridad` – gasto anual en ciberseguridad.  
- `Perdida_Anual_Actual` – estimación de pérdidas anuales por incidentes (si existe).  
- `Perdida_Anual_Historica` – referencia de años anteriores (si existe).  

Si la encuesta no recoge estos valores cuantitativos, se pueden incorporar mediante una fase posterior o un módulo adicional.

### 5.2. Cálculos básicos

1. **Porcentaje de gasto en ciberseguridad:**

```text
Pct_Ciber = Presupuesto_Ciberseguridad / Presupuesto_TI_Total
```

2. **Estimación de pérdidas evitadas** (simplificada):

Si existe un periodo histórico con mayor número de incidentes/pérdidas y se supone que parte de la mejora en IGM ha contribuido a reducirlas, se puede aproximar:

```text
Perdida_Evitada = Perdida_Anual_Historica - Perdida_Anual_Actual
```

(limitar a ≥ 0 para evitar valores negativos si la tendencia es inversa).

3. **Estimación de ROI de ciberseguridad (a muy alto nivel):**

```text
ROI = (Perdida_Evitada - Presupuesto_Ciberseguridad) / Presupuesto_Ciberseguridad
```

Interpretación:

- `ROI > 0`: la reducción de pérdidas estimada supera la inversión.  
- `ROI ≈ 0`: equilibrio (no necesariamente malo si el riesgo habría crecido sin inversión).  
- `ROI < 0`: o bien la inversión no se ha traducido en reducción de pérdidas, o bien el horizonte temporal es insuficiente.

### 5.3. Vinculación IGM–ROI

Aunque no se recomienda una correlación simplista, se puede analizar:

- Gráficos de dispersión IGM vs. Pérdida_Anual_Actual.  
- Segmentación por rango de IGM y media de pérdidas.  

Esto no “demuestra” causalidad, pero ayuda a contar una historia coherente: organizaciones con mayor madurez tienden a sufrir menos impacto (o a gestionarlo mejor).

---

## 6. Hoja `Reportes`

Elementos sugeridos:

- Tabla resumen por organización: IGM y subíndices.  
- Gráficos de barras por sector (IGM medio por sector).  
- Histogramas de distribución de IGM.  
- Gráficos de dispersión IGM vs. Pérdida_Anual_Actual, % gasto en ciberseguridad, etc.

El objetivo es generar material directamente reutilizable en el reporte ejecutivo descrito en (f).

---

## 7. Consideraciones metodológicas

- Los códigos numéricos deben ser coherentes con la lógica de madurez (0 = ausencia, máximo = situación deseable).  
- La traducción de respuestas textuales a números debe mantenerse documentada para asegurar replicabilidad y comparabilidad.  
- Cualquier análisis de ROI debe tratarse con prudencia: es preferible hablar de “indicadores de eficiencia” que de fórmulas mágicas.

Esta plantilla pretende ser un esqueleto: el músculo vendrá de los datos reales y del juicio experto.