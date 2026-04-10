# Matriz de Evaluación PRAGMATIC Completa

> Versión 1.0 – Ejemplo de evaluación PRAGMATIC de métricas SIEM derivadas del marco GQM.

---

## 1. Leyenda

Escala de puntuación por criterio:

- 0 = Muy débil / no cumple el criterio.
- 1 = Cumple parcialmente.
- 2 = Cumple adecuadamente.
- 3 = Cumple de forma excelente.

Criterios:

- P – Predictivo  
- R – Relevante  
- A – Accionable  
- G – Genuino  
- M – Significativo  
- P2 – Preciso  
- T – Oportuno  
- I – Independiente  
- C – Rentable  

---

## 2. Tabla de evaluación (ejemplo base)

```markdown
| Métrica                                    | P | R | A | G | M | P2 | T | I | C | Score total |
|--------------------------------------------|---|---|---|---|---|----|---|---|---|------------|
| M1.1 MTTD incidentes críticos              | 2 | 3 | 3 | 2 | 3 | 2  | 2 | 2 | 2 | 21         |
| M1.2 MTTR hasta contención                 | 2 | 3 | 3 | 2 | 3 | 2  | 2 | 2 | 2 | 21         |
| M1.3 Distribución MTTD por tipo incidente  | 2 | 3 | 2 | 2 | 3 | 2  | 1 | 2 | 1 | 18         |
| M2.1 Plazo medio detección‑notificación    | 2 | 3 | 3 | 2 | 3 | 2  | 2 | 2 | 2 | 21         |
| M2.2% incidentes notificados en plazo     | 2 | 3 | 3 | 2 | 3 | 2  | 2 | 2 | 2 | 21         |
| M2.3 Índice de completitud de evidencias   | 1 | 3 | 2 | 2 | 3 | 2  | 1 | 2 | 1 | 17         |
| M3.1% activos críticos monitorizados      | 1 | 3 | 2 | 2 | 3 | 2  | 1 | 2 | 2 | 18         |
| M3.2% técnicas ATT&CK cubiertas           | 2 | 3 | 2 | 2 | 3 | 2  | 1 | 2 | 1 | 18         |
| M3.3 Latencia ingesta eventos críticos     | 1 | 2 | 2 | 2 | 2 | 2  | 3 | 2 | 2 | 18         |
| M4.1% detecciones impulsadas por IA       | 2 | 2 | 2 | 1 | 2 | 1  | 2 | 1 | 1 | 14         |
| M4.2% incidentes con respuesta automatiz. | 2 | 3 | 3 | 2 | 3 | 2  | 2 | 2 | 2 | 21         |
| M4.3 Δ% falsos positivos tras IA           | 3 | 3 | 3 | 2 | 3 | 2  | 2 | 2 | 2 | 22         |
| M5.1% comités riesgo con métricas SIEM    | 2 | 3 | 3 | 2 | 3 | 2  | 2 | 2 | 2 | 21         |
| M5.2 Frecuencia anual de incidentes graves | 2 | 3 | 2 | 2 | 3 | 2  | 2 | 2 | 2 | 20         |
| M5.3 Estimación de pérdidas evitadas (€)   | 3 | 3 | 3 | 1 | 3 | 1  | 2 | 1 | 2 | 19         |
```

### 2.1 Comentarios orientativos

- Las métricas de tiempo (MTTD, MTTR, plazos de notificación) suelen puntuar alto en Relevante, Accionable y Significativo.
- Las métricas de estimación económica (pérdidas evitadas) son muy predictivas y accionables, pero tienden a puntuar más bajo en Genuino y Preciso.
- Las métricas de IA pueden mejorar en Genuino e Independiente a medida que se dispone de mejores modelos y métodos de validación.

---

## 3. Uso de la matriz

1. Ajustar las puntuaciones en función del contexto sectorial (p. ej., energía vs. banca vs. administración).
2. Establecer un umbral mínimo para que una métrica sea considerada KPI estratégico.
3. Documentar las justificaciones de cada puntuación en una columna adicional `Comentario`.
4. Revisar la matriz periódicamente (al menos cada 2–3 años).

---

_Fin de la matriz PRAGMATIC._