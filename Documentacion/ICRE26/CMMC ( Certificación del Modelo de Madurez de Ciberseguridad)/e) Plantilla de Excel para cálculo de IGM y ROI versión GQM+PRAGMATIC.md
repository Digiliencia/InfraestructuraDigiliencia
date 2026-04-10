# Plantilla Excel para Cálculo de IGM y ROI (Versión GQM + PRAGMATIC)

> Esta plantilla extiende la anterior incorporando campos para Objetivos GQM y puntuaciones PRAGMATIC por métrica.

---

## 1. Hojas recomendadas

1. `Respuestas` – Respuestas a la encuesta (igual que antes).  
2. `Ponderaciones` – Puntuación de respuestas, pesos por bloque.  
3. `GQM_Metrics` – Catálogo de métricas con su G, Q, M.  
4. `PRAGMATIC` – Puntuación de calidad por métrica.  
5. `IGM` – Cálculo de índice global y parciales.  
6. `ROI` – Cálculo de retorno de inversión.  
7. `Dashboards` – Cuadros de mando.

---

## 2. Hoja “GQM_Metrics”

Columnas sugeridas:

| ID_Métrica | Objetivo_G | Pregunta_Q | Fórmula_M | Unidad | Bloque | Referencias_normativas |
| --- | --- | --- | --- | --- | --- | --- |

Ejemplos:

- `M1_%_Cuentas_criticas_MFA`, Objetivo G1 (control de accesos críticos), etc.  
- `M2_MTTP_critico`, Objetivo G2 (ventana de exposición).  
- `M3_MTTD_incidentes`, Objetivo G3 (detección temprana), etc.

Esto documenta el “por qué” de cada métrica en el propio Excel.

---

## 3. Hoja “PRAGMATIC”

Columnas:

| ID_Métrica | Nombre | P | R | A | G | M | A_c | T | I | C | Total | Usar_en_IGM (Sí/No) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

El campo `Usar_en_IGM` permite excluir del cálculo global aquellas métricas con baja calidad PRAGMATIC (por ejemplo, Total < 30).

---

## 4. Hoja “IGM”

Igual que en la versión anterior, pero:

- Se puede construir el IGM sólo a partir de métricas con `Usar_en_IGM = Sí`.  
- Se puede calcular un “IGM_AltaCalidad” frente a “IGM_Completo” para análisis.

---

## 5. Hoja “ROI”

Sin cambios conceptuales, pero con posibilidad de:

- Relacionar la mejora en determinadas métricas (ej. subida del `%_Cuentas_criticas_MFA`) con reducciones de incidentes y pérdidas.  
- Documentar en comentarios/columnas qué objetivos GQM se han visto más impactados por las inversiones.

---

## 6. Hoja “Dashboards”

Se recomienda añadir:

- Gráficos que muestren **IGM** vs. **media total PRAGMATIC de las métricas** empleadas.  
- Indicadores que alerten si se usan demasiadas métricas de baja calidad (PRAGMATIC bajo).

---

_Esta plantilla permite no sólo calcular índices, sino también justificar por qué ciertas métricas merecen figurar en el cuadro de mando._