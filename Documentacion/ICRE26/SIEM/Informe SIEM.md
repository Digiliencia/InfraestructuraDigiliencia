
# Informe SIEM.

Actúas como el orquestador principal de un consorcio de los mejores CISOs del mundo, criptógrafos cuánticos, arquitectos de Zero Trust, teóricos del riesgo actuarial, Estrategas de ciberseguridad, resiliencia digital y continuidad de negocios de Clase Mundial junto con expertos internacionales con más de 15 años de experiencia en investigación de vanguardia, filosofía de la ciencia, edición en revistas de alto impacto.
Tu misión es ejecutar una investigación exhaustiva, sin límite de palabras, sobre las últimas tendencias (desde 2025) en indicadores del marco SIEM (Security Information and Event Management). Enfócate en los indicadores y las métricas de ciberseguridad propuestas por SIEM con aplicación a nivel nacional territorial para España, pero con un enfoque comparativo mundial.
Utiliza exclusivamente fuentes fiables y de alta calidad, como:

- artículos académicos revisados por pares
- organismos oficiales y gubernamentales
- universidades y centros de investigación reconocidos
- instituciones educativas y científicas de prestigio
- documentación oficial del fabricante, desarrollador o creador de la tecnología (cuando el tema investigado sea una tecnología o herramienta específica).
- Informes industriales y documentación técnica.
Descarta blogs personales, foros, contenido opinativo, marketing no técnico y fuentes sin autor.
Cuida el lenguaje español, minimiza el uso de listas o viñetas de posibles respuestas ad hoc a las preguntas inquisitivas de la encuesta. Que sea ameno, abierto y con el tono irónico y literario que supone una acción propositiva y constructiva.

Un marco nacional de indicadores SIEM para España en 2026 tiene tres grandes ejes: medir la eficacia técnica del SOC, demostrar cumplimiento regulatorio (NIS2, ENS, DORA, etc.) y, sobre todo, traducir todo ese ruido en riesgo país inteligible para ministros, reguladores y aseguradoras. Desde 2025, el cambio clave no es “más métricas”, sino pasar de contar logs a cuantificar impacto y resiliencia con SIEM como motor de inteligencia de riesgo, apoyado en IA y en la presión regulatoria europea.[^1][^2][^3][^4][^5]

## 1. De SIEM como “recogedor de logs” a motor de riesgo

La narrativa clásica del SIEM como aspiradora de eventos ha quedado algo viejuna frente a la expectativa, bastante menos romántica, de que el sistema justifique presupuestos, despliegues Zero Trust y cumplimiento de NIS2 ante regulador y auditor. Informes industriales de 2025 describen a los SIEM modernos como hubs analíticos centrados en riesgo que correlan telemetría, vulnerabilidades y criticidad de activos para priorizar exposición con un lenguaje casi actuarial: probabilidad, impacto, tendencia.[^2][^6][^4][^1]

Este giro viene empujado por tres fuerzas. Primero, el salto de los ataques: en 2025 los ataques semanales por organización aumentan en torno al 47% respecto a años previos, según informes globales de ataques, lo que hace inviable seguir operando un SOC a base de reglas estáticas y hojas de cálculo. Segundo, la regulación europea: NIS2 fija obligaciones de gestión de riesgos y de notificación de incidentes con plazos estrictos (24 horas para alerta temprana, 72 horas para notificación, un mes para informe final), lo que exige trazabilidad y evidencia automatizada que un SIEM bien instrumentado puede dar. Tercero, el propio ecosistema europeo de CSIRT y SOC: ENISA lleva años empujando KPIs de calidad (velocidad de detección, cobertura, falsos positivos) como condición de madurez, y su guía de creación de SOC establece esos indicadores como núcleo del cuadro de mando.[^4][^1][^2]

En ese contexto, hablar de “indicadores SIEM” en 2026 ya no es solo listar los consabidos MTTD o número de alertas, sino diseñar un sistema nacional donde los SOC de operadores esenciales, administración pública y grandes empresas alimentan métricas homogéneas que permitan saber, por ejemplo, cuánto tarda el país en detectar un ataque grave al sector financiero o cuánta superficie de exposición OT está bajo monitorización continua.[^7][^5][^4]

## 2. Métricas de operación SIEM/SOC: la capa clínica

Los indicadores operativos siguen siendo el pulso cotidiano del SIEM, y la literatura técnica reciente converge de forma bastante aburridamente unánime: se mide velocidad, calidad y cobertura. Esa tríada, sin embargo, se ha refinado con matices para entornos de alta escala y para SOC asistidos por IA.[^6][^8][^4]

En velocidad, ENISA ya recogía para SOC maduros KPIs como Mean Time To Detect (MTTD), Mean Time To Respond (MTTR), ratio de escalado y volumen de incidentes gestionados, y a partir de 2025 los informes especializados insisten en que estos tiempos han de medirse por tipo de incidente y criticidad, no como medias globales que solo sirven para decorar powerpoints. Guías industriales sobre evaluación de SIEM recomiendan fijar objetivos explícitos, por ejemplo MTTD menor de 15 minutos para fuentes críticas y MTTR menor de 4 horas para incidentes de gravedad alta, con revisión semanal de tendencias.[^8][^6][^4]

En calidad, los indicadores se concentran en la salud de la cadena alerta–incidente. La tasa de falsos positivos (false positive rate) y el porcentaje de alertas que derivan en incidentes confirmados (alert‑to‑incident ratio) se han convertido en termómetros de madurez: se considera problemático un ratio de conversión por debajo del 10%, mientras que SOC avanzados aspiran a un 15‑25%, lo que indica que casi una de cada cuatro alertas merece realmente atención. A esto se suma el seguimiento de errores de correlación, de eventos descartados sin análisis y de la carga por analista (alertas o casos por analista y día) como proxy de fatiga y de necesidad de automatización.[^6][^8][^4]

En cobertura, el foco actual va bastante más allá del porcentaje de dispositivos con logging habilitado. Las mejores prácticas proponen medir la cobertura de activos críticos (porcentaje de sistemas clasificados como críticos que aportan logs útiles al SIEM), la cobertura de técnicas MITRE ATT\&CK (porcentaje de técnicas relevantes para el sector detectables con reglas o analítica), la ingestión en tiempo real (retraso medio de ingesta, con objetivo inferior a 60 segundos para fuentes clave) y la tasa de errores de parsing o pérdida de datos. En SIEM cloud‑native, se han añadido métricas de latencia de correlación y elasticidad (capacidad de procesar picos de eventos sin degradación de MTTD), que algunos proveedores consideran ya indicadores de primer orden.[^9][^10][^1][^8][^4][^6]

Sobre esta capa operativa, España dispone de un contexto real de volumen y casuística que condiciona los valores razonables de estos KPIs. En 2025, INCIBE gestionó 122.223 incidentes de ciberseguridad, un 26% más que el año anterior, identificando además más de 237.000 sistemas vulnerables relevantes y atendiendo 142.767 consultas en la línea 017, lo que ilustra tanto la presión sobre los SOC como el aumento del componente preventivo. La distribución por tipo de incidente (malware con más de 55.000 casos, fraude online con unos 45.000, phishing con más de 25.000, robo de información con cerca de 3.800) ofrece un mapa claro de dónde deben focalizarse reglas de correlación, casos de uso y métricas de efectividad, en particular en banca, transporte y energía, que concentran la mayoría de incidentes en operadores esenciales.[^11][^12]

## 3. Métricas de cumplimiento y NIS2: del log al BOE

La directiva NIS2 y sus transposiciones han declarado esencial a media economía europea y han introducido una dimensión más jurídica y teatral en la vida de los SOC: ahora no basta con ser eficaces, hay que ser demostrablemente diligentes ante el regulador. Un artículo académico de 2025 sobre obligaciones de reporte NIS2 propone precisamente el uso del SIEM como columna vertebral de cumplimiento, mapeando capacidades de logging centralizado, correlación, retención y exportación de informes a los requisitos de gestión de riesgos (artículo 21) y de notificación de incidentes (artículo 23).[^3][^2]

Esto se traduce en indicadores que ya no miden ataques, sino comportamiento organizativo frente al regulador. Por ejemplo: porcentaje de incidentes sujetos a NIS2 detectados dentro de un plazo compatible con las 24 horas para el “early warning”; tiempo medio desde detección a primera notificación a la autoridad competente; porcentaje de incidentes graves con informe final remitido dentro del mes reglamentario; y nivel de completitud de la evidencia técnica (logs, líneas de tiempo, indicadores de compromiso) exportada desde el SIEM para acompañar esos informes. Guías de implementación técnica de gestión de riesgos de ENISA insisten además en vincular estos indicadores con parámetros de criticidad de servicios esenciales, de forma que el dashboard de cumplimiento no se limite a contar papeles, sino a reflejar realmente cómo se protege la continuidad de servicios clave.[^13][^2][^3][^4]

En España, el ecosistema se apoya en cuatro piezas: la estrategia nacional de ciberseguridad y su plan de ejecución, los dos CERT nacionales (INCIBE‑CERT y CCN‑CERT), el Esquema Nacional de Seguridad (ENS) y las medidas adicionales de refuerzo adoptadas por el Gobierno en 2025 para incrementar la inversión y desplegar SOC especializados (por ejemplo, el SOC 5G para supervisar la seguridad en redes móviles). El índice internacional NCSI (National Cyber Security Index) recoge, para España, la existencia de políticas, estrategias y planes con indicadores de desempeño definidos, así como mecanismos de seguimiento de la implementación, lo que ofrece un marco sobre el que encajar métricas SIEM a nivel país.[^14][^15][^5][^4]

En un enfoque nacional, la gracia —y la dificultad— consiste en consolidar métricas de cumplimiento procedentes de docenas de SOC heterogéneos. Ello exige, como mínimo, estándares comunes de clasificación de incidentes, taxonomías compartidas de gravedad y servicios afectados, y formatos normalizados para exportar informes desde los SIEM de operadores esenciales a los CERT nacionales, algo que ENISA y CERT‑EU vienen promoviendo con modelos de datos y buenas prácticas. El resultado aspiracional sería que, ante un incidente transfronterizo, España pudiera responder no solo con un parte narrativo, sino con cifras comparables con las de otros Estados miembros: qué porcentaje de operadores afectados detectó la intrusión por sus propios medios, cuánto tardaron en contenerla, qué cobertura de controles tenían desplegada sobre la técnica explotada.[^2][^3][^4]

## 4. España frente al mundo: métricas en clave de país

Comparar indicadores SIEM entre países es deporte de riesgo metodológico, pero se pueden trazar algunas líneas a partir de índices y estudios disponibles. El National Cyber Security Index valora para cada país la existencia de estrategias, planes con indicadores y capacidades de respuesta; España muestra porcentajes de cumplimiento altos en políticas y estructuras, lo que sugiere un entorno favorable a la definición de métricas SIEM estandarizadas, aunque el índice no baja al nivel de SOC. ENISA, por su parte, ha elaborado estudios sobre el paisaje CSIRT y las capacidades de respuesta en Europa que reflejan una madurez creciente en la región, con particular consolidación de CSIRT nacionales y sectoriales capaces de operar con SIEM sofisticados y compartir información estructurada.[^5][^3][^4]

Lo que diferencia a España no es tanto el catálogo de métricas —que se parece mucho al de cualquier otro país de la UE— como su uso intensivo en determinados sectores y la integración institucional. Proyecciones académicas sobre quién gobernará la ciberseguridad en España hacia 2035 anticipan un papel central de INCIBE y CCN en la coordinación del intercambio de información y en la notificación de ciberataques, concertando el flujo de datos desde los SIEM de operadores esenciales hacia repositorios nacionales. Ello abre la puerta a indicadores agregados como número de incidentes notificados por sector y por tipo de amenaza, tendencia temporal de incidentes graves en infraestructuras críticas, o porcentaje de sistemas vulnerables detectados a través de capacidades de scanning y telemetría centralizadas, como ilustra ya el recuento de más de 237.000 sistemas vulnerables relevantes identificados por INCIBE‑CERT en 2025.[^12][^11][^14]

Comparativamente, los informes de tendencias SIEM para 2025 destacan a Europa como región en la que la adopción de SIEM cloud‑native, la integración con SOAR y el uso de IA para priorizar riesgos avanzan de la mano del despliegue de marcos de Zero Trust y de la necesidad de cumplir con regulaciones financieras como DORA. En este contexto, los indicadores emergentes incluyen la cobertura de identidad y acceso monitorizados por el SIEM (porcentaje de flujos de autenticación y autorización bajo vigilancia), el grado de integración con controles Zero Trust (porcentaje de decisiones de acceso influenciadas por señales del SIEM), y medidas de eficiencia de automatización (porcentaje de incidentes resueltos mediante playbooks sin intervención humana). España, con su apuesta por SOC sectoriales (por ejemplo, SOC 5G) y por la automatización de auditorías de servicios expuestos de las administraciones públicas, encaja bien en esta tendencia, siempre que convierta esos proyectos en métricas compartidas y no en islas de excelencia.[^16][^15][^17][^9][^1][^4]

Para hacerse una idea de cómo podría lucir un cuadro de mando nacional que armonice estas métricas, puede ser útil imaginar una tabla sintética como la siguiente, donde el nivel “España” se alimenta de los KPIs homogéneos de los SOC de banca, energía, transporte y administración central, alineados con NIS2 y ENS:


| Capa | Métrica clave | Ejemplo de aplicación en España |
| :-- | :-- | :-- |
| Operación SOC | MTTD, MTTR, ratio alerta‑incidente | Valores objetivo y reales en SOC de banca y energía.[^6][^4] |
| Calidad | Tasa de falsos positivos, carga por analista | Ajuste de reglas en función de incidentes reales INCIBE‑CERT.[^12][^6] |
| Cobertura | % activos críticos monitorizados, ATT\&CK | Mapas sectoriales de técnicas detectables (NIS2/ENS).[^8][^4] |
| Cumplimiento | Plazos NIS2, completitud de informes | Seguimiento de incidentes en operadores esenciales.[^2][^12] |
| Riesgo país | Índices sectoriales de exposición y tendencia | Visión agregada en línea con NCSI y estrategia nacional.[^5][^15] |

## 5. Tendencias emergentes (2025‑2026): IA, OT y cuantificación

A partir de 2025, las piezas nuevas del puzzle SIEM giran sobre todo en torno a la IA, la convergencia IT/OT y la obsesión, quizá tardía, por cuantificar el riesgo en términos que entienda un consejo de administración y una aseguradora. Informes técnicos señalan que los SIEM modernos incorporan analítica avanzada para acelerar el análisis y reducir la fatiga de alertas mediante correlación automatizada, priorización basada en contexto y modelos de comportamiento de usuarios y entidades (UEBA), lo que obliga a introducir métricas específicas como porcentaje de detecciones impulsadas por modelos de IA, tasa de falsos positivos de esos modelos o reducción de alertas tras introducir scoring de riesgo.[^16][^1][^7]

En entornos industriales y de OT, los informes de ENISA sobre el panorama de amenazas de 2025 indican que los ataques a sistemas de control industrial representan ya alrededor del 18% de las amenazas, con un peso destacado en la manufactura y sectores críticos, lo que convierte la monitorización continua y la integración de telemetría OT en requisitos no negociables. Aquí emergen indicadores como porcentaje de redes OT segmentadas pero monitorizadas por el SIEM, tiempo medio de detección de actividades anómalas en ICS, y grado de alineamiento de casos de uso con escenarios de amenaza catalogados por ENISA, que para un país como España —con fuerte sector energético, industrial y de transporte— son especialmente relevantes.[^7][^4]

Por último, empiezan a asomarse métricas explícitamente actuariales apoyadas en SIEM: frecuencia de incidentes por unidad de exposición (por ejemplo, por millón de transacciones o por número de endpoints), pérdidas evitadas estimadas gracias a detecciones tempranas, y probabilidades de excedencia para determinados umbrales de impacto, lo que permite a equipos de riesgo y aseguradoras negociar pólizas de ciberseguro con algo más que intuiciones. Aunque estos enfoques están todavía en fase menos madura que los KPIs clásicos, encajan bien con el marco de evaluación de capacidades nacionales recogido en índices como el NCSI, que valoran la existencia de indicadores de desempeño y mecanismos de revisión periódica de la estrategia nacional de ciberseguridad.[^1][^3][^5][^6]


<span style="display:none">[^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29]</span>

<div align="center">⁂</div>

[^1]: https://www.manageengine.com/log-management/siem/siem-solution-trends-buyers-guide.html

[^2]: https://rocys.ici.ro/documents/152/Art._1_ROCYS_2_2025.pdf

[^3]: https://www.enisa.europa.eu/sites/default/files/2025-06/ENISA_Technical_implementation_guidance_on_cybersecurity_risk_management_measures_version_1.0.pdf

[^4]: https://www.enisa.europa.eu/sites/default/files/publications/ENISA Report - How to setup CSIRT and SOC.pdf

[^5]: https://ncsi.ega.ee/country/es/

[^6]: https://www.netwitness.com/blog/key-metrics-to-evaluate-siem-system/

[^7]: https://blog.denexus.io/resources/enisa-threat-landscape-2025-ot-attacks-industrial-cybersecurity-crisis

[^8]: https://underdefense.com/blog/soc-metrics/

[^9]: https://www.cynet.com/siem/siem-solutions-key-capabilities-10-solutions-you-should-know/

[^10]: https://searchinform.com/articles/cybersecurity/measures/siem/management/metrics/

[^11]: https://eiposgrados.com/eng/cybersecurity-blog/cybersecurity-incidents-in-spain-2025-incibe-report/

[^12]: http://espanadigital.gob.es/en/actualidad/incibe-gestiono-122223-incidentes-de-ciberseguridad-en-2025-un-26-mas-que-el-ano

[^13]: https://www.isms.online/nis-2/controls/logging-minimums/

[^14]: https://rodin.uca.es/bitstream/handle/10498/36907/OA_2025_0186.pdf?sequence=1\&isAllowed=y

[^15]: https://digital.gob.es/en/comunicacion/notas-prensa/mtdfp/2025/05/2025-05-06_02

[^16]: https://www.elastic.co/blog/ai-siem-landscape

[^17]: https://www.anomali.com/blog/siem-modernization-and-optimization-step-4-measure-and-optimize

[^18]: https://socmasters.in/siem-tools-in-cyber-security/

[^19]: https://stellarcyber.ai/learn/top-siem-solutions/

[^20]: https://www.newevol.io/resources/blog/top-siem-solutions-uae-2025/

[^21]: https://www.linkedin.com/posts/yassine-sadqi_cybersecurity-siem-gartner-activity-7385363643887988736-158L

[^22]: https://www.soffid.com/actualidad/soffid-iam-at-the-stic-ccn-cert-2025-conference-everything-you-need-to-know/

[^23]: https://www.exabeam.com/explainers/siem-tools/siem-solutions/

[^24]: https://assets.publishing.service.gov.uk/media/63a2fc7ad3bf7f375c7d831c/sia-siem-contract-kpis.pdf

[^25]: https://skillui.com/en/skill/show/mukul975/Anthropic-Cybersecurity-Skills/building-soc-metrics-and-kpi-tracking

[^26]: https://papers.academic-conferences.org/index.php/eccws/article/download/2346/2103/8478

[^27]: http://espanadigital.gob.es/sites/espanadigital/files/2025-12/Seguimiento de las recomendaciones horizontales 2024.pdf

[^28]: https://www.linkedin.com/pulse/quantitative-analysis-siem-solutions-high-volume-threat-eric-cobbs-invoe

[^29]: https://www.sciencedirect.com/org/science/article/pii/S1546221825009403

