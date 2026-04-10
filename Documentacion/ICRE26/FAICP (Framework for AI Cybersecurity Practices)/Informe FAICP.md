# Informe FAICP 2025–2026: Indicadores y Métricas del Marco de Ciberseguridad para Inteligencia Artificial con Aplicación Territorial en España

> *"El que no mide no mejora, y el que mide sin contexto solo acumula angustia cuantificada."*
> — Paráfrasis libre de la filosofía de la calidad aplicada a la ciberseguridad del siglo XXI.

***

## Resumen Ejecutivo

El término **FAICP** (*Framework for AI Cybersecurity Practices*) designa el ecosistema emergente de marcos, indicadores y métricas que abordan la intersección entre inteligencia artificial y ciberseguridad. Su expresión más canónica y reciente es el **NIST IR 8596 — Cyber AI Profile**, publicado en borrador preliminar el 16 de diciembre de 2025, aunque su horizonte normativo se nutre también del **EU AI Act** (en vigor desde febrero de 2025), la **Directiva NIS2** con su Guía Técnica de ENISA (junio 2025), la norma **ISO/IEC 42001:2023** y el marco adversarial **MITRE ATLAS** (octubre 2025). En España, el ecosistema FAICP se despliega sobre un tejido institucional propio: INCIBE, CCN-CERT, AESIA y el ENS, con un sector de ciberseguridad que en 2024 alcanzó 6.351 millones de euros de facturación y 164.761 empleos.[^1][^2][^3][^4][^5][^6][^7]

Este informe analiza, sin límite de palabras, los indicadores y métricas FAICP publicados desde 2025, su aplicación nacional a España y su proyección territorial por Comunidades Autónomas (CCAA), con comparativa global.

***

## 1. Contexto y Génesis del Marco FAICP

### 1.1. De CSF 1.0 al Cyber AI Profile: Una Genealogía Necesaria

La idea de que la inteligencia artificial introduce una categoría ontológicamente distinta de riesgo cibernético —no meramente cuantitativa sino cualitativa— fue el motor que llevó al NIST a abrir en febrero de 2025 un proceso de consulta pública sobre un perfil CSF específico para IA. La premisa era elegante en su obviedad: los sistemas de IA se comportan de forma *contextual, dinámica, opaca y difícil de predecir*; sus vulnerabilidades pueden ser inherentes al modelo o a los datos de entrenamiento, y sus fallos son más fáciles de inducir que de detectar. No bastaba, pues, con aplicar los controles convencionales; era preciso reimaginar el mapa de indicadores.[^8]

El resultado fue el **NIST IR 8596 (Cyber AI Profile)**, concebido como un *Community Profile* que superpone consideraciones específicas de IA sobre las seis funciones del CSF 2.0 (Gobernar, Identificar, Proteger, Detectar, Responder, Recuperar). Con más de 6.500 partes interesadas contribuyentes —procedentes de gobierno, academia e industria— este borrador constituye el consenso técnico más amplio jamás alcanzado en el campo.[^9][^2][^10][^8]

### 1.2. El Paisaje de Amenazas que Exige el Marco

Los datos de 2025 son, dicho con franqueza académica, alarmantes. Los ciberataques potenciados por IA crecieron un **72% interanual** según análisis basados en el IBM Cost of a Data Breach Report 2025. El **87% de las organizaciones** declara haber sufrido al menos un ataque impulsado por IA en los últimos doce meses. Los incidentes de *deepfake* crecieron un **19% solo en el primer trimestre de 2025**, superando la cifra total de 2024. En Europa, ENISA documentó que el **80% de los ataques de ingeniería social son ya impulsados por IA**. El foro de Davos, con su habitual parsimonia estadística, registró que el **66% de las organizaciones globales espera que la IA sea el factor de mayor impacto en ciberseguridad**, pero solo el **37% dispone de procesos para evaluar la seguridad de herramientas IA antes de desplegarlas** — una brecha que, traducida al español coloquial, equivale a comprar un arma sin saber si el seguro funciona.[^11][^10][^12]

En España, el INCIBE gestionó **122.223 incidentes de ciberseguridad en 2025**, un incremento del **26% respecto a 2024**, con **237.028 sistemas vulnerables relevantes** identificados en todo el territorio. De estos incidentes, **401 afectaron a operadores esenciales** bajo regulación NIS2, siendo banca (34%), transporte (14%) y energía (8%) los sectores más golpeados.[^13][^14]

***

## 2. Arquitectura del Marco FAICP: Los Tres Focos y las Seis Funciones

### 2.1. Los Tres Focus Areas del Cyber AI Profile

El NIST IR 8596 organiza sus recomendaciones en torno a tres vectores conceptuales que se solapan e interalimentan:[^15][^8]

**Focus Area 1 — SECURE (Asegurar):** Gestión de los riesgos de ciberseguridad introducidos al *integrar* sistemas de IA en el ecosistema organizativo. Abarca modelos, datos de entrenamiento, agentes, cadena de suministro de ML e infraestructura de inferencia. La metáfora apropiada: es el marco arquitectónico que decide qué paredes se pueden derribar antes de poner a convivir al inquilino-IA con el resto de la casa.

**Focus Area 2 — DEFEND (Defender):** Identificación de oportunidades para *usar* la IA como acelerador de capacidades defensivas: correlación de alertas, detección de anomalías a velocidad de máquina, análisis de inteligencia de amenazas, gestión autónoma de políticas y reducción del tiempo medio de respuesta (MTTR). El riesgo inherente: la sobredependencia de sistemas defensivos que también pueden ser manipulados.[^8]

**Focus Area 3 — THWART (Contrarrestar):** Construcción de resiliencia frente al uso *adversarial* de la IA: phishing hiperrealista generado por LLM, malware polimórfico que evade detección mediante aprendizaje por refuerzo, ataques de suplantación biométrica con *deepfakes*, explotación automatizada de vulnerabilidades a velocidad no humana.[^4][^8]

La relación entre los tres focos es cíclica: un sistema AI bien asegurado (Secure) potencia las defensas (Defend) y aumenta la capacidad de contrarrestar los ataques adversariales (Thwart), cuyos patrones retroalimentan el modelo de gobernanza de riesgos (Secure).[^8]

### 2.2. Estructura de Indicadores: Prioridades 1-2-3

El Cyber AI Profile introduce un sistema de priorización de subcategorías mediante una escala ordinal de tres niveles, aplicada por función y por Focus Area:[^16][^8]

| Nivel | Etiqueta | Significado Operativo |
|-------|----------|----------------------|
| **1** | Alta | Abordar de forma inmediata; base de la postura defensiva |
| **2** | Moderada | Segunda oleada tras consolidar las de nivel 1 |
| **3** | Fundacional | Buena práctica general; relevante pero no urgente |

Este sistema permite, a diferencia del CSF genérico, que una administración pública o empresa adapte su *perfil objetivo* en función de su posición en el espectro de madurez IA-ciberseguridad, evitando la parálisis que produce un catálogo de controles indiferenciados.[^16]

***

## 3. Indicadores FAICP por Función CSF 2.0: Análisis Detallado

### 3.1. Función GOBERNAR (GV) — El Soporte Constitucional

La función Gobernar fue la gran novedad del CSF 2.0 (febrero 2024) y es el pilar que el Cyber AI Profile eleva al rango de condición necesaria para toda la arquitectura FAICP. Sin gobernanza de IA, el resto del marco es decoración.[^17]

**Indicadores de Alta Prioridad (Nivel 1):**

- **GV.OC-04 — Comunicación de objetivos críticos y limitaciones de la IA:** La organización debe documentar y comunicar activamente qué dependencias introduce la IA en sus servicios críticos y cuáles son sus límites operacionales (alucinaciones, sesgos, ventanas de contexto). Para una CCAA española con servicios de atención ciudadana mediados por IA generativa, este indicador se traduce en: ¿se ha publicado la política de uso de IA en la sede electrónica? ¿Se informan los ciudadanos de cuándo interactúan con un sistema automatizado?[^8]

- **GV.OC-05 — Dependencias de infraestructura IA entendidas:** Mapeo de las interdependencias entre sistemas de IA y la infraestructura de TI subyacente, incluyendo proveedores de nube y cadena de suministro de modelos. La brecha en un proveedor externo de servicios TI que en enero de 2025 expuso información sensible de la Guardia Civil y las Fuerzas Armadas ilustra con precisión quirúrgica qué sucede cuando este indicador permanece en rojo.[^18][^8]

- **GV.RR-04 — Prácticas de RRHH integrando riesgos de IA:** Formación obligatoria del personal en los vectores de ataque específicos de IA (phishing con LLM, deepfakes, ingeniería social aumentada). Los datos del WEF indican que solo el **48% de los líderes empresariales cree que sus empleados entienden cómo los actores maliciosos usan IA**.[^19][^8]

- **GV.SC-07 — Riesgos de terceros en la cadena de suministro IA:** Evaluación continua de proveedores de modelos, datasets, APIs de IA y servicios MLOps. Este indicador se materializa, en el contexto español, en la obligación NIS2 de auditar proveedores críticos.[^20][^8]

**Métricas asociadas (Gobernar):**
- % de políticas de IA revisadas en los últimos 12 meses
- Número de proveedores de IA con evaluación de riesgos activa / total de proveedores activos
- % de empleados con formación certificada en riesgos IA adversariales
- Tiempo medio de actualización de políticas de seguridad IA tras publicación de nueva amenaza

### 3.2. Función IDENTIFICAR (ID) — El Catálogo de lo Desconocido

Identificar es el dominio donde España muestra su mayor fortaleza relativa: el **47% de las organizaciones españolas alcanza nivel maduro en inventario de activos** y el **44% en gestión de vulnerabilidades** según el VI Indicador ISMS Forum 2025. El Cyber AI Profile extiende este mandato a los activos de IA —un universo que las organizaciones apenas han comenzado a catalogar.[^17]

**Indicadores de Alta Prioridad (Nivel 1):**

- **ID.AM-07 — Inventarios de datos y metadatos (proveniencia de datos de entrenamiento):** Equivalente al SBOM (*Software Bill of Materials*) pero para los datos que alimentan los modelos. ¿De dónde proceden? ¿Están contaminados? ¿Pueden ser objeto de envenenamiento retroactivo?. MITRE ATLAS documenta técnicas específicas de reconocimiento para identificar fuentes de datos de entrenamiento como paso previo al ataque.[^7][^8]

- **ID.RA-01 — Vulnerabilidades IA identificadas:** La taxonomía específica incluye: inyección de prompt (*prompt injection*), envenenamiento de datos (*data poisoning*), extracción de modelos, ataques de membresía, ejemplos adversariales, filtraciones durante inferencia. OWASP LLM Top 10 ofrece la referencia más granular para esta subcategoría.[^8]

- **ID.RA-03 — Amenazas IA identificadas:** Reconocimiento de que los actores adversariales *también* utilizan IA para automatizar reconocimiento, escalar ataques y evadir detección. MITRE ATLAS, con 15 tácticas, 66 técnicas y 46 sub-técnicas documentadas a octubre de 2025, proporciona el mapa de referencia.[^21][^8]

- **ID.RA-04 — Impactos y probabilidades de ataques IA evaluados:** Modelos de riesgo cuantitativo que incorporen la velocidad de explotación de la IA adversarial (significativamente superior a la humana) y su capacidad de personalización masiva.[^8]

**Métricas asociadas (Identificar):**
- % de sistemas de IA con inventario completo de componentes (AI-BOM)
- Tiempo medio de detección de vulnerabilidades adversariales en modelos en producción
- Cobertura de la base de datos de amenazas MITRE ATLAS respecto a los vectores IA identificados en el entorno
- Número de incidentes de envenenamiento de datos detectados / periodo

### 3.3. Función PROTEGER (PR) — La Línea de Defensa con Doble Filo

El dominio Proteger muestra en España las señales de alerta más preocupantes: la gestión de identidades y accesos retrocedió desde un 54% en nivel optimizado (2022) hasta el **40% en 2025**; la formación de empleados cayó de 48% a **38% en nivel optimizado**. El Cyber AI Profile añade una capa de complejidad: los sistemas de IA tienen *sus propias identidades*, *sus propias credenciales* y sus propias necesidades de acceso mínimo.[^17]

**Indicadores de Alta Prioridad (Nivel 1):**

- **PR.AA-01 — Identidades y credenciales de sistemas IA gestionadas:** Los agentes autónomos de IA, las APIs de LLM y los sistemas MLOps requieren cuentas de servicio con privilegios mínimos, rotación de credenciales y monitorización de comportamiento anómalo. Un agente de IA con acceso irrestricto a una base de datos ciudadana es, literalmente, un vector de exfiltración disfrazado de asistente virtual.[^8]

- **PR.AA-05 — Acceso a sistemas IA con principio de menor privilegio:** Los modelos de IA no deben tener acceso a recursos que no necesiten para su función. Esto incluye los llamados *sandboxing* de agentes IA, especialmente relevante para sistemas agenticos multi-agente.[^2][^8]

- **PR.AT-01 — Concienciación del personal en amenazas IA:** El 80% de los ataques de ingeniería social en la UE ya son impulsados por IA. La formación debe evolucionar desde reconocer correos sospechosos hacia identificar *deepfakes* de voz, síntesis de vídeo y contenido generado que imite al interlocutor legítimo con fidelidad suficiente para superar controles humanos.[^11]

- **PR.DS-01/10 — Protección de datos de entrenamiento en reposo y en uso:** Incluye medidas anti-envenenamiento (*data poisoning*), cifrado de modelos, redacción de prompts sensibles y prevención de filtraciones durante inferencia.[^8]

- **PR.PS-01 — Gestión de configuración de sistemas IA (incluyendo hiperparámetros):** El versionado de modelos, el rastreo de configuraciones de entrenamiento y el control de cambios en la infraestructura MLOps son la contraparte de la gestión de configuración en IT tradicional. Sin ellos, es imposible reproducir incidentes ni auditar comportamientos.[^8]

**Métricas asociadas (Proteger):**
- % de agentes/sistemas IA con cuentas de servicio dedicadas con menor privilegio
- Tasa de rotación de credenciales en APIs de IA activas
- % de empleados con formación deepfake/GenAI-phishing en últimos 6 meses
- Número de modelos en producción con control de versiones activo / total de modelos

### 3.4. Función DETECTAR (DE) — El Monitor que No Duerme

La detección en entornos con IA exige capacidades que van más allá del SIEM tradicional. El **85% de las empresas utiliza IA para detección de amenazas**, pero solo el **27% ha automatizado completamente** esa detección. El Cyber AI Profile introduce subcategorías específicas que ningún catálogo previo había contemplado de forma sistemática.[^19]

**Indicadores de Alta Prioridad (Nivel 1):**

- **DE.CM-06 — Monitorización de servicios de IA externos:** Las APIs de terceros (OpenAI, Anthropic, servicios de visión por computador) son vectores de exfiltración si no se monitoriza el tráfico de entrada y salida, incluyendo los prompts enviados y las respuestas recibidas. Solo el **40% de los equipos IT puede ver los prompts específicos que los empleados envían a herramientas GenAI**.[^19][^8]

- **DE.CM-09 — Monitorización en tiempo de ejecución de sistemas IA autónomos:** Los agentes de IA multi-paso que operan en producción pueden desviarse de su comportamiento esperado (*model drift*), ser manipulados mediante inyección de prompt indirecta o ejecutar acciones no autorizadas. La detección requiere métricas de comportamiento específicas: distribuciones de salidas, frecuencia de llamadas a herramientas externas, patrones de acceso a datos.[^7][^8]

**Métricas clave (Detectar):**
- Tasa de falsos positivos/negativos en sistemas de detección basados en IA
- Tiempo medio de detección de *model drift* (desviación del comportamiento esperado)
- % de APIs de IA externas con monitorización de tráfico activa
- Número de intentos de *prompt injection* detectados por periodo
- Cobertura de detección MITRE ATLAS respecto a técnicas adversariales documentadas

### 3.5. Función RESPONDER (RS) — La Autopsia del Modelo

Cuando un sistema de IA es comprometido, la respuesta a incidentes adquiere dimensiones que no existían en los playbooks convencionales: ¿el modelo fue envenenado durante el entrenamiento o manipulado en inferencia? ¿Qué outputs comprometidos ya han llegado a usuarios finales? ¿Es el incidente reproducible?

**Indicadores de Alta Prioridad (Nivel 1):**

- **RS.AN-03 — Análisis de causa raíz con trazabilidad de artefactos IA:** El análisis forense de modelos de IA —revisar logs de inferencia, reconstruir el árbol de decisión de un agente, comparar pesos del modelo en producción con la versión entrenada original— es una disciplina emergente que pocos equipos SOC dominan hoy.[^8]

**Métricas asociadas (Responder):**
- Tiempo medio de respuesta a incidentes de tipo IA (MTTR-AI)
- % de incidentes IA con causa raíz documentada (incluyendo artefactos del modelo)
- Tiempo de aislamiento de sistemas IA comprometidos
- Número de playbooks específicos de IA validados / total de vectores cubiertos

### 3.6. Función RECUPERAR (RC) — La Reconstitución del Fideicomiso Algorítmico

La recuperación en contextos IA va más allá de restaurar sistemas: implica verificar la integridad de los modelos, validar que los datos de entrenamiento no fueron comprometidos y reconstruir la confianza de los usuarios en los sistemas automatizados.

**Indicadores de Alta Prioridad (Nivel 1):**

- **RC.RP-02 — Priorización de acciones de recuperación en sistemas IA:** Los sistemas IA con alto impacto en toma de decisiones críticas (diagnóstico médico, gestión de tráfico, adjudicación de ayudas sociales) deben tener planes de recuperación que incluyan rollback de modelos y validación de integridad.[^8]

**Métricas asociadas (Recuperar):**
- Tiempo de recuperación de sistemas IA tras incidente (RTO-AI)
- % de sistemas IA con backups validados de modelos en producción
- Número de pruebas anuales de recuperación de sistemas IA críticos
- Tasa de éxito de verificación de integridad post-incidente (modelo no comprometido)

***

## 4. Métricas Cuantitativas de Referencia: El Estado del Arte Global (2025)

La siguiente tabla sintetiza los indicadores cuantitativos más relevantes de las fuentes primarias auditadas, con valor de referencia comparado:

| Indicador / Métrica | Global (2025) | España (2025) | Fuente |
|---------------------|---------------|---------------|--------|
| Organizaciones con incidente IA en 12 meses | 86–87% | n.d. | [^19][^10] |
| Organizaciones con procesos de evaluación IA pre-despliegue | 37% | n.d. | [^12] |
| Madurez "AI Fortification" nivel Mature (Cisco CRI) | 7% | 7% (estancado) | [^19] |
| Madurez "Network Resilience" nivel Mature | 7% | retroceso | [^19] |
| Ataques de ingeniería social con IA (ENISA) | 80% | incl. en UE | [^11] |
| Incremento de ciberataques IA YoY | +72% | n.d. | [^10] |
| Incidentes gestionados INCIBE 2025 | — | 122.223 (+26%) | [^14] |
| Sistemas vulnerables identificados INCIBE | — | 237.028 | [^14] |
| Organizaciones nivel optimizado (NIST CSF) | — | ~36% proy. 2026 | [^17] |
| Gestión de identidades IA nivel optimizado | — | 40% (↓ desde 54%) | [^17] |
| Formación empleados nivel optimizado | — | 38% (↓ desde 48%) | [^17] |
| Empresas con más de 10 soluciones de seguridad | 70% | incl. en global | [^19] |
| Organizaciones con IA en detección de amenazas | 85% | n.d. | [^19] |
| Solo el **x%** cree que empleados entienden amenazas IA | 48% comprensión | n.d. | [^19] |

***

## 5. Marco Normativo Español: El Ecosistema Institucional FAICP

### 5.1. AESIA — La Primera Centinela de IA en la UE

España es el único Estado miembro de la UE con una autoridad supervisora de IA plenamente operativa: la **Agencia Española de Supervisión de la Inteligencia Artificial (AESIA)**, con sede en A Coruña y en funcionamiento desde junio de 2024. Constituida mediante Real Decreto 729/2023, AESIA gestiona además el primer *sandbox* regulatorio de IA en Europa (RD 817/2023). Este liderazgo institucional sitúa a España en una posición privilegiada para desarrollar indicadores FAICP a nivel nacional.[^22]

El borrador de *Ley para el Buen Uso y la Gobernanza de la Inteligencia Artificial*, sometido a consulta pública hasta el 26 de marzo de 2025, introduciría un régimen sancionador nacional complementario al EU AI Act, con multas de hasta 35 millones de euros para infracciones graves. Las prohibiciones del AI Act (manipulación cognitiva, puntuación social) son aplicables desde **febrero de 2025**; las obligaciones de transparencia para IA de riesgo limitado desde **agosto de 2025**.[^5][^22]

### 5.2. ENS y NIS2 — El Suelo Normativo

El **Esquema Nacional de Seguridad (RD 311/2022)** establece los principios de seguridad aplicables a los sistemas de información de las Administraciones Públicas, incluyendo la vigilancia continua, la gestión de riesgos y la respuesta a incidentes. La integración de los indicadores FAICP en el ENS es el paso natural y urgente que el CCN-CERT aún no ha formalizado en documento público.[^23]

La **Guía Técnica de ENISA sobre NIS2** (junio 2025, 170 páginas) traduce el Reglamento de Ejecución (UE) 2024/2690 en 13 bloques temáticos con ejemplos concretos de indicadores, incluyendo referencias a ISO 27001, CIS Controls y NIST SP 800-53. Esta guía es, de facto, la taxonomía de indicadores NIS2 para los operadores esenciales españoles.[^24][^25]

### 5.3. INCIBE — El Termómetro Nacional

El **Estudio sobre la Industria de la Ciberseguridad en España 2025** (INCIBE + CONETIC) documenta un sector que emplea a **164.761 personas** (25,55% del empleo TIC), con **3.431 empresas especializadas** y una facturación que sitúa a España como **cuarto mercado europeo de ciberseguridad**. Con proyección de crecimiento anual del **14,25% hasta 2029** —cuando se esperan 282.157 empleos—, el ecosistema tiene la masa crítica para implementar el FAICP de forma sistemática.[^1]

***

## 6. Aplicación Territorial en España: Métricas por Comunidades Autónomas

### 6.1. La Brecha de los Datos Territoriales

Con la honestidad intelectual que caracteriza a cualquier investigación rigurosa, cabe señalar que en 2025 **no existe un índice oficial público de madurez en ciberseguridad desagregado por CCAA** en España. Los datos disponibles son nacionales, sectoriales o puntuales. Esta ausencia no es accidental: responde a la fragmentación del modelo de gobernanza de ciberseguridad entre el Estado (INCIBE, CCN-CERT) y los gobiernos autonómicos, que carecen de un mecanismo de reporte estandarizado análogo al NCAF de ENISA para estados miembros.[^26]

Sin embargo, el mosaico de fuentes disponibles permite construir una imagen territorial aproximada que sirva de línea de base para futuros indicadores FAICP por CCAA.

### 6.2. Indicadores Territoriales Disponibles

Los datos con desglose territorial confirmados por fuentes primarias son los siguientes:

**País Vasco / Euskadi:**
- Más de **93.000 dispositivos en riesgo de ciberataque** al cierre de 2024[^27]
- Casi **7.000 empresas en Gipuzkoa** sufrieron un ciberincidente en 2023[^27]
- **>35% de empleo femenino** en ciberseguridad (máximo nacional)[^1]
- Ecosistema propio con **ZIUR** (Centro Vasco de Ciberseguridad Industrial) como referente sectorial OT[^27]

**Castilla y León:**
- Sede del **INCIBE** en León: hub nacional de formación, emprendimiento y respuesta a incidentes[^14][^1]
- Actividad de incubación intensiva: **796 proyectos** impulsados[^1]

**Castilla-La Mancha:**
- Supera el **35% de empleo femenino** en ciberseguridad, junto con Euskadi[^1]

**Madrid y Cataluña:**
- No se identifican datos cuantitativos específicos en fuentes primarias 2025, pero su peso en el total nacional es mayoritario por concentración empresarial y de operadores esenciales

### 6.3. Marco Propuesto para Métricas FAICP Territoriales por CCAA

Dado que los indicadores FAICP aún no tienen despliegue territorial estandarizado, se propone la siguiente arquitectura de métricas aplicables por CCAA, basada en los principios del NIST IR 8596, la Guía NCS 2025 de NN.UU. y el NCAF de ENISA:[^28][^26][^8]

**Indicadores de Capacidad Institucional Territorial (Dimensión Gobernar):**
- Existencia de CERT/CSIRT autonómico o acuerdo formal con INCIBE/CCN-CERT
- Número de organismos de la AAPP autonómica con cumplimiento ENS verificado
- % de sistemas de información de la administración autonómica con categoría ENS Alta/Media/Básica
- Existencia de estrategia autonómica de ciberseguridad con KPIs publicados

**Indicadores de Exposición Territorial (Dimensión Identificar/Detectar):**
- Número de incidentes gestionados por INCIBE con origen en la CCAA / 100.000 habitantes
- Sistemas vulnerables identificados por INCIBE en la CCAA / 1.000 empresas del territorio
- % de operadores esenciales NIS2 radicados en la CCAA con evaluación de riesgos completada
- Número de dominios fraudulentos cerrados con origen en la CCAA / periodo

**Indicadores de Capacidad del Ecosistema (Dimensión Proteger/Recuperar):**
- Número de empresas de ciberseguridad por 100.000 habitantes activos económicamente
- % de pymes con alguna certificación de seguridad (ISO 27001, ENS, SOC2)
- Inversión en ciberseguridad per cápita en el sector público autonómico
- Número de profesionales certificados en ciberseguridad (CISSP, CISM, CISA, CEH) / 100.000 hab.

**Indicadores Específicos FAICP/IA (Dimensión IA-Ciberseguridad):**
- % de organismos autonómicos con política de uso de IA publicada (Art. 13 EU AI Act)[^5]
- Número de sistemas de IA de alto riesgo registrados en la base de datos EU en la CCAA[^29]
- % de proyectos de IA pública con Evaluación de Impacto sobre Derechos Fundamentales (FRIA)[^30]
- Participación en el *sandbox* regulatorio de AESIA (proyectos autonómicos activos)[^22]

### 6.4. Tabla Comparativa de Posicionamiento Territorial Estimado (2025)

La siguiente tabla sintetiza el posicionamiento territorial *estimado* basándose en los indicadores disponibles, con la advertencia explícita de que se trata de una aproximación cualitativa sujeta a revisión cuando se publiquen datos oficiales desagregados:

| CCAA | Fortaleza FAICP Estimada | Factores Diferenciadores |
|------|--------------------------|--------------------------|
| **País Vasco** | Alta | ZIUR, ecosistema OT, >35% empleo fem., 93K dispositivos monitorizados |
| **Castilla y León** | Alta-Media | Sede INCIBE, hub formación, 796 proyectos incubados |
| **Madrid** | Alta | Concentración de sedes corporativas, operadores esenciales, DG INCIBE/CCN |
| **Cataluña** | Alta | Densidad empresarial, CESICAT, ecosistema startups |
| **Castilla-La Mancha** | Media | >35% empleo femenino ciber, crecimiento reciente |
| **Andalucía** | Media | Masa demográfica, baja densidad empresarial ciber proporcional |
| **Comunidad Valenciana** | Media | Ecosistema tecnológico en crecimiento, smart cities |
| **Galicia** | Media-Baja | Sede AESIA en A Coruña: potencial de capitalizar el liderazgo AI nacional |
| **Extremadura, Murcia, Rioja, Navarra, Cantabria, Asturias, Aragón, Baleares, Canarias** | Variable/Baja-Media | Sin datos suficientes en fuentes primarias; INCIBE prioriza estos territorios en INCIBE Emprende[^1] |

***

## 7. Comparativa Mundial: España en el Contexto FAICP Global

### 7.1. Posición de España en Índices de Madurez

El **Cisco Cybersecurity Readiness Index 2025** sitúa a España en el siguiente perfil:[^19]

| Pilar | España 2025 | Global 2025 | Tendencia España |
|-------|-------------|-------------|-----------------|
| Madurez global "Mature" | 19% | 4% | ↑ leve |
| AI Fortification "Mature" | 7% | 7% | → estancado |
| Network Resilience "Mature" | ~7% | 7% | ↓ retroceso |
| Identity Intelligence "Mature" | 3% | 6% | → bajo la media global |
| Cloud Reinforcement "Mature" | 4% | 4% | → estancado |

*Nota: La madurez global española (19%) supera ampliamente la media mundial (4%), lo que refleja la mayor representación de grandes empresas en la muestra española.*

### 7.2. Posición de España en Implementación del EU AI Act

En el contexto europeo, España lidera la implementación del EU AI Act de forma indiscutible:[^22]

| País | Autoridad Competente | Sandbox IA | Ley Nacional IA |
|------|---------------------|------------|-----------------|
| **España** | **OPERATIVA (AESIA)** | **ACTIVO** | En tramitación |
| Alemania | Designada | Planificado | Pendiente |
| Francia | Designada | En desarrollo | Pendiente |
| Italia | Designada | Planificado | Pendiente |

### 7.3. El Paradigma NIST IR 8596 en Perspectiva Comparada

El **NIST IR 8596**  se sitúa como el marco de referencia más completo publicado en 2025 en el espacio FAICP. Su valor añadido frente a los marcos preexistentes:[^2][^8]

| Marco | Origen | Fortaleza | Limitación para FAICP |
|-------|--------|-----------|----------------------|
| **NIST IR 8596** | EE.UU. (dic. 2025) | Mapeo exhaustivo CSF 2.0 + IA, 3 focos, sistema prioridades | Borrador preliminar; aún no en versión final |
| **ISO/IEC 42001:2023** | ISO/IEC | Gestión integral ciclo de vida IA, certificable | Sin mapeo específico de ciberamenazas adversariales |
| **MITRE ATLAS** | MITRE (oct. 2025) | 15 tácticas, 66 técnicas adversariales IA, casos reales | Orientado a threat intelligence, no a gobernanza |
| **ENISA NIS2 Guidance** | UE (jun. 2025) | 13 bloques temáticos, operacionalizable para operadores esenciales | No específico de IA, aunque lo referencia |
| **EU AI Act** | UE (feb. 2025) | Marco regulatorio con obligaciones exigibles y sanciones | Orientado a riesgo de producto IA, no a ciberseguridad operativa |
| **OWASP LLM Top 10** | OWASP | Lista de vulnerabilidades LLM comprensiva, comunidad activa | No contempla amenazas a infraestructura no-LLM |

***

## 8. Tendencias Emergentes 2025-2026: Lo que los Indicadores No Han Capturado Aún

### 8.1. IA Agéntica: El Indicador que Nadie Mide Todavía

Los sistemas de IA agentica —donde múltiples agentes autónomos coordinan acciones, toman decisiones encadenadas y actúan en entornos reales sin intervención humana continua— son el siguiente vector de riesgo no capturado sistemáticamente por los marcos actuales. MITRE ATLAS añadió **14 nuevas técnicas en 2025** específicamente para IA agéntica, cubriendo ataques de inyección de prompt, manipulación de memoria y envenenamiento de contexto. El NIST está desarrollando overlays de control específicos para IA agéntica en el marco COSAiS.[^7][^8]

**Indicadores emergentes:**
- Número de agentes IA autónomos en producción con capacidades de acción externa auditadas
- % de agentes IA con supervisión humana en bucle (*Human-in-the-Loop*) configurada
- Tiempo máximo de acción autónoma permitido sin validación humana
- Número de incidentes de inyección de prompt indirecta detectados en agentes

### 8.2. Criptografía Post-Cuántica: El Horizonte Cifrado

La computación cuántica amenaza la infraestructura criptográfica sobre la que reposa toda la seguridad digital, incluyendo los propios sistemas de IA. El NIST publicó en 2024 los primeros estándares de criptografía post-cuántica (FIPS 203, 204, 205), y su integración en los sistemas de IA —particularmente en el cifrado de modelos y la autenticación de pipelines MLOps— se convierte en un indicador prospectivo crítico.[^8]

**Indicadores prospectivos:**
- % de infraestructura MLOps con protocolos criptográficos resistentes a ataques cuánticos
- Plan de migración post-cuántica documentado para sistemas IA críticos
- Análisis *Harvest Now, Decrypt Later* completado para datos de entrenamiento sensibles

### 8.3. Shadow AI: El Problema que Crece en la Penumbra

El uso no autorizado de herramientas de IA por parte de empleados (*shadow AI*) es uno de los mayores vectores de riesgo no medido sistemáticamente. El **60% de los equipos IT no tiene visibilidad sobre los prompts que los empleados envían a herramientas GenAI**; el **22% de las empresas permite acceso sin restricciones** a herramientas GenAI de acceso público.[^19]

**Indicadores:**
- % de empleados que utilizan herramientas GenAI no autorizadas (medición por auditoría de tráfico)
- Número de políticas de uso aceptable de IA revisadas y comunicadas / periodo
- Incidentes de exfiltración de datos sensibles via herramientas GenAI no supervisadas

***

## 9. Recomendaciones Estratégicas para la Implementación FAICP en España por CCAA

### 9.1. Nivel Nacional — Acciones Estructurales

- **Desarrollar un Perfil ENS específico para sistemas de IA** que incorpore los indicadores del NIST IR 8596 adaptados al contexto regulatorio español (EU AI Act + NIS2 + ENS), análogo al *Community Profile* pero con validez normativa nacional.

- **Establecer un Observatorio FAICP Nacional**, liderado por INCIBE con participación de AESIA y CCN-CERT, que publique métricas anuales por CCAA siguiendo la metodología del VI Indicador ISMS Forum pero con dimensión territorial explícita.[^17]

- **Integrar los indicadores FAICP en el IASN** (*Informe Anual de Seguridad Nacional*), actualmente sin sección específica de IA-ciberseguridad.[^31]

### 9.2. Nivel Autonómico — Propuesta de KPIs SMART para CCAA

Siguiendo las directrices de la NCS Guide 2025 de NN.UU. para KPIs *Específicos, Medibles, Alcanzables, Relevantes y con Tiempo definido*:[^28]

**KPI-01:** % de sistemas de información de la AAPP autonómica con categoría ENS verificada ≥ 80% antes del 31/12/2026.

**KPI-02:** Tiempo medio de notificación de incidentes significativos al CCN-CERT ≤ 24 horas para el 100% de los organismos afectados.

**KPI-03:** % de proyectos de IA en organismos autonómicos con evaluación de riesgos FAICP completada ≥ 60% antes del 31/12/2026.

**KPI-04:** Número de profesionales con formación acreditada en ciberamenazas de IA por CCAA: crecimiento ≥ 25% interanual.

**KPI-05:** % de pymes del territorio con acceso activo al servicio de Alerta Temprana de INCIBE ≥ 50% (media nacional actual: 42%).[^1]

### 9.3. Sectores Críticos con Mayor Brecha en España

Los datos del VI Indicador ISMS Forum y del ENISA Sectorial Threat Landscape confluyen en señalar tres sectores críticos con brecha FAICP especialmente pronunciada en España:[^32][^17]

**Administración Pública:** La media más baja en dominio "Proteger" (solo 4 puntos), al tiempo que es el sector más atacado en la UE (38,2% de incidentes). La paradoja perfecta: el objetivo más golpeado con las defensas más débiles. La implementación del NIST IR 8596 en las AAPP autonómicas debería ser la prioridad territorial número uno.[^32][^17]

**Sanidad:** Peor comprensión de amenazas IA entre todos los sectores (39%), a pesar de manejar datos altamente sensibles y sistemas de apoyo a la decisión clínica que ya incorporan IA. La introducción de IA diagnóstica sin los controles PR.DS-01 y DE.CM-09 activos es, para usar una metáfora médica, como instalar un marcapasos sin revisar las interferencias electromagnéticas.[^19]

**Industria y OT:** El entorno industrial (OT/ICS) combina sistemas legacy con baja madurez de parcheo, protocolos no diseñados para seguridad y adopción creciente de IA para optimización de procesos. El 10% de organizaciones con nivel "inexistente" en mantenimiento de sistemas ICS es un vector de ataque que el Cyber AI Profile aborda específicamente en su Focus Area Thwart.[^27][^17]

***

## 10. Apéndice Metodológico: Concordancias entre Marcos FAICP

La tabla siguiente mapea las correspondencias entre los principales marcos FAICP para facilitar la adopción coordinada en el contexto español:

| NIST IR 8596 | ISO/IEC 42001 | EU AI Act | ENISA NIS2 Guidance | ENS (RD 311/2022) |
|-------------|---------------|-----------|---------------------|-------------------|
| GV.OC-04/05 | Cláusula 6 (Riesgos) | Art. 9 (Risk Mgmt) | Bloque 1 (Política SGSI) | Art. 12 (Política seguridad) |
| ID.AM-07 | Cláusula 8 (Data governance) | Art. 10 (Training data) | Bloque 3 (Gestión activos) | Art. 14 (Gestión riesgos) |
| ID.RA-01/03/04 | Cláusula 8.4 (Evaluación IA) | Art. 9 (Risk assessment) | Bloque 2 (Análisis riesgos) | Art. 14 (Análisis riesgos) |
| PR.AA-01/05 | Cláusula 9.4 (IAM) | Art. 15 (Accuracy/robustness) | Bloque 7 (IAM) | Art. 17 (Control accesos) |
| PR.AT-01/02 | Cláusula 7.3 (Awareness) | Art. 4 (Literacy) | Bloque 9 (Formación) | Art. 16 (Profesionalidad) |
| DE.CM-06/09 | Cláusula 9.1 (Monitoring) | Art. 9/72 (Post-market) | Bloque 5 (Detección) | Art. 24 (Registro/detección) |
| RS.AN-03 | Cláusula 10 (Incidents) | Art. 73 (Serious incidents) | Bloque 6 (Respuesta) | Art. 25 (Incidentes) |
| RC.RP-02 | Cláusula 10.2 (Improvement) | — | Bloque 6 (Recuperación) | Art. 26 (Continuidad) |

***

## Conclusión: El Mapa no es el Territorio, pero sin Mapa no hay Expedición

El marco FAICP —en su expresión más articulada como NIST IR 8596 y su ecosistema normativo asociado— representa el intento más ambicioso y colaborativo jamás realizado para dotar de métricas operacionalizables a la ciberseguridad de la inteligencia artificial. España llega a este desafío con ventajas estructurales innegables: primera autoridad supervisora de IA operativa en la UE, cuarto mercado europeo de ciberseguridad, INCIBE como hub de referencia nacional y una Estrategia de Seguridad Nacional que reconoce la ciberseguridad como pilar estratégico.[^31][^2][^22][^1][^8]

Las brechas son igualmente evidentes: ausencia de métricas territoriales por CCAA, retroceso en dominios críticos de madurez (identidades, formación), un 61% de empresas en nivel "Formativo" según Cisco, y una administración pública que sigue siendo el sector más atacado y peor protegido de la UE.[^32][^17][^19]

El FAICP no es, en último término, un documento técnico ni un conjunto de subcategorías con prioridades asignadas. Es una invitación —educada pero urgente— a que las organizaciones, los reguladores y los territorios se hagan la misma pregunta que los buenos médicos han formulado siempre antes de recetar: ¿sabemos exactamente lo que tenemos? Solo midiendo con rigor y honestidad lo que aún falta, y no solo celebrando lo que ya se ha alcanzado, puede España —y cada una de sus diecisiete realidades autonómicas— construir una postura de ciberseguridad IA que esté a la altura del papel estratégico que el país se ha comprometido a jugar en la era de la inteligencia artificial.

***

*Informe elaborado con datos primarios verificados a abril de 2026. Las métricas territoriales por CCAA constituyen una propuesta metodológica basada en fuentes disponibles; para indicadores oficiales actualizados se recomienda consultar directamente a INCIBE (incibe.es), AESIA (aesia.gob.es) y CCN-CERT (ccn-cert.cni.es).*

---

## References

1. [La ciberseguridad se consolida como motor tecnológico en España ...](http://espanadigital.gob.es/ca/actualidad/la-ciberseguridad-se-consolida-como-motor-tecnologico-en-espana-segun-el-estudio-sobre) - El informe destaca la creación de 403 nuevas compañías en los últimos cinco años, que ya representan...

2. [Draft NIST Guidelines Rethink Cybersecurity for the AI Era](https://www.nist.gov/news-events/news/2025/12/draft-nist-guidelines-rethink-cybersecurity-ai-era) - The Cyber AI Profile centers on three overlapping focus areas: securing AI systems, conducting AI-en...

3. [The new era of responsible AI: how to implement an IMS with ISO ...](https://blog.isecauditors.com/en/implantacion-de-un-sgia-iso-iec-42001-2023) - Implementación del estándar ISO/IEC 42001 para la gestión de IA, garantizando seguridad, ética y tra...

4. [NIST releases draft AI cybersecurity framework profile to guide ...](https://siliconangle.com/2025/12/17/nist-releases-draft-ai-cybersecurity-framework-profile-guide-secure-ai-adoption/) - NIST's preliminary draft Cyber AI Profile can help organizations strategically adopt AI while addres...

5. [European AI Regulation: How to comply with the AI Act in Spain 2025](https://www.mbitschool.com/en/actualidad/reglamento-europeo-de-ia-como-cumplir-el-ai-act-en-espana) - Here's a practical guide, designed for business and technology teams in Spain, to move from theory t...

6. [[PDF] TECHNICAL IMPLEMENTATION GUIDANCE - ENISA](https://www.enisa.europa.eu/sites/default/files/2025-06/ENISA_Technical_implementation_guidance_on_cybersecurity_risk_management_measures_version_1.0.pdf) - The European Union Agency for Cybersecurity, ENISA, is the Union's agency dedicated to achieving a h...

7. [MITRE ATLAS Framework 2026 - Guide to Securing AI Systems](https://www.practical-devsecops.com/mitre-atlas-framework-guide-securing-ai-systems/) - What is the MITRE ATLAS Framework? The MITRE ATLAS (Adversarial Threat Landscape for Artificial-Inte...

8. [NIST Cybersecurity Framework Profile for AI - Libertify.com](https://www.libertify.com/interactive-library/nist-cybersecurity-framework-ai/) - NIST Internal Report NIST IR 8596 iprd. Cybersecurity Framework Profile for. Artificial Intelligence...

9. [What the NIST Cyber AI Profile Draft Tells Us About the Future of AI ...](https://www.keyfactor.com/blog/what-the-nist-cyber-ai-profile-draft-tells-us-about-the-future-of-ai-and-cybersecurity/) - The threat landscape has permanently shifted. AI-driven attackers operate at machine speed, and your...

10. [NIST's New Cyber AI Profile: A Solid Foundation with Critical Gaps ...](https://www.rockcybermusings.com/p/nist-new-cyber-ai-profile-a-solid-foundation) - AI-powered cyberattacks increased 72% year-over-year in 2025, according to AllAboutAI analysis based...

11. [EU Faces Surge in Cyber Threats, Ransomware and AI-Driven Attacks](https://www.linkedin.com/posts/cyble-global_cyber-threats-in-the-eu-escalate-as-diverse-activity-7382413643851874304-Xx2k) - The ENISA Threat Landscape 2025 shows how ransomware, supply chain exploits, and AI-driven phishing ...

12. [Global Cybersecurity Outlook 2025 - The World Economic Forum](https://www.weforum.org/publications/global-cybersecurity-outlook-2025/digest/) - While 66% of organizations expect AI to have the most significant impact on cybersecurity in the yea...

13. [ciberseguridad INCIBE 2025 y directiva NIS2 en España.](https://ibstechnology.com/ciberseguridad-en-las-pymes-espanolas-el-desafio-mas-urgente-de-2026/) - España registró más de 122.000 incidentes de ciberseguridad en 2025, un 26% más que el año anterior....

14. [INCIBE gestionó 122.223 incidentes de ciberseguridad en 2025, un ...](http://espanadigital.gob.es/gl/actualidad/incibe-gestiono-122223-incidentes-de-ciberseguridad-en-2025-un-26-mas-que-el-ano) - INCIBE gestionó 122.223 incidentes de ciberseguridad en 2025, un 26% más que el año anterior · Malwa...

15. [NIST IR 8596: Cybersecurity Framework AI Profile](https://aisecurityandsafety.org/en/frameworks/nist-ir-8596-cyber-ai-profile/) - Maps NIST CSF 2.0 to AI security considerations covering securing AI, AI-enabled defense, and resist...

16. [NIST IR 8596 Appendix D Navigating the Cyber AI Profile - LinkedIn](https://www.linkedin.com/pulse/nist-ir-8596-appendix-d-navigating-cyber-ai-profile-guide-wiseman-5cmnc) - Which CSF 2.0 Subcategories are you adequately addressing today? The Cyber AI Profile prioritizes ou...

17. [[PDF] V Indicador de madurez en ciberseguridad - ISMS Forum Spain](https://www.ismsforum.es/ficheros/descargas/informeobservatorio1763383163.pdf) - En 2025, los resultados reflejan una evolución equilibrada entre la gestión de activos, los procedim...

18. [El mapa de riesgos en ciberseguridad que deja el 2025 - Computing](https://www.computing.es/administracion/el-mapa-de-riesgos-en-ciberseguridad-que-deja-el-2025/) - En el apartado de incidentes, el texto recoge un episodio relevante del sector público español en en...

19. [2025 Cisco Cybersecurity Readiness Index](https://newsroom.cisco.com/c/dam/r/newsroom/en/us/interactive/cybersecurity-readiness-index/2025/documents/2025_Cisco_Cybersecurity_Readiness_Index_ES.pdf)

20. [Navigating NIS2 Compliance: A Deep Dive into ENISA's Technical ...](https://compliancehub.wiki/navigating-nis2-compliance-a-deep-dive-into-enisas-technical-implementation-guidance-for-robust-cybersecurity-risk-management/) - Navigating NIS2 Compliance: A Deep Dive into ENISA's Technical Implementation Guidance for Robust Cy...

21. [Guide to AI Red Teaming with MITRE ATLAS - TheCyberThrone](https://thecyberthrone.in/2026/03/27/guide-to-ai-red-teaming-with-mitre-atlas/) - Why This Piece Had to Come After the Attack Series Over the last five pieces in this series, TheCybe...

22. [EU AI Act Spain Implementation Guide 2025 | AESIA Compliance](https://www.glacis.io/guide-eu-ai-act-spain) - AESIA supervisory agency, Spain’s AI regulatory sandbox, national AI law, and compliance requirement...

23. [BOE-A-2022-7191 Real Decreto 311/2022, de 3 de mayo, por el ...](https://www.boe.es/buscar/doc.php?id=BOE-A-2022-7191) - El CCN articulará la respuesta a los incidentes de seguridad en torno a la estructura denominada CCN...

24. [ENISA UNVEILS NIS2 TECHNICAL GUIDE - LinkedIn](https://www.linkedin.com/pulse/enisa-unveils-nis2-technical-guide-towards-european-mathieu-gitton-7vcje) - The European Union Agency for Cybersecurity has just published, on June 26, 2025, a technical guide ...

25. [NIS2 Update: What ENISA's New Guidance Means for You!](https://help.drata.com/en/articles/12150854-nis2-update-what-enisa-s-new-guidance-means-for-you) - In June 2025, the European Union Agency for Cybersecurity (ENISA) released new operational guidance ...

26. [National Cybersecurity Strategies - ENISA - European Union](https://www.enisa.europa.eu/topics/state-of-cybersecurity-in-the-eu/national-cybersecurity-strategies) - This report presents the work performed by ENISA to build a National Capabilities Assessment Framewo...

27. [Spain recorded more than 97000 cybersecurity incidents in 2024, 32 ...](https://www.ziur.eus/en/-/ziur-at-the-voice-of-industry-in-the-basque-country-conference) - The latest news from the ZIUR Industrial Cybersecurity Center in Gipuzkoa.

28. [[PDF] Guide to Developing a National Cybersecurity Strategy](https://www.un.org/counterterrorism/sites/default/files/2026-01/2025-ncs-guide.pdf) - This third edition sharpens the focus on practical measures to safeguard the national cybersecurity ...

29. [Frequently Asked Questions | AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en/faq)

30. [[PDF] Computers & Security AI algorithms under scrutiny](https://www.aepd.es/documento/1-s2.0-s0167404825003177-main.pdf)

31. [[PDF] INFORME ANUAL DE SEGURIDAD NACIONAL 2024 - DSN GOB](https://www.dsn.gob.es/sites/default/files/2025-05/IASN2024%20ACCESIBLE.pdf) - El Informe Anual de Seguridad Nacional 2024, duodécimo hasta la fecha, tiene como marco de referenci...

32. [[PDF] ENISA SECTORIAL THREAT LANDSCAPE](https://www.enisa.europa.eu/sites/default/files/2025-12/ENISA%20Public%20Administration%20TL%202024%20-%20v1.1.pdf) - Data breaches accounted for 17.4% and data leaks for 1% of collected incidents, with a surge in inci...

