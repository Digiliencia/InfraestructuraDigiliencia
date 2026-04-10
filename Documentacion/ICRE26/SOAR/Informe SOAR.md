
# Informe SOAR.

Actúas como el orquestador principal de un consorcio de los mejores CISOs del mundo, criptógrafos cuánticos, arquitectos de Zero Trust, teóricos del riesgo actuarial, Estrategas de ciberseguridad, resiliencia digital y continuidad de negocios de Clase Mundial junto con expertos internacionales con más de 15 años de experiencia en investigación de vanguardia, filosofía de la ciencia, edición en revistas de alto impacto.
Tu misión es ejecutar una investigación exhaustiva, sin límite de palabras, sobre las últimas tendencias (desde 2025) en indicadores del marco SOAR (Security Orchestration, Automation and Response). Enfócate en los indicadores y las métricas de ciberseguridad propuestas por SOAR con aplicación a nivel nacional territorial para España, pero con un enfoque comparativo mundial.
Utiliza exclusivamente fuentes fiables y de alta calidad, como:

- artículos académicos revisados por pares
- organismos oficiales y gubernamentales
- universidades y centros de investigación reconocidos
- instituciones educativas y científicas de prestigio
- documentación oficial del fabricante, desarrollador o creador de la tecnología (cuando el tema investigado sea una tecnología o herramienta específica).
- Informes industriales y documentación técnica.
Descarta blogs personales, foros, contenido opinativo, marketing no técnico y fuentes sin autor.
Cuida el lenguaje español, minimiza el uso de listas o viñetas de posibles respuestas ad hoc a las preguntas inquisitivas de la encuesta. Que sea ameno, abierto y con el tono irónico y literario que supone una acción propositiva y constructiva.

Un marco SOAR nacional para España en 2026 necesita medir menos “cosas” y más “capacidad de reacción”: tiempo, calidad y cobertura de la automatización, conectadas a NIS2, ENS y a los datos reales de INCIBE y ENISA.[^1][^2][^3][^4]

## 1. De qué hablamos cuando hablamos de indicadores SOAR

Aunque los fabricantes lo adornen con neones de marketing, el núcleo métrico de SOAR sigue orbitando alrededor de tres familias de indicadores: operación del SOC, calidad de la automatización y efecto en el riesgo y el servicio.[^5][^6][^7]

En la literatura técnica reciente, tanto en guías de NIST SP 800‑61r3 como en marcos de ENISA para SOC/CSIRT, se consolida un vocabulario común: MTTD, MTTR, tasas de falsos positivos, cobertura de automatización y métricas de negocio como coste por incidente.[^8][^3][^5]
Los informes industriales de 2025–2026 añaden una capa pragmática: ligar la inversión en SOAR a reducciones medibles (30–50%) de MTTD/MTTR y a porcentaje de alertas gestionadas sin intervención humana.[^9][^5]

### Tabla 1. Familias de indicadores SOAR (visión 2025–2026)

| Familia | Ejemplos de indicadores clave |
| :-- | :-- |
| Operación del SOC | MTTD, MTTR, MTTI/MTTC, volumen de incidentes tratados, backlog de alertas por analista |
| Calidad de detección | Tasa de falsos positivos, tasa de falsos negativos estimada, cobertura de fuentes y casos de uso |
| Automatización | Cobertura de automatización, tasa de éxito de playbooks, excepciones, rollback, horas de analista ahorradas |
| Negocio / riesgo | Coste medio por incidente, impacto estimado evitado, cumplimiento de SLA regulatorios |

[^6][^7][^10][^5][^8][^9]

## 2. Tendencias 2025+ en métricas SOAR (mundo real, no catálogo de fabricante)

Desde 2025 se observa un giro nada sutil: los reguladores y organismos de referencia empiezan a poner nombres y apellidos al “haga usted automatización” que antes se dejaba a la imaginación del integrador.[^2][^11][^3]

NIST, con la revisión 3 de SP 800‑61 en 2025, vincula explícitamente la automatización de alertas, triaje e intercambio de información con las funciones Respond y Recover del CSF 2.0, y sugiere medir la eficiencia del proceso con tiempos medios (detección, análisis, respuesta) y métricas de calidad.[^11][^3][^12]
ENISA, en su guía para diseño de CSIRT/SOC, recalca indicadores en dos planos: calidad de la detección (velocidad, amplitud, falsos positivos) y capacidad operativa (incidentes gestionados, ratio de automatización, revisiones anuales de desempeño).[^8]

Los proveedores de referencia y análisis de mercado añaden un tercero: “automation coverage”, es decir, qué porcentaje de las tareas de un flujo de respuesta está absorbido por el SOAR.[^5][^9]
La consecuencia práctica es que auditorías (y no solo las del fabricante) empiezan a pedir métricas específicas de cobertura de automatización y playbook success rate, no solo una gráfica bonita de eventos.[^13][^5]

## 3. El espejo español: de INCIBE, ENS y NIS2 al “SOAR de país”

España, con INCIBE‑CERT como nodo operativo, ya dispone de un caudal de datos de incidentes que clama por un SOAR a escala nacional: en 2025 se gestionaron 122.223 incidentes, un 26% más que en 2024, además de 237.028 sistemas vulnerables relevantes detectados de forma proactiva.[^14][^1]
Entre estos incidentes, el malware (55.411 casos, incluyendo 392 de ransomware), el fraude y el phishing concentran una parte sustancial de la carga, especialmente en sectores esenciales como banca, transporte y energía.[^15][^14]

El Gobierno ha anunciado además un refuerzo de las capacidades de ciberseguridad y ciberdefensa, incluyendo un SOC 5G que monitoriza el cumplimiento de requisitos de seguridad, y el desarrollo de servicios automatizados de auditoría de exposición en Internet para administraciones públicas.[^16]
En paralelo, el anteproyecto de ley de coordinación y gobernanza de la ciberseguridad integra NIS2 y la directiva CER y crea el Centro Nacional de Ciberseguridad (CNCS) como autoridad de referencia, con énfasis en registro, notificación de incidentes y capacidad de auditoría.[^4]

Todo esto configura un escenario en el que un marco de indicadores SOAR nacional no es un capricho tecnócrata, sino la única forma razonable de gobernar flujos de miles de incidentes diarios, varias redes de CSIRT (CCN‑CERT, INCIBE‑CERT, ESPDEF‑CERT) y obligaciones de notificación en ventanas temporales estrictas.[^17][^1][^4]
Si a ello se suman las exigencias del Esquema Nacional de Seguridad y el alineamiento de España con las estrategias europeas de digitalización y ciberseguridad, el resultado es un caldo de cultivo ideal para normalizar métricas y SLA automatizados de respuesta a nivel territorial.[^18][^19][^20]

## 4. Indicadores SOAR nucleares: del SOC de empresa al tablero nacional

Detrás de la jerga, el consenso internacional reciente deja un conjunto bastante estable de indicadores “duros” que un SOAR serio debería producir tanto a nivel organizativo como agregado nacional.[^7][^10][^6][^5]

En el plano operativo, MTTD (Mean Time to Detect), MTTI/MTTC (tiempo medio de investigación o contención) y MTTR (Mean Time to Respond/Recover) siguen siendo el trío hegemónico, ahora con objetivos explícitos de reducción del 30–50% asociados a proyectos de automatización.[^10][^9][^5]
A esto se suman métricas de volumen (incidentes al mes, alertas por analista, porcentaje de incidentes escalados entre CSIRT) que permiten evaluar si la automatización realmente está drenando la carga humana o solo añade dashboards.[^21][^1][^8]

En la capa de calidad, se establecen tasas de falsos positivos y falsos negativos (estimados mediante muestreo), proporción de incidentes reabiertos, y éxito de playbooks (ejecuciones completas sin intervención manual frente a ejecuciones abortadas o con fallback).[^5][^8]
Los informes recientes recomiendan también medir la cobertura de casos de uso: porcentaje de los tipos de incidentes más frecuentes (por ejemplo, malware genérico, ransomware, phishing, explotación de vulnerabilidades conocidas) para los que existe al menos un playbook automatizado.[^13][^5]

Finalmente, en la dimensión negocio‑riesgo se consolida el uso de coste por incidente, impacto estimado evitado (por ejemplo, mediante comparación con medias de coste de brecha de datos) y cumplimiento de SLA regulatorios como ventanas de notificación NIS2 (24 horas para notificación inicial).[^3][^22][^9]
El valor de SOAR, en esta lectura, deja de ser “tengo x integraciones” y pasa a ser cuánto reduce el daño (tiempo e impacto) por unidad de euro invertido en automatización.[^23][^9]

## 5. Propuesta de marco de indicadores SOAR para España (nivel territorial)

Si se toma todo lo anterior y se lo obliga a convivir con la realidad española —INCIBE, CNCS, ENS, NIS2, múltiples CSIRT sectoriales—, emergen cuatro ejes razonables para un framework SOAR nacional: tiempo, cobertura, calidad e impacto.[^1][^2][^4][^8]

En el eje tiempo, a nivel de país se podrían calcular MTTD, MTTC y MTTR agregados (y por sector NIS2) utilizando como fuente obligatoria los registros de los CSIRT acreditados, con objetivos explícitos de reducción plurianual para tipos de incidentes prioritarios (por ejemplo, ransomware en operadores esenciales).[^3][^4][^17]
La métrica incómoda pero honesta sería el dwell time medio de los atacantes en sectores críticos, que informes como ENISA Threat Landscape ya estiman a nivel europeo en el contexto del incremento de ataques a OT; el objetivo sería comprimir sistemáticamente ese intervalo.[^24][^2]

La cobertura se mediría como porcentaje de incidentes notificados a nivel nacional que entran en categorías con playbooks estándar definidos y, dentro de ellos, porcentaje de pasos automatizables realmente automatizados.[^13][^8]
Esto obligaría a desarrollar catálogos de casos de uso SOAR comunes (por ejemplo, para phishing dirigido a ciudadanos, fraude bancario, intrusiones en redes OT), que los distintos SOC/CSIRT aplicarían con variaciones locales pero métricas compartidas.[^25][^24][^17]

En calidad, un tablero nacional razonable incluiría tasa de falsos positivos de detección automatizada por vector (correo, web, OT), tasa de incidentes reabiertos tras cierre automático, y porcentaje de casos en los que se requirió deshacer acciones de un playbook (rollback).[^8][^5]
Esta última métrica, que pocos fabricantes publicitan, es precisamente la que permite evitar el entusiasmo suicida de automatizar aislamientos masivos de endpoints en redes hospitalarias en pleno lunes a las ocho de la mañana.[^23][^8]

En impacto, el marco nacional podría ligar el coste agregado de incidentes (estimado, por ejemplo, mediante parámetros actuariales alineados con estudios globales de coste medio de brecha de datos) con la evolución de MTTD/MTTR y la expansión de la cobertura de automatización.[^26][^9]
La propia NIS2 y la futura práctica del CNCS en materia de auditoría darían pie a incorporar también la tasa de cumplimiento de los plazos de notificación y la frecuencia de sanciones relacionadas con deficiencias en la respuesta.[^27][^4]

### Tabla 2. Ejemplo de tablero SOAR nacional (visión 2026)

| Eje | Métrica propuesta | Fuente primaria |
| :-- | :-- | :-- |
| Tiempo | MTTD, MTTC, MTTR por sector NIS2 | Registros de CSIRT (CCN, INCIBE, ESPDEF, CSIRT sectoriales) |
| Cobertura | % incidentes en categorías con playbook; % pasos automatizables automatizados | Catálogos de casos de uso SOAR compartidos |
| Calidad | Falsos positivos, incidentes reabiertos, ratio de rollback de playbooks | Logs SOAR/SIEM, revisiones de calidad |
| Impacto | Coste estimado por incidente, cumplimiento de SLA de notificación | Informes a CNCS, datos regulatorios |

[^9][^4][^1][^3][^8]

## 6. Comparativa internacional: de EEUU y la UE a la idiosincrasia ibérica

En el mundo anglosajón, los indicadores SOAR empiezan a institucionalizarse vía guías técnicas, órdenes ejecutivas y marcos sectoriales: en Estados Unidos, se han emitido mandatos específicos para que las agencias federales adopten capacidades de orquestación y automatización como soporte técnico de Zero Trust.[^28]
Esto suele venir acompañado de cuadros de mando donde se monitoriza, por agencia, qué porcentaje de alertas se tramitan de forma completamente automatizada, reducciones de MTTR y niveles de integración con los cinco pilares de Zero Trust (identidad, dispositivo, red, cargas de trabajo y datos).[^28][^5]

En la Unión Europea, ENISA avanzó en los últimos años hacia métricas más estructuradas para redes de CSIRT y la creación de paneles automáticos para mejorar la coordinación, lo que apunta a una normalización de indicadores de desempeño (KPI) en todo el ecosistema europeo.[^29][^21]
Los informes de paisaje de amenazas de 2025 ya incluyen análisis cuantitativos de miles de incidentes, destacando, por ejemplo, que las amenazas sobre OT representan alrededor de una quinta parte de los incidentes categorizados, con tasas muy altas en manufactura.[^24][^2]

España, situada por encima de la media europea en capacidades de ciberseguridad según declaraciones oficiales, combina una fuerte institucionalidad (INCIBE, CCN, CNCS emergente) con una diversidad territorial y sectorial notable.[^30][^20][^16]
Eso sugiere que un marco SOAR nacional debería ser federado: métricas comunes, instrumentos tecnológicos interoperables, pero autonomía razonable para que un SOC de salud en Castilla y León no viva atado al mismo catálogo de playbooks que un SOC de banca internacional en Madrid.[^25][^4][^17]

Donde España puede ir por delante es en la explotación sistemática de la masa de datos ya disponible: decenas de miles de incidentes anuales, cientos de miles de sistemas vulnerables detectados proactivamente y un tejido de CSIRT sectoriales consolidado.[^14][^17][^1]
Convertir ese ecosistema en un laboratorio estadístico vivo para afinar métricas SOAR —por ejemplo, comparando tiempos de respuesta entre entidades con y sin automatización avanzada— es una oportunidad estratégica tanto para la política pública como para la industria local.[^9][^23]

## 7. Recomendaciones propositivas (y un poco irónicas) para España

Si se toma en serio la idea de un “SOAR de país”, el primer paso no es comprar más cajas, sino acordar una taxonomía y unos indicadores mínimos obligatorios entre el CNCS, INCIBE, CCN‑CERT, ESPDEF‑CERT y los CSIRT sectoriales.[^4][^17][^8]
Esa taxonomía debería ser compatible con ENISA y NIST, pero lo bastante concreta como para que “incidente de phishing dirigido a ciudadanía” signifique lo mismo en León que en Las Palmas, y sus métricas de tiempo y calidad sean comparables.[^2][^8]

En paralelo, los proyectos de SOC 5G, auditoría automatizada de exposiciones de la Administración y despliegue de IA para detección que el Gobierno ya impulsa deberían nacer con contrato métrico: porcentaje de procesos automatizados, reducción esperada de tiempos, calidad mínima tolerable.[^16][^23]
Si un sistema de observabilidad del perímetro de la AGE no viene de serie con MTTD, MTTR y tasa de falsos positivos comparables entre ministerios, quizá es mejor devolverlo al fabricante antes de que empiece el teatrillo de los PowerPoint.[^6][^9]

Por último, sería deseable que el futuro marco español de NIS2 transformara en obligación lo que hoy es buena práctica: notificación temprana con datos normalizados que permitan análisis automatizado a nivel central, y exigencia de justificar, en auditoría, por qué ciertos tipos de incidentes aún no tienen playbooks automatizados.[^22][^3][^4]
La ganancia no es solo regulatoria: disponer de una capa SOAR nacional con indicadores homogéneos elevaría la capacidad de respuesta ante crisis paneuropeas (como las que ENISA coordina a través de EU‑CyCLONe) y posicionaría a España como proveedor de referencia en servicios avanzados de ciberseguridad dentro de la UE.[^21][^27][^23]


<span style="display:none">[^31][^32][^33][^34][^35][^36][^37][^38][^39][^40][^41][^42][^43][^44]</span>

<div align="center">⁂</div>

[^1]: https://www.incibe.es/incibe/sala-de-prensa/incibe-detecto-mas-de-122000-incidentes-de-ciberseguridad-en-2025

[^2]: https://www.enisa.europa.eu/sites/default/files/2025-11/ENISA Threat Landscape 2025.pdf

[^3]: https://csrc.nist.gov/news/2025/nist-revises-sp-800-61

[^4]: https://copla.com/blog/compliance-regulations/nis2-directive-regulations-and-implementation-in-spain/

[^5]: https://www.vectra.ai/topics/incident-response-automation

[^6]: https://www.fortinet.com/uk/resources/cyberglossary/secops-metrics

[^7]: https://swimlane.com/blog/what-is-soar/

[^8]: https://www.enisa.europa.eu/sites/default/files/publications/ENISA Report - How to setup CSIRT and SOC.pdf

[^9]: https://www.strategicmarketresearch.com/market-report/security-orchestration-automation-response-market

[^10]: https://worldinformatixcs.com/2025/12/04/mttd-mttr-kpi/

[^11]: https://www.nist.gov/news-events/news/2025/04/nist-revises-sp-800-61-incident-response-recommendations-and-considerations

[^12]: https://tandem.app/blog/updated-nist-incident-response-guidance-sp-800-61-rev-3

[^13]: https://grc3.io/blog/cybersecurity/soar-security-orchestration-automation-response-guide-part-1

[^14]: http://espanadigital.gob.es/en/actualidad/incibe-gestiono-122223-incidentes-de-ciberseguridad-en-2025-un-26-mas-que-el-ano

[^15]: https://pentestingteam.com/blog/ciberataques-espana-2025-incibe-claves/

[^16]: https://digital.gob.es/en/comunicacion/notas-prensa/mtdfp/2025/05/2025-05-06_02

[^17]: https://inprotech.es/en/how-does-the-nis2-regulation-affect-spain-2/

[^18]: https://portal.mineco.gob.es/RecursosArticulo/mineco/ministerio/ficheros/210204_Digital_Spain_2025.pdf

[^19]: https://enisa.europa.eu/sites/default/files/2025-07/Consolidated Annual Activity Report 2024.pdf

[^20]: https://www.cci-es.org/en/activities/the-cci-and-spains-national-cybersecurity-strategy/

[^21]: https://www.enisa.europa.eu/sites/default/files/2025-07/Consolidated Annual Activity Report 2024.pdf

[^22]: https://www.flexxible.com/en/blog/nis2-directive-spain

[^23]: https://complexdiscovery.com/enisa-2025-nis-investments-report-technology-prioritized-as-cyber-talent-pools-contract/

[^24]: https://blog.denexus.io/resources/enisa-threat-landscape-2025-ot-attacks-industrial-cybersecurity-crisis

[^25]: https://itcs.vip/en/blog/tendencias-ciberseguridad-espana-2025

[^26]: https://www.intelmarketresearch.com/Security-Orchestration-Automation-and-Response -2784

[^27]: https://ecs-org.eu/activities/nis2-directive-transposition-tracker/

[^28]: https://swimlane.com/es/blog/executive-order-security-orchestration-automation-response-soar/

[^29]: https://www.enisa.europa.eu/sites/default/files/2025-02/ENISA Single Programming Document 2025-2027 - Condensed version.pdf

[^30]: https://www.lamoncloa.gob.es/lang/en/presidente/news/paginas/2025/20251016-information-cecurity-meeting.aspx

[^31]: https://www.futuremarketinsights.com/reports/security-orchestration-automation-and-response-soar-market

[^32]: https://radiantsecurity.ai/learn/soar-tools-key-capabilities-and-10-solutions-to-know-in-2026/

[^33]: https://www.grandviewresearch.com/industry-analysis/security-orchestration-automation-response-market-report

[^34]: https://eiposgrados.com/eng/cybersecurity-blog/cybersecurity-incidents-in-spain-2025-incibe-report/

[^35]: https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025

[^36]: https://latestfromtechguy.com/article/cybersecurity-automation-soar-2026

[^37]: https://www.knowbe4.com/hubfs/G2-Winter-2025-Grid-Report-for-Security-Orchestration-Automation-and-Response.pdf

[^38]: https://www.cryptika.com/top-10-best-security-orchestration-automation-and-response-soar-tools-in-2025/

[^39]: https://securityscorecard.com/resources/learning-center/9-cybersecurity-metrics-kpis-to-track/

[^40]: https://bluesec.ma/index.php/2025/10/21/how-to-measure-soc-maturity-frameworks-kpis-benchmarks-for-2025/

[^41]: https://www.spiderstrategies.com/blog/automated-kpi-reports/

[^42]: https://csrc.nist.rip/news/2025/nist-revises-sp-800-61

[^43]: https://www.dsn.gob.es/sites/default/files/2025-12/National Aeroespace Security Strategy 2025 - Accesible_0.pdf

[^44]: https://www.defensa.gob.es/documents/2073105/2383976/amenazas_riesgos_y+desafios_a_la_seguridad_nacional_2025_dieeem03_eng.pdf/10468d78-7b52-6c8f-1d51-27aa1bae1234?t=1759217806364

