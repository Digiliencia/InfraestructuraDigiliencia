
# Informe MITRE ATT\&CK.

MITRE ATT\&CK, desde 2025, se ha consolidado como el “idioma” operativo para medir la capacidad de detección y respuesta, y está empezando a utilizarse como base de indicadores a escala país en la UE, incluida España, aunque todavía de forma desigual y, en ocasiones, más aspiracional que real.[^1][^2][^3][^4]

## 1. MITRE ATT\&CK como base de indicadores

- MITRE ATT\&CK es una base de conocimiento global de tácticas, técnicas y subtécnicas adversarias, construida a partir de observaciones de ataques reales, que hoy supera centenares de TTP y se actualiza de forma continua.[^5][^6][^1]
- La matriz Enterprise (v13) organiza 14 tácticas y cerca de 200 técnicas con más de 400 subtécnicas, cubriendo entornos on‑prem, nube, contenedores e identidades.[^6][^1]
- ENISA adopta MITRE ATT\&CK como “grid” de referencia para mapear comportamientos de amenaza en sus Threat Landscapes, que sirven como brújula estratégica para los Estados miembros.[^2][^3]
- A nivel de producto, las Evaluaciones MITRE ATT\&CK Enterprise se han convertido en un benchmark de facto, centrado en métricas de cobertura de detección, calidad de alertas y protección preventiva.[^7][^8][^9]

Ejemplo ilustrativo: en la evaluación Enterprise 2025 algunos proveedores logran 100% de cobertura de técnicas y protección, con cero falsos positivos en los escenarios probados, lo que marca el listón de lo que se exige a un SOC “serio” en 2026.[^8][^10][^7]

### Tabla: niveles donde se usa ATT\&CK

| Nivel | Uso principal ATT\&CK |
| :-- | :-- |
| Producto / SOC | Medir cobertura de detección, calidad de alertas |
| Organización | Roadmap de detección, priorización de casos de uso SIEM/SOAR |
| Sector / UE (ENISA) | Tipificación de TTP, análisis de tendencias |
| País (España y UE) | Alineación con planes nacionales, evaluación de capacidades |

## 2. Métricas “clásicas” apoyadas en MITRE ATT\&CK

Desde 2025 se está convergiendo hacia un pequeño canon de métricas operativas donde ATT\&CK no aparece sólo como taxonomía bonita, sino como **eje de medición**.[^9][^11][^12]

### 2.1 Cobertura de detección ATT\&CK

- Porcentaje de técnicas/subtécnicas relevantes para el entorno que generan, al menos, un evento observable y una lógica de detección asociada.[^11][^9]
- En las Evaluaciones Enterprise 2025 se reporta cobertura de técnicas a nivel granular: 90/90 técnicas detectadas, 100% de técnica‑coverage, etc., y esto ha contaminado positivamente el lenguaje de los CISOs.[^10][^7][^8]
- En España, soluciones gestionadas tipo xMDR ya anuncian porcentajes explícitos de cobertura de tácticas (≈93%) y de técnicas (≈66%), lo que muestra una adopción explícita del marco como métrica comercial y técnica.[^13]


### 2.2 Calidad de detección y señal‑ruido

- MITRE ha enfatizado desde 2025 métricas sobre calidad de detección (precisión, nivel de detalle en la técnica/subtécnica) y volumen de alertas, en lugar de “más es mejor”.[^9]
- ENISA, al mapear incidentes a TTP ATT\&CK, impulsa a medir qué técnicas se detectan de forma temprana y cuáles sólo se descubren a posteriori, tras exfiltración o impacto.[^3][^2]
- Fabricantes punteros presumen de detección con 100% de técnicas, 0 falsos positivos y detección a nivel de técnica/subtécnica, reforzando la idea de que la métrica ya no es sólo “ver algo”, sino “ver lo que importa, a la resolución correcta”.[^7][^8]


### 2.3 Métricas de tiempo (MTTD, MTTC, MTTR)

- Prácticamente todos los marcos de métricas de 2025–2026 incorporan Mean Time to Detect (MTTD), Mean Time to Contain (MTTC) y Mean Time to Recover (MTTR); la aportación de ATT\&CK es permitir desglosar estos tiempos por táctica/técnica.[^14][^11]
- El análisis reciente de cobertura destaca que, ante el auge de intrusiones “malware‑free” (≈81% en 2024–2025), es crítico reducir MTTD en técnicas de credenciales, movimiento lateral y “living‑off‑the‑land”, más que en firmas de malware clásico.[^12]


## 3. Indicadores avanzados basados en ATT\&CK

Desde 2025 la comunidad académica e industrial ha pasado de “dibujar matrices” a usar ATT\&CK como base para indicadores compuestos y modelos de decisión.[^15][^2][^3]

### 3.1 Índices de riesgo técnico por táctica

- Trabajos recientes proponen caracterizar dinámicamente ataques según secuencias de técnicas ATT\&CK, optimizando la selección de mitigaciones según la ruta probable del adversario.[^15]
- ENISA usa el mapeo ATT\&CK para identificar qué tácticas concentran más actividad (p. ej., exfiltración y credenciales suman alrededor de un tercio de los casos analizados en su ETL 2025), señalando dónde deben concentrarse capacidades y métricas.[^2]
- Esto permite definir indicadores como “riesgo residual por táctica”: combinación de frecuencia observada en el ecosistema europeo y brecha de cobertura de detección/prevención en la infraestructura nacional.[^3][^2]


### 3.2 Cobertura nacional y sectorial ATT\&CK

- ENISA ha refinado su metodología para procesar conjuntos de datos de TTP según ATT\&CK, integrando CTI de proveedores, CERT nacionales y fuentes OSINT, con vistas a vistas sectoriales y, potencialmente, por Estado miembro.[^2][^3]
- Para España, los informes de ciberamenazas de la UE destacan que la administración pública es uno de los sectores más atacados, con especial protagonismo de ransomware, exfiltración y operaciones de espionaje; mapeado a ATT\&CK, esto se traduce en concentración en tácticas de impacto, exfiltración y acceso a credenciales.[^4][^2]
- La progresiva adopción de herramientas de análisis de cobertura alineadas con ATT\&CK facilita generar “mapas de calor” por país o sector, identificando las técnicas donde la detección es sistemáticamente pobre.[^11][^3]


### 3.3 Métricas de madurez: ATT\&CK + Zero Trust

- Algunos white papers orientados a seguridad nacional combinan ATT\&CK con marcos de inteligencia de amenazas para definir indicadores de madurez: porcentaje de flujos críticos cubiertos, capacidad de microsegmentación efectiva frente a tácticas de movimiento lateral, etc.[^16][^2]
- El enlace con Zero Trust es directo: medir cuántas de las técnicas de acceso inicial, credenciales y movimiento lateral pueden completar su “coreografía” antes de que los controles de identidad, red y endpoint activen una respuesta.[^16][^9]


## 4. España en el tablero ATT\&CK

### 4.1 Marco institucional

- España se posiciona como país con fuerte compromiso en ciberseguridad según informes internacionales, apoyado por un Plan Nacional de Ciberseguridad y nuevas inversiones superiores a 1 100 millones de euros para fortalecer capacidades de prevención, detección y respuesta.[^4]
- El ecosistema nacional articula varios centros clave: INCIBE, CCN‑CERT y el Mando Conjunto del Ciberespacio, que cooperan con la UE y ENISA en el intercambio de CTI y en la alineación con metodologías basadas en ATT\&CK.[^17][^3][^4]
- INCIBE aparece citado como actor nacional asociado al uso de ATT\&CK en iniciativas internacionales, lo que apunta a su utilización al menos como marco de referencia en programas de capacitación y servicios a empresas.[^17]


### 4.2 Uso de ATT\&CK en España (indicios)

- Casos recientes de ataques a infraestructuras españolas (p. ej., incidentes de ransomware o brechas en ministerios y puertos) se analizan y comunican con referencias explícitas a técnicas ATT\&CK, incluyendo phishing, ejecución de scripts y persistencia en sistemas críticos.[^18][^19]
- El sector privado español incorpora métricas basadas en ATT\&CK en servicios gestionados avanzados, declarando cobertura explícita en tácticas y técnicas como argumento de calidad y madurez.[^13]
- Empresas y alianzas GRC‑ciber en España alinean sus servicios con el Esquema Nacional de Seguridad, el GDPR y marcos como ATT\&CK para integrar cumplimiento, amenazas y capacidades técnicas en un mismo cuadro de mando.[^13][^4]


### 4.3 Oportunidad: indicadores “nacionales ATT\&CK”

Partiendo de las tendencias europeas y el tejido español, un conjunto razonable de indicadores a nivel país podría incluir:

- Porcentaje de técnicas ATT\&CK prioritarias (top N por frecuencia en la UE) con detección sistemática en infraestructuras críticas nacionales.
- Tiempo medio de detección de cadenas de ataque que involucren credenciales y movimiento lateral, en comparación con la media de la UE.[^12][^2]
- Cobertura ATT\&CK del ecosistema de servicios gestionados que dan soporte a pymes y administraciones locales (en porcentaje de tácticas técnicas relevantes).[^11][^13]
- Índice de alineación entre incidentes reportados a CERT nacionales y su mapeo ATT\&CK frente al panorama europeo (¿detectamos lo mismo, más tarde, antes?).[^3][^4][^2]


## 5. Tendencias globales desde 2025

### 5.1 Evaluaciones ATT\&CK como presión selectiva

- Las Evaluaciones Enterprise 2025 amplían el foco a dominios híbridos (endpoint, identidad, nube) e incorporan táctica de Reconocimiento, presionando para medir detección desde las fases más tempranas del ciclo de ataque.[^20][^7][^9]
- Varios fabricantes alcanzan 100% de detección y protección en los escenarios testados, lo que eleva la expectativa mínima y convierte cualquier cosa por debajo de cierto umbral de cobertura en una confesión de culpa.[^8][^10][^7]
- Aunque las evaluaciones no nombran “ganadores”, la transparencia de los datos por técnica permite a gobiernos y grandes organizaciones seleccionar tecnologías según su propio modelo de amenaza.[^8][^9]


### 5.2 Europa y ENISA: ATT\&CK como lingua franca

- ENISA sitúa ATT\&CK en el centro de su metodología de Threat Landscape, normalizando los TTP reportados por Estados miembros, proveedores y OSINT.[^2][^3]
- La sectorialización (p. ej., administración pública) permite extraer patrones de TTP que, traducidos a ATT\&CK, pueden convertirse en listas de “técnicas mínimas” que deberían estar cubiertas en cualquier SOC gubernamental europeo.[^21][^2]
- Esta convergencia prepara el terreno para métricas comparativas entre países, aunque todavía no se ha publicado un ranking explícito por cobertura ATT\&CK.[^22][^2]


### 5.3 Academia e industria: operacionalizar ATT\&CK

- Estudios recientes muestran que ATT\&CK es uno de los marcos más adecuados para procesar datos de amenazas a gran escala, especialmente aprovechando técnicas de IA para clasificar y correlacionar TTP.[^23][^15]
- La caracterización dinámica de ataques basada en ATT\&CK permite optimizar la selección de mitigaciones y priorizar inversiones en funciones de seguridad con mayor impacto marginal.[^12][^15]
- Herramientas industriales han aparecido específicamente para mapear, medir y reportar cobertura ATT\&CK, proporcionando reporting exportable para auditorías y decisiones de inversión.[^11]

***


<span style="display:none">[^24][^25][^26][^27][^28][^29][^30][^31][^32][^33][^34][^35][^36][^37][^38][^39][^40][^41][^42][^43]</span>

<div align="center">⁂</div>

[^1]: https://attack.mitre.org

[^2]: https://www.enisa.europa.eu/sites/default/files/2026-01/ENISA Threat Landscape 2025_v1.2.pdf

[^3]: https://www.enisa.europa.eu/sites/default/files/publications/ENISA CTL Methodology RECAST.pdf

[^4]: https://digital.gob.es/en/comunicacion/notas-prensa/mtdfp/2025/05/2025-05-06_02

[^5]: https://digitalperito.es/glosario/mitre-attack/

[^6]: https://www.tarlogic.com/es/blog/mitre-attck/

[^7]: https://www.crowdstrike.com/en-us/blog/crowdstrike-achieves-100-percent-2025-mitre-attack-enterprise-evaluation/

[^8]: https://www.cynet.com/mitre-attck-results/

[^9]: https://evals.mitre.org/enterprise/er7

[^10]: https://radar.offseq.com/threat/mitre-posts-results-of-2025-attck-enterprise-evalu-0eb3a600

[^11]: https://stellarcyber.ai/mitre-attck-coverage-analyzer/

[^12]: https://kcyerrid.com/2026/03/22/detection-coverage-measuring-what-you-can-actually-see/

[^13]: https://www.ecija.com/en/news-and-insights/cipher-y-ecija-acuerdan-prestar-servicios-conjuntos-en-materia-de-ciberseguridad-en-espana-portugal-y-latam/

[^14]: https://securityscorecard.com/resources/learning-center/9-cybersecurity-metrics-kpis-to-track/

[^15]: https://www.sciencedirect.com/science/article/pii/S0167739X25005667

[^16]: https://filigran.io/app/uploads/2025/11/filigran-white-paper-operationalizing-threat-intelligence-for-national-security-nov25.pdf

[^17]: https://cybilportal.org/publications/mitre-attck/

[^18]: https://techjacksolutions.com/scc-intel/ransomware-attack-disrupts-digital-operations-at-spains-port-of-vigo/

[^19]: https://www.picussecurity.com/resource/blog/t1059-006-python

[^20]: https://www.vectra.ai/topics/mitre-attack

[^21]: https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025

[^22]: https://securitydelta.nl/media/com_hsd/report/690/document/ENISA-Threat-Landscape-2024.pdf

[^23]: https://digital.csic.es/bitstream/10261/334427/1/Analysis_of_Cyber-Intelligence_Sanchez.pdf

[^24]: https://www.ibm.com/es-es/think/topics/mitre-attack

[^25]: https://www.fortinet.com/lat/resources/cyberglossary/mitre-attck

[^26]: https://www.paloaltonetworks.es/cyberpedia/what-is-mitre-attack

[^27]: https://www.ibm.com/mx-es/think/topics/mitre-attack

[^28]: https://www.campusciberseguridad.com/blog-alumno/tecnicas-tacticas-y-procedimientos-ttps-de-attck-de-mitre/

[^29]: https://es.scribd.com/document/914764798/MITRE-ATT-CK

[^30]: https://www.trendmicro.com/es_es/what-is/cyber-attack/mitre-attack-framework.html

[^31]: https://cibersafety.com/que-es-mitre-attck-ciberseguridad/

[^32]: https://oa.upm.es/83716/3/83716.pdf

[^33]: https://www.globalsuitesolutions.com/es/que-es-marco-mitre-att-ck/

[^34]: https://www.paloaltonetworks.es/cyberpedia/what-is-mitre-attack-framework

[^35]: https://download.manageengine.com/latam/log-management/el-mitre-attck-visto-bajo-microscopio.pdf

[^36]: https://attack.mitre.org/resources/attackcon/october-2025/

[^37]: https://www.ismsforum.es/noticias/lista-noticias.php?idsubcategoria=471

[^38]: https://www.reddit.com/r/pwnhub/comments/1pk2qwk/mitre_releases_2025_attck_evaluations_companies/

[^39]: https://www.shadecoder.com/topics/mitre-att-ck-a-comprehensive-guide-for-2025

[^40]: https://attack.mitre.org/groups/

[^41]: https://attack.mitre.org/techniques/T1036/005/

[^42]: https://www.linkedin.com/posts/allsafeus-sec_spains-ministry-of-science-breach-a-critical-activity-7425296199580028928-Kso_

[^43]: https://s-bay.co.uk/blog/files/7548e97524dad041a9bf06db43ad035e-29.html

