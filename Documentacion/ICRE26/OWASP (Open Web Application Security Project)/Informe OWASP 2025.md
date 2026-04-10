# Indicadores OWASP 2025 cuantitativos aplicables a España y su alineamiento con NIS2

## 1. Introducción y alcance

Este informe se centra en los indicadores cuantitativos que se pueden derivar de los marcos OWASP más relevantes en 2025 (Top 10:2025, SAMM, ASVS 5.0 y la Metodología de Rating de Riesgo), y en cómo pueden aplicarse a España a nivel nacional, en coherencia con el ENS y la Directiva NIS2. Se pone el énfasis en la definición precisa de métricas medibles (qué contar, cómo y con qué unidad), más que en fijar umbrales numéricos normativos, ya que ni OWASP ni NIS2 establecen valores concretos, sino obligaciones de gestión de riesgos y buenas prácticas.[^1][^2][^3][^4][^5][^6][^7][^8][^9][^10][^11]

España ofrece un contexto fértil para operacionalizar estas métricas: un marco ENS basado en riesgos, la transposición en curso de NIS2 y una arquitectura institucional que incluye CCN, INCIBE y un futuro Centro Nacional de Ciberseguridad, junto con datos recientes que muestran 122.223 incidentes de ciberseguridad gestionados por INCIBE en 2025 (+26% interanual) y 237.028 sistemas vulnerables relevantes detectados.[^12][^13][^14][^4][^7][^8]

## 2. Familias de métricas OWASP relevantes en 2025

### 2.1. OWASP Top 10:2025 – métricas de exposición y prevalencia

El OWASP Top 10:2025 es un documento de concienciación que agrupa vulnerabilidades y debilidades en diez categorías de riesgo, encabezadas por A01:2025 – Broken Access Control, A02:2025 – Security Misconfiguration y A03:2025 – Software Supply Chain Failures. Para construir la lista, OWASP utiliza un dataset de alrededor de 175.000 CVEs mapeados a CWEs y calcula un "risk score" por CWE que combina tasa máxima de incidencia, cobertura de pruebas, explotabilidad e impacto (derivados de CVSS v2/v3) y número de ocurrencias.[^15][^16][^17][^18][^19][^11][^1]

Aunque OWASP no publica indicadores por país, la propia metodología (incidencia, cobertura, explotabilidad, impacto) sugiere tipos de métricas cuantitativas que se pueden replicar a nivel nacional: proporción de sistemas afectados por categorías del Top 10, grado de cobertura de escaneos y distribución de scores de explotabilidad e impacto en los sistemas españoles.[^17][^18][^1]

### 2.2. OWASP SAMM – métricas de madurez de programa

OWASP SAMM (Software Assurance Maturity Model) estructura la seguridad del software en cinco funciones de negocio y quince prácticas, cada una evaluada en niveles de madurez de 0 a 3, donde 0 implica ausencia de actividad y 3 una maestría integrada en la organización. La práctica "Strategy and Metrics" de la función de Gobernanza se centra precisamente en definir objetivos de seguridad de software y en medir la postura y las mejoras del programa, incluyendo el alineamiento con indicadores organizativos y el valor de los activos.[^2][^20]

La comunidad SAMM propone agrupar las métricas en tres categorías: de esfuerzo (p. ej., número de formaciones, horas invertidas), de resultado (p. ej., defectos de seguridad por funcionalidad) y de entorno (p. ej., factores de contexto de negocio), y enfatiza que toda métrica debe ser medible de forma consistente, asequible de recolectar y útil para la toma de decisiones. El SAMM Benchmark Report, lanzado en 2025, se apoya en datos de evaluaciones reales para construir estadísticas comparativas de madurez, con primeras medias en torno a 1,44 sobre 3 en la muestra disponible.[^21][^22][^23]

### 2.3. OWASP ASVS 5.0 – métricas de verificación técnica

El OWASP Application Security Verification Standard (ASVS) proporciona un catálogo de requisitos técnicos de seguridad que sirven, entre otros fines, "como métrica" para que desarrolladores y propietarios de aplicaciones puedan evaluar el grado de confianza que cabe depositar en ellas. La versión 5.0, publicada en mayo de 2025, agrupa unos 350 requisitos en 17 capítulos y define tres niveles de verificación (1, 2 y 3) que permiten clasificar el grado de aseguramiento alcanzado por una aplicación.[^5][^24]

Esta estructura habilita métricas cuantitativas claras: porcentaje de aplicaciones que alcanzan un determinado nivel ASVS, proporción de requisitos cumplidos por capítulo (autenticación, control de acceso, gestión de sesiones, criptografía, logging, cadena de suministro), y cobertura de pruebas frente a esos requisitos mediante automatización y pruebas manuales.[^25][^24][^5]

### 2.4. OWASP Risk Rating Methodology – métricas de probabilidad e impacto

La Metodología de Rating de Riesgo de OWASP descompone el riesgo en probabilidad (Likelihood) e impacto, ambos cuantificados con factores en escala 0–9. La probabilidad resulta del promedio de factores del agente de amenaza (nivel de habilidad, motivación, oportunidad, tamaño) y de factores de vulnerabilidad (facilidad de descubrimiento, facilidad de explotación, nivel de conocimiento, capacidad de detección de intrusiones).[^26][^27][^6]

El impacto se calcula a partir de factores técnicos (pérdida de confidencialidad, integridad, disponibilidad, trazabilidad) o, cuando se dispone de información, de impacto de negocio (daño financiero, reputacional, legal) y el riesgo final suele expresarse como Risk = Likelihood * Impact, normalmente normalizado en una escala de 1 a 10 o en niveles bajo/medio/alto. Esta estructura permite construir indicadores agregados de riesgo medio por cartera de sistemas, sector o país.[^27][^6][^28][^26]

## 3. Catálogo de métricas cuantitativas OWASP aplicables a España

### 3.1. Métricas de exposición por categorías Top 10:2025

**M1 – Densidad de vulnerabilidades OWASP Top 10:2025 en sistemas españoles**  
- **Definición:** número de vulnerabilidades conocidas (CVE) explotables en sistemas bajo jurisdicción española, mapeadas a CWEs y agrupadas por categorías del Top 10:2025, dividido por el número total de activos inventariados en cada categoría de ENS (bajo, medio, alto).[^4][^6][^18][^1]
- **Unidad:** vulnerabilidades por 100 activos.  
- **Datos necesarios:** inventario de activos (ENS), bases de datos de vulnerabilidades de INCIBE-CERT y CCN-CERT, mapeo CWE–Top 10:2025.[^29][^30][^12][^4]

**M2 – Proporción de activos críticos sin vulnerabilidades abiertas en A01–A03**  
- **Definición:** porcentaje de sistemas clasificados como "servicios esenciales" o "importantes" bajo NIS2/ENS que no tienen vulnerabilidades abiertas de severidad alta o crítica asociadas a A01 (Broken Access Control), A02 (Security Misconfiguration) o A03 (Software Supply Chain Failures).[^16][^3][^7][^18][^10][^15][^1]
- **Unidad:** porcentaje de activos.  
- **Uso:** indicador sintético de exposición a categorías que reflejan fallos estructurales de control de acceso, configuración y cadena de suministro.

**M3 – Cobertura de análisis frente a Top 10:2025**  
- **Definición:** porcentaje de aplicaciones y APIs críticas que, al menos una vez al año, se someten a pruebas (SAST, DAST, SCA, pentesting) con reglas o configuraciones explícitamente mapeadas a las diez categorías del Top 10:2025.[^31][^32][^33][^25]
- **Unidad:** porcentaje de aplicaciones.  
- **Uso:** aproxima la "cobertura de detección" frente a riesgos OWASP.

**M4 – Tiempo medio de remediación (MTTR) de vulnerabilidades Top 10:2025**  
- **Definición:** tiempo medio entre la detección de una vulnerabilidad asociada a una categoría del Top 10:2025 en sistemas esenciales o importantes y su cierre efectivo en producción.[^34][^35][^36][^1]
- **Unidad:** días.  
- **Uso:** refleja la capacidad operativa de respuesta frente a riesgos priorizados.

### 3.2. Métricas de madurez de programa (SAMM)

**M5 – Score medio SAMM por función en organismos españoles**  
- **Definición:** media de los niveles SAMM (0–3) por función de negocio (Gobernanza, Diseño, Implementación, Verificación, Operaciones) en administraciones públicas y entidades sujetas a NIS2, calculada a partir de autoevaluaciones periódicas.[^20][^7][^2][^4]
- **Unidad:** valor medio en escala 0–3.  
- **Uso:** indicador global de madurez de seguridad de software.

**M6 – Porcentaje de entidades con nivel ≥2 en "Strategy and Metrics"**  
- **Definición:** porcentaje de organismos que alcanzan al menos nivel 2 en la práctica SAMM "Strategy and Metrics", lo que implica una estrategia de seguridad del software unificada y métricas implantadas.[^22][^2]
- **Unidad:** porcentaje de entidades.  
- **Uso:** indica el grado de institucionalización de la medición de la seguridad del software.

**M7 – Pendiente de mejora SAMM (ΔSAMM)**  
- **Definición:** variación anual media del score SAMM por práctica clave (p. ej., Verificación, Operaciones) en un conjunto estable de organizaciones españolas.[^23][^21]
- **Unidad:** puntos SAMM/año.  
- **Uso:** muestra la velocidad de maduración del ecosistema.

**M8 – Cobertura de autoevaluaciones SAMM**  
- **Definición:** porcentaje de entidades de un sector regulado que realizan una autoevaluación SAMM al menos cada dos años.[^2][^20][^23]
- **Unidad:** porcentaje de entidades.  
- **Uso:** refleja la adopción de SAMM como herramienta de gestión.

### 3.3. Métricas de verificación técnica (ASVS)

**M9 – Distribución de niveles ASVS por criticidad ENS/NIS2**  
- **Definición:** porcentaje de aplicaciones clasificadas como de criticidad alta, media o baja (según ENS/NIS2) que alcanzan, respectivamente, ASVS Nivel 3, 2 o 1.[^7][^24][^10][^4][^5]
- **Unidad:** porcentaje de aplicaciones por combinación criticidad/nivel ASVS.  
- **Uso:** permite comprobar si el nivel de aseguramiento técnico se ajusta a la criticidad regulatoria.

**M10 – Densidad de requisitos ASVS cumplidos por capítulo**  
- **Definición:** porcentaje de requisitos ASVS aplicables cumplidos en capítulos clave (por ejemplo, autenticación, control de acceso, gestión de sesiones, criptografía, logging, cadena de suministro) para cada aplicación crítica.[^24][^5]
- **Unidad:** porcentaje por capítulo.  
- **Uso:** identifica áreas técnicas con mayor deuda de seguridad.

**M11 – Cobertura de pruebas frente a ASVS**  
- **Definición:** porcentaje de requisitos ASVS aplicables que están cubiertos por pruebas automatizadas (SAST, DAST, SCA, tests de integración) y manuales (revisión de código, pentesting) en cada aplicación.[^33][^25][^5][^24]
- **Unidad:** porcentaje de requisitos cubiertos.  
- **Uso:** mide la robustez de la verificación en el SDLC.

**M12 – Ratio de defectos ASVS en producción**  
- **Definición:** número de requisitos ASVS no cumplidos detectados en producción (mediante incidentes, auditorías o revisiones forenses) por cada 100.000 usuarios activos o transacciones críticas.[^5][^24]
- **Unidad:** defectos por 100.000 usuarios/transacciones.  
- **Uso:** aproxima la "densidad de deuda de seguridad" que escapa al proceso de desarrollo.

### 3.4. Métricas de riesgo agregado (Risk Rating Methodology)

**M13 – Distribución de severidad OWASP (baja/media/alta) en infraestructuras críticas**  
- **Definición:** porcentaje de vulnerabilidades en infraestructuras críticas españolas clasificadas como de severidad baja, media o alta según la Risk Rating Methodology de OWASP (combinando probabilidad e impacto).[^3][^6][^28][^10][^26][^27]
- **Unidad:** porcentaje de vulnerabilidades por nivel de severidad.  
- **Uso:** indica si el perfil de riesgo está dominado por vulnerabilidades de alto impacto o por deuda de menor severidad.

**M14 – Riesgo medio normalizado OWASP por sector**  
- **Definición:** valor medio de Risk normalizado (por ejemplo, 1–10) calculado para vulnerabilidades en cada sector regulado por NIS2 (energía, transporte, salud, banca, infraestructuras digitales, etc.) usando la fórmula Risk = Likelihood * Impact y umbrales definidos.[^6][^28][^26][^3][^27][^7]
- **Unidad:** score medio 1–10.  
- **Uso:** permite comparar perfiles de riesgo entre sectores y priorizar esfuerzos regulatorios.

**M15 – Tiempo medio desde detección técnica a decisión de riesgo**  
- **Definición:** media de días entre la identificación de una vulnerabilidad de severidad alta según OWASP y la decisión formal de la alta dirección (o comité de riesgos) sobre el tratamiento (corregir, aceptar, transferir, mitigar).[^37][^26][^27][^6]
- **Unidad:** días.  
- **Uso:** conecta métricas técnicas con la gobernanza exigida por NIS2 en materia de responsabilidad de la alta dirección.[^9][^3]

## 4. Comparativa: métricas OWASP vs obligaciones NIS2 (España)

### 4.1. NIS2: ejes de gestión de riesgos y medidas técnicas

La Directiva NIS2 refuerza la gestión proactiva de riesgos, la obligación de notificar incidentes, la responsabilidad de la alta dirección y la necesidad de adoptar medidas técnicas y organizativas proporcionadas, especialmente en sectores esenciales y críticos. Para España, esto se articula a través de la transposición mediante una Ley de Coordinación y Gobernanza de la Ciberseguridad, que amplía el alcance del régimen de 2018 y establece una arquitectura nacional que integra CCN, INCIBE y autoridades sectoriales.[^8][^10][^3][^7][^34][^9]

El ENS, por su parte, es el marco nacional para la seguridad de la información en el sector público y entidades relacionadas, basado también en la gestión de riesgos y en la aplicación de medidas técnicas, organizativas y de continuidad diferenciadas por nivel (bajo, medio, alto). Ambos marcos requieren evidencias cuantificables de que los riesgos se gestionan y los controles se aplican de forma sistemática.[^38][^4][^7]

### 4.2. Tabla de alineamiento conceptual (OWASP → NIS2/ENS)

En la tabla siguiente se sintetiza la relación entre familias de métricas OWASP y dominios clave de NIS2/ENS para España.

| Dominio NIS2/ENS | Obligación principal (resumen) | Familia de métricas OWASP relevante | Ejemplos de métricas (de este informe) |
|------------------|--------------------------------|-------------------------------------|----------------------------------------|
| Gestión de riesgos (NIS2, ENS principios de riesgo) | Evaluar y gestionar riesgos de ciberseguridad de forma proactiva y continua.[^3][^4][^7][^9] | OWASP Risk Rating Methodology; SAMM Strategy and Metrics | M5 (score SAMM por función), M6 (entidades ≥ nivel 2 en Strategy and Metrics), M13 (distribución de severidad OWASP), M14 (riesgo medio por sector), M15 (tiempo detección–decisión). |
| Medidas técnicas de protección (acceso, configuración, vulnerabilidades) | Implantar controles de acceso, endurecimiento de sistemas, gestión de vulnerabilidades y medidas de prevención proporcionadas a los riesgos.[^3][^4][^7][^10] | OWASP Top 10:2025; ASVS 5.0 | M1 (densidad de vulnerabilidades por categoría Top 10), M2 (activos sin vulnerabilidades abiertas en A01–A03), M3 (cobertura de análisis), M9 (distribución de niveles ASVS), M10–M12 (cumplimiento y defectos ASVS). |
| Seguridad de la cadena de suministro | Evaluar y mitigar riesgos derivados de proveedores y dependencias, incluido software y servicios TIC.[^3][^7][^9][^10] | Top 10:2025 A03 – Software Supply Chain Failures; ASVS capítulos de integridad de software y actualizaciones | M1 y M2 filtradas por A03; M10/M11 en capítulos ASVS de integridad de software, actualizaciones y dependencias; indicadores específicos sobre SBOM y gestión de parches (no detallados en este informe). |
| Continuidad de servicios y resiliencia | Garantizar continuidad, copias de seguridad, recuperación y respuesta a incidentes.[^3][^4][^7][^34][^9] | SAMM Operaciones; ASVS (logging, monitorización); métricas de incidentes nacionales | M5 (madurez SAMM en Operaciones), M7 (ΔSAMM en Operaciones), M3 (cobertura de análisis), M4 (MTTR de vulnerabilidades Top 10), indicadores de INCIBE sobre incidentes y sistemas vulnerables.[^21][^12][^13][^23] |
| Gobernanza y responsabilidad de la alta dirección | Implicar a la alta dirección en las decisiones de ciberseguridad, con responsabilidad y posibles sanciones.[^3][^7][^9][^10] | SAMM Gobernanza; OWASP Risk Rating Methodology (impacto de negocio) | M5/M6 (madurez en Gobernanza y Strategy and Metrics), M15 (tiempo detección–decisión), indicadores de integración de riesgos OWASP en marcos de riesgos corporativos (no cuantificados aquí). |
| Notificación de incidentes | Notificar incidentes significativos en plazos de 24–72 horas y cooperar con autoridades.[^3][^34][^9][^10] | No hay un marco OWASP específico, pero ASVS y SAMM Operaciones cubren logging y respuesta | M3 (cobertura de logging/monitoreo vía ASVS), M4 (MTTR), métricas nacionales de incidentes gestionados por INCIBE/CCN.[^12][^13][^23] |

### 4.3. Aprovechar mappings y estándares relacionados

La comunidad OWASP mantiene mappings entre SAMM y otros estándares (NIST SSDF, ISO 27k, PCI-DSS, ASVS, NIST 800-53), lo que facilita traducir métricas SAMM/ASVS a requisitos de marcos más amplios que los reguladores conocen bien. Además, el proyecto OWASP OT Top 10 publica una tabla de mapping entre riesgos OT y la Directiva NIS2 (incluyendo referencias al Reglamento de Ejecución de la Comisión C(2024) 7151), mostrando cómo puede alinearse una taxonomía OWASP con requisitos europeos detallados.[^39][^40]

Aunque ese mapping se centra en entornos OT, ilustra una aproximación que España podría aplicar al contexto TI: mapear, por ejemplo, A03 (Software Supply Chain Failures) y requisitos ASVS de integridad de software a las obligaciones de NIS2 sobre seguridad de la cadena de suministro, o las prácticas SAMM de Operaciones a los requisitos de monitorización y respuesta a incidentes de la normativa.

## 5. Consideraciones sobre umbrales y su fijación en España

Ni OWASP ni NIS2 fijan umbrales numéricos universales para métricas concretas (porcentaje de aplicaciones en ASVS Nivel 2, tiempo máximo de remediación, etc.); en su lugar exigen una gestión de riesgos proporcionada y basada en el contexto. Esto implica que los umbrales medibles deben definirse políticamente (regulador), estratégicamente (gobierno corporativo) o contractualmente (pliegos ENS/NIS2), tomando OWASP como referencia técnica, pero no como fuente normativa directa.[^3][^4][^7][^9]

Para España, un enfoque razonable podría consistir en:

- **Definir umbrales mínimos obligatorios por tipo de entidad y criticidad**, utilizando métricas como M2 (ausencia de vulnerabilidades altas/críticas en A01–A03), M9 (nivel ASVS mínimo por criticidad) o M13/M14 (porcentaje máximo de vulnerabilidades de severidad alta).[^15][^6][^7][^5]
- **Utilizar métricas de madurez SAMM (M5–M8) como objetivos de mejora**, por ejemplo exigiendo nivel ≥2 en determinadas prácticas a medio plazo para sectores esenciales.
- **Incorporar métricas de tiempo (M4, M15)** como SLA internos y regulatorios (sin fijar aquí números específicos), en línea con las exigencias de notificación rápida de incidentes y con la responsabilidad de la alta dirección.[^10][^34][^9][^3]

En todos los casos, los umbrales deberían revisarse periódicamente en función de datos empíricos (por ejemplo, informes de INCIBE, encuestas nacionales tipo Reino Unido, evaluaciones de amenaza como las canadienses) y de la evolución tecnológica y de amenazas.[^41][^36][^12]

## 6. Conclusiones

Los marcos OWASP vigentes en 2025 proporcionan una base sólida para definir métricas cuantitativas de ciberseguridad aplicables a España, desde la exposición a categorías del Top 10:2025 hasta la madurez de programas (SAMM), el nivel de verificación técnica (ASVS 5.0) y los perfiles de riesgo agregados (Risk Rating Methodology). Estas métricas son compatibles y complementarias con las exigencias de la Directiva NIS2 y del ENS, pero requieren que reguladores y organizaciones definan sus propios umbrales en función de riesgos, criticidad y capacidad de implementación.[^18][^1][^4][^6][^7][^24][^8][^9][^2][^3][^5]

Para España, la combinación de datos empíricos (como los incidentes y sistemas vulnerables identificados por INCIBE en 2025), la arquitectura institucional de ciberseguridad y la existencia de marcos normativos consolidados ofrece una oportunidad clara para institucionalizar un cuadro de mando nacional basado en OWASP. La clave no está solo en medir, sino en asegurar que cada métrica se conecta de forma explícita con decisiones de inversión, prioridades regulatorias y responsabilidades de la alta dirección, cumpliendo así tanto el espíritu como la letra de NIS2.[^13][^14][^12][^4][^7][^8]

---

## References

1. [What are Application Security Risks? - OWASP Top 10:2025](https://owasp.org/Top10/2025/0x02_2025-What_are_Application_Security_Risks/) - What are Application Security Risks? Attackers can potentially use many different paths through your...

2. [Strategy and Metrics - OWASP SAMM](https://owaspsamm.org/model/governance/strategy-and-metrics/) - Software assurance entails many different activities and concerns. Without an overall plan, you migh...

3. [The European NIS2 Directive strengthens cybersecurity in Spain ...](https://www.dominios.es/en/informacion-de-interes/noticias/european-nis2-directive-strengthens-cybersecurity-spain-leading) - The implementation of NIS2 in Spain will strengthen the security of critical strategic services, pos...

4. [What measures do the European NIS 2 Directive and the National ...](https://appsec.es/en/what-measures-do-the-european-nis-2-directive-and-the-national-security-scheme-coincide-in/) - Risk-Based Approach: NIS 2 establishes the need to carry out risk assessments and adopt security mea...

5. [OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/) - The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web...

6. [OWASP Risk Rating Methodology](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology) - Risk = Likelihood * Impact. In the sections below, the factors that make up “likelihood” and “impact...

7. [ENS and NIS2: key cybersecurity regulations in Spain](https://eiposgrados.com/eng/cybersecurity-blog/ens-y-nis2-ciberseguridad/) - Descubre qué son el ENS y NIS2, cómo impactan en empresas y por qué la ciberseguridad es clave para ...

8. [Transposition in Spain - NIS 2 Directive](https://www.nis-2-directive.com/Transposition/Spain.html) - The proposed legislation is a substantial reform of Spain's cybersecurity regulatory architecture. A...

9. [ENS and NIS2: key cybersecurity regulations in Spain](https://eiposgrados.com/eng/cybersecurity-blog/ens-and-nis2-cybersecurity/) - Discover what the ENS and NIS2 are, how they impact companies, and why cybersecurity is key to your ...

10. [NIS2 Regulations: Obligations and requirements for companies](https://edorteam.com/en/nis2-regulations-obligations-and-requirements-for-companies/) - The NIS2 Directive requires companies in essential sectors to adopt advanced protection and risk man...

11. [OWASP Top 10:2025](https://owasp.org/Top10/2025/en/) - It represents a broad consensus about the most critical security risks to web applications. About Th...

12. [INCIBE gestionó 122.223 incidentes de ciberseguridad en 2025, un ...](http://espanadigital.gob.es/en/actualidad/incibe-gestiono-122223-incidentes-de-ciberseguridad-en-2025-un-26-mas-que-el-ano) - El Instituto Nacional de Ciberseguridad (INCIBE), dependiente del Ministerio para la Transformación ...

13. [INCIBE gestionó 122.223 incidentes de ciberseguridad en 2025, un ...](http://espanadigital.gob.es/gl/actualidad/incibe-gestiono-122223-incidentes-de-ciberseguridad-en-2025-un-26-mas-que-el-ano) - El Instituto Nacional de Ciberseguridad (INCIBE), dependiente del Ministerio para la Transformación ...

14. [The Government approves a strengthening of Spain's ...](https://digital.gob.es/en/comunicacion/notas-prensa/mtdfp/2025/05/2025-05-06_02)

15. [Introduction - OWASP Top 10:2025](https://owasp.org/Top10/2025/0x00_2025-Introduction/) - OWASP Top 10:2025

16. [OWASP Top 10 2025: Key Changes & What They Mean](https://orca.security/resources/blog/owasp-top-10-2025-key-changes/) - The OWASP Top 10 2025 release candidate is here, marking an important milestone in the evolution of ...

17. [OWASP Top 10 2025: What's changed and why it matters - GitLab](https://about.gitlab.com/blog/2025-owasp-top-10-whats-changed-and-why-it-matters/) - The OWASP Top 10 2025: Complete breakdown · A01: Broken Access Control · A02: Security Misconfigurat...

18. [OWASP Top 10:2025](https://owasp.org/Top10/2025/) - OWASP Top 10:2025. Welcome to the OWASP Top 10:2025 Release. The OWASP Top 10 is a standard awarenes...

19. [OWASP Top Ten Web Application Security Risks](https://owasp.org/www-project-top-ten/) - OWASP Top 10 2025 Data Analysis Plan. Goals. To collect the most comprehensive dataset related to id...

20. [How OWASP SAMM compares...](https://codific.com/owasp-samm-comprehensive-introduction/) - Learn what OWASP SAMM is, how it compares to other frameworks, and how to start improving your softw...

21. [OWASP SAMM Benchmark Data Analysis - Codific](https://codific.com/owasp-samm-benchmark/) - View the latest OWASP SAMM Benchmark data including our in-depth analysis and interpretation of the ...

22. [OWASP SAMM: Measure and Improve - WiseSec](https://wisesec.nl/owasp-samm-measure-and-improve/) - Basic information about the efficacy and efficiency of your AppSec program

23. [Introducing the SAMM Benchmark Report](https://owaspsamm.org/blog/2025/05/07/introducing-the-samm-benchmark-report/) - A comprehensive analysis based on real-world data that provides actionable insights into the current...

24. [OWASP ASVS: A Comprehensive Overview - Codific](https://codific.com/owasp-asvs-a-comprehensive-overview/) - Version 5.0, released in May 2025, includes about 350 requirements across 17 chapters, making applic...

25. [Establishing a Modern Application Security Program](https://owasp.org/Top10/2025/0x03_2025-Establishing_a_Modern_Application_Security_Program/) - We would encourage anyone wanting to adopt an application security standard to use the OWASP Applica...

26. [The OWASP Risk Rating Methodology and SimpleRisk](https://www.simplerisk.com/blog/owasp-risk-rating-methodology-and-simplerisk) - Risk scoring methodologies vary widely, but understanding how to prioritize risks is key to managing...

27. [A deep dive into the OWASP risk rating methodology](https://beaglesecurity.substack.com/p/a-deep-dive-into-the-owasp-risk-rating) - The OWASP Risk Rating Methodology typically uses a simple risk matrix or formula to combine the like...

28. [OWASP vs. CVSS: A Practical Guide](https://www.practical-devsecops.com/owasp-risk-rating-methodology-vs-cvss/) - Confused about OWASP and CVSS? This in-depth guide breaks down the differences, pros, and cons of ea...

29. [CVE-2024-31061 - Vulnerabilidades - INCIBE](https://www.incibe.es/incibe-cert/alerta-temprana/vulnerabilidades/cve-2024-31061) - Fecha de publicación: 28/03/2024. Última modificación: 03/04/2025 ... https://github.com/sahildari/c...

30. [CVE-2024-35582 - Vulnerabilidades - INCIBE](https://www.incibe.es/incibe-cert/alerta-temprana/vulnerabilidades/cve-2024-35582) - Referencias a soluciones, herramientas e información · https://github.com/r04i7/CVE/blob/main/CVE-20...

31. [OWASP Top 10 2025: Key Changes and What Developers Should ...](https://www.aikido.dev/blog/owasp-top-10-2025-changes-for-developers) - For organizations that want a measurable, testable standard, OWASP recommends pairing the Top 10 wit...

32. [OWASP SAMM Software Assurance Maturity Model - Xygeni](https://xygeni.io/articles/owasp-samm-software-assurance-maturity-model/) - The OWASP SAMM – Software Assurance Maturity Model provides a structured framework for assessing and...

33. [Application Security Frameworks: A Practical Guide to OWASP ...](https://www.globaldots.com/resources/blog/application-security-frameworks/) - You can map ASVS controls or NIST control families to pipeline gates. Rely heavily on Infrastructure...

34. [NIS2 Directive Spain: Cybersecurity Requirements 2025 | Flexxible](https://www.flexxible.com/en/blog/nis2-directive-spain) - The regulation was approved in 2022 and came into force in Spain on October 17, 2024, initiating its...

35. [Application Security in 2025: What the Data Really Tells Us](https://www.2ns.fi/en/application-security-in-2025-what-the-data-really-tells-us/) - Based on our own findings — and reflected as well in the OWASP Top 10 (2025) mapping — Broken Access...

36. [National Cyber Threat Assessment 2025-2026 - Canadian Centre ...](https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026) - The National Cyber Threat Assessment 2025-2026 highlights the cyber threats facing individuals and o...

37. [[XML] https://public-pages-files-2025.frontiersin.org/journals/big-data ...](https://public-pages-files-2025.frontiersin.org/journals/big-data/articles/10.3389/fdata.2024.1381163/xml/nlm) - > <!DOCTYPE article PUBLIC "-//NLM//DTD Journal ... Cybersecurity Lab, University of Piraeus ... met...

38. [Why complying with ENS, ISO 27001 and NIS2 is not optional - SQS](https://www.sqs.es/why-complying-with-ens-iso-27001-and-nis2-is-not-optional/?lang=en) - NIS2 requires: Active management of cyber risk,; Specific technical measures,; Incident notification...

39. [SAMM Mappings](https://owaspsamm.org/resources/mappings/) - The SAMM core team has created mappings between IEC-62443-4-1 and OWASP SAMM. You can find the mappi...

40. [Standards Mapping Table - OWASP OT Top 10](https://ot.owasp.org/v/2025/appendix/mappingTable/) - The following table maps the OWASP OT top 10 items to relevant standard and legislative requirements...

41. [Cyber security breaches survey 2025 - GOV.UK](https://www.gov.uk/government/statistics/cyber-security-breaches-survey-2025/cyber-security-breaches-survey-2025) - This report summarises key findings from the survey, highlighting trends in cyber security awareness...

