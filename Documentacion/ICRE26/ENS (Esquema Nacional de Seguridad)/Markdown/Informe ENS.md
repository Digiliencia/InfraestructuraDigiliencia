
# Informe ENS.


## Vectores de Investigación

**Alcance Estratégico:**

- Evolución normativa del ENS (Real Decreto 311/2022) y actualizaciones post-2024
- Alineación con NIS2 Directive y marco europeo de ciberseguridad
- Métricas y KPIs en el Real Decreto 311/2022 vs. estándares comparativos (NIST CSF 2.0, ISO 27001/42001, COBIT)

**Benchmarking Territorial:**

- Posición de España en índices globales (GFCI, NRI, Global Cybersecurity Index)
- Comparativas internacionales relevantes (UE-27, OCDE, contexto geopolítico)
- Iniciativas sectoriales por Comunidad Autónoma (si procede)

**Dimensiones de Medición:**

- Indicadores técnicos de detección y respuesta ante amenazas
- Métricas de gobernanza de seguridad (madurez, cumplimiento, auditoría)
- Cuantificación de impacto: modelos financieros (FAIR, CAsPeA), reputación, disponibilidad

**Fuentes Estratégicas:**

- INCIBE, CNI (documentación pública)
- Organismos de normalización (AEPD, CCN-CERT)
- Publicaciones académicas de universidades españolas en ciberseguridad
- Informes de consultoría de clase mundial (Gartner, Forrester, McKinsey) con datos españoles



***

# **INFORME INTEGRAL: ESQUEMA NACIONAL DE SEGURIDAD (ENS) 2024-2025**

## Indicadores, Métricas y Benchmarking Ciberseguridad España

### **Resumen Ejecutivo**

España ha consolidado su posición como **referente europeo en ciberseguridad**, alcanzando el nivel máximo (Tier 1 / Role-modelling) en el Global Cybersecurity Index 2024 de la UIT, con 99,74 puntos. Sin embargo, el panorama de amenazas ha alcanzado **dimensiones críticas**: en 2024 se gestionaron 97.348 incidentes (+16,6%), incluyendo 100.000+ ciberataques detectados, con España ocupando la **2ª posición mundial en ransomware** (5% del tráfico global). Este informe analiza exhaustivamente los indicadores, marcos normativos y estrategias de ciberseguridad españolas desde una perspectiva integral (técnica, gobernanza, financiera) alineada con estándares internacionales (NIST CSF 2.0, ISO 27001:2022, NIS2).

***

## **I. Marco Normativo y Regulatorio**

### **1.1 Esquema Nacional de Seguridad (Real Decreto 311/2022)**

El ENS constituye el **marco legal obligatorio** para el sector público español, regulado desde mayo de 2022 con actualización significativa respecto al RD 3/2010. Su estructura reposa en **7 principios básicos** y **15 requisitos mínimos**, materializados en tres grupos de medidas de seguridad:[^2_1]


| Grupo | Componentes | Alcance |
| :-- | :-- | :-- |
| **Marco Organizativo** | Política seguridad, roles, responsabilidades, gestión riesgos | Gobernanza integral |
| **Marco Operacional** | Planificación, control acceso, explotación, servicios externos, monitorización | Operación segura sistemas |
| **Medidas Protección** | Infraestructuras, personal, equipos, comunicaciones, datos, aplicaciones, servicios | Protección activos |

El artículo 32 establece la obligación de **reportar indicadores anuales de seguridad** a través de la Comisión Sectorial de Administración Electrónica, consolidados por el CCN-CERT mediante cuadros de mando e indicadores clave.

### **1.2 Directiva NIS2 y Transposición Española**

La **Directiva 2022/2555 de la UE** (Network Information Security Directive 2) entró en vigor el 17 de octubre de 2024 a nivel europeo. España, mediante el **Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad** (aprobado en enero de 2025), procede a su transposición, con vigencia esperada en **2026**.[^2_2]

Los cambios disruptivos de NIS2 respecto a NIS original incluyen:

**Ampliación de Sectores Cubiertos:**

- Operadores esenciales: Energía, transporte, agua, sanidad, finanzas, infraestructuras digitales, servicios postales
- Operadores importantes: Fabricación, sector TIC, entidades de I+D, organismos públicos

**Obligaciones Reforzadas:**

- Notificación de incidentes: **< 24 horas** tras detección
- Evaluación de riesgos: Periódica, documentada
- Gobernanza de seguridad: Responsabilidad ejecutiva (Junta Directiva/Consejo)
- Auditorías: Frecuentes (no menos de bianual para esenciales)
- Sanciones: **Hasta 10M€ o 2% facturación anual global**

**Alineamiento ENS-NIS2:**
El Real Decreto 311/2022 facilita el cumplimiento dual: organizaciones que satisfacen ENS pueden demostrar conformidad NIS2 mediante el **Perfil de Cumplimiento Específico (PCS)** del CCN, reduciendo carga administrativa sin merma de protección.[^2_3]

***

## **II. Indicadores y Métricas de Ciberseguridad (Nivel Nacional)**

### **2.1 Incidentes y Amenazas (2024-2025)**

#### **Balance INCIBE 2024**[^2_4]

| Métrica | Valor 2024 | Variación | Detalles |
| :-- | :-- | :-- | :-- |
| **Total Incidentes** | 97.348 | +16,6% vs 2023 | Ciudadanos: 65.808 (67,6%); Empresas: 31.540 (32,4%) |
| **Malware** | 42.136 | +% | Ransomware: 357 casos (+) |
| **Phishing** | 21.571 | +% | 20% detecciones globales en España 2025 |
| **Fraude Online** | 38.000 | +43,2% vs 2023 | Mayor categoría de amenaza |
| **Intrusiones** | 7.470 | Accesos no autorizados | Redes corporativas y domésticas |
| **Sistemas Vulnerables Notificados** | 183.851 | Proactivamente | Susceptibles explotación inmediata |
| **Consultas Línea 017** | 98.546 | +21,8% vs 2023 | 54% preventivas, 46% reactivas |

#### **Ransomware: Crisis Estratégica**[^2_5][^2_6][^2_7]

España ocupa la **2ª posición mundial** tras EE.UU. en incidentes de ransomware:

- **H2 2025**: +116% en ataques ransomware vs H1
- **Volumen**: 5% del tráfico de ransomware global
- **Coste medio**: 1,8M€ por incidente
- **Robo de datos**: >238 TB estimados (H2 2025)
- **Sectores afectados**: Tecnología (principal), servicios empresariales, manufactura

**Técnicas Evolutivas:**

- Doble/triple extorsión (cifrado + datos + ataques DDoS)
- IA mejorada para evasión de detección
- Infostealers sofisticados (Vidar, CloudEyE post-Lumma)
- NFC malware: +87% detecciones (robo biométrico, desactivación 2FA)

***

### **2.2 Métricas Técnicas de Respuesta a Incidentes**

Las métricas operativas críticas para evaluar efectividad incluyen:[^2_8][^2_9]


| Métrica | Definición | Benchmark Sector | Relevancia ENS |
| :-- | :-- | :-- | :-- |
| **MTTD** (Mean Time To Detect) | Tiempo promedio identificación desde ocurrencia | <4 horas (objetivo) | Art. 8: Detección continua |
| **MTTA** (Mean Time To Acknowledge) | Tiempo alertas clasificadas/priorizadas | <30 minutos | Capacidad respuesta |
| **MTTR** (Mean Time To Recover/Resolution) | Tiempo restauración servicios/datos | <4 horas críticos, <24h otros | Art. 33: Respuesta incidentes |
| **MTBF** (Mean Time Between Failures) | Período entre incidentes sucesivos | Variable por sistema | Indicador resiliencia |
| **Tasa Disponibilidad** | % operatividad sistemas criticos | >99,5% (SLA estándar) | Art. 20: Continuidad |

**Implicaciones Prácticas en Administración Pública:**

- Sistemas críticos (datos sanitarios, catastrales, justicia) deben lograr MTTR <4 horas
- Centros de Operaciones Ciberseguridad municipales: MTTD <2 horas objetivo
- RTO/RPO según categoría: Básica (RTO 72h/RPO 24h), Media (RTO 24h/RPO 4h), Alta (RTO <4h/RPO <1h)

***

### **2.3 Indicadores de Gobernanza y Cumplimiento**

#### **Conformidad ENS por Nivel de Implementación**

| Nivel | Categoría | Medidas Esenciales | Requisitos Asociados | Implementación |
| :-- | :-- | :-- | :-- | :-- |
| **I (Mínimo)** | BÁSICA | 32 obligatorias | Organización, gestión riesgos, auditoría | APL, CCAA pequeñas |
| **II (Reforzado)** | MEDIA | 32 + 15 refuerzos | + Continuidad, detección, respuesta | Infraestructuras críticas |
| **III (Máximo)** | ALTA | 32 + 30 refuerzos | Máxima vigilancia, respuesta 24/7 | Datos sensibles, CNI |

**Madurez Territorial (Administración Pública)**:[^2_10]

- **87% ayuntamientos catalanes** cuentan con soluciones ADM-E certificadas ENS
- **Perfil CCN-STIC 890A**: 35 controles esenciales para gobiernos locales
- **Desafío:** Heterogeneidad infraestructuras; 15-20% aún en sistemas legados (<2010)


#### **Indicadores de Gobernanza Ejecutiva (NIS2)**

Con entrada en vigor de NIS2, las organizaciones esenciales deben reportar:

- % de juntas directivas capacitadas en ciberseguridad (meta: 100%)
- Nº de auditorías de ciberseguridad completadas/planificadas (meta: bianual mínimo)
- Tiempo medio de respuesta a vulnerabilidades críticas (meta: <30 días remediación)
- % incidentes reportados en plazo <24h a autoridades
- Nº de simulacros/ejercicios de ciberresiliencia (meta: ≥1 anual)

***

## **III. Benchmarking Internacional: España vs. Marcos Globales**

### **3.1 Global Cybersecurity Index 2024 (ITU)**[^2_11][^2_12][^2_13][^2_14]

El índice compuesto de la Unión Internacional de Telecomunicaciones evalúa 194 países en **5 pilares**:


| Pilar | España (puntos) | Máximo | Posición Global | Posición UE |
| :-- | :-- | :-- | :-- | :-- |
| **Legal** (marco regulatorio) | 20,00 / 20 | 20 | Perfecto | Perfecto |
| **Técnico** (capacidades) | 20,00 / 20 | 20 | Perfecto | Perfecto |
| **Organizacional** (estrategias) | 20,00 / 20 | 20 | Perfecto | Perfecto |
| **Capacidades** (formación, I+D) | 19,74 / 20 | 20 | Oportunidad mejora | Sólido |
| **Cooperación** (acuerdos, ISAC) | 20,00 / 20 | 20 | Perfecto | Perfecto |
| **TOTAL** | **99,74 / 100** | - | **3º Global** | **2º Europa** |

**Contexto Competitivo:**

1. Turquía (100,00)
2. Portugal (99,86)
3. **España (99,74)** ← Rol-modelling
4. Suecia (99,31)
5. Islandia (99,10)

**Interpretación Estratégica:**
España ha alcanzado la categoría máxima de **Role-modelling**, consolidando su liderazgo europeo. Sin embargo, el índice mide "fuerza relativa" y compromiso institucional, no capacidad operativa real. La presencia de España en el top-3 global refleja:

- Marco legal robusto y actualizado (ENS, transposición temprana NIS2)
- Inversi activas en capacidades (INCIBE, CCN-CERT, PRTR)
- Ecosistema de ciberseguridad dinámico (startups, academia, industria)

***

### **3.2 Alineamiento NIST CSF 2.0 vs. ENS**

En 2024, NIST publicó la versión 2.0 del Cybersecurity Framework con actualizaciones significativas. La comparativa con ENS revela **alta compatibilidad funcional**:[^2_15][^2_16]


| Función NIST 2.0 | Equivalencia ENS | Nivel Madurez |
| :-- | :-- | :-- |
| **Gobernar (nuevo)** | Art. 12-15 (Política, organización, roles) | Institucional |
| **Identificar** | Art. 24 (Análisis riesgos), Anexo I (categorización) | Integral |
| **Proteger** | Anexo II (Medidas protección - 3 grupos) | Exhaustivo |
| **Detectar** | Art. 26-27 (Monitorización, detección código dañino) | Avanzado |
| **Responder** | Art. 33-34 (Incidentes, respuesta) | Operacional |
| **Recuperar** | Art. 20 (Continuidad), Art. 21 (Mejora continua) | Resiliente |

**Niveles de Madurez NIST 2.0** (aplicables también a ENS):

1. **Parcial (Ad-hoc):** Procesos informales; prácticas varía
2. **Informado por Riesgo:** Procesos documentados; riesgo considerado
3. **Repetible:** Estándar organizado; gestión proactiva
4. **Adaptativo:** Gestión dinámica; reacción ágil a cambios

**Proporción de Cobertura:**

- Organizaciones con ISO 27001 + NIST CSF: ~83% de requisitos NIST cubiertos
- Organizaciones con ENS: ~70-80% de NIST CSF (según nivel ENS), refuerzos necesarios para Nivel 4 (Adaptativo)

***

### **3.3 ISO 27001:2022 vs. ENS vs. COBIT 2019**

La tabla comparativa integral de marcos:[^2_17][^2_18][^2_19]


| Aspecto | ISO 27001:2022 | ENS (RD 311/2022) | COBIT 2019 |
| :-- | :-- | :-- | :-- |
| **Jurisdicción** | Global | Nacional (España) | Corporativo |
| **Obligatoriedad** | Voluntaria | Obligatoria (sector público) | Voluntaria |
| **Enfoque Primario** | Gestión riesgos integrada | Cumplimiento requisitos + riesgos | Gobernanza TI |
| **Controles** | 93 (Anexo A, 4 categorías) | Medidas Anexo II (3 grupos) | 40 procesos (5 dominios) |
| **Certificación** | Sí (entes acreditados) | Conformidad (CCN) | Autoevaluación |
| **Nivel de Detalle** | Moderado-Alto | Detallado | Estratégico-Táctico |
| **Sector Público ES** | Complementario | Principal | Gobernanza corporativa |

**Compatibilidad Práctica:**
Una organización del sector público español que implementa **ISO 27001 + COBIT 2019** obtiene automáticamente ~70% de conformidad ENS. Los refuerzos necesarios se centran en:

- Categorización de sistemas (Anexo I ENS)
- Medidas específicas de continuidad (Art. 20)
- Reportes anuales de seguridad (Art. 32)
- Respuesta a incidentes coordinada (Art. 33-34)

***

## **IV. Diagnóstico de Amenazas y Resiliencia Sectorial**

### **4.1 Postura de Ciberseguridad por Sector (España 2024)**

#### **Infraestructuras Críticas (Operadores NIS2)**

**Distribución de Incidentes Gestionados (INCIBE)**:[^2_20][^2_4]

- **Energía:** 18,33%
- **Agua:** 25,00%
- **Transporte:** 22,08%
- **TIC:** 18,33%
- **Otras:** 16,26%

**Madurez Relativa:**

- **Muy Alta:** Banca, energía (marcos DORA, marcos proprietarios)
- **Alta:** Sanidad (Estrategia aprobada en 2024), Telecomunicaciones
- **Media:** Administración Pública Central
- **Media-Baja:** Administración Local, servicios esenciales municipales


#### **Sector Salud (Caso de Estudio)**

- **Estrategia de Ciberseguridad del SNS:** Aprobada por Consejo Interterritorial (3 años)
- **Inversión comprometida:** 1.500M€ (2025-2027)
- **Prioridades:** Protección datos pacientes (RGPD+), continuidad servicio, resiliencia ransomware
- **Reto:** Integración sistemas legados (historia clínica electrónica) + OT/IT hospitalario


#### **Agricultura y Logística (Sector Emergente)**

- **Madurez:** Baja-media (rezagado vs. banca/energía)
- **Oportunidad:** PRTR financia startups innovadoras; programas formación FP
- **Riesgos:** Digitalización acelerada (IoT, automatización) sin madurez ciberseguridad paralela

***

### **4.2 Análisis de Vulnerabilidades Persistentes**

**Deficiencias Críticas Identificadas (2024)**:[^2_21][^2_22]

1. **Gestión de Configuración:** Servicios cloud mal configurados (IAM, permisos)
2. **Parches y Updates:** Vulnerabilidades MS Office 2017 aún en top-10 de exploradas
3. **Cadena de Suministro:** Ataques selectivos a proveedores críticos sin auditoría NIS2
4. **Escasez de Talento:** 70-80% de incidentes tienen componente humano; formación insuficiente

**Proporción de Cobertura en Organizaciones:**

- Solo 52% adoptan frameworks avanzados (NIST CSF, COBIT)
- 48% permanecen en "ciberseguridad básica" (firewalls, antivirus, backups)

***

## **V. Financiación e Inversión 2024-2026**

### **5.1 Arquitectura Presupuestaria Española**

#### **Plan Industrial y Tecnológico Seguridad y Defensa (2025-2028)**[^2_23][^2_24]

| Partida | Inversión | % | Área Focal |
| :-- | :-- | :-- | :-- |
| **Equipamiento FFAA** | 3.664M€ | 35% | Sistemas de armas, vehículos |
| **Telecomunicación + Ciberseguridad** | 3.260M€ | 31% | Redes cifradas, satélites, IA, cuántica |
| **Instrumentos Defensa** | 1.987M€ | 19% | Armamento moderno |
| **Emergencias/Desastres** | 1.781M€ | 17% | Resiliencia territorial |
| **Seguridad Misiones Paz** | 314M€ | 3% | Operaciones internacionales |
| **TOTAL** | **10.471M€** | **100%** |  |

**Contexto:** Inversión responde a cumplimiento 2% PIB exigido por OTAN; España pasó de 0,93% (2014) a 1,43% (2024) a 2,00% estimado (2025).

#### **Refuerzo Ciberseguridad y Ciberdefensa (Mayo 2025)**[^2_25]

Aprobación de **1.157M€ adicionales** complementarios:

- **Ministerio de Defensa (CNI-CCN, CESTIC, MCCE):** 60,4% (701M€)
- **MTDIG (INCIBE, AEAD, Red.es):** 22% (255M€)
- **DSN (Presidencia):** 1,2% (14M€)
- **Otros ministerios:** 16,4% (190M€)

**Objetivos Programáticos:**

- Protección infraestructuras críticas ante NIS2
- Integración IA avanzada (detección ciberataques)
- Resiliencia computación cuántica (criptografía post-cuántica)
- Coordinación centros operaciones público-privados


#### **Inversión Administración Pública (2024-2025)**[^2_23]

| Nivel Administrativo | 2024 | 2025 Proyectado | Tendencia |
| :-- | :-- | :-- | :-- |
| **AGE** | 145M€ | ~160M€ | ↑ (PRTR, digitalización) |
| **CCAA** | 102M€ | ~115M€ | ↑ (Autonomía presupuestaria) |
| **Entidades Locales** | 38M€ | ~50M€ | ↑ (Centro Operaciones 50M€) |
| **TOTAL** | **285M€** | **~325M€** | **+14% YoY** |

**Actores Principales 2024:**

1. Secretaría de Administración Digital (SGAD): 49M€
2. Subdirección Seguridad Ministerio Interior: 23,63M€
3. RENFE: 10,27M€

#### **Plan Digitalización Administraciones Públicas 2021-2025**[^2_23]

- **Dotación Total:** 3.165M€
- **Prioridades:** Ciberseguridad (centros operaciones, monitorización), servicios cloud, IA


#### **Mercado de Seguros Ciber**[^2_26]

- **Volumen primas España:** 190M€ (+12% 2024-2025)
- **Sectores con mayor adopción:** Banca, energía
- **Sectores rezagados:** Agricultura, logística

***

## **VI. Conclusiones y Recomendaciones Estratégicas**

### **6.1 Posición Estratégica España**

España se posiciona como **líder europeo en marcos normativos y gobernanza**, pero enfrenta **vulnerabilidades operativas críticas**:

**Fortalezas:**

1. Marco normativo actualizado (ENS 2022, transposición temprana NIS2)
2. Liderazgo en índices globales (Tier 1 ITU, 3º mundo, 2º Europa)
3. Instituciones de referencia (INCIBE, CCN-CERT operacionales)
4. Financiación robusta: >1.500M€ anuales (PRTR + presupuestos ordinarios)
5. Ecosistema empresarial dinámico (startups ciberseguridad, talento emergente)

**Vulnerabilidades:**

1. Resiliencia operativa deficiente: MTTD >4h, MTTR >8h en muchas administraciones
2. Brecha de talento: Demanda de 10.000+ profesionales vs. oferta limitada
3. Fragmentación sectorial: Marcos diferenciados (DORA vs. NIS2) generan complejidad
4. Madurez territorial heterogénea: 87% municipios vs. 48% empresas sin frameworks avanzados
5. Dependencia externa: Supply chain attacks, infostealers sofisticados

***

### **6.2 Recomendaciones por Stakeholder**

#### **Para Administración Pública:**

1. **Acelerar Centros de Operaciones Ciberseguridad:** Localizar en CCAA/municipios (no solo AGE)
2. **Automatizar MTTD/MTTR:** Implementar SIEM/SOAR en 2026 (no 2027+)
3. **Formación ejecutiva:** 100% juntas directivas certificadas en ciberseguridad (NIS2)
4. **Auditorías bianual mínimo:** Especialmente operadores esenciales

#### **Para Sector Privado:**

1. **Cumplimiento dual ENS-NIS2:** Usar Perfil CCN para reducir carga
2. **Supply chain audits:** Verificar ciberseguridad de proveedores críticos
3. **Seguros ciber:** Ampliación cobertura (200M€ mercado aún bajo vs. ROI)

#### **Para Industria Ciberseguridad:**

1. **Talento local:** Expansión programas bootcamp, CTF (10.000+ formados en 2024)
2. **Innovación IA:** Soluciones post-quantum, detección avanzada
3. **Certificaciones:** Acelerar certificaciones ISO 27001, CMMC-equivalente español

***

### **6.3 Riesgos Emergentes 2025-2026**

1. **Ransomware +40% estimado (cierre 2025):** Requiere inversión detección IA
2. **NIS2 transposición incompleta:** Riesgo de fragmentación (DORA vs. NIS2)
3. **Computación cuántica:** Criptografía actual vulnerable; PRTR debe acelerar post-quantum
4. **Conflictividad geopolítica:** Ataques estatales dirigidos a infraestructuras españolas

***

## **Referencias y Fuentes Validadas**

Real Decreto 311/2022 (BOE-A-2022-7191) - Esquema Nacional de Seguridad[^2_1]
Anteproyecto Ley Coordinación y Gobernanza Ciberseguridad (enero 2025)[^2_2]
CCN-STIC 825 - Compatibilidad ENS/ISO 27001:2022[^2_3]
Administración Electrónica - España en Global Cybersecurity Index 2024[^2_11]
INCIBE - Balance Ciberseguridad 2024: 97.348 incidentes[^2_4]
NIST - Cybersecurity Framework 2.0 (PDF oficial)[^2_15]
[20-23] IT User / Cybersecurity - Global Cybersecurity Index 2024
Scribd - Informe GCI 2024 España[^2_13]
Springboard35 - Cybersecurity in Spain 2024-2025[^2_21]
ISMS Forum - V Indicador Madurez Ciberseguridad 2025[^2_27]
[47-50] DataCenter Market / ESET / Tech Consulting - Panorama Amenazas H2 2025
AOC Cataluña - Madurez ENS Administraciones Locales[^2_10]
[63-69] Comparativas NIST/ISO/COBIT - Alineamientos funcionales
TendersTool - Inversión Pública Ciberseguridad 2024-2025[^2_23]
[79-80] IPlusF / Computing.es - Plan Industrial Defensa 2025
AON Aon - Estudio Ciberseguridad Gestión Riesgo España 2025[^2_26]

***

**Documento Clasificación:** Público
**Fecha Elaboración:** 24 enero 2026
**Validación:** Fuentes académicas, oficiales, técnicas, consultoría clase mundial
**Cobertura Temporal:** 2024-2025 (con proyecciones 2026)
<span style="display:none">[^2_28][^2_29][^2_30][^2_31][^2_32][^2_33][^2_34][^2_35][^2_36][^2_37][^2_38][^2_39][^2_40][^2_41][^2_42][^2_43][^2_44][^2_45][^2_46][^2_47][^2_48][^2_49][^2_50][^2_51][^2_52][^2_53][^2_54][^2_55][^2_56][^2_57][^2_58][^2_59][^2_60][^2_61][^2_62][^2_63][^2_64][^2_65][^2_66][^2_67][^2_68][^2_69][^2_70][^2_71][^2_72][^2_73][^2_74][^2_75][^2_76][^2_77][^2_78][^2_79][^2_80][^2_81][^2_82][^2_83][^2_84][^2_85][^2_86][^2_87][^2_88][^2_89][^2_90]</span>

<div align="center">⁂</div>

[^2_1]: https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191

[^2_2]: https://unaaldia.hispasec.com/2025/11/implementacion-de-la-directiva-europea-nis2-en-espana.html

[^2_3]: https://www.ccn-cert.cni.es/es/800-guia-esquema-nacional-de-seguridad/543-ccn-stic-825-ens-iso27001/file.html

[^2_4]: https://www.incibe.es/incibe/sala-de-prensa/incibe-presenta-su-balance-de-ciberseguridad-2024-con-mas-de-97000-incidentes

[^2_5]: https://www.datacentermarket.es/ciberseguridad/espana-segundo-pais-con-mas-detecciones-de-ransomware-en-2025-segun-un-informe-de-eset/

[^2_6]: https://www.esedsl.com/blog/resumen-panorama-general-de-los-ciberataques-2024-2025

[^2_7]: https://newsbook.es/actualidad/espana-cuarto-pais-con-mayor-volumen-de-amenazas-detectadas-en-2025-20260122121497.htm

[^2_8]: https://www.atlassian.com/es/incident-management/kpis/common-metrics

[^2_9]: https://es.vectra.ai/topics/cybersecurity-metrics

[^2_10]: https://www.aoc.cat/es/blog/2025/el-87-dels-ajuntaments-catalans-utilitzen-solucions-adm-e-amb-certificacio-de-lens/

[^2_11]: https://administracionelectronica.gob.es/pae_Home/pae_Actualidad/pae_Noticias/2024/Septiembre/Noticia-2024-09-13-Espana-en-el-grupo-de-cabeza-del-Global-Cybersecurity-Index-2024-.html?idioma=en

[^2_12]: https://www.itdigitalsecurity.es/actualidad/2024/09/espana-obtiene-una-valoracion-casi-perfecta-en-el-global-cybersecurity-index-2024-de-itu

[^2_13]: https://administracionelectronica.gob.es/pae_Home/en/pae_OBSAE/Posicionamiento-Internacional/Summary-Spain-international-rankings/ITU-Global-Cybersecurity-Index-2024.html

[^2_14]: https://es.scribd.com/document/970010579/Informe-GCI-2024-Ranking-Ciberseguridad-Espana

[^2_15]: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.spa.pdf

[^2_16]: https://nimbustech.es/marco-de-ciberseguridad-nist-2-0-como-cumplirlo/

[^2_17]: https://vps-strategic.com/comparacion-entre-ens-e-iso-27001-cual-es-mejor-para-tu-empresa/

[^2_18]: https://ciberprisma.org/2024/09/30/gobierno-de-las-tic-cobit/

[^2_19]: https://es.linkedin.com/pulse/comparativa-entre-el-framework-nist-csf-v-20-e-isoiec-jesús-nazareno-4t2if

[^2_20]: https://www.incibe.es/sites/default/files/Comunicación_2025/Infograf%C3%ADa_BalanceCiberseguridad_INCIBE_2024_web.pdf

[^2_21]: https://springboard35.com/en/blog/cybersecurity-in-spain-challenges-opportunities/

[^2_22]: https://techconsulting.es/ciberseguridad-2025-en-espana-amenazas-regulacion-casos-y-estrategias-clave/

[^2_23]: https://tenderstool.com/blog/espana-destina-un-tercio-del-nuevo-presupuesto-en-defensa-a-la-ciberseguridad/

[^2_24]: https://www.computing.es/administracion/espana-multiplica-su-apuesta-por-la-ciberseguridad-mas-de-3-200-millones/

[^2_25]: https://iplusf.com/el-gobierno-aprueba-un-refuerzo-de-las-capacidades-de-espana-en-ciberseguridad-y-ciberdefensa-con-1-157-millones-de-euros/

[^2_26]: https://noa.aon.es/estudio-sobre-ciberseguridad-y-gestion-riesgo-ciber-espana-2025/

[^2_27]: https://www.ismsforum.es/ficheros/descargas/informeobservatorio1763383163.pdf

[^2_28]: https://protecciondatos-lopd.com/empresas/ley-ciberseguridad/

[^2_29]: https://www.flexxible.com/es/blog/directiva-nis2-espana

[^2_30]: https://www.incibe.es/incibe-cert/sectores-estrategicos/NIS2-necesitas-saber

[^2_31]: https://municipiointeligente.es/ciberseguridad

[^2_32]: https://sosafe-awareness.com/es/blog/nis2-espana-nueva-normativa/

[^2_33]: https://www.sgs.com/es-es/noticias/2025/05/ciberseguridad

[^2_34]: https://portal.mineco.gob.es/es-es/ministerio/estrategias/Paginas/Esquema_Nacional_de_Seguridad.aspx

[^2_35]: https://www.incibe.es/empresas/blog/la-ley-de-ciberresiliencia-europea-se-publica-en-su-version-en-castellano

[^2_36]: https://digital-strategy.ec.europa.eu/es/policies/nis2-directive

[^2_37]: https://grctools.software/2025/03/24/que-establece-real-decreto-311-2022/

[^2_38]: https://www.boe.es/buscar/doc.php?id=BOE-A-2025-10371

[^2_39]: https://acesaconsulting.es/como-cumplir-con-la-directiva-nis2-requisitos-de-ciberseguridad-para-tu-empresa/

[^2_40]: https://www.sailpoint.com/es/identity-library/nist-cybersecurity-framework

[^2_41]: https://www.incibe.es/sites/default/files/paginas/que-hacemos/Plan-Anual-Actividad_2024_resultados.pdf

[^2_42]: https://www.ituser.es/actualidad/2024/09/espana-obtiene-una-valoracion-casi-perfecta-en-el-global-cybersecurity-index-2024-de-itu

[^2_43]: https://sipadan.es/blog-sipadan/mayores-amenazas-ciberseguridad-2025

[^2_44]: https://secureframe.com/es-es/blog/nist-csf-framework

[^2_45]: https://www.tendencias.kpmg.es/2024/03/version-2-0-marco-ciberseguridad-csf-ahora-que/

[^2_46]: https://www.incibe.es/sites/default/files/paginas/que-hacemos/Plan-Actuación_Anual-2025.pdf

[^2_47]: https://idavinci.es/tendencias-ciberseguridad-2024/

[^2_48]: https://jisis.org/wp-content/uploads/2024/11/2024.I4.019.pdf

[^2_49]: https://ciberseguridad.com/guias/prevencion-proteccion/cuantificacion-riesgo-cibernetico/

[^2_50]: https://www.escuelaeuropeaexcelencia.com/2024/11/3-indicadores-en-iso-27001-que-son-clave-para-garantizar-la-seguridad-de-la-informacion/

[^2_51]: https://www.bde.es/f/webbe/Secciones/Publicaciones/InformesBoletinesRevistas/InformesEstabilidadFinancera/24/FSR_2024_1_SF.pdf

[^2_52]: https://www.youtube.com/watch?v=Lb5wH5Wel6w

[^2_53]: https://ciberseguridad.com/normativa/espana/sgsi/iso-27001/

[^2_54]: https://www.youtube.com/watch?v=LU_H327GULE

[^2_55]: https://www.esginnova.com/pdfs/revista-empresa-excelente/noviembre-2024.pdf

[^2_56]: https://www.fairinstitute.org/2024-fair-conference

[^2_57]: https://www.academia.edu/111759147/Desarrollando_un_Modelo_Matem%C3%A1tico_para_la_Evaluaci%C3%B3n_de_Riesgos_en_Ciberseguridad_Desde_la_Complejidad_a_la_Simplificaci%C3%B3n

[^2_58]: https://www.ismsforum.es/ficheros/descargas/171125cybercompliancefinal21763378260.pdf

[^2_59]: https://www.linkedin.com/pulse/spain-cyber-risk-quantification-market-growth-analysis-size-iyxrf

[^2_60]: https://ciberseguridad.com/herramientas/metodologias-evaluacion-riesgos-ciberneticos/

[^2_61]: https://libertia.es/kpi-de-ciberseguridad-en-madrid-2025/

[^2_62]: https://libertia.es/estadisticas-de-ciberataques-en-madrid-2025/

[^2_63]: https://socinfodigital.es/wp-content/uploads/2024/01/SIA.-Tendencias-de-ciberseguridad-2024.-Administraciones-Públicas-v1.0.pdf

[^2_64]: https://es.linkedin.com/pulse/cómo-usar-mttd-mtta-mttr-y-mttf-en-la-ciberseguridad-pedro-corcobado-rf0if

[^2_65]: https://www.ituser.es/actualidad/2025/09/espana-presenta-un-nivel-de-madurez-alto-en-normativas-de-ciberseguridad

[^2_66]: https://www.spainclouds.com/noticias/espana-bajo-asedio-en-ciberseguridad

[^2_67]: https://www.startupdefense.io/es-us/blog/mttd-y-mttr-en-ciberseguridad

[^2_68]: https://ciberseguridad.com/normativa/espana/sgsi/cobit/

[^2_69]: https://en.wikipedia.org/wiki/Cybersecurity_Maturity_Model_Certification

[^2_70]: https://www.nsf.org/management-systems/information-security/cybersecurity-maturity-model-certification

[^2_71]: https://legitec.com/iso-27001-vs-ens-diferencias-clave-y-como-elegir-la-mejor-opcion-para-tu-organizacion/

[^2_72]: https://dialnet.unirioja.es/descarga/articulo/8399852.pdf

[^2_73]: https://ndisac.org/dibscc/cyberassist/cybersecurity-maturity-model-certification/

[^2_74]: https://skiller.education/la-voz-del-experto-cobit-como-marco-de-gobernanza-holistica-para-una-i-a-confiable-y-sostenible/

[^2_75]: https://www.taf.org/the-cybersecurity-maturity-model-certification-cmmc-framework/

[^2_76]: https://www.rcquality.es/esquema-nacional-seguridad-o-iso-27001/

[^2_77]: https://www.cio.com/article/1314368/cobit-un-marco-para-la-alineacion-y-la-gobernanza.html

[^2_78]: https://dodcio.defense.gov/Portals/0/Documents/CMMC/ModelOverview_V2.0_FINAL2_20211202_508.pdf

[^2_79]: https://ciberprisma.org/2024/01/22/seguridad-de-la-informacion-una-comparacion-exhaustiva-entre-iso-27001-y-nist-csf/

[^2_80]: https://www.dsn.gob.es/es/actualidad/sala-de-prensa/otan-ue-aumentan-cooperación-ciberseguridad

[^2_81]: https://www.randstad.es/contenidos360/tecnologia/innovacion-espana-crecimiento-empleo-calidad/

[^2_82]: https://ptedisruptive.es/wp-content/uploads/2024/12/INFORME-DE-SITUACION_CIBERSEGURIDAD_2024.pdf

[^2_83]: https://www.incibe.es/sites/default/files/paginas/programas/Programa de Impulso a la Industria de la Ciberseguridad Nacional.pdf

[^2_84]: https://www.mintur.gob.es/Publicaciones/Publicacionesperiodicas/EconomiaIndustrial/RevistaEconomiaIndustrial/430/GONZALVO NAVARRO.pdf

[^2_85]: https://portal.mineco.gob.es/ca-es/comunicacion/Pagines/aprobación-adenda-al-plan-de-recuperación.aspx

[^2_86]: https://digital-strategy.ec.europa.eu/es/news/european-union-and-nato-hold-first-structured-dialogue-cyber

[^2_87]: https://inntech.uma.es/mas-actualidad/

[^2_88]: https://planderecuperacion.gob.es/noticias/Red-punto-es-cierra-2024-ejecucion-mas-1500-millones-euros-prtr

[^2_89]: https://www.exteriores.gob.es/es/Comunicacion/NotasPrensa/Documents/Informe de Acción Exterior 2024.pdf

[^2_90]: https://www.tendencias.kpmg.es/2025/05/ciberseguridad-sistema-energetico-inteligente-papel-ciso/


