# Matriz de Evaluación PRAGMATIC Completa

## 1. Introducción

Esta matriz aplica los criterios PRAGMATIC a las principales métricas definidas en el marco GQM para las dimensiones TRIKE. [web:39][web:42][web:45]

Escala de valoración por criterio (0–5):

- 0 = No cumple el criterio.
- 1–2 = Cumplimiento débil o contextual.
- 3–4 = Cumplimiento razonable / bueno.
- 5 = Cumplimiento excelente.

## 2. Tabla resumen de métricas TRIKE y scores PRAGMATIC

> Nota: Los valores propuestos son orientativos y deben ajustarse en ejercicios reales con expertos nacionales. [web:45]

### 2.1 Threat (T)

| Métrica | P (Predictivo) | R (Relevante) | A (Accionable) | G (Genuino) | S (Significativo) | Pr (Preciso) | O (Oportuno) | I (Independiente) | Rn (Rentable) | Comentario |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T1.1.a Incidentes/100.000 hab. por sector | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | Métrica central para ver presión de amenazas; depende de calidad de reporte. [web:22][web:46] |
| T1.1.b Incidentes NIS2 por tipo de entidad | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | Muy alineada con supervisión; requiere madurez en notificación. [web:23][web:44] |
| T1.2.a % incidentes APT/eCrime | 4 | 5 | 4 | 3 | 4 | 3 | 3 | 3 | 3 | Requiere capacidad de atribución; muy útil para priorización. [web:13][web:46] |
| T1.2.b % ataques malware-free/IA | 4 | 5 | 4 | 3 | 4 | 3 | 3 | 3 | 3 | Indica sofisticación del panorama; depende de fuentes de detección. [web:13] |
| T1.3.a Incidentes vía proveedores críticos | 4 | 5 | 5 | 4 | 5 | 3 | 3 | 3 | 3 | Clave para cadena de suministro; precisión limitada por sub-reporte. [web:23][web:46] |
| T1.3.b % vulns cadena suministro SW | 3 | 4 | 4 | 3 | 4 | 3 | 3 | 3 | 3 | Difícil de medir con precisión, pero relevante para seguridad de software. [web:23] |

### 2.2 Risk (R)

| Métrica | P | R | A | G | S | Pr | O | I | Rn | Comentario |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R1.1.a Pérdida esperada por 1.000 M€ VA | 5 | 5 | 5 | 3 | 5 | 3 | 3 | 3 | 3 | Excelente para decisiones macro; requiere estimaciones y supuestos sólidos. [web:16][web:23] |
| R1.2.a % entidades con riesgo cuantitativo | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | Mide madurez de prácticas; relativamente fácil de recabar por encuesta. |
| R1.3.a Ratio incidentes/entidad por categoría | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | Útil para ver concentración de riesgo por tipo de entidad. |
| R1.3.b Pérdida media por incidente | 4 | 5 | 4 | 3 | 5 | 3 | 3 | 3 | 3 | Aporta contexto económico; sensibilidad a calidad de datos de impacto. [web:22] |

### 2.3 Impact (I)

| Métrica | P | R | A | G | S | Pr | O | I | Rn | Comentario |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I1.1.a Duración media de indisponibilidad | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | Directamente accionable para resiliencia y continuidad. [web:23] |
| I1.2.a Coste medio de incidentes | 4 | 5 | 4 | 3 | 5 | 3 | 3 | 3 | 3 | Clave para ROI; requiere modelos de estimación homogéneos. [web:22] |
| I1.2.b P90/P95 impacto | 4 | 5 | 4 | 3 | 5 | 3 | 3 | 3 | 3 | Resalta incidentes extremos; útil para seguros y regulación. [web:23] |
| I1.3.a Nº usuarios afectados | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | Social y políticamente muy significativo; suele estar bien registrado. [web:22] |
| I1.3.b Nº y cuantía de sanciones | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | Máximo valor para cumplimiento; datos trazables en fuentes oficiales. [web:44] |

### 2.4 Knowledge (K)

| Métrica | P | R | A | G | S | Pr | O | I | Rn | Comentario |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| K1.1.a % entidades con threat intel formal | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | Indica capacidad de anticipación; fácil de recoger por encuesta. [web:25][web:40] |
| K1.2.a % incidentes con post-mortem | 4 | 4 | 5 | 4 | 4 | 3 | 3 | 3 | 3 | Excelente para medir aprendizaje organizativo; requiere cultura de reporte. [web:25] |
| K1.3.a Profesionales cert. /100.000 hab. | 3 | 4 | 3 | 4 | 4 | 4 | 3 | 4 | 3 | Buen indicador de capacidad estructural; datos a consolidar desde certificadoras. [web:16] |
| K1.3.b Ratio vacantes/puestos ECSF | 3 | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 3 | Mide brecha de talento; estimaciones sujetas a incertidumbre. [web:40] |

### 2.5 Evaluation (E)

| Métrica | P | R | A | G | S | Pr | O | I | Rn | Comentario |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1.1.a % entidades con revisión anual de controles/modelos | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | Clave para medir mejora continua; se recaba por encuesta/auditoría. [web:23][web:43] |
| E1.2.a % entidades con alto alineamiento NIS2 | 3 | 5 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | Indicador de cumplimiento percibido; complementarlo con evidencias objetivas. [web:17][web:44] |
| E1.2.b Nº hallazgos de supervisión por categoría | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | Tal vez la métrica más “genuina” de realidad regulatoria; coste de obtención moderado. [web:43][web:44] |
| E1.3.a % entidades que vinculan auditoría a cambios de recursos | 4 | 5 | 5 | 4 | 4 | 4 | 3 | 4 | 4 | Mide el grado en que la evaluación cambia la práctica, no solo el discurso. [web:16][web:41] |

## 3. Uso de la matriz PRAGMATIC

1. Revisar y ajustar los scores con un panel de expertos nacionales y sectoriales.
2. Calcular un “meta-score” PRAGMATIC por métrica (por ejemplo, media ponderada de los nueve criterios). [web:45]
3. Priorizar métricas con meta-score alto y eliminar o mejorar aquellas con puntuaciones bajas.
4. Revisar la matriz periódicamente para incorporar nuevas métricas o retirar las obsoletas. [web:46]

La ambición no es tener más métricas, sino mejores métricas.

---