
# Informe FAIR.

El marco FAIR ha pasado, en pocos años, de ser una excentricidad cuantitativa a convertirse en la vara de medir respetable con la que los consejos de administración justifican (o cuestionan) presupuestos de ciberseguridad en millones de euros.  Desde 2025, la discusión ya no es si usar FAIR, sino qué indicadores concretos derivar de FAIR, cómo automatizarlos y cómo conectarlos con la contabilidad nacional del riesgo digital, especialmente en países como España donde la regulación europea aprieta más que el verano en Sevilla.[^1][^2][^3][^4][^5][^6]

## 1. FAIR hoy: estándar cuantitativo y tríada FAIR–CAM–MAM

FAIR se ha consolidado como estándar internacional para cuantificar el ciber-riesgo en términos financieros, sustituyendo las viejas escalas de “alto-medio-bajo” por probabilidades y distribuciones de pérdida anual esperada.  El modelo define el riesgo como la combinación de la frecuencia probable de eventos de pérdida (Loss Event Frequency, LEF) y la magnitud probable de la pérdida (Loss Magnitude, LM), lo que obliga a traducir logs, vulnerabilidades y percepciones de amenaza a números defendibles delante de un auditor o de Hacienda.[^7][^8][^9][^10][^11][^1]

Desde 2025 el FAIR Institute publica como estándar la versión 3.0 del modelo, y lo integra con dos piezas nuevas: FAIR-CAM (Controls Analytics Model) y FAIR-MAM (Materiality Assessment Model), formando un marco único de gestión de riesgo cuantitativo.  FAIR-CAM modela explícitamente cómo los controles (técnicos, organizativos, de detección, de respuesta) afectan a la frecuencia de eventos de amenaza y a la magnitud de la pérdida, mientras que FAIR-MAM se centra en la materialidad financiera de los incidentes, es decir, en hablar el idioma que entiende el CFO y, por extensión, el regulador.[^12][^13][^1]

En los informes globales de 2025, alrededor del 45% de las organizaciones declaran usar o planear usar FAIR para cuantificación del riesgo; entre quienes lo adoptan, cerca del 90% reportan resultados positivos en términos de alineamiento con negocio y priorización de inversiones.  El mensaje es claro: los indicadores FAIR han dejado de ser un experimento académico y se han convertido en una métrica de competitividad, no sólo de cumplimiento.[^2][^3][^14][^15][^16][^5]

### Tabla: piezas del estándar FAIR actualizado

| Elemento | Rol principal | Indicadores clave que habilita |
| :-- | :-- | :-- |
| FAIR v3.0 | Modelo base de riesgo (LEF × LM) [^1][^10] | Frecuencia de eventos de pérdida, pérdida anual |
| FAIR‑CAM | Modelo de eficacia de controles [^12][^13] | Reducción de TEF, variación en LM por madurez |
| FAIR‑MAM | Materialidad financiera [^12][^11] | Umbrales de impacto, escenarios “materiales” |

## 2. Indicadores FAIR “clásicos”: de la teoría a los cuadros de mando

La gracia de FAIR no está en las definiciones —razonablemente sobrias— sino en los indicadores que fuerza a construir cuando uno lo aplica en serio a nivel organizativo o nacional.  La estructura básica es conocida: la frecuencia de eventos de pérdida se deriva de la frecuencia de eventos de amenaza (Threat Event Frequency, TEF) y de la vulnerabilidad (probabilidad de que el evento de amenaza se convierta en pérdida), mientras que la magnitud de la pérdida se descompone en formas de pérdida primarias y secundarias (productividad, respuesta, sustitución, reputación, sanciones, etc.).[^8][^17][^9][^10][^7][^1]

A nivel de indicadores, desde 2025 se observan tendencias claras en cómo las organizaciones —y algunos proyectos nacionales— utilizan FAIR:

1. **Indicadores de frecuencia (LEF, TEF, vulnerabilidad)**
Se generaliza la estimación de Loss Event Frequency como distribución anual, apoyada en históricos de incidentes, inteligencia de amenazas y, cada vez más, simulaciones (Monte Carlo, modelos bayesianos) que permiten capturar la incertidumbre.  Threat Event Frequency se alimenta con índices de actividad de actores de amenaza, mapeados a marcos como MITRE ATT\&CK y los catálogos de controles de NIST, CIS o similares, mientras que la vulnerabilidad se estima comparando la “capacidad del atacante” con la “fuerza de control” existente.[^18][^13][^19][^3][^20][^12][^1]
2. **Indicadores de magnitud de pérdida (LM)**
El FAIR Institute insiste en seis grandes formas de pérdida: productividad, respuesta, sustitución, multas y sanciones, pérdida de ingresos y daños reputacionales, que se agrupan en indicadores de pérdida primaria (operativa) y secundaria (mercado, regulación, reputación).  En los cuadros de mando de 2025 se observa un énfasis especial en separar explícitamente las multas regulatorias (GDPR, NIS2) y los costes de litigios, reflejando la presión normativa global y, en el caso europeo, particularmente intensa.[^17][^10][^3][^4][^7][^12][^2]
3. **Pérdida anual esperada (Annualized Loss Exposure) y curvas de valor‑en‑riesgo**
La combinación de LEF y LM produce indicadores como la pérdida anual esperada en euros, percentiles de pérdidas (por ejemplo, “pérdida con 95% de confianza”) y curvas de riesgo que recuerdan a las del valor‑en‑riesgo financiero, lo que hace muy feliz a los actuarios y al Banco Central de turno.  Estos indicadores se utilizan para priorizar programas de mitigación y para demostrar, con números, la eficacia marginal de un control adicional.[^13][^19][^3][^15][^16][^12][^1]
4. **Indicadores de eficacia de controles (FAIR‑CAM)**
FAIR‑CAM introduce indicadores sobre la “operational efficacy” de los controles: capacidad, cobertura y fiabilidad, así como su contribución cuantitativa a la reducción de TEF y LM.  En la práctica, esto se traduce en métricas como “reducción porcentual de probabilidad de intrusión por mejora de EDR” o “impacto de la segmentación de red en el número de escenarios de compromiso crítico”, conectadas con el lenguaje FAIR.[^21][^3][^15][^20][^12][^13]
5. **Indicadores de materialidad (FAIR‑MAM)**
FAIR‑MAM propone umbrales de materialidad basados en ratios financieros (porcentaje de ingresos, EBITDA, capitalización) y en la comparativa con riesgos operacionales tradicionales, produciendo indicadores binarios (“escenario material / no material”) y niveles de prioridad para reporting financiero.  Esta capa resulta especialmente relevante para el debate nacional, porque acerca el ciber-riesgo a los supervisores financieros y a los bancos centrales que comienzan a considerar el riesgo cibernético dentro de sus pruebas de estrés.[^19][^3][^11][^22][^16][^5][^12]

## 3. Tendencias 2025+ en métricas FAIR: automatización, IA y cuantificación de país

La novedad desde 2025 no está tanto en nuevas definiciones como en tres movimientos: la automatización (FAIR deja de hacerse “a mano”), la integración con IA y datos masivos, y la extensión desde el ámbito corporativo al territorial o nacional.[^3][^12][^19][^2]

En el plano metodológico, surgen enfoques bayesianos que integran FAIR con modelos probabilísticos más ricos, permitiendo actualizar indicadores a medida que se dispone de nuevos datos de incidentes o inteligencia de amenazas.  Estudios recientes emplean redes bayesianas para cuantificar el riesgo financiero cibernético, citando FAIR como base conceptual, pero añadiendo capas de KPIs específicos de la organización (tiempo medio de detección, ratios de parches aplicados, densidad de vulnerabilidades críticas por activo, etc.), lo que facilita un aterrizaje hacia indicadores operativos profundamente cuantitativos.[^20][^6][^19][^3]

En la práctica industrial, además del ecosistema internacional de plataformas de cuantificación, aparecen iniciativas europeas y españolas que utilizan FAIR como motor interno y lo combinan con IA y simulación Monte Carlo.  Por ejemplo, plataformas desarrolladas en España, como Armatum dentro del grupo ABAI, declaran explícitamente basarse en el estándar Open FAIR, el catálogo de controles CIS y técnicas de simulación Monte Carlo para ofrecer a empresas un cálculo de pérdida económica en distintos escenarios y recomendar la inversión óptima en controles.[^23][^6][^3][^20]

Proyectos europeos orientados a infraestructuras críticas, como estudios sobre cuantificación del riesgo OT o iniciativas de I+D como DICYME, también adoptan FAIR como base, integrándolo con indicadores específicos de amenaza (índice de actividad de actores, mapeo a ATT\&CK, indicadores de vulnerabilidad en tiempo real) y con motores de IA para generar índices de ciberriesgo más agregados.  Esta combinación da lugar a indicadores como “índice de ciberriesgo OT sectorial”, “probabilidad anual de incidente severo en la red industrial nacional” o “elasticidad de pérdida frente a inversión en controles”, todos ellos anclados en la semántica FAIR.[^6][^3][^20]

A nivel global, los informes de mercado de cuantificación de ciber-riesgo señalan explícitamente a FAIR como el marco dominante y describen una tendencia a estandarizar métricas de riesgo en términos financieros, especialmente para facilitar comparaciones entre sectores y países.  La discusión ya no es si se deben producir métricas FAIR, sino hasta qué punto se pueden compartir y homogeneizar sin traicionar las particularidades de cada ecosistema de amenaza.[^14][^22][^15][^16][^5][^2][^3]

## 4. España: FAIR, infraestructuras críticas y el arte de cuantificar el desastre

En el contexto español, FAIR empieza a abandonar discretamente los powerpoints para instalarse en la mesa —a veces metafórica, a veces muy literal— donde se discuten incidentes nacionales.  La narrativa del gran apagón eléctrico de 2025, que afectó a España, Portugal y parte de Francia durante varias horas, ofrece un ejemplo ilustrativo de cómo se utiliza FAIR en la práctica para dimensionar daños: informes jurídicos y de gestión de crisis describen explícitamente el uso del modelo FAIR para estimar superficie comprometida, datos filtrados y coste económico aproximado del incidente.[^4][^3][^20][^6]

En paralelo, el entorno regulatorio nacional —muy influido por GDPR y NIS2, además de la normativa específica sobre infraestructuras críticas— obliga a incorporar en la cuantificación FAIR la probabilidad de sanciones, la necesidad de notificación a autoridades como la AEPD o el CNPIC y los costes de coordinación regulatoria.  Estos componentes se traducen en indicadores de riesgo secundarios: probabilidad anual de sanción, exposición a multas por sector, coste esperado de notificación y gestión de crisis regulatoria, todos dentro de la estructura de Loss Magnitude.[^17][^4][^6]

En el ecosistema empresarial español, iniciativas industriales y centros tecnológicos empiezan a explotar FAIR para transformar métricas técnicas en indicadores económicos entendibles por la alta dirección y por aseguradoras.  Informes sobre “ciberseguridad inteligente” elaborados por centros de innovación regionales describen explícitamente cómo la cuantificación FAIR permite expresar la probabilidad y el impacto económico de los ciber-escenarios, convirtiendo indicadores como número de vulnerabilidades críticas, tiempo de exposición, cobertura de copias de seguridad o nivel de segmentación en euros de pérdida esperada.[^23][^20][^6]

Proyectos de I+D financiados en España y en el entorno europeo, como la calculadora de ciberriesgo DICYME, se apoyan en FAIR pero añaden indicadores derivados de ciencia de datos e IA, como índices de actores de amenaza, mapas de vulnerabilidades enlazados con MITRE ATT\&CK y series temporales de severidad de incidentes, con apariencia de cuadro de mando nacional.  Aunque formalmente el objetivo es la empresa, la arquitectura de estos proyectos sugiere un potencial claro de escalado a nivel de sector o de país: basta agregar por CNAE, por región o por tipo de infraestructura crítica y mantener la semántica FAIR.[^3][^20]

Desde el punto de vista institucional, asociaciones como ISMS Forum trabajan en marcos estandarizados de indicadores de ciberseguridad para CISOs, que aunque no son puramente FAIR, empiezan a converger hacia la cuantificación económica y la explotación de modelos basados en riesgo, facilitando la futura adopción de FAIR como referencia tácita.  La conversación nacional se desplaza, lentamente pero con determinación, del “cumplimos ISO” al “cuánto nos cuesta no hacer nada”, con FAIR proporcionando la aritmética incómoda.[^24][^2][^6][^3]

## 5. Hacia indicadores FAIR territoriales: una propuesta para España comparada con el mundo

Aplicar FAIR a nivel nacional es, por definición, un deporte de riesgo: convertir la complejidad del tejido productivo, la diversidad de amenazas y la maraña regulatoria en indicadores cuantitativos exige una mezcla poco habitual de estadística, política y masoquismo. Aun así, las tendencias internacionales y las herramientas ya desplegadas apuntan a un conjunto razonable de indicadores FAIR “territoriales” que España podría adoptar y armonizar con otros países.[^5][^19][^2][^3]

En el eje de frecuencia, un marco nacional FAIR podría definir, por ejemplo, un “Índice de Frecuencia de Eventos de Pérdida Cibernética” por sector crítico, expresado como distribución de incidentes significativos por año, calibrado con datos de CSIRTs sectoriales, informes de aseguradoras y plataformas de cuantificación FAIR existentes.  Este índice se complementaría con un “Índice Nacional de Actividad de Amenazas”, derivado de inteligencia de amenazas y mapas ATT\&CK, que informaría el TEF a nivel país, y con un “Índice de Susceptibilidad” basado en madurez de controles (NIST CSF, ENS, etc.) para cada sector.[^13][^19][^20][^6][^3]

En el eje de magnitud, tendría sentido establecer indicadores de pérdida anual esperada por sector (en euros y como porcentaje del PIB sectorial), así como percentiles de pérdida extrema (por ejemplo, “pérdida con 99% de confianza en un incidente catastrófico de red eléctrica”), incorporando costes de productividad, respuesta, sustitución, reputación y sanciones regulatorias.  La experiencia del apagón de 2025, con estimaciones de pérdidas de alrededor de 1.600 millones de euros, ofrece una referencia empírica para calibrar estos indicadores en el caso de infraestructuras energéticas.[^12][^19][^4][^3]

Comparativamente, los países que más avanzan en cuantificación de riesgo —especialmente aquellos que integran FAIR en estudios de mercado, en modelos bayesianos de riesgo financiero y en plataformas de cuantificación para infraestructuras OT— se orientan hacia marcos nacionales donde la pérdida esperada y la materialidad se incorporan a ejercicios de estrés macrofinanciero.  España dispone de todos los ingredientes: regulación europea exigente, incidentes de referencia dolorosos, ecosistema FAIR emergente, industria aseguradora interesada y proyectos de I+D alineados con FAIR y con IA.  Lo que falta, como casi siempre, es la decisión de convertir estos indicadores en política pública: métricas FAIR obligatorias para infraestructuras críticas, exigencia de cuantificación económica en planes de seguridad y resiliencia, y quizá, por qué no, la publicación anual de un “Informe FAIR del Riesgo Cibernético en España” donde el Estado admita, con números, cuánto le puede costar la próxima tormenta digital.[^22][^19][^2][^4][^20][^5][^6][^3]

Si quisieras aterrizar esto en un informe FAIR concreto —por ejemplo, para el sector eléctrico español o para la administración pública—, ¿qué ámbito te interesa modelar primero: infraestructuras críticas, administración central, o sector privado regulado (banca, seguros, telecomunicaciones)?
<span style="display:none">[^25][^26][^27][^28][^29][^30][^31][^32][^33][^34][^35][^36][^37][^38][^39][^40][^41][^42][^43][^44]</span>

<div align="center">⁂</div>

[^1]: https://www.fairinstitute.org/hubfs/Standards Artifacts/Factor Analysis of Information Risk (FAIR) Standard v3.0 (January 2025).pdf

[^2]: https://www.fairinstitute.org/state-of-crm-2025

[^3]: https://blog.denexus.io/resources/operational-technology-cyber-risk-quantification-dsit-2025-study

[^4]: https://certuslegalfirm.com/en/comprehensive-guide-to-cybersecurity-crisis-management-doubts-and-lessons-from-the-great-spanish-blackout-of-2025/

[^5]: https://marketintelo.com/report/cyber-risk-quantification-market

[^6]: https://cdticextremadura.es/ebooks/Libro-Ciberseguridad-Empresas.pdf

[^7]: https://www.fairinstitute.org/blog/fair-risk-basics-what-is-loss-magnitude

[^8]: https://www.fairinstitute.org/blog/loss-event-frequency-explained-in-3-minutes-video

[^9]: https://www.techtarget.com/searchsecurity/tip/Using-the-FAIR-model-to-quantify-cyber-risk

[^10]: https://www.mimecast.com/content/factor-analysis-of-information-risk-fair-guide/

[^11]: https://jumpcloud.com/it-index/what-is-the-fair-model-a-guide-to-financial-risk-analysis

[^12]: https://1616664.fs1.hubspotusercontent-na1.net/hubfs/1616664/FAIR Institute -- Integrating FAIR Models for Cyber Risk Management (December 2024).pdf

[^13]: https://safe.security/fair-cam/

[^14]: https://www.fairinstitute.org/hubfs/State of Cyber Risk Management/FAIRInstitute_2025StateOfCyberRiskManagement%20Report_June2025.pdf

[^15]: https://www.optiv.com/insights/discover/blog/cyber-risk-quantification-crq-lessons-learned

[^16]: https://www.forvismazars.us/forsights/2025/09/from-guesswork-to-metrics-a-guide-to-measuring-cyber-risk

[^17]: https://www.cisecurity.org/insights/blog/fair-a-framework-for-revolutionizing-your-risk-analysis

[^18]: https://www.cybersaint.io/blog/a-pocket-guide-to-factor-analysis-of-information-risk-fair

[^19]: https://www.sciencedirect.com/science/article/pii/S0167404826000763

[^20]: https://dicyme.denexus.io/hubfs/20409508/E5.2 informe presentación resultados.pdf

[^21]: https://www.linkedin.com/posts/anshea_chatgpt-activity-7380706894581190656-gaL3

[^22]: https://blog.denexus.io/resources/extreme-cyberattacks-dont-blow-over-quickly-what-a-2-year-market-study-found

[^23]: https://www.abaigroup.com/armatum-la-primera-plataforma-que-utiliza-inteligencia-artificial-en-la-cuantificacion-del-ciber-riesgo/

[^24]: https://www.ismsforum.es/noticias/lista-noticias.php

[^25]: https://www.juntadeandalucia.es/datosabiertos/portal/actualidad/detalle/2296

[^26]: https://publications.iadb.org/es/fair-tech-radar-explorando-la-adopcion-de-inteligencia-artificial-en-america-latina-y-el-caribe

[^27]: https://datos.gob.es/es/etiquetas/principios-fair

[^28]: https://es.labvantage.com/blog/fair-data-principles-research-and-manufacturing/

[^29]: https://www.hotosm.org/es/herramientas-y-recursos/suite-de-productos-tecnologicos/fair/

[^30]: https://www.sentinelone.com/es/cybersecurity-101/cybersecurity/cyber-security-architecture/

[^31]: https://ticnova.es/blog/marcos-referencia-gestion-riesgo/

[^32]: https://www.sentinelone.com/es/cybersecurity-101/cybersecurity/cyber-maturity-assessment/

[^33]: https://producciocientifica.uv.es/documentos/68dfd721bfefdc7dda48cd96

[^34]: https://www.checkpoint.com/es/cyber-hub/cyber-security/what-is-a-cyber-security-architecture/

[^35]: https://es.scribd.com/document/985160189/FAIR-Para-Gestion-de-Riesgo

[^36]: https://www.youtube.com/watch?v=rHrXtH-IRRc

[^37]: https://es.linkedin.com/pulse/en-ciberseguridad-la-arquitectura-puede-hacer-diferencia-maye

[^38]: https://www.idbs.com/es/base-de-conocimientos/principios-de-datos-justos-en-gxp/

[^39]: https://www.linkedin.com/posts/fair-institute_cyberrisk-fair-cyberriskquantification-activity-7443396824943640576-hvrw

[^40]: https://www.youtube.com/watch?v=6nelMKVprSg

[^41]: https://files.mediaset.es/file/2023/0223/17/informe-de-sostenibilidad-2022-2-pdf.pdf

[^42]: https://igfspain.org/wp-content/uploads/2017/04/gobernanza_internet_spain_2015_pdf.pdf

[^43]: https://www.inditex.com/itxcomweb/api/media/80c8400b-4c0a-474e-82bd-c482bcba19f9/InformedeSostenibilidad.pdf?t=1773333742399

[^44]: https://www.lacnic.net/innovaportal/file/7769/1/solano-guia-de-gobernanza-desarrollo-y-adopcion-de-la-ia.pdf

