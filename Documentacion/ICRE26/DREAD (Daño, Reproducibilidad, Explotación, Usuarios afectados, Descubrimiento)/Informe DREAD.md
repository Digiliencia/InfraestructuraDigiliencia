# Informe DREAD: Indicadores y Métricas Cuantitativas 2025–2026
## Aplicación Nacional Territorial en España con Perspectiva Comparativa Mundial

> *"Todo modelo es erróneo; algunos modelos son útiles." — George Box*
> *Y DREAD, con todas sus cicatrices y su abolengo Microsoft, sigue siendo, cuando se le acompaña de buen juicio y herramientas modernas, notablemente útil.*

***

## Resumen Ejecutivo

El marco DREAD —acrónimo de **D**amage (Daño), **R**eproducibility (Reproducibilidad), **E**xploitability (Explotabilidad), **A**ffected Users (Usuarios Afectados) y **D**iscoverability (Descubribilidad)— fue concebido a comienzos de los 2000 en los laboratorios de Microsoft como un sistema de puntuación para cuantificar y priorizar amenazas en el ciclo de vida del desarrollo de software. Aunque Microsoft lo retiró formalmente alrededor de 2008, alegando inconsistencia intersubjetiva, el marco ha gozado de una segunda vida en entornos industriales, de ciberseguridad gubernamental y, más recientemente, como substrato cuantitativo enriquecido con técnicas de aprendizaje automático, lógica difusa y análisis multicriterio.[^1][^2][^3][^4]

El panorama de 2025–2026 sitúa a España ante un año históricamente adverso: **122.223 incidentes de ciberseguridad gestionados por INCIBE en 2025**, un 26% más que en 2024, con 237.028 sistemas vulnerables notificados y pérdidas estimadas que superan los 500 millones de euros. La ENISA, por su parte, analizó 4.875 incidentes entre julio de 2024 y junio de 2025, señalando que el ransomware sigue siendo la amenaza de mayor impacto en la Unión Europea. En este contexto, las métricas cuantitativas del modelo DREAD adquieren valor estratégico no solo como instrumento técnico de priorización, sino como lenguaje común entre equipos de seguridad, directivos, reguladores y organismos de defensa nacional.[^5][^6][^7][^8][^9]

El presente informe ofrece una investigación exhaustiva sobre los cinco indicadores DREAD —sus fundamentos matemáticos, sus extensiones cuantitativas más recientes (2025–2026), sus aplicaciones en infraestructuras críticas y su proyección al ámbito nacional español—, situándolos en perspectiva comparativa con marcos de referencia internacionales (CVSS v4.0, EPSS, FAIR) y alineándolos con el ecosistema normativo vigente: ENS, NIS2, DORA y el recién gestado Centro Nacional de Ciberseguridad (CNCS).[^10][^11]

***

## 1. Genealogía y Arquitectura del Marco DREAD

### 1.1 Origen y Discontinuación

El modelo DREAD fue introducido en el libro *Writing Secure Code* (Meier et al., 2003), publicado por Microsoft Press, como complemento al análisis de amenazas STRIDE. Nació con una premisa seductora: asignar un valor numérico a cada dimensión de riesgo —de 0 a 10— y obtener una puntuación media que permitiera ordenar amenazas de forma defendible ante equipos de desarrollo y gestión. Su sencillez aritmética fue, paradójicamente, tanto su mayor virtud como su talón de Aquiles.[^1]

Microsoft discontinuó formalmente su uso interno aproximadamente en 2008, arguyendo que los equipos alcanzaban puntuaciones radicalmente distintas sobre un mismo vector de amenaza, dependiendo del perfil del evaluador y del contexto organizativo. La dimensión de **Descubribilidad** recibió además críticas filosóficas de primer orden: premiar la dificultad de descubrimiento de una vulnerabilidad equivale a incentivar la **"seguridad por oscuridad"**, principio explícitamente rechazado por la comunidad de seguridad desde los postulados de Kerckhoffs y, más modernamente, por todos los organismos de estandarización relevantes (NIST, ENISA, ISO/IEC).[^2][^12][^13]

A pesar de todo, DREAD sobrevivió al olvido institucional de Microsoft por razones pragmáticas: su costo de implementación es mínimo, no requiere herramientas específicas y produce resultados comprensibles para audiencias no técnicas. En 2025 persiste como herramienta de **priorización ejecutiva** semanal, base para evaluaciones rápidas en entornos industriales (OT/ICS/SCADA), y como estructura que frameworks académicos han elevado con álgebra difusa, redes neuronales y comparación pareada de criterios.[^14][^3][^15]

### 1.2 Fórmula de Puntuación Base

La puntuación DREAD se calcula como la media aritmética de cinco dimensiones, cada una evaluada en una escala discreta de 1 a 10:[^16]

\[
\text{DREAD}_{\text{score}} = \frac{D + R + E + A + D_{\text{isc}}}{5}
\]

El resultado numérico se clasifica en cuatro niveles de severidad:[^17][^18][^1]

| Nivel | Rango (suma 5 dimensiones) | Rango (media) | Interpretación operativa |
|-------|---------------------------|---------------|--------------------------|
| **Crítico** | 40–50 | 8.0–10.0 | Intervención inmediata; potencial impacto en continuidad de operaciones |
| **Alto** | 25–39 | 5.0–7.9 | Revisión urgente; resolución antes del siguiente ciclo |
| **Medio** | 11–24 | 2.2–4.9 | Programar tras mitigar críticos y altos |
| **Bajo** | 1–10 | 0.2–2.0 | Riesgo menor; monitorización periódica |

La variante **DREAD-D** — *DREAD minus D* — omite la dimensión de Descubribilidad y promedia solo cuatro categorías, eliminando el incentivo implícito a mantener vulnerabilidades ocultas. Esta variante ha ganado terreno en entornos de alta madurez de seguridad donde la transparencia interna es una exigencia cultural.[^13][^2]

***

## 2. Los Cinco Indicadores: Métricas Cuantitativas 2025–2026

Cada indicador se examina a continuación con sus criterios de puntuación, las propuestas más recientes de cuantificación objetiva y su relevancia específica para el contexto territorial español.

### 2.1 Indicador D — Daño Potencial (*Damage Potential*)

#### Definición operativa

El Daño Potencial mide el **alcance máximo del impacto** que puede provocar la explotación exitosa de una vulnerabilidad o amenaza. Incluye pérdida de datos, interrupción de servicios, daño reputacional, consecuencias regulatorias y pérdidas económicas directas.[^19]

#### Escala cuantitativa (2025)

| Puntuación | Nivel | Criterios de evaluación | Ejemplo empírico |
|------------|-------|-------------------------|------------------|
| 8–10 | Crítico | Compromiso total del sistema; ejecución de comandos privilegiados; violación regulatoria grave (GDPR, NIS2); paralización de servicios esenciales | Ransomware en hospital; ataque a red eléctrica; filtración masiva de datos ciudadanos |
| 5–7 | Alto | Pérdida significativa de datos sensibles; alteración grave de funcionalidades críticas; impacto en alta disponibilidad | Exfiltración de credenciales corporativas; modificación de datos financieros |
| 2–4 | Medio | Exposición de datos no críticos; degradación parcial del servicio; impacto reversible | Fuga de metadatos; interrupción temporal de un microservicio no crítico |
| 0–1 | Bajo | Impacto mínimo o nulo; sin datos sensibles involucrados | Divulgación de información pública |

En el contexto de infraestructuras críticas nacionales —donde el modelo DREAD se aplica a entornos OT/SCADA— la puntuación de Daño debe incorporar indicadores de impacto físico: vidas en riesgo, impacto en el PIB por interrupción de servicios, o cascada regulatoria. Estudios de 2025 aplicados a refinerías de petróleo (Shieldworkz, 2026) y a entornos de ciudades inteligentes (Frontiers in Computer Science, 2025) han ampliado la escala de Daño con sub-indicadores sectoriales.[^20][^21][^22]

En España, los sectores con mayor puntuación de Daño potencial corresponden a **banca (34% de los incidentes en operadores esenciales), transporte (14%) y energía (8%)** según los datos de INCIBE 2025. Un ataque de ransomware contra infraestructura bancaria obtendría puntuación máxima en esta dimensión dados el carácter sistémico del sector y el marco DORA, que exige continuidad operacional en el sector financiero.[^23][^24][^5]

#### Extensiones cuantitativas avanzadas

La literatura académica de 2025 propone enriquecer el indicador de Daño con métricas derivadas de marcos complementarios:[^25][^26]

- **CVSS v4.0 — Impacto de Confidencialidad/Integridad/Disponibilidad** (C/I/A): valores None/Low/High que pueden traducirse a escala 0–10 para alimentar la dimensión DREAD[^27]
- **FAIR — Loss Magnitude**: cuantificación financiera del daño esperado en términos de frecuencia y magnitud monetaria[^28]
- **Indicadores KRI del INCIBE-IMC**: basados en MITRE y metodología GQM (Goal-Question-Metric), los indicadores de ciberresiliencia de INCIBE incluyen métricas de disponibilidad, integridad y confidencialidad directamente mapeables a esta dimensión[^29]

***

### 2.2 Indicador R — Reproducibilidad (*Reproducibility*)

#### Definición operativa

La Reproducibilidad evalúa **con qué fiabilidad y frecuencia puede repetirse un ataque** bajo condiciones similares. Un exploit que funciona el 100% de las veces representa el escenario de mayor riesgo; uno que depende de condiciones de carrera específicas o de ventanas temporales estrechas, un riesgo menor.[^30][^16]

#### Escala cuantitativa (2025)

| Puntuación | Nivel | Criterios | Anchoring empírico |
|------------|-------|-----------|-------------------|
| 10 | Muy fácil | Reproducible en cada intento; no requiere condiciones especiales | Exploits públicos con PoC funcional; vulnerabilidades sin parche en sistemas masivamente desplegados |
| 7.5 | Fácil | Reproducible con esfuerzo moderado; requiere condiciones básicas | Explotación de configuraciones por defecto; ataques de fuerza bruta con listas estándar |
| 5 | Complejo | Requiere múltiples pasos o conocimiento del entorno objetivo | Ataques multi-etapa; exploits que requieren acceso previo |
| 0–2.5 | Muy difícil | Condiciones de carrera, timing específico, o entornos rarísimos | Zero-days con ventana de explotación < 24h; vulnerabilidades hardware complejas |

La Microsoft Security Development Lifecycle (SDL) recomendó en su momento fijar esta dimensión siempre en 10, bajo el principio de que **toda vulnerabilidad será eventualmente explotada**. Si bien esta es la postura más conservadora, distorsiona la priorización relativa entre amenazas. El enfoque más refinado, adoptado en estudios recientes de aplicación nacional, consiste en correlacionar esta dimensión con la **puntuación EPSS (Exploit Prediction Scoring System)** del FIRST:[^12][^31][^32]

\[
R_{\text{DREAD}} \approx 10 \times P_{\text{EPSS}}(\text{CVE}, t \leq 30\text{ días})
\]

Esta correlación, propuesta formalmente en la literatura de gestión de vulnerabilidades de 2025, permite transicionar DREAD hacia una metodología más basada en evidencia empírica. Para amenazas sin CVE asociado —como las amenazas de actores estatales con herramientas personalizadas (Russia, China, Corea del Norte, Irán)— la evaluación de Reproducibilidad se basa en análisis de TTPs del MITRE ATT&CK, alimentados por los informes de CCN-CERT y los ISAC sectoriales.[^33][^34][^13]

#### Relevancia para España

Los 237.028 sistemas vulnerables detectados por INCIBE-CERT en 2025 constituyen el indicador empírico más directo de la reproducibilidad sistémica de amenazas en el territorio español. La existencia de exploits públicos para vulnerabilidades conocidas en sistemas críticos, sin parche aplicado, equivale a una puntuación de reproducibilidad cercana a 10. El CCN-CERT documenta en su Informe IA-04/24 cómo los actores maliciosos compran accesos en mercados negros y reutilizan herramientas conocidas como técnica de primera etapa, lo que convierte muchos vectores en altamente reproducibles.[^35][^5][^33]

***

### 2.3 Indicador E — Explotabilidad (*Exploitability*)

#### Definición operativa

La Explotabilidad cuantifica **el nivel de habilidad, recursos y acceso** que un atacante necesita para materializar la amenaza. A diferencia de la Reproducibilidad —que mide la fiabilidad del ataque una vez iniciado— la Explotabilidad evalúa la **barrera de entrada** para comenzarlo.[^36][^16]

#### Escala cuantitativa (2025)

| Puntuación | Perfil de atacante | Recursos requeridos | Ejemplo 2025 |
|------------|-------------------|---------------------|--------------|
| 7–10 | Script kiddie; usuario no técnico | Herramientas públicas; guías en foros | Phishing con plantillas comerciales; ataques de credential stuffing con listas HIBP |
| 4–6 | Profesional con formación básica | Frameworks semicomerciales (Metasploit, Cobalt Strike) | Explotación de CVE con PoC; ataques de lateral movement con herramientas estándar |
| 0–3 | Actor sofisticado; posiblemente Estado-nación | Herramientas custom; zero-days; conocimiento profundo del objetivo | APT con implantes persistentes; ataques OT/SCADA especializados; supply chain attacks |

En el ecosistema de ataques con IA generativa de 2025 se ha producido un fenómeno significativo: la reducción sistemática de la barrera de entrada para ataques que históricamente requerían alta sofisticación. CrowdStrike reportó en su Global Threat Report 2025 un **incremento del 75% en el uso de automatización basada en IA para el desarrollo de malware**. Esto presiona a la baja las puntuaciones de Explotabilidad en toda la taxonomía de amenazas conocidas.[^37]

Aplicado al ámbito de LLMs en 2025, la investigación de la University of Waikato (Zahid et al., 2025) demuestra que ataques como *Token Smuggling* y *Direct Prompt Injection* obtienen Explotabilidad = 10 porque son ejecutables por cualquier usuario sin conocimiento técnico del modelo subyacente. Esta inflación de la Explotabilidad en entornos de IA generativa tiene consecuencias directas para organizaciones del sector público y educativo español, crecientes usuarios de estas tecnologías.[^38]

#### Correlación con CVSS v4.0

La componente **Attack Complexity (AC)** de CVSS v4.0 es el correlato más directo de la Explotabilidad DREAD. La equivalencia aproximada es:[^27]

| CVSS AC | Puntuación DREAD-E equivalente |
|---------|-------------------------------|
| Low | 7–10 |
| High | 1–6 |

Esta equivalencia permite a organizaciones que ya utilizan CVSS alimentar automáticamente la dimensión E de DREAD, reduciendo la carga evaluadora y mejorando la consistencia inter-analista.

***

### 2.4 Indicador A — Usuarios Afectados (*Affected Users*)

#### Definición operativa

Los Usuarios Afectados cuantifican **el alcance poblacional** de una amenaza materializada. A diferencia de otras dimensiones que evalúan características del ataque en sí, este indicador mide la **superficie social del impacto**, lo que lo convierte en el más relevante para la aplicación a escala territorial nacional.[^30][^19]

#### Escala cuantitativa estándar (2025)

La escala de referencia más frecuentemente citada en la literatura técnica 2025 opera en décimas de la base de usuarios:[^39][^16]

| Puntuación | % Usuarios afectados | Nivel | Contexto territorial |
|------------|---------------------|-------|---------------------|
| 1 | 0–10% | Mínimo | Subsistema interno no crítico |
| 3 | 21–30% | Bajo | Servicio regional o departamental |
| 5 | 41–50% | Medio | Plataforma de uso extendido |
| 7 | 61–70% | Alto | Infraestructura sectorial (ej.: red bancaria regional) |
| 10 | 91–100% | Crítico | Infraestructura nacional esencial (DNI digital, Red eléctrica, DNS nacional) |

#### Extensión a escala nacional territorial

Cuando DREAD se aplica en el nivel de análisis de ciberseguridad nacional —como proponen varios marcos de evaluación de resiliencia adoptados por CCN-CERT y documentos del Consejo de Seguridad Nacional— la dimensión A debe reescalarse sobre la **población total** del territorio y los **sectores estratégicos**:[^40][^35]

| Puntuación ajustada | Alcance territorial | Ejemplo operativo España |
|---------------------|---------------------|--------------------------|
| 10 | >10M ciudadanos o >3 sectores críticos en paralelo | Apagón eléctrico nacional; ataque al sistema CLAVE de identidad digital |
| 7–9 | 1M–10M ciudadanos o 1–2 sectores críticos (bancario, sanitario) | Indisponibilidad del sistema SEPE; breach masivo en Hacienda |
| 4–6 | 100K–1M afectados o impacto sectorial significativo | Ataque a red de distribución de agua metropolitana |
| 1–3 | <100K o impacto organizacional local | Incidente en un municipio pequeño; fuga de datos de una PYME |

Este enfoque de reescalado es coherente con la propuesta del *National Cyber Security Index* (NCSI) para España y con la estructura del Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad aprobado en enero de 2025, que categoriza entidades **esenciales e importantes** según NIS2.[^41][^42][^11][^10]

En 2025, el 85% de los sistemas infectados en botnet identificados por INCIBE-CERT corresponden a **dispositivos IoT domésticos**, lo que implica que un ataque de gran escala sobre la superficie IoT española puede alcanzar puntuaciones A de 7–9 casi automáticamente, dado el nivel de penetración tecnológica en hogares y PYMEs.[^5]

#### Tipos de usuarios y su ponderación diferencial

Las investigaciones más recientes (Thakur et al., JCOMSS 2026; Zahid et al., 2025) proponen distinguir subtipos de usuarios para refinar la puntuación:[^3][^38]

- **Administradores/superusuarios**: afectación = multiplicador ×1.5 sobre puntuación base
- **Usuarios regulares masivos**: base de cálculo principal
- **Operadores de infraestructura crítica**: afectación = multiplicador ×2 si hay riesgo de vida
- **Datos de menores o colectivos vulnerables**: multiplicador regulatorio ×1.5 (GDPR, artículo 9)

***

### 2.5 Indicador D — Descubribilidad (*Discoverability*)

#### Definición operativa

La Descubribilidad estima **la probabilidad de que un atacante descubra la vulnerabilidad** o el vector de ataque por medios propios, sin asistencia externa. Es la dimensión más controvertida del modelo, la más directamente ligada al debate filosófico entre seguridad proactiva y seguridad por oscuridad.[^2][^12]

#### Escala cuantitativa (2025)

| Puntuación | Nivel de exposición | Ejemplo operativo |
|------------|---------------------|-------------------|
| 10 | Información pública; buscable en Google; PoC en GitHub | CVE con exploit público; configuraciones inseguras documentadas en guides técnicas |
| 7.5 | Requiere conocimiento del entorno o escaneo activo | Vulnerabilidades detectables con Shodan/Censys sin autenticación |
| 5 | Requiere heurísticas o conocimiento técnico especializado | Vulnerabilidades lógicas que exigen ingeniería inversa parcial |
| 0–2.5 | Muy difícil de descubrir sin insider knowledge | Bugs zero-day no publicados; fallos en criptografía personalizada |

#### La controversia de la Descubribilidad y el enfoque DREAD-D

Tres posiciones prevalecen en la práctica profesional de 2025:[^43][^12][^13]

1. **Posición conservadora (Microsoft SDL)**: fijar D = 10 siempre. Todo será descubierto eventualmente. Ventaja: elimina el sesgo hacia la oscuridad. Desventaja: no discrimina entre amenazas.

2. **Posición eliminacionista (DREAD-D)**: retirar la dimensión por completo y calcular DREAD sobre 4 indicadores. Esta variante —formalmente reconocida en Wikipedia y adoptada por SimpleRisk— otorga un 25% menos de peso total a la dimensión más subjetiva.[^28][^2]

3. **Posición correlacionada**: vincular Descubribilidad a métricas de inteligencia de amenazas activas —menciones en dark web, actividad en foros de exploits, publicaciones en CVE/NVD— usando la **metodología de vigilancia digital** del CCN-CERT o soluciones comerciales CTIS (Cyber Threat Intelligence Services). Esta es la posición académicamente más robusta para aplicaciones nacionales.[^35]

En el contexto del **CCN-CERT y la Estrategia de Ciberdefensa Activa** española, la Descubribilidad debería medirse en tiempo real mediante indicadores de telemetría sobre lo que los atacantes están *buscando activamente* en el espacio de amenazas español, no simplemente sobre lo que *podría encontrarse* en abstracto. Esta vinculación convierte la dimensión en un indicador dinámico, revisable en ciclos semanales, coherente con la filosofía de *Zero Trust Architecture* y con la propuesta de servicios horizontales de ciberseguridad del Plan Nacional.[^44][^35]

***

## 3. Extensiones Cuantitativas Avanzadas del Modelo DREAD (2025–2026)

### 3.1 DREAD Ponderado (Weighted DREAD)

La crítica más fundada al DREAD clásico es que trata todas las dimensiones como **igualmente relevantes**, cuando en contextos específicos —como infraestructuras críticas— el Daño debería pesar más que la Descubribilidad. La solución propuesta desde la investigación académica es la **ponderación diferencial** mediante Análisis Jerárquico de Procesos (AHP):[^45][^15]

\[
\text{DREAD}_{\text{ponderado}} = w_D \cdot D + w_R \cdot R + w_E \cdot E + w_A \cdot A + w_{D_{\text{isc}}} \cdot D_{\text{isc}}
\]

donde \( \sum w_i = 1 \) y los pesos se calculan por comparación pareada de expertos según el contexto organizativo o sectorial.

Un ejemplo de ponderación propuesta para **infraestructuras críticas nacionales** podría ser:

| Dimensión | Peso propuesto (CI nacional) | Justificación |
|-----------|------------------------------|---------------|
| Daño (D) | 0.35 | Impacto físico y social prioritario |
| Usuarios Afectados (A) | 0.30 | Escala poblacional: decisiva para gobernanza |
| Explotabilidad (E) | 0.20 | Barrera de entrada reducida por IA |
| Reproducibilidad (R) | 0.10 | Proxy de madurez del exploit |
| Descubribilidad (D) | 0.05 | Mínimo peso; vinculada a vigilancia activa |

Esta distribución reflejaría la prioridad estratégica española: proteger a la mayor cantidad de ciudadanos del mayor daño posible, asumiendo que los atacantes sofisticados (actores estatales) tienen capacidad ilimitada de descubrimiento.

### 3.2 Fuzzy DREAD

La lógica difusa (*Fuzzy Logic*) resuelve el problema de la subjetividad categórica en la asignación de scores discretos (1, 5, 10) permitiendo **números difusos triangulares (TFN)**. En lugar de afirmar que la explotabilidad es "7", el evaluador expresa que es "aproximadamente entre 6 y 8, con valor modal 7", representado como el triplete (6, 7, 8).[^15][^46]

Estudios de 2024–2025 en el *Journal of Information Systems Engineering and Management* (Shabbir et al., 2025) demuestran que la integración AHP-TOPSIS con DREAD mejora significativamente la consistencia interobservador en procesos de evaluación de riesgos de software. Esta metodología ha sido adoptada en tesis doctorales recientes (NAIST, Japón, 2025) para la evaluación de contenedores y entornos cloud.[^46][^15]

### 3.3 DREAD Híbrido con Machine Learning

El avance más significativo en la literatura técnica de 2025–2026 es la **integración de DREAD con clasificadores de aprendizaje automático** para automatizar el scoring y reducir la dependencia del juicio humano. El artículo de Thakur et al. publicado en el *Journal of Communications Software and Systems* (Vol. 22, No. 1, marzo 2026) presenta un marco híbrido STRIDE-DREAD con Random Forest que alcanza una precisión del **99.91%** sobre el dataset CIC-BCCC-NRC TabularIoTAttack-2024.[^3]

Los scores DREAD empíricos obtenidos para amenazas IoT en este estudio son:

| Categoría STRIDE | DREAD Score (heurístico) | Clasificación |
|-----------------|--------------------------|---------------|
| Tampering | 8.7 | **Alto-Crítico** |
| Spoofing | 8.2 | **Alto** |
| Denial of Service | 7.8 | **Alto** |
| Information Disclosure | 6.5 | **Medio-Alto** |
| Elevation of Privilege | 6.0 | **Medio-Alto** |
| Repudiation | 5.4 | **Medio** |

La detección en tiempo real —menos de 50ms por evaluación en hardware estándar— convierte este enfoque en viable para **SOCs (Security Operations Centers)** nacionales como el INCIBE-CERT, donde la escala de incidentes (237.028 sistemas vulnerables notificados en 2025) hace inviable la evaluación manual.[^5]

### 3.4 DREAD Aplicado a Amenazas sobre LLMs (2025)

La investigación de Zahid et al. (University of Waikato, 2025) aplica DREAD con escala cuantitativa de cinco puntos (0, 2.5, 5, 7.5, 10) a una taxonomía de 50 ataques sobre LLMs, obteniendo la siguiente distribución de riesgo:[^38]

- **4 ataques críticos** (score ≥ 8.5): Token Smuggling, Direct Prompt Injection, Adversarial Prompt Injection, Multi-step Jailbreak
- **32 ataques de riesgo alto** (score 7.0–8.4)
- **14 ataques de riesgo medio** (score 5.5–6.9)
- **0 ataques de riesgo bajo**: toda la superficie de ataque a LLMs se sitúa en nivel medio o superior

Scores detallados de los ataques críticos sobre eLLMs:

| Ataque | D | R | E | A | Disc. | **Score** |
|--------|---|---|---|---|-------|-----------|
| Direct Injection | 5.0 | 10 | 10 | 10 | 10 | **9.0** |
| Adversarial Prompt | 7.5 | 10 | 10 | 7.5 | 10 | **9.0** |
| Token Smuggling | 7.5 | 10 | 10 | 7.5 | 10 | **9.0** |
| Multi-step Jailbreak | 10 | 10 | 7.5 | 10 | 7.5 | **9.0** |

Esta evidencia tiene consecuencias directas para España: la adopción masiva de herramientas de IA generativa en la Administración Pública, el sector educativo y el sector financiero expande la superficie de ataque con vectores de explotabilidad máxima.

***

## 4. Panorama Nacional: DREAD Aplicado al Territorio Español (2025–2026)

### 4.1 Contexto Estadístico de Amenazas

El ecosistema de amenazas español en 2025 puede evaluarse cualitativamente mediante los indicadores DREAD a partir de los datos oficiales disponibles:

| Tipo de Amenaza | D | R | E | A | Disc. | **Score estimado** |
|-----------------|---|---|---|---|-------|--------------------|
| **Ransomware en infraestructura crítica** | 10 | 7 | 6 | 9 | 7 | **7.8** |
| **Malware masivo (botnet IoT)** | 6 | 10 | 9 | 9 | 10 | **8.8** |
| **Phishing a ciudadanos** | 5 | 10 | 10 | 9 | 10 | **8.8** |
| **Ciberespionaje estatal (APT)** | 10 | 4 | 3 | 7 | 3 | **5.4** |
| **Ataque a banca online (DORA)** | 9 | 7 | 6 | 9 | 6 | **7.4** |
| **Vulnerabilidades IoT doméstico** | 5 | 10 | 10 | 10 | 10 | **9.0** |

*Puntuaciones estimadas sobre la base de datos INCIBE 2025, CCN-CERT IA-04/24 y ENISA ETL 2025. Escala 0–10 por dimensión; media aritmética.*

Las amenazas de **mayor score DREAD territorial** son las que combinan alta explotabilidad (vectores ampliamente conocidos, herramientas públicas disponibles), alta reproducibilidad (incidentes que se repiten sistemáticamente) y alcance masivo de usuarios. No coinciden necesariamente con las más sofisticadas: el ciberespionaje estatal, técnicamente el más avanzado, obtiene scores DREAD menores porque su baja Explotabilidad y Descubribilidad reducen el promedio.

### 4.2 Distribución de Incidentes INCIBE 2025 bajo la Lente DREAD

| Indicador INCIBE 2025 | Cifra | Dimensión DREAD relevante | Interpretación |
|-----------------------|-------|--------------------------|----------------|
| Incidentes totales | 122.223 (+26%) | A — Usuarios Afectados | Escalada sostenida del alcance poblacional |
| Malware (incl. ransomware) | 55.411 casos | D — Daño + R — Reproducibilidad | Tipo más reproducible y dañino |
| Sistemas vulnerables notificados | 237.028 | R + E — Reproducibilidad + Explotabilidad | Superficie de ataque activa extremadamente alta |
| Botnets IoT (85% de infectados) | ~201.924 disp. | A + E | Máxima explotabilidad, máximo alcance |
| Incidentes en operadores esenciales | 401 | D + A | Sectores de impacto nacional |
| Sector bancario (34% op. esenciales) | ~136 incidentes | D — Daño sistémico DORA | Máxima consecuencia por incidente |

Fuente: INCIBE, Balance de Ciberseguridad 2025[^9][^5]

### 4.3 Marco Normativo y Ecosistema Institucional

El ecosistema institucional español articula la gestión del riesgo cibernético en tres vectores principales, cada uno con afinidad específica a las dimensiones DREAD:[^42][^40][^29]

**CCN-CERT** (Centro Criptológico Nacional):
- Ámbito: Sector público, defensa, infraestructuras críticas
- Relevancia DREAD: Análisis de Daño máximo (D) y Explotabilidad por actores estatales (E)
- Documenta TTPs de Rusia, China, Corea del Norte e Irán como actores de mayor score en D y A[^33]

**INCIBE-CERT** (Instituto Nacional de Ciberseguridad):
- Ámbito: Ciudadanos, empresas, operadores esenciales privados
- Relevancia DREAD: Usuarios Afectados (A), Reproducibilidad (R) en amenazas masivas
- Metodología IMC basada en GQM con KPIs y KRIs mapeables a dimensiones DREAD[^29]

**CNPIC** (Centro Nacional de Protección de Infraestructuras Críticas):
- Ámbito: Protección de sectores estratégicos (energía, agua, transporte, finanzas)
- Relevancia DREAD: Daño en cascada (D), Usuarios Afectados a escala nacional (A)

El **Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad** (enero 2025), que transpone NIS2 y crea el **Centro Nacional de Ciberseguridad (CNCS)**, establece una arquitectura de gobernanza que centraliza la supervisión sin eliminar las especializaciones institucionales existentes. Para la aplicación de DREAD a nivel nacional, este marco ofrece la estructura orgánica necesaria: el CNCS coordinaría la metodología de scoring inter-institucional, el CCN-CERT aportaría inteligencia de amenazas para alimentar Reproducibilidad y Descubribilidad, e INCIBE-CERT contribuiría con los datos de alcance real (Usuarios Afectados) desde su telemetría de incidentes.[^11][^41][^10]

### 4.4 Posición Comparativa de España en el Contexto Europeo

El *National Cyber Security Index* (NCSI, versión septiembre 2025) asigna a España puntuaciones robustas en liderazgo gubernamental (12/15, 80%), análisis de amenazas (5/5, 100%) y desarrollo de políticas. Sin embargo, la realidad operativa —España como 5º país europeo más afectado por ransomware, con un 25% de incremento en ataques en el primer semestre de 2025— muestra que la capacidad institucional no basta cuando la superficie de ataque crece más rápido que las defensas.[^47][^8][^42]

La comparativa DREAD con otros países avanzados revela patrones de riesgo diferenciados:

| País / Marco | Énfasis principal en DREAD | Mecanismo de medición | Fuente |
|--------------|---------------------------|----------------------|--------|
| **España (INCIBE/CCN)** | Usuarios Afectados (A), Daño (D) sectorial | KPIs/KRIs bajo GQM | [^29][^42] |
| **UE (ENISA ETL 2025)** | Daño (D), Reproducibilidad (R) de TTPs | EU Relevance Scoring + Admiralty | [^48][^6] |
| **Países Bajos (NCTV 2025)** | Resiliencia nacional + Daño cascada (D+A) | CER Resilience Model | [^49][^50] |
| **Canadá (CSE NCTA 2025-26)** | Actores estatales: E + R sofisticados | Intelligence Assessment Tiers | [^51][^52] |
| **EE.UU. (CISA 2025)** | Infraestructuras críticas: D + A nacional | KEV + CVSS + EPSS combinados | [^53][^13] |

***

## 5. DREAD en Perspectiva Comparativa: Posicionamiento frente a CVSS, EPSS y FAIR

La selección del marco de puntuación de riesgo apropiado no es una decisión técnica neutral: refleja prioridades organizativas, audiencias objetivo y horizontes temporales de decisión. A continuación se presenta una comparación estructurada que sitúa DREAD en el ecosistema contemporáneo de métricas:[^54][^14][^28]

| Dimensión de análisis | DREAD | CVSS v4.0 | EPSS | FAIR |
|----------------------|-------|-----------|------|------|
| **Propósito** | Priorización de amenazas con impacto en negocio | Severidad técnica de vulnerabilidades | Predicción de explotación a 30 días | Cuantificación financiera del riesgo |
| **Unidad de output** | Score 0–10 (promedio 5 dimensiones) | Score 0–10 (fórmula compuesta) | Probabilidad 0–1 | Rango monetario de pérdida esperada |
| **Objetividad** | Media (contextual, subjetiva) | Alta (estandarizada FIRST) | Muy alta (ML empírico) | Alta (modelo actuarial) |
| **Audiencia** | Business stakeholders + equipos seguridad | Técnicos, auditores, compliance | SOC, gestores de vulnerabilidades | CISO, CFO, Consejo de Administración |
| **Mejor uso** | Priorización semanal; informe ejecutivo; OT/ICS | Compliance; CVE tracking; reporte a reguladores | Patching prioritization; threat hunting | Justificación de inversiones; presupuesto |
| **Alineación regulatoria** | Flexible (NIS2, ENS, DORA) | CVSS requerido en algunos marcos (PCI-DSS) | Recomendado CISA/NIST para patching | DORA, NIS2 (articulación financiera) |
| **Temporalidad** | Estático (revisión periódica) | Estático (actualizable con métricas temporales) | Dinámico (diario) | Estático con escenarios |
| **Escalabilidad nacional** | Alta (con reescalado A) | Media (orientado a activos individuales) | Alta (API FIRST, gratuita) | Media (requiere datos financieros internos) |

La combinación **CVSS + DREAD** es la más recomendada en la literatura 2025 para evaluaciones de penetración y auditorías de seguridad. Para el nivel estratégico nacional, la combinación **DREAD ponderado + FAIR** permite traducir puntuaciones técnicas en lenguaje financiero para el informe al Consejo de Ministros o a los órganos de dirección empresarial requeridos por NIS2.[^23][^54][^14][^11]

El EPSS, publicado diariamente por el FIRST para todos los CVE activos, puede alimentar directamente la dimensión **R (Reproducibilidad)** y **E (Explotabilidad)** del modelo DREAD, creando un marco semi-automatizado que actualiza scores de riesgo en tiempo real sin necesidad de evaluación manual completa.[^32]

***

## 6. Aplicaciones Sectoriales Emergentes 2025–2026

### 6.1 DREAD en Entornos OT/ICS/SCADA

La industria de ciberseguridad industrial ha encontrado en DREAD una herramienta adaptable a entornos OT, donde la especificidad técnica de CVSS no siempre captura el impacto físico de las amenazas. Shieldworkz (marzo 2026) documenta la aplicación de STRIDE+DREAD a un entorno DCS (Distributed Control System) de refinería petroquímica, obteniendo una visión comprehensiva de riesgos desde estaciones de ingeniería, HMIs, PLCs y redes de proceso hasta infraestructura de acceso remoto.[^21]

Dragos (Annual OT Threat Landscape 2025) reporta que el 25% de los advisories ICS tienen scores CVSS incorrectos, y propone su propio modelo "Now, Next, Never" como alternativa. Solo el 2% de vulnerabilidades ICS requieren acción inmediata según este modelo, lo que correlaciona con las categorías "Critical" de DREAD aplicado con contexto operativo.[^55]

En España, el CCN-CERT documentó en su informe IA-04/16 las amenazas específicas a Sistemas de Control Industrial, con metodología propia de clasificación de amenazas y criterios de análisis de riesgos adaptados a ICS. La integración de esta metodología con DREAD ponderado representaría un avance significativo en la homogeneización del lenguaje de riesgo entre el mundo IT y OT.[^56]

### 6.2 DREAD para IA Generativa e IA en Infraestructura Crítica

La expansión de IA en infraestructuras críticas (redes eléctricas, sistemas de salud, transporte) introduce nuevos vectores de ataque con características DREAD específicas: alta Explotabilidad (interfaces en lenguaje natural), alta Reproducibilidad (herramientas públicas disponibles) y potencial Daño severo (sistemas de control integrado).[^57]

Los cuatro ataques críticos identificados por Zahid et al. (2025) —Token Smuggling, Direct Injection, Adversarial Prompt, Multi-step Jailbreak, todos con score DREAD = 9.0— sitúan los sistemas basados en LLMs en la categoría de **prioridad máxima** cuando se aplican a servicios esenciales. Para España, esto afecta directamente a los servicios digitales de la Administración Pública que incorporan chatbots y asistentes de IA, al sector educativo (eLLMs en universidades) y a la banca digital.[^38]

### 6.3 DREAD en el Contexto de Supply Chain

El CCN-CERT advierte en su informe de 2024 sobre metodologías híbridas que combinan phishing, vulnerabilidades en software desactualizado y malware personalizado como primera etapa de ataques de cadena de suministro. DREAD aplicado a Supply Chain Risk Management (SCRM) implica evaluar cada proveedor tecnológico como un vector de amenaza potencial, con las dimensiones A y D ampliadas al ecosistema cliente.[^58]

NIS2 y DORA establecen específicamente la obligación de evaluar y gestionar el riesgo de terceros, lo que crea una demanda directa de metodologías de scoring como DREAD aplicadas a proveedores, integradores y servicios cloud.[^59][^11]

***

## 7. Limitaciones del Modelo y Agenda de Investigación 2026–2027

### 7.1 Limitaciones Estructurales Reconocidas

Cualquier profesional que utilice DREAD debe operar con plena consciencia de sus limitaciones estructurales:[^12][^43][^13][^2]

- **Subjetividad inter-analista**: la misma amenaza puede recibir scores radicalmente diferentes según el perfil del evaluador, su tolerancia al riesgo y su conocimiento del contexto. Las técnicas de ponderación AHP y lógica difusa mitigan, pero no eliminan, este problema.

- **Escala lineal y cardinal**: DREAD asume que la diferencia entre score 7 y score 8 es equivalente a la diferencia entre 1 y 2. En realidad, algunos ataques son *exponencialmente* peores que otros; la escala lineal no captura esta no-linealidad.[^12]

- **Sin captura de correlaciones**: las cinco dimensiones se tratan como independientes, cuando en la práctica están correlacionadas. Un ataque altamente explotable tiende a ser también altamente reproducible; sumar ambas puntaciones independientemente puede sobreponderar el riesgo.[^60]

- **Ausencia de temporalidad**: DREAD es estático. Un score evaluado en enero puede quedar obsoleto en marzo si se publica un exploit. La integración con EPSS (actualización diaria) o con feeds STIX/TAXII del CCN-CERT es esencial para aplicaciones operativas.[^48][^32]

- **Dificultad de auditoría**: los scores son difíciles de auditar externamente, lo que complica su uso en contextos de compliance regulatorio donde la trazabilidad metodológica es exigible (NIS2, ENS, DORA).[^11][^23]

### 7.2 Líneas de Investigación Prioritarias

La agenda de investigación identificada por la comunidad científica para 2026–2027 incluye:[^61][^62][^3]

1. **DREAD-ML v2**: incorporación de modelos de atención (*attention-based neural networks*) para capturar relaciones no lineales entre dimensiones DREAD y TTPs del MITRE ATT&CK
2. **DREAD continual learning**: actualización incremental de scores sin reentrenamiento completo, para adaptarse a la evolución de amenazas en tiempo real
3. **DREAD territorial normativo**: propuesta de metodología para aplicar DREAD a la evaluación de cumplimiento NIS2 y ENS, integrando los KPIs del INCIBE-IMC con las cinco dimensiones
4. **DREAD cross-sector**: marco unificado de evaluación que permita comparar scores entre sectores distintos (energía vs. salud vs. finanzas) con ponderaciones contextualmente ajustadas
5. **DREAD + FAIR nacional**: modelo integrado que traduzca puntuaciones DREAD a pérdidas financieras esperadas en términos de impacto en el PIB español, coherente con los requisitos de reporte del CNCS

***

## 8. Síntesis: DREAD como Lenguaje Estratégico Nacional

El valor diferencial de DREAD en 2025–2026 no reside en su precisión matemática —que es modesta— sino en su función como **lenguaje común de priorización entre audiencias heterogéneas**: técnicos de seguridad, gestores de riesgo, reguladores y responsables políticos. Esta función comunicativa es especialmente relevante en el momento de transformación institucional que vive España, con el CNCS en formación, la NIS2 en proceso de transposición y la inversión de 1.157 millones de euros en capacidades de ciberseguridad anunciada en mayo de 2025.[^44]

La síntesis de evidencias indica que el uso óptimo de DREAD en el contexto nacional español en 2026 pasa por cuatro decisiones metodológicas:

1. **Adoptar la variante DREAD-D** (sin Descubribilidad) o fijar D=10 sistemáticamente para evaluar amenazas en infraestructuras críticas, eliminando el sesgo hacia la oscuridad[^13][^2]

2. **Aplicar ponderación AHP diferencial** con pesos adaptados al sector: mayor peso en Daño y Usuarios Afectados para infraestructuras esenciales; mayor peso en Explotabilidad para aplicaciones web y servicios ciudadanos expuestos[^45][^15]

3. **Integrar EPSS como proxy dinámico** de las dimensiones R y E, usando la API diaria del FIRST para actualizar scores de vulnerabilidades conocidas (CVEs)[^34][^32]

4. **Escalar la dimensión A al territorio nacional**, redefiniéndola en términos de porcentaje de población afectada o número de sectores críticos impactados simultáneamente, en línea con los umbrales de notificación de incidentes significativos definidos por NIS2 y el futuro CNCS[^41][^10]

Adoptado con estas extensiones, DREAD deja de ser un artefacto metodológico de los años 2000 para convertirse en un instrumento de gobernanza del ciberriesgo nacional: sencillo en su núcleo, extensible en sus capas y —sobre todo— comprensible para el decisor que, sin necesariamente dominar el álgebra de vulnerabilidades, debe asignar recursos escasos en el tablero de la seguridad nacional.

***

## Referencias y Fuentes Clave

Las fuentes citadas en este informe incluyen:
- Informe INCIBE: Balance de Ciberseguridad 2025 (INCIBE, febrero 2026)[^9][^5]
- ENISA Threat Landscape 2025 (ENISA, octubre 2025)[^6][^7]
- ENISA CTL Methodology, agosto 2025[^48]
- Thakur et al., "A Novel Hybrid Threat Modeling Framework for IoT Security using STRIDE-DREAD and Machine Learning", JCOMSS Vol. 22 No. 1, 2026[^3]
- Zahid et al., "Securing Educational LLMs: A Generalised Taxonomy of Attacks on LLMs and DREAD Risk Assessment", University of Waikato, 2025[^38]
- CCN-CERT, Ciberamenazas y Tendencias IA-04/24, 2024[^33]
- Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad, enero 2025[^10][^41]
- Shabbir et al., "Evaluating the Impact of Security Risks through Fuzzy AHP-TOPSIS Method", JISEM 2025[^15]
- Dragos 9th Annual OT Threat Landscape 2025 (publicado 2026)[^55]
- CISA Year in Review 2025[^53]
- Del-Real et al., "Who Will Govern Cybersecurity in Spain by 2035?", Wiley Risk Analysis, 2025[^63]
- National Cyber Security Index (NCSI) España, septiembre 2025[^42]
- INCIBE, Metodología de evaluación de indicadores IMC (GQM), 2023[^29]
- Shieldworkz, "STRIDE-Based Threat Modeling & DREAD Risk Evaluation for Oil Refinery DCS Environments", 2026[^21]

---

## References

1. [DREAD Threat Modeling: An Introduction to Qualitative Risk Analysis](https://www.eccouncil.org/cybersecurity-exchange/threat-intelligence/dread-threat-modeling-intro/) - The DREAD model quantitatively assesses the severity of a cyberthreat using a scaled rating system t...

2. [DREAD (risk assessment model) - Wikipedia](https://en.wikipedia.org/wiki/DREAD_(risk_assessment_model)) - When a given threat is assessed using DREAD, each category is given a rating from 1 to 10, and the s...

3. [[PDF] A Novel Hybrid Threat Modeling Framework for IoT Security using ...](https://jcoms.fesb.unist.hr/pdfs/v22n1_2025-0236_Thakur.pdf) - A new threat modeling framework integrates structured threat assessment methods STRIDE and DREAD tog...

4. [STRIDE vs. DREAD vs. PASTA: Choosing the Right Threat Modeling ...](https://apiiro.com/blog/stride-vs-dread-vs-pasta-choosing-the-right-threat-modeling-framework/) - DREAD. DREAD is a risk scoring framework designed to add quantitative prioritization to threat model...

5. [INCIBE detectó más de 122.000 incidentes de ciberseguridad en 2025](https://www.incibe.es/incibe/sala-de-prensa/incibe-detecto-mas-de-122000-incidentes-de-ciberseguridad-en-2025) - Entre los incidentes más recurrentes en 2025 destacaron: Malware, con 55.411 casos, incluyendo virus...

6. [ENISA Threat Landscape 2025 - European Union](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025) - This publication outlines the updated ENISA Cybersecurity Threat Landscape (CTL) methodology, buildi...

7. [ENISA Threat Landscape 2025 Overview | PDF - Scribd](https://www.scribd.com/document/974731303/ENISA-Threat-Landscape-2025-Booklet) - The ENISA Threat Landscape 2025 report highlights that state-aligned operations and hacktivism are s...

8. [Spain Fifth in Europe for Cyberattacks in 2025 - LinkedIn](https://www.linkedin.com/posts/luis-oria-seidel-%F0%9F%87%BB%F0%9F%87%AA-301a758a_cybersecurity-cyberattacks-digitalsecurity-activity-7384884426373136384-s5Rt) - Spain, Fifth Most Affected European Country by Cyberattacks in the First Semester of 2025 🛡️ In a co...

9. [Balance INCIBE 2025: 122.223 ciberincidentes en España (+26%)](https://digitalperito.es/blog/incibe-balance-2025-122000-ciberincidentes-espana/) - INCIBE gestionó 122.223 ciberincidentes en 2025 (+26%). 55.411 malware, 25.133 phishing, 392 ransomw...

10. [NIS2 Spain Transposition: Status, Requirements, and Roadmap](https://copla.com/blog/compliance-regulations/nis2-directive-regulations-and-implementation-in-spain/) - Cybersecurity risk management; Non-compliance penalties; Third-party risk oversight; Incident report...

11. [The NIS2 Directive will transform cybersecurity in Spain - PKF Attest](https://www.pkf-attest.es/en/noticias/la-directiva-que-cambiara-la-ciberseguridad-empresarial-en-espana/) - The NIS2 Directive is the new European regulation that seeks to strengthen cybersecurity in all Memb...

12. [A somewhat DREADful vulnerability scoring method - Deploy Securely](https://blog.stackaware.com/p/a-somewhat-dreadful-vulnerability) - A critique of (and homage to) one of the original cybersecurity rubrics.

13. [Risk, Severity, Threat Modeling, and Why You Need A Pentest](https://innovatecybersecurity.com/news/risk-severity-threat-modeling-and-why-you-need-a-pentest/) - DREAD. Structure: Mnemonic for Damage, Reproducibility, Exploitability, Affected Users, Discoverabil...

14. [Scoring Framework Comparison - VulnTrack - Mintlify](https://www.mintlify.com/ogdmerlin/vulntrack/scoring/comparison) - Compare CVSS, DREAD, and STRIDE frameworks to understand when to use each for vulnerability assessme...

15. [Journal of Information Systems Engineering and Management](https://jisem-journal.com/index.php/journal/article/download/3972/1773/6523)

16. [Threat Modeling Methods: STRIDE, PASTA & DREAD](https://destcert.com/resources/threat-modeling-methodologies/) - To use the DREAD model, you should analyze each threat according to each of the five metrics and giv...

17. [DREAD: A Classic Framework for Navigating Cyber Threat Seas](https://www.oreateai.com/blog/dread-a-classic-framework-for-navigating-cyber-threat-seas/cc5b64955c5cfc11f380e36613778226) - The DREAD threat modeling framework, despite its age and subjectivity concerns, remains a valuable t...

18. [[PDF] Findings and Recommendations](https://cdn-cybersecurity.att.com/docs/DREAD_scoring_template.pdf)

19. [DREAD Model: Basics of Risk Assessment - Cycore Secure](https://www.cycoresecure.com/blogs/dread-model-basics-of-risk-assessment) - Learn how the DREAD model simplifies risk assessment in cybersecurity by evaluating threats based on...

20. [A framework for cyber threat modeling and risk assessment in smart ...](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1647179/full) - The Common Vulnerability Scoring System, which assigns a risk score on a range of 0 to 10 in ascendi...

21. [STRIDE-Based Threat Modeling & DREAD Risk Evaluation for Oil ...](https://shieldworkz.com/regulatory-playbooks/stride-based-threat-modeling-and-dread-evaluation-for-oil-refinery-distributed-control-systems) - Download the STRIDE and DREAD threat modeling Whitepaper for refinery DCS environments to identify c...

22. [Why OT, IoT, and SCADA Systems Need Threat Modeling](https://blog.secureflag.com/2025/01/17/ot-iot-scada-threat-modeling/) - Threat modeling is one of the best ways to stay ahead of cyber threats so you can protect your syste...

23. [Looking Ahead to 2025: Cybersecurity Trends and the FAIR ...](https://www.fairinstitute.org/blog/looking-ahead-to-2025-cybersecurity-trends-and-the-fair-institutes-plans) - Now that we've stepped into 2025, let's take a look at what's in store for cyber risk quantification...

24. [INCIBE gestionó 122.223 incidentes de ciberseguridad en 2025, un ...](http://espanadigital.gob.es/en/actualidad/incibe-gestiono-122223-incidentes-de-ciberseguridad-en-2025-un-26-mas-que-el-ano) - En 2025 los incidentes más recurrentes fueron: Malware: 55.411 casos, incluidos 392 ataques de ranso...

25. [A quantitative methodology for systemic impact assessment of cyber ...](https://www.sciencedirect.com/science/article/pii/S0167404825004183) - To address these limitations, this study proposes a simulation-based framework that complements TARA...

26. [Developing security metrics for space systems: A study considering ...](https://www.sciencedirect.com/science/article/pii/S1874548225000666) - We quantify how the various NIST Cybersecurity Framework (CSF) 2.0 functions, categories, and subcat...

27. [From Risk to Resilience: Harnessing the Potential of CVSS v4.0](https://safe.security/resources/insights/from-risk-to-resilience-harnessing-the-potential-of-cvss-v4-0/) - Microsoft's DREAD model, designed specifically for software vulnerabilities, offers a simple and str...

28. [There is Nothing Simple About FAIR - SimpleRisk](https://www.simplerisk.com/blog/there-nothing-simple-about-fair) - We support DREAD, which is the old school Microsoft risk rating methodology. We support the OWASP Ri...

29. [IMC_01 – Methodology for Assessing Cyberresilience ...](https://www.incibe.es/sites/default/files/contenidos/guias/IMC/imc_01_evaluation-methodology_2023.pdf)

30. [What Is the DREAD Threat Model? | Everpure (formerly Pure Storage)](https://www.purestorage.com/knowledge/dread-threat-model.html) - The DREAD threat model is a risk assessment framework that helps organizations quantify, compare, an...

31. [EPSS vs. CVSS: What's The Best Approach To Vulnerability ...](https://www.intruder.io/blog/epss-vs-cvss) - EPSS is a model that provides a daily estimate of the probability that a vulnerability will be explo...

32. [Exploit Prediction Scoring System (EPSS) Special Interest Group (SIG)](https://www.first.org/epss/) - Help defenders incorporate EPSS into their vulnerability management and quantitative risk models thr...

33. [El CCN-CERT advierte de las principales ciberamenazas](https://www.tecnonews.info/noticias/el_ccn_cert_advierte_de_las_principales_ciberamenazas) - El Informe de Ciberamenazas y Tendencias 2024 analiza las principales amenazas registradas durante 2...

34. [Vulnerability Management in 2025: Prioritization with CVSS & EPSS](https://www.linkedin.com/pulse/vulnerability-management-2025-prioritization-cvss-epss-andrew-crotty-yvgic) - CVSS assigns vulnerabilities a score from 0 to 10 based on severity. It considers exploitability (at...

35. [CCN-CERT. Ciberamenazas 2024](https://www.pap.hacienda.gob.es/sitios/150aniversario/Documents/PresentacionCCNMesaredondaciberseguridadAP.pdf)

36. [Threat Modeling with STRIDE and DREAD: A Complete Guide to ...](https://inventivehq.com/blog/threat-modeling-stride-dread-complete-guide) - We cover the foundational frameworks (STRIDE and DREAD), the construction of data flow diagrams, met...

37. [AI and Cybersecurity in 2025: How AI Model Advances Reshape ...](https://www.hu.ac.ae/it-hub/artificial-intelligence/ai-and-cybersecurity-in-2025-how-ai-model-advances-reshape-digital-risk) - Explore how rapid AI model advances are reshaping digital risk and cybersecurity in 2025, including ...

38. [A Generalised Taxonomy of Attacks on LLMs and DREAD Risk ...](https://arxiv.org/html/2508.08629v1) - Mapping the proposed LLMs -based attack taxonomy to the education sector and quantification of the a...

39. [DREAD Risk Assessment - AegisShield - Mintlify](https://www.mintlify.com/mgrofsky/AegisShield/features/risk-assessment) - Quantitative risk assessment using the DREAD methodology for threat prioritization

40. [Principios y](https://www.ospi.es/export/sites/ospi/documents/documentos/Seguridad-y-privacidad/CCN-CERT_BP_01_Principios_y_recomendaciones_basicas_de_seguridad_202103.pdf)

41. [The European NIS2 Directive strengthens cybersecurity in Spain ...](https://www.dominios.es/en/informacion-de-interes/noticias/european-nis2-directive-strengthens-cybersecurity-spain-leading) - The implementation of NIS2 in Spain will strengthen the security of critical strategic services, pos...

42. [NCSI :: Spain - National Cyber Security Index](https://ncsi.ega.ee/country/es/)

43. [Understanding DREAD: A Legacy Threat Modeling Framework](https://www.linkedin.com/posts/habibar_threatmodeling-dread-microsoftsecurity-activity-7363277440661483520-FmyK) - 🥷 Hi Ninjas, I’m covering another security threat modeling framework today—this time a legacy one th...

44. [The Government approves a strengthening of Spain's cybersecurity ...](https://digital.gob.es/en/comunicacion/notas-prensa/mtdfp/2025/05/2025-05-06_02) - The Council of Ministers today approved a set of actions in cybersecurity and cyberdefence that comp...

45. [Determination of Weighting Assessment on DREAD Model using Profile Matching](https://thesai.org/Publications/ViewPaper?Volume=9&Issue=10&Code=ijacsa&SerialNo=9) - Web application creators often get lack understanding of security threats that can occur in applicat...

46. [[PDF] Doctoral Dissertation Towards a Risk-Secured Container ...](https://naist.repo.nii.ac.jp/record/2001210/files/R019739.pdf) - Third, it introduces FuzzyFortify, a multi- attribute risk assessment framework that integrates fuzz...

47. [EspañaSec 2025: Securing Critical Infrastructure in an Era of IT-OT ...](https://ismg.io/espanasec-2025-strengthening-spains-cybersecurity-through-public-private-cooperation/) - The summit brings together Spain's cybersecurity leaders to address evolving challenges affecting th...

48. [[PDF] ENISA CYBERSECURITY THREAT LANDSCAPE METHODOLOGY](https://www.enisa.europa.eu/sites/default/files/2025-08/ENISA%20CTL%20Methodology_Updated%20August%202025.pdf) - To assess relevance of a specific event to the EU threat landscape, ENISA analysts rely on a simple ...

49. [The Critical National Infrastructure Threat Landscape (2025)](https://english.nctv.nl/documents/2025/11/14/the-critical-national-infrastructure-threat-landscape) - This first ever threat landscape report provides an overview of the main threats to critical infrast...

50. [[PDF] The Critical National Infrastructure Threat Landscape](https://english.nctv.nl/site/binaries/site-content/collections/documents/2025/11/14/the-critical-national-infrastructure-threat-landscape/84346-NCTV-Dreigingsbeeld+Vitale+Infrastructuur-ENG_TG-UA+def.pdf) - This first ever threat landscape report provides an overview of the main threats to critical infrast...

51. [[PDF] National cyber threat assessment 2025–2026](https://newsletter.radensa.ru/wp-content/uploads/2024/11/national-cyber-threat-assessment-2025-2026-e.pdf) - Canada is confronting an expanding and complex cyber threat landscape with a growing cast of malicio...

52. [National Cyber Threat Assessment 2025-2026 - Canadian Centre ...](https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026) - The National Cyber Threat Assessment 2025-2026 highlights the cyber threats facing individuals and o...

53. [CISA 2025 Year in Review focuses on driving security and ...](https://industrialcyber.co/cisa/cisa-2025-year-in-review-focuses-on-driving-security-and-resilience-across-critical-infrastructure/) - The agency reported blocking 2.62 billion malicious connections across federal civilian networks and...

54. [Understanding Risk Rating Frameworks in Pen Testing: DREAD vs ...](https://mainnerve.com/pen-testing-risk-rating-frameworks/) - The choice between DREAD and CVSS depends on factors such as the organization's technical expertise,...

55. [Dragos 2025 Threat Landscape flags control loop mapping and ...](https://industrialcyber.co/industrial-cyber-attacks/dragos-2025-threat-landscape-flags-control-loop-mapping-and-escalation-of-ot-intent/) - Industrial cybersecurity firm Dragos reports the rise of specialized threat groups whose varied tact...

56. [CCN-CERT_IA-04-16](https://es.scribd.com/document/859587534/CCN-CERT-IA-04-16) - El informe CCN-CERT IA-04/16 aborda las amenazas y riesgos en Sistemas de Control Industrial (ICS), ...

57. [AI Security Risks in 2025: 6 Threats & 6 Defensive Measures - Oligo](https://www.oligo.security/academy/ai-security-risks-in-2025-6-threats-6-defensive-measures) - AI is increasingly applied in managing critical infrastructure like power grids, healthcare systems,...

58. [El CCN-Cert publica su informe de Ciberamenazas y ...](https://www.lksnext.com/es/noticias_boletin/el-ccn-cert-publica-su-informe-de-ciberamenazas-y-tendencias-de-2024/) - Datos de recaudación Acuerdo internacional sobre fiscalidad digital Hacienda ultima el reglamento de...

59. [NIS2 Directive Spain: Cybersecurity Requirements 2025 | Flexxible](https://www.flexxible.com/en/blog/nis2-directive-spain) - It is the new European legislation that establishes common measures to strengthen cybersecurity in c...

60. [www.ijprems.com](https://www.ijprems.com/uploadedfiles/paper/issue_5_may_2025/41272/final/fin_ijprems1747981649.pdf)

61. [Posted on 28 Oct 2024 — CC-BY 4.0 — https://doi.org/10.36227/techrxiv.173014171.11449253/v1 — e-Prints posted on TechRxiv are preliminary reports that are not peer reviewed. They should not b...](https://d197for5662m48.cloudfront.net/documents/publicationstatus/229586/preprint_pdf/1de13ed459287bea5da5358b59d15c38.pdf)

62. [Threat Modeling for the Defense Industry: Past, Present, and Future](https://ieeexplore.ieee.org/iel8/6287639/10820123/10921707.pdf) - Most threat modeling studies present it as a procedure for identify- ing threats and developing miti...

63. [[PDF] Who Will Govern Cybersecurity in Spain by 2035? Results From a ...](https://rodin.uca.es/bitstream/handle/10498/36907/OA_2025_0186.pdf?sequence=1&isAllowed=y) - ABSTRACT. This study explores the future of cybersecurity governance in Spain by 2035, focusing on t...

