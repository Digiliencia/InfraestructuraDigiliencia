
# Informe sobre Business Continuity Management (BCM) y Ciber‑Resiliencia

## Enfoque en indicadores nacionales para España con comparación internacional (≥2024)


***

## 1. Resumen ejecutivo

Desde 2024, la gestión de la continuidad de negocio ha dejado de ser el primo aburrido de la ciberseguridad para convertirse en coprotagonista: reguladores, índices internacionales y estudios académicos convergen en un mensaje incómodo pero claro: **la ciber-resiliencia nacional ya no se mide sólo por “cuántos firewalls tengo”, sino por “cuánto aguanto y cómo me levanto”**.

A grandes rasgos:

- **Convergencia BCM–ciberseguridad–resiliencia operativa.** La literatura reciente y los informes industriales muestran que los programas de BCP/BCM con mayor madurez reducen de forma significativa el tiempo de respuesta, las pérdidas económicas y el downtime tras ciberataques; en un estudio de 2025 sobre entidades financieras, un incremento del 10% en madurez BCP se asocia con caídas de ~17–22% en tiempos de respuesta, pérdidas y tiempo de interrupción tras incidentes ciber.[^1_1]
- **Regulación como motor de métricas.** NIS2 y DORA exigen explícitamente planes de continuidad, pruebas periódicas, objetivos de recuperación y reporting estructurado de incidentes para operadores de servicios esenciales y entidades financieras en la UE. El ENS 2022 en España refuerza controles de “continuidad del servicio” (análisis de impacto, plan de continuidad, pruebas periódicas y medios alternativos).[^1_2][^1_3][^1_4][^1_5][^1_6][^1_7][^1_8]
- **Giro hacia indicadores nacionales de ciber-resiliencia.** El *Global Cybersecurity Index 2024* (ITU) pasa de ranking a sistema por tiers e insiste en que los países integren métricas de ciberseguridad en su planificación nacional. Paralelamente, se proponen marcos de *National Cyber Resilience Index (NCRI)* que combinan gobernanza, capacidades técnicas, capital humano y colaboración, con indicadores como MTTD/MTTR nacionales, % de infraestructuras críticas certificadas, número de profesionales por millón de habitantes, etc..[^1_9][^1_10]
- **España entra en la “primera división” de la ciber‑resiliencia global.**
    - Tier 1 (países “role‑modelling”, score 95–100) en el GCI 2024.[^1_10]
    - 15.ª posición mundial en el *National Cyber Security Index* (89,17 puntos).[^1_11][^1_12]
    - Estrategia Nacional de Ciberseguridad 2019 + Plan Nacional de Ciberseguridad 2022, que anuncia un “sistema nacional integrado de indicadores de ciberseguridad”.[^1_13][^1_14][^1_15]
    - En 2023, el CCN‑CERT gestionó 107.777 incidentes, INCIBE‑CERT 83.517 y el ESDF‑CERT 1.480, según el *Informe Anual de Seguridad Nacional 2023*.[^1_16][^1_17]
- **El hueco: indicadores de continuidad y resiliencia a nivel país.** España mide muy bien “amenazas e incidentes”, pero todavía de forma fragmentaria la **resiliencia funcional**: tiempo medio de recuperación de servicios esenciales, cobertura nacional de planes de continuidad, porcentaje de OSE con ejercicios coordinados, etc. Esto la alinea con la crítica del BIS al sector financiero global: **abundan los indicadores de cumplimiento; escasean los de resiliencia prospectiva**.[^1_18]

Este informe propone:

1. Un mapa de tendencias internacionales en BCM aplicado a ciber-riesgo desde 2024.
2. Una lectura comparativa de los principales índices globales (GCI, NCSI, índices compuestos de “cyber safety”).
3. Un **esquema de indicadores nacionales de BCM/ciber‑resiliencia para España**, coherente con ENCS 2019, ENS 2022, NIS2 y DORA.
4. Un **banco de preguntas de encuesta**, con posibles respuestas en clave amable y ligeramente irónica, orientado a capturar la madurez de continuidad y resiliencia a nivel territorio/sector.

***

## 2. Contexto: de la continuidad corporativa a la resiliencia país

Históricamente, el BCM nació con un foco muy empresarial: incendios, huelgas, desastres naturales. Los ciberataques se veían como un asunto del CISO y su SOC. La evidencia reciente apunta a un cambio claro:

- Una revisión de literatura sobre BCM y ciber‑resiliencia concluye que **BCM y Enterprise Risk Management son componentes críticos de la ciber‑resiliencia** y que la capacidad de responder, recuperarse y evitar crisis depende de marcos integrados, no sólo de controles técnicos.[^1_19]
- Estudios empíricos en el sector financiero prueban que **la madurez en BCP es uno de los determinantes más fuertes de la ciber‑resiliencia**, por encima incluso de cierta automatización basada en IA, cuando se mide en términos de reducción de pérdidas, downtime y tiempos de respuesta.[^1_1]
- El campo de BCM está viviendo una “segunda ola”: análisis bibliométricos recientes destacan como tendencias emergentes la integración con sistemas de gestión (ISO 9001, ISO 27001, ISO 22301), la resiliencia operativa y la gestión de la complejidad y la incertidumbre.[^1_20][^1_21][^1_22][^1_23]

Al trasladar esto al plano nacional, el debate se desplaza de “¿tengo un plan de continuidad por empresa?” a “¿es capaz el país de mantener servicios esenciales y funciones críticas ante ciberincidentes sistémicos, fallos de proveedores cloud, o ataques coordinados a OT?”.

***

## 3. Tendencias globales (≥2024) en BCM para la gestión eficaz del riesgo ciber

### 3.1. Convergencia BCM – ciber‑resiliencia – resiliencia operativa

Los últimos informes de DRI, BCI, WEF y ENISA muestran una convergencia clara:

- El *BCI – A Year in the World of Resilience 2024* indica que la alta dirección toma ya un papel estratégico en continuidad (56,8%), ciber‑resiliencia (55,1%) y resiliencia operativa (48,7%), y que se espera un aumento de inversión en 2025 especialmente en ciber‑resiliencia y resiliencia operativa.[^1_24][^1_25]
- El *Global Cybersecurity Outlook 2024* del WEF subraya que existe una **brecha estructural** en capacidades de ciber‑resiliencia entre organizaciones y países, y que los enfoques deben pasar de la defensa perimetral a la “capacidad de absorber y recuperarse” de incidentes.[^1_26][^1_27]
- El BIS, en *Cyber resilience: Range of practices*, constata que muchos supervisores financieros empiezan a evaluar explícitamente prácticas de continuidad y disponibilidad (BCM, pruebas de fallo, segregación de backups), pero que aún hay pocos **indicadores adelantados de resiliencia** sistemáticamente usados.[^1_18]

**Traducción para métricas:** los indicadores puramente “de seguridad” (nº de vulnerabilidades, % de sistemas parcheados) ya no bastan. Se buscan métricas que conecten:

- **Capacidades** (existencia de BCP, pruebas, backups segregados).
- **Rendimiento** (MTTD, MTTR, cumplimiento de RTO/RPO, tiempo medio de recuperación de servicios críticos).
- **Impacto** (pérdidas económicas, tiempo de interrupción de funciones esenciales, impacto en ciudadanos/empresas).


### 3.2. Regulación como palanca de continuidad y métricas

#### NIS2

NIS2 introduce obligaciones detalladas de gestión de riesgos y continuidad para entidades esenciales e importantes en la UE, incluyendo:

- Gestión de riesgos e incidentes, con registro interno, plazos estrictos de notificación (24 h para aviso inicial, 72 h para informe detallado, 1 mes para informe final).[^1_5][^1_2]
- **Continuidad de negocio:** exigencia de planes de continuidad y recuperación, con definición de funciones críticas, objetivos de recuperación y pruebas periódicas de dichos planes.[^1_28][^1_2][^1_5]
- Cadena de suministro y evaluación sistemática de proveedores críticos, incluyendo su situación de continuidad.[^1_29][^1_2]

Esto empuja a medir, como mínimo, a nivel organización y sector:

- % de servicios esenciales cubiertos por BCP probado.
- Tiempos medios de restauración vs. RTO comprometidos.
- Cobertura de continuidad en proveedores clave.


#### DORA

DORA, plenamente aplicable desde enero de 2025, lleva esta lógica al extremo en el sector financiero europeo:

- Exige un **marco de gestión del riesgo TIC** que cubra clasificación de funciones críticas, inventario de activos y escenarios de disrupción severos.[^1_3][^1_30][^1_31][^1_8]
- Obliga a disponer de **planes de continuidad y de recuperación TIC**, con backups segregados, al menos pruebas anuales y re‑pruebas tras cambios relevantes.[^1_3]
- Refuerza la supervisión de **proveedores TIC críticos (CTPPs)**, que deberán demostrar capacidad de resiliencia y continuidad a nivel europeo.[^1_31][^1_8][^1_3]

**Implicación nacional:** aunque DORA es sectorial, genera datos estructurados sobre BC y resiliencia (ejercicios realizados, resultados de pruebas, tiempos de recuperación, fallos en contingencias) que, agregados, pueden alimentar indicadores país.

#### ENS 2022 y continuidad en el sector público español

El Real Decreto 311/2022, que actualiza el ENS, incorpora explícitamente:

- Requisito de **“continuidad de la actividad”** como uno de los requisitos mínimos de seguridad (art. 11.6.n).[^1_4]
- Obligación de **vigilancia continua** y “evaluación permanente del estado de la seguridad de los activos” para medir su evolución y detectar deficiencias.[^1_4]
- En el desarrollo técnico se especifican controles de **análisis de impacto, plan de continuidad, pruebas periódicas y medios alternativos**.[^1_6][^1_7]

Esto da pie, de facto, a:

- KPIs de cumplimiento ENS en continuidad (porcentaje de sistemas con BIA, BCP, ejercicios anuales, resultados de auditorías).
- Indicadores agregados a nivel administración general del Estado, CCAA, EELL, etc.


### 3.3. Digitalización del BCM: IA, datos y cultura

Tendencias 2024–2025 en BCM destacan:

- Uso creciente de **IA para monitorización de riesgos y escenarios**, integrando feeds de amenazas, clima, conflictos, etc., en motores que alimentan planes de continuidad dinámicos.[^1_32][^1_33][^1_1]
- Extensión de **BCM a cadenas de suministro y entornos OT**, especialmente tras el auge de ataques a infraestructuras críticas y OT reportados por ENISA y otros.[^1_34][^1_35][^1_36]
- Valoración de la **“resiliencia como cultura”**: formar a toda la organización, hacer ejercicios de crisis multidisciplinares y entrenar operaciones en “modo degradado”.[^1_33][^1_32][^1_26]

Desde el punto de vista de indicadores, esto se traduce en:

- Métricas de **cobertura de ejercicios** (nº de simulacros al año, participación por área, cobertura de escenarios ciber, OT, terceros).
- **Indicadores humanos:** porcentaje de personal crítico formado, resultados de ejercicios, tasa de éxito en simulaciones de phishing y crisis.[^1_37][^1_38]
- Integración de métricas de continuidad en cuadros de mando de dirección (nº de días en que el país/sector ha operado en “modo degradado” por incidentes TIC, número de servicios con plan probado de trabajo manual alternativo, etc.).

***

## 4. Índices y marcos internacionales de indicadores nacionales de ciber‑resiliencia

### 4.1. Global Cybersecurity Index 2024 (ITU)

El GCI 2024 mide compromisos nacionales en cinco pilares: legal, técnico, organizativo, desarrollo de capacidades y cooperación. Cambios clave:[^1_10]

- Pasa de ranking a un modelo por **tiers (T1–T5)**. Tier 1 agrupa países con puntuaciones 95–100 y fuerte compromiso transversal.[^1_10]
- Incorpora como indicadores:
    - Existencia de **Estrategia Nacional de Ciberseguridad** con plan de acción e indicadores.[^1_10]
    - Regulación de infraestructuras críticas y capacidad de respuesta (CIRTs/CSIRTs).[^1_10]
    - Campañas de concienciación, formación, currículos, acuerdos internacionales, etc..[^1_10]

**España** está clasificada en **Tier 1 – Role‑modelling** (score 95–100), dentro del grupo de países europeos más avanzados.[^1_10]

### 4.2. National Cyber Security Index (NCSI)

El NCSI, desarrollado por la e‑Governance Academy de Estonia, evalúa capacidades de ciberseguridad nacionales en base a **medidas implementadas**, no incidentes sufridos.[^1_12][^1_39]

- Dimensiones: política de ciberseguridad, lucha contra el crimen, protección de servicios esenciales, educación y cultura de ciberseguridad, ciberdefensa, etc..[^1_11][^1_12]
- Cada indicador evalúa si el país tiene:
    - Estrategia vigente.
    - Marcos de supervisión.
    - Requisitos obligatorios para operadores esenciales y sector público (ISO 27001, ENS, etc.).
    - CSIRT nacional con mandato claro y capacidades, entre otros.[^1_12][^1_11]

**España**:

- Puntación NCSI: **89,17 / 100**, posición **15.ª mundial** (versión 2025 del índice).[^1_11][^1_12]
- Anteriormente, ya se situaba por encima de 88 puntos y 10.ª posición, lo que refleja una posición consolidada.[^1_40]


### 4.3. Índices compuestos de “Cyber Safety / Cyber Resilience”

Informes recientes (ej. *Global Cybercrime Report 2024*) combinan NCSI, GCI, índices de exposición y un *Cyber Resilience Index* propio para generar un “Final Cyber Safety Score” por país.[^1_41][^1_42]

- Países nórdicos y algunos anglosajones (Finlandia, Noruega, Dinamarca, Australia, Reino Unido, Canadá) aparecen como los de menor riesgo, con puntuaciones finales > 88, combinando alta preparación técnica, marco legal robusto y madurez en resiliencia.[^1_42][^1_41]
- Estos índices componen, de forma explícita, las dimensiones que veremos luego en el NCRI académico: **gobernanza, capacidades técnicas, exposición y resiliencia**.[^1_9][^1_41]

Aunque no publican para todos los países todos los sub‑scores, sí orientan:

- Qué **familias de indicadores** se consideran clave a nivel país.
- Dónde se ubica el listón de los “mejores de la clase” que suele interesar a reguladores y estrategas.


### 4.4. Propuestas académicas: National Cyber Resilience Index (NCRI)

Un trabajo académico reciente propone un **NCRI** que va un paso más allá de los índices de ciberseguridad clásicos:[^1_9]

- Dimensiones:
    - **Gobernanza:** nº y calidad de leyes, estrategias, tiempo de respuesta del CERT nacional, % presupuesto público dedicado a ciber.[^1_9]
    - **Capacidades técnicas:** MTTD y MTTR promedio nacional, % de infraestructuras críticas certificadas (ISO 27001, ISO 22301), adopción de estándares y redundancias.[^1_9]
    - **Capital humano:** profesionales certificados por millón de habitantes, programas formativos, campañas de concienciación.[^1_9]
    - **Colaboración:** acuerdos internacionales, asociaciones público‑privadas, ejercicios nacionales de cibercrisis.[^1_9]
- Metodología:
    - Selección de indicadores cuantificables y comparables.
    - Normalización, ponderación transparente y benchmarking frente a índices existentes (GCI, NCSI).
    - Uso de **balanced scorecard** para proporcionar una visión equilibrada.[^1_9]

Lo interesante para España no es tanto el valor absoluto (el índice está en propuesta), sino:

- Que **incluye explícitamente indicadores de rendimiento** (MTTD/MTTR nacionales, frecuencia de ejercicios, etc.) y no sólo de existencia de marcos.
- Que conecta bien con la filosofía ENS (evaluación continua y mejora) y con los requerimientos de NIS2/DORA.

***

## 5. Posición de España en el panorama internacional

### 5.1. Estrategia, planes y marco normativo

- **Estrategia Nacional de Ciberseguridad 2019 (ENCS 2019).**
    - Actualiza la estrategia de 2013 y se alinea con la Estrategia de Seguridad Nacional.[^1_43][^1_44][^1_45]
    - Define como objetivo específico la **seguridad y resiliencia de las redes y sistemas del sector público y servicios esenciales**, y compromete al sistema público a elaborar un informe anual de evaluación del grado de ejecución.[^1_15][^1_13]
    - Incluye la creación de mecanismos e indicadores agregados de riesgo adecuados a las condiciones de ciberseguridad y a la protección de infraestructuras y servicios esenciales.[^1_13]
- **Plan Nacional de Ciberseguridad (PNC) 2022.**
    - Aprobado por el Consejo de Ministros el 29 de marzo de 2022; contempla cerca de 150 iniciativas para tres años.[^1_15]
    - Entre sus líneas se incluye **desarrollar un sistema nacional integrado de indicadores de ciberseguridad**, crear una plataforma nacional de notificación y seguimiento de ciberincidentes y reforzar la ciberseguridad de pymes y autónomos.[^1_14][^1_46]
- **ENS 2022 (RD 311/2022).**
    - Reafirma la necesidad de plena implantación del ENS como medida clave del primer objetivo de la ENCS 2019.[^1_15]
    - Establece principios de “vigilancia continua” y “reevaluación periódica” del estado de la seguridad.[^1_4]
    - Incorpora y detalla requisitos de **continuidad del servicio**: análisis de impacto, planes de continuidad, pruebas y medios alternativos.[^1_7][^1_6][^1_4]
- **Refuerzo normativo 2025.**
    - El anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad para transponer NIS2 crea la figura del **Centro Nacional de Ciberseguridad** y fija un régimen sancionador reforzado.[^1_47]
    - La Orden PJC/448/2025 se presenta como refuerzo del PNC, aprobando nuevas actuaciones en materia de ciberseguridad y aumentando la inversión total hasta alrededor de 1.157 M€.[^1_47]
    - Estrategias sectoriales específicas, como la **Estrategia de Ciberseguridad del SNS 2025‑2028**, incluyen objetivos de garantizar la continuidad asistencial y la disponibilidad de datos sanitarios frente a incidentes, alineados con ENS y NIS2.[^1_47]


### 5.2. Capacidades y resultados medidos

Algunos datos de “salud nacional” de ciber‑resiliencia:

- **Rangos internacionales.**
    - Tier 1 (score 95–100) en el GCI 2024.[^1_10]
    - 15.ª posición en NCSI (89,17 puntos; muy por encima de la media global).[^1_12][^1_11]
- **Gestión de incidentes.**
    - En 2023, el CCN‑CERT gestionó **107.777 ciberincidentes**, INCIBE‑CERT **83.517** y el ESDF‑CERT **1.480**, según el *Informe Anual de Seguridad Nacional 2023*.[^1_17][^1_16]
    - INCIBE detalla que de los 83.517 incidentes: >58.000 afectaron a ciudadanía, >22.000 a empresas, 237 a operadores esenciales y críticos y 1.673 a universidades, salud y otras entidades RedIRIS.[^1_48][^1_49][^1_50][^1_51]
    - Se detectaron 183.077 sistemas vulnerables y más de 7.000 sitios con contenido abusivo; 3 de cada 10 incidentes gestionados fueron fraude online.[^1_49][^1_50][^1_17]
- **Análisis de amenazas y tendencias.**
    - El CCN‑CERT publica anualmente su informe de *Ciberamenazas y Tendencias* (IA‑04/24 para edición 2024), que destaca el papel del ciberespionaje, hacktivismo (especialmente DDoS a administraciones públicas) y cibercrimen tipo ransomware, así como el uso creciente de IA generativa en ataques.[^1_52][^1_53][^1_54][^1_55][^1_56]

Estos datos son oro para construir indicadores nacionales, pero hoy se usan sobre todo en clave descriptiva (volumen, tipo de amenaza, evolución) más que en clave de **objetivos de resiliencia** (p. ej., “reducir el MTTR agregado de incidentes críticos un X % en tres años”).

### 5.3. Lo que falta medir (y que otros países ya empiezan a medir)

Comparando con las propuestas NCRI y con estrategias como las de Estonia o Canadá, se aprecian algunas brechas:[^1_36][^1_57][^1_9]

- Falta un conjunto público y estable de **KPIs nacionales de resiliencia**, más allá de rankings (GCI, NCSI) y volúmenes de incidentes.
- Poca visibilidad de indicadores como:
    - Tiempo medio de recuperación de servicios públicos críticos tras incidentes TIC.
    - Cobertura de BCP/BCM en operadores esenciales y administración (nº y % con planes probados).
    - Frecuencia de ejercicios nacionales de cibercrisis y continuidad multinivel (Estado–CCAA–sector privado) y su evaluación.
- Escasa explotación pública de métricas derivadas de ENS (grado de conformidad en controles de continuidad, nivel de madurez) a nivel agregado.[^1_6][^1_7][^1_4]

En términos futbolísticos: España juega en Champions en ciberseguridad normativa y de capacidades, pero aún no publica la tabla de “kilómetros recorridos, pases completos y recuperación tras gol en contra” a nivel de continuidad nacional.

***

## 6. Propuesta de sistema de indicadores nacionales de BCM y ciber‑resiliencia para España

### 6.1. Principios de diseño

Siguiendo tu línea GQM y la literatura sobre NCRI:[^1_58][^1_19][^1_20][^1_9]

1. **Orientación a objetivos país.**
    - Ejemplo de objetivo estratégico: “Mantener la prestación de servicios esenciales a niveles aceptables ante ciberincidentes graves y fallos de proveedores TIC”.
2. **Capas de indicadores.**
    - Estratégicos (orientados a Gobierno y opinión pública).
    - Tácticos (ministerios, agencias, reguladores sectoriales).
    - Operacionales (CERTs, operadores, administraciones).
3. **Dimensiones MECE.**
    - Gobernanza y marco.
    - Capacidades y preparación.
    - Rendimiento y impacto.
    - Ecosistema y cultura.
4. **Fuentes existentes, no utópicas.**
    - GCI, NCSI, ENS, informes CCN‑CERT, INCIBE, ENS‑auditorías, estadísticas sectoriales (energía, salud, transporte).
5. **Comparabilidad internacional.**
    - Siempre que sea posible, usar indicadores análogos a los de GCI, NCSI, NCRI y marcos BIS/BCBS.[^1_18][^1_12][^1_9][^1_10]

### 6.2. Cuadro sintético de indicadores propuestos

| Dimensión | Indicador nacional sugerido | Fuente principal (potencial) | Notas / comparabilidad |
| :-- | :-- | :-- | :-- |
| Gobernanza | Existencia y vigencia de Estrategia Nacional de Ciberseguridad con plan de acción e indicadores (S/N) | ENCS 2019, PNC[^1_13][^1_15][^1_14] | Alineado con GCI (pilar organizativo)[^1_10] |
| Gobernanza | % de medidas del Plan Nacional de Ciberseguridad ejecutadas o en curso | Seguimiento PNC[^1_15][^1_47] | Indicador de implementación real, no sólo de diseño |
| Gobernanza | Posición y puntuación en GCI y NCSI | ITU GCI, NCSI[^1_10][^1_12][^1_11] | Benchmark externo consolidado |
| Capacidades | Nº de CERT/CSIRT nacionales (gobierno, ciudadanos/empresas, defensa) con mandato operativo definido | CCN‑CERT, INCIBE‑CERT, ESDF‑CERT[^1_16][^1_49] | Se puede extender a CSIRT sectoriales (salud, energía…) |
| Capacidades | % de operadores de servicios esenciales con BCP/BCM alineado con ISO 22301 o equivalente y probado al menos anual | Supervisores sectoriales, transposición NIS2[^1_2][^1_5][^1_59][^1_60] | Refleja cumplimiento de NIS2 y buenas prácticas ISO 22301 |
| Capacidades | % de sistemas de información del sector público con controles ENS de continuidad (BIA, BCP, pruebas, medios alternativos) implantados | Auditorías ENS[^1_4][^1_7][^1_6] | Requiere explotación agregada de datos ENS |
| Rendimiento | Nº de ciberincidentes significativos por 100.000 habitantes y por sector (ciudadanía, empresas, operadores esenciales, sector público) | INCIBE‑CERT, CCN‑CERT, ESDF‑CERT[^1_16][^1_49][^1_50] | Conviene estandarizar definiciones de “significativo” |
| Rendimiento | Tiempo medio nacional de recuperación de servicios esenciales tras incidentes TIC (MTTR agregado estimado) | Informes de operadores esenciales, reguladores, CCN‑CERT[^1_16][^1_49][^1_18] | Puede empezar con recolocación por rangos (≤4h, 4–24h, >24h) |
| Rendimiento | % de incidentes críticos en operadores esenciales que requieren activar planes de continuidad (uso real del BCP) | Operadores esenciales, NIS2[^1_2][^1_5] | Mide uso efectivo de BCM, no sólo su existencia |
| Impacto | Estimación anual de pérdidas económicas directas por ciberincidentes (% del PIB) | IASN, estudios económicos complementarios[^1_16][^1_27] | Puede comenzar con bandas agregadas |
| Impacto | Nº de días/año en los que servicios clave (salud, energía, transporte, administración electrónica) operan en modo degradado por incidentes TIC | Informes sectoriales, BCP[^1_36][^1_47][^1_61] | Indicador potente de resiliencia real, pero exige armonizar reporting |
| Ecosistema | Nº de ejercicios nacionales de cibercrisis y continuidad multi‑actor al año, y % de CCAA/sectores participantes | DSN, CCN, INCIBE, CCAA[^1_43][^1_16][^1_36] | Se puede puntuar por escala (municipal, autonómica, nacional) |
| Ecosistema | Nº de personas formadas en ciberseguridad y continuidad (ciudadanía, pymes, sector público) / 100.000 habitantes | INCIBE, programas de formación[^1_49][^1_48][^1_62] | Indicador ya medido parcialmente (117.000 personas formadas en 2023)[^1_48] |
| Cultura | % de organizaciones del sector público y operadores esenciales que realizan al menos un ejercicio anual de BCP que incluya escenarios ciber | ENS, NIS2, supervisores[^1_2][^1_4][^1_7] | Alineado con BIS/BCBS y DORA[^1_18][^1_3] |

No todo esto es inmediatamente medible hoy, pero buena parte ya se genera —aunque dispersa— en:

- Seguimiento del PNC.
- Auditorías ENS.
- Informes anuales de DSN (IASN).
- Reporting NIS/NIS2 sectorial.
- Memorias de reguladores (CNMV, BdE, DGSFP, CNMC, etc.).

El desafío es más de **gobernanza de datos e integración** que de ausencia de información.

***

## 7. Banco de preguntas de encuesta y respuestas sugeridas (tono ameno, pero útil)

A continuación, se propone un conjunto de bloques temáticos de encuesta pensados para capturar la percepción y madurez de continuidad/ciber‑resiliencia a nivel nacional/territorial (ministerios, CCAA, grandes operadores, etc.). Se sugiere escala tipo Likert de 4–5 niveles, con formulaciones que inviten a la reflexión (y a la sonrisa resignada).

### 7.1. Gobernanza y marco de continuidad

**P1. En su organización, ¿cómo describiría el grado de integración entre la estrategia de ciberseguridad y la de continuidad de negocio?**

- a) “Cada una vive en su universo paralelo; se cruzan sólo en los pasillos (o en los incidentes).”
- b) “Nos coordinamos para las grandes ocasiones (auditorías, regulador, sustos serios).”
- c) “Compartimos objetivos, riesgos y casi las mismas reuniones, pero aún hay silos.”
- d) “Funcionan como un único programa de resiliencia, con gobierno, métricas y reporting comunes.”

**P2. Respecto al cumplimiento de ENS/NIS2/DORA en materia de continuidad, su organización se siente…**

- a) “En fase de lectura atenta del BOE y subrayado intensivo.”
- b) “Hemos hecho el diagnóstico y tenemos una hoja de ruta en marcha.”
- c) “Cumplimos los mínimos y hacemos pruebas puntuales (cuando el calendario lo permite).”
- d) “Tenemos un modelo maduro, con auditorías regulares, métricas y mejora continua.”


### 7.2. Planificación y alcance del BCM

**P3. ¿Qué porcentaje aproximado de sus procesos/servicios críticos están cubiertos por planes de continuidad formales?**

- a) “Menos del 25%: confiamos mucho en la suerte y en el heroísmo del personal.”
- b) “Entre el 25% y el 60%: las joyas de la corona están cubiertas, el resto… en proceso.”
- c) “Entre el 60% y el 90%: casi todo lo que duele tiene un plan, aunque alguno sea vintage.”
- d) “Más del 90%: si algo es crítico, tiene BCP vivo, probado y con dueño claro.”

**P4. En esos planes, ¿hasta qué punto se contemplan escenarios específicos de ciberincidentes (ransomware, DDoS, caída de proveedor cloud, fallo masivo de actualización tipo CrowdStrike)?**

- a) “Están implícitos: ‘si pasa algo de ordenadores, ya se verá’.”
- b) “Tenemos menciones genéricas a ‘incidentes TIC’ sin bajar mucho al detalle.”
- c) “Hay escenarios tipo, pero todavía no cubren bien dependencias OT/proveedores.”
- d) “Los principales escenarios ciber están modelizados, con acciones concretas y roles definidos.”


### 7.3. Ejercicios, pruebas y aprendizaje

**P5. ¿Con qué frecuencia se realizan pruebas o simulacros de los planes de continuidad (incluyendo escenarios ciber) en su organización?**

- a) “Nunca, o sólo cuando la realidad decide organizar su propio simulacro.”
- b) “Esporádicamente (cada 2–3 años) y más por obligación que por convicción.”
- c) “Al menos una vez al año, aunque con alcance limitado.”
- d) “Con una planificación anual estructurada, incluyendo ejercicios conjuntos con otras entidades.”

**P6. Tras ejercicios o incidentes reales, ¿qué ocurre con las lecciones aprendidas?**

- a) “Se comentan en un par de correos y quedan para la posteridad en una carpeta olvidada.”
- b) “Se elabora un informe, pero las acciones correctivas se diluyen con el tiempo.”
- c) “Se genera un plan de acción con responsables y plazos, aunque el seguimiento es irregular.”
- d) “Las lecciones alimentan un registro central, se priorizan y se cierran con seguimiento ejecutivo.”


### 7.4. Métricas y reporting

**P7. ¿Qué tipo de indicadores de continuidad y ciber‑resiliencia se reportan regularmente a la alta dirección?**

- a) “Principalmente indicadores de cumplimiento (nº de políticas, auditorías superadas).”
- b) “Se incluyen algunos KPIs técnicos (MTTD, MTTR, nº de incidentes) sin gran conexión de negocio.”
- c) “Se presentan también métricas de impacto (downtime de servicios, pérdidas estimadas, cumplimiento de RTO).”
- d) “Existe un cuadro de mando de resiliencia que integra riesgos, capacidades, rendimiento e impacto, con objetivos anuales.”

**P8. ¿Cómo describiría la calidad de los datos usados para estos indicadores?**

- a) “Artesanales y con mucho Excel emocional.”
- b) “Aceptables, aunque con lag y alguna inconsistencia entre fuentes.”
- c) “En general fiables, automatizados en buena parte, con validaciones básicas.”
- d) “Automatizados, trazables y auditables; los datos se usan también para analítica avanzada.”


### 7.5. Ecosistema, proveedores y territorio

**P9. Respecto a sus proveedores TIC críticos (incluyendo cloud, telecomunicaciones, OT…), ¿cómo valora su integración en sus propios planes de continuidad?**

- a) “Los contratos dicen algo de ‘soporte 24x7’ y confiamos en su buena voluntad.”
- b) “Se les exige un BCP, pero rara vez se revisa o prueba conjuntamente.”
- c) “Participan en algunos ejercicios y existe intercambio básico de información de resiliencia.”
- d) “Están plenamente integrados: BCP alineados, ejercicios conjuntos y métricas compartidas de continuidad.”

**P10. Desde la perspectiva de país/territorio, ¿hasta qué punto percibe que existe una coordinación efectiva de continuidad y ciber‑resiliencia entre administración, operadores esenciales y sector privado?**

- a) “Cada uno juega su propia liga; nos vemos en los comunicados de prensa tras los incidentes.”
- b) “Hay foros y grupos de trabajo, pero la coordinación operativa aún es limitada.”
- c) “Se realizan ejercicios conjuntos y hay canales de intercambio de información más o menos fluidos.”
- d) “Existe un marco claro de coordinación en crisis, con roles definidos, protocolos y ejercicios regulares multi‑actor.”

Estas preguntas, adaptadas por sector/territorio, permiten derivar **índices de madurez** (por dimensión) que pueden mapearse directamente a los indicadores propuestos en el apartado anterior.

***

## 8. Conclusiones y recomendaciones

1. **La continuidad de negocio se ha convertido en el lenguaje común entre ciberseguridad, negocio y reguladores.** Estudios empíricos, normas ISO 22301/27001/27035 y marcos de resiliencia lo confirman: la madurez BCM correlaciona con mejor desempeño ante ciberincidentes. Ignorar esto a nivel país sería una excentricidad estratégica.[^1_60][^1_63][^1_59][^1_19][^1_1]
2. **España parte de una posición de fuerza, pero con margen de sofisticación en indicadores.** Estar en Tier 1 del GCI y en el top‑20 del NCSI significa que el armazón institucional y normativo es sólido. El reto está en bajar al terreno de:[^1_11][^1_12][^1_10]
    - MTTR de servicios esenciales.
    - Cobertura real de BCP (ENS, NIS2, DORA).
    - Resultados de ejercicios y capacidad de operar en modo degradado.
3. **La ventana de oportunidad es ahora.**
    - La actualización del ENS, la transposición de NIS2, la entrada en vigor de DORA y el refuerzo del Plan Nacional de Ciberseguridad crean el contexto perfecto para formalizar un **Sistema Nacional de Indicadores de Ciber‑Resiliencia y Continuidad**.[^1_14][^1_2][^1_3][^1_47][^1_15][^1_4]
    - Si este sistema se diseña alineado con GCI, NCSI y propuestas NCRI, España puede no sólo medir mejor, sino también **influir en los estándares internacionales**.
4. **Recomendaciones concretas de política y comunidad técnica:**
    - **Consolidar una “Oficina de Datos de Resiliencia Nacional”** bajo el futuro Centro Nacional de Ciberseguridad, con mandato claro de:
        - Definir y mantener el catálogo oficial de indicadores nacionales.
        - Integrar datos de ENS, NIS2, DORA, CERTs y reguladores.
        - Publicar informes periódicos de resiliencia (no sólo de amenazas/incidentes).
    - **Normalizar el reporting de continuidad en operadores esenciales y sector público.**
        - Formularios estándar de incidentes que recojan RTO comprometidos, tiempos reales de restauración, uso de BCP, modo degradado, etc..[^1_2][^1_5][^1_3]
        - Incorporar estos datos en el IASN y en los informes anuales de ENCS/PNC.[^1_16][^1_13][^1_15]
    - **Extender la lógica de ENS a la empresa privada crítica.**
        - Aprovechar la actualización ENS y la futura Ley de Ciberseguridad para alinear controles de continuidad (BIA, BCP, pruebas) con NIS2/DORA, y exigir reportes agregables.[^1_7][^1_2][^1_3][^1_4]
    - **Impulsar ejercicios nacionales de cibercrisis y continuidad multinivel con métricas claras.**
        - Cada ejercicio debería producir KPIs comparables (tiempos de decisión, de notificación, de restauración, calidad de la coordinación) y alimentar el cuadro nacional.[^1_61][^1_36][^1_18]
    - **Convertir el banco de preguntas de encuesta en instrumento de diagnóstico periódico.**
        - Aplicado a CCAA, grandes operadores y ministerios, permitiría seguir la evolución de la madurez de BCM/ciber‑resiliencia con un coste bajo y una riqueza cualitativa alta.[^1_58][^1_9]
5. **Narrativa país: de “ciberseguridad avanzada” a “ciber‑resiliencia demostrable”.**
España ya figura como actor destacado en índices globales. El siguiente paso es poder responder, con datos y no sólo con buenas intenciones, a preguntas como:[^1_27][^1_12][^1_10]
    - “¿Cuánto tarda el país en recuperar sus servicios esenciales tras un ciberincidente grave?”
    - “¿Qué porcentaje de nuestra economía depende de proveedores TIC críticos cuya continuidad hemos probado en serio?”
    - “¿Cuántas veces al año ensayamos, como país, una gran interrupción digital?”

Cuando esas respuestas puedan darse con indicadores claros, series temporales y comparaciones internacionales, la continuidad de negocio habrá dejado de ser un capítulo técnico para convertirse en una **palanca estratégica de soberanía y competitividad digital**. Y, de paso, dormirán todos —CISOs, DPOs, directores de continuidad y responsables públicos— un poco mejor. O al menos con la conciencia más tranquila.
<span style="display:none">[^1_100][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: https://journalwjaets.com/sites/default/files/fulltext_pdf/WJAETS-2025-0102.pdf

[^1_2]: https://n2ws.com/blog/nis2-requirements

[^1_3]: https://www.skadden.com/insights/publications/2024/07/the-eus-digital-operational-resilience-act

[^1_4]: https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191

[^1_5]: https://nis2directive.eu/nis2-requirements/

[^1_6]: https://www.globalsuitesolutions.com/es/ens-2022-novedades-para-empresas-esquema-nacional-seguridad/

[^1_7]: https://www.fontadvocats.com/principales-obligaciones-del-esquema-nacional-de-seguridad-ens-2022/

[^1_8]: https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en

[^1_9]: https://eudoxuspress.com/index.php/pub/article/download/4030/2926/8022

[^1_10]: https://www.itu.int/en/ITU-D/Cybersecurity/Documents/GCIv5/2401416_1b_Global-Cybersecurity-Index-E.pdf

[^1_11]: https://ncsi.ega.ee/country/es/

[^1_12]: https://ncsi.ega.ee/ncsi-index/

[^1_13]: https://www.realinstitutoelcano.org/analisis/la-nueva-estrategia-de-ciberseguridad-de-2019/

[^1_14]: https://aggity.com/estrategia-de-ciberseguridad-para-empresas/

[^1_15]: https://www.boe.es/buscar/doc.php?id=BOE-A-2022-7191

[^1_16]: https://www.dsn.gob.es/sites/default/files/documents/ACCESIBLE MAQUETA IASN2023.pdf

[^1_17]: https://enthec.com/ciberataques-empresas/

[^1_18]: https://www.bis.org/bcbs/publ/d454.pdf

[^1_19]: https://www.scirp.org/pdf/oalibj_2023042015461836.pdf

[^1_20]: https://onlinelibrary.wiley.com/doi/abs/10.1111/1468-5973.12501

[^1_21]: https://discovery.researcher.life/article/business-continuity-management-trends-structures-and-future-issues/345c17b3eba63295a7fe133ec89b7272?page=1

[^1_22]: https://www.econbiz.de/Record/business-continuity-management-trends-structures-and-future-issues-widianti-tri/10015324484

[^1_23]: https://www.cn.aminer.org/pub/6695cb1b01d2a3fbfcc3ef3a

[^1_24]: https://go.riskonnect.com/hubfs/Riskonnect/BCI Sponsored Reports/BCI-A-year-in-The-World-of-Resilience-Report-2024 Final.pdf

[^1_25]: https://drive.drii.org/2024/12/09/10th-annual-global-risk-and-resilience-trends-report/

[^1_26]: https://www.weforum.org/stories/2024/04/cybersecurity-key-strategies-cyber-resilience-2024/

[^1_27]: https://www3.weforum.org/docs/WEF_Global_Cybersecurity_Outlook_2024.pdf

[^1_28]: https://www.keepit.com/blog/nis2-key-to-compliance/

[^1_29]: https://www.infinigate.com/wp-content/uploads/2024/06/Infingate-NIS2-guide.pdf

[^1_30]: https://www.pwc.com/it/it/publications/docs/pwc-digital-operational-resilience-act.pdf

[^1_31]: https://www.digital-operational-resilience-act.com

[^1_32]: https://expressbcp.com/emerging-trends-in-business-continuity-2024/

[^1_33]: https://www.infrascale.com/resolutions-for-resilience-business-continuity-goals-for-2024/

[^1_34]: https://nexusconnect.io/articles/enisa-warns-of-escalating-ot-threats

[^1_35]: https://industrialcyber.co/reports/enisa-report-reveals-surge-in-ddos-and-data-breaches-against-eu-public-administration/

[^1_36]: https://www.enisa.europa.eu/sites/default/files/ncss-map/strategies/reports/EE_NCSS_2024_en.pdf

[^1_37]: https://cycoresecure.com/blogs/10-security-metrics-your-vciso-should-report-to-the-board

[^1_38]: https://www.ncontracts.com/nsight-blog/key-resilience-and-business-continuity-indicators-for-financial-institutions

[^1_39]: https://e-estonia.com/the-national-cyber-security-index-ranks-160-countries-cyber-security-status/

[^1_40]: https://ncsi.ega.ee/country/es_2022/?pdfReport=1

[^1_41]: https://www.mixmode.ai/blog/global-cybercrime-report-2024-which-countries-face-the-highest-risk

[^1_42]: https://betanews.com/article/highest-and-lowest-cyber-risk-countries-revealed/

[^1_43]: https://www.dsn.gob.es/sites/default/files/2025-04/Estrategia Nacional de Ciberseguridad 2019 -  Interactivo_0%20(1)_0.pdf

[^1_44]: https://www.dsn.gob.es/sites/default/files/documents/Estrategia Nacional de Ciberseguridad 2019.pdf

[^1_45]: https://www.acta.es/medios/articulos/internet/150001.pdf

[^1_46]: https://www.dsn.gob.es/sites/default/files/2025-04/ESPAÑA, HUB DE CIBERSEGURIDAD EUROPEO.pdf

[^1_47]: https://www.ismsforum.es/noticias/2486/2025-las-organizaciones-refuerzan-sus-estrategias-de-ciberseguridad-en-el-marco-de-adaptaci-n-a-la-nis2/

[^1_48]: https://elrealce.com/los-incidentes-de-ciberseguridad-de-2023-gestionados-por-incibe-aumentan-en-un-24-respecto-al-ano-anterior/

[^1_49]: https://www.incibe.es/incibe/sala-de-prensa/los-incidentes-de-ciberseguridad-de-2023-gestionados-por-incibe-aumentan-en

[^1_50]: https://www.redseguridad.com/actualidad/ciberseguridad/incibe-supera-los-83-500-ciberincidentes-gestionados-en-2023-un-24-mas-que-el-ano-anterior_20240429.html

[^1_51]: https://www.elradar.es/incibe-balance-ciberseguridad-2023/

[^1_52]: https://www.lksnext.com/es/noticias_boletin/el-ccn-cert-publica-su-informe-de-ciberamenazas-y-tendencias-de-2024/

[^1_53]: https://es.linkedin.com/posts/cuadernosdeseguridad_ccn-informe-ia-0424-ciberamenazas-y-tendencias-activity-7282682931205001216-JWjH

[^1_54]: https://ciberseguridadegalicia.gal/es/actualidad/noticias/el-ccn-cert-publica-la-edicion-de-2024-del-informe-de-ciberamenazas-y

[^1_55]: https://www.administracionpublicadigital.es/tecnologias/2024/12/ciberespionaje-hacktivismo-y-ransomware-las-principales-ciberamenazas-segun-el-ccncert

[^1_56]: https://www.lisanews.org/ciberseguridad/resumen-informe-amenazas-tendencias-cnn-cert/

[^1_57]: https://www.publicsafety.gc.ca/cnt/rsrcs/pblctns/ntnl-cbr-scrt-strtg-2025/index-en.aspx

[^1_58]: https://www.ciat.org/Biblioteca/DocumentosTecnicos/Espanol/2024_Guia_plan_Continuidad_CIAT_GIZ.pdf

[^1_59]: https://isij.eu/system/files/download-count/2024-10/5523_Business_continuity.pdf

[^1_60]: https://www.isms.online/iso-22301/

[^1_61]: https://www.eurofi.net/wp-content/uploads/2024/12/iii.4-cybersecurity-and-digital-operational-resilience.pdf

[^1_62]: https://www.incibe.es/incibe/informacion-corporativa/que-hacemos

[^1_63]: https://ecs.qa/a-complete-guide-to-iso-standards-in-cybersecurity-and-how-they-can-secure-your-business/

[^1_64]: https://www.linkedin.com/pulse/business-continuity-metrics-all-you-need-know-raouf-riahi-mbci

[^1_65]: https://wjarr.com/sites/default/files/WJARR-2023-1166.pdf

[^1_66]: https://www.technavio.com/report/business-continuity-management-solutions-market-industry-analysis

[^1_67]: https://bryghtpath.com/strengthening-business-resilience/

[^1_68]: https://riskonnect.com/business-continuity-resilience/business-resilience-guide-iso-22301-certification/

[^1_69]: https://drive.drii.org/2025/12/01/dri-11th-annual-trends-report/

[^1_70]: https://www.linkedin.com/pulse/implementing-business-continuity-dora-iso-22301-emma-rvd2c

[^1_71]: https://riskimmune.ai/blog/implementing-cybersecurity-operational-risk-integration

[^1_72]: https://www.linkedin.com/pulse/united-states-business-continuity-management-planning-r4soe

[^1_73]: https://racetteconseils.com/en/implementing-cyber-resilience-as-part-of-business-continuity/

[^1_74]: https://www.sciencedirect.com/org/science/article/pii/S146371542400075X

[^1_75]: https://www.bankingsupervision.europa.eu/ecb/pub/pdf/annex/ssm.nl241113_4_annex.en.pdf

[^1_76]: https://www.coyfer.es/en/cyber-resilience-how-to-protect-your-business-continuity-from-cyberattacks/

[^1_77]: https://www.enisa.europa.eu/news/eu-financial-entities-cybersecurity-upgrade-dora-is-now-alive-and-kicking

[^1_78]: https://www.cyber.gov.au/about-us/view-all-content/reports-and-statistics/annual-cyber-threat-report-2023-2024

[^1_79]: https://www.enisa.europa.eu/topics/national-cyber-security-strategies/ncss-map/national-cyber-security-strategies-interactive-map/strategies

[^1_80]: https://aag-it.com/the-latest-cyber-crime-statistics/

[^1_81]: https://morningsidepost.com/articles/2025/11/24/cybersecurity-as-a-macroeconomic-indicator-national-resilience-in-the-digital-age

[^1_82]: https://www.facebook.com/GIS.Mauritius/posts/global-cybersecurity-index-2024-mauritius-ranks-1st-in-africa-and-secures-a-spot/528870953171948/

[^1_83]: https://www.worldcomplianceassociation.com/3164/articulo-cmo-mejorar-la-ciberseguridad-en-espaa-.html

[^1_84]: https://www.ccn-cert.cni.es/publico/dmpublidocuments/EstrategiaNacionalCiberseguridad.pdf

[^1_85]: https://occ.ses.mir.es/publico/occ/dam/jcr:3eb90c21-7e92-4512-ac2a-e93b10889570/Plan Estratégico contra la Cibercriminalidad.pdf

[^1_86]: https://canieti.org/storage/PageBuilderFiles/U8qtgYwLbQbxIuNSDAgwmKmlqtp32e-metaU21DKyAtIENhbmlldGkgLSBFc3RyYXRlZ2lhIENpYmVyc2VndXJpZGFkIC0gMjAyNTExIC0gdjEuMC5wZGY=-.pdf

[^1_87]: https://www.itu.int/en/ITU-D/Cybersecurity/Documents/National_Strategies_Repository/Spain_2013_NCSS_ESen.pdf

[^1_88]: https://www.aesseguridad.es/wp-content/uploads/2020/09/CBS290A.pdf

[^1_89]: https://www.newtral.es/incidentes-incibe/20240429/

[^1_90]: https://dgsfp.mineco.gob.es/es/Publicaciones/DocumentosPublicaciones/V6 Memoria informe del sector 2023.pdf

[^1_91]: https://www.comunidad.madrid/sites/default/files/doc/pe_agencia_ciberseguridad_cmadrid.pdf

[^1_92]: https://www.imarcgroup.com/business-continuity-management-market

[^1_93]: https://www.justice.gc.ca/eng/abt-apd/sd-dd/2023_2024.html

[^1_94]: https://dspd.forte-data.com/d/f63f142d-80d4-11ef-b086-029254d29bb1

[^1_95]: https://reports.weforum.org/docs/WEF_Global_Cybersecurity_Outlook_2025.pdf

[^1_96]: https://openknowledge.worldbank.org/bitstreams/8533db92-a206-4680-be8e-6164248dfbe2/download

[^1_97]: https://commercial.allianz.com/news-and-insights/reports/cyber-risk-trends.html

[^1_98]: https://www.twfire.gov.uk/wp-content/uploads/2025/02/Community-Risk-Management-Plan-2024-27.pdf

[^1_99]: https://www.dc3.mil/Portals/100/Documents/DC3/Missions/DCISE/Cyber Resilience Analysis (CRA)/Cyber Resilience Analysis Self-Assessment User Guide Rev.2-dc3-1.pdf?ver=JyBKuIjLDHlReEZZ8UDVeg%3D%3D

[^1_100]: https://gcscc.ox.ac.uk/sites/default/files/gcscc/documents/media/albania_cmm_report_final_190205.pdf


---