# (b) Matriz de Evaluación PRAGMATIC Completa

La tabla siguiente resume la evaluación PRAGMATIC (escala 1–5) para las métricas clave definidas en el marco GQM. Las puntuaciones son orientativas y deben ajustarse a cada contexto nacional o sectorial.

## Leyenda de criterios

- PRED: Predictivo
- REL: Relevante
- ACC: Accionable
- GEN: Genuino
- SIG: Significativo
- PRE: Preciso
- OPO: Oportuno
- IND: Independiente
- REN: Rentable (cost-effective)

## Tabla de métricas y evaluación

| Métrica | Descripción breve | PRED | REL | ACC | GEN | SIG | PRE | OPO | IND | REN | Comentario síntesis |
|--------|--------------------|------|-----|-----|-----|-----|-----|-----|-----|-----|----------------------|
| M1.1 | % técnicas ATT&CK críticas con ≥1 contramedida D3FEND implementada | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | Muy buen indicador de postura defensiva frente a amenazas prioritarias; requiere inventario y mapeo robustos.[web:5][web:8][web:18] |
| M1.2 | % técnicas críticas con cobertura parcial | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | Señala zonas grises donde detección y mitigación no están alineadas; útil para priorización. |
| M1.3 | Nº/% técnicas críticas sin contramedidas | 4 | 5 | 5 | 4 | 5 | 4 | 3 | 4 | 4 | Métrica incómoda pero potente para decisiones de inversión y supervisión. |
| M1.4 | Densidad de contramedidas por técnica crítica | 3 | 4 | 3 | 4 | 3 | 4 | 3 | 4 | 3 | Aporta contexto de profundidad defensiva, aunque su interpretación requiere madurez. |
| M2.1 | MTTD incidentes críticos | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | Métrica clásica de SOC, ampliamente comprendida y ligada a efectividad de detección.[web:18][web:21] |
| M2.2 | MTTR/MTTM incidentes críticos | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | Refleja capacidad de respuesta y recuperación; relevante para resiliencia operacional. |
| M2.3 | % incidentes detectados dentro de umbral | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | Facilita fijar SLOs y evaluar cumplimiento de objetivos de tiempo. |
| M2.4 | Variación % MTTD/MTTR tras nuevas contramedidas | 5 | 5 | 5 | 4 | 5 | 4 | 3 | 4 | 4 | Métrica muy útil para evaluar ROI de iniciativas específicas de seguridad.[web:5][web:18] |
| M3.1 | Tasa de éxito de mitigaciones | 4 | 5 | 5 | 4 | 5 | 4 | 3 | 4 | 4 | Indica qué parte del esfuerzo de respuesta se traduce en neutralización real.[web:5][web:18] |
| M3.2 | Indicador de recurrencia de incidentes | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | Ayuda a detectar “parches” que no resuelven causas de fondo. |
| M3.3 | Tasa de éxito por familia D3FEND | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | Permite refinar qué tipos de controles son más efectivos en la práctica. |
| M4.1 | % activos/artefactos críticos con sensores adecuados | 3 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | Conecta arquitectura de telemetría con la defensa informada por amenazas.[web:1][web:19] |
| M4.2 | % flujos de datos críticos monitorizados | 3 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | Complementa M4.1 y orienta inversiones en instrumentación. |
| M4.3 | Indicador de calidad de telemetría | 3 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 3 | Métrica compuesta útil pero más compleja de definir con precisión. |
| M4.4 | Nº técnicas D3FEND no aplicables por falta de telemetría | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | Visibiliza el coste de no instrumentar adecuadamente el entorno. |
| M5.1 | % rutas mando/control OT con controles y monitorización | 4 | 5 | 5 | 4 | 5 | 4 | 3 | 4 | 3 | Crítica para sectores OT; alta relevancia para resiliencia nacional.[web:5][web:20] |
| M5.2 | % protocolos industriales críticos monitorizados | 3 | 5 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | Aporta visibilidad sobre cobertura específica OT. |
| M5.3 | MTTR-OT funciones críticas | 4 | 5 | 5 | 4 | 5 | 4 | 3 | 4 | 4 | Directamente ligada a continuidad de servicios esenciales.[web:20] |
| M5.4 | % incidentes OT con pérdida limitada dentro de umbrales | 4 | 5 | 5 | 4 | 5 | 4 | 3 | 4 | 4 | Permite evaluar efectividad global de la preparación OT frente a incidentes. |

> Nota: las puntuaciones PRAGMATIC deben adaptarse a cada contexto; aquí se ofrece una línea base razonable para España y entornos similares.[web:17][web:20][web:23]