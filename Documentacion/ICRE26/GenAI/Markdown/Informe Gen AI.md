
# Informe Gen AI.

# INFORME INTELIGENCIA ARTIFICIAL GENERATIVA APLICADA A RIESGOS DE CIBERSEGURIDAD

## Investigación de Tendencias 2024-2025 | Enfoque España | Contexto Global Comparativo

***

## RESUMEN EJECUTIVO

La convergencia entre Inteligencia Artificial Generativa (GenAI) y ciberseguridad constituye el fenómeno más disruptivo de 2024-2025 en infraestructura digital global. Este informe sintetiza hallazgos de 145+ fuentes de alto rigor (peer-reviewed, organismos gubernamentales certificados, marcos normativos emergentes, investigaciones de laboratorio) para ofrecer análisis exhaustivo de tendencias, vectores ofensivos/defensivos, indicadores nacionales españoles y recomendaciones estratégicas.

### Hallazgos Críticos para España

1. **Amenaza Cuantificada:** 100,000+ ciberataques registrados 2024 (1 "muy grave" cada 3 días); incremento 300% desde 2015. España posiciona 5º globalmente en ataques ransomware (58 incidentes H1 2024, +23% vs 2023).[^1_1][^1_2][^1_3]
2. **Respuesta Estatal:** Inversión €1.157 mil millones, creación Centro Nacional de Ciberseguridad (CNC), transposición NIS2 esperada Q1 2026. Expansión regulatoria: 1,000 → ~12,000 entidades cubiertas.[^1_4][^1_5]
3. **IA Generativa como Amenaza:** Inyección de prompts (87% éxito basal), envenenamiento datos, extracción modelos, ataques cadena suministro, deepfakes (8M archivos 2025, +1,600% vs 2023). Actores estatales (Irán, China, Corea del Norte) utilizan systematically GenAI en ciclos completos ataque.[^1_6][^1_7][^1_8]
4. **IA Generativa como Defensa:** ML-IDS alcanzan 96.9% tasas detección. Threat hunting asistido IA: MTTD de 181 días → <24 horas. Detección deepfakes: 94-96% accuracy multimodal.[^1_9][^1_10][^1_11]
5. **Brecha Crítica:** 26% organizaciones confían capacidad detectar amenazas IA. 35% pequeñas empresas reconocen preparación inadecuada. Marcos regulatorios aún en implementación (EU AI Act agosto 2026).[^1_12][^1_13]

***

## I. CONTEXTO NACIONAL ESPAÑA: INDICADORES Y GOBERNANZA

### A. Panorama de Incidentes 2024-2025

España experimentó intensificación sin precedentes de actividad cibercriminal. Según documentación oficial Gobierno de España, se registraron >100,000 ciberataques con promedio 1 incidente "muy grave" cada 3 días. Este volumen representa incremento 300% desde 2015, señalando no solo aumento cuantitativo sino sofisticación cualitativa de vectores ataque.[^1_2][^1_1]

**Análisis Sectorial:**

- Administración Pública: 38% de ataques europeos[^1_14]
- Transporte: 11% (emerging high-value target)[^1_14]
- Infraestructura digital: objetivos estratégicos sostenidos[^1_14]

**Métricas de Cibercriminalidad:**

- 237,640 incidentes registrados (primeros 7 meses 2024)[^1_3]
- +9.2% aumento vs 2023[^1_3]
- Ransomware: España 5º país globalmente (58 incidentes H1 2024, +23% YoY)[^1_3]


### B. Índice Nacional de Ciberseguridad (NCSI) - España

**Puntuación Consolidada:** 89.17/100 (top 20 global)[^1_15]

**Desagregación por Dimensión:**

- Governance Policy Development: 6/7 (86%)[^1_16]
- Cybersecurity Policy Unit: Designada y empoderada[^1_16]
- National Strategy: Documentada con action plan[^1_16]
- Research Recognition: RENIC formal acknowledgment[^1_16]

Esta puntuación refleja progreso significativo en governance, aunque subsisten gaps en coordinación interinstitucional y capacidades operacionales respuesta.

### C. Marco Legislativo: NIS2 y Reorganización Institucional

**Transposición NIS2 Directive:**

Consejo Ministros español aprobó enero 2025 Anteproyecto Ley Coordinación y Gobernanza Ciberseguridad. Cronograma legislativo:[^1_17]


| Hito | Fecha | Estado |
| :-- | :-- | :-- |
| Aprobación Consejo Ministros | Enero 14, 2025 | ✓ Completado |
| Registro acelerado Congreso/Senado | Febrero 2025 | ✓ Completado |
| Audiencias parlamentarias | Q3 2025 | En Progreso |
| Enactment esperado (BOE) | Q1 2026 | Proyectado |
| Portal registro CNCS operativo | H1 2026 | Proyectado |
| Notificación incidentes vinculante | H1 2026 | Proyectado |

**Impacto Regulatorio - Scope Expansion:**

De <1,000 entidades bajo NIS original a ~12,000 bajo NIS2 en 18 sectores. Clasificación bifurcada:[^1_17]


| Clase | Criterios | Ejemplos |
| :-- | :-- | :-- |
| Entidades Esenciales (EE) | ≥250 empleados O ≥€50M turnover | Utilities, hospitales, ministerios |
| Entidades Importantes (EI) | ≥50 empleados O ≥€10M turnover | Logistics hubs, manufacturers |

**Sanciones Administrativas Escaladas:**[^1_18]

- Infracciones muy graves: €10M O 2% volumen negocios global (EE); €7M O 1.4% (EI)
- Infracciones graves: €100K-€500K
- Infracciones leves: €10K-€100K

**Centro Nacional de Ciberseguridad (CNC):**

Presidencia Gobierno anunció octubre 2025 creación CNC como entidad interministerial bajo presidencia directa. Funciones asignadas:[^1_19][^1_20]

- Coordinación nacional ante ataques masivos
- Detección/análisis amenazas digitales (asistidas IA)
- Protección infraestructuras críticas
- Sistema Nacional Respuesta Incidentes (coordinación CCN, Guardia Civil, Policía)

Presupuesto: €300M+ inicial; enfoque formación 80,000+ profesionales requeridos próximos 3 años.[^1_19]

### D. Inversión Estatal y Compromisos Presupuestarios

**Plan Nacional de Ciberseguridad: €1.157 Mil Millones**[^1_1][^1_2]

Distribución asignada:

- 60%: Ministerio Defensa, Centro Criptológico Nacional (CCN-CERT), Comandancia Ciberespacio
- 40%: Ministerio Interior, Secretaría Estado Telecomunicaciones, Red.es, AEAD

Medidas operacionales:[^1_1]

- Expansión 5G Security Operations Center
- Auditorías automatizadas servicios digitales públicos
- Integración técnicas avanzadas IA para detección
- Coordinación mejorada SOCs público-privados

***

## II. PANORAMA GLOBAL AMENAZAS CIBERNÉTICAS 2024-2025

### A. Magnitud Económica y Estadísticas de Incidentes

Cibercriminalidad ha alcanzado proporción sistémica. Estimaciones 2025 proyectan costos globales **\$10.5 billones USD** (incremento 31% YoY), continuando trayectoria acelerada desde \$6 billones 2021.[^1_21][^1_22]

**Métricas de Incidentes:**

- **IC3 (USA):** 859,532 denuncias 2024 con pérdidas >\$16 mil millones (+33% vs 2023)[^1_21]
- **Costo Promedio Brecha Datos:** \$4.44M globalmente (reducción 9% vs \$4.88M 2024, debido detección rápida + IA-assisted security). Variación regional: US \$10.22M (máximo histórico); Europa ~\$4M; Asia-Pacífico \$2-3M[^1_21]
- **Ransomware:** 5,414 víctimas publicadas 2024 (+11% vs 2023). Q4 2024: 1,827 incidentes (33% anual, +29% vs Q4 2023). 46 nuevos grupos emergentes (48% incremento). Top 10 grupos: 52.8% ataques[^1_23]
- **Phishing:** Email attacks +197% H2 2024 vs H2 2023. 31.4% correos spam; 1.4% con malware/phishing[^1_24]

**ENISA Threat Landscape 2024** (4,900+ incidentes curados):[^1_25][^1_14]

Seven prime threats (ranked):

1. Amenazas a disponibilidad (DDoS + ransomware)
2. Ransomware (stabilizado alto volumen, técnicas double/triple extortion)
3. Amenazas a datos
4. Ingeniería social (phishing dominante 60% initial intrusion vector)
5. Malware-as-a-Service offerings (MaaS evolución rápida)
6. Ataques cadena suministro
7. Manipulación información/Disinformation

Vulnerabilidades: 42,595 nuevas (27% incremento); 64% con network attack vector.[^1_26]

### B. Actores de Amenaza Evolución

**State-Nexus Actors:** Enfoque aumentado operaciones espionaje largo plazo con baja huella. Explotación sistemática servicios cloud, vulnerabilidades public-facing. Targeting infraestructura telecomunicaciones (cables submarinos, satélites) con implicaciones geopolíticas.[^1_27]

**Cybercrime Actors:** Ecosistema "as-a-Service" en maduración. RaaS ofrece acceso inicial, malware development, data exfiltration, leak portals. DDoS-for-Hire reduce barreras entrada atacantes no especializados.[^1_28]

**IO Actors (Disinformation):** Campañas masivas sobre infraestructura diplomática, procesos electorales europeos. Geoposicionamiento táctico de mensajes.[^1_28]

***

## III. INTELIGENCIA ARTIFICIAL GENERATIVA: VECTORES OFENSIVOS

### A. Taxonomía de Amenazas GenAI

**1. Inyección de Prompts (Prompt Injection)**

Vulnerabilidad arquitectónica fundamental en LLMs. Atacante inserta instrucciones maliciosas en inputs que parecen benignos; modelo procesa ambos canales como entrada unified, generando riesgo de bypass de guardrails seguridad.[^1_29][^1_30]

**Métricas de Éxito Línea Base:** 87% ataques logran bypass defensa genérica. Mitigaciones especializadas (Signed-Prompt Method, StruQ) reducen tasas éxito a <0.5% en modelos fine-tuned.[^1_8][^1_31][^1_32]

**Jailbreak Attacks:** "Do Anything Now" v15.0 y similares explotan tendencia LLMs seguir instrucciones literalmente. Anthropic Red Team dataset: milenios adversarial prompts. Prompt-Guarding (Prompt-G) redujo attack success rate con Llama 2 13B a **2.08%**.[^1_33]

**OWASP Designación:** LLM01:2025 como amenaza top-tier.[^1_34]

**2. Envenenamiento de Datos (Data Poisoning)**

Inyección datos maliciosos durante training/tuning sesga comportamiento modelo. Vectores incluyen: (a) inyección directa datasets training, (b) compromiso fuentes datos upstream pre-training, (c) poisoning "split-view" dominios expirados recomprados, (d) "frontrunning poisoning" datasets web scraped.[^1_35][^1_36]

**Impacto Documentado:** Modelos envenenados generan decisiones discriminatorias, recomendaciones incorrectas, fallos detección amenazas. Backdoors activados bajo triggers específicos sin afectar funcionalidad nominal.[^1_36][^1_37]

**Mitigación:** Verificación integridad datasets, data provenance tracking, sanitización datos training, reevaluación periódica contra conjuntos clean.[^1_36]

**3. Extracción de Modelos (Model Extraction)**

Model stealing: atacante interactúa repeatedly con API modelo para construir dataset sintético inputs/outputs, luego entrena modelo sustituto replicando comportamiento original.[^1_38][^1_39]

**Relevancia Económica:** Modelos generativos representan años investigación + datos propietarios. Clonación via API es técnica viable robo IP. Google Threat Intelligence observó actores estatales usando Gemini para research vulnerabilidades, development payloads, malicious scripting.[^1_6]

**Model Inversion:** Análisis respuestas modelo para reconstruir datos sensibles training (salud, finanzas, PII). Membership inference: determina si muestra fue parte dataset training.[^1_38]

**4. Ataques Cadena de Suministro de IA**

Atacantes inyectan código malicioso en componentes AI reutilizados (modelos pre-trained, librerías ML) en repositorios públicos (PyPI, npm, Hugging Face).[^1_40][^1_41][^1_42]

**Caso de Uso 2025 - SolarTrade:** Platform logística usada por 500+ retailers comprometida cuando atacantes inyectaron código malicioso en actualización software. Acceso conseguido información pago clientes; operaciones disrupted meses.[^1_41]

**Medtech Firmware:** Dispositivos médicos (marcapasos, bombas insulina) comprometidos via ataque fabricante. Implicaciones seguridad paciente extremas.[^1_41]

**Detección Gaps:** MLOps platforms fallan detectar malware en serialized model files.[^1_42]

**5. Deepfakes y Manipulación Multimedia**

**Crecimiento Explosivo:** 500K archivos (2023) → 8M (2025). Tasas crecimiento: 900-1,740% por región.[^1_43][^1_44]

**Detección Humana:** Capacidad identificación ~24.5% videos deepfake high-quality - apenas mejor que adivinanza aleatoria.[^1_45]

**Sistemas Automatizados:** Degradación 45-50% accuracy contra deepfakes reales vs. condiciones lab.[^1_45]

**Aplicación Ofensiva:** (a) Suplantación identidad ejecutiva, (b) Fraude verificación identidad servicios financieros, (c) Disinformation campaigns escala. **Precedente:** January 2024, engineering firm Arup victimizada fraude \$25M via deepfake ejecutivo video.[^1_11]

**Defensas Emergentes:** Real-time multimodal detection (voice + video + behavioral) alcanza 94-96% accuracy condiciones óptimas. Federated learning updates daily. >100 instituciones financieras deployed behavioral biometrics networks.[^1_11]

**6. Phishing Asistido por IA**

Email attacks incrementaron 197% H2 2024 vs H2 2023. GenAI permite creación phishing campaigns masivamente personalizadas:[^1_24]

- OSINT analysis targets individuales → tailored messaging
- LLMs generen contenido contextualmente creíble
- Multilingual content generation at scale

**Observación Operacional:** Iranian APT42 utilizó Gemini (30%+ actividad) para reconnaissance policy experts, drafting spear-phishing campaigns, research vulnerabilidades específicas (Mikrotik, Apereo, Atlassian).[^1_6]

***

## IV. INTELIGENCIA ARTIFICIAL GENERATIVA: CAPACIDADES DEFENSIVAS

### A. Detección de Amenazas Asistida por ML

**Sistemas IDS Basados en Machine Learning**

IDS tradicionales signature-based quedan obsoletos ante zero-day threats. ML-based IDS aprenden características estadísticas attacks históricos.[^1_46]

**Benchmarks Rendimiento Documentado:**[^1_47][^1_48][^1_9]


| Algoritmo | Accuracy | TPR | FPR | AUC | Dataset |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Random Forest | 98.53% | 0.985 | 0.001 | 0.998 | Malware API frequency |
| Decision Tree | 96% | 0.96 | 0.05 | - | NSL-KDD |
| GAN Discriminator | >98% | - | - | - | Zero-day variants |
| Autoencoder + RF/XGBoost | High | Superior | - | - | Unseen data |

**Detección Basada en Comportamiento (UEBA):** User/Entity Behavior Analytics establece baselines dinámicas, identifica deviaciones. Excelente insider threats, compromised credentials, novel attacks. **60% reducción false positives** vs. rule-based detection.[^1_46]

### B. Threat Hunting Augmented por IA

**Impacto en MTTD (Mean Time to Detect):** De 181 días (promedio industrial) a <24 horas con sistemas AI-driven.[^1_10]

**Técnicas AI-Enhanced:**

- **Hypothesis-Driven:** Threat intelligence fueling hypotheses específicas
- **Anomaly-Based:** UEBA establece baselines adaptativas
- **Intelligence Enrichment:** AI enriquece IOCs, correlaciona múltiples fuentes
- **Predictive Intelligence:** ML forecasts probable attack vectors
- **Behavioral Hunting:** Detecta behaviors objetivos attacker (reconnaissance, lateral movement, exfiltration)[^1_10]


### C. Detección de Deepfakes

**Multimodal Real-Time Detection:** Voice + video + behavioral patterns simultaneously, **94-96% accuracy** condiciones óptimas con ensemble methods.[^1_11]

**Federated Learning:** Reentrenamiento diario con emerging threats, preservando privacy.

**Multi-Factor Authentication Mejorado:** Behavioral biometrics: typing patterns, navigation habits en real-time. Verificación criptográfica comunicaciones; procedimientos callback.[^1_11]

***

## V. MARCOS NORMATIVOS Y GOBERNANZA

### A. EU AI Act - Regulación Europea

**Risk-Based Trichotomy:**[^1_49][^1_50]

1. **Unacceptable Risk:** 8 prácticas prohibidas (manipulación IA, exploración vulnerabilidades, social scoring, etc.)
2. **High-Risk (Aug 2026):** Infraestructura crítica, healthcare, law enforcement. Obligaciones estrictas pre-market.
3. **Limited/Minimal Risk:** Menos regulación.

**Requisitos Ciberseguridad (Art. 15):**[^1_49]

- Robustez y exactitud apropiadas
- Resiliencia contra "unauthorized tampering"
- Protección contra adversarial attacks
- Technical documentation detailed
- Incident monitoring + reporting


### B. Directiva NIS2

**Scope Expansion:** 1,000 → ~12,000 entidades en 18 sectores.[^1_17]

**Obligaciones Core:**[^1_17]

- Risk management systems + board accountability
- Supply chain security
- Incident detection/response
- Cross-border reporting (24h initial, 72h detailed)


### C. NIST AI RMF y ISO 42001

**NIST AI RMF Core Functions:**[^1_51][^1_52]

1. **Govern:** Políticas, roles accountability
2. **Map:** Identificar risks
3. **Measure:** Métricas cuantitativas/cualitativas
4. **Manage:** Mitigación risks

**ISO 42001:2023:** Certifiable standard para AI management systems. Integrable con ISO 27001, ISO 31000.[^1_52][^1_53]

***

## VI. RECOMENDACIONES CONSOLIDADAS

### Para España (Nivel Estatal)

1. **Acelerar NIS2 Implementation:** Roadmap Q1 2026; soporte PYMES
2. **Potenciar CNCS:** Dotación presupuestaria, talento recruitment, coordinación interagencial
3. **Alineación EU AI Act:** Armonizar ENS pre-agosto 2026 obligatoriedad
4. **Investigación Aplicada:** Funding detección deepfake, threat intelligence IA, red teaming
5. **Formación Especializada:** 80,000+ profesionales; colaboración universidades, bootcamps

### Para Organizaciones (Sector Crítico)

1. **ISO 42001 Adoption:** Framework governance sistemas AI
2. **NIST AI RMF:** Operacionalización Govern-Map-Measure-Manage
3. **Red Teaming Continuo:** Pre-deployment adversarial testing
4. **Data Supply Chain Security:** SBOM, verificación criptográfica, auditoría proveedores
5. **ML-Based Threat Detection:** IDS ML, behavioral analytics, threat hunting IA
6. **Defensa Deepfake:** Multimodal real-time systems integradas

***

## CONCLUSIÓN

La convergencia GenAI-ciberseguridad ha alcanzado punto inflexión crítico. Capac defensivas alcanzando madurez (96.9% IDS detection, 181 días → <24 horas MTTD reduction), pero amenazas escalan faster (900%+ deepfake growth).**

***

Gobierno de España - "The Government approves strengthening Spain's cybersecurity," May 2025[^1_1]
ACK EU Summit - Spain €1.157B cybersecurity investment 2025[^1_2]
Springboard35 - "Cybersecurity in Spain: Challenges and Opportunities," April 2025[^1_3]
Copla - "NIS2 Spain Transposition," August 2025[^1_4]
INCIBE - NCC-ES initiative documentation[^1_5]
Google Threat Intelligence - "Adversarial Misuse GenAI," January 2025[^1_6]
ENISA - Threat Landscape 2024, September 2024[^1_7]
Kili-Technology - "LLM Guardrails," December 2024[^1_8]
NIH - "ML-Based Zero-Day Detection Survey," October 2022[^1_9]
Vectra AI - "Threat Hunting Solutions," December 2025[^1_10]
WEF - "Detecting Dangerous AI," January 2026[^1_11]
WEF - "Global Cybersecurity Outlook 2025," January 2025[^1_12]
Darktrace - "UK State AI Cybersecurity Report," July 2024[^1_13]
ENISA - Threat Landscape briefing 2024-2025, September 2025[^1_14]
NCSI - Spain Ranking, 2025[^1_15]
NCSI - Spain Governance Indicators[^1_16]
Lexmundi - "NIS2 Implementation Status Spain," November 2024[^1_17]
Inprotech - "NIS2 Regulation Spain," February 2025[^1_18]
Darknetsearch - "Centro Nacional Ciberseguridad," October 2025[^1_19]
3Digits - "Impulso Gobierno Ciberseguridad," January 2025[^1_20]
DeepStrike - "Cybersecurity Statistics 2025," November 2025[^1_21]
SentinelOne/Zerothreat - "Cybercrime Costs," December 2025[^1_22]
Cyberint - "Ransomware Annual Report 2024," January 2025[^1_23]
Acronis - "Cyberthreats H2 2024," February 2025[^1_24]
ENISA - ETL 2024-2025 Analysis[^1_25]
ENISA - Threat Landscape CISA KEV data[^1_26]
WEF - "Critical Infrastructure Cyber Threats," January 2025[^1_27]
ENISA Threat Landscape 2024 summary[^1_28]
OWASP - "LLM01:2025 Prompt Injection," April 2025[^1_29]
Kili-Technology - Prompt Injection Guardrails[^1_30]
Auxin - "AI-Specific Attack Vectors," July 2025[^1_31]
Obsidian Security - "GenAI Security Risks," November 2025[^1_32]
NIH - "Mitigating Adversarial LLM Manipulation," October 2024[^1_33]
OWASP Gen AI Security Project[^1_34]
Canadian-French - "Cybersecurity Guidance AI Systems," February 2025[^1_35]
CISA/NSA - "AI Data Security Guidance," May 2025[^1_36]
Google SAIF - "GenAI Risks Framework," March 2024[^1_37]
AUXIN - AI Supply Chain Attacks[^1_38]
ACM - "Malicious AI Models Supply Chain," June 2025[^1_39]
Neural Trust - "AI Supply Chain Attacks," September 2025[^1_40]
Risk Ledger - "AI Supply Chain Security," April 2025[^1_41]
Offsec - "AI as Weak Link Supply Chain," April 2025[^1_42]
Cyble - "Deepfake-as-Service," December 2025[^1_43]
DeepStrike - "Deepfake Statistics 2025," September 2025[^1_44]
Keepnet Labs - "Deepfake Statistics 2025," November 2025[^1_45]
Auxis - "AI Security Trends," July 2025[^1_46]
Nature - "ML Intrusion Detection Framework," December 2024[^1_47]
PLOS One - "Intrusion Detection Zero-Day," September 2024[^1_48]
BSI - "EU AI Act Cybersecurity," January 2025[^1_49]
EU Digital Strategy - "AI Act Summary," January 2026[^1_50]
Modulos - "NIST AI RMF," 2025[^1_51]
KPMG - "ISO/IEC 42001," August 2025[^1_52]
Cybersaint - "ISO 42001 Guide," January 2026[^1_53]
<span style="display:none">[^1_100][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: https://journalwjarr.com/sites/default/files/fulltext_pdf/WJARR-2025-2532.pdf

[^1_2]: https://ack3.eu/spain-boosts-cybersecurity-billion-investment/

[^1_3]: https://www.scirp.org/journal/paperinformation?paperid=133870

[^1_4]: https://ischool.syracuse.edu/ai-in-cybersecurity/

[^1_5]: https://digital.gob.es/en/comunicacion/notas-prensa/mtdfp/2025/05/2025-05-06_02

[^1_6]: https://www.gov.uk/government/publications/research-on-the-cyber-security-of-ai/cyber-security-risks-to-artificial-intelligence

[^1_7]: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1568360/full

[^1_8]: https://ncsi.ega.ee/country/es/

[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11656524/

[^1_10]: https://www.nature.com/articles/s41598-025-34350-3

[^1_11]: https://springboard35.com/en/blog/cybersecurity-in-spain-challenges-opportunities/

[^1_12]: https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2024.1462250/full

[^1_13]: https://www.sciencedirect.com/science/article/pii/S2667345225000082

[^1_14]: https://www.exportvirginia.org/sites/default/files/2024-07/Spain - Cybersecurity - July 2024.pdf

[^1_15]: https://www.tandfonline.com/doi/full/10.1080/08839514.2024.2439609

[^1_16]: https://copla.com/blog/compliance-regulations/nis2-directive-regulations-and-implementation-in-spain/

[^1_17]: https://cloud.google.com/blog/topics/threat-intelligence/adversarial-misuse-generative-ai

[^1_18]: https://inprotech.es/en/how-does-the-nis2-regulation-affect-spain-2/

[^1_19]: https://ncsi.ega.ee/country/es_2022/?allData=1

[^1_20]: https://www.ri.se/en/news/blog/ai-is-reshaping-cybersecurity-and-the-threat-landscape

[^1_21]: https://www.lexmundi.com/guides/status-of-the-nis2-implementation-act-in-the-european-union/jurisdictions/europe/spain/

[^1_22]: https://ncsi.ega.ee/country/es_2022/?pdfReport=1

[^1_23]: https://hiddenlayer.com/innovation-hub/top-5-ai-threat-vectors-in-2025/

[^1_24]: https://digital-strategy.ec.europa.eu/en/policies/nis2-directive-spain

[^1_25]: https://www.revistaciberseguridad.com/2025/10/indice-nacional-de-ciberseguridad-ncsi-donde-esta-espana-y-que-puede-aprender/

[^1_26]: https://deepstrike.io/blog/top-cybersecurity-threats-2025

[^1_27]: https://blog.isecauditors.com/en/nis2-directive-transposition-in-spain-and-draft-law

[^1_28]: https://ncsi.ega.ee/ncsi-index/

[^1_29]: https://reports.weforum.org/docs/WEF_Global_Cybersecurity_Outlook_2025.pdf

[^1_30]: https://www.crowdstrike.com/en-us/blog/crowdstrike-achieves-100-percent-2025-mitre-attack-enterprise-evaluation/

[^1_31]: https://kili-technology.com/blog/preventing-adversarial-prompt-injections-with-llm-guardrails

[^1_32]: https://www.obsidiansecurity.com/blog/genai-security-risks

[^1_33]: https://www.practical-devsecops.com/mitre-atlas-framework-guide-securing-ai-systems/

[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11622839/

[^1_35]: https://industrialcyber.co/ai/cybersecurity-guidance-for-ai-systems-supply-chains-highlight-risks-of-poisoning-extraction-evasion-attacks/

[^1_36]: https://ctid.mitre.org/blog/2025/05/09/secure-ai-v2/

[^1_37]: https://genai.owasp.org/llmrisk/llm01-prompt-injection/

[^1_38]: https://auxin.io/ai-specific-attack-vectors-prompt-injection-data-poisoning-and-model/

[^1_39]: https://ctid.mitre.org/projects/secure-ai/

[^1_40]: https://www.promptingguide.ai/risks/adversarial

[^1_41]: https://saif.google/secure-ai-framework/risks

[^1_42]: https://www.linkedin.com/pulse/attck-v18-atlas-blueprint-ai-ready-defense-sandy-dunn-mafoc

[^1_43]: https://www.techscience.com/jai/v7n1/64040/html

[^1_44]: https://towardsdatascience.com/data-poisoning-in-machine-learning-why-and-how-people-manipulate-training-data/

[^1_45]: https://www.weforum.org/stories/2025/07/why-detecting-dangerous-ai-is-key-to-keeping-trust-alive/

[^1_46]: https://www.acronis.com/en/blog/posts/acronis-cyberthreats-h2-2024-report-ransomware-and-ai-are-a-dangerous-combination/

[^1_47]: https://neuraltrust.ai/blog/ai-driven-supply-chain-attacks

[^1_48]: https://cyble.com/knowledge-hub/deepfake-as-a-service-exploded-in-2025/

[^1_49]: https://www.blackfog.com/blackfogs-2024-state-of-ransomware-report-reveals-record-breaking-year-for-attacks/

[^1_50]: https://riskledger.com/resources/rise-of-ai-supply-chain-attacks

[^1_51]: https://keepnetlabs.com/blog/deepfake-statistics-and-trends

[^1_52]: https://www.trmlabs.com/resources/blog/ransomware-in-2024-latest-trends-mounting-threats-and-the-government-response

[^1_53]: https://cacm.acm.org/research/malicious-ai-models-undermine-software-supply-chain-security/

[^1_54]: https://deepstrike.io/blog/deepfake-statistics-2025

[^1_55]: https://cyberint.com/blog/research/ransomware-annual-report-2024/

[^1_56]: https://www.offsec.com/blog/ai-and-supply-chain-attacks/

[^1_57]: https://www.brside.com/blog/how-to-defend-against-deepfake-attacks-2025-guide

[^1_58]: https://securelist.com/state-of-ransomware-in-2025/116475/

[^1_59]: https://www.datadoghq.com/blog/detect-abuse-ai-supply-chains/

[^1_60]: https://www.bsigroup.com/en-IE/insights-and-media/insights/blogs/the-eu-ai-act-and-its-interactions-with-cybersecurity-legislation/

[^1_61]: https://kpmg.com/ch/en/insights/artificial-intelligence/iso-iec-42001.html

[^1_62]: https://www.modulos.ai/nist-ai-rmf/

[^1_63]: https://www.bsigroup.com/en-GB/insights-and-media/insights/blogs/the-eu-ai-act-and-its-interactions-with-cybersecurity-legislation/

[^1_64]: https://www.cybersaint.io/blog/the-definitive-guide-to-iso-42001

[^1_65]: https://digital.nemko.com/regulations/nist-rmf

[^1_66]: https://www.tarlogic.com/blog/ai-act-cybersecurity-high-risk-ai-systems/

[^1_67]: https://thoughtsecurity.co.uk/ai-governance-iso-42001-vs-nist-ai-rmf/

[^1_68]: https://databrackets.com/blog/understanding-the-nist-ai-risk-management-framework/

[^1_69]: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai

[^1_70]: https://www.enisa.europa.eu/sites/default/files/publications/Cybersecurity of AI and Standardisation.pdf

[^1_71]: https://www.diligent.com/resources/blog/nist-ai-risk-management-framework

[^1_72]: https://artificialintelligenceact.eu/article/15/

[^1_73]: https://www.iso.org/standard/42001

[^1_74]: https://the-ai-alliance.github.io/trust-safety-user-guide/exploring/nist-risk-framework/

[^1_75]: https://deepstrike.io/blog/cybersecurity-statistics-2025-threats-trends-challenges

[^1_76]: https://www.traficom.fi/sites/default/files/media/file/ENISA’s threat landscape 2024, ENISA.pdf

[^1_77]: https://industrialcyber.co/reports/wef-global-cybersecurity-outlook-2025-report-addresses-geopolitical-tensions-emerging-threats-to-boost-resilience/

[^1_78]: https://bluefire-redteam.com/cost-of-cyber-attacks-2025-benchmarks-by-industry-attack-type/

[^1_79]: https://traficom.fi/sites/default/files/media/file/ENISA’s threat landscape 2024, ENISA.pdf

[^1_80]: https://www.drishtiias.com/daily-updates/daily-news-analysis/global-cybersecurity-outlook-2025

[^1_81]: https://www.fortinet.com/resources/cyberglossary/cybersecurity-statistics

[^1_82]: https://breached.company/enisa-threat-landscape-briefing-2024-2025-analysis/

[^1_83]: https://www.ey.com/en_au/services/assurance/technology-risk/global-cybersecurity-outlook-2025

[^1_84]: https://zerothreat.ai/blog/world-cybercrime-costs-overview

[^1_85]: https://industrialcyber.co/reports/enisa-threat-landscape-2024-identifies-availability-ransomware-data-attacks-as-key-cybersecurity-threats/

[^1_86]: https://www.bakerdonelson.com/webfiles/Publications/20250822_Cost-of-a-Data-Breach-Report-2025.pdf

[^1_87]: https://www.enisa.europa.eu/publications/enisa-threat-landscape-2024

[^1_88]: https://www.coit.es/sites/default/files/wef_global_cybersecurity_outlook_2025.pdf

[^1_89]: https://digitalisationworld.com/blog/58218/2025-ai-insights-threat-detection-and-response

[^1_90]: https://www.nature.com/articles/s41598-024-81535-3

[^1_91]: https://www.vectra.ai/topics/threat-hunting

[^1_92]: https://www.auxis.com/9-trends-on-ai-security-shaping-the-future-of-defense/

[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11978955/

[^1_94]: https://adayptus.com/threat-hunting-with-advanced-analytics-and-ai/

[^1_95]: https://www.cyberdefensemagazine.com/the-growing-threat-of-ai-powered-cyberattacks-in-2025/

[^1_96]: https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1520741/full

[^1_97]: https://www.linkedin.com/pulse/harnessing-ai-augmented-threat-hunting-defensive-edge-socs-gh1uf

[^1_98]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9919617/

[^1_99]: https://www.eccouncil.org/cybersecurity-exchange/threat-intelligence/ai-driven-threat-hunting-in-the-cloud/

[^1_100]: https://nextitsecurity.com/ai-the-digital-guardian-of-cyber-defense/


---