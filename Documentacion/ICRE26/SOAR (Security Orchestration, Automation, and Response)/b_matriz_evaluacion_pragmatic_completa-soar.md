# Matriz de Evaluación PRAGMATIC de métricas SOAR

Escala utilizada: **A = Alto**, **M = Medio**, **B = Bajo**.

## 1. Métricas de tiempo (G1)

| Métrica  | Predictivo | Relevante | Accionable | Genuino | Significativo | Preciso | Oportuno | Independiente | Rentable | Comentario breve |
|---------|------------|-----------|------------|---------|---------------|---------|----------|-------------|----------|-------------------|
| M1.1 – MTTD nacional/sectorial | A | A | A | M | A | M | M | M | A | Alto valor para anticipar riesgo, requiere buena instrumentación de detección. |
| M1.2 – MTTC/MTTI nacional | A | A | A | M | A | M | M | M | A | Clave para evaluar eficiencia de análisis y contención inicial. |
| M1.3 – MTTR nacional | A | A | A | M | A | M | M | M | A | Directamente vinculado a resiliencia percibida y operativa. |
| M1.4 – Dwell time en sectores críticos | A | A | M | M | A | B | B | M | M | Difícil de medir con precisión, pero muy ilustrativo del riesgo real. |
| M1.5 – % reducción MTTD/MTTR por SOAR | A | A | A | M | A | M | M | M | A | Es la “métrica estrella” para justificar inversiones en automatización. |

## 2. Métricas de cobertura y calidad de automatización (G2)

| Métrica  | Predictivo | Relevante | Accionable | Genuino | Significativo | Preciso | Oportuno | Independiente | Rentable | Comentario breve |
|---------|------------|-----------|------------|---------|---------------|---------|----------|-------------|----------|-------------------|
| M2.1 – % alertas tratadas automáticamente | M | A | A | M | A | A | A | M | A | Métrica de adopción clave; se interpreta mejor junto a calidad. |
| M2.2 – % incidentes con soporte SOAR | M | A | A | M | A | A | A | M | A | Relaciona automatización con casos de negocio reales (incidentes). |
| M2.3 – Cobertura de casos de uso (Top 10) | M | A | A | M | A | M | M | M | A | Permite priorizar desarrollo de playbooks en incidentes frecuentes. |
| M2.4 – Tasa de éxito de playbooks | M | A | A | A | A | A | A | M | A | Directamente accionable para mejorar diseño y pruebas de playbooks. |
| M2.5 – Tasa de excepciones / rollbacks | M | A | A | A | A | M | M | M | A | Señala riesgos de automatización excesiva o mal gobernada. |

## 3. Métricas de cumplimiento y reporting (G3)

| Métrica  | Predictivo | Relevante | Accionable | Genuino | Significativo | Preciso | Oportuno | Independiente | Rentable | Comentario breve |
|---------|------------|-----------|------------|---------|---------------|---------|----------|-------------|----------|-------------------|
| M3.1 – % org. que usan SOAR para notificación | B | A | M | A | M | A | M | M | A | Indica nivel de industrialización del cumplimiento, más que riesgo técnico. |
| M3.2 – Tiempo medio hasta notificación inicial | M | A | A | M | A | A | A | M | A | Conecta operación con obligación regulatoria concreta. |
| M3.3 – % notificaciones dentro del plazo | M | A | A | A | A | A | A | A | A | Métrica clara para supervisores y auditores. |
| M3.4 – Grado de estructuración de informes | B | A | M | M | M | M | M | M | A | Facilita reutilización y análisis, pero su impacto directo es indirecto. |

## 4. Métricas de impacto económico y ROI (G4)

| Métrica  | Predictivo | Relevante | Accionable | Genuino | Significativo | Preciso | Oportuno | Independiente | Rentable | Comentario breve |
|---------|------------|-----------|------------|---------|---------------|---------|----------|-------------|----------|-------------------|
| M4.1 – % org. que estiman coste de incidentes | B | A | M | A | M | M | M | A | A | Señal de madurez económica, base para métricas más sofisticadas. |
| M4.2 – Coste medio anual de incidentes | M | A | A | M | A | M | M | M | A | Soporta decisiones de inversión, pero depende de supuestos. |
| M4.3 – Inversión anual en SOAR | B | A | M | A | M | A | A | A | A | Necesaria para cálculos de ROI y planificación presupuestaria. |
| M4.4 – ROI de proyectos SOAR | A | A | A | M | A | M | M | M | A | Métrica políticamente poderosa, pero difícil de estimar con alta precisión. |
| M4.5 – Correlación IGM–coste/incidentes | A | A | M | M | A | M | B | M | M | Útil para análisis estratégicos, menos para operación diaria. |

## 5. Métricas de estructura y madurez (apoyo transversal)

Además de las métricas numéricas anteriores, algunas métricas de estructura (existencia de catálogos, hojas de ruta, modelos de SOC) se valoran cualitativamente:

| Métrica cualitativa | Predictivo | Relevante | Accionable | Genuino | Significativo | Preciso | Oportuno | Independiente | Rentable | Comentario breve |
|---------------------|------------|-----------|------------|---------|---------------|---------|----------|-------------|----------|-------------------|
| Existencia de catálogo formal de casos de uso | M | A | A | A | A | A | M | A | A | Fuerte indicador de madurez organizativa de SOC/SOAR. |
| Existencia de hoja de ruta SOAR aprobada | M | A | A | A | A | A | M | A | A | Conecta visión estratégica con ejecución, muy apreciada en auditorías. |
| Modelo de SOC (interno/externo/híbrido) definido | B | A | M | A | M | A | A | A | A | Base para interpretar otras métricas y planificar capacidades. |

La matriz puede ser refinada con puntuaciones numéricas (por ejemplo, A=3, M=2, B=1) para construir un “score PRAGMATIC” por métrica y ayudar a priorizar las que deben ocupar un lugar central en el cuadro nacional de mando.