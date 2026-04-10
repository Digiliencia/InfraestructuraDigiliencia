# Indicadores Nacionales CSCRM en España: Marco, Métricas y Tendencias 2025–2026

> *"La ciberseguridad de una entidad es tan fuerte como el eslabón más débil de su cadena de suministro."*  
> — INCIBE, FAQ NIS2

***

## Resumen Ejecutivo

España ha consolidado en 2025 uno de los ecosistemas de gobernanza en ciberseguridad más activos de Europa —segundo país del mundo en centros de ciberseguridad, solo por detrás de Estados Unidos— y, sin embargo, el flanco de la cadena de suministro permanece como la grieta más urgente del sistema. Los ciberataques a la cadena de suministro se duplicaron en 2025 respecto al año anterior, con un coste medio por incidente de 4,33 millones de euros y un impacto agregado global de 53.200 millones de dólares anuales; el 22,5% de todas las brechas de seguridad registradas implicaron a terceros o proveedores, cifra que dobla a la de 2024. Las organizaciones tardan de media 254 días en detectar y contener una brecha originada en la cadena de suministro. El presente informe cartografía, de forma exhaustiva y con orientación territorial para España, el ecosistema de indicadores y métricas del marco CSCRM (*Cyber Supply Chain Risk Management*), articulando los instrumentos normativos nacionales, los estándares técnicos, las iniciativas público-privadas y las tendencias emergentes que marcan la agenda hasta 2026.[^1][^2][^3][^4]

***

## 1. El Paisaje Normativo Nacional: De la Buena Voluntad a la Obligación

### 1.1. El Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad (2025)

El 14 de enero de 2025 el Consejo de Ministros aprobó el Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad, que transpone —con más de quince meses de retraso sobre el plazo europeo de octubre de 2024— la Directiva NIS2 (UE 2022/2555) al ordenamiento jurídico español. Esta norma afecta a más de 5.700 entidades con residencia fiscal o actividad en España en sectores de alta criticidad: energía, transporte, banca, salud, infraestructuras digitales y administración pública. Respecto a la cadena de suministro, la ley impone la **evaluación obligatoria de proveedores** con acceso a sistemas críticos —software, nube, servicios gestionados—, el establecimiento de cláusulas contractuales de ciberseguridad y plazos estrictos de notificación: alerta temprana en 24 horas, notificación detallada en 72 horas y reporte final en un mes. El incumplimiento acarrea multas de hasta 10 millones de euros.[^5][^6][^7][^8][^9][^10]

La Comisión Europea inició en noviembre de 2024 un procedimiento de infracción contra España por el retraso en la transposición. A fecha de abril de 2026 el anteproyecto sigue pendiente de tramitación parlamentaria, aunque ya genera efectos de anticipación en el sector privado.[^9]

### 1.2. El Plan Nacional de Ciberseguridad 2025: Inversión Récord

El 6 de mayo de 2025 el Consejo de Ministros aprobó un paquete de actuaciones dotado con **1.157 millones de euros**, el mayor esfuerzo inversor en ciberseguridad de la historia de España. Del total, 700 millones corresponden al Ministerio de Defensa (CNI-CCN, CESTIC, MCCE), 255 millones al Ministerio para la Transformación Digital (Red.es, SETID) y 189 millones al Ministerio del Interior. Las actuaciones abarcan desde la prevención y detección hasta la respuesta y la recuperación, con especial atención a la resiliencia de las infraestructuras críticas y a la cadena de suministro digital.[^11][^12][^13][^1]

### 1.3. El Esquema Nacional de Seguridad (ENS, RD 311/2022): El Ancla Técnica

El Real Decreto 311/2022 actualiza el ENS e introduce controles explícitos para proveedores y cadena de suministro. Entre sus novedades más relevantes para CSCRM:[^14][^15]

- **Ampliación del ámbito subjetivo**: incluye expresamente a los proveedores tecnológicos del sector público.[^16][^15]
- **Control op.ext**: medidas específicas para servicios externalizados —incluido el entorno *cloud*— con verificación en cadena: los proveedores de primer nivel deben acreditar que sus subcontratistas también cumplen.[^17]
- **Figura del POC** (*Punto/Persona de Contacto*): actor específico en servicios externalizados para analizar y supervisar los requisitos de seguridad.[^18]
- **Auditorías y revisiones de seguridad**: registro de auditorías realizadas a proveedores y recursos externos, documentando hallazgos y acciones correctivas; seguimiento continuo de la seguridad en toda la cadena.[^19]
- **Certificación escalonada** (Básica, Media, Alta): los proveedores cloud de infraestructura crítica deben acreditar el nivel correspondiente; AWS y Azure tienen nivel Alto ENS, Google Cloud tiene nivel Medio en proceso de alta.[^17]

***

## 2. Los Instrumentos de Medición Nacionales: El Arsenal del Analista

### 2.1. El Diccionario IMC de INCIBE-CERT: 46 Métricas para la Ciberresiliencia

El *Diccionario de Indicadores para la Mejora de la Ciberresiliencia* (IMC v2.8, INCIBE-CERT, 2023) constituye el instrumento de medición nacional más completo para organizaciones de sectores críticos e infraestructuras estratégicas. Define **46 métricas** organizadas en cuatro metas —Anticipar, Resistir, Recuperar, Evolucionar— y nueve dominios funcionales (IT y OT). La escala de madurez es uniforme: de **L0** (ausencia total) a **L5** (mejora continua), siendo L5 la medida objetivo en todos los indicadores.[^20][^21]

Aunque el marco no crea un dominio CSCRM independiente, ocho indicadores nucleares abordan directamente la gestión de riesgos en la cadena de suministro:

| Código | Meta / Dominio | Objeto del Indicador (CSCRM) | Pregunta Planteada |
|--------|---------------|------------------------------|--------------------|
| **A-PC-OE5-01** | Anticipar / Política de Ciberseguridad | Acuerdos formales de cooperación/intercambio de información con entidades públicas, privadas, CERT o proveedores | ¿Se ha establecido algún acuerdo formal de ayuda mutua o intercambio de información con otras entidades en ciberresiliencia? |
| **A-GR-OE6-01** | Anticipar / Gestión de Riesgos | Inventario de activos que soportan el servicio esencial, incluyendo activos externos | ¿Existe un inventario de activos actualizado, incluyendo dependencias externas? |
| **A-GR-OG1-03** | Anticipar / Gestión de Riesgos | Procedimiento formal de gestión de riesgos (inventario de activos, amenazas, vulnerabilidades, medidas) | ¿Se han establecido procedimientos para gestionar el riesgo asociado al servicio esencial? |
| **T-SC-OE4-01** | Resistir / Supervisión Continua | Procedimiento acordado en ANS para que proveedores externos reporten eventos de ciberseguridad | ¿Existe procedimiento acordado con proveedores externos para reportar eventos? |
| **R-CS-OE5-02** | Recuperar / Gestión de Continuidad | Identificar y priorizar dependencias externas críticas para la provisión del servicio esencial | ¿Se identifican y priorizan las dependencias externas del servicio esencial? |
| **R-CS-OE6-01** | Recuperar / Gestión de Continuidad | Gestión de riesgos asociados a dependencias externas | ¿Se gestionan los riesgos de las dependencias externas? |
| **R-CS-OE7-04** | Recuperar / Gestión de Continuidad | Acuerdos específicos de ciberresiliencia con terceros implicados en la provisión del servicio esencial (RTO, penalizaciones, requisitos contractuales) | ¿Se han establecido requisitos de ciberresiliencia en acuerdos con terceros? |
| **R-CS-OE8-01** | Recuperar / Gestión de Continuidad | Supervisión y gestión de operaciones de dependencias externas según requisitos acordados | ¿Se supervisan las operaciones de terceros conforme a los requisitos acordados? |

[^21]

Cada métrica incluye: descripción operativa, pregunta planteada, escala L0–L5, método de recogida (entrevista manual), responsable (CSO/CISO), correlación normativa (ENS, ISO 27001:2022, NIST SP 800-53 R5, NIS) y acciones correctivas diferenciadas. El indicador **T-SC-OE4-01** es particularmente revelador: exige que el ANS (*Acuerdo de Nivel de Servicio*) con cada proveedor externo incluya un procedimiento explícito y documentado de reporte de eventos de ciberseguridad —algo que la mayoría de las organizaciones en España todavía incumple a nivel práctico.[^21]

### 2.2. El Cuestionario Unificado CCN-CERT / ISMS Forum Spain (Febrero 2025)

En febrero de 2025, la colaboración entre el **CCN-CERT** (Centro Criptológico Nacional) y **ISMS Forum Spain** produjo el *Modelo de Cuestionario Unificado para el Control de la Cadena de Suministro*, la iniciativa práctica más significativa del ecosistema nacional en materia CSCRM. Su objetivo: estandarizar la *Declaración Responsable* del proveedor, reducir la heterogeneidad de formularios circulantes entre empresas y establecer una base mínima de conocimiento verificable sobre el estado de ciberseguridad de lo contratado.[^22][^23]

El marco normativo de referencia que legitima el cuestionario abarca el ENS (controles op.ext), el RGPD (encargados del tratamiento), DORA, NIS2, CRA e ISO 27001:2022 (apartados 5.19–5.23). El documento propone una **pirámide de mecanismos de supervisión** escalonados por coste y profundidad:[^23]

1. **Compromiso tácito** con especificaciones técnicas del contrato — nivel base, mínimo esfuerzo.
2. **Rating de ciberseguridad** mediante herramientas de monitorización externa del proveedor.
3. **Declaración Responsable** (el cuestionario propiamente dicho) sobre aspectos concretos de ciberseguridad.
4. **Monitorización activa** sobre los sistemas y servicios del proveedor.
5. **Resultados de auditorías externas** presentados por el proveedor.
6. **Auditorías propias o de terceros** del proveedor para el alcance contratado.

[^23]

El Grupo de Trabajo aspira a obtener respaldo institucional formal para convertir este modelo en una buena práctica o incluso en un **modelo obligado de control**, particularmente para sectores regulados por NIS2 y DORA.[^23]

### 2.3. Las Plataformas del CCI: MACIN, RECIN y ESCIM

El **Centro de Ciberseguridad Industrial (CCI)**, con más de 9.000 profesionales en su comunidad, tiene como eje estratégico para 2025–2026 la *ciberresiliencia de la cadena de suministro industrial*. Sus plataformas constituyen instrumentos operativos de medición:[^24]

- **MACIN**: nueva plataforma para evaluar la madurez y ciberresiliencia industrial, orientada al rol ICSO (*Industrial Cybersecurity Officer*).[^24]
- **RECIN**: facilita la incorporación de requisitos de ciberseguridad en proyectos industriales según IEC-62443-3-3 y el *Framework* de NIST, permitiendo generar informes de requisitos por componente del proyecto.[^25]
- **ESCIM**: plataforma de análisis, evaluación y respuesta para entornos OT en la cadena de suministro.[^24]

El *Catálogo Activo* del CCI complementa este ecosistema identificando proveedores de ciberseguridad industrial certificados bajo IEC-62443 y NIST CSF, con filtros por sector, alcance geográfico y certificaciones profesionales.[^25]

***

## 3. Indicadores Cuantitativos del Estado CSCRM en España (2025)

### 3.1. Datos de Situación: El Termómetro Nacional

El *Balance de Ciberseguridad 2025* de INCIBE-CERT ofrece el cuadro de indicadores de referencia para el contexto nacional:[^26][^27]

| Indicador | Valor 2025 | Var. Interanual |
|-----------|-----------|-----------------|
| Incidentes totales gestionados (INCIBE-CERT) | 122.223 | +26% |
| Sistemas vulnerables detectados y notificados | 237.028 | — |
| Incidentes en operadores esenciales e importantes (NIS2) | 401 | — |
| Sector más afectado: Banca | 34% de incidentes esenciales | — |
| Transporte | 14% | — |
| Energía | 8% | — |
| Infraestructuras de mercados financieros | 7% | — |
| Aseguradoras y fondos de pensiones | 6% | — |

[^27][^28][^29][^26]

El malware encabeza la tipología de amenazas con 55.411 casos, incluyendo 392 ataques de ransomware, mientras el fraude online representa 4 de cada 10 incidentes.[^27]

### 3.2. Indicadores de Cadena de Suministro: La Foto Específica

El informe de Cipher/Grupo Prosegur (*Ataques a la cadena de suministro: análisis 2025 y tendencias 2026*, febrero 2026) aporta los indicadores más granulares para el contexto nacional e internacional:[^30][^3]

| Indicador CSCRM | Valor 2025 |
|-----------------|-----------|
| Incremento de ataques a cadena de suministro (interanual) | ×2 (duplicación) |
| Porcentaje de brechas que involucran terceros/proveedores | 22,5% (vs. ~11% en 2024) |
| Coste medio por incidente en cadena de suministro | 4,33 M€ |
| Coste global anual de ataques a cadena de suministro | 53.200 M$ |
| Tiempo medio de detección y contención (cadena de suministro) | 254 días |
| Crecimiento de ataques en sector manufacturero (interanual) | +61% |
| Paquetes maliciosos detectados en repositorios *open source* | 877.522 |

[^2][^3][^4][^31]

La métrica **"254 días de detección"** merece atención especial: multiplica por cuatro el umbral operativo razonable y convierte cualquier brecha en un incidente de impacto sistémico antes de ser identificado. Es, por sí sola, un indicador de madurez CSCRM de primer orden.

### 3.3. Benchmarking Europeo: Dónde se Sitúa España

El informe *NIS Investments 2025* de ENISA (diciembre 2025), basado en una muestra de 1.080 profesionales de organizaciones de la UE, proporciona el marco comparativo europeo:[^32][^33]

| Indicador CSCRM (UE, sectores NIS2) | Valor |
|--------------------------------------|-------|
| Organizaciones que implementan controles de seguridad orientados a proveedores | 90% |
| Organizaciones que citan CSCRM como el área más difícil de cumplir en NIS2 | 37% |
| Organizaciones que señalan ataques a cadena de suministro como principal preocupación futura | 47% |
| Organizaciones con >3 meses para parchear vulnerabilidades críticas | 28% |
| Organizaciones sin ninguna evaluación de seguridad en el último año | 30% |
| Dificultad para atraer talento en ciberseguridad | 76% |
| Dificultad para retener talento en ciberseguridad | 71% |

[^34][^35][^32]

El informe *NIS360* de ENISA (marzo 2025), primera evaluación de madurez sectorial bajo NIS2, aporta un hallazgo crítico: entre el **60% y el 80%** de las entidades evaluadas tienen políticas de CSCRM, pero las directrices para aplicarlas eficazmente son escasas y los esfuerzos de evaluación inconsistentes entre sectores. Los sectores en *zona de riesgo* por menor madurez relativa a su criticidad —ICT, espacio, administración pública, sector marítimo, salud y gas— coinciden con sectores de notable presencia en la cadena de suministro española.[^36][^37][^38]

***

## 4. El Mapa de Indicadores CSCRM: Taxonomía Nacional

### 4.1. Dimensión de Gobernanza (GV.SC)

Siguiendo la estructura del *NIST Cybersecurity Framework 2.0* —el referente conceptual que subyace a todos los marcos nacionales— y adaptándola a la realidad regulatoria española, los indicadores nacionales de gobernanza CSCRM se articulan en torno a cinco ejes:

**GV.SC-E1 — Estrategia y Política de Programa CSCRM**
- *¿Existe una política formal de ciberseguridad en la cadena de suministro, aprobada por la Dirección?* (correlación: IMC A-PC-OG1-01, ENS Artículo 12, ISO 27001:2022 [5.1])
- *¿Se ha integrado el CSCRM en el sistema de gestión de riesgos corporativo (ERM)?* (correlación: ISO 31000:2018, NIS2 Art. 21)
- *¿La alta dirección recibe formación en riesgos de cadena de suministro?* (obligación expresa bajo el anteproyecto de Ley de Coordinación y Gobernanza)[^8]

**GV.SC-E2 — Inventario y Criticidad de Proveedores**
- *¿Existe un inventario actualizado de proveedores TIC con acceso a sistemas críticos, clasificados por criticidad?* (correlación: IMC A-GR-OE6-01, ENS op.ext, ISO 27001:2022 [5.19])
- *¿Se aplica análisis de impacto (BIA) para determinar la criticidad de cada dependencia externa?* (correlación: IMC A-GR-OE1-03)
- *¿Se ha estimado el Tiempo Máximo Tolerable de Interrupción (MTD) para cada proveedor crítico?* (correlación: IMC A-GR-OE1-04, ENS op.cont.1)

**GV.SC-E3 — Requisitos Contractuales de Seguridad**
- *¿Los contratos con proveedores incluyen cláusulas de ciberseguridad exigibles (estándares, ENS, ISO 27001, NIS2)?* (correlación: IMC R-CS-OE7-04, ISO 27001:2022 [5.20][5.21], Anteproyecto Ley)[^8]
- *¿Se requiere certificación ENS o ISO 27001 a proveedores críticos?* (correlación: ENS RD 311/2022, NIS2 Artículo 21)
- *¿Los contratos incluyen el derecho de auditoría sobre el proveedor?* (correlación: ISMS Forum cuestionario unificado)[^23]
- *¿Se exige al proveedor disponer de un SBOM (*Software Bill of Materials*) actualizado?* (correlación: CISA 2025 SBOM Minimum Elements, ENISA SBOM Landscape Analysis dic 2025, Cyber Resilience Act)[^39][^40]

**GV.SC-E4 — Due Diligence y Evaluación Inicial**
- *¿Se realiza una evaluación de ciberseguridad del proveedor antes de formalizar la relación contractual?* (correlación: Cuestionario CCN-CERT/ISMS Forum, ISO 27001:2022 [5.19])[^23]
- *¿Se utilizan herramientas de *rating* o puntuación de ciberseguridad del proveedor?* (correlación: ISMS Forum)[^23]
- *¿Se valoran las vulnerabilidades específicas del proveedor y la calidad de sus prácticas de seguridad?* (correlación: NIS2 Art. 21.2.d, ENISA NIS2 Technical Guidance jun 2025)[^41]

**GV.SC-E5 — Roles y Responsabilidades**
- *¿Existe un responsable (CISO/CSO o POC) que gestiona los riesgos de proveedores?* (correlación: ENS RD 311/2022 figura POC, anteproyecto ley)[^5][^18]
- *¿Se han definido roles y responsabilidades en el plan de respuesta a incidentes con alcance a terceros?* (correlación: IMC R-GI-OE3-01, NIS2)

### 4.2. Dimensión de Identificación y Evaluación de Riesgos

**ID.SC-E1 — Proceso de Gestión de Riesgos de Terceros**
- *¿Existe un procedimiento formal y documentado de gestión de riesgos del proveedor, con revisión periódica?* (correlación: IMC A-GR-OG1-03, ISO 27005:2022, NIST SP 800-161r1)
- *¿Se clasifican y priorizan los riesgos del proveedor según su impacto potencial sobre los servicios esenciales?* (correlación: IMC A-GR-OE5-03, Magerit v3, CCN-STIC 882)
- *¿Se realiza un análisis de riesgo en la cadena de suministro a nivel n-tier (más allá del proveedor directo)?* (correlación: NIST SP 800-161r1, NIS2 Art. 22 — evaluaciones coordinadas de riesgo)

**ID.SC-E2 — Evaluaciones Coordinadas**
- *¿La organización participa en evaluaciones sectoriales coordinadas de riesgos en cadena de suministro?* (correlación: NIS2 Art. 22, Foro Nacional de Ciberseguridad sep 2025, ENISA)[^42][^37]
- *¿Se toman en cuenta los resultados de las evaluaciones coordinadas de ENISA y el Grupo de Cooperación NIS2?* (correlación: ENISA NIS360, NIS2 Art. 22)[^37]

### 4.3. Dimensión de Protección y Controles Técnicos

**PR.SC-E1 — Controles de Seguridad en Proveedores**
- *¿Se verifica que los proveedores aplican los controles técnicos mínimos exigibles (parcheo, MFA, cifrado, segmentación de red)?* (correlación: ENS op.ext, NIS2 Art. 21, ENISA NIS Investments 2025)[^32]
- *¿Se exigen prácticas de desarrollo seguro (*Secure SDLC*) a los proveedores de software?* (correlación: ENISA NIS2 Technical Guidance, Cyber Resilience Act, SBOM)[^39][^41]
- *¿Se implementa Zero Trust en el acceso de proveedores a sistemas críticos?* (correlación: ENS, ENISA, buenas prácticas industriales CCI)[^24]
- *¿Se exige o evalúa la hoja de ruta de criptografía post-cuántica (PQC) a proveedores con datos de larga vida útil?* (correlación: Comunicación CE jun 2025, NIST FIPS 203/204/205, roadmap europeo 2026-2030-2035)[^43][^44][^45][^46]

**PR.SC-E2 — SBOM y Transparencia de Software**
- *¿Se exige un SBOM (Software Bill of Materials) a los proveedores de productos con elementos digitales?* (correlación: CISA 2025 Minimum Elements, ENISA SBOM Landscape Analysis, CRA)[^40][^39]
- *¿Se utiliza el SBOM para la gestión de vulnerabilidades en componentes de terceros?* (correlación: ISO 27001:2022 [8.8], ENISA)[^40]
- *¿Se valora la posibilidad de requerir AIBOM (*AI Bill of Materials*) para proveedores de sistemas IA?* (correlación: ASD/ACSC AI ML Supply Chain Guidance oct 2025, ISO 42001)[^47]

### 4.4. Dimensión de Detección y Supervisión Continua

**DE.SC-E1 — Monitorización de Proveedores**
- *¿Existe monitorización continua del estado de ciberseguridad de los proveedores críticos?* (correlación: IMC T-SC-OE4-01, ISMS Forum)[^23]
- *¿Se establecen alertas ante eventos de seguridad en el entorno del proveedor?* (correlación: IMC T-SC-OG1-03)
- *¿Se utilizan herramientas de *rating* de ciberseguridad o inteligencia de amenazas de terceros?* (correlación: ISMS Forum, ENISA NIS360)[^37][^23]
- *¿Se monitoriza la presencia de software/hardware no autorizado en sistemas que soportan el servicio esencial?* (correlación: IMC T-SC-OE1-02)

**DE.SC-E2 — Métricas de Desempeño del Proveedor**
- *¿Se mide el tiempo medio de respuesta del proveedor ante un incidente de seguridad notificado?* (KPI cuantitativo derivado de ANS)
- *¿Se mide el tiempo de aplicación de parches críticos por parte del proveedor?* (correlación: NIS Investments 2025: 28% de organizaciones tarda >3 meses)[^32]
- *¿Se auditan los resultados de las evaluaciones de seguridad del proveedor con periodicidad definida?* (correlación: ISMS Forum, ISO 27001:2022 [5.22])[^23]

### 4.5. Dimensión de Respuesta y Recuperación

**RS.SC-E1 — Gestión de Incidentes con Terceros**
- *¿El plan de respuesta a incidentes incluye procedimientos específicos para incidentes originados en la cadena de suministro?* (correlación: IMC R-GI-OE1-01, R-GI-OE3-01, NIS2 Art. 23)
- *¿Se ha verificado que los proveedores críticos notifican incidentes en los plazos NIS2 (24h/72h/1 mes)?* (correlación: Anteproyecto Ley, INCIBE FAQ NIS2)[^6][^48][^8]
- *¿Existe comunicación bi-direccional formal con los proveedores en materia de incidentes?* (correlación: IMC T-SC-OE4-01)

**RS.SC-E2 — Continuidad y Recuperación**
- *¿El plan de continuidad de negocio cubre explícitamente la interrupción de servicios de proveedores críticos?* (correlación: IMC R-CS-OE1-01, R-CS-OE3-01)
- *¿Se han probado los planes de continuidad con escenarios de fallo del proveedor?* (correlación: IMC R-CS-OE3-01)
- *¿Se mide el tiempo de recuperación real ante la interrupción de un proveedor crítico (RTO real vs. RTO objetivo)?* (correlación: IMC R-CS-OE1-06, R-CS-OE3-03, R-CS-OE4-04)
- *¿Existen planes de contingencia con proveedores alternativos para los servicios más críticos?* (correlación: IMC R-CS-OE5-02)

***

## 5. Las Tres Fronteras Emergentes: Criptografía Cuántica, IA y Zero Trust

### 5.1. Criptografía Post-Cuántica (PQC) en la Cadena de Suministro

La amenaza "recolecta ahora, descifra después" (*harvest now, decrypt later*) convierte el riesgo cuántico en un problema de cadena de suministro ya presente, no futuro. Los intercambios de datos sensibles con proveedores —contratos, datos de cumplimiento, información de transacciones— utilizan mayoritariamente RSA y curvas elípticas (ECC), algoritmos vulnerables a un ordenador cuántico con capacidad suficiente. Aunque ese umbral no se ha cruzado, los adversarios ya capturan tráfico cifrado para su explotación futura.[^45][^43]

La Comunicación de la Comisión Europea de junio de 2025 establece un **roadmap de transición PQC** con hitos en 2026, 2030 y 2035. Para España, esto se traduce en indicadores CSCRM emergentes:[^44]

- *¿Se dispone de un inventario de dependencias criptográficas (*crypto inventory*) en la cadena de suministro?* (derivado de recomendaciones apexanalytix y SafeCipher PQC Checklist)[^49][^43]
- *¿Se exige a los proveedores críticos una hoja de ruta de migración a PQC (NIST FIPS 203 ML-KEM, FIPS 204 ML-DSA, FIPS 205 SLH-DSA)?*
- *¿Los contratos de renovación incluyen ya requisitos de agilidad criptográfica y divulgación de roadmap PQC?* (correlación: Talan/RiskInsight 2026, apexanalytix)[^46][^43]
- *¿Se ha evaluado cuántos proveedores de la cadena siguen usando algoritmos vulnerables a quantum?* (recomendación directa de apexanalytix)[^43]

El riesgo complementario es el *"Trust Now, Forge Later"*: firmas digitales y certificados hoy fiables podrían falsificarse mañana, permitiendo el despliegue transparente de malware o la alteración de la cadena de suministro sin detección inmediata.[^44]

### 5.2. IA y Aprendizaje Automático: El AIBOM como Indicador Emergente

Los proveedores que integran componentes IA/ML en sus productos introducen vectores de ataque específicos: datos de entrenamiento envenenados, *backdoors* en modelos, dependencias de APIs externas y cadenas MLOps comprometidas. La Agencia de Ciberseguridad australiana (ACSC) publicó en octubre de 2025 la guía *Artificial Intelligence and Machine Learning: Supply Chain Risks and Controls*, que incluye la recomendación de exigir y mantener un **AIBOM** (*AI Bill of Materials*), equivalente al SBOM pero para sistemas de IA.[^50][^47]

Los indicadores CSCRM-IA emergentes para España son:

- *¿Se ha realizado una clasificación de los modelos IA de proveedores por impacto sobre el negocio, sensibilidad de datos y exposición a amenazas?* (correlación: Hodeitek CISO Playbook)[^50]
- *¿Se exige un AIBOM a proveedores que integran componentes IA en servicios o productos contratados?* (correlación: ACSC oct 2025, ISO 42001)[^47]
- *¿Se monitoriza el *drift* y posible alteración post-despliegue de los modelos IA del proveedor?* (correlación: Hodeitek)[^50]
- *¿Se requiere la verificación de la integridad (checksums, firmas digitales) de los artefactos IA entregados por proveedores?* (correlación: ACSC)[^47]

Los KPIs operativos propuestos para CSCRM-IA incluyen: porcentaje de modelos del proveedor con atestaciones válidas, tiempo medio para revocar tokens comprometidos, incidentes de *drift* detectados y resueltos, y porcentaje de conectores con alcance de mínimo privilegio.[^50]

### 5.3. Zero Trust como Indicador de Madurez CSCRM

El principio Zero Trust (*nunca confíes, siempre verifica*) ha dejado de ser una aspiración arquitectónica para convertirse en un indicador de madurez CSCRM de primer orden. El 63% de las organizaciones globales tenían estrategias Zero Trust parcialmente implantadas a mediados de 2024, pero la mayoría cubrían solo una fracción reducida del entorno. El sector de manufactura, de fuerte presencia en la cadena de suministro española, registró un incremento del 61% en ataques en 2025, lo que sitúa la adopción de Zero Trust OT como una urgencia nacional.[^51][^2]

Indicadores Zero Trust aplicados a CSCRM:

- *¿Se aplica acceso de mínimo privilegio a todos los proveedores con acceso remoto a sistemas críticos?* (correlación: ENS, NIST SP 800-161r1, Zero Trust Architecture NIST SP 800-207)
- *¿Se segmenta la red para aislar los sistemas accedidos por proveedores externos?* (correlación: IEC 62443, ENS, CCI RECIN)[^25]
- *¿Se verifica la identidad del proveedor en cada sesión de acceso (autenticación multifactor, certificados)?*
- *¿Se audita y registra toda la actividad de los proveedores en los sistemas de la organización?*

***

## 6. El Foro Nacional de Ciberseguridad: Propuestas para una Gobernanza CSCRM Nacional

El informe del **Foro Nacional de Ciberseguridad** de septiembre de 2025, *"Análisis y propuestas relativas a la seguridad de la cadena de suministro"*, identifica los grandes retos estructurales del ecosistema español:[^42]

- **Inviabilidad de la supervisión total**: en ecosistemas con cientos de subcontratistas, la auditoría individual es inviable por coste y capacidad técnica.
- **Ausencia de certificación universal**: coexisten ISO 27001, PCI-DSS, HIPAA, ENS y otros esquemas sectoriales, sin visión global.
- **Regulación fragmentada**: cada sector define sus propias reglas, generando dispersión normativa y dificultando la adopción homogénea.

Las propuestas formuladas tienen implicaciones directas en el diseño de indicadores nacionales:

| Propuesta del Foro | Indicador Derivado |
|--------------------|-------------------|
| Establecer medidas mínimas obligatorias de CSCRM | Tasa de entidades con programa CSCRM formal sobre total reguladas |
| Gobernanza compartida público-privada | Número de acuerdos de intercambio de información (ISACs) activos por sector |
| Mecanismo de certificación armonizado | Porcentaje de proveedores certificados (ENS, ISO 27001) del total del inventario |
| Evaluaciones coordinadas de riesgo por sector | Frecuencia y cobertura de evaluaciones sectoriales coordinadas (NIS2 Art. 22) |
| Marco regulatorio armonizado | Índice de convergencia normativa (superposición ENS/NIS2/DORA/CRA por sector) |

[^42]

La Estrategia Nacional de Ciberseguridad (medida 8 de la línea de acción 2) involucra al sector público y privado en la gestión de riesgos de la cadena de suministro, especialmente en aquellos que afectan a servicios esenciales. El proceso para una nueva Estrategia Nacional de Ciberseguridad 2025–2030 fue abierto mediante Orden PJC/522/2025 de mayo de 2025.[^11][^42]

***

## 7. Cuadro de Mando CSCRM Nacional: Propuesta de Indicadores Sintéticos para España

La siguiente propuesta integra los instrumentos nacionales existentes (IMC-INCIBE, ENS, cuestionario CCN-CERT/ISMS Forum, Foro Nacional de Ciberseguridad) con las tendencias emergentes (PQC, AIBOM, Zero Trust) en un cuadro de mando sintético de 20 indicadores de uso territorial, aplicable a nivel de sector o de entidad supervisada:

### Bloque A — Gobernanza y Programa

| ID | Indicador | Umbral de Referencia | Fuente Normativa |
|----|-----------|---------------------|-----------------|
| CSCRM-A1 | % de entidades con política CSCRM formal aprobada por la Dirección | ≥80% | IMC A-PC-OG1-01, ISO 27001 5.19 |
| CSCRM-A2 | % de entidades con inventario de proveedores TIC críticos actualizado | ≥90% | IMC A-GR-OE6-01, ENS op.ext |
| CSCRM-A3 | % de proveedores críticos con evaluación de seguridad inicial documentada | ≥70% | Cuestionario CCN-CERT/ISMS Forum[^23] |
| CSCRM-A4 | % de contratos con proveedores críticos que incluyen cláusulas de ciberseguridad exigibles | ≥85% | IMC R-CS-OE7-04, NIS2 Art. 21, ENS |
| CSCRM-A5 | % de entidades con responsable formal de CSCRM (CISO/CSO/POC) designado | ≥95% | ENS RD 311/2022, Anteproyecto Ley[^5] |

### Bloque B — Evaluación y Riesgo

| ID | Indicador | Umbral de Referencia | Fuente Normativa |
|----|-----------|---------------------|-----------------|
| CSCRM-B1 | % de proveedores clasificados por nivel de criticidad (alta/media/baja) | 100% | IMC A-GR-OE1-03, NIS2 Art. 21.2.d |
| CSCRM-B2 | Tiempo máximo tolerable de interrupción (MTD) estimado para proveedores críticos | Documentado y revisado anualmente | IMC A-GR-OE1-04 |
| CSCRM-B3 | % de entidades que realizan análisis de riesgo n-tier (más allá del proveedor directo) | ≥40% | NIST SP 800-161r1, Foro Nacional[^42] |
| CSCRM-B4 | % de entidades que exigen SBOM a proveedores de software | ≥30% (tendencia) | CISA 2025[^39], ENISA[^40], CRA |
| CSCRM-B5 | % de proveedores críticos con evaluación de madurez criptográfica (PQC readiness) | ≥20% (tendencia 2026) | Roadmap CE PQC[^44], NIST FIPS 203-205 |

### Bloque C — Supervisión y Monitorización

| ID | Indicador | Umbral de Referencia | Fuente Normativa |
|----|-----------|---------------------|-----------------|
| CSCRM-C1 | % de proveedores críticos con ANS que incluye obligación de reporte de incidentes | ≥90% | IMC T-SC-OE4-01, NIS2 Art. 21 |
| CSCRM-C2 | % de proveedores monitorizados continuamente con herramientas de *rating* | ≥50% | ISMS Forum[^23], ENISA Good Practices |
| CSCRM-C3 | Tiempo medio de parcheado de vulnerabilidades críticas en proveedores (días) | <30 días | ENISA NIS Investments 2025[^32] |
| CSCRM-C4 | % de proveedores que disponen de resultados de auditoría de seguridad en los últimos 12 meses | ≥60% | ISMS Forum[^23], ISO 27001:2022 5.22 |
| CSCRM-C5 | Frecuencia de revisión del inventario de proveedores | Al menos anual | ENS, NIST SP 800-161r1 |

### Bloque D — Respuesta, Recuperación y Resiliencia

| ID | Indicador | Umbral de Referencia | Fuente Normativa |
|----|-----------|---------------------|-----------------|
| CSCRM-D1 | % de planes de respuesta a incidentes que cubren explícitamente la cadena de suministro | ≥75% | IMC R-GI-OE3-01, NIS2 Art. 23 |
| CSCRM-D2 | Tiempo medio de detección de brechas originadas en la cadena de suministro (días) | <60 días (ref. actual: 254)[^4] | Cipher/Prosegur 2026 |
| CSCRM-D3 | % de planes de continuidad probados con escenarios de fallo de proveedor crítico | ≥50% | IMC R-CS-OE3-01 |
| CSCRM-D4 | % de entidades con proveedor alternativo identificado para servicios esenciales críticos | ≥70% | IMC R-CS-OE5-02, BIA |
| CSCRM-D5 | % de entidades participantes en mecanismos de intercambio de información CSCRM sectorial | ≥30% | IMC A-PC-OE5-01, NIS2 Art. 29 |

***

## 8. Brechas, Paradojas y el Horizonte 2026

### 8.1. La Paradoja del Cumplimiento

El dato europeo más desconcertante de 2025 es también el más elocuente: el **90% de las organizaciones NIS2 declara implementar controles de seguridad orientados a proveedores**, pero el **37% señala el CSCRM como el área más difícil de cumplir en NIS2**. La brecha entre la existencia formal de controles y su eficacia operativa es la auténtica grieta del sistema. España no es ajena a esta paradoja: el Foro Nacional de Ciberseguridad la diagnostica con precisión en su informe de septiembre de 2025.[^34][^42][^32]

### 8.2. La Brecha de Transposición

La ausencia de una Ley de Coordinación y Gobernanza de la Ciberseguridad en vigor —a abril de 2026 el anteproyecto sigue en tramitación parlamentaria— genera una incertidumbre jurídica que desincentiva la inversión en CSCRM por parte de las organizaciones afectadas. La Comisión Europea ya ha iniciado procedimiento de infracción contra España. El coste de este retraso no es abstracto: mientras no existe obligación legal explícita de notificación de incidentes en cadena de suministro, muchos eventos permanecen sin reportar al INCIBE-CERT o al CCN-CERT.[^9]

### 8.3. La Emergencia de los Modelos de IA como Vector

La integración masiva de componentes IA en proveedores de servicios digitales crea una superficie de ataque sin indicadores de medición establecidos en el ecosistema español. La ausencia del AIBOM como requisito contractual y la falta de métricas de *drift* o integridad de modelos representa la siguiente frontera que el marco CSCRM nacional deberá abordar.[^47][^50]

### 8.4. La Ventana Cuántica

El riesgo cuántico en la cadena de suministro no requiere un ordenador cuántico operativo para materializarse: los atacantes ya recolectan tráfico cifrado hoy. España, con una economía fuertemente internacionalizada y una cadena de suministro industrial diversa, tiene exposición a este riesgo a través de los miles de proveedores que todavía intercambian contratos y datos sensibles con algoritmos RSA y ECC. El roadmap europeo 2026-2030-2035 es la hoja de ruta normativa, pero la acción preventiva —inventario criptográfico, exigencia de roadmap PQC a proveedores— ya es necesaria hoy.[^45][^43][^44]

***

## 9. Conclusiones Operativas

El ecosistema español de indicadores CSCRM ha alcanzado en 2025 un punto de inflexión: la arquitectura normativa existe (ENS, NIS2 en transposición, Foro Nacional), los instrumentos de medición están disponibles (IMC de INCIBE, cuestionario CCN-CERT/ISMS Forum, plataformas CCI) y la evidencia de riesgo es contundente (ataques duplicados, 22,5% de brechas en terceros, 254 días de detección). Lo que falta es la **institucionalización obligatoria del programa CSCRM** —la ley pendiente— y la **integración efectiva de los indicadores emergentes** (PQC, AIBOM, Zero Trust OT) en los marcos existentes.

Las organizaciones que operen en sectores esenciales en España deben, con carácter prioritario:

1. **Activar el cuestionario CCN-CERT/ISMS Forum** como herramienta de evaluación inicial de proveedores, sin esperar a la entrada en vigor de la Ley de Coordinación y Gobernanza.
2. **Elevar a L4–L5 los indicadores IMC** relativos a dependencias externas (R-CS-OE5-02 a R-CS-OE8-01) y a supervisión del proveedor (T-SC-OE4-01).
3. **Incluir el SBOM como requisito contractual** en todos los nuevos contratos con proveedores de software, anticipando las obligaciones del Cyber Resilience Act.
4. **Iniciar el inventario criptográfico** en la cadena de suministro, identificando qué proveedores utilizan RSA/ECC en intercambios de datos de larga vida útil.
5. **Integrar la métrica de "tiempo de detección en cadena de suministro"** (objetivo: <60 días frente a los 254 días actuales) como KPI de junta directiva en los sectores banca, transporte y energía.

El indicador que, en última instancia, resume la madurez CSCRM de una organización —o de un país— no es la existencia de una política, sino la capacidad de responder honestamente a esta pregunta: *¿cuánto tardaríamos en detectar que uno de nuestros proveedores críticos ha sido comprometido?* En España, la respuesta media todavía ronda los ocho meses. Esa cifra, más que cualquier otra, define la urgencia de la agenda.

***

*Informe elaborado con fuentes primarias de INCIBE-CERT, CCN-CERT/ISMS Forum Spain, Foro Nacional de Ciberseguridad (DSN), Centro de Ciberseguridad Industrial (CCI), ENISA (NIS360 y NIS Investments 2025), Cipher/Grupo Prosegur, Gobierno de España (Consejo de Ministros), NIST SP 800-161r1 y SP 800-55 Vol. 2, y análisis especializados sobre PQC e IA en cadena de suministro.*

---

## References

1. [The Government approves a strengthening of Spain's cybersecurity ...](https://digital.gob.es/en/comunicacion/notas-prensa/mtdfp/2025/05/2025-05-06_02) - The Council of Ministers today approved a set of actions in cybersecurity and cyberdefence that comp...

2. [Los ataques a la cadena de suministro se duplican y cuestan ...](https://digitalinside.es/los-ataques-a-la-cadena-de-suministro-se-duplican-y-cuestan-millones-a-las-empresas/) - El estudio señala al sector manufacturero, donde los ataques crecieron un 61% interanual, como uno d...

3. [Los ciberataques a la cadena de suministro se duplican en 2025 y ...](https://www.prosegur.com/media/articulo/prensa/ciberataques-cadena-suministro-duplican-2025-coste-global-53200-millones-dolares) - La unidad de ciberseguridad del Grupo Prosegur pone de relieve la intensificación y diversificación ...

4. [Cipher: se duplican los ataques a la cadena en 2025 - Logística 360](https://logistica360.es/cipher-se-duplican-los-ataques-a-la-cadena-en-2025/) - De cara a 2026, la compañía anticipa una intensificación de los ataques contra las cadenas de sumini...

5. [El Gobierno aprueba el anteproyecto de Ley de Coordinación y ...](https://www.twobirds.com/es/insights/2025/spain/el-gobierno-aprueba-el-anteproyecto-de-ley-de-coordinaci%C3%B3n-y-gobernanza-de-la-ciberseguridad) - El anteproyecto transpone al ordenamiento jurídico español la Directiva NIS-2 , en vigor desde el 16...

6. [Directiva NIS2 en Espana: obligaciones, plazos y sanciones para ...](https://www.delbion.com/insights/nis2-espana-obligaciones-empresas/) - La directiva NIS2 afecta a miles de empresas en Espana. Te explicamos que obligaciones tienes, los p...

7. [The Government of Spain presents the future Law on Cybersecurity ...](https://www.lamoncloa.gob.es/lang/en/gobierno/councilministers/paginas/2025/20250114-council-press-conference.aspx) - The aim of the regulation is to strengthen the protection of networks and information systems, which...

8. [Directiva NIS2 en España: todo lo que debes saber - Factorial](https://factorial.es/blog/nis2-espana/) - En España, tras su transposición mediante la Ley de Coordinación y Gobernanza de la Ciberseguridad, ...

9. [NIS2 España: qué exige la ley de ciberseguridad a las empresas](https://digitalperito.es/blog/ley-ciberseguridad-nis2-espana-2026-obligaciones-empresas/) - Guía completa sobre la Directiva NIS2 en España. Qué empresas están obligadas, sanciones hasta 10M€,...

10. [¿Cómo afectará la Ley de Coordinación y Gobernanza de la ...](https://www.tarlogic.com/es/blog/ley-de-coordinacion-y-gobernanza-de-la-ciberseguridad/) - La Ley de Coordinación y Gobernanza de la Ciberseguridad contempla multas de hasta 10 millones de € ...

11. [Orden PJC/448/2025, de 6 de mayo, por la que se publica ...](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-9088) - BOE-A-2025-9088 Orden PJC/448/2025, de 6 de mayo, por la que se publica el Acuerdo del Consejo de Mi...

12. [El Gobierno aprueba un plan de 1.157 millones para reforzar ...](https://www.rtve.es/noticias/20250506/gobierno-aprueba-plan-1157-millones-para-reforzar-ciberseguridad-ciberdefensa/16567959.shtml) - El Gobierno aprueba un plan de 1.157 millones para reforzar la ciberseguridad y ciberdefensa de Espa...

13. [El Gobierno aprueba un plan de 1.157 millones para reforzar la ciberseguridad](https://elpais.com/espana/2025-05-06/el-gobierno-aprueba-un-plan-de-1157-millones-para-reforzar-la-ciberseguridad.html) - España sufrió más de 100.000 ciberataques el año pasado, uno grave cada tres días, el 70% contra adm...

14. [Real Decreto 311/2022 y ENS: Guía completa - Consultores ISO](https://consultoresiso.es/real-decreto-311-2022-y-el-esquema-nacional-de-seguridad-ens-guia-completa) - Seguridad de la cadena de suministro. Se incorporan controles específicos para proveedores, servicio...

15. [Esquema Nacional de Seguridad | Sitio oficial del Departamento de ...](https://www.dsn.gob.es/ca/node/17481) - Con estos parámetros, el Real Decreto 311/2022 tiene como objetivos principales: Mejorar y alinear e...

16. [La necesidad de cumplir el ENS | Derten Ciberseguridad](https://www.derten.com/es/articulos-generales/tic-tac-empieza-la-cuenta-atras-para-cumplir-el-esquema-nacional-de-seguridad) - Esta normativa actualiza y refuerza el ENS, enfocándose en la resiliencia de los sistemas frente a c...

17. [ENS 2025: Nuevos Requisitos para Proveedores Cloud - abemon](https://abemon.es/es/insights/ens-2025-requisitos-proveedores-cloud) - Actualizacion del Esquema Nacional de Seguridad para proveedores cloud en 2025. Nuevos requisitos, p...

18. [Esquema Nacional de Seguridad 2022: Cambios y novedades](https://www.globalsuitesolutions.com/es/ens-2022-novedades-para-empresas-esquema-nacional-seguridad/) - El 3 de Mayo de 2022 se ha publicado la actualización del nuevo Esquema Nacional de Seguridad. Descu...

19. [Medidas de Seguridad según el Esquema Nacional de Seguridad](https://iveconsultores.com/medidas-de-seguridad-segun-el-esquema-nacional-de-seguridad/) - Estas son las Medidas de Seguridad según el Esquema Nacional de Seguridad - Conócelas e Impleméntala...

20. [46 métricas para mejorar la ciberresiliencia en un servicio esencial](https://www.incibe.es/incibe-cert/blog/46-metricas-para-mejorar-la-ciberresiliencia-en-un-servicio-esencial) - Estas 46 métricas, miden cuatro objetivos o metas a alcanzar, y nueve categorías o dominios funciona...

21. [[PDF] Diccionario de Indicadores para Mejora de la Ciberresiliencia (IMC)](https://www.incibe.es/sites/default/files/contenidos/guias/IMC/imc_02_diccionario-indicadores_2023.pdf) - respuesta a incidentes o CERT, INCIBE-CERT, compañías de consultoría en ciberseguridad, proveedores ...

22. [PUBLICADO EL CUESTIONARIO DE LA CADENA DE ...](https://es.linkedin.com/posts/javalfer_publicado-el-cuestionario-de-la-cadena-de-activity-7294669201242259456-5Kyv) - PUBLICADO EL CUESTIONARIO DE LA CADENA DE SUMINISTRO Es una colaboración conjunta entre el CCN-CERT ...

23. [[PDF] Portada carta cadena de suministros (2) - ISMS Forum Spain](https://www.ismsforum.es/ficheros/descargas/cartacadenasuministrosfinal1739549325.pdf) - ISMS Forum, a través del Grupo de trabajo de la cadena de suministro, busca confeccionar un modelo d...

24. [La ciberseguridad industrial en 2025 y la estrategia del ...](https://www.cci-es.org/la-ciberseguridad-industrial-en-2025-y-la-estrategia-del-cci-para-2026/) - Descubre las tendencias de ciberseguridad industrial en 2025 y la estrategia del CCI para 2026, cent...

25. [El CCI crea dos plataformas para identificar proveedores y requisitos de ciberseguridad industrial](https://www.automaticaeinstrumentacion.com/texto-diario/mostrar/3494108/cci-crea-plataformas-identificar-proveedores-requisitos-ciberseguridad-industrial) - Denominadas RECIN y Catálogo Activo. ...

26. [INCIBE gestionó 122.223 incidentes de ciberseguridad en 2025, un ...](http://espanadigital.gob.es/gl/actualidad/incibe-gestiono-122223-incidentes-de-ciberseguridad-en-2025-un-26-mas-que-el-ano) - INCIBE gestionó 122.223 incidentes de ciberseguridad en 2025, un 26% más que el año anterior · Malwa...

27. [INCIBE detectó más de 122.000 incidentes de ciberseguridad en 2025](https://www.tribunamadrid.com/noticias/433509/incibe-detecto-mas-de-122-000-incidentes-de-ciberseguridad-en-2025) - La Línea de Ayuda ? 017 atendió más de 142.000 consultas, un 45% más que el año anterior

28. [INCIBE detectó 122.223 incidentes en 2025 y el 017 se dispara](https://www.opensecurity.es/incibe-detecto-122-223-incidentes-en-2025-y-el-017-se-dispara-mas-fraude-mas-iot-y-mas-urgencia/) - La ciberseguridad en España cerró 2025 con una fotografía que ya no admite lecturas complacientes: e...

29. [Balance INCIBE 2025: 122.223 ciberincidentes en España (+26%)](https://digitalperito.es/blog/incibe-balance-2025-122000-ciberincidentes-espana/) - INCIBE gestionó 122.223 ciberincidentes en 2025 (+26%). 55.411 malware, 25.133 phishing, 392 ransomw...

30. [Los ciberataques a la cadena de suministro se duplican en 2025](https://www.ituser.es/seguridad/2026/02/los-ciberataques-a-la-cadena-de-suministro-se-duplican-en-2025) - El estudio revela que el 22,5% de todas las brechas de seguridad registradas en 2025 involucraron a ...

31. [Los ciberataques a cadenas de suministro se han duplicado en 2025](https://www.cadenadesuministro.es/logistica/ciberataques-cadenas-suministro-se-han-duplicado-en-2025_1513976_102.html) - Los ciberataques han generado un coste medio de 4,33 millones de euros por incidente en 2025. Foto: ...

32. [NIS Investments 2025](https://www.metametris.com/articles/nis-investments-2025) - This annual report analyzes how cybersecurity policy translates into practical actions, investments,...

33. [NIS Investments 2025 - ENISA - European Union](https://www.enisa.europa.eu/publications/nis-investments-2025) - The NIS360 is a new ENISA product that assesses the maturity and criticality of sectors of high crit...

34. [Enisa NIS Investments 2025 Report | Davide Maniscalco - LinkedIn](https://www.linkedin.com/posts/davide-maniscalco_enisa-nis-investments-2025-report-activity-7404043917194792960-BIXU) - European Union Agency for Cybersecurity (ENISA) #NIS Investments 2025 — Key Takeaways on How Cyber P...

35. [ENISA - NIS Investments 2025](https://www.youtube.com/watch?v=kE5gx7GmZrQ) - The annual NIS Investments report presents the findings of a study conducted by ENISA to explore how...

36. [ENISA issued its first NIS360 report - Ceeyu](https://www.ceeyu.io/company/news/enisa-issued-its-first-nis-360-report-assessing-the-cybersecurity-maturity-companies-in-sectors-of-high-criticality-under-the-nis-2-directive) - ENISA issued its first NIS360 report assessing the Cybersecurity maturity companies in sectors of hi...

37. [ENISA's NIS360: Cybersecurity Maturity in 2025 - Cyble](https://cyble.com/blog/enisa-nis2-cybersecurity-maturity-report/) - The NIS360 report provides a roadmap for improving cybersecurity maturity across Europe's most criti...

38. [New ENISA NIS360 Report: Key Takeaways for Digital Compliance ...](https://streamlex.eu/news/new-enisa-nis360-report-key-takeaways-for-digital-compliance-professionals/) - The ENISA NIS360 report assesses the maturity and criticality of key sectors under the NIS2 Directiv...

39. [CISA releases 2025 SBOM Minimum Elements outlining minimum ...](https://industrialcyber.co/cisa/cisa-releases-2025-sbom-minimum-elements-outlining-minimum-requirements-for-software-transparency/) - The 2025 SBOM Minimum Elements document updates CISA's earlier guidance to account for advances in S...

40. [[PDF] SBOM LANDSCAPE ANALYSIS - ENISA](https://www.enisa.europa.eu/sites/default/files/2025-12/SBOM%20Analysis%20-%20Towards%20an%20Implementation%20Guide_v1.20-Published.pdf) - A Software Bill of Materials is a formal, machine-readable inventory documenting all components, lib...

41. [NIS2 Technical Implementation Guidance | ENISA - European Union](https://www.enisa.europa.eu/publications/nis2-technical-implementation-guidance) - This report provides technical guidance to support the implementation of the NIS2 Directive for seve...

42. [Análisis y propuestas relativas a la seguridad de la cadena ...](https://e8dsoluciones.es/analisis-y-propuestas-relativas-a-la-seguridad-de-la-cadena-de-suministro-foro-nacional-de-ciberseguridad/) - La cadena de suministro digital se ha convertido en un eslabón crítico para la resiliencia empresari...

43. [Quantum security is turning into a supply chain problem - Help Net ...](https://www.helpnetsecurity.com/2026/02/20/post-quantum-cryptography-supply-chain-priority/) - Post-quantum cryptography is becoming a supply chain security priority as organizations plan for qua...

44. [Post-Quantum Cryptography for products & OT - RiskInsight](https://www.riskinsight-wavestone.com/en/2026/02/post-quantum-cryptography-for-products-ot-from-trends-to-industrial-reality/) - Post-Quantum Cryptography (PQC) has fueled debates for years, but since the European Commission’s Ju...

45. [Post-Quantum Cryptography in 2026: 5 Predictions](https://quantumxc.com/blogs-podcasts/quantum-predictions-it-network-infrastructure/) - In 2026, sophisticated attackers will increasingly target supply chain partners with weaker cryptogr...

46. [Post-quantum cryptography in 2026 | Talan - Site groupe](https://www.talan.com/uk/en/post-quantum-cryptography-2026) - It is also framing it as a question of industrial scale-up, supply-chain resilience, governance, and...

47. [Artificial intelligence and machine learning: Supply chain risks and ...](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/artificial-intelligence-and-machine-learning-supply-chain-risks-and-mitigations) - Adopting AI and ML systems introduces unique supply chain risks, which can threaten the cyber securi...

48. [FAQ NIS2 | INCIBE-CERT](https://www.incibe.es/incibe-cert/sectores-estrategicos/FAQNIS2) - A fin de identificar las cadenas de suministro que deben ser objeto de una evaluación coordinada de ...

49. [[PDF] SafeCipher's 2026 Post-Quantum Cryptography (PQC) Readiness ...](https://safecipher.co.uk/wp-content/uploads/2025/12/SafeCipher-PQC-Readiness-Checklist.pdf) - Introduction to the Quantum Threat in 2026. As we enter 2026, quantum computing advances make “harve...

50. [AI supply chain security: CISO Guide 2025 - Hodeitek](https://hodeitek.com/blog/cybersecurity/ciso-playbook-ai-supply-chain-security-strategies-risks-and-controls-for-2025/) - AI workloads generate unique telemetry—vector DB queries, model latency, drift metrics, and guardrai...

51. [Zero Trust in 2025: 5 Sensitive Areas to Prioritize - Secude](https://www.secude.com/posts/zero-trust-in-2025-5-sensitive-areas-to-prioritize) - It only takes one third-party breach to infect a whole supply chain, so focus on Zero Trust tools th...

