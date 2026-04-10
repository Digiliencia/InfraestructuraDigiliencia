# Informe MSS: Indicadores y Métricas de Servicios de Seguridad Gestionados
## Marco Comparativo Mundial y Aplicación Territorial en España (2025–2026)

***

> *"Quien no mide, no gestiona; quien no gestiona, solo espera."*
> — Paráfrasis libre del canon actuarial, ahora con urgencia de CISO.

***

## Resumen Ejecutivo

Los Servicios de Seguridad Gestionados (MSS, por sus siglas en inglés) han pasado, en apenas un lustro, de ser un commodity tecnológico para grandes corporaciones a convertirse en infraestructura crítica nacional. En 2025, su definición formal fue consagrada en el Reglamento (UE) 2025/37, que los integra en el marco del Cybersecurity Act europeo, y la Comisión Europea encargó a la Agencia de Ciberseguridad de la UE (ENISA) el desarrollo de un esquema de certificación europeo específico (EUMSS). Al mismo tiempo, España aprobó una inversión histórica de 1.157 millones de euros en ciberseguridad, gestionó 122.223 incidentes de ciberseguridad en 2025 — un 26% más que el año anterior — y puso en marcha el andamiaje legislativo para crear su Centro Nacional de Ciberseguridad (CNCS).[^1][^2][^3][^4][^5]

Este informe investiga exhaustivamente el estado del arte de los indicadores y métricas del marco MSS desde 2025, con foco en la aplicación territorial española y perspectiva comparativa mundial. Se estructura en diez capítulos que abarcan desde el ecosistema regulatorio hasta la criptografía postcuántica, pasando por la taxonomía de indicadores operativos, la soberanía digital y los modelos de madurez SOC.

***

## 1. Marco Conceptual y Regulatorio: Qué Son los MSS y Por Qué Importan Sus Métricas

### 1.1 Definición Formal y Alcance Normativo

La definición vigente de MSS, según el Reglamento (UE) 2025/37 (en vigor desde el 4 de febrero de 2025), es precisa y cargada de consecuencias regulatorias:

> *"Servicio prestado a terceros que consiste en llevar a cabo o asistir en actividades de gestión de riesgos de ciberseguridad, como gestión de incidentes, pruebas de penetración, auditorías de seguridad y consultoría, incluido asesoramiento experto y apoyo técnico."*[^1]

Esta definición no es meramente académica. El mismo Reglamento clasifica a los proveedores de MSS como entidades esenciales o importantes bajo la Directiva NIS2, lo que implica un régimen de supervisión activa, notificación obligatoria de incidentes y, eventualmente, certificación obligatoria en el contexto de la Reserva de Ciberseguridad de la UE. En términos prácticos, medir el rendimiento de un MSSP ya no es opcional: es un requisito regulatorio en formación.[^4]

La taxonomía de servicios MSS identificada por ENISA en su análisis de mercado de junio 2025 articula tres grandes familias:[^1]

**Servicios técnicos y de soluciones de seguridad:**
- Gestión de identidad y acceso (IAM), incluida la gestión de privilegios
- Seguridad de datos gestionada (DLP, backup, continuidad de negocio)
- Gestión de seguridad de endpoints (antivirus, parcheo, cifrado de dispositivos)
- Seguridad perimetral de red (IDS/IPS, firewalls, SASE)
- Detección y respuesta gestionadas (MDR/SIEM, threat hunting, ingeniería inversa)
- Evaluación técnica (escaneo de vulnerabilidades, pentesting)
- Gestión de amenazas (CTI, compartición de inteligencia)
- Seguridad cloud gestionada

**Servicios de consultoría y despliegue:**
- Evaluación de conformidad
- Auditoría e informes
- Gestión de riesgos
- Desarrollo de simulaciones y ejercicios
- Evaluaciones de madurez y políticas
- Despliegue e integración

**Servicios de formación:**
- Ejercicios de simulación (tabletop, red team/blue team)
- Formación y concienciación del personal

Esta arquitectura de servicios es el lienzo sobre el que se pintan los indicadores. Un MSSP que no mide no puede demostrar que ninguno de esos servicios produce valor. Y un cliente que no exige métricas está, efectivamente, comprando fe.

### 1.2 El Problema Central de las Métricas en MSS: La Brecha Demanda-Oferta

El análisis de mercado de ENISA 2025 revela una tensión estructural que conviene nombrar desde el principio: la demanda de personalización de métricas y SLAs supera con creces lo que la oferta está dispuesta a conceder. El 86% de las organizaciones del lado demanda exigen personalización de SLAs adaptada a sus necesidades operativas, frente al 59% de proveedores que la ofrecen. Más revelador aún: solo el 24% de la demanda logra negociar la selección y parametrización de métricas específicas en sus SLAs, y del lado oferta, ese porcentaje cae a cero estadístico.[^1]

Esta asimetría no es técnica, sino estratégica: los MSSPs, en su mayoría, prefieren los dashboards estandarizados — manejables, escalables y, convenientemente, difíciles de comparar. La certificación EUMSS en desarrollo por ENISA apunta precisamente a romper este oligopolio de la opacidad métrica.

***

## 2. El Ecosistema de Indicadores MSS: Taxonomía y Arquitectura

### 2.1 Los Indicadores Temporales Fundamentales (Time-Based KPIs)

Los indicadores basados en tiempo constituyen el núcleo duro de cualquier contrato MSS y son los primeros que aparecen en los SLAs, las auditorías y las reclamaciones de indemnización. Son, metafóricamente, el electrocardiograma de la salud del servicio:

| Indicador | Acrónimo | Definición Operativa | Relevancia MSS |
|-----------|----------|----------------------|----------------|
| Tiempo Medio de Detección | MTTD | Tiempo promedio desde el inicio de la actividad maliciosa hasta su identificación[^6] | Mide eficacia del motor de detección y cobertura de telemetría |
| Tiempo Medio de Reconocimiento | MTTA | Tiempo desde la creación de la alerta hasta que un analista la gestiona[^6] | Evalúa dotación y workflows del SOC |
| Tiempo Medio de Contención | MTTC | Tiempo desde la detección hasta el aislamiento efectivo de la amenaza[^7] | Crítico para limitar el "blast radius" de ransomware |
| Tiempo Medio de Respuesta/Recuperación | MTTR | Tiempo hasta la remediación completa y retorno seguro a operaciones[^6] | Mide la completitud del ciclo de respuesta |

La fórmula canónica del MTTD es:

\[ \text{MTTD} = \frac{\sum (\text{Tiempo de Detección} - \text{Tiempo de Compromiso})}{\text{Número de Incidentes}} \]

[^8]

Un MTTD elevado es, en la práctica, un subsidio invisible al atacante. CrowdStrike documentó en 2025 que los atacantes comprometían un sistema en un promedio de 48 minutos desde el acceso inicial, lo que convierte cualquier MTTD medido en días en una invitación a una catástrofe. Microsoft, con Security Copilot integrado en Defender XDR, reportó una reducción del 40% en MTTR y un recorte del 60% en falsos positivos, mientras que Cortex XSIAM de Palo Alto Networks procesa 1 billón de eventos diarios para exponer rutas de ataque ocultas.[^9][^10]

### 2.2 Indicadores de Visibilidad y Cobertura

Más allá del tiempo de reacción, los indicadores de cobertura responden a la pregunta que los CISOs más temen formular en voz alta: *¿Qué porcentaje de nuestra infraestructura está realmente monitorizado?*

- **Asset Coverage Ratio (ACR):** Proporción del patrimonio digital incluido en cada ciclo de escaneo o monitorización continua. Un ACR inferior al 90% en entornos críticos es una bandera roja en cualquier auditoría ENS de categoría ALTA.[^11]
- **Scan Coverage Rate:** Porcentaje de activos incluidos en cada ciclo de análisis de vulnerabilidades.[^11]
- **Exploitability Coverage:** Proporción de vulnerabilidades activamente explotables que han sido remediadas.[^11]
- **Critical Vulnerability Exposure (CVE%):** Porcentaje de vulnerabilidades de alto riesgo que permanecen abiertas dentro de los plazos SLA.[^11]
- **Porcentaje de endpoints sin protección activa:** Indicador de brechas en la gestión del parque de dispositivos.[^12]

INCIBE detectó de forma proactiva 237.028 sistemas vulnerables relevantes en España en 2025, lo que ilustra la magnitud del problema de cobertura a escala nacional. Un dato que, convenientemente, ningún cuadro de mandos corporativo había capturado antes de que INCIBE lo hiciera por ellos.[^2]

### 2.3 Indicadores de Gestión de Incidentes y Calidad del Servicio

| Indicador | Descripción | Benchmarking |
|-----------|-------------|--------------|
| Tasa de Falsos Positivos | Proporción de alertas que resultan no ser incidentes reales[^12][^11] | <5% es excelencia; >20% indica fatiga de analistas |
| Tasa de Falsos Negativos | Amenazas que escapan a la detección[^13] | Difícil de medir; requiere ejercicios red team periódicos |
| Vulnerability Reopen Rate | Porcentaje de vulnerabilidades que reaparecen tras remediación[^11] | Indica calidad de los procesos de corrección |
| Downtime per Incident | Tiempo de indisponibilidad operativa por incidente[^14] | Relevante especialmente en entornos OT/ICS |
| Losses Accrued vs. Losses Prevented | Ratio entre daños materializados y ataques bloqueados[^14] | Indicador de ROI de seguridad |
| Incident-Free Operational Periods | Períodos sin incidentes significativos[^13] | Indicador de madurez preventiva |

### 2.4 Indicadores de Cumplimiento y Gobernanza

La convergencia regulatoria de 2025 (NIS2, DORA, ENS actualizado, Cyber Resilience Act) ha elevado los indicadores de conformidad de la categoría de "buenas prácticas" a "condición sine qua non" de supervivencia empresarial:

- **Compliance Score por Framework:** Porcentaje de controles implementados sobre el total aplicable. Fórmula: \[ CS = \frac{\text{Controles Implementados}}{\text{Controles Aplicables Totales}} \times 100 \][^15]
  - Para ISO 27001: benchmarks de excelencia sitúan el umbral en ≥92% de controles implementados.[^15]
  - Para ENS categoría MEDIA/ALTA: auditoría externa obligatoria cada 2 años (ENAC acreditada).[^16]
- **Remediation Cycle Time para Auditorías:** Tiempo transcurrido entre la identificación de una no conformidad y su cierre documentado.[^17]
- **Management Training Completion Rate:** Porcentaje de directivos que han completado formación en ciberseguridad (obligatorio bajo NIS2 Art. 20).[^18]
- **Supplier Security Assessment Coverage:** Porcentaje de proveedores críticos con evaluación de seguridad documentada y periódica.[^19][^20]

Bajo NIS2, la cadena de suministro se convierte en indicador de primer orden: el 38% de las vulnerabilidades identificadas en cadenas de suministro reguladas provienen de proveedores críticos, y los incumplimientos exponen a multas de hasta 10 millones de euros o el 2% de la facturación global anual.[^20][^18]

### 2.5 Indicadores Financiero-Actuariales: El Lenguaje del Consejo de Administración

Ningún indicador técnico sobrevive al primer comité de dirección si no viene acompañado de su traducción económica. Los indicadores financieros de MSS articulan el riesgo en el idioma universal del dinero:

- **Coste por Incidente (CPI):** Suma de costes directos (respuesta, recuperación, multas) e indirectos (reputación, continuidad de negocio) por incidente.[^8]
- **ROSI (Return on Security Investment):** \[ \text{ROSI} = \frac{\text{Pérdidas Esperadas Evitadas} - \text{Coste del Control}}{\text{Coste del Control}} \times 100 \]
- **Prima de Ciberseguro:** Indicador de mercado que refleja la percepción externa del riesgo de una organización. En España, las primas del mercado de ciberseguros crecieron un 12% en 2025, alcanzando 190 millones de euros, con una proyección de crecimiento del mercado desde 268,3 millones USD en 2025 hasta 1.221,5 millones USD en 2034 (CAGR 18,34%).[^21][^22]
- **Ratio de Mejora en Controles Críticos:** AON documenta una mejora interanual del 5% en los controles críticos de ciberseguridad entre sus clientes en 2025.[^23]
- **Reducción de Precios de Ciberseguro:** -7% de media en Q1 2025, señal de madurez del mercado aunque también de mayor competencia aseguradora.[^23]

El modelo actuarial aplicado al ciberriesgo es, paradójicamente, el más honesto de todos los marcos de medición: convierte la incertidumbre en probabilidad, la probabilidad en prima y la prima en incentivo para mejorar controles. La Casualty Actuarial Society (CAS) publicó en junio de 2025 un marco de cuantificación de ciberriesgo que complementa las métricas operativas con modelos probabilísticos para escenarios de estrés.[^24]

***

## 3. Los Cinco Pilares del Marco de Métricas MSS para 2025

A partir de la síntesis de frameworks internacionales (NIST CSF 2.0, ISO/IEC 27004, ENISA MSS Market Analysis 2025, CIS Controls v8, ENS), se propone una arquitectura de cinco pilares para la medición integral de MSS:

### Pilar I — Visibilidad del Riesgo y Exposición a Amenazas

Responde a la pregunta: *¿Cuán expuestos estamos?*

- Índice de Exposición a Vulnerabilidades (número de CVEs críticas sin parche / total activos)
- Cobertura de monitorización de superficie de ataque (%)
- Edad media de vulnerabilidades críticas no remediadas (días)
- Puntuación de riesgo de terceros (supplier risk score)
- Indicador de madurez de inteligencia de amenazas (CTI maturity)

La adopción de ISO/IEC 27004 (monitorización, medición y evaluación de SGSI) es una señal de madurez que ENISA registra en el 92% de los proveedores y en el 53% de los clientes MSS encuestados en 2025.[^1]

### Pilar II — Efectividad Operativa

Responde a la pregunta: *¿Funcionan nuestros controles cuando los necesitamos?*

- MTTD, MTTA, MTTC, MTTR (el cuarteto temporal de referencia)[^6]
- False Positive Rate (FPR) y False Negative Rate (FNR)
- Alert Escalation Accuracy (porcentaje de alertas escaladas correctamente)
- First Time Fix Rate en respuesta a incidentes
- Coverage y telemetría de endpoints y activos en la nube
- Incident Closure Rate dentro de SLA

### Pilar III — Gobernanza y Cumplimiento

Responde a la pregunta: *¿Cumplimos con lo que prometemos y con lo que exige la ley?*

- Compliance Score por framework regulatorio (NIS2/ENS/DORA/ISO 27001)
- Audit Pass Rate (porcentaje de controles que superan auditoría interna/externa)[^7]
- Unremediated High-Risk Findings (vulnerabilidades críticas fuera de plazo SLA)[^7]
- Management Accountability Index (formación directiva obligatoria NIS2)
- Supplier Assessment Coverage Rate (% proveedores críticos evaluados)[^20]
- SLA Achievement Rate por tipo de servicio MSS

### Pilar IV — Impacto Financiero y Actuarial

Responde a la pregunta: *¿Cuánto nos cuesta y cuánto nos ahorra la seguridad?*

- Coste Total por Incidente (CPI, desglosado por tipología)
- ROSI (Return on Security Investment)
- Prima de ciberseguro como proxy de riesgo percibido
- Índice de Variación de Prima YoY (mejora o deterioro del perfil de riesgo)
- Pérdidas Evitadas vs. Pérdidas Materializadas (ratio de prevención)
- Cyber Risk Quantification (CRQ) score — indicador emergente en entornos OT[^14]

### Pilar V — Alineación Estratégica y Madurez

Responde a la pregunta: *¿Estamos mejorando sistemáticamente y en la dirección correcta?*

- Índice de Madurez SOC (CMM-SOC, niveles 1-5)[^25]
- Security Incident Management Maturity (SIM3 de Open CSIRT Foundation)[^26]
- NPS/CSAT del servicio MSS (satisfacción del cliente)
- Proactive Prevention vs. Reactive Response Ratio[^13]
- Digital Resilience Score (indicador compuesto de continuidad de negocio)
- Onboarding Time (tiempo de incorporación de nuevas entidades al servicio MSS)

***

## 4. Modelos de Madurez SOC y MSS: De la Reactividad a la Autonomía Cognitiva

### 4.1 El Modelo CMM Aplicado a SOC y MSS

El Capability Maturity Model (CMM), adaptado a entornos SOC, define cinco niveles de madurez cuya progresión marca la diferencia entre un MSS que reacciona y uno que anticipa:[^25]

| Nivel | Denominación | Características Operativas | Indicadores Típicos |
|-------|-------------|---------------------------|---------------------|
| 1 | Inicial | Procesos ad hoc, dependientes de individuos | MTTD: días-semanas; sin SLAs formales |
| 2 | Gestionado | Monitorización básica, respuesta a incidentes elementales | MTTD: horas; SLAs simples definidos |
| 3 | Definido | Procesos estandarizados, SIEM integrado, playbooks[^25] | MTTD: <1h; compliance score >80% |
| 4 | Gestionado Cuantitativamente | Analítica avanzada, automatización, threat hunting[^25] | MTTD: <15min; falsos positivos <5% |
| 5 | Optimizado | IA-driven, threat hunting proactivo, mejora continua[^25] | MTTD: <5min; ROSI documentado positivo |

El SOC-CMM (Rob van Os) y el SIM3 (Open CSIRT Foundation) son los modelos de evaluación más citados en entornos académicos y regulatorios europeos. La Red Nacional de SOC española, gestionada por el CCN-CERT con nodos en las Comunidades Autónomas, aspira a operar en nivel 4 para infraestructuras críticas como horizonte del Plan de Inversión 2025.[^27][^28][^26]

### 4.2 La Irrupción de la IA: Del SOC Gestionado al SOC Autónomo

2025 marcó el punto de inflexión en el que la IA generativa dejó de ser un argumento de marketing para convertirse en un diferencial medible. Los indicadores de adopción de IA en entornos MSS incluyen:

- **Reducción de Falsos Positivos inducida por IA:** Microsoft documenta -60% con Security Copilot/Defender XDR.[^9]
- **Reducción de MTTR inducida por IA:** -40% en el mismo entorno.[^9]
- **Volumen de eventos procesados por IA:** Cortex XSIAM (Palo Alto) procesa 1 billón de eventos diarios para identificar rutas de ataque ocultas.[^9]
- **Tasa de automatización de playbooks:** Porcentaje de incidentes resueltos sin intervención humana.
- **Analyst Augmentation Rate:** Reducción de necesidades de personal humano por automatización (indicador estratégico ante la crisis de talento).

En el reverso oscuro de la moneda, los atacantes también han adoptado la IA con resultados estadísticamente elocuentes: el fraude basado en IA creció un 1.210% en 2025, los ataques deepfake aumentaron un 880%, y el 82% de los hackers ya utiliza IA en sus flujos de trabajo. Esto convierte la detección de ataques asistidos por IA en un indicador MSS emergente que los marcos actuales todavía no capturan adecuadamente.[^29]

***

## 5. Aplicación Territorial en España: Diagnóstico Nacional 2025

### 5.1 El Panorama Cuantitativo de la Amenaza

El Balance de Ciberseguridad 2025 de INCIBE, publicado en febrero de 2026, es el documento de referencia para la calibración de indicadores MSS en contexto español. Sus cifras merecen lectura detenida:[^30]

| Indicador Nacional | Valor 2025 | Variación vs. 2024 |
|-------------------|------------|---------------------|
| Incidentes totales gestionados | 122.223[^2] | +26% |
| Sistemas vulnerables detectados proactivamente | 237.028[^2] | — |
| Incidentes en operadores esenciales (NIS2) | 401[^2] | — |
| Casos de malware | 55.411[^2] | — |
| Ataques de ransomware | 392[^2] | — |
| Fraude online | 45.445[^31] | — |
| Phishing | 25.133[^31] | — |
| Dispositivos IoT en botnets | 85% del total[^2] | — |
| Robo de información | 3.849 casos[^2] | — |
| Dominios .es fraudulentos cerrados | 4.600[^2] | — |
| Consultas a Línea 017 | 142.767[^2] | +44,9% |

El incremento del 26% en incidentes no debe interpretarse exclusivamente como mayor actividad delictiva. INCIBE señala que también refleja una mayor capacidad de detección, notificación y coordinación institucional. Esta distinción es epistemológicamente importante para los indicadores MSS: la mejora en la capacidad de detección incrementa el numerador de los incidentes reportados antes de mejorar el denominador del daño real.[^30]

### 5.2 Sectores Críticos y Concentración del Riesgo

Los operadores esenciales más afectados en España bajo el paraguas NIS2 son:[^32][^2]
- **Banca:** 34% de los incidentes en operadores esenciales
- **Transporte:** 14%
- **Energía:** 8%
- **Infraestructuras de los mercados financieros:** 7%
- **Aseguradoras y fondos de pensiones:** 6%

El informe Aon 2025 sobre ciberseguridad en España confirma que banca y energía actúan como "locomotoras de madurez" en la gestión del riesgo ciber, mientras que agro y logística se sitúan en el extremo menos maduro del espectro. Esta heterogeneidad sectorial es un dato crítico para el diseño de indicadores MSS territorializados: los benchmarks de MTTD para el sector bancario no son trasladables a una cooperativa agrícola del Valle del Ebro.[^22]

### 5.3 El Marco Regulatorio Nacional: Capas, Tensiones y Oportunidades

España opera simultáneamente bajo cuatro capas regulatorias que generan tanto sinergias como fricciones en el ecosistema MSS:

**Esquema Nacional de Seguridad (ENS, RD 311/2022):** El marco de referencia para la Administración Pública y sus proveedores tecnológicos. Clasifica los sistemas en tres categorías (básica, media, alta) con requisitos de medidas y auditoría diferenciados. Las auditorías externas (ENAC acreditadas) son obligatorias para sistemas de categoría MEDIA y ALTA cada dos años. El ENS es, en la práctica, el primer marco de métricas MSS para el sector público español.[^33][^16]

**Directiva NIS2 (transposición en curso):** El anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad fue aprobado por el Consejo de Ministros el 14 de enero de 2025 y se encuentra pendiente de tramitación parlamentaria. Crea el CNCS como autoridad única, amplía el ámbito de aplicación a más de 5.700 entidades con residencia fiscal o actividad en España, e impone plazos de notificación de incidentes de 24h (alerta inicial), 72h (notificación) y 1 mes (informe completo).[^34][^35][^18]

**DORA (Digital Operational Resilience Act):** En vigor desde enero 2025 para el sector financiero. Introduce métricas específicas de resiliencia operativa digital, incluyendo pruebas de penetración basadas en amenazas (TLPT) y gestión del riesgo de terceros con aplicación directa a los MSSPs.[^36]

**Regulación sectorial sectorial (GDPR, ENS Sanitario, etc.):** La Estrategia de Ciberseguridad del Sistema Nacional de Salud 2025-2028, aprobada en noviembre de 2025, introduce 8 objetivos estratégicos y 12 ejes de actuación específicos para el sector sanitario, incluyendo la creación de una red nacional de colaboración sobre ciberincidentes.[^37]

### 5.4 Arquitectura Institucional: El SOC Nacional y la Red Distribuida

La arquitectura institucional española de ciberseguridad para MSS se articula en tres niveles:[^38][^27]

1. **Nivel Estratégico-Central:** Centro Nacional de Ciberseguridad (CNCS, en creación), CCN-CERT (Administración Pública y defensa), INCIBE-CERT (sector privado y ciudadanía).
2. **Nivel Operativo Nacional:** Centro de Operaciones de Ciberseguridad (COCS) — desplegado en el marco de España Digital —, que provee SIEM centralizado, sensores, threat hunting y servicios de ticketing para entidades adscritas a la Red SARA.[^38]
3. **Nivel Regional Distribuido:** SOC regionales en las Comunidades Autónomas (especialmente Madrid, Cataluña, Andalucía y País Vasco son mencionados como los más avanzados), integrados en la Red Nacional de SOC del CCN-CERT.[^27]

El Plan de Inversión de 1.157 millones de euros aprobado en mayo de 2025 articula este modelo distribuido, con el objetivo de "proteger información y servicios, especialmente infraestructuras críticas". El 5G SOC —financiado en 2025— monitoriza los slices de red transfronterizos y comparte telemetría de anomalías con ENISA, convirtiendo a España en un nodo activo del espacio de información de ciberseguridad europeo.[^5][^39][^40]

***

## 6. Perspectiva Comparativa Mundial: España en el Ecosistema Global MSS

### 6.1 El Mercado Global MSS en 2025: Escala, Concentración y Dinámica

El mercado global de MSS presenta en 2025 estimaciones divergentes según la metodología de segmentación utilizada, pero todas apuntan a una dinámica de crecimiento sostenido y acelerado:

| Fuente | Valor 2025 | Proyección | CAGR |
|--------|------------|-----------|------|
| Mordor Intelligence[^9] | USD 38,31 Mrd | USD 69,16 Mrd | ~12,5% |
| Fortune Business Insights[^41] | USD 19,04 Mrd | USD 50,17 Mrd (2034) | 11,50% |
| Revista Ciberseguridad[^42] | USD 67 Mrd | — | — |

Las divergencias reflejan diferencias en la definición del perímetro del mercado (algunos modelos incluyen MDR autónomo, otros solo MSSP tradicional). Lo que no está en disputa es la dirección: el mercado se expande estructuralmente impulsado por la confluencia de escasez de talento, complejidad normativa creciente y sofisticación de las amenazas.

América del Norte domina con una cuota del 44,40% en 2025, mientras que Europa —con la entrada en vigor del Reglamento 2025/37 y la Directiva NIS2 como catalizadores regulatorios— protagoniza la expansión más dinámica. Los drivers de crecimiento en el mercado global según Mordor Intelligence 2025 son:[^41][^9]

- Mandatos de cumplimiento DORA/NIS2/SEC: +2,3% al CAGR
- Automatización SOC con IA y adopción XDR: +2,1%
- Crisis de talento impulsando MSS co-gestionado: +1,9%
- Expansión de superficie de ataque multi-nube: +1,8%
- Precios basados en uso y bundling MDR: +1,2%
- Urgencia de cifrado resistente a cuántica: +0,9%

### 6.2 La Paradoja de la Soberanía Digital: Quién Gestiona la Seguridad de Europa

Uno de los hallazgos más perturbadores del análisis de mercado MSS de ENISA 2025 merece destacarse en negrita y subrayarse con tinta de alarma: **el 51% de los proveedores MSS que operan en Europa están bajo control de entidades no europeas**, a pesar de tener sede en la UE. Solo el 38% son compañías genuinamente controladas desde Europa.[^43][^44]

Las implicaciones para los indicadores MSS son inmediatas y profundas:
- Las cadenas de suministro de los propios MSSPs no han sido investigadas en el análisis ENISA 2025, constituyendo un "punto ciego" sistémico.[^43]
- La dependencia de infraestructura, software y herramientas de proveedores no-UE introduce vectores de riesgo geopolítico que los indicadores técnicos convencionales no capturan.
- La diversidad del mercado proveedor implica que los requisitos de certificación EUMSS en desarrollo podrán, potencialmente, nivelar el campo y favorecer la oferta europea de mayor confianza.

Para España, con su posición estratégica como hub potencial de ciberseguridad europeo — ancla de cables submarinos hacia Senegal y Brasil, posición de interconexión entre Europa, África y Latinoamérica — esta dinámica plantea una tensión entre apertura comercial y soberanía digital que el CNCS deberá gestionar con indicadores específicos de dependencia tecnológica extracomunitaria.[^45][^40]

### 6.3 Tendencias Globales con Impacto Directo en los Indicadores MSS (2025-2026)

**Zero Trust + XDR como nueva línea base:** La convergencia de Zero Trust (arquitectura de confianza cero, sin perímetro implícito) con XDR (Extended Detection and Response, visibilidad unificada de endpoints, red, identidad y cloud) está redefiniendo los indicadores operativos de los MSS. Los indicadores relevantes incluyen: tasa de autenticación sin contraseña (passwordless), contextualization score de alertas, número de movimientos laterales detectados por análisis de comportamiento.[^46][^47]

**MDR como estándar emergente:** La transición de los MSS tradicionales (monitorización de logs, gestión de firewall) hacia MDR (Managed Detection and Response) implica un cambio cualitativo en los indicadores: del "cuántos eventos procesamos" al "cuántas amenazas reales contenemos". El 30% de los MSPs prevé un crecimiento superior al 20% en 2025, liderado por la adopción de MDR.[^48][^49][^47]

**Supply Chain Security como indicador de primer orden:** Los ataques a la cadena de suministro digital representan una de las amenazas de mayor crecimiento según ENISA Threat Landscape 2025. Los indicadores de seguridad de proveedores — cobertura de evaluación, tiempo de respuesta ante vulnerabilidades de terceros, tasa de cumplimiento contractual de seguridad — son ahora exigibles bajo NIS2 para las entidades esenciales.[^50][^51][^19]

**Ransomware como termómetro financiero:** A pesar de un descenso del 11% en 2025, el ransomware sigue siendo la amenaza de mayor impacto económico. Los indicadores de exposición al ransomware — porcentaje de sistemas sin MFA, tiempo de remediación de vulnerabilidades explotadas activamente (KEV de CISA), frecuencia de backups verificados — son esenciales en cualquier scorecard MSS.[^52]

***

## 7. Criptografía Postcuántica y Resiliencia Digital: El Horizonte 2026-2030

### 7.1 La Amenaza "Harvest Now, Decrypt Later" como Indicador de Urgencia

La criptografía postcuántica (PQC) ha pasado en 2025 de ser una preocupación futurista a una prioridad estratégica con plazos regulatorios concretos. El NIST publicó en agosto 2024 los tres primeros estándares de algoritmos PQC (ML-KEM/CRYSTALS-Kyber, ML-DSA y SLH-DSA), y su adopción se convierte en indicador de madurez para organizaciones que gestionan datos con horizontes de confidencialidad a largo plazo.[^53][^54]

La amenaza "harvest now, decrypt later" — donde adversarios recopilan datos cifrados hoy para descifrarlos cuando dispongan de capacidad cuántica suficiente — afecta especialmente a sectores con datos de larga vida: banca, defensa, salud y administraciones públicas. Los MSSPs que no incorporan métricas de preparación PQC están, literalmente, midiendo la seguridad de hoy con la mentalidad de hace una década.[^54][^55]

Los indicadores MSS emergentes de preparación postcuántica incluyen:[^56][^53][^54]
- **Crypto-Agility Score:** Proporción de sistemas que pueden actualizar algoritmos criptográficos sin rediseño arquitectónico.
- **PQC Readiness Index:** Porcentaje de sistemas de comunicación críticos migrados a algoritmos NIST PQC.
- **Quantum-Vulnerable Asset Inventory:** Número de activos con criptografía clásica vulnerable (RSA, ECC) que gestionan datos sensibles a largo plazo.
- **Long-Lived Data Exposure Score:** Volumen de datos con horizonte de confidencialidad >10 años protegidos exclusivamente con criptografía pre-cuántica.

En España, la Estrategia Española de Tecnologías Cuánticas 2025-2030 y el proyecto Quantum Spain articulan el camino hacia la transición postcuántica en sectores críticos. El Centro Nacional de Ciberseguridad en creación deberá incorporar indicadores PQC en su marco de supervisión.[^57][^58]

***

## 8. Los Indicadores del Esquema de Certificación EUMSS: La Arquitectura en Construcción

### 8.1 El Proceso de Certificación EUMSS y su Impacto Prospectivo

La Comisión Europea solicitó formalmente a ENISA en abril de 2025 la preparación de un esquema candidato de certificación europeo para MSS (EUMSS). ENISA estableció un Grupo de Trabajo Ad Hoc (AHWG) para su desarrollo. Este esquema, cuando esté operativo, definirá de facto los indicadores mínimos exigibles a los MSSPs que operen en Europa.[^59][^60][^4]

La arquitectura conceptual del EUMSS prevé dos dimensiones:[^4]
1. **Capa horizontal:** Requisitos mínimos aplicables a todos los MSS, independientemente del tipo específico de servicio.
2. **Capas verticales:** Requisitos técnicos específicos agrupados por tipo de MSS.

El primer vertical en desarrollo se centra en el **Ciclo de Vida de la Gestión de Incidentes**, comenzando por el Perfil de Servicio de Respuesta a Incidentes. Los proveedores bajo la Reserva de Ciberseguridad de la UE deberán certificarse dos años después de que el esquema esté en vigor.[^4]

Las implicaciones para los indicadores MSS son directas: el esquema EUMSS establecerá qué métricas deben ser monitorizadas, reportadas y auditadas de forma homogénea en todos los Estados miembros, eliminando la fragmentación actual que dificulta la comparabilidad y favorece la opacidad.

### 8.2 ECSMAF V3.0: La Metodología de Observatorio Permanente

ENISA publicó en marzo de 2026 la versión 3.0 del ENISA Cybersecurity Market Analysis Framework (ECSMAF), desarrollado conjuntamente con la Università Bocconi. Esta actualización es metodológicamente relevante para los indicadores MSS porque:[^61][^62]

- Incorpora soporte para **análisis recurrente y monitorización continua** del mercado, habilitando comparaciones interanuales de indicadores.[^61]
- Diseña un **modelo federado** donde los estados miembros realizan análisis locales con la misma metodología, y los resultados se agregan a escala UE.[^61]
- Incluye 17 anexos con plantillas de encuesta para cuatro tipos de stakeholders (demanda, oferta, reguladores, I+D).[^61]
- Aspira a constituir un **observatorio de mercado permanente** para MSS.[^61]

Para España, la adopción del ECSMAF V3.0 como marco de análisis del mercado nacional MSS permitiría al futuro CNCS disponer de datos comparables con el resto de Estados miembros y contribuir al análisis agregado europeo.

***

## 9. Brechas, Desafíos y Áreas de Investigación Prioritaria

### 9.1 Las Brechas Identificadas en el Ecosistema MSS de Indicadores

El análisis comparativo de las fuentes disponibles revela cuatro brechas estructurales que los indicadores actuales no resuelven adecuadamente:

**Brecha 1 — Métricas de Calidad de Mercado MSS:** ENISA identifica la necesidad de desarrollar "métricas de calidad de mercado" para la vigilancia de los MSS. Los indicadores actuales miden el rendimiento de servicios individuales pero no la calidad sistémica del mercado proveedor (concentración, dependencia tecnológica, resiliencia del ecosistema).[^1]

**Brecha 2 — Indicadores de Madurez para PYMEs:** El análisis ENISA 2025 constata que las organizaciones de menor tamaño están estructuralmente subrepresentadas tanto en la oferta como en la demanda de MSS. La ausencia de indicadores adaptados a PYMEs — que representan el 99% del tejido empresarial español — crea un "punto ciego" de gobernanza. El 85% de las PYMEs españolas reportaron al menos un ataque en 2023, pero sus capacidades de medición son mínimas.[^42][^1]

**Brecha 3 — Indicadores de Seguridad Operacional (OT/ICS):** Los entornos industriales (energía, agua, manufactura) requieren una extensión específica de los indicadores MSS que incorpore la métrica de "downtime operativo por incidente" y la distinción entre sistemas IT y OT. La convergencia IT/OT es una de las tendencias más significativas y menos instrumentadas en el ecosistema español.[^14]

**Brecha 4 — Indicadores de Dependencia Tecnológica Extracomunitaria:** Como se ha señalado, el 51% del mercado MSS europeo está bajo control no-UE, pero no existe todavía un marco de indicadores que cuantifique el riesgo sistémico de esta dependencia. La certificación EUMSS debería incluir indicadores de "provenance" tecnológica como parte de su capa horizontal.[^43]

### 9.2 El Paisaje de Amenazas como Calibrador de Indicadores

El ENISA Threat Landscape 2025 — basado en 4.875 incidentes analizados entre julio 2024 y junio 2025 — ofrece el contexto operativo en el que deben calibrarse los indicadores MSS:[^63]

- **DDoS: 77% de los incidentes reportados** (motivación ideológica dominante: 79,4% de ataques)[^64][^52]
- **Sector público (administraciones): 38% de los objetivos principales**[^64]
- **Phishing: 60% de vectores iniciales de intrusión**[^65]
- **Explotación de vulnerabilidades: 21%**[^65]
- **Ransomware: -11%, pero sigue siendo la amenaza de mayor impacto económico**[^52]
- **Grupos APT28, APT29, Sandworm: los más activos en la UE**[^52]

Esta distribución implica que los indicadores MSS deben ponderar la detección de ataques DDoS volumétricos como métrica primaria para administraciones públicas, mientras que para el sector financiero el foco es el ransomware y el fraude online. La universalización de indicadores sin contextualización sectorial produce cuadros de mando que impresionan en las presentaciones al Consejo y explican poco en la post-mortem de un incidente.

***

## 10. Recomendaciones para la Implementación de Indicadores MSS en Contexto Español

### 10.1 Marco de Implementación por Nivel de Madurez Organizacional

El diseño de un sistema de indicadores MSS para España debe asumir la heterogeneidad radical del ecosistema organizacional:

**Para organizaciones en niveles de madurez 1-2 (Inicial/Gestionado):**
- Comenzar con el cuarteto temporal esencial: MTTD, MTTC, MTTR, FPR[^6]
- Establecer Asset Inventory completo como prerequisito (no se puede medir lo que no se conoce)
- Adoptar compliance score ENS/NIS2 como indicador de gobernanza mínimo
- Objetivo MTTD razonable: <24h en el primer año, <4h en el segundo

**Para organizaciones en niveles 3-4 (Definido/Gestionado Cuantitativamente):**
- Incorporar indicadores de cobertura: ACR, Scan Coverage, Exploitability Coverage[^11]
- Desarrollar ROSI como indicador de justificación presupuestaria
- Implementar Supplier Security Assessment Coverage (NIS2 obligatorio)[^19]
- Monitorizar indicadores de detección de amenazas IA-asistidas

**Para organizaciones en nivel 5 (Optimizado) e infraestructuras críticas:**
- Sistema completo de cinco pilares (Sección 3)
- Crypto-Agility Score y PQC Readiness Index[^53]
- Cyber Risk Quantification (CRQ) con modelos actuariales[^24]
- Integración de indicadores en la Red Nacional de SOC del CCN-CERT[^27]

### 10.2 Principios para el Diseño de SLAs MSS con Indicadores Robustos

Los principios siguientes derivan de la síntesis de las mejores prácticas internacionales identificadas:[^13][^6][^14][^11]

1. **Especificidad contextual:** Los indicadores deben reflejar el sector y el perfil de amenaza del cliente, no ser genéricos. Un SLA bancario no es un SLA logístico.
2. **Verificabilidad independiente:** El cliente debe poder auditar los indicadores sin depender exclusivamente de los datos del proveedor. La certificación EUMSS aspira a operacionalizar este principio.
3. **Orientación a resultados:** Priorizar indicadores de impacto (pérdidas evitadas, tiempo de indisponibilidad, incidentes contenidos) sobre indicadores de actividad (número de alertas procesadas, tickets cerrados).
4. **Gradualidad regulatoria:** Los SLAs deben incorporar cláusulas de escalado automático de requisitos conforme madure la transposición de NIS2 y entre en vigor la certificación EUMSS.
5. **Revisión periódica documentada:** Los indicadores obsoletos son peores que la ausencia de indicadores: generan falsa confianza. La revisión trimestral de la relevancia de los KPIs es una buena práctica en todos los frameworks consultados.[^66][^15]

***

## Conclusión: Medir para Existir, Existir para Resistir

Los indicadores del marco MSS en 2025-2026 no son un ejercicio burocrático de cumplimiento ni un adorno estadístico para presentaciones corporativas. Son el sistema nervioso de una estrategia de ciberseguridad que, en el contexto español y europeo, ha asumido sin ambigüedades su condición de asunto de Estado.

España enfrenta este momento con activos significativos: una inversión histórica de 1.157 millones de euros, un ecosistema institucional articulado alrededor del futuro CNCS, INCIBE y CCN-CERT, una posición geográfica estratégica como hub entre Europa y el mundo hispanohablante, y una experiencia acumulada de 122.223 incidentes gestionados en 2025 que, aunque dolorosa, constituye un activo de inteligencia operativa difícilmente replicable.[^3][^40][^2][^5][^27]

Los desafíos son igualmente reales: la transposición tardía de NIS2 (con más de 16 meses de retraso), la dependencia de proveedores MSS extracomunitarios que controlan el 51% del mercado europeo, la brecha de talento que afecta transversalmente a todo el ecosistema, y la emergencia de superficies de ataque radicalmente nuevas — IA generativa, computación cuántica, entornos OT conectados — que los marcos de indicadores actuales todavía no capturan de forma adecuada.[^35][^43]

La certificación EUMSS en desarrollo por ENISA, el ECSMAF V3.0 como metodología de observatorio permanente, y la Estrategia Nacional de Ciberseguridad en proceso de elaboración son los tres vectores que, en los próximos dos a tres años, definirán el paisaje de indicadores MSS para España y Europa. Participar activamente en su diseño no es opcional para un país que aspira a ser hub de ciberseguridad europeo: es la condición de posibilidad de esa aspiración.[^67][^4][^61]

Medir con rigor es, al final, la única forma honesta de afirmar que se está seguro. Todo lo demás es, como diría cualquier actuario de temperamento literario, una póliza sin prima y sin cláusula de cobertura.

***

*Fuentes primarias consultadas: ENISA MSS Market Analysis (junio 2025); ENISA ECSMAF V3.0 (marzo 2026); ENISA Threat Landscape 2025 (octubre 2025); Balance de Ciberseguridad 2025 INCIBE (febrero 2026); Informe Aon Ciberseguridad y Riesgo Ciber España 2025; Plan de Inversión en Ciberseguridad del Gobierno de España (mayo 2025); Reglamento (UE) 2025/37; Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad (enero 2025); Estrategia de Ciberseguridad SNS 2025-2028; DenexusIO OT MSSP Performance Metrics (diciembre 2025); CAS Research Paper on Cyber Risk (junio 2025).*

---

## References

1. [[PDF] MSS Market Analysis - ENISA](https://www.enisa.europa.eu/sites/default/files/2025-06/ENISA_MSS_Market_Analysis_en_0.pdf) - Regulation (EU) 2025/37 (4) adds the following definition of MSS to the Cybersecurity Act. (CSA): a ...

2. [INCIBE detectó más de 122.000 incidentes de ciberseguridad en 2025](https://www.incibe.es/incibe/sala-de-prensa/incibe-detecto-mas-de-122000-incidentes-de-ciberseguridad-en-2025) - INCIBE detectó más de 122.000 incidentes de ciberseguridad en 2025 · Banca: 34% · Transporte: 14% · ...

3. [The NIS2 draft in Spain enters the approval stage | Sngular](https://www.sngular.com/insights/352/nis2-directive-the-draft-law-in-spain-enters-the-approval-phase) - On January 14, the Council of Ministers of the Government of Spain approved the draft bill on the Co...

4. [EU Managed Security Services Certification to drive ... - ENISA](https://www.enisa.europa.eu/news/eu-managed-security-services-certification-to-drive-the-cybersecurity-market) - ENISA: Every day we experience the Information Society. Interconnected networks touch our everyday l...

5. [El Gobierno aprueba un plan de 1.157 millones para reforzar la ciberseguridad](https://elpais.com/espana/2025-05-06/el-gobierno-aprueba-un-plan-de-1157-millones-para-reforzar-la-ciberseguridad.html) - España sufrió más de 100.000 ciberataques el año pasado, uno grave cada tres días, el 70% contra adm...

6. [OT MSSP Metrics: 3 Performance KPI Types for Industrial Security](https://blog.denexus.io/resources/ot-mssp-performance-metrics) - Learn the 3 OT MSSP metric types—external, internal, and customer-facing—with examples (MTTD/MTTR, c...

7. [Find a Bank with the Best Cybersecurity Practices - Huntress](https://www.huntress.com/cybersecurity-for-financial-institutions-guide/banks-with-the-best-cybersecurity) - The Zero Trust framework assumes that the network is already compromised and implements segmentation...

8. [30 Cybersecurity Metrics & KPIs Every Company Must Track in 2025](https://securityboulevard.com/2025/05/30-cybersecurity-metrics-kpis-every-company-must-track-in-2025/) - These include risk visibility, operational effectiveness, governance and compliance, financial impac...

9. [Tamaño del Mercado de Servicios de Seguridad Gestionados ...](https://www.mordorintelligence.com/es/industry-reports/security-managed-services-market) - El tamaño del mercado de servicios de seguridad gestionados se sitúa en USD 38,31 mil millones en 20...

10. [NIS2 Directive Spain: Cybersecurity Requirements 2025 | Flexxible](https://www.flexxible.com/en/blog/nis2-directive-spain) - The regulation was approved in 2022 and came into force in Spain on October 17, 2024, initiating its...

11. [MSSP Vulnerability Management KPIs and SLAs Overview](https://www.indusface.com/blog/mssp-vulnerability-management-kpis-slas/) - Overview of key KPIs and SLAs for MSSP vulnerability management, ensuring effective risk tracking, t...

12. [Métricas y KPI de ciberseguridad: qué hay que supervisar en 2025](https://www.sentinelone.com/es/cybersecurity-101/cybersecurity/cybersecurity-metrics/) - Las métricas de ciberseguridad miden la postura de seguridad de una organización mediante la medició...

13. [MSP Security KPIs That Matter: Beyond Vanity Metrics to Business ...](https://www.todyl.com/blog/msp-security-kpis-business-outcomes-metrics) - Transform client relationships with business outcome metrics. Move beyond vanity metrics to KPIs tha...

14. [OT MSSP Metrics: 3 Performance KPI Types for Industrial Security](https://blog.denexus.io/resources/ot-mssp-performance-metrics?hs_amp=true) - Learn the 3 OT MSSP metric types—external, internal, and customer-facing—with examples (MTTD/MTTR, c...

15. [30 Cybersecurity Metrics & KPIs Every Company Must Track in 2025](https://strobes.co/blog/30-cybersecurity-metrics-kpis/) - Cybersecurity is no longer an IT issue but a board-level priority. You are working on blind spots if...

16. [ENS Esquema Nacional de Seguridad - DNV](https://www.dnv.es/services/ens-esquema-nacional-de-seguridad-227674/) - La realización de auditorías de seguridad es obligatoria en los sistemas de información que tengan l...

17. [ISO 27001:2022 KPI Metrics - cyberatos.com](https://cyberatos.com/gallery/ISO%20270012022%20KPI%20Metrics.pdf)

18. [NIS2 Directive in Spain: obligations, deadlines and penalties for ...](https://www.delbion.com/en/insights/nis2-spain-business-obligations/) - The NIS2 directive affects thousands of businesses in Spain. We explain your obligations, transposit...

19. [NIS2 compliance in manufacturing: how to secure your supply chain ...](https://www.suppliershield.com/es/post/nis2-compliance-in-manufacturing-how-to-secure-your-supply-chain-and-meet-eu-requirements) - Discover how manufacturers can achieve NIS2 compliance, secure their supply chains, and reduce third...

20. [NIS2: Understanding the Obligations of Critical Suppliers - Aprovall](https://www.aprovall.com/en/blog/nis2-the-obligations-of-critical-suppliers/) - Understand NIS2 obligations for critical suppliers and learn how to assess, map, and monitor third p...

21. [Spain Cyber Insurance Market Size, Share, Growth, Trends 2034](https://www.imarcgroup.com/spain-cyber-insurance-market) - The Spain cyber insurance market grew from USD 268.3 Million in 2025 to a projected USD 1221.5 Milli...

22. [El volumen de primas de seguros Ciber en España se incrementa un 12% alcanzando los 190 millones de euros](https://www.europapress.es/comunicados/sociedad-00909/noticia-comunicado-volumen-primas-seguros-ciber-espana-incrementa-12-alcanzando-190-millones-euros-20250721163623.html) - Madrid, 21 de julio de 2025.- Aon plc (NYSE: AON), empresa global líder en servicios profesionales, ...

23. [Aon Cyber 2025 Spain (EMEA)](https://www.aon.com/cyber-risk-report/es-es)

24. [[PDF] cas research paper - cyber risk: quantification, stress scenarios ...](https://www.casact.org/sites/default/files/2025-06/CAS_Research_Paper-on_Cyber-Risk-Final.pdf) - Founded in 1914, the CAS is the world's only actuarial organization focused exclusively on property-...

25. [What Are The Challenges...](https://www.manageengine.com/log-management/cyber-security/soc/soc-maturity-model-cmm-model.html) - ManageEngine Log360!

26. [Understanding and Using Maturity Models in SOCs - SOCCER - AGH](https://soccer.agh.edu.pl/en/detail/understanding-and-using-maturity-models-in-socs-a-look-at-chapter-2-of-the-toolbox) - Serwis AGH

27. [[PDF] Informe Ciberseguridad 2025 | PTE Disruptive](https://ptedisruptive.es/wp-content/uploads/2025/12/Informe-Ciberseguridad-2025.pdf) - El CCN-CERT, dependiente del Centro Criptológico Nacional, mantiene su papel de coordinación naciona...

28. [SOC-CMM](https://www.soc-cmm.com) - The SOC-CMM is a capability maturity model and self-assessment tool for Security Operations Centers ...

29. [AI Cybersecurity Statistics 2026 (Q1+Q2) - CyberSecStats](https://www.cybersecstats.com/ai-cybersecurity-statistics-2026-q1-q2/) - AI fraud surged 1,210% in 2025 (Pindrop). Non-AI fraud increased by 195% by the end of 2025 (Pindrop...

30. [Balance de Ciberseguridad 2025 de INCIBE - Elantia](https://elantia.es/balance-de-ciberseguridad-2025-de-incibe/) - Durante 2025 se gestionaron 122.223 incidentes de ciberseguridad, lo que supone un incremento del 26...

31. [INCIBE gestionó más de 122.000 incidentes de ciberseguridad en ...](https://agers.es/incibe-gestiono-mas-de-122-000-incidentes-de-ciberseguridad-en-2025-un-26-mas-que-el-ano-anterior/) - INCIBE gestionó más de 122.000 incidentes de ciberseguridad en 2025, un 26% más que el año anterior ...

32. [INCIBE gestionó 122.223 incidentes de ciberseguridad en 2025, un ...](http://espanadigital.gob.es/ca/actualidad/incibe-gestiono-122223-incidentes-de-ciberseguridad-en-2025-un-26-mas-que-el-ano) - INCIBE gestionó 122.223 incidentes de ciberseguridad en 2025, un 26% más que el año anterior · Malwa...

33. [Niveles del Esquema Nacional de Seguridad: Guía 2026 - Audidat](https://www.audidat.com/blog/esquema-nacional-de-seguridad/niveles-esquema-nacional-seguridad/) - Nivel medio: gestión de riesgos en servicios con impacto moderado. Nivel alto: protección máxima par...

34. [NIS2 Spain Transposition: Status, Requirements, and Roadmap](https://copla.com/blog/compliance-regulations/nis2-directive-regulations-and-implementation-in-spain/) - Deadline for Member States to transpose NIS2 into national law. Spanish Draft Approval, 14 January 2...

35. [NIS2 España: qué exige la ley de ciberseguridad a las empresas](https://digitalperito.es/blog/ley-ciberseguridad-nis2-espana-2026-obligaciones-empresas/) - Guía completa sobre la Directiva NIS2 en España. Qué empresas están obligadas, sanciones hasta 10M€,...

36. [Ciberseguridad 2025 en España: amenazas, regulación, casos y ...](https://techconsulting.es/ciberseguridad-2025-en-espana-amenazas-regulacion-casos-y-estrategias-clave/) - El 2025 está definiendo un escenario de ciberamenazas sin precedentes para las empresas españolas: a...

37. [Aprobada la Estrategia de Ciberseguridad del Sistema Nacional de ...](https://cetic.es/estrategia-de-ciberseguridad-del-sistema-nacional-de-salud/) - Aprobada la Estrategia de Ciberseguridad del Sistema Nacional de Salud 2025-2028 · Crear una red nac...

38. [Despliegue y Operación del Centro de ... - España Digital](http://espanadigital.gob.es/medida/despliegue-y-operacion-del-centro-de-operaciones-de-ciberseguridad-cocs) - Asimismo, el Centro Criptológico Nacional (CCN-CERT) pone a disposición su capacidad de operación de...

39. [El Gobierno aprueba un refuerzo de las capacidades de España en ...](https://digital.gob.es/comunicacion/notas-prensa/mtdfp/2025/05/2025-05-06_02)

40. [Cybersecurity Market in Spain - Size, Share & Industry Analysis](https://www.mordorintelligence.com/industry-reports/spain-cybersecurity-market) - The Spain cybersecurity market size was valued at USD 4.57 billion in 2025 and estimated to grow fro...

41. [Tamaño del mercado de servicios gestionados de seguridad ...](https://www.fortunebusinessinsights.com/es/cyber-security-managed-services-market-106883) - Se prevé que el tamaño del mercado mundial de servicios gestionados de ciberseguridad crezca de 21.0...

42. [Los servicios de seguridad gestionados (MSS) crecerán hasta los ...](https://www.revistaciberseguridad.com/2025/02/los-servicios-de-seguridad-gestionados-mss-creceran-hasta-los-67-mil-millones-en-2025/) - Los servicios de seguridad gestionados (MSS) crecerán hasta los $67 mil millones en 2025 · Inversion...

43. [European MSS Market: ENISA's Comprehensive Analysis Reveals ...](https://www.security.land/european-mss-market-enisas-comprehensive-analysis-reveals-critical-gaps-and-emerging-trends/) - ENISA's groundbreaking 2025 market analysis exposes significant vulnerabilities in Europe's digital ...

44. [[PDF] MSS Market Analysis - ENISA - European Union](https://www.enisa.europa.eu/sites/default/files/2025-06/ENISA_MSS_Market_Analysis_en_2.pdf) - Non-EU enterprises have a limited presence, particularly in compliance assessment and risk managemen...

45. [[PDF] españa, hub de ciberseguridad europeo - DSN GOB](https://www.dsn.gob.es/sites/default/files/2025-04/ESPA%C3%91A,%20HUB%20DE%20CIBERSEGURIDAD%20EUROPEO.pdf) - El documento “España, Hub de Ciberseguridad Europeo” elaborado por el Foro Nacional de. Cibersegurid...

46. [Zero Trust Framework Trends for 2025 - Cyber Advisors Blog](https://blog.cyberadvisors.com/zero-trust-framework-trends-for-2025) - Explore Zero Trust trends for 2025, from AI-driven automation to self-healing networks, and why ente...

47. [Managed Security Services (MSS) - A Global Market Overview](https://techmarketexperts.com/managed-security-services-mss-market) - Top trends include the rise of Managed Detection and Response (MDR), adoption of cloud-native securi...

48. [El 30% de los MSP prevé un crecimiento superior al 20% para 2025](https://www.watchguard.com/es/wgrd-news/blog/el-30-de-los-msp-preve-un-crecimiento-superior-al-20-para-2025-0) - Crecimiento de los servicios de TI gestionados y ciberseguridad: Los ingresos de los servicios gesti...

49. [La importancia de los MSS en un 2025 amenazante](https://www.computerweekly.com/es/cronica/La-importancia-de-los-MSS-en-un-2025-amenazante) - “Algo que vemos fuerte es la tendencia a la adopción de servicios como MDR (Managed ... Servicios de...

50. [Key Trends from the ENISA Threat Landscape 2025 - GECAD](https://www.gecad.isep.ipp.pt/pc2phish/en/panorama-de-ameacas-ciberneticas-europeias-principais-tendencias-do-enisa-threat-landscape-2025-eng/) - Drawing on thousands of reported incidents across multiple countries, the document identifies emergi...

51. [Ultimate NIS2 Directive Compliance Guide for 2025](https://gauss.hr/en/blog/nis2-compliance-guide) - NIS2 aims to strengthen security requirements, tackle supply chain vulnerabilities, make reporting p...

52. [Key Findings from ENISA Threat Landscape 2025 Report - HEIC](https://heic.eu/key-findings-from-enisa-threat-landscape-2025-report/) - The data is unambiguous: a staggering 79.4% of attacks were ideology-driven, completely dwarfing the...

53. [Tendencias clave para 2025 Parte I: Criptografía postcuántica](https://www.sectigo.com/es/blog/criptografia-postcuantica-tendencias-2025) - Descubre las tendencias 2025 en criptografía postcuántica, incluyendo HSM seguros y algoritmos estan...

54. [Las principales tendencias en criptografía post-cuántica para 2025](https://www.revistaciberseguridad.com/2025/02/las-principales-tendencias-en-criptografia-post-cuantica-para-2025/) - Estas tecnologías de cifrado están diseñadas para resistir las amenazas que los ordenadores cuántico...

55. [Novedades en ciberseguridad post-cuántica - KPMG Tendencias](https://www.tendencias.kpmg.es/2025/06/novedades-ciberseguridad-post-cuantica-aviso-plan-accion/) - La computación cuántica no ha dejado de desarrollarse y cada día son más patentes sus progresos apli...

56. [10 Cyber Security Trends For 2026 - SentinelOne](https://www.sentinelone.com/cybersecurity-101/cybersecurity/cyber-security-trends/) - Adopting quantum-resistant cryptographic standards is emerging as a crucial move to protect sensitiv...

57. [Criptografía post cuántica: cómo proteger nuestra información en el ...](https://futuros.gob.es/tendencias/criptografia-post-cuantica) - El próximo estándar de seguridad digital será una carrera contrarreloj para actualizar la cibersegur...

58. [Criptografía post cuántica: cómo proteger nuestra información en el futuro | España 2050](https://futuros.gob.es/index.php/tendencias/criptografia-post-cuantica) - Casi todo lo que hacemos en internet está protegido por sistemas de seguridad digital: desde enviar ...

59. [Cyber and Operational Resilience - Client Update: May 2025](https://publications.arthurcox.com/tech-and-innovation/client-update-may-2025/cyber-and-operational-resilience)

60. [Cyber and Operational Resilience - Client Update](https://publications.arthurcox.com/tech-and-innovation-client-update/april-to-june-2025/cyber-and-operational-resilience) - Explore key developments in EU cybersecurity regulation, including updates on the NIS2 Directive, th...

61. [ENISA Overhauls Its Cybersecurity Market Analysis Playbook With ...](https://complexdiscovery.com/enisa-overhauls-its-cybersecurity-market-analysis-playbook-with-version-3-0-of-ecsmaf/) - ENISA releases ECSMAF V3.0, upgrading its cybersecurity market analysis framework with continuous mo...

62. [ECSMAF v3.0 Explained: How ENISA Maps the EU Cybersecurity ...](https://craevidence.com/blog/enisa-ecsmaf-market-framework-cra-strategy) - ENISA's ECSMAF v3.0 defines how the EU categorises and monitors its cybersecurity market. We break d...

63. [ENISA Threat Landscape 2025 - European Union](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025) - The primary objective of this report is to identify and assess the cybersecurity threat landscape fo...

64. [ENISA 2025 Threat Landscape report highlights EU faces escalating ...](https://industrialcyber.co/reports/enisa-2025-threat-landscape-report-highlights-eu-faces-escalating-hacktivist-attacks-and-state-aligned-cyber-threats/) - The 2025 Threat Landscape report highlights that DDoS attacks were the dominant incident type, accou...

65. [ENISA Cybersecurity Threat Landscape Report 2025 - LinkedIn](https://www.linkedin.com/posts/franciscoalvesmatos_enisa-cybersecurity-threat-landscape-report-activity-7394757321781829632-wDFV) - Safeguarding patient data is more critical than ever in 2025. Discover BESLER's top cybersecurity in...

66. [Your essential guide to cybersecurity KPIs in 2025 - Thoropass](https://www.thoropass.com/blog/cybersecurity-kpis) - Discover how to choose relevant metrics, build a KPI dashboard, and effectively communicate your cyb...

67. [BOE-A-2025-10371 Orden PJC/522/2025, de 23 de mayo, por la ...](https://www.boe.es/buscar/doc.php?id=BOE-A-2025-10371) - Acuerdo por el que se aprueba el procedimiento para la elaboración de una nueva Estrategia Nacional ...

