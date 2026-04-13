
# Informe MITRE D3FEND.

MITRE D3FEND, desde 2025, ha dejado de ser un “árbol genealógico de controles” para convertirse en un sistema de medida: una ontología que permite definir, calcular y comparar métricas de defensa con una granularidad casi obscena, desde el sensor que ve un paquete hasta la política pública que intenta dormir tranquila en un Consejo de Ministros.[^1][^2][^3]

***

## 1. Qué es realmente D3FEND en 2026 (y por qué importa para medir)

MITRE D3FEND es una base de conocimiento y ontología de contramedidas de ciberseguridad que modela técnicas defensivas, artefactos digitales y relaciones con técnicas ofensivas (principalmente MITRE ATT\&CK) en un grafo semántico basado en OWL 2 DL. No es un checklist ni una “matriz más”, sino un lenguaje formal para razonar sobre coberturas, lagunas, telemetría y eficacia defensiva, con referencias cruzadas a estándares como CWE, NIST 800‑53 o DISA CCI.[^4][^5][^2][^1]

Desde la GA 1.0 (enero 2025) el grafo ha triplicado su tamaño respecto a la beta de 2021 y organiza más de 240 técnicas defensivas en tácticas como Model, Harden, Detect, Isolate, Deceive, Evict y Restore, extendidas en diciembre de 2025 al mundo OT (ICS/SCADA, IoT industrial, protocolos industriales). El lanzamiento de D3FEND CAD y su librería de grafos, junto con el extractor de CWE, marca el punto en que D3FEND deja de ser sólo documentación y se convierte en instrumento operativo para arquitectos, SOCs y reguladores que quieren medir algo más serio que el número de alertas por mes.[^5][^6][^2][^3][^7][^4]

***

## 2. De “matriz” a sistema de indicadores: cómo D3FEND propone medir

D3FEND no entrega un “cuadro de mando” predefinido, pero su estructura ontológica fuerza una forma de pensar en indicadores que va más allá de los KPIs decorativos habituales. El núcleo es el grafo: técnicas defensivas, artefactos digitales, sensores, debilidades (CWE) y técnicas ofensivas enlazados mediante relaciones tipadas (counters, monitors, protects, etc.), que son precisamente la materia prima de las métricas.[^3][^8][^1][^4]

El flujo típico de medición que se deriva de la propia documentación de D3FEND y de guías industriales recientes es algo así: se mapean técnicas ATT\&CK prioritarias, se identifican los artefactos afectados, se obtienen las técnicas D3FEND que pueden contrarrestarlas, se conectan con sensores y controles concretos, y solo entonces se definen SLIs y SLOs de eficacia, latencia y cobertura. Esta lógica se ha ido consolidando en 2025‑2026 en documentación profesional y técnica, que insiste en métricas como latencia de detección, cobertura de telemetría, tasa de éxito de mitigaciones o análisis sistemático de lagunas frente a ATT\&CK, todas ellas expresables sobre el grafo D3FEND.[^9][^8][^3]

***

## 3. Indicadores técnicos derivados de D3FEND (nivel micro)

En el plano micro, el propio ecosistema D3FEND y su documentación de CAD describen explícitamente qué tipos de inferencias pueden hacer los analistas, y eso se traduce directamente en métricas. CAD permite consultar, para un ataque o contramedida concreta, qué artefactos intervienen, qué técnicas defensivas son aplicables, qué sensores pueden vigilar esos artefactos, qué debilidades software (CWE) subyacen, y qué eventos están asociados; cada uno de esos conjuntos es un espacio de medida.[^1][^3]

Esto conduce, en la práctica, a indicadores tales como: número y proporción de artefactos críticos sin sensor asignado en el grafo, porcentaje de técnicas ATT\&CK relevantes que no tienen contramedida D3FEND instanciada en la arquitectura, densidad de mapeos CWE→técnicas defensivas desplegadas, o grado de instrumentación de una ruta de ataque modelada en CAD. Documentación industrial y formativa sobre D3FEND sugiere explícitamente métricas de latencia de detección (tiempo entre evento y alerta), tasa de éxito de mitigaciones, cobertura de telemetría y calidad de la observabilidad como SLIs/SLOs ligados a las técnicas D3FEND utilizadas.[^8][^9][^3]

***

## 4. Métricas de cobertura y eficacia (el matrimonio ATT\&CK–D3FEND)

La aportación menos aburrida de D3FEND es que, al abrazar ATT\&CK, permite pasar de “tenemos muchos controles” a “tenemos X por ciento de las técnicas del adversario razonablemente cubiertas”. Los informes técnicos y guías recientes de 2025 muestran estructuras de evaluación donde cada técnica ATT\&CK relevante se enlaza a una o varias contramedidas D3FEND y a controles concretos, marcando si la cobertura es completa, parcial o inexistente, y priorizando las lagunas.[^10][^11][^12][^5][^9]

Sobre esa malla ATT\&CK–D3FEND se derivan métricas como: porcentaje de técnicas ATT\&CK prioritarias completamente cubiertas por al menos una técnica D3FEND implementada, ratio de técnicas sólo parcialmente cubiertas, distribución de coberturas por táctica defensiva (Detect vs Harden vs Deceive, etc.) y densidad de contramedidas por técnica ofensiva crítica. Más sofisticado todavía, la integración con CWE permite medir la trazabilidad completa “debilidad→técnica ATT\&CK→contramedida D3FEND”, algo que MITRE ha señalado como objetivo para facilitar planificación de defensa centrada en vulnerabilidades y su mantenimiento automatizado mediante aprendizaje semi‑supervisado sobre literatura y datos abiertos.[^6][^2][^12][^4][^5][^9]

***

## 5. D3FEND CAD como fábrica de KPIs (y cómo se mide lo que no se ve)

El D3FEND CAD User Guide deja claro que los grafos CAD son realizaciones concretas de la ontología, con nodos de tipo Attack, Countermeasure, Artifact, Sensor, Vulnerability y Event sobre los que se aplican inferencias definidas. Esas inferencias (por ejemplo, “artefactos asociados a un ataque”, “técnicas defensivas aplicables”, “sensores posibles para un artefacto”, “debilidades asociadas”) permiten derivar, casi automáticamente, indicadores estructurales como profundidad de defensa, centralidad de nodos críticos o número de rutas de ataque sin defensa efectiva.[^7][^3]

La introducción en 2025 de una librería CAD de grafos reutilizables y de un IDE específico, documentados en los recursos oficiales de D3FEND, habilita la estandarización de análisis cuantitativos sobre arquitecturas complejas, incluyendo entornos OT. Informes y artículos técnicos a partir de esta herramienta señalan que se puede pasar de los diagramas estáticos en PowerPoint a grafos consultables en los que medir, por ejemplo, cuántos nodos de control protegen una función crítica, qué porcentaje de artefactos OT tiene sensores propuestos pero no implementados o qué subredes quedan fuera de cualquier trayectoria de detección.[^6][^3][^7]

***

## 6. Extensión OT 2025: nuevos indicadores para infraestructuras críticas

La extensión D3FEND para entornos OT, anunciada en diciembre de 2025, incorpora técnicas defensivas específicas para controladores industriales (PLC, RTU, DCS), sensores, actuadores, componentes de red OT y protocolos industriales. Mitre y la industria han enfatizado que es el primer marco estandarizado de contramedidas para estos sistemas, permitiendo aplicar la misma metodología de medición de coberturas y lagunas tanto en TI como en OT.[^2][^5]

Esto abre la puerta a indicadores frescos a nivel de infraestructuras esenciales: porcentaje de rutas de mando y control industrial cubiertas por segmentación y monitorización según D3FEND, proporción de funciones de seguridad instrumentadas con sensores recomendados por la ontología, densidad de técnicas de Harden y Detect aplicadas a protocolos críticos, o lagunas de Restore y Evict en escenarios de ransomware OT modelados en CAD. Para Estados que, como España, viven obsesionados con la continuidad de servicios esenciales, este tipo de métricas OT sobre D3FEND se vuelve particularmente atractivo para supervisores sectoriales y ejercicios de resiliencia.[^13][^14][^5][^9][^3]

***

## 7. De la métrica técnica al indicador nacional (España como caso)

España entra en esta conversación con una paradoja: un nivel de madurez reconocido internacionalmente (TIER 1 en el Global Cybersecurity Index de la UIT) y, al mismo tiempo, un crecimiento del 300% en ciberataques desde 2015, con más de 100.000 ataques detectados en 2024, uno muy grave cada tres días. El Gobierno ha reforzado en 2025 su apuesta en ciberseguridad y ciberdefensa con una inversión superior a 1.100 millones de euros, complementando el Plan Nacional de Ciberseguridad de 2022 y dentro de la estrategia España Digital 2025, con metas explícitas en talento y capacidades.[^15][^14][^13]

El modelo español se articula sobre un entramado institucional (INCIBE, Centro Criptológico Nacional, Mando Conjunto del Ciberespacio y, recientemente, el nuevo Centro Nacional de Ciberseguridad adscrito a Presidencia) y un marco jurídico–organizativo robusto que el propio Ejecutivo presenta como por encima de la media europea. Nada de esto menciona explícitamente D3FEND a día de hoy, pero el tipo de indicadores de resiliencia y capacidad que se necesitan —porcentaje de servicios críticos con protección adecuada, grado de cobertura de amenazas prioritarias, eficacia en detección y respuesta— encaja con la lógica de medición que D3FEND y sus herramientas CAD facilitan en el plano técnico.[^14][^9][^3][^13]

***

## 8. Cómo se podría usar D3FEND como “motor oculto” de indicadores país (España)

A nivel nacional, D3FEND ofrece un vocabulario común para traducir el estado real de las defensas técnicas de miles de organizaciones en indicadores agregables, comparables y trazables a amenazas concretas. La idea, ampliamente discutida en la literatura profesional ATT\&CK/D3FEND de 2025, es utilizar ambos marcos como “lenguaje común” entre threat intel, operaciones y estrategia.[^11][^10][^5][^9]

Aplicado a España, un esquema razonable sería: se definen catálogos de técnicas ATT\&CK relevantes para cada sector crítico, se exige (o recomienda fuertemente) que operadores clave modelen sus contramedidas con referencia a D3FEND y (cuando sea posible) en forma de grafos CAD, y se agregan métricas como porcentaje de técnicas cubiertas, lagunas críticas sin contramedida, latencias medianas de detección o tasa de éxito de mitigaciones a nivel sectorial o nacional. Todo ello se puede alinear con los objetivos de España Digital 2025 de reforzar capacidades y con la revisión en marcha de la Estrategia Nacional de Ciberseguridad, que busca adaptar el país a nuevas tendencias tecnológicas y geopolíticas.[^15][^9][^3][^13][^8][^14]

***

## 9. Comparativa internacional: tendencias 2025–2026 en uso de D3FEND

La literatura técnica reciente subraya que D3FEND se ha convertido en una pieza clave de la conversación internacional sobre marcos de defensa, especialmente en entornos financiados o impulsados por la NSA y el National Cybersecurity FFRDC de MITRE, que trabajan en soluciones realistas para infraestructuras críticas y mejora de capacidad de detección y recuperación. Organizaciones de defensa, proveedores de seguridad y centros de investigación están utilizando ATT\&CK y D3FEND como base común para describir TTPs de atacantes y contramedidas, y para derivar métricas operativas de cobertura, calidad de detecciones y priorización de inversiones.[^16][^10][^5][^2][^9]

Países con estrategias nacionales muy formalizadas tienden a integrar marcos como ATT\&CK en su threat modeling, y se observa un movimiento gradual hacia la utilización de D3FEND como lenguaje de referencia para controles y contramedidas, lo que facilita evaluaciones comparativas y ejercicios internacionales. España, ya bien posicionada en rankings globales y con una revisión activa de su Estrategia de Ciberseguridad para 2026, tiene margen para aprovechar D3FEND como infraestructura conceptual de medición sin necesidad de reinventar estándares domésticos, armonizando con los enfoques que se consolidan en Estados Unidos y otros socios europeos.[^10][^11][^16][^13][^14][^15]

***

## 10. Propuesta: familia de indicadores MITRE D3FEND para España (visión 2026)

A partir de lo que D3FEND define formalmente y de cómo lo operacionaliza CAD, la familia de métricas puede estructurarse en tres niveles que dialoguen con la política pública sin perder la precisión técnica.[^3][^8][^1]

En un primer nivel, táctico, se pueden definir indicadores de cobertura ATT\&CK–D3FEND (porcentaje de técnicas críticas cubiertas, lagunas sin contramedida, distribución de tácticas defensivas usadas), de latencia y eficacia (tiempo a detección, tiempo a contención, tasa de éxito de mitigaciones por familia de técnica) y de telemetría (proporción de artefactos relevantes con sensores adecuados, conforme sugiere D3FEND CAD).[^9][^8][^3]

En un segundo nivel, operacional y sectorial, esos indicadores se agregan por sector (energía, financiero, sanitario, etc.) y se conectan con requisitos regulatorios y planes de inversión, permitiendo expresar, por ejemplo, qué sectores presentan las mayores lagunas frente a ciertas técnicas o dónde la latencia media de detección supera lo razonable para la continuidad del servicio.[^13][^14][^9]

En un tercer nivel, estratégico y nacional, España podría integrar estos indicadores en su revisión de la Estrategia Nacional de Ciberseguridad y en la evolución de España Digital 2025, alineando objetivos como número de especialistas, refuerzo de infraestructuras y evolución del índice de resiliencia con datos cuantitativos derivados de grafos D3FEND y de la experiencia acumulada de sus CERTs y CSIRTs. No sería un cuadro de mando “bonito”, sino algo más interesante: un mapa de qué ataques sabemos detener, cuáles sólo intuimos, y cuáles dependen todavía de la suerte y del operador mal pagado de guardia a las tres de la mañana.[^14][^15][^13]


<span style="display:none">[^17][^18][^19][^20][^21][^22][^23]</span>

<div align="center">⁂</div>

[^1]: https://d3fend.mitre.org

[^2]: https://industrialcyber.co/regulation-standards-and-compliance/mitre-rolls-out-d3fend-1-0-to-bring-in-new-era-in-cybersecurity-standardization/

[^3]: https://d3fend.mitre.org/cad/docs/

[^4]: https://bsg.tech/blog/mitre-d3fend/

[^5]: https://www.vectra.ai/topics/mitre-d3fend

[^6]: https://d3fend.mitre.org/changelog/

[^7]: https://gbhackers.com/mitre-unveils-d3fend-cad-tool/

[^8]: http://devsecopsschool.com/blog/mitre-d3fend/

[^9]: https://www.deepwatch.com/glossary/mitre-d3fend-matrix/

[^10]: https://pgcs.org.au/paper/attck-d3fend-frameworks-in-2025-a-common-language-to-understand-threat-actors-drive-action-to-disrupt-the-kill-chain/

[^11]: https://blueridgenetworks.com/wp-content/uploads/2025/03/MITRE-MatricesAligments-3-19-2025.pdf

[^12]: https://www.cyberquizzer.com/blog/mitre-d3fend-framework-explained

[^13]: https://digital.gob.es/en/comunicacion/notas-prensa/mtdfp/2025/05/2025-05-06_02

[^14]: https://www.lamoncloa.gob.es/lang/en/presidente/news/paginas/2025/20251016-information-cecurity-meeting.aspx

[^15]: https://portal.mineco.gob.es/RecursosArticulo/mineco/ministerio/ficheros/210204_Digital_Spain_2025.pdf

[^16]: https://www.mitre.org/our-impact/rd-centers/national-cybersecurity-ffrdc

[^17]: https://www.exabeam.com/blog/infosec-trends/decoding-the-2025-mitre-attck-evals-a-call-for-clarity-and-a-guide-for-analysts/

[^18]: https://www.youtube.com/watch?v=SqtGd4KnZvE

[^19]: https://www.dsn.gob.es/sites/default/files/2025-07/Disinformation Campaigns 2024 Initiatives.pdf

[^20]: https://www.linkedin.com/pulse/mitre-attck-framework-evolution-strategic-2025-how-francis-cgqtc

[^21]: https://d3fend.mitre.org/resources/

[^22]: https://cymulate.com/cybersecurity-glossary/mitre-defend/

[^23]: https://www.linkedin.com/pulse/understanding-mitre-defend-knowledge-graph-brandy-owk9e

