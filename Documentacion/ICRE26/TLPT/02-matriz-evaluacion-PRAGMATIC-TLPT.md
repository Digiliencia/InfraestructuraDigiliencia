# Matriz de Evaluación PRAGMATIC – Métricas TLPT

> Escala por criterio (0–3): 0 = muy débil, 1 = aceptable, 2 = buena, 3 = excelente.  
> Valoraciones orientativas; deben recalibrarse con la experiencia de uso real.

## 1. Tabla resumen PRAGMATIC

| Métrica | Descripción breve                                   | P (Pred) | R (Rel) | A (Acc) | G (Gen) | M (Sig) | P2 (Prec) | T (Oport) | I (Indep) | C (Rent) |
|--------|------------------------------------------------------|---------:|--------:|--------:|--------:|--------:|----------:|----------:|----------:|---------:|
| M1     | % funciones críticas cubiertas                      | 2 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 2 |
| M2     | % servicios TIC críticos en alcance                 | 2 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 2 |
| M3     | Uso de producción (índice 0–2)                      | 1 | 3 | 2 | 3 | 2 | 3 | 3 | 3 | 3 |
| M4     | Nº / % escenarios TTI ejercitados                   | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 |
| M5     | Duración Red Team (semanas)                         | 2 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 |
| M6     | MTTD TLPT (horas)                                   | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 2 |
| M7     | % acciones del Red Team detectadas                  | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 2 |
| M8a    | MTTC (contención)                                   | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 2 |
| M8b    | MTTR (recuperación)                                 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 2 |
| M9     | Nº / % hallazgos críticos/altos                     | 2 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 2 |
| M10    | % remediación en plazo                              | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 2 |
| M11    | % hallazgos recurrentes                             | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| M12    | Cumplimiento ciclo trienal TLPT                     | 1 | 3 | 2 | 3 | 2 | 3 | 3 | 3 | 3 |
| M13    | Índice plan plurianual de pruebas                   | 1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |
| M14    | Coste total TLPT                                    | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 1 |
| M15    | Pérdidas previstas evitadas                         | 3 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 |
| M16    | ROI TLPT                                            | 3 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 |

## 2. Comentarios cualitativos por métrica

### M1 – % funciones críticas cubiertas

- Predictiva: buena; mayor cobertura suele anticipar menor “sorpresa” operacional en incidentes reales.  
- Relevante: muy alta; conecta directamente con DORA sobre funciones críticas y TLPT.[web:16]  
- Accionable: permite priorizar alcance en próximos ciclos.  
- Genuina: moderadamente robusta; depende de que el inventario de funciones críticas no esté “maquillado”.  
- Significativa: fácil de interpretar por comités.  
- Precisa: definición clara, siempre que el BIA esté consolidado.  
- Oportuna: se conoce en el cierre de cada TLPT.  
- Independiente: se complementa con otras métricas de alcance, pero aporta valor propio.  
- Rentable: coste bajo, datos ya disponibles.

### M6 – MTTD TLPT (ejemplo de detalle ampliado)

- Predictiva: alta; el MTTD en ejercicios avanzados se correlaciona bien con la capacidad real de detección.  
- Relevante: clave para medir eficacia del pilar de monitorización e incidentes en DORA.[web:26]  
- Accionable: orienta mejoras en SOC, reglas de correlación, telemetría.  
- Genuina: susceptible a cierto sesgo (ayudas del White Team), pero en conjunto bastante representativa.  
- Significativa: intuitiva (menos horas = mejor), entendible a nivel ejecutivo.  
- Precisa: requiere definición rigurosa de “evento de detección válida”.  
- Oportuna: se obtiene al cierre del ejercicio y puede compararse entre ciclos.  
- Independiente: correlacionada con M7/M8, pero con foco diferente.  
- Rentable: requiere cierta disciplina de registro, pero se apoya en datos ya capturados durante el TLPT.

*(El resto de métricas pueden documentarse de forma similar en versiones extendidas del kit.)*
