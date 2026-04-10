# Matriz de Evaluación PRAGMATIC Completa para métricas Zero Trust

Este documento resume la evaluación PRAGMATIC de un conjunto de métricas clave derivadas del marco GQM para Zero Trust. Cada criterio se puntúa de 0 a 3 (0 = no cumple, 3 = alto cumplimiento).

## 1. Leyenda de criterios PRAGMATIC

- **P – Predictivo**: capacidad de anticipar resultados futuros (incidentes, brechas, impacto económico).  
- **R – Relevante**: alineación con objetivos estratégicos y decisiones clave.  
- **A – Accionable**: capacidad para sugerir acciones concretas cuando cambia el valor.  
- **G – Genuino**: resistencia a ser manipulado o maquillado; proximidad a la realidad.  
- **M – Significativo (Meaningful)**: comprensibilidad y significado para los stakeholders.  
- **P – Preciso (Precise)**: exactitud y consistencia en la medición.  
- **T – Oportuno (Timely)**: disponibilidad con la frecuencia requerida.  
- **I – Independiente**: grado en que no duplica información de otras métricas.  
- **C – Rentable (Cost-effective)**: relación coste/beneficio de obtener la métrica.  

## 2. Matriz PRAGMATIC (extracto de métricas principales)

### 2.1. Identidad y Acceso

| Métrica (ID) | Descripción breve                                             | P | R | A | G | M | P (Preciso) | T | I | C | Comentario síntesis |
|-------------:|---------------------------------------------------------------|---|---|---|---|---|-------------|---|---|---|----------------------|
| M1.1         | % usuarios con MFA en sistemas críticos                      | 3 | 3 | 3 | 2 | 3 | 3           | 3 | 2 | 3 | KPI central de robustez de identidad. |
| M1.2         | % cuentas con permisos revisados al menos anual              | 2 | 3 | 3 | 2 | 3 | 2           | 2 | 2 | 2 | Indica disciplina de mínimo privilegio. |
| M1.3         | % cuentas privilegiadas bajo PAM                             | 3 | 3 | 3 | 2 | 3 | 2           | 2 | 2 | 2 | Crítico para ataques de escalada de privilegios. |
| M1.4         | Nº incidentes de acceso anómalo detectados por UEBA          | 2 | 3 | 2 | 2 | 2 | 2           | 2 | 2 | 2 | Requiere contexto para interpretarse (más detecciones no siempre es peor). |

### 2.2. Dispositivos y Endpoints

| Métrica (ID) | Descripción breve                                             | P | R | A | G | M | P (Preciso) | T | I | C | Comentario síntesis |
|-------------:|---------------------------------------------------------------|---|---|---|---|---|-------------|---|---|---|----------------------|
| M2.1         | % dispositivos inventariados y gestionados                   | 2 | 3 | 3 | 2 | 3 | 2           | 2 | 2 | 3 | Base para toda gestión de riesgos. |
| M2.2         | Tiempo medio de despliegue de parches críticos (días)        | 3 | 3 | 3 | 2 | 3 | 2           | 2 | 2 | 2 | Alta capacidad predictiva de exposición a CVEs. |
| M2.3         | % endpoints con EDR/XDR activo                               | 2 | 3 | 3 | 2 | 3 | 2           | 2 | 2 | 2 | Complementa a inventario y parcheo. |
| M2.4         | Nº dispositivos no gestionados/1.000 usuarios                | 2 | 2 | 2 | 2 | 2 | 2           | 2 | 2 | 2 | Métrica de “sombra” de TI, útil para priorizar controles ZTNA. |

### 2.3. Red, ZTNA y Microsegmentación

| Métrica (ID) | Descripción breve                                             | P | R | A | G | M | P (Preciso) | T | I | C | Comentario síntesis |
|-------------:|---------------------------------------------------------------|---|---|---|---|---|-------------|---|---|---|----------------------|
| M3.1         | % tráfico interno inspeccionado en L7                         | 3 | 3 | 3 | 2 | 3 | 2           | 2 | 2 | 2 | Buena proxy de visibilidad sobre amenazas internas. |
| M3.2         | % accesos remotos críticos vía ZTNA vs. VPN                   | 3 | 3 | 3 | 2 | 3 | 2           | 2 | 2 | 2 | Indica transición hacia Zero Trust en acceso remoto. |
| M3.3         | Nº segmentos/microsegmentos por aplicación crítica            | 2 | 2 | 2 | 2 | 2 | 1           | 1 | 2 | 1 | Métrica algo técnica; requiere normalización. |
| M3.4         | Nº intentos de movimiento lateral detectados/bloqueados       | 2 | 3 | 2 | 2 | 2 | 1           | 1 | 2 | 1 | Difícil de medir con precisión, pero relevante. |

### 2.4. Aplicaciones, Nube y Cargas de Trabajo

| Métrica (ID) | Descripción breve                                             | P | R | A | G | M | P (Preciso) | T | I | C | Comentario síntesis |
|-------------:|---------------------------------------------------------------|---|---|---|---|---|-------------|---|---|---|----------------------|
| M4.1         | % nuevas apps Zero-Trust-by-design                           | 3 | 3 | 3 | 2 | 3 | 2           | 2 | 2 | 2 | KPIs de diseño seguro y arquitectura. |
| M4.2         | % secretos de servicios en vault con rotación automática      | 3 | 3 | 3 | 2 | 3 | 2           | 2 | 2 | 2 | Crítico frente a fugas de credenciales. |
| M4.3         | MTTR de incidentes cloud (horas)                              | 3 | 3 | 3 | 2 | 3 | 2           | 2 | 2 | 2 | Directamente vinculado a resiliencia. |
| M4.4         | % APIs críticas bajo gateway con controles avanzados          | 3 | 3 | 3 | 2 | 3 | 2           | 2 | 2 | 2 | Mide robustez en superficie de APIs. |

### 2.5. Datos y Protección de la Información

| Métrica (ID) | Descripción breve                                             | P | R | A | G | M | P (Preciso) | T | I | C | Comentario síntesis |
|-------------:|---------------------------------------------------------------|---|---|---|---|---|-------------|---|---|---|----------------------|
| M5.1         | % activos de información clasificados                         | 2 | 3 | 3 | 2 | 3 | 2           | 2 | 2 | 2 | Base para controles RGPD/NIS2. |
| M5.2         | % repositorios sensibles con acceso contextual                | 3 | 3 | 3 | 2 | 3 | 2           | 2 | 2 | 2 | Indica madurez en controles de datos. |
| M5.3         | Ratio exfiltraciones detectadas vs. bloqueadas                | 3 | 3 | 3 | 2 | 2 | 1           | 1 | 2 | 1 | Difícil pero muy relevante. |
| M5.4         | % accesos a datos sensibles registrados/correlacionados       | 2 | 3 | 3 | 2 | 3 | 2           | 2 | 2 | 2 | Sustento de trazabilidad y forense. |

### 2.6. Monitorización, Resiliencia y Continuidad

| Métrica (ID) | Descripción breve                                             | P | R | A | G | M | P (Preciso) | T | I | C | Comentario síntesis |
|-------------:|---------------------------------------------------------------|---|---|---|---|---|-------------|---|---|---|----------------------|
| M6.1         | % sistemas críticos integrados en SIEM                        | 3 | 3 | 3 | 2 | 3 | 2           | 2 | 2 | 2 | Fuerte predictor de capacidad de detección. |
| M6.2         | MTTD incidentes significativos (días)                         | 3 | 3 | 3 | 2 | 3 | 2           | 2 | 2 | 2 | Directamente vinculado a reducción de impacto. |
| M6.3         | MTTR contención/recuperación (horas)                          | 3 | 3 | 3 | 2 | 3 | 2           | 2 | 2 | 2 | Central para resiliencia. |
| M6.4         | % procesos críticos con planes de aislamiento Zero Trust      | 2 | 3 | 3 | 2 | 3 | 2           | 2 | 2 | 2 | Indica madurez de continuidad técnica. |
| M6.5         | Nº simulacros de ciberincidentes al año                       | 2 | 3 | 3 | 2 | 2 | 2           | 2 | 2 | 3 | Métrica barata y útil de preparación. |

## 3. Uso de la matriz PRAGMATIC

- Priorizar aquellas métricas con puntuaciones altas (≥ 22–24 sobre 27) como KPIs nacionales/sectoriales.  
- Identificar métricas con baja puntuación en “Genuino” o “Preciso” para mejorar procesos de medición.  
- Evaluar periódicamente la matriz (cada 1–2 años) para adaptarla a cambios normativos, tecnológicos y de amenazas. [web:47][web:53]