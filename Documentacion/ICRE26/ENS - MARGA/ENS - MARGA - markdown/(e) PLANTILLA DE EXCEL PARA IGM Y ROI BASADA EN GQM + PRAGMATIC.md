# (e) PLANTILLA DE EXCEL PARA IGM Y ROI BASADA EN GQM + PRAGMATIC

## 1. Hojas propuestas

1. `Metas_GQM` – listado de metas, preguntas y métricas MARGA‑ENS.  
2. `Datos_Encuesta` – respuestas de la encuesta (igual que antes).  
3. `Codificacion_Metricas` – traducción de respuestas a valores numéricos Mx.y.z.  
4. `PRAGMATIC_Scores` – puntuaciones P,R,A,G,M,A(c),T,I,C para cada métrica.  
5. `IGM_Calculo` – cálculo de subíndices e IGM, ponderando métricas según PRAGMATIC.  
6. `ROI_Calculo` – cálculos de pérdida esperada, pérdida evitada y ROI.  
7. `Reportes` – tablas y gráficos para el reporte ejecutivo.

---

## 2. Hoja `Metas_GQM`

Tabla con columnas:

- `Meta_ID` – G1, G2, etc.  
- `Meta_Descripcion` – texto de la meta.  
- `Pregunta_ID` – Qx.y.  
- `Pregunta_Descripcion` – texto de la pregunta.  
- `Metrica_ID` – Mx.y.z.  
- `Metrica_Descripcion`.

Estos datos se derivan del marco integrativo (documento (a)).

---

## 3. Hoja `Codificacion_Metricas`

Para cada Mx.y.z, definir:

- Tipo de métrica (porcentaje, escala 0–3, tiempo, €).  
- Regla de codificación desde las respuestas de `Datos_Encuesta`.

Ejemplo simplificado:

| Metrica_ID | Pregunta_encuesta | Respuesta_encuesta                        | Valor_numerico |
|-----------|-------------------|-------------------------------------------|----------------|
| M1.1.a    | P7                | 0–25 %                                    | 0.25           |
| M1.1.a    | P7                | 26–50 %                                   | 0.5            |
| M1.1.a    | P7                | 51–75 %                                   | 0.75           |
| M1.1.a    | P7                | 76–95 %                                   | 0.9            |
| M1.1.a    | P7                | 96–100 %                                  | 1.0            |

La hoja se utilizará con BUSCARV/XLOOKUP para convertir respuestas en valores.

---

## 4. Hoja `PRAGMATIC_Scores`

Tabla con columnas:

- `Metrica_ID`  
- `P` – Predictive (0–3)  
- `R` – Relevant  
- `A` – Actionable  
- `G` – Genuine  
- `M` – Meaningful  
- `Ac` – Accurate  
- `T` – Timely  
- `I` – Independent  
- `C` – Cost‑effective  
- `Score_Total` – suma P+R+…+C  
- `Peso_PRAGMATIC` – opcional (p. ej. Score_Total / 27)

Se pueden precargar los valores de la matriz del documento (b) y ajustarlos en función del contexto.

---

## 5. Hoja `IGM_Calculo`

### 5.1. Subíndices por meta GQM

Para cada organización (fila):

1. Calcular las métricas Mx.y.z a partir de `Datos_Encuesta` + `Codificacion_Metricas`.  
2. Asociar cada métrica a una meta GQM (G1–G7).  
3. Calcular un subíndice de madurez por meta, ponderando por el peso PRAGMATIC:

```text
Subindice_G1 =
   SUMA( Valor_normalizado_M1.* * Peso_PRAGMATIC_M1.* ) 
 / SUMA( Peso_PRAGMATIC_M1.* )
```

Hacer lo mismo para G2…G7.

### 5.2. IGM global

Definir pesos por meta (por ejemplo):

- G1, G2, G3: 0,15 cada una  
- G4, G5, G6: 0,12 cada una  
- G7: 0,09  

Y calcular:

```text
IGM = 0,15*G1 + 0,15*G2 + 0,15*G3
    + 0,12*G4 + 0,12*G5 + 0,12*G6
    + 0,09*G7
```

Cada Gx es un valor de 0 a 100, obteniendo un IGM de 0 a 100.

---

## 6. Hoja `ROI_Calculo`

### 6.1. Entradas

- `Presupuesto_TI_Total`  
- `Presupuesto_Ciberseguridad`  
- `Perdida_Anual_Actual`  
- `Perdida_Anual_Base` (año base)  

### 6.2. Cálculos

1. Porcentaje de gasto en ciberseguridad:

```text
Pct_Ciber = Presupuesto_Ciberseguridad / Presupuesto_TI_Total
```

2. Pérdida evitada:

```text
Perdida_Evitada = MAX(0; Perdida_Anual_Base - Perdida_Anual_Actual)
```

3. ROI:

```text
ROI = (Perdida_Evitada - Presupuesto_Ciberseguridad) / Presupuesto_Ciberseguridad
```

4. Análisis conjunto con IGM:

- Tabla cruzada con IGM, Pct_Ciber y ROI.  
- Gráficos de dispersión IGM vs. ROI.

---

## 7. Hoja `Reportes`

Preparar gráficos:

- Barras por meta GQM (G1–G7) y sector.  
- Distribución de IGM global.  
- IGM vs. ROI.  
- Subíndices con pesos PRAGMATIC (indicando qué metas se basan en métricas más robustas).

Esta plantilla mantiene la esencia del Excel anterior, añadiendo trazabilidad explícita GQM y ponderación PRAGMATIC.