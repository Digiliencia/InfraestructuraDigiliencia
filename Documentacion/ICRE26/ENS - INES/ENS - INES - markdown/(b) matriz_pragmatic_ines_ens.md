# Matriz de Evaluación PRAGMATIC Completa para métricas INES–ENS

> Resumen compacto de la calidad de cada métrica propuesta, vista a través de la lente PRAGMATIC.

---

## 1. Leyenda

- PRED = Predictiva.  
- REL = Relevante.  
- ACC = Accionable.  
- GEN = Genuina.  
- SIG = Significativa.  
- PRE = Precisa.  
- OPO = Oportuna.  
- IND = Independiente.  
- REN = Rentable.

Calificación: A = Alta, M = Media, B = Baja.

---

## 2. Matriz PRAGMATIC (extracto por métrica clave)

| ID Métrica | Descripción breve                                           | PRED | REL | ACC | GEN | SIG | PRE | OPO | IND | REN |
|-----------|--------------------------------------------------------------|------|-----|-----|-----|-----|-----|-----|-----|-----|
| 1.1.1     | % medidas ENS implantadas (sobre aplicables)                | M    | A   | A   | M   | A   | M   | M   | M   | A   |
| 1.2.1     | Frecuencia de revisión formal de implantación ENS           | M    | A   | A   | A   | A   | A   | A   | M   | A   |
| 1.3.1     | % medidas con evidencia automatizada                        | M    | M   | M   | A   | M   | M   | A   | A   | M   |
| 2.1.1     | Nº incidentes graves / 1.000 activos críticos (anual)       | A    | A   | A   | A   | A   | M   | M   | M   | M   |
| 2.2.1     | MTTD medio incidentes significativos                        | A    | A   | A   | M   | A   | M   | A   | M   | M   |
| 2.2.2     | MTTR medio incidentes significativos                        | A    | A   | A   | M   | A   | M   | A   | M   | M   |
| 2.3.1     | % presupuesto TIC dedicado a seguridad                      | M    | A   | M   | M   | A   | A   | M   | A   | A   |
| 2.3.2     | FTE seguridad / 1.000 usuarios                               | M    | A   | M   | M   | A   | A   | M   | A   | A   |
| 3.1.1     | Nº interrupciones de servicios críticos por incidentes      | A    | A   | A   | M   | A   | M   | M   | M   | M   |
| 3.2.1     | % incidentes que cumplen RTO                                | A    | A   | A   | M   | A   | M   | A   | M   | M   |
| 3.3.1     | % incidentes graves con análisis de causa raíz              | M    | A   | A   | A   | A   | A   | M   | M   | A   |
| 4.1.1     | % contratos de proveedores críticos con cláusulas ENS/NIS2  | M    | A   | A   | A   | A   | A   | M   | M   | A   |
| 4.2.1     | % proveedores críticos con evaluación de seguridad anual    | M    | A   | A   | M   | A   | M   | A   | M   | M   |
| 4.3.1     | Nº ejercicios con participación de proveedores              | M    | M   | A   | A   | M   | A   | M   | A   | M   |
| 5.1.1     | Puntuación madurez 1–5 por dominio                          | A    | A   | A   | M   | A   | M   | M   | M   | A   |
| 5.1.2     | IGM (media ponderada)                                       | A    | A   | A   | M   | A   | M   | M   | M   | A   |
| 5.2.1     | Variación anual del IGM                                     | A    | A   | A   | A   | A   | M   | M   | A   | A   |
| 6.1.1     | Grado de reutilización de datos INES (escala 1–4)           | M    | A   | A   | M   | M   | M   | A   | M   | A   |
| 6.2.1     | % procesos ENS soportados por herramientas                  | M    | M   | M   | M   | M   | M   | M   | A   | M   |
| 7.1.1     | % presupuesto seguridad vs criticidad                       | M    | A   | M   | M   | A   | A   | M   | A   | A   |
| 7.2.1     | ROI de seguridad (beneficio estimado / coste)               | A    | A   | A   | M   | M   | M   | M   | M   | M   |
| 8.1.1     | Estado de preparación post‑cuántica                         | A    | M   | A   | A   | M   | M   | B   | A   | M   |
| 8.2.1     | Nº sistemas IA con evaluación de riesgos completada         | M    | A   | A   | M   | M   | M   | M   | M   | M   |

---

## 3. Interpretación general

- Métricas con A en la mayoría de criterios (como 1.1.1, 2.1.1, 5.1.2) deben considerarse “core” y mantenerse en el tiempo.  
- Métricas con predominio de M y alguna B (por ejemplo, 8.1.1, 6.2.1) pueden verse como exploratorias o de madurez futura.  
- Métricas con baja rentabilidad (REN = B) deberían revisarse: o se simplifica su obtención, o se justifica su valor estratégico.

---

## 4. Uso de la matriz

1. Revisar anualmente la PRAGMATIC de cada métrica.  
2. Eliminar o simplificar aquellas que sistemáticamente obtienen baja puntuación y poca utilidad práctica.  
3. Priorizar, en el discurso con dirección, las métricas “A–A–A” (Altamente relevantes, accionables y significativas) para evitar infoxicación numérica.

> El objetivo no es tener la matriz más larga, sino la más útil.