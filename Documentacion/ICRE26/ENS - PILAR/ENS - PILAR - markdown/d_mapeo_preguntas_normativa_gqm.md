# Mapeo GQM de objetivos, preguntas y métricas a requisitos ENS / PILAR

> Correspondencia entre cada elemento del marco GQM y las referencias normativas ENS y capacidades de PILAR.

---

## 1. Tabla de mapeo

| Tipo | Identificador | Descripción breve | Referencia ENS / normativa | Elementos PILAR relevantes |
|------|---------------|--------------------|----------------------------|----------------------------|
| Goal | G1 | Mantener el riesgo residual en niveles aceptables | ENS art. 14 – Análisis y gestión de riesgos; principios de proporcionalidad [web:12] | Cálculo de riesgo potencial y residual; árboles de riesgo repercutido/acumulado [web:38] |
| Goal | G2 | Asegurar madurez adecuada de salvaguardas y controles | ENS anexo II – Medidas de seguridad; guías de madurez ENS [web:23] | Evaluación L0–L5 de salvaguardas; perfiles ENS [web:39][web:18] |
| Goal | G3 | Proveer indicadores útiles para decisiones e inversiones | ENS – Organización de la seguridad, revisión continua [web:12] | Recomendación 0–10, semáforos, informes de madurez y riesgo [web:40][web:1] |
| Question | Q1.1 | Riesgo residual de activos esenciales por dimensión | ENS – Protección de la información y servicios esenciales [web:12] | Riesgo repercutido por activo esencial y dimensión C/I/D/etc. [web:38] |
| Question | Q1.2 | Concentración de riesgo por activos, dominios, servicios | ENS – Clasificación de sistemas y servicios [web:12] | Árbol de riesgos por nivel (activos esenciales, soporte, amenazas) [web:38][web:40] |
| Question | Q1.3 | Riesgos residuales que superan umbrales aceptables | ENS – Aceptación y tratamiento del riesgo [web:12] | Valores de riesgo residual por escenario/amenaza [web:38] |
| Question | Q2.1 | Madurez media L0–L5 de salvaguardas por dominio | ENS – Implementación de medidas de seguridad [web:23] | Tabla de salvaguardas y madurez por dominio [web:39][web:18] |
| Question | Q2.2 | Diferencia entre madurez actual y objetivo | ENS – Mejora continua y planificación de medidas [web:12] | Fases de proyecto; recomendación de madurez; semáforo [web:1][web:40] |
| Question | Q2.3 | Medidas en overkill / underkill | ENS – Proporcionalidad de medidas [web:12] | Análisis de adaptación de medidas al riesgo, recomendación vs. madurez [web:46] |
| Question | Q3.1 | Salvaguardas de mayor valor y baja madurez | ENS – Prioridad a medidas críticas [web:12] | Recomendación 0–10 combinada con L0–L5 [web:40][web:18] |
| Question | Q3.2 | Reducción de riesgo por incremento de madurez | ENS – Eficacia de medidas; coste/beneficio | Cálculo de riesgo antes/después de cambios de madurez [web:38][web:39] |
| Question | Q3.3 | Comprensibilidad y accionabilidad de las métricas | ENS – Comunicación a la dirección, concienciación [web:12] | Informes y cuadros de mando derivados de PILAR [web:1][web:40] |
| Metric | M1.1 | Riesgo medio repercutido (0–10) por dimensión | ENS – Protección de información y servicios esenciales [web:12] | Niveles de riesgo repercutido en activos esenciales [web:38] |
| Metric | M1.2 | % activos esenciales con riesgo alto | ENS – Gestión de riesgos significativos [web:12] | Filtros sobre valores de riesgo repercutido [web:38] |
| Metric | M1.3 | Riesgo acumulado por dominio | ENS – Segmentación y zonas; análisis de impacto [web:12] | Riesgo acumulado de activos de soporte por dominio [web:38][web:40] |
| Metric | M1.4 | Nº riesgos residuales sobre umbral | ENS – Aceptación del riesgo [web:12] | Listado de escenarios con riesgo residual ≥ umbral [web:38] |
| Metric | M2.1 | Madurez media L0–L5 por dominio | ENS – Índices de madurez de medidas [web:23] | Valores L0–L5 de salvaguardas en dominios [web:39][web:18] |
| Metric | M2.2 | % salvaguardas en verde | ENS – Revisión de medidas y mejora continua [web:12] | Semáforo comparando madurez actual vs. objetivo [web:1][web:40] |
| Metric | M2.3 | Ratio rojo/amarillo en salvaguardas críticas | ENS – Priorización de medidas significativas [web:12] | Cruce de recomendación y semáforo [web:40][web:46] |
| Metric | M2.4 | Distribución L0–L5 en controles ENS obligatorios | ENS – Cumplimiento de medidas obligatorias [web:23] | Perfil ENS, salvaguardas etiquetadas como obligatorias [web:39] |
| Metric | M3.1 | Top-N salvaguardas de alto valor y baja madurez | ENS – Plan de adecuación priorizado [web:12] | Ordenación por recomendación y madurez [web:40][web:46] |
| Metric | M3.2 | Δ riesgo por Δ madurez | ENS – Proporcionalidad y eficiencia de medidas | Simulación de escenarios en PILAR (antes/después) [web:38][web:39] |
| Metric | M3.3 | Índice de cobertura ENS por madurez | ENS – Adecuación global a medidas [web:23] | Porcentaje de medidas ENS aplicables en L≥L3 [web:39] |
| Metric | M3.4 | Coste / riesgo mitigado | ENS – Uso eficiente de recursos [web:12] | Riesgo mitigado estimado (PILAR) + datos de coste externos |

---

## 2. Uso del mapeo

- Verificar que cada objetivo y métrica tiene una referencia explícita en el ENS o guías asociadas.  
- Documentar, junto a cada métrica, la sección del proyecto PILAR donde se obtiene el dato.  
- Facilitar el trabajo a auditores y revisores ENS, mostrando la trazabilidad completa de GQM.
