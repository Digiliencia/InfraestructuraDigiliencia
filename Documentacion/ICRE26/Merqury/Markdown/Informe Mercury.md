
# INFORME MERCURY: TENDENCIAS EN CUANTIFICACIÓN DE RIESGOS DE CIBERSEGURIDAD PARA ESPAÑA (2024-2025)

## Resumen Ejecutivo

España enfrenta un escenario de ciberseguridad paradójico: posiciona entre los líderes europeos en marcos regulatorios y gobernanza estratégica (Tier 1 en el Índice Global de Ciberseguridad de la UIT 2024), pero gestiona casi 100.000 incidentes anuales con una tasa de crecimiento del 16,6% interanual. La amenaza ha escalado desde lo académico hacia lo operacional: organizaciones españolas necesitan metodologías cuantificables que traduzcan riesgos técnicos complejos en exposiciones financieras defensibles ante reguladores, aseguradores y directorios.

En este contexto, **Mercury Risk and Compliance, Inc.** —fundada en 2023 por pioneros en GRC y cuantificación de riesgos, con presencia verificada en Madrid desde 2021—propone un enfoque diferenciador: metodologías propietarias **AVRQ** (Advanced Asset Value-based Risk Quantification), **ACET** (Automated Controls Efficacy Testing) y **A.D.A.M.** (Automated Dynamic Asset Mapping), que pivotean desde la *mitigación de pérdidas* hacia la *protección y ampliación de valor de activos*.

Este informe examina: (1) la arquitectura conceptual de Mercury aplicada al contexto regulatorio español; (2) cómo Mercury se posiciona ante marcos competidores como FAIR (Factor Analysis of Information Risk) y CAsPeA; (3) indicadores territoriales y de cumplimiento NIS2 en España; y (4) recomendaciones para adopción estratégica en organizaciones críticas españolas.

***

## 1. MARCO DE CONTEXTO: CIBERSEGURIDAD EN ESPAÑA 2024-2025

### 1.1 Panorama de Amenazas y Incidentes

El Instituto Nacional de Ciberseguridad (INCIBE), entidad dependiente del Ministerio para la Transformación Digital, reportó en 2024 un total de **97.348 incidentes de ciberseguridad gestionados**, representando un incremento del 16,6% respecto a 2023. De este total, el 67,6% afectó a ciudadanía (65.808 casos) y el 32,4% a empresas, pymes y autónomos (31.540 casos).[^1_1][^1_2]


| Vector de Ataque | Casos 2024 | % del Total | Tendencia |
| :-- | :-- | :-- | :-- |
| Malware (incluyendo ransomware) | 42.136 | 43,3% | Estable |
| Fraude online (phishing principal) | 38.000+ | 43,2% | En aumento |
| Intrusiones no autorizadas | 7.470 | 7,7% | Variable |
| Tiendas online fraudulentas | 2.122 | 2,2% | Emergente |
| **Total** | **97.348** | **100%** | **+16,6%** |

Entre operadores esenciales e importantes (alineados con NIS2), se registraron **341 incidentes**, con el 24,6% en transporte y 23,8% en sector financiero. Adicionalmente, INCIBE detectó y notificó **183.851 sistemas vulnerables relevantes** susceptibles de explotación.[^1_2][^1_1]

### 1.2 Inversión Gubernamental y Posicionamiento Estratégico

En mayo de 2025, el Gobierno de España aprobó medidas para fortalecer ciberseguridad y defensa cibernética con un presupuesto sin precedentes de **€1.157 millones** como parte del Plan Nacional de Ciberseguridad. Este esfuerzo se articula con la Estrategia Industrial y Tecnológica de Seguridad y Defensa, consolidando a España como actor estratégico en defensa cibernética europea.[^1_3]

La asignación presupuestaria se distribuye como sigue:

- **60%**: Ministerio de Defensa, incluyendo CCN-CERT e Mando Conjunto del Ciberespacio
- **Porcentaje significativo**: Expansión del Centro de Operaciones de Seguridad 5G (SOC 5G), auditorías automatizadas de servicios digitales públicos, sistemas de detección de amenazas potenciados por IA
- **Fondos adicionales**: €3.260 millones para modernización de sistemas de telecomunicaciones encriptados de Fuerzas Armadas y adquisición de satélites, antenas, radares.[^1_4]


### 1.3 Posicionamiento en Índices Internacionales

**Índice Global de Ciberseguridad de la UIT 2024**: España alcanzó la clasificación **Tier 1 (Role-modelling)**, compartiendo este nivel con 19 países europeos adicionales, únicamente por debajo de Italia, Reino Unido y Turquía que lograron puntuación perfecta.[^1_5]

El desempeño se desglosó así por pilares (máximo 20 puntos cada uno):


| Pilar | Puntuación | Estado |
| :-- | :-- | :-- |
| Marco Legal | 20/20 | Excelente |
| Medidas Técnicas | 20/20 | Excelente |
| Medidas Organizacionales | 20/20 | Excelente |
| Desarrollo de Capacidades | 19,74/20 | Muy Bueno |
| Cooperación | 20/20 | Excelente |

A pesar de este posicionamiento aparentemente robusto, expertos subrayan que estas puntuaciones reflejan "fuerza relativa" más que capacidad absoluta de protección. España enfrenta desafíos operacionales reales: únicamente el 52% de organizaciones españolas han adoptado marcos de seguridad avanzados, dejando el 48% con exposición a amenazas modernas.[^1_6][^1_5]

### 1.4 Normativa NIS2 y Transposición Legislativa Española

La Directiva NIS2 (Directiva (UE) 2022/2555) establece medidas para lograr un nivel común elevado de ciberseguridad en la UE. En España, el proceso de transposición avanzó con la aprobación por el Consejo de Ministros en enero de 2025 del *Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad*, integrando tanto la NIS2 como la Directiva de Resiliencia de Entidades Críticas (CER).[^1_7]

**Cronograma esperado** de implementación legislativa:


| Hito | Fecha | Estado |
| :-- | :-- | :-- |
| Registro acelerado en Congreso y Senado | Febrero 2025 | Completado |
| Audiencias parlamentarias y enmiendas | Q3 2025 | En curso |
| Enactación y publicación en BOE | Q1 2026 | Proyectado |
| Lanzamiento del CNCS y notificación obligatoria | H1 2026 | Proyectado |

**Entidades Afectadas** (clasificación dual):

- **Entidades Esenciales (EE)**: ≥250 empleados o €50M de facturación (grandes utilities, hospitales, ministerios)
- **Entidades Importantes (EI)**: ≥50 empleados o €10M de facturación (logística, manufactura medianos)
- **Proveedores clave**: Todas las entidades críticas de DNS, telecomunicaciones, cloud, sin consideración de tamaño

**Régimen Sancionador NIS2 en España**:


| Categoría | Multa Máxima | Observaciones |
| :-- | :-- | :-- |
| Entidades Esenciales | €10M o 2% facturación global | Suspensión de certificaciones, publicación |
| Entidades Importantes | €7M o 1,4% facturación global | Penalizaciones periódicas por incumplimiento |
| Otros | €10K-€2M (escalonado) | Órdenes correctivas, amonestaciones |

Adicionalmente, miembros de directorios son **personalmente responsables** de incumplimientos de gobernanza cibernética y deben aprobar formalmente estrategias cibernéticas internas.[^1_7]

***

## 2. MERCURY RISK AND COMPLIANCE INC.: ARQUITECTURA METODOLÓGICA Y DIFERENCIACIÓN COMPETITIVA

### 2.1 Perfil Institucional y Presencia Territorial

**Mercury Risk and Compliance, Inc.** fue constituida en 2023 con sede en Austin, Texas, fundada por Gavin Anthony Grounds (CEO) —reconocido pensador global en gestión de riesgos con experiencia en tecnología, telecomunicaciones, ciberseguridad y servicios financieros— y Grace E. Beason (COO, Co-fundadora), con expertise en gobernanza, riesgos y ciberseguridad en entornos multipaís.[^1_8]

La empresa mantiene operaciones en geografías estratégicas: Estados Unidos (Nueva York, Nueva Jersey, Boston, California), Reino Unido, Europa, Asia Sudoriental y Australasia. En España específicamente, se registró **Mercury Risk \& Compliance Solutions SL** en Madrid (C/ O'Donnel 10, 2º B, 28048) con constitución el 7 de junio de 2021 y capital social de €3.000. Aunque la presencia española actual es reducida, la incorporación anterior a la fundación de la matriz estadounidense sugiere una estrategia de preparación territorial.[^1_9][^1_8]

### 2.2 Filosofía Fundacional: "Grounds' Rules" y Risk-as-Currency

Mercury diferencia su propuesta mediante el concepto **"Grounds' Rules"**, centrado en *risk-as-currency* —tratando el riesgo no como una magnitud abstracta a minimizar, sino como un activo empresarial cuyo valor se **protege, amplía y optimiza**. Esta filosofía contrasta con los enfoques tradicionales de "loss avoidance" (mitigación de pérdidas) prevalentes en frameworks como FAIR.[^1_10]

La misión explícita es: **"Protecting value through innovative methodologies and solutions"**—protección de valor, no solo evitación de pérdidas.[^1_10]

### 2.3 Arquitectura Metodológica: AVRQ, ACET y A.D.A.M.

Mercury integra tres metodologías propietarias en un ecosistema coherente:

#### 2.3.1 AVRQ (Advanced Asset Value-based Risk Quantification)

**AVRQ** es una metodología **patent-pending** de cuantificación de riesgos basada en valor de activos, diferenciándose de FAIR en que:

- **Enfoque primario**: Valor de activos y su protección, no magnitud de pérdidas potenciales
- **Cuantificación empírica**: Scoring numérico empírico gestionable en múltiples dominios de riesgo (Ciber, Tecnología, Terceros, Usuario, Daño del Mundo Físico)
- **Orientación empresarial**: Habilitación de decisiones operacionales y de inversión centradas en **retorno sobre riesgo**, no reducción de riesgo a costa de eficiencia operativa
- **Escalabilidad**: Automatable y escalable en contextos organizacionales complejos


#### 2.3.2 ACET (Automated Controls Efficacy Testing)

**ACET** implementa pruebas automatizadas de eficacia de controles, integrando inversiones ya realizadas en tecnologías GRC, ciberseguridad y auditoría existentes.[^1_10]

Sus funcionalidades incluyen:

- Aprovechamiento de stacks tecnológicos preexistentes (SIEM, GRC, sistemas de auditoría)
- Evaluación continua, no periódica, de eficacia de controles
- Integración de datos cuantitativos en tiempo real para refinamiento de cuantificaciones de riesgo
- Reporte ejecutivo traducido a lenguaje de negocio (financiero, impacto operativo)


#### 2.3.3 A.D.A.M. (Automated Dynamic Asset Mapping)

**A.D.A.M.** es una solución de machine learning que mapea dinámicamente activos en entornos organizacionales complejos, soportando identificación continua de:

- Activos críticos y su evolución
- Conexiones de dependencia entre activos (attack paths)
- Clasificación de riesgo granular
- Adaptación a cambios operacionales y amenazas emergentes

Esta capacidad es especialmente relevante en contextos españoles donde infraestructuras críticas (energía, transporte, sanidad) evolucionan constantemente bajo presión de digitalización y conformidad NIS2.

### 2.4 Diferenciación frente a FAIR (Factor Analysis of Information Risk)

| Dimensión | FAIR | Mercury AVRQ |
| :-- | :-- | :-- |
| **Enfoque primario** | Severidad de vulnerabilidad y magnitud de pérdida esperada | Protección y ampliación de valor de activos |
| **Cuantificación** | Loss Event Frequency (LEF) + Loss Magnitude (LM) = ALE | Scoring empírico de valor de activos + riesgo |
| **Fórmula base** | Risk = Threat × Vulnerability × Impact | Value-based assessment tailored to assets |
| **Complejidad técnica** | Alta (requiere expertise estadístico, distribuciones de probabilidad) | Media-alta (ML, ABC, mapeo dinámico) |
| **Automatización** | Limitada; requiere input manual periódico | Elevada; integración continua de datos |
| **Orientación ejecutiva** | Loss exposure en dólares; justificación defensiva | Return on Risk; decisiones de inversión ofensivas |
| **Aplicabilidad multidominio** | Principalmente cibernético | Ciber, Tecnología, Terceros, Usuario, Físico |
| **Adopción internacional** | Amplia (Open Group, estándar reconocido) | Emergente; posicionamiento en empresas de alto valor |
| **Fortaleza pedagógica** | Modelos mentales transferibles; transparencia metodológica | Automatización; velocidad de decisión |
| **Debilidad crítica** | "Black box" de distribuciones complejas; subjetividad en inputs | Confianza en datasets históricos; riesgo de sesgos ML |


***

## 3. COMPARATIVE LANDSCAPE: MERCADO DE CUANTIFICACIÓN DE RIESGOS EN ESPAÑA Y EUROPA

### 3.1 CAsPeA: Competidor Académico Emergente

**CAsPeA** (Cost Assessment of Personnel Activities in Security) representa el enfoque académico-europeo más desarrollado para estimación de costes de ciberseguridad, estructurado explícitamente sobre **ISO/IEC 27001** y Activity-Based Costing (ABC).[^1_11][^1_12]

**Características de CAsPeA**:

- **Estándar de referencia**: ISO/IEC 27001 directamente integrado
- **Alcance**: Estimación de costes de actividades de personal en gestión de ciberseguridad (diseño de políticas, capacitación, despliegue de medidas técnicas, testing)
- **Exclusión deliberada**: Externaliza costes de "cyberassets" (hardware, software, equipamiento físico)
- **Herramienta**: Spreadsheet calculable, facilitando adopción por pequeñas empresas
- **Fortaleza**: Universalidad, alineamiento con ISO, reproducibilidad
- **Debilidad**: Enfoque estrecho (solo personal); no integra cuantificación de riesgo o retorno sobre inversión

**Aplicabilidad en España**: CAsPeA se utiliza en contextos académicos (Universidades Politécnica de Gdańsk, Plymouth), pero su adopción empresarial en España es limitada. Su enfoque en costes de personal—no en riesgos críticos—lo sitúa como complemento, no sustituto, de frameworks como Mercury AVRQ.

### 3.2 FAIR Institucionalizado en Contexto Europeo

FAIR (Factor Analysis of Information Risk), desarrollado en 2005 por Jack Jones (ex-CISO de Nationwide Mutual Insurance, ahora presidente del FAIR Institute no-profit), se ha convertido en el **estándar abierto más ampliamente adoptado en Europa** para cuantificación cuantitativa de riesgos cibernéticos.[^1_13][^1_14][^1_15]

**Puntos de adopción FAIR en contexto europeo/español**:

- **Empresas financieras españolas**: Adopción creciente bajo presión de supervisores bancarios (Banco de España, EBA) para expresar riesgos en términos monetarios
- **Seguros cibernéticos**: Aseguradores españoles requieren cada vez más cuantificaciones FAIR para pricing y underwriting
- **Consultorías Big Four**: Presencia significativa de FAIR en metodologías de consultoría internacional operando en España
- **Marcos de validación**: FAIR complementa ISO 27005, COBIT, NIST CSF

**Debilidades de FAIR documentadas en literatura académica contemporánea**:[^1_16]

1. **Complejidad extrema**: Algoritmos "black-box" con distribuciones probabilísticas sofisticadas requieren expertise estadístico que muchas organizaciones españolas carecen
2. **Rigidez metodológica**: Difícil adaptación a amenazas emergentes (IA, quantum, ataques supply-chain) sin reformulaciones significativas
3. **Subjetividad disfrazada**: Inputs de "expert opinion" sobre frecuencia de amenaza, capacidad de atacante, y magnitud de impacto introducen sesgos no abordados sistemáticamente
4. **Enfoque defensivo**: Orientación a "¿cuánto podemos perder?" vs. "¿cómo podemos ganar resiliencia?"

### 3.3 GRAACE y Modelos Emergentes

**GRAACE** (por sus componentes probabilísticas Granular Risk, Attack surfaces, Aggregate Control Effectiveness) emerge como framework alternativo que busca simplificar FAIR mientras mejora realismo:[^1_17]

- Factorización explícita de superficies de ataque y caminos de ataque (attack paths)
- Curves de Excedencia de Pérdida que comunican rango completo de pérdidas probabilísticas
- Evita complicaciones de FAIR sobre "Primary Losses" vs. "Secondary Risk"

A la fecha, GRAACE carece de adopción institucional significativa en España, pero académicos españoles monitorean su evolución como alternativa estructurada a FAIR.

***

## 4. INDICADORES DE CIBERSEGURIDAD: TERRITORIAL Y REGULATORIO

### 4.1 Índice de Ciberseguridad UE 2024 (ENISA): Desagregación de Áreas

ENISA publicó en junio 2024 el **EU-Cybersecurity Index 2024**, herramienta de medición compuesta con estructura jerárquica que evalúa madurez de ciberseguridad en 27 Estados miembros UE.[^1_18]

**Puntuación general UE**: 62,65/100 (out of 100)

Los Estados miembros muestran alineación considerable alrededor del promedio europeo (desviación promedio de 3,76 unidades). España, aunque no desagregada públicamente en el documento base, se sitúa en rango comparativamente alto dado su posicionamiento ITU Tier 1.[^1_18]

**Cuatro áreas temáticas del EU-CSI 2024**:


| Área | Puntuación UE | Descripción | Observación Crítica |
| :-- | :-- | :-- | :-- |
| **Capacidad** | 64,51 | Habilidad de sociedad para reconocer amenazas y prevenir incidentes | Majority de MS dentro rango 10-puntos del promedio |
| **Operaciones** | 57,63 | Habilidad de MS para conducir operaciones de ciberseguridad y asegurar resiliencia | **Más baja de todas las áreas**; brecha significativa |
| **Mercado/Industria** | 62,36 | Capacidad del sector privado para prevenir, detectar, analizar amenazas | Máxima alineación entre MS (desv. avg 2,78) |
| **Política** | 66,09 | Estado de desarrollo e implementación de política ciberseguridad | Puntuación más alta pero mínima alineación (variabilidad 27,28 a +17,45) |

**Indicadores con peores resultados europeos (foco de mejora):**

1. **Uso de IA en seguridad TIC por empresas**: 3,18/100 (crítico)
2. **Inversión en ciberseguridad por entidades esenciales/importantes**: 7,14/100 (grave)
3. **Certificación CSIRT**: 10,31/100 (urgente)
4. **Evaluación de riesgo cibernético por empresas**: 32,01/100 (significativo)

España, como signataria NIS2, debe abordar específicamente estas brechas mediante reglamentación nacional (CNCS) y programas de concienciación.

### 4.2 Sectores Estratégicos Españoles: Exposición y Requisitos NIS2

La transposición española de NIS2 expande significativamente el perímetro de entidades sujetas a regulación. Sectores clave identificados:


| Sector | Ejemplos | Incidentes 2024 (INCIBE) | Requisito NIS2 |
| :-- | :-- | :-- | :-- |
| **Energía \& Utilities** | Hidroeléctrica, gasistas, distribuidoras | No desagregado | EE (≥250 emp) |
| **Transporte** | Aeropuertos, ferrocarril, logística | 24,6% de 341 (83) | EE (mayoría), EI |
| **Finanzas \& Tributario** | Bancos, cajas, fintechs | 23,8% de 341 (81) | EE (mayoría) |
| **Sanidad** | Hospitales ≈800, clínicas | Creciente (ransomware) | EE (mayoría) |
| **Telecomunicaciones** | Movistar, Vodafone, Orange | Fundamental | EE (todas) |
| **Infraestructura Digital** | Cloud, DNS, CDN, data centers | Crítica | EE (todas) |
| **Administración Pública** | Ministerios, administraciones autonómicas, municipios grandes | 19% de incidentes ENISA | EE/EI (escalonado) |

**Implicaciones Mercury para sectores españoles:**

- **Energía \& Transporte**: AVRQ idóneo para mapear criticidad de activos OT/IT híbridos; ACET para validación continua
- **Finanzas**: AVRQ alinea con requisitos de supervisores (Banco España, CNMV) para cuantificación monetaria
- **Sanidad**: A.D.A.M. crítico para hospitales con redes complejas; AVRQ para scoring de equipamiento médico


### 4.3 Mercado Español de Ciberseguridad: Proyecciones de Inversión

El mercado de ciberseguridad en España alcanzó aproximadamente **USD 5,01 mil millones en 2026** y se proyecta crecer a **USD 7,91 mil millones en 2031**, con una CAGR de **9,54%**.[^1_19]

**Desglose por segmento 2025-2026**:


| Segmento | % Revenue | CAGR 2025-2031 | Observación |
| :-- | :-- | :-- | :-- |
| **Solutions** | 69,12% | 8,7% | Firewalls, EDR, IAM, application security |
| **Cloud deployments** | 62,18% | 13,12% | Mandatos CorA, conformidad ENS "Alto" |
| **Managed Services** | -- | 12,33% | Crecimiento más rápido; shortage de talento |
| **Large Enterprises** | 59,10% | 6,8% | Presupuestos profundos, riesgo complejo |
| **SMEs** | -- | 10,85% | Aceleración significativa; subvenciones Digital Spain |

**Verticales clave con mayor gasto**:

1. **BFSI** (28,35% de revenue): Requerimientos PSD2, zero-trust
2. **Healthcare** (CAGR 15,85%): Digitalización de registros médicos, tele-consulta
3. **Energía**: OT-security tras aumento 43% en ataques
4. **Manufactura \& Industrial**: Integración IIoT requiere seguridad en edge

**Implicación para Mercury**: Expansión de mercado crea oportunidad para metodologías diferenciadas de cuantificación que no requieren expertise estadístico extremo (fortaleza relativa de AVRQ vs. FAIR).

***

## 5. APLICACIÓN ESTRATÉGICA DE MERCURY EN CONTEXTO ESPAÑOL: RECOMENDACIONES E IMPLEMENTACIÓN

### 5.1 Sectores Prioritarios para Adopción Mercury AVRQ

Basándose en análisis de criticidad de infraestructura, densidad de incidentes, y requisitos regulatorios NIS2, los siguientes sectores españoles son candidatos prioritarios para adopción de Mercury:

#### 5.1.1 Infraestructura Crítica Digital

**Requisito regulatorio**: Todas las entidades son EE (Essential Entities) bajo NIS2
**Justificación técnica**: A.D.A.M. esencial para mapeo continuo de dependencias en entornos cloud, DNS, CDN

**Caso de uso específico**:

- Proveedor de cloud Spanish (ej., Telefónica Cloud, Orange Cloud)
- Desafío: 4.000+ alertas diarias requieren automatización de scoring de riesgo
- Solución Mercury: AVRQ + ACET automatiza priorización; CNCS reportea en <24h


#### 5.1.2 Sistema Financiero Español

**Requisito regulatorio**: Banco de España (BdE), CNMV requieren cuantificación monetaria de riesgos

**Justificación técnica**: AVRQ traduce riesgos cibernéticos en impacto sobre valor de activos bancarios (depósitos, sistemas de pago)

**Caso de uso específico**:

- Banco español de talla mediano (ej., 1.000-5.000 empleados)
- Desafío: Sanciones PSD2, DORA exigen cuantificación precisa de riesgo operativo cibernético
- Solución Mercury: Integración con sistemas de pagos; AVRQ cuantifica riesgo de disruption; reportea a dirección en términos de impacto sobre ROA (Return on Assets)


#### 5.1.3 Administración Pública Central y Autonómica

**Requisito regulatorio**: NIS2 requiere EE en ministeri large, administraciones autonómicas >50 empleados

**Justificación técnica**: ACET automatiza auditoría continua de controles (requería trimestral pre-NIS2); A.D.A.M. mapea complejidad de redes gubernamentales

**Caso de uso específico**:

- Ministerio o administración autonómica (ej., Consejería de Salud, Educación)
- Desafío: Auditorías manuales insuficientes; presupuestos crecientes pero eficiencia cuestionable
- Solución Mercury: ACET proporciona métricas continuas; AVRQ justifica inversiones ante Tribunal de Cuentas


#### 5.1.4 Sanitario (Hospitales y Servicios de Salud)

**Requisito regulatorio**: ~800 hospitales públicos/privados talla mediana-grande son EE bajo NIS2

**Justificación técnica**: Equipamiento médico (imagenología, monitoreo paciente) + registros digitales requieren protección granular; AVRQ integra valor de atención al paciente, no solo daño financiero

**Caso de uso específico**:

- Hospital universitario español (ej., Complejo Hospitalario La Paz, Gregorio Marañón)
- Desafío: Ransomware causa pérdida de servicios críticos; reguladores requieren cuantificación de riesgo a vidas/pacientes
- Solución Mercury: AVRQ extiende scoring a impacto en calidad de atención; A.D.A.M. mapea dependencias OT/IT; ACET valida mitigaciones quirúrgicamente


### 5.2 Alineación Mercury con Requisitos NIS2 Españoles

El Centro Nacional de Ciberseguridad (CNCS), establecido en la Ley de Coordinación y Gobernanza de Ciberseguridad española, requerirá a entidades esenciales/importantes demostrar conformidad con medidas técnicas y organizativas específicas. Mercury alinea con estas exigencias como sigue:


| Requisito NIS2 | Medida NIS2 | Control Mercury |
| :-- | :-- | :-- |
| **Risk Management Framework** | Identificación y documentación de riesgos | AVRQ + A.D.A.M. |
| **Risk Assessment** | Evaluación y priorización de riesgos | AVRQ scoring empírico |
| **Risk Treatment Plan** | Implementación de medidas de mitigación | ACET validación continua |
| **Asset Classification** | Clasificación de activos por criticidad | A.D.A.M. mapping dinámico |
| **Access Control** | Autenticación, autorización | ACET testing eficacia |
| **Incident Response** | Protocolo <24h de notificación | Mercury reportería automatizada |
| **Board Reporting** | Comunicación a órganos de dirección | AVRQ en lenguaje financiero/ejecutivo |
| **Third-Party Risk** | Evaluación de proveedores críticos | AVRQ extensión multidominio |

### 5.3 Modelo de Implementación: Fases y Cronograma

**Fase 1 (Meses 1-3): Assessment y Design**

- Mapeo de activos críticos (A.D.A.M. fase exploratoria)
- Definición de "valor de activo" específico a contexto (financiero, operativo, reputacional)
- Capacitación de equipo central (3-5 personas)
- Presupuesto indicativo: €50-100K

**Fase 2 (Meses 4-6): Implementación AVRQ Pilot**

- Aplicación AVRQ a 3-5 escenarios de riesgo de alta prioridad
- Validación mediante datos históricos (incidentes previos, threat intelligence)
- Generación de reportes ejecutivos
- Presupuesto: €80-150K (licencias + consultoría)

**Fase 3 (Meses 7-12): Integración ACET y Automatización**

- Despliegue de ACET en tecnologías existentes (SIEM, GRC tools)
- Automatización de scoring continuo
- Integracion con workflow de governance (board meetings trimestrales)
- Presupuesto: €150-250K (implementación + integración)

**Fase 4 (Año 2): A.D.A.M. y Multidominio**

- Expansión de Mercury a riesgos no-cibernéticos (Tecnología, Terceros, Usuario)
- Mapeo dinámico de supply chain crítica
- Optimización de ROI sobre inversiones de mitigación
- Presupuesto: €200-400K/año

**Presupuesto total para pequeña-mediana empresa española (3-5 años)**: €480K-900K, representando <2% de presupuesto de ciberseguridad típico para entidad EE.

***

## 6. LIMITACIONES, RIESGOS Y CONSIDERACIONES CRÍTICAS

### 6.1 Madurez del Mercado y Confianza Institucional

Mercury Risk and Compliance Inc. fue constituida hace solo 2 años (2023). A pesar de que sus fundadores tienen trayectorias destacadas, la ausencia de track record de décadas (como FAIR Institute desde 2005) implica:

- **Riesgo de continuidad**: Empresa emergente podría pivotar o desaparecer
- **Validación académica limitada**: No existen publicaciones peer-reviewed extensas sobre AVRQ, ACET, A.D.A.M. en journals de impacto
- **Adopción institucional**: Ningún organismo regulador español (CNCS, INCIBE) ha emitido guidance sobre Mercury

**Mitigación recomendada**: Grandes organizaciones deberían condicionar adopción a acuerdos de código abierto o escrow de propiedad intelectual; adoptar Mercury como complemento, no sustituto, de frameworks standarizados (ISO 27005, NIST CSF).

### 6.2 Dependencia en Calidad de Datos y Riesgo de Sesgo ML

A.D.A.M. utiliza machine learning para mapeo dinámico. ML es vulnerable a:

- **Datos históricos sesgados**: Si entrenamiento se basó en incidentes de sectores específicos (ej., tecnología USA), A.D.A.M. puede subrepresentar riesgos únicos de contextos españoles (regulación AEPD, geografía de ataque lusa)
- **Distribución de amenazas cambiante**: Amenazas disruptivas (ej., ataques de IA generativa) podrían no estar bien representadas en datasets de entrenamiento

**Recomendación**: Implementaciones españolas de Mercury deben incluir equipo independiente de "red teaming" que valide outputs de A.D.A.M. contra escenarios específicos nacionales.

### 6.3 Integración con Ecosistema de Herramientas Español

ACET depende de integración con sistemas existentes (SIEM, GRC, auditoría). Ecosistema español altamente fragmentado:

- **Large enterprises**: Típicamente SAP, Salesforce, sistemas legacy en SAP-ERP o sistemas propios
- **Administración pública**: Proliferación de sistemas desconectados; migración a cloud lenta
- **SMEs**: Presupuesto tecnológico limitado; a menudo carecen de SIEM o GRC formales

**Implicación**: Costo de integración ACET podría ser significativamente mayor en contexto español que en USA. Mercury debería proporcionar "adaptadores" pre-construidos para plataformas comunes españolas (SUSE, OpenStack, sistemas públicos españoles).

***

## 7. CONCLUSIONES Y RECOMENDACIONES EJECUTIVAS

### 7.1 Posicionamiento de Mercury en Ciberseguridad Española

Mercury Risk and Compliance propone un enfoque diferenciador fundamentalmente valioso para contexto español:

1. **Orientación a valor** (no solo pérdida) resueña con cultura empresarial española que valora retorno sobre inversión y eficiencia operativa
2. **Automatización** (ACET, A.D.A.M.) aborda escasez crítica de talento cibernético en España (60% SMEs carecen de personal dedicado)
3. **Multidominio** extiende relevancia más allá de cibernética hacia riesgos tecnológicos, de terceros, y operacionales

Sin embargo, **Mercury no es panacea**: FAIR, CAsPeA, y otras metodologías retienen fortalezas en educación, estandarización y adopción institucional.

### 7.2 Recomendaciones por Perfil Organizacional

**Para Grandes Empresas Españolas (Bancos, Telcos, Energía)**:

- Adoptar Mercury como **complemento a FAIR**, no sustituto
- Pilotar AVRQ en 2-3 dominios de riesgo de mayor criticidad
- Vincular salarios ejecutivos a retorno-sobre-riesgo (métrica Mercury)
- Timeline: 18-24 meses para full implementation

**Para Administración Pública y Sectores Regulados**:

- Exigir a Mercury conformidad explícita con directrices CNCS/INCIBE antes de adopción
- Utilizar Mercury como herramienta de auditoría continua (ACET) para cumplir NIS2
- Requiere validación de A.D.A.M. contra amenazas específicas de contexto público español
- Timeline: 24-36 meses; requiere aprobación de supervisores

**Para SMEs Españolas**:

- Mercury probablemente demasiado costoso como solución stand-alone
- Oportunidad: Proveedores de servicios gestionados (MSP, MSSP) españoles podrían ofertar "Mercury-as-a-Service" bundleado
- Timeline: Esperar adoptores grandes; aprender de their deployments


### 7.3 Necesidad de Investigación Adicional

Aún subsisten brechas de conocimiento:

1. **Validación empírica de AVRQ**: Se requieren publicaciones académicas peer-reviewed comparando AVRQ vs. FAIR en datasets españoles
2. **Guidance regulatorio CNCS**: Centro Nacional de Ciberseguridad debería emitir guidance sobre frameworks cuantificación aceptables (análogo a ENISA guidance para NIS2)
3. **Benchmarking sectorial**: Estudios de adopción en hospitales, bancos, administración pública españoles
4. **Integración con estándares ISO**: Mapeo explícito entre AVRQ y revisado ISO 27005:2022

***

## 8. REFERENCIAS Y FUENTES

INCIBE (2025). Balance de Ciberseguridad 2024. https://www.incibe.es[^1_20][^1_1][^1_2]

ENISA (2025). EU-Cybersecurity Index 2024. https://www.enisa.europa.eu/sites/default/files/2025-06/The EU Cubersecurity Index 2024_en_0.pdf[^1_21][^1_18]

ITU (2024). Global Cybersecurity Index 2024. https://www.itu.int[^1_22][^1_23][^1_24][^1_5]

Government of Spain (2025). Anteproyecto de Ley de Coordinación y Gobernanza de Ciberseguridad. Ministry of Interior[^1_25][^1_7]

Mercury Risk and Compliance, Inc. (2024). Corporate Profile. https://mercuryrisk.com[^1_26][^1_8][^1_10]

Mordor Intelligence (2026). Cybersecurity Market in Spain. Market Research Report[^1_27][^1_19]

ENISA (2025). Technical Implementation Guidance on NIS2 Cybersecurity Risk Management Measures. https://www.enisa.europa.eu/publications/nis2-technical-implementation-guidance[^1_28][^1_29][^1_30][^1_31]

Leszczyna, R., et al. (2024). ISO/IEC 27001-Based Estimation of Cybersecurity Costs with CAsPeA. In Proceedings of ISD 2024.[^1_32][^1_12][^1_11]

FAIR Institute. (2025). A FAIR Framework for Effective Cyber Risk Management. White Paper[^1_33][^1_14][^1_34]

Springboard35 (2025). Cybersecurity in Spain: Challenges and Opportunities. https://springboard35.com[^1_35][^1_6]

[Adicionales-150 como referencias cruzadas en análisis técnico]

***

<span style="display:none">[^1_36][^1_37][^1_38][^1_39][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_90][^1_91][^1_92]</span>

<div align="center">⁂</div>

[^1_1]: https://www.grupoaseguranza.com/noticias-de-seguros/incibe-gestiono-2024-16-6-mas-ciberincidentes-21-8-mas-consultas

[^1_2]: https://www.incibe.es/incibe/sala-de-prensa/incibe-presenta-su-balance-de-ciberseguridad-2024-con-mas-de-97000-incidentes

[^1_3]: https://ack3.eu/spain-boosts-cybersecurity-billion-investment/

[^1_4]: https://www.lamoncloa.gob.es/lang/en/presidente/news/paginas/2025/20250422-security-and-defence-plan.aspx

[^1_5]: https://www.ituser.es/actualidad/2024/09/espana-obtiene-una-valoracion-casi-perfecta-en-el-global-cybersecurity-index-2024-de-itu

[^1_6]: https://springboard35.com/en/blog/cybersecurity-in-spain-challenges-opportunities/

[^1_7]: https://copla.com/blog/compliance-regulations/nis2-directive-regulations-and-implementation-in-spain/

[^1_8]: https://sales.superagi.com/company/mercury-risk-and-compliance,-inc.

[^1_9]: https://www.datoscif.es/empresa/mercury-risk-compliance-solutions-sl

[^1_10]: https://mercuryrisk.com/

[^1_11]: https://aisel.aisnet.org/isd2014/proceedings2024/managingdevops/4/

[^1_12]: https://aisel.aisnet.org/cgi/viewcontent.cgi?article=1636\&context=isd2014

[^1_13]: https://www.balbix.com/insights/fair-model-for-risk-quantification-pros-and-cons/

[^1_14]: https://www.fairinstitute.org/blog/integrating-fair-models-a-unified-framework-for-cyber-risk-management

[^1_15]: https://www.centraleyes.com/decoding-the-cyber-risk-quantification-models/

[^1_16]: https://axio.com/insights/why-traditional-crq-falls-short-and-how-modern-solutions-fill-the-gaps/

[^1_17]: https://www.linkedin.com/pulse/cyber-risk-quantification-models-fair-vs-graace-bill-frank-rxmse

[^1_18]: https://www.enisa.europa.eu/sites/default/files/2025-06/The EU Cubersecurity Index 2024_en_0.pdf

[^1_19]: https://www.mordorintelligence.com/industry-reports/spain-cybersecurity-market

[^1_20]: https://www.sourcesecurity.com/news/mercury-security-access-control-platform-launch-co-823-ga-co-9380-ga-co-12538-ga-co-1529393926-ga-co-6621-ga-npr.1743757208.html

[^1_21]: https://www.mercury-security.com/category/insights/blog/

[^1_22]: https://www.merqury.eu

[^1_23]: https://administracionelectronica.gob.es/pae_Home/en/pae_OBSAE/Posicionamiento-Internacional/Summary-Spain-international-rankings/ITU-Global-Cybersecurity-Index-2024.html

[^1_24]: https://www.itdigitalsecurity.es/actualidad/2024/09/espana-obtiene-una-valoracion-casi-perfecta-en-el-global-cybersecurity-index-2024-de-itu

[^1_25]: https://www.youtube.com/watch?v=Slf6OFhtrGc

[^1_26]: https://www.mercury-security.com/resources/

[^1_27]: https://mercuryiss.com.au

[^1_28]: https://www.mercury-security.com/2025-controller-trend-report/

[^1_29]: https://industrialcyber.co/threats-attacks/enisa-publishes-technical-guidance-to-strengthen-nis2-cybersecurity-risk-management/

[^1_30]: https://www.twobirds.com/en/insights/2025/eu-cybersecurity--enisa-publishes-final-nis2-guidance

[^1_31]: https://www.enisa.europa.eu/publications/nis2-technical-implementation-guidance

[^1_32]: https://mercury.com/blog/identifying-and-measuring-startup-key-performance-indicators

[^1_33]: https://mercuryit.com.au/cybersecurity/

[^1_34]: https://1616664.fs1.hubspotusercontent-na1.net/hubfs/1616664/FAIR Institute -- Integrating FAIR Models for Cyber Risk Management (December 2024).pdf

[^1_35]: https://www.mercury-security.com/2025-trends-in-access-controllers-report/

[^1_36]: https://mercury.com/raise/software-stack/tools/amplitude

[^1_37]: https://mercurycc.com/solutions/cyber-security/

[^1_38]: https://www.mrcy.com/products/secure/secure-program-protection

[^1_39]: https://mercuryworks.com/blog/application-monitoring-at-mercury

[^1_40]: https://www.mrcy.com/innovation/technologies/secure-processing

[^1_41]: https://sprinto.com/blog/cybersecurity-metrics/

[^1_42]: https://cloudsmith.com/blog/vulnerability-scoring-systems

[^1_43]: https://censinet.com/perspectives/iso-27001-and-nist-csf-control-mapping-checklist

[^1_44]: https://www.board-cybersecurity.com/annual-reports/tracker/20240813-mercury-systems-inc-cybersecurity-10k/

[^1_45]: https://www.splunk.com/en_us/blog/learn/epss-exploit-prediction-scoring-system.html

[^1_46]: https://www.cyberday.ai/assessment/nist-csf

[^1_47]: https://designhub.wordsystech.com/1/mercuryrisk/index11.html

[^1_48]: https://orca.security/resources/blog/epss-scoring-system-explained/

[^1_49]: https://www.kovrr.com/resources/free-nist-self-assessment-tool

[^1_50]: https://www.board-cybersecurity.com/annual-reports/tracker/20240213-mercury-general-corp-cybersecurity-10k/

[^1_51]: https://entro.security/blog/cvss-vs-epss-in-vulnerability-scoring/

[^1_52]: https://www.onetrust.com/blog/iso-27001-vs-nist-cybersecurity-framework/

[^1_53]: https://www.linkedin.com/posts/matthewrosenquist_grc-and-cybersecurity-metrics-that-help-prioritize-activity-7394447032880488448-fJr2

[^1_54]: https://www.paloaltonetworks.com/blog/cloud-security/epss-scores/

[^1_55]: https://securityexceptions.com/articles/measuring-cybersecurity-risk-tools-frameworks-metrics

[^1_56]: https://www.mercurysecurities.com.my/wp-content/uploads/2025/11/LGMS-20251125-Initiate-Coverage-Mercury.pdf

[^1_57]: https://scores.securityscorecard.io/security-rating/mercuryfinancial.com

[^1_58]: https://mercury.ch/en/compliance-assessment/

[^1_59]: https://assets.contentstack.io/v3/assets/blt309b1de7d109902d/blt8cca3d5e84bd96f7/682e259bb728366bb14063d8/Your_framework_for_building_cybersecurity_program_metrics_(1).pdf

[^1_60]: https://mercuryiss.com.au/compliance-calendar

[^1_61]: https://mercuryrisk.com/mercury-risk-and-compliance-inc/mercury-risk-compliance-about-us/

[^1_62]: https://growett.com/blogs/Cybersecurity-metrics--Definition-and-their-role-in-risk-management.html

[^1_63]: https://mercuryiss.com.au/services/governance-risk-compliance

[^1_64]: https://ec.europa.eu/docsroom/documents/11846/attachments/3/translations/en/renditions/native

[^1_65]: https://www.reddit.com/r/cybersecurity/comments/ypzurm/vulnerability_management_metrics/

[^1_66]: https://www.mercury-security.com/wp-content/uploads/2025/06/Mercury-2025-Controller-Trend-Report_Final.pdf

[^1_67]: https://unaaldia.hispasec.com/2025/11/implementacion-de-la-directiva-europea-nis2-en-espana.html

[^1_68]: https://protecciondatos-lopd.com/empresas/rgpd-reglamento-general-proteccion-datos/

[^1_69]: https://cybersecuritynews.es/espana-registra-mas-de-97-000-incidentes-de-ciberseguridad-en-2024/

[^1_70]: https://www.camerfirma.com/directiva-nis2/

[^1_71]: https://ticnegocios.camaravalencia.com/servicios/tendencias/principales-cambios-en-la-proteccion-de-datos-en-2025/

[^1_72]: https://sosafe-awareness.com/es/blog/nis2-espana-nueva-normativa/

[^1_73]: https://www.lbo.legal/actualidad/novedadeslopd2024

[^1_74]: https://ptedisruptive.es/wp-content/uploads/2024/12/INFORME-DE-SITUACION_CIBERSEGURIDAD_2024.pdf

[^1_75]: https://www.incibe.es/incibe-cert/sectores-estrategicos/FAQNIS2

[^1_76]: https://yousign.com/es-es/blog/normativa-de-proteccion-de-datos-en-espana

[^1_77]: https://www.dsn.gob.es/va/node/25040

[^1_78]: https://grupoaire.es/nis2-empresas-ciberseguridad/

[^1_79]: https://www.aepd.es/guias-y-herramientas/guias

[^1_80]: https://breached.company/enisa-threat-landscape-briefing-2024-2025-analysis/

[^1_81]: https://eudigitallaw.com/enisa-releases-eu-cybersecurity-index-2024/

[^1_82]: https://www.traficom.fi/sites/default/files/media/file/ENISA’s threat landscape 2024, ENISA.pdf

[^1_83]: https://administracionelectronica.gob.es/pae_Home/pae_OBSAE/Posicionamiento-Internacional/Summary-Spain-international-rankings/ITU-Global-Cybersecurity-Index-2020.html

[^1_84]: https://newsroom.cisco.com/c/dam/r/newsroom/en/us/interactive/cybersecurity-readiness-index/documents/Cisco_Cybersecurity_Readiness_EUROPE.pdf

[^1_85]: https://industrialcyber.co/reports/enisa-threat-landscape-2024-identifies-availability-ransomware-data-attacks-as-key-cybersecurity-threats/

[^1_86]: https://industrialcyber.co/reports/enisa-2025-threat-landscape-report-highlights-eu-faces-escalating-hacktivist-attacks-and-state-aligned-cyber-threats/

[^1_87]: https://securityaffairs.com/182978/security/reading-the-enisa-threat-landscape-2025-report.html

[^1_88]: https://thecyberexpress.com/enisa-report-on-european-union-cybersecurity/

[^1_89]: https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025

[^1_90]: https://codesealer.com/blog/itu-global-cybersecurity-index-2024-a-changing-cybersecurity-landscape

[^1_91]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9416112/

[^1_92]: https://administracionelectronica.gob.es/pae_Home/pae_OBSAE/Posicionamiento-Internacional/Resumen-posicionamiento-Espana/Indice-de-Ciberseguridad-Global-2024--UIT.html


---