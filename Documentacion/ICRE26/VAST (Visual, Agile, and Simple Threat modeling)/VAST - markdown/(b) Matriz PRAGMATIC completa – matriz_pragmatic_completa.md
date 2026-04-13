# Matriz de Evaluación PRAGMATIC Completa

> Escala de valoración: 1 (muy bajo) – 5 (muy alto)

## 1. Leyenda de criterios

- **P (Predictiva)**
- **R (Relevante)**
- **A (Accionable)**
- **G (Genuina)**
- **M (Significativa)**
- **P2 (Precisa)**
- **O (Oportuna)**
- **I (Independiente)**
- **C (Rentable / Cost-effective)**

## 2. Tabla de métricas principales

### 2.1. Métricas de G1 – Cobertura de modelado de amenazas

| Métrica | Descripción                                                        | P | R | A | G | M | P2 | O | I | C | Comentarios clave |
|---------|--------------------------------------------------------------------|---|---|---|---|---|----|---|---|---|-------------------|
| G1.M1   | % de sistemas críticos con modelo de amenazas vigente             | 4 | 5 | 4 | 4 | 5 | 4  | 3 | 4 | 4 | Métrica central de madurez en modelado; requiere inventario fiable. |
| G1.M2   | Frecuencia media de revisión de modelos (meses)                   | 3 | 4 | 4 | 4 | 4 | 3  | 3 | 4 | 4 | Ayuda a ver si los modelos son “vivos”; precisa registro de revisiones. |
| G1.M3   | % de proyectos con modelado de amenazas en SDLC/CI-CD             | 4 | 5 | 5 | 4 | 5 | 3  | 3 | 4 | 3 | Alta capacidad para impulsar DevSecOps; costes de medición moderados. |
| G1.M4   | Índice de participación multidisciplinar en sesiones de modelado  | 3 | 4 | 3 | 3 | 4 | 3  | 2 | 4 | 4 | Buen indicador cultural; algo más cualitativo y menos preciso. |

### 2.2. Métricas de G2 – Vulnerabilidades explotadas activamente

| Métrica | Descripción                                                        | P | R | A | G | M | P2 | O | I | C | Comentarios clave |
|---------|--------------------------------------------------------------------|---|---|---|---|---|----|---|---|---|-------------------|
| G2.M1   | % de vulnerabilidades explotadas activamente abiertas             | 5 | 5 | 5 | 4 | 5 | 4  | 3 | 4 | 3 | Muy predictiva de riesgo inmediato; requiere buena integración con feeds de amenazas. |
| G2.M2   | % de vulnerabilidades explotadas activas con >12 meses de antigüedad | 5 | 5 | 5 | 4 | 5 | 4  | 3 | 4 | 3 | Señal clara de deuda de seguridad; algo costoso de mantener en organizaciones sin inventario maduro. |
| G2.M3   | Tiempo medio de remediación de vulnerabilidades críticas (días)   | 4 | 5 | 5 | 4 | 5 | 4  | 3 | 4 | 4 | Métrica clásica de gestión de vulnerabilidades, muy accionable. |

### 2.3. Métricas de G3 – Tiempos de detección, contención y recuperación

| Métrica | Descripción                                                        | P | R | A | G | M | P2 | O | I | C | Comentarios clave |
|---------|--------------------------------------------------------------------|---|---|---|---|---|----|---|---|---|-------------------|
| G3.M1   | MTTD de incidentes significativos                                 | 4 | 5 | 5 | 4 | 5 | 4  | 3 | 4 | 3 | Requiere definición clara de “incidente significativo”; muy útil para SOC. |
| G3.M2   | MTTC de incidentes significativos                                 | 4 | 5 | 5 | 4 | 5 | 4  | 3 | 4 | 3 | Complementa al MTTD; refleja capacidad operativa. |
| G3.M3   | MTTR de servicios esenciales tras incidentes                       | 4 | 5 | 5 | 4 | 5 | 4  | 3 | 4 | 3 | Muy relevante para negocio y reguladores; medición más compleja. |

### 2.4. Métricas de G4 – Riesgo económico y decisiones

| Métrica | Descripción                                                        | P | R | A | G | M | P2 | O | I | C | Comentarios clave |
|---------|--------------------------------------------------------------------|---|---|---|---|---|----|---|---|---|-------------------|
| G4.M1   | % de organizaciones que usan modelos económicos de riesgo         | 3 | 4 | 4 | 4 | 4 | 3  | 2 | 4 | 4 | Buena para ver adopción; menos predictiva por sí misma. |
| G4.M2   | Frecuencia de reporting de métricas económicas al Consejo         | 3 | 4 | 4 | 4 | 4 | 3  | 3 | 4 | 4 | Indica madurez en comunicación; precisión moderada. |
| G4.M3   | % de decisiones de inversión que citan explícitamente modelos de riesgo | 4 | 4 | 5 | 3 | 4 | 2  | 2 | 3 | 3 | Accionable pero difícil de medir con precisión; requiere trazabilidad en decisiones. |

### 2.5. Métricas de G5 – Cadena de suministro y terceros

| Métrica | Descripción                                                        | P | R | A | G | M | P2 | O | I | C | Comentarios clave |
|---------|--------------------------------------------------------------------|---|---|---|---|---|----|---|---|---|-------------------|
| G5.M1   | % de proveedores críticos evaluados en ciber                       | 4 | 5 | 5 | 4 | 5 | 3  | 3 | 4 | 3 | Clave para NIS2/DORA; dependiente de inventarios contractuales fiables. |
| G5.M2   | Frecuencia media de revisión de riesgos de terceros                | 3 | 4 | 4 | 4 | 4 | 3  | 3 | 4 | 4 | Ayuda a ver si el control es continuo o puntual. |
| G5.M3   | % de incidentes significativos atribuibles a terceros              | 4 | 5 | 5 | 3 | 5 | 3  | 2 | 3 | 3 | Difícil de atribuir con precisión; muy significativa para regulación. |

### 2.6. Métricas de G6 – Talento, cultura y colaboración

| Métrica | Descripción                                                        | P | R | A | G | M | P2 | O | I | C | Comentarios clave |
|---------|--------------------------------------------------------------------|---|---|---|---|---|----|---|---|---|-------------------|
| G6.M1   | Índice de suficiencia de recursos internos                         | 3 | 4 | 4 | 3 | 4 | 3  | 3 | 3 | 4 | Basado en autoevaluación; útil para políticas de talento. |
| G6.M2   | % de organizaciones con dificultades graves para cubrir vacantes   | 3 | 4 | 4 | 4 | 4 | 3  | 3 | 4 | 4 | Agregado nacional útil para planificación de formación y empleo. |
| G6.M3   | % de empleados cubiertos por programas de concienciación anual     | 3 | 4 | 4 | 4 | 4 | 3  | 3 | 4 | 4 | Métrica clásica, fácil de obtener y comunicar. |
| G6.M4   | % de organizaciones que participan en foros/CSIRTs                 | 3 | 4 | 4 | 4 | 4 | 3  | 3 | 4 | 4 | Indica madurez colaborativa y capacidad de respuesta sectorial. |

## 3. Puntuación PRAGMATIC global por métrica

Se puede calcular una **puntuación compuesta** por métrica como:

PRAGMATIC_Score = (P + R + A + G + M + P2 + O + I + C) / 9

Opcionalmente, se pueden ponderar más algunos criterios (por ejemplo, Relevante, Accionable y Rentable) según el contexto de análisis nacional.

La matriz anterior puede ampliarse a todas las métricas derivadas del cuestionario VAST, añadiendo filas y ajustando las puntuaciones a medida que se obtenga experiencia práctica.