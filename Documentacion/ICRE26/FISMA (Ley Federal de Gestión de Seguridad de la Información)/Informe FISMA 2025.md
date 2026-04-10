# Informe FISMA 2025: Indicadores, Métricas de Ciberseguridad y su Aplicación Territorial en España

## Resumen Ejecutivo

La Ley Federal de Gestión de Seguridad de la Información de los Estados Unidos (*Federal Information Security Modernization Act*, FISMA), en su ciclo fiscal FY2025, ha cristalizado en la versión definitiva **FY2025 IG FISMA Reporting Metrics v2.0** (publicada el 3 de abril de 2025), con 25 indicadores estructurados en seis funciones y diez dominios alineados con el **NIST Cybersecurity Framework (CSF) 2.0**. Tres novedades de primer orden marcan este ciclo: la irrupción de la función **Govern** como eje de gobernanza corporativa de la ciberseguridad, la reubicación y renombrado del dominio de seguridad en la cadena de suministro (**C-SCRM**), y la incorporación de dos métricas suplementarias dedicadas a la **Arquitectura Zero Trust (ZTA)**.[^1][^2]

Para España, la traslación de este paradigma norteamericano al entorno autonómico no es un ejercicio de ingeniería comparada sino una necesidad estratégica de primer orden: el **Esquema Nacional de Seguridad (ENS)**, regulado por el Real Decreto 311/2022, y el Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad, aprobado el 14 de enero de 2025 para transponer la Directiva NIS2, constituyen los vectores nacionales más próximos al modelo FISMA. Con 122.223 incidentes gestionados por INCIBE en 2025 —un 26% más que en 2024— y 278 incidentes críticos gestionados por el CCN-CERT —un abrumador +293% en un solo año—, la urgencia de un sistema métrico robusto, comparable e interoperable con estándares internacionales deja de ser académica para convertirse en imperativo de Estado.[^3][^4][^5][^6]

***

## 1. Marco Normativo FISMA FY2025: La Arquitectura del Rigor

### 1.1 Genealogía y Base Jurídica

La FISMA original de 2002, reformulada en 2014 (Public Law 113-283), asigna a la **Oficina de Gestión y Presupuesto (OMB)** la supervisión de las políticas de seguridad, a la **Agencia de Ciberseguridad e Infraestructura (CISA)** la coordinación operativa y la implementación de directivas vinculantes, y al **Director Nacional de Ciberseguridad** la estrategia de conjunto. El memorándum **OMB M-25-04** (*Fiscal Year 2025 Guidance on Federal Information Security and Privacy Management Requirements*, publicado el 14 de enero de 2025) establece los principios rectores del ciclo anual:[^7][^8]

- **Automatización como norma, no como excepción**: las agencias deben suministrar métricas en formato *machine-readable* incluso donde la automatización plena no sea aún posible.[^8]
- **Datos orientados a resultados**: el foco se desplaza del inventario documental al impacto real sobre la postura de riesgo.[^8]
- **Integración del Programa CDM**: al menos el 90% del equipamiento gubernamental (*Government-Furnished Equipment*, GFE) debe reportarse a través del Programa de **Diagnóstico y Mitigación Continuos (CDM)** de CISA.[^8]
- **Alineación con Zero Trust**: los indicadores para FY2025 incorporan progresión medible hacia la arquitectura ZTA conforme al **Zero Trust Maturity Model v2.0** de CISA, en sintonía con el CSF 2.0.[^9][^8]

### 1.2 El CDM como Columna Vertebral de la Automatización

El Programa CDM de CISA —dotado con **469,8 millones de dólares** en el presupuesto FY2025— opera como el sistema nervioso de la monitorización federal continua. Provee a cada agencia un *dashboard* automatizado que agrega datos de herramientas de seguridad en tiempo casi real y los transfiere al *Federal Dashboard* de DHS para evaluación del conjunto del gobierno. A partir de 2024, el programa amplió su alcance a sistemas de **Tecnología Operacional (OT) e IoT**, un giro que se refleja directamente en los indicadores FY2025 de gestión de activos.[^10][^11][^12]

***

## 2. Los 25 Indicadores FISMA FY2025: Anatomía del Marco Métrico

### 2.1 Estructura: Funciones, Dominios y Tipología

Los **FY2025 IG FISMA Reporting Metrics v2.0** organizan 25 indicadores en seis funciones del NIST CSF 2.0 y diez dominios. El sistema distingue entre **20 métricas core** (evaluación anual obligatoria) y **5 métricas suplementarias** (métricas 1, 2, 3, 10 y 27) en alcance para FY2025.[^13][^2][^14][^1]

| Función CSF 2.0 | Dominio FISMA | Tipo de métricas incluidas |
|---|---|---|
| **Govern** | Cybersecurity Governance *(nuevo FY2025)* | Gobernanza, perfiles CSF, tolerancia al riesgo[^2] |
| **Govern** | C-SCRM *(reubicado desde Identify)* | Cadena de suministro, proveedores externos[^15][^2] |
| **Identify** | Risk and Asset Management *(nuevo agrupamiento)* | Inventario de sistemas, hardware, software, datos[^2] |
| **Protect** | Configuration Management | Líneas base seguras, gestión de parches[^2] |
| **Protect** | Identity and Access Management (IDAM) | MFA, control de acceso, gestión de privilegios[^2] |
| **Protect** | Data Protection and Privacy | Cifrado, clasificación de datos, privacidad[^2] |
| **Protect** | Security Training | Formación, concienciación, simulacros[^2] |
| **Detect** | Information Security Continuous Monitoring (ISCM) | CDM, EDR, detección de anomalías[^2] |
| **Respond** | Incident Response | Playbooks, tiempos de respuesta, notificación[^2] |
| **Recover** | Contingency Planning | Continuidad de negocio, recuperación[^2] |

### 2.2 La Nueva Función Govern: El Gobierno como Palanca de Madurez

La incorporación del **dominio Cybersecurity Governance** es la innovación arquitectónica más significativa del ciclo FY2025. En el NIST CSF 2.0 publicado en febrero de 2024, la función *Govern* consolida los objetivos de gobernanza dispersos en la versión 1.1 y eleva la ciberseguridad a asunto del consejo de dirección. Las tres métricas suplementarias de esta función evalúan:[^16][^17][^2][^14]

- La **utilización de perfiles CSF** para articular, priorizar y comunicar objetivos de ciberseguridad.[^2]
- La **estrategia de gestión del riesgo cibernético** que defina prioridades, restricciones y niveles de tolerancia al riesgo.[^2]
- Los **procesos y autoridades de rendición de cuentas**, la evaluación del desempeño y la mejora continua.[^2]

Esta orientación produce una consecuencia de enorme importancia para la comparativa internacional: los indicadores FISMA FY2025 exigen evidencia no sólo de controles técnicos sino de **gobernanza corporativa de la ciberseguridad**, algo que el ENS español solo contempla implícitamente a través de la política de seguridad.

### 2.3 El Dominio C-SCRM: La Cadena de Suministro como Riesgo Estratégico

El traslado del dominio de **Gestión de Riesgos en la Cadena de Suministro Cibernético (C-SCRM)** desde la función *Identify* a la función *Govern* refleja un cambio de paradigma conceptual: la cadena de suministro ya no es un asunto técnico sino una **responsabilidad de gobernanza corporativa**. La guía de adquisición C-SCRM del GSA (abril 2025) especifica que los indicadores IG FISMA FY2023/2024 ya evaluaban la madurez C-SCRM en cuatro dimensiones, y en FY2025 este dominio opera bajo la función *Govern*, exigiendo a las agencias demostrar:[^18][^15][^2]

- Políticas y procedimientos documentados para productos, componentes y servicios de terceros.[^2]
- Identificación y priorización de proveedores externos con acceso a sistemas críticos.[^2]
- Integración de requisitos de ciberseguridad en los contratos de adquisición.[^2]

Los resultados FY2025 revelaron que este dominio es el talón de Aquiles sistémico: la FTC, por ejemplo, alcanzó únicamente **Level 3 (Consistently Implemented)** en C-SCRM, con una POA&M pendiente de resolución.[^2]

### 2.4 Las Dos Métricas Zero Trust: Midiendo lo Inmaterial

El FY2025 introduce **dos métricas suplementarias** específicamente diseñadas para evaluar el progreso hacia la Arquitectura Zero Trust (ZTA):[^2]

1. **Capacidades de gestión de datos** (*data management capabilities*): mide la madurez de la agencia para inventariar, clasificar, proteger y monitorizar sus datos como activo crítico, alineándose con el pilar *Data* del ZTA.[^9][^2]
2. **Monitorización e integridad de activos propios y asociados**: evalúa la capacidad de monitorizar y medir continuamente la integridad y la postura de seguridad de todos los activos controlados por la agencia, incluidos dispositivos no convencionales como IoT y OT.[^12][^2]

Estas métricas se enmarcan en la implementación progresiva de **OMB M-22-09** (*Moving the U.S. Government Toward Zero Trust Cybersecurity Principles*) y el *CISA Zero Trust Maturity Model v2.0*, cuya alineación con el NIST CSF 2.0 era un objetivo explícito del memorándum M-25-04 para finales de FY2025.[^8]

### 2.5 El Modelo de Madurez de 5 Niveles

La escala de evaluación, heredada y perfeccionada desde FY2022, clasifica los programas de seguridad en cinco niveles:[^14][^2]

| Nivel | Denominación | Descripción operativa | ¿Efectivo? |
|---|---|---|---|
| **1** | Ad Hoc | Sin formalización; respuesta reactiva y personalista | ✗ |
| **2** | Defined | Políticas documentadas pero implementación inconsistente | ✗ |
| **3** | Consistently Implemented | Implementación uniforme; sin métricas cuantitativas | ✗ |
| **4** | Managed and Measurable | Métricas cuantitativas y cualitativas; gestión basada en datos | ✓ |
| **5** | Optimized | Institucionalización plena; mejora continua y autoregenerativa | ✓ |

Los niveles 4 y 5 constituyen el umbral de efectividad según la guía OMB. El cálculo del nivel global utiliza **medias ponderadas por función**, sin redondeo automático, para preservar la granularidad analítica. En FY2025, agencias como la GSA lograron el nivel 5 (Optimized) en la función *Detect*, mientras que la AmeriCorps se mantuvo en nivel 3 global, ilustrando la enorme dispersión entre agencias.[^19][^20][^13][^14][^2]

***

## 3. Métricas CIO FY2025: El Eje de Reporte Automatizado

Paralelamente a los indicadores IG, las agencias deben alimentar trimestralmente los **CIO FISMA Metrics** a OMB y CISA vía **CyberScope**, el portal federal de reporte de ciberseguridad. Los CIO metrics para FY2025 amplían la cobertura automatizada y exigen:[^19][^8]

- **Reporte de inventario de activos**: al menos el 90% de los dispositivos GFE deben estar incluidos en el programa CDM con herramientas EDR desplegadas.[^8]
- **Métricas de registro de eventos**: conformidad con **OMB M-21-31** (*Improving the Federal Government's Investigative and Remediation Capabilities Related to Cybersecurity Incidents*), que exige niveles de logging graduados (EL1 a EL3) según la criticidad del sistema.[^8][^2]
- **Indicadores de progreso Zero Trust**: métricas trimestrales sobre los cinco pilares ZTA (Identidad, Dispositivos, Redes, Aplicaciones/Cargas de trabajo, Datos).[^8]
- **Reporte de incidentes mayores**: inventario de todos los incidentes con impacto significativo sobre datos personales (*PII*), con detalle de amenazas, vulnerabilidades, número de afectados y acciones de remediación.[^8]
- **Datos IoT/OT**: inventario completo de dispositivos IoT establecido como requisito desde FY2024 y en maduración activa en FY2025.[^21]

El Subcomité de Métricas FISMA del CISO Council Federal tiene el mandato explícito de **identificar métricas adicionales susceptibles de automatización** y de madurar los indicadores de medición de la arquitectura Zero Trust a lo largo del ciclo.[^8]

***

## 4. Resultados FY2025: El Estado Real de la Ciberseguridad Federal

Los datos de las auditorías publicadas en 2025-2026 revelan un panorama heterogéneo pero con tendencia consolidada hacia el nivel 4:

| Agencia | Nivel Global | Punto de Fortaleza | Área de Mejora |
|---|---|---|---|
| GSA | 4/5 (Detect: 5) | Monitorización continua | — [^19] |
| FTC | 4 (Efectivo) | Security Training (L5) | C-SCRM, Event Logging [^2] |
| DFC | 4 (Efectivo) | Gestión generalizada | Data protection [^1] |
| CIGIE | 4/5 | 5 de 6 funciones en L4 | — [^22] |
| AmeriCorps | 3 (No efectivo) | — | Múltiples funciones [^13] |
| USITC | 4 (Efectivo) | Gestión global | — [^23] |

El patrón sistemático más recurrente en las auditorías FY2025 es el **rezago en C-SCRM** y el **incumplimiento de los requisitos de registro de eventos (Event Logging)** según M-21-31. Ambas debilidades apuntan a la misma realidad estructural: la madurez organizativa y la gobernanza corporativa siguen siendo el eslabón más débil del sistema, precisamente los ámbitos que la nueva función *Govern* de NIST CSF 2.0 pretende sistematizar.[^15][^2]

***

## 5. Aplicación Territorial en España: Del Océano Atlántico al Archipiélago Autonómico

### 5.1 El ENS como Arquitectura Análoga

El **Esquema Nacional de Seguridad (ENS)**, actualizado por el Real Decreto 311/2022, es el análogo funcional más próximo a FISMA en el ecosistema español. Obligatorio para todas las administraciones públicas —desde la Administración General del Estado hasta el último municipio— y extensivo a las empresas privadas proveedoras del sector público, el ENS estructura la seguridad en torno a:[^24][^25][^26]

- **Cinco principios básicos**: seguridad integral, gestión basada en riesgos, prevención-detección-respuesta-conservación, existencia de líneas de defensa, vigilancia continua y diferenciación de responsabilidades.[^26]
- **Tres categorías de sistemas**: Básica, Media y Alta, determinadas por el impacto potencial de una brecha sobre la confidencialidad, integridad, disponibilidad, trazabilidad y autenticidad.[^27][^28]
- **Certificación formal** obligatoria para sistemas de categoría Media y Alta, a través de entidades acreditadas por ENAC bajo la norma UNE-EN ISO/IEC 17065:2012.[^29]

La herramienta **INES** (*Informe Nacional del Estado de Seguridad*), gestionada por el CCN, es el equivalente funcional al CyberScope americano: permite la recogida anual de indicadores sobre el estado de cumplimiento ENS de cada entidad pública, incluyendo ahora, obligatoriamente, a las empresas privadas proveedoras desde la entrada en vigor del RD 311/2022. INES, junto con AMPARO (para la adecuación), MARGA y PILAR (para el análisis de riesgos), conforman el ecosistema de **gobernanza de la ciberseguridad nacional** del CCN.[^30][^31][^32][^25]

### 5.2 La Realidad Autonómica: Heterogeneidad Estructural

La arquitectura territorial española, con sus 17 Comunidades Autónomas como titulares de servicios esenciales —sanidad, educación, servicios sociales, medio ambiente, infraestructuras—, genera un mapa de madurez profundamente desigual. Mientras los estudios disponibles indican que el **87% de los ayuntamientos catalanes** utilizan soluciones administrativas electrónicas certificadas ENS, sólo **41 municipios en toda España** habían alcanzado la certificación ENS completa a mediados de 2025, una cifra que, frente a los más de 8.000 municipios existentes, resulta... llamémosla "mejorable con energía renovable".[^33]

Las debilidades estructurales identificadas en el entorno autonómico son:

- **Fragmentación de capacidades**: cada comunidad autónoma desarrolla sus capacidades de forma mayoritariamente autónoma, lo que genera economías de escala desaprovechadas y ausencia de métricas comparables entre territorios.[^34]
- **Déficit de coordinación**: el informe *España, Hub de Ciberseguridad Europeo* del Foro Nacional de Ciberseguridad señala que la colaboración autonómica es "voluntaria" y recomienda "incremento y consolidación de procesos transversales".[^34]
- **Vulnerabilidad acreditada**: en 2025 se documentaron ataques de ransomware que dejaron inoperativos durante dos semanas los sistemas informáticos municipales de Melilla y Villajoyosa (Alicante), con impacto sobre servicios administrativos esenciales.[^35]
- **Brecha NIS2**: España inició procedimientos de infracción ante la Comisión Europea por no completar la transposición de NIS2 antes de octubre de 2024, aunque el Anteproyecto de Ley de Coordinación y Gobernanza de Ciberseguridad aprobado en enero de 2025 puso en marcha el proceso.[^4][^36][^5]

### 5.3 La Estrategia Sectorial Autonómica: El Caso del SNS

El avance más relevante en la aplicación territorial de métricas estructuradas en 2025 proviene del sector sanitario. El **Consejo Interterritorial del Sistema Nacional de Salud (CISNS)** aprobó en noviembre de 2025 la **Estrategia de Ciberseguridad del SNS 2025-2028**, elaborada con la participación activa de las CC.AA. de Andalucía, Cataluña, Comunidad Valenciana, Galicia e Islas Baleares. Esta estrategia define ocho objetivos y doce ejes, entre los que destacan:[^37][^38]

- Creación de una **red nacional de colaboración sobre ciberincidentes** entre administraciones autonómicas de salud.[^37]
- Integración de indicadores alineados con **ENS y NIS2** como base de cumplimiento normativo.[^38][^37]
- Protección de la cadena de suministro sanitaria, con inventario de activos y evaluación de proveedores tecnológicos.[^38]
- Métricas de continuidad asistencial ante incidentes: el ransomware es la amenaza dominante en el sector.[^37]

Paralelamente, el convenio RETECH entre INCIBE y las CC.AA. de Cataluña, Galicia, Comunidad Valenciana, Canarias, Cantabria, Murcia y Navarra establece redes territoriales de especialización tecnológica en ciberseguridad, con financiación del Plan de Recuperación (Next Generation EU), creando por primera vez una estructura de colaboración autonómica con métricas compartidas.[^39][^40]

### 5.4 La Nueva Arquitectura Institucional: El Centro Nacional de Ciberseguridad

El elemento más transformador para la aplicación territorial del modelo FISMA en España es la creación del **Centro Nacional de Ciberseguridad (CNC)**, contemplada en el Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad (enero 2025). El CNC se concibe como:[^5]

- **Autoridad nacional competente única** en materia de ciberseguridad, adscrita a la Presidencia del Gobierno.[^5]
- **Punto de contacto único** para la cooperación intersectorial y transfronteriza, actuando como interlocutor ante la UE.[^5]
- **Autoridad nacional de gestión de crisis de ciberseguridad**, equivalente funcional al rol operativo de CISA en el modelo FISMA.[^5]

El Consejo de Seguridad Nacional aprobó en abril de 2025 el procedimiento para elaborar una nueva **Estrategia Nacional de Ciberseguridad**, reconociendo explícitamente los retos emergentes de la inteligencia artificial y la computación cuántica como vectores de transformación del panorama de amenazas.[^41]

***

## 6. Análisis Comparativo: FISMA vs. ENS vs. NIS2

La comparativa de los tres marcos en sus dimensiones métricas más relevantes revela convergencias profundas en los principios y divergencias significativas en la implementación:

| Dimensión | FISMA FY2025 | ENS (RD 311/2022) | NIS2 / Anteproyecto España 2025 |
|---|---|---|---|
| **Ámbito de aplicación** | Agencias federales EE.UU. y contratistas[^42] | Sector público español + proveedores TI privados[^24] | Entidades esenciales e importantes; 18 sectores[^43][^4] |
| **Marco de referencia** | NIST CSF 2.0 + SP 800-53 Rev.5[^42][^17] | ISO/IEC 27001 + NIST CSF 2.0 (implícito)[^27] | ENISA Technical Guidance (junio 2025, 170 pp.)[^44][^45] |
| **Modelo de madurez** | 5 niveles (Ad Hoc → Optimized); umbral efectividad: L4[^14] | 3 categorías de sistema (Básica/Media/Alta)[^28] | Madurez implícita; evaluación por autoridades nacionales[^46] |
| **Número de métricas** | 25 (20 core + 5 suplementarias)[^13][^2] | Sin número fijo; guías CCN-STIC (>100 controles)[^30] | Sin métricas prescriptivas; 13 áreas temáticas ENISA[^44] |
| **Función de gobernanza** | Sí, explícita (función *Govern* FY2025)[^2] | Implícita (Art. 13 RD 311/2022)[^26] | Sí: responsabilidad ejecutiva explícita; directivos formados[^47] |
| **Cadena de suministro** | Dominio C-SCRM bajo *Govern* (nuevo FY2025)[^15][^2] | Art. 19: adquisición productos/servicios seguros[^26] | Obligación explícita: evaluación de riesgos de terceros[^47] |
| **Zero Trust** | 2 métricas suplementarias ZTA en FY2025[^2] | Sin mención explícita | Sin mención directa; implícito en segmentación |
| **Certificación** | Authority to Operate (ATO) + auditoría IG anual[^42] | Obligatoria sistemas Media/Alta; ENAC[^29] | No prescriptiva; certificaciones tipo ENS reconocidas[^48] |
| **Notificación incidentes** | Anual + situacional para incidentes mayores[^8][^47] | Según ITS de Notificación CCN-CERT[^46] | Alerta: <24h; notificación completa: <72h[^46][^47] |
| **Automatización** | CDM obligatorio; 90% activos GFE[^8][^10] | INES anual (no automatizado) + CCN-SAT (monitorización)[^25] | Sin requisito de automatización específico |
| **Sanciones** | Sin multas directas; consecuencias contractuales[^47] | Marco sancionador español (LOPDGDD)[^46] | Hasta 10M€ o 2% facturación global (esenciales)[^47][^46] |
| **Herramienta de reporte** | CyberScope (DHS)[^19] | INES (CCN)[^25] | Plataformas nacionales de cada Estado Miembro |
| **Evaluación independiente** | IG anual obligatorio[^23] | Auditoría bienal obligatoria sistemas Media/Alta[^29] | Auditorías periódicas por autoridades nacionales[^48] |

### 6.1 Convergencias Profundas

Los tres marcos comparten una constelación de principios que apuntan hacia una **gramática universal de la ciberseguridad institucional**:

- **Gestión basada en riesgos**: los tres rechazan el modelo de cumplimiento-casilla-marcada en favor de la evaluación continua del riesgo real.[^42][^46][^27]
- **Monitorización continua**: FISMA vía CDM, ENS mediante vigilancia continua como principio básico (Art. 10 RD 311/2022) y NIS2/ENISA con requisitos de detección temprana.[^11][^44][^26]
- **Cadena de suministro**: los tres marcos exigen gestión proactiva de riesgos de terceros, aunque con diferente nivel de prescripción.[^49][^47][^18]
- **Gobernanza de alto nivel**: FISMA FY2025 lo formaliza en métricas; NIS2 lo prescribe mediante responsabilidad ejecutiva; ENS lo implica a través de la política de seguridad del organismo.[^47][^26][^2]

### 6.2 Divergencias Estructurales

Las diferencias más relevantes desde una perspectiva de aplicación territorial española son:

- **Granularidad métrica**: FISMA opera con 25 indicadores cuantificados y un modelo de madurez de 5 niveles con medias ponderadas; el ENS trabaja con controles técnicos sin puntuación agregada comparable; NIS2 define 13 áreas temáticas sin prescribir métricas concretas.[^44][^46][^2]
- **Automatización como mandato**: la obligatoriedad del CDM y el formato *machine-readable* en FISMA no tiene equivalente ni en ENS ni en NIS2, aunque la UE trabaja en esta dirección a través de ENISA.[^50][^8]
- **Zero Trust como métrica**: FISMA es el único de los tres marcos que incorpora indicadores específicos de ZTA como criterio de evaluación formal; ENS y NIS2 lo contemplan indirectamente como práctica recomendada.[^2]

***

## 7. Propuesta de Adaptación: Indicadores FISMA para la Administración Autonómica Española

La aplicación de los indicadores FISMA al ámbito autonómico español requiere una **adaptación normativa contextualizada**, no una mera traducción. A continuación se propone una correspondencia operativa entre los 10 dominios FISMA FY2025 y su correlato en el ecosistema normativo español:

| Dominio FISMA FY2025 | Equivalente ENS/NIS2/CCN | Indicador operativo propuesto para CC.AA. |
|---|---|---|
| Cybersecurity Governance | Art. 13 RD 311/2022 + Política de Seguridad | % sistemas con política de seguridad aprobada por máximo órgano directivo[^2][^26] |
| C-SCRM | Art. 19 RD 311/2022 + NIS2 cadena de suministro | % contratos TIC con cláusulas de seguridad y evaluación de proveedores[^18][^46] |
| Risk and Asset Management | Art. 14 + Medida op.exp.1 ENS (inventario activos) | % sistemas categorizados y con análisis de riesgos actualizado[^26][^25] |
| Configuration Management | Medidas técnicas ENS: configuración segura | % equipos con configuración de línea base aplicada y monitorizada[^2] |
| Identity and Access Management | Medida ENS: control de acceso + MFA | % sistemas críticos con MFA y revisión trimestral de accesos[^2][^51] |
| Data Protection and Privacy | LOPDGDD + ENS cifrado en tránsito/reposo | % datos clasificados como sensibles con cifrado verificado[^2][^26] |
| Security Training | Art. 15 y 16 RD 311/2022 + CCN-CERT ANGELES | % personal TIC con formación ENS/ciberseguridad anual completada[^2][^26] |
| Information Security Continuous Monitoring | Art. 24 RD 311/2022 + CCN-CERT SAT | % sistemas de categoría Media/Alta con monitorización 24/7 activa[^2] |
| Incident Response | Art. 25 RD 311/2022 + ITS Notificación CCN-CERT | % incidentes notificados en plazo + tiempo medio de contención[^52][^26] |
| Contingency Planning | Art. 26 RD 311/2022: continuidad de actividad | % sistemas críticos con plan de continuidad probado en el último año[^2][^26] |

***

## 8. El Horizonte Cuántico y la Inteligencia Artificial: Las Métricas del Futuro Inmediato

El Consejo de Seguridad Nacional español reconoció explícitamente en abril de 2025 que la **computación cuántica** y la **inteligencia artificial** representan vectores de transformación del paradigma de amenazas que deben incorporarse a la nueva Estrategia Nacional de Ciberseguridad. En el plano de los indicadores FISMA, el horizonte inmediato apunta hacia:[^41]

- **Post-Quantum Cryptography (PQC)**: el NIST finalizó los primeros estándares PQC en agosto de 2024 (FIPS 203, 204, 205), y la OMB ya ha comenzado a trabajar con las agencias en métricas de inventario y migración criptográfica que previsiblemente se incorporarán como indicadores FISMA en FY2026-2027.
- **IA en la automatización de métricas**: el Subcomité FISMA del CISO Council tiene el mandato de identificar métricas adicionales para automatización, y los modelos de detección basados en IA son el candidato natural para incrementar la cobertura del CDM.[^8]
- **Indicadores de resiliencia operativa digital**: la convergencia entre FISMA, DORA (aplicable en la UE desde enero de 2025) y NIS2 apunta hacia métricas de **resiliencia operativa cuantificable** que van más allá del cumplimiento puntual para medir la capacidad real de absorber y recuperarse de incidentes complejos.[^47]
- **Métricas de riesgo actuarial**: la integración de modelos actuariales de cuantificación del riesgo cibernético —como los promovidos por el Foro de Riesgos Emergentes de ENISA— en los marcos métricos institucionales es una tendencia emergente que coloca a los indicadores FISMA en la frontera entre la gestión de la seguridad y la gestión financiera del riesgo.

***

## 9. Diagnóstico de Brechas y Líneas de Acción para España

### 9.1 Las Cinco Brechas Críticas

El análisis comparativo permite identificar cinco brechas estructurales entre el modelo FISMA FY2025 y la realidad del ecosistema español:

1. **Brecha métrica**: España carece de un sistema equivalente al CyberScope federal con indicadores cuantificados, ponderados y comparables entre administraciones autonómicas. INES ofrece datos de cumplimiento, pero no produce el perfil de madurez multidimensional que genera FISMA.[^25][^2]

2. **Brecha de automatización**: el mandato CDM de FISMA —90% de activos monitorizados automáticamente— no tiene equivalente en el ENS, cuya monitorización continua es un principio pero no un requisito cuantificado. Sólo 41 municipios españoles tienen certificación ENS completa.[^33][^8]

3. **Brecha de gobernanza**: la función *Govern* de FISMA FY2025 mide explícitamente si los órganos de dirección de las agencias ejercen responsabilidad sobre la ciberseguridad. En España, la NIS2 introduce responsabilidad ejecutiva pero la transposición aún no se ha completado.[^36][^2]

4. **Brecha Zero Trust**: FISMA FY2025 incorpora métricas específicas de ZTA; ENS y NIS2 lo contemplan como buena práctica pero sin métricas prescriptivas. Las administraciones autonómicas españolas no disponen de orientación metodológica equivalente al *CISA Zero Trust Maturity Model*.[^2]

5. **Brecha de coordinación territorial**: la colaboración autonómica en ciberseguridad es "voluntaria" y fragmentada, en contraste con el modelo FISMA donde todas las agencias federales reportan al mismo sistema con las mismas métricas bajo supervisión de OMB y CISA.[^34]

### 9.2 Líneas de Acción Estratégica

Del análisis precedente emergen ocho líneas de acción para cerrar las brechas identificadas:

- **Desarrollar un sistema métrico autonómico interoperable** basado en los 10 dominios FISMA adaptados al ENS, con reporte anual normalizado via INES 2.0 y agregación en el futuro CNC.[^25][^5]
- **Establecer un umbral mínimo autonómico de madurez ENS** equivalente al nivel 3 FISMA (Consistently Implemented) como condición de habilitación para la prestación de servicios digitales esenciales.
- **Implementar el modelo CDM adaptado** para al menos el 80% de los sistemas de categoría Media y Alta en CC.AA., aprovechando el presupuesto del Plan Nacional de Ciberseguridad (1.000 millones de euros, más de 150 iniciativas).[^53]
- **Acelerar la transposición NIS2** mediante el Centro Nacional de Ciberseguridad, estableciendo métricas de notificación de incidentes (24/72h) aplicables también a administraciones autonómicas.[^46][^5]
- **Integrar métricas de cadena de suministro** en los pliegos de contratación pública TIC de las CC.AA., alineando con el dominio C-SCRM de FISMA FY2025.[^18][^15]
- **Crear un programa de formación autonómica** en métricas de ciberseguridad equivalente al modelo NIST RMF, aprovechando la plataforma ÁNGELES del CCN y los convenios RETECH con INCIBE.[^40][^39]
- **Adoptar un marco de resiliencia digital autonómica** que incorpore elementos de ZTA, continuidad de negocio y recuperación ante incidentes con indicadores cuantificables y comparables entre territorios.
- **Desarrollar métricas de preparación post-cuántica**: dado el mandato explícito del Consejo de Seguridad Nacional, las CC.AA. deberían iniciar el inventario de sistemas criptográficos vulnerables a ataques cuánticos, anticipando los futuros indicadores FISMA/ENS de migración PQC.[^41]

***

## 10. Conclusión: El Tiempo de las Métricas

Si FISMA FY2025 nos enseña algo —más allá de sus 25 indicadores, sus cinco niveles de madurez y su función Govern recién estrenada—, es que la ciberseguridad sin métricas no es seguridad: es fe. Y en un contexto donde el CCN-CERT ha gestionado un 293% más de incidentes críticos en un solo año, donde INCIBE registra 122.223 incidentes en 2025 y donde España ocupa el quinto puesto europeo en el desgraciado ranking de países más atacados en el primer semestre de ese mismo año, la fe —por muy robusta que sea— resulta insuficiente como activo de ciberseguridad nacional.[^6][^3]

El modelo FISMA FY2025, con toda su complejidad burocrática norteamericana, ofrece a España y a sus comunidades autónomas un espejo útil: no para copiarlo miméticamente —el ENS y el ecosistema NIS2/CCN tienen sus propias virtudes, su propia lógica y su particular encanto mediterráneo—, sino para aprender de su rigor métrico, de su automatización, de su gobernanza corporativa medible y de su obsesión por la mejora continua demostrable. Que el nivel 3 no sea suficiente y que el nivel 5 sea el horizonte, no el techo.

La nueva Estrategia Nacional de Ciberseguridad en elaboración, el Centro Nacional de Ciberseguridad en ciernes, la Estrategia SNS 2025-2028 ya aprobada y los convenios RETECH de INCIBE con las CC.AA. son, precisamente, las primeras piezas de esa arquitectura métrica que España necesita. El trabajo, como el más noble de los softwares, aún está en versión beta. Pero a diferencia de los malos sistemas, al menos tiene ya el diseño arquitectónico aprobado.[^39][^37][^41][^5]

***

*Informe elaborado con base en fuentes oficiales de OMB, DHS/CISA, NIST, CCN-CERT, INCIBE, ENISA, BOE, DSN y auditorías públicas de Inspectores Generales federales publicadas entre enero de 2025 y abril de 2026. Las opiniones analíticas son responsabilidad del consorcio redactor y no representan posición oficial de ningún organismo gubernamental.*

---

## References

1. [[PDF] REDACTED Final FISMA FY 2025 Audit Report_508.docx - DFC](https://www.dfc.gov/sites/default/files/media/documents/fisma_fy_25_audit_report_508_redacted_dfc-25-005-c.pdf) - The FY 2025 IG. Metrics were aligned with the following Cybersecurity Framework function areas: Gove...

2. [[PDF] Federal Trade Commission Office of Inspector General - Oversight.gov](https://www.oversight.gov/sites/default/files/documents/reports/2025-12/Final%20Redacted%20FY25%20FISMA%20Report.pdf) - ... 2025 IG FISMA Reporting ... Govern, includes metrics pertaining to cybersecurity governance and ...

3. [INCIBE detectó más de 122.000 incidentes de ciberseguridad en 2025](https://www.incibe.es/incibe/sala-de-prensa/incibe-detecto-mas-de-122000-incidentes-de-ciberseguridad-en-2025) - INCIBE detectó más de 122.000 incidentes de ciberseguridad en 2025 · Banca: 34% · Transporte: 14% · ...

4. [Anteproyecto de Ley de Coordinación y Gobernanza de la ...](https://www.dsn.gob.es/en/node/24160) - El 14 de enero de 2025 el Consejo de Ministros ha aprobado el anteproyecto de Ley de Coordinación y ...

5. [Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad](https://www.dsn.gob.es/es/actualidad/sala-de-prensa/anteproyecto-ley-coordinacion-gobernanza-ciberseguridad) - El 14 de enero de 2025 el Consejo de Ministros ha aprobado el anteproyecto de Ley de Coordinación y ...

6. [Los incidentes críticos en España por ciberespionaje y cibercrimen ...](https://cadenaser.com/nacional/2025/11/25/los-incidentes-criticos-en-espana-por-ciberespionaje-y-cibercrimen-se-disparan-un-300-cadena-ser/) - España es el quinto país europeo que más se ha visto afectado por los ciberataques en la primera mit...

7. [House lawmakers introduce FISMA modernization legislation](https://fedscoop.com/house-lawmakers-introduce-fisma-modernization-legislation/) - House lawmakers have introduced new legislation that would clarify federal cybersecurity roles, impr...

8. [[PDF] M-25-04 Fiscal Year 2025 Guidance on Federal Information Security ...](https://bidenwhitehouse.archives.gov/wp-content/uploads/2025/01/M-25-04-Fiscal-Year-2025-Guidance-on-Federal-Information-Security-and-Privacy-Management-Requirements.pdf) - Purpose. This memorandum provides agencies with Fiscal Year (FY) 2025 reporting guidance and deadlin...

9. [[PDF] Federal Zero Trust Data Security Guide](https://resources.data.gov/assets/documents/Zero-Trust-DataSecurityGuide_RevisedMay2025_CIO.govVersion.pdf) - Utilizing an existing maturity model, such as CISA's ZTMM,8 provides a way to evaluate the agency's ...

10. [A Guide to the Continuous Diagnostic and Mitigation Program by CISA](https://www.carahsoft.com/blog/carahsoft-continuous-diagnostic-and-mitigation-program-by-cisa-blog-2024) - In CISA's projected budget for 2025, $469.8M will be allotted for the CDM program to strengthen the ...

11. [The Federal Push for Continuous Diagnostics and Mitigation](https://govciomedia.com/the-federal-push-for-continuous-diagnostics-and-mitigation/) - The CDM program is designed to help agencies monitor their IT systems, identify cybersecurity threat...

12. [The Federal CDM Program and OT - Claroty](https://claroty.com/blog/the-federal-cdm-program-and-ot) - One of the Federal programs calling for improvements in OT security in the civilian sector is Contin...

13. [[PDF] FY 2025 Federal Information Security Modernization Act (FISMA ...](https://www.oversight.gov/sites/default/files/documents/reports/2026-02/OIG%20Final%20Report%20FY%202025%20FISMA%20Audit%20(OIG-AR-25-03).pdf) - The FY 2025 Inspector General (IG) FISMA Reporting Metrics required IGs to assess 20 core4 and five ...

14. [[PDF] Evaluation Report - Farm Credit Administration](https://www.fca.gov/template-fca/about/FISMA2025EvaluationPublic.pdf) - The FISMA maturity model summarizes the status of agencies' information security programs on a five-...

15. [[PDF] QCR 2025 STB FISMA.pdf - DOT OIG](https://www.oig.dot.gov/sites/default/files/library-items/QCR%202025%20STB%20FISMA.pdf) - Develop and formalize thresholds or target values for key cybersecurity and risk performance metrics...

16. [What's New in NIST CSF 2.0: The Top 4 Changes | UpGuard](https://www.upguard.com/blog/key-changes-nist-csf-version-2) - Top 4 NIST CSF 2.0 Changes · 1. Revamped respond and recover functions · 2. Introduction of a new(is...

17. [[PDF] The NIST Cybersecurity Framework (CSF) 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf) - The GOVERN. Function provides outcomes to inform what an organization may do to achieve and prioriti...

18. [[PDF] Cybersecurity Supply Chain Risk Management (C-SCRM) - GSA](https://buy.gsa.gov/api/system/files/documents/c-scrm-acquisition-guide-april-2025-508reviewed.pdf) - The FY. 2023/2024 Inspector General (IG) FISMA reporting metrics assess agencies' C-SCRM performance...

19. [[PDF] Independent Auditors' FISMA Audit Report - Fiscal Year 2025.pdf](https://www.gsaig.gov/sites/default/files/audit-reports/Independent%20Auditors'%20FISMA%20Audit%20Report%20-%20Fiscal%20Year%202025.pdf) - Agencies are required to use CyberScope to submit reporting metrics, including the annual IG FISMA M...

20. [[PDF] The FDIC's Information Security Program – 2025 - FDICOIG.gov](https://www.fdicoig.gov/sites/default/files/reports/2025-09/Final%20Report_FISMA%202025%20-%20Public%20Version%20-%20Redacted%20AND%20Sanitized%20for%20Posting.pdf) - FISMA directs federal agencies to report annually to the Office of Management and Budget ... (FISMA)...

21. [OMB Issues Reporting Guidance and Deadlines under FISMA for ...](https://www.fedweek.com/federal-managers-daily-report/omb-issues-reporting-guidance-and-deadlines-under-fisma-for-fiscal-2024/) - OMB has issued (in memo M-24-04) guidance to agencies on reporting requirements and deadlines for fi...

22. [[PDF] Final FY25 CIGIE FISMA Audit Report.pdf](https://www.ignet.gov/sites/default/files/files/Final%20FY25%20CIGIE%20FISMA%20Audit%20Report.pdf) - • OMB Memorandum M-25-04, Fiscal Year 2025 Guidance on Federal Information. Security and Privacy Man...

23. [[PDF] Fiscal Year 2025 FISMA Audit - Oversight.gov](https://www.oversight.gov/sites/default/files/documents/reports/2025-09/FY%202025%20FISMA%20Report%20(OIG-AR-25-09).pdf) - The FY 2025 IG FISMA Reporting Metrics represent a continuation of the work started in FY 2022, when...

24. [ENS vs. NIS2: diferencias y aplicación - Easy Telecom Law](https://www.easytelecomlaw.com/blog/ens-y-nis2-que-son-y-diferencias/) - El ENS y la NIS2 son dos marcos normativos clave en materia de ciberseguridad, pero tienen objetivos...

25. [¿Las entidades privadas deben comunicar el informe INES? - Govertis](https://www.govertis.com/entidades-privadas-deben-comunicar-informe-ines) - INES es la herramienta del CCN para la recogida de información y análisis de indicadores que permite...

26. [BOE-A-2022-7191 Real Decreto 311/2022, de 3 de mayo, por el ...](https://www.boe.es/buscar/doc.php?id=BOE-A-2022-7191) - El CCN y el Instituto Nacional de Administración Pública desarrollarán programas de sensibilización,...

27. [Esquema Nacional de Seguridad (ENS): Guía Completa 2025](https://grupoadaptalia.es/blog/esquema-nacional-de-seguridad-que-es) - Conoce el Esquema Nacional de Seguridad (ENS), el marco regulador en España para garantizar la prote...

28. [Understanding the ENS Framework: A Guide to Spain's National ...](https://graylog.org/post/understanding-the-ens-framework/) - Learn how the ENS Framework protects Spain's public sector systems and how centralized log managemen...

29. [ENS - FAQ - CNI](https://ens.ccn.cni.es/es/que-es-el-ens/faq) - Por su parte, la certificación contra el RD 311/2022, de 3 de mayo, podrá acometerse desde el 1 de d...

30. [ENS - ENS](https://ens.ccn.cni.es/es/) - Para facilitar la toma de decisiones estratégicas, es necesario obtener información del estado de ci...

31. [ENS - Inicio - CNI](https://ens.ccn.cni.es/gl/inicio) - Ir a Métricas e indicadores. Para facilitar a toma de decisións estratéxicas ... Herramientas de Gob...

32. [Guía de Usuario INES CCN-STIC 844 - Scribd](https://es.scribd.com/document/890969152/844-Manual-usuario-INES) - El documento es un manual de usuario para la herramienta INES, desarrollada por el Centro Criptológi...

33. [El 87% de los ayuntamientos utilizan soluciones certificadas con el ...](https://www.aoc.cat/es/blog/2025/el-87-dels-ajuntaments-catalans-utilitzen-solucions-adm-e-amb-certificacio-de-lens/) - La situación a nivel estatal es similar. Sólo unos 41 municipios en España han alcanzado la certific...

34. [[PDF] españa, hub de ciberseguridad europeo - DSN GOB](https://www.dsn.gob.es/sites/default/files/2025-04/ESPA%C3%91A,%20HUB%20DE%20CIBERSEGURIDAD%20EUROPEO.pdf) - A menudo las comunidades autónomas colaboran de forma voluntaria en el ámbito de la ciberseguridad, ...

35. [Top 7 ciberincidentes durante el año 2025 | INCIBE-CERT](https://www.incibe.es/incibe-cert/publicaciones/bitacora-de-seguridad/top-7-ciberincidentes-durante-el-ano-2025) - En el año 2025, se han llevado a cabo algunos de los ataques cibernéticos más importantes y conocido...

36. [Directiva NIS2: Transposición en España y Anteproyecto de Ley](https://blog.isecauditors.com/directiva-nis2-transposicion-en-espana-y-anteproyecto-de-ley) - Estado actual de la transposición de la Directiva NIS2 en España y el Anteproyecto de Ley de Coordin...

37. [Aprobada la Estrategia de Ciberseguridad del Sistema Nacional de ...](https://cetic.es/estrategia-de-ciberseguridad-del-sistema-nacional-de-salud/) - El Consejo Interterritorial del Sistema Nacional de Salud (CISNS) ha aprobado la Estrategia de Ciber...

38. [Aprobada la Estrategia de Ciberseguridad del Sistema Nacional de ...](https://www.cogesasl.com/2025/11/19/aprobada-la-estrategia-de-ciberseguridad-del-sistema-nacional-de-salud/) - Crear una red nacional de colaboración sobre ciberincidentes. · Garantizar la integridad, la confide...

39. [[PDF] convenio de colaboración en el ámbito de la convocatoria retech](https://ciberseguridadegalicia.gal/sites/default/files/media/document/2025-06/convenio_ccaa_incibe.pdf) - ciberseguridad, establece como reto incrementar las capacidades de ciberseguridad en España, fomenta...

40. [Diario Oficial de Extremadura- Formato HTML](https://doe.juntaex.es/otrosFormatos/html.php?xml=2025060210&anio=2025&doe=190o) - INCIBE está comprometido con la generación de conocimiento y el desarrollo actividades destinadas a ...

41. [BOE-A-2025-10371 Orden PJC/522/2025, de 23 de mayo, por la ...](https://www.boe.es/buscar/doc.php?id=BOE-A-2025-10371) - Acuerdo por el que se aprueba el procedimiento para la elaboración de una nueva Estrategia Nacional ...

42. [A 2026 Guide to FISMA Compliance - Concentric AI](https://concentric.ai/a-guide-to-federal-information-security-modernization-act-fisma-compliance-in-2025/) - What Are the Core FISMA Requirements in 2025? · 1. Risk-based information security program · 2. Cate...

43. [Navigating NIS2 2025: How the New EU Cybersecurity Directive ...](https://leaf-it.com/navigating-nis2-2025/) - The NIS2 Directive is a crucial step in strengthening the EU's cybersecurity framework, with expande...

44. [NIS2 Update: What ENISA's New Guidance Means for You!](https://help.drata.com/en/articles/12150854-nis2-update-what-enisa-s-new-guidance-means-for-you) - In June 2025, the European Union Agency for Cybersecurity (ENISA) released new operational guidance ...

45. [EU Cybersecurity ENISA publishes final NIS2 guidance - Bird & Bird](https://www.twobirds.com/en/insights/2025/eu-cybersecurity--enisa-publishes-final-nis2-guidance) - In June 2025, ENISA published the NIS2 technical guidance, which provides detailed advice on mandato...

46. [NIS2 vs ENS: ¿en qué se diferencian? - Factorial](https://factorial.es/blog/nis2-vs-ens/) - NIS2 o ENS? Te explicamos las diferencias clave entre ambas normativas, qué organizaciones deben cum...

47. [NIS2, DORA & FISMA: Cybersecurity Frameworks Explained - Lawrbit](https://www.lawrbit.com/article/navigating-nis2-dora-and-fisma-a-legal-perspective-on-cybersecurity-regulations/) - Unlike DORA or NIS2, FISMA does not prescribe financial penalties. However, federal agencies, third ...

48. [NIS2 en España: normativa de ciberseguridad - SoSafe](https://sosafe-awareness.com/es/blog/nis2-espana-nueva-normativa/) - La NIS2 obliga a las organizaciones a implantar programas estructurados de concienciación y formació...

49. [What is Cyber Supply Chain Risk Management? - UpGuard](https://www.upguard.com/blog/cyber-supply-chain-risk-management) - Cyber supply chain risk management (C-SCRM) is the process of identifying, assessing, and mitigating...

50. [ENISA 2025 NIS Investments Report: Technology Prioritized as ...](https://complexdiscovery.com/enisa-2025-nis-investments-report-technology-prioritized-as-cyber-talent-pools-contract/) - The median cybersecurity budget for European organizations has settled at 1.5 million euros, a figur...

51. [FY 2025 FISMA Metrics Overview | PDF | Security - Scribd](https://www.scribd.com/document/981612804/Fisma-fatima-Razzaq-zainab-Arif) - It discusses core cybersecurity domains, metrics evolution, and the importance of privacy requiremen...

52. [Guía CCN-STIC-817: Gestión Ciberincidentes | PDF - Scribd](https://es.scribd.com/document/436814287/CCN-STIC-817-ENS-Gestion-ciberincidentes) - Este documento proporciona orientación sobre la gestión de ciberincidentes de acuerdo con el Esquema...

53. [Visión Global | España Digital 2026](http://espanadigital.gob.es/vision-global) - Dotado con 1.000 millones de euros, este plan impulsa más de 150 iniciativas para reforzar la cibers...

