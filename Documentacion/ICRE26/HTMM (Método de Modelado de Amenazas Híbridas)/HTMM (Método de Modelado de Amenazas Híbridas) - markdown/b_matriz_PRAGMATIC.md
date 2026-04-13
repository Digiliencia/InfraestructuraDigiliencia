# Matriz de Evaluación PRAGMATIC de métricas HTMM

La siguiente matriz ilustra la evaluación PRAGMATIC de un subconjunto representativo de métricas definidas en el marco GQM anterior. Las valoraciones pueden ajustarse a una escala numérica (por ejemplo 1 = bajo, 5 = alto) en la hoja de cálculo correspondiente.

## 1. Leyenda

- Escala sugerida: 1 (muy bajo) a 5 (muy alto).
- P: Predictivo, R: Relevante, A: Accionable, G: Genuino, M: Significativo, Pr: Preciso, T: Oportuno (Timely), I: Independiente, C: Coste-efectivo.

## 2. Matriz resumida

| Métrica | Descripción breve | P | R | A | G | M | Pr | T | I | C | Comentario síntesis |
|--------|--------------------|---|---|---|---|---|----|---|---|---|----------------------|
| M1.1 Cobertura STRIDE | % de categorías STRIDE con amenazas identificadas | 3 | 5 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | Buena para ver amplitud de cobertura, pero no capta profundidad ni calidad de cada amenaza. |
| M1.2 Cobertura ENISA | % de categorías ENISA presentes en modelos | 4 | 5 | 4 | 4 | 5 | 3 | 3 | 3 | 4 | Conecta directamente con el paisaje de amenazas UE; exige taxonomía clara. [web:13][web:7] |
| M1.3 Tasa de amenazas nuevas | % de amenazas no presentes en catálogo previo | 4 | 4 | 3 | 3 | 4 | 3 | 2 | 2 | 3 | Indicador de creatividad y sensibilidad a emergentes, pero muy dependiente de criterios subjetivos. [web:6] |
| M2.1 Varianza inter-equipo | Varianza en nº de amenazas por sistema | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | Útil para evaluar consistencia; puede requerir muestras suficientes para ser robusta. [web:6][web:16] |
| M2.2 % amenazas descartadas | % de amenazas podadas como poco plausibles | 3 | 4 | 4 | 3 | 3 | 3 | 3 | 2 | 4 | Si es muy alto indica ruido; si es muy bajo, posible falta de filtro. Depende de criterios de poda. [web:6] |
| M2.3 Solapamiento de catálogos | % de amenazas comunes entre catálogos | 4 | 4 | 4 | 4 | 4 | 3 | 2 | 3 | 3 | Buena proxy de convergencia; requiere definiciones consistentes y repositorios comparables. |
| M3.1 Esfuerzo total sesión | Horas totales dedicadas por sesión | 2 | 4 | 3 | 5 | 3 | 4 | 4 | 5 | 3 | Métrica genuina y fácil de obtener; por sí sola no dice si el esfuerzo está bien invertido. [web:6] |
| M3.2 Esfuerzo por amenaza útil | Horas / amenazas con control asociado | 3 | 5 | 5 | 4 | 5 | 3 | 3 | 3 | 3 | Muy accionable para optimizar el proceso; requiere buena trazabilidad amenazas-controles. |
| M3.3 Esfuerzo relativo hTMM | Ratio esfuerzo hTMM / método base | 3 | 4 | 4 | 4 | 4 | 3 | 2 | 3 | 3 | Permite discutir costo-efectividad del enfoque híbrido; exige datos históricos consistentes. [web:6] |
| M4.1 % amenazas con control | % de amenazas con al menos un control | 4 | 5 | 5 | 4 | 5 | 3 | 3 | 3 | 4 | Métrica muy relevante y accionable; no diferencia calidad/eficacia del control. |
| M4.2 Tiempo a registro de riesgos | Días hasta incorporar amenaza crítica al registro | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 3 | 3 | Buena proxy de agilidad de gobernanza de riesgos; sensible a procesos internos. |
| M4.3 % amenazas críticas con RTO/RPO | % amenazas críticas con parámetros de continuidad | 3 | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 3 | Indicador de integración con continuidad; requiere coordinación entre áreas. [web:8] |
| M5.1 Mapeo a ENISA | % amenazas internas con categoría ENISA | 4 | 5 | 4 | 4 | 5 | 3 | 3 | 3 | 4 | Refuerza alineación con paisaje UE; depende de calidad de la taxonomía ENISA y del mapeo. [web:13] |
| M5.2 Uso de datos ENISA | % organizaciones que usan datos ENISA para priorizar | 3 | 5 | 4 | 3 | 4 | 3 | 3 | 3 | 4 | Métrica de adopción de inteligencia externa; no mide profundidad del uso. [web:13][web:7] |
| M5.3 Tiempo de reacción ENISA | Tiempo hasta actualizar modelos tras nuevo TL | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 3 | Indica sensibilidad institucional a inteligencia UE; puede estar condicionado por ciclos presupuestarios. |

## 3. Uso práctico de la matriz

- La matriz sirve como base para seleccionar un subconjunto de métricas “estrella” con alta puntuación global, equilibrando capacidad predictiva, relevancia y coste.
- La implantación nacional o sectorial puede afinar los valores numéricos (1–5) y añadir comentarios específicos.
- Para el cálculo del IGM, se recomienda ponderar las métricas mejor valoradas en PRAGMATIC para evitar un índice hinchado de números poco útiles en la práctica.