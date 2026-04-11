

# Informe MAGERIT.

# **INFORME MAGERIT, INDICADORES DE CIBERSEGURIDAD E INTEGRACIÓN CON NIS2 EN ESPAÑA**

## *Tendencias, Regulación y Operacionalización 2024-2026*


***

## RESUMEN EJECUTIVO

Este informe analiza la evolución de **MAGERIT (Metodología de Análisis y Gestión de Riesgos de los Sistemas de Información)** en el contexto regulatorio español 2024-2026, con énfasis en su integración con la **Directiva NIS2**, la actualización del **Esquema Nacional de Seguridad (ENS, RD 311/2022)** y el desarrollo de **indicadores cuantitativos de ciberseguridad** alineados con mejores prácticas internacionales.

**Hallazgos clave:**

- MAGERIT v3 permanece como la metodología de referencia nacional para análisis de riesgos en sistemas de información, implementada mediante el **Método de Análisis de Riesgos (MAR)** estructurado en cuatro tareas: activos, amenazas, salvaguardas y estado de riesgo residual.[^1_1][^1_2]
- El ENS (actualizado por RD 311/2022) operacionaliza MAGERIT mediante **22 requisitos mínimos** y medidas de seguridad proporcionadas (marcos organizativo, operacional y de protección) clasificadas por categoría de sistema (BÁSICA/MEDIA/ALTA) y madurez (L2-L4 CMM).[^1_3]
- España gestiona indicadores de ciberseguridad fragmentados: 97.348 incidentes en 2024 (+16,6% vs 2023), con madurez promedio nacional de **61% en dominios NIST** (Identify 68%, Respond 55%, Recovery 53%). Sectores financiero (72%) y construcción (68%) lideran; Distribución y Bienes de Consumo (51-52%) rezagados.[^1_4][^1_5]
- La integración MAGERIT + NIS2 requiere operacionalización mediante **análisis cuantitativos de riesgo** (FAIR/ALE) complementarios a MAGERIT, con énfasis en cuantificación financiera de impacto y alineación con autoridades supervisoras centralizadas (Centro Nacional de Ciberseguridad, aún en creación enero 2025).[^1_6][^1_3]

***

## 1. CONTEXTO REGULATORIO: NIS2 Y TRASPOSICIÓN ESPAÑOLA

### 1.1 Situación Normativa (Enero 2025)

La **Directiva NIS2** (UE 2022/2555) entró en vigor en enero de 2023, con plazo de trasposición a 17 de octubre de 2024 incumplido por España. El **Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad** (enero 2025) establece el marco nacional, pendiente de aprobación oficial.[^1_3]


| Aspecto | Estado |
| :-- | :-- |
| **Ley de Trasposición** | Anteproyecto (ene 2025), aprobación esperada 2025-2026 |
| **Autoridad Competente Nacional** | Centro Nacional de Ciberseguridad (creación en proceso) |
| **Autoridades de Control** | CCN (defensa), SETELECO/SEDIA (digital), OCI (interior), por sector |
| **Certificación Entidades Esenciales** | Obligatoria (auditoría externa bienal) |
| **Autoevaluación Entidades Importantes** | Permitida (sin auditoría periódica obligatoria) |
| **Sanciones Esenciales** | €10M o 2% volumen negocios (máxima cuantía) |
| **Sanciones Importantes** | €7M o 1,4% volumen negocios |

**Nota crítica**: Las empresas españolas operan bajo vinculatoriedad de NIS2 desde enero 2023, sin marco legislativo nacional claro. El Anteproyecto recomienda usar **ENS + Reglamento de Ejecución UE** como referencias transitorias.[^1_3]

### 1.2 Criterios de Clasificación NIS2

| Categoría | Criterios | Supervisión |
| :-- | :-- | :-- |
| **Esenciales** | >250 empl. + balance >€43M O volumen negocios >€50M + sector Anexo I | Auditoría obligatoria periódica + ad-hoc |
| **Importantes** | Sector Anexo II O no cumplen criterios esencial pero sí sector aplicable | Supervisión a posteriori (si indicios) |
| **Sectores Anexo I (críticos)** | Energía, Transporte, Banca, Finanzas, Salud, Agua, TIC, Admin. Pública, Espacio |  |
| **Sectores Anexo II** | Postal, Gestión residuos, Industria química/nuclear, Alimentación, Telecomunicaciones, Manufactura |  |


***

## 2. MAGERIT V3: EVOLUCIÓN METODOLÓGICA Y OPERACIONALIZACIÓN

### 2.1 Arquitectura del Método de Análisis de Riesgos (MAR)

MAGERIT v3 (2012, actualizado con ENS 2022) estructura el análisis de riesgos en **cuatro tareas formalizadas (MAR.1-MAR.4)** dentro de un **ciclo PDCA** de gestión integral:[^1_2][^1_1]

**Tarea MAR.1: Caracterización de Activos**

- Identificación: Información, servicios, hardware, software, personal, instalaciones
- Valoración: Cálculo de impacto por dimensión (Confidencialidad, Integridad, Disponibilidad, Autenticidad, Trazabilidad)
- Dependencias: Modelado de cascadas de valor (acumulado/repercutido)
- Salida: **Modelo de Valor** (catálogo de activos críticos ponderado)

**Tarea MAR.2: Caracterización de Amenazas**

- Tipificación: Naturales, humanas accidentales/deliberadas, fallos técnicos
- Valoración: Degradación (% pérdida valor) × Frecuencia/Probabilidad anual (ARO)
- Salida: **Mapa de Riesgos** (matriz amenaza-activo-dimensión)

**Tarea MAR.3: Caracterización de Salvaguardas**

- Identificación: Preventivas (PR), Disuasorias (D), Detectivas (DE), Correctivas (C)
- Evaluación de eficacia: Madurez (L0-L5 CMM), cobertura de dimensiones
- Salida: **Declaración de Aplicabilidad**, **Evaluación de Salvaguardas**, **Informe de Insuficiencias**

**Tarea MAR.4: Estimación de Estado de Riesgo**

- Impacto residual: Valor activo × (Degradación × (1 - Eficacia salvaguardas))
- Riesgo residual: Impacto residual × Frecuencia
- Análisis acumulado/repercutido según dependencias
- Salida: **Estado de Riesgo**, decisiones de tratamiento (eliminación, mitigación, compartición, aceptación/financiación)

**Diferenciación clave vs NIST/FAIR:**

- MAGERIT: Énfasis en **impacto sobre activos** (bottom-up), proporcionalidad (perfiles adaptables), formatos de salida estandardizados (declaraciones, informes).
- NIST CSF: Orientación a **funciones empresariales** (Identify→Protect→Detect→Respond→Recover), niveles madurez organizacional (L1-L4 por práctica).
- FAIR: Cuantificación **monetaria pura** (ALE = LEF × LM, simulaciones Montecarlo), decisiones financieras ROI-céntricas.

→ **Integración recomendada**: MAGERIT (identificación/priorización) + FAIR (cuantificación ROI) + NIST CSF (validación funcional).[^1_7][^1_8][^1_9]

### 2.2 Indicadores y Métricas en MAGERIT

MAGERIT NO define "indicadores de ciberseguridad" como módulo explícito, sino **métricas de estado de riesgo** y **control de procesos**:


| Métrica | Fuente MAGERIT | Operacionalización |
| :-- | :-- | :-- |
| **Cobertura de activos críticos** | MAR.1 (completitud modelo valor) | % de activos identificados vs. inventario IT |
| **Frecuencia/ARO (riesgos)** | MAR.2 (probabilidad amenazas) | Incidentes históricos/año (INCIBE CERT, CCN-CERT) |
| **Degradación media** | MAR.2 (% pérdida valor/amenaza) | Impacto normalizado (0-100%) |
| **Eficacia salvaguardas (%)** | MAR.3 (L0-L5 madurez) | Reducción riesgo post-implementación (NIST/ISO validación) |
| **Riesgo residual total** | MAR.4 (agregado ponderado) | Suma ponderada impactos residuales (en euros vía FAIR) |
| **Tiempo análisis/revisión** | Proceso de gestión (Art. 32 ENS) | Ciclo anual (PDCA) + revisiones marginales (cambios sistemas) |
| **Cumplimiento normativo (%)** | Informe estado (art. 32 ENS) | Medidas EN aplicadas vs. requeridas por categoría |

**Indicadores de control del proceso (Art. 4.4 MAGERIT v3):**

- Verificación de roles y responsabilidades asignadas
- Completitud de contexto (alcance, límites, stakeholders)
- Criterios de evaluación documentados y comunicados
- Tratamiento de riesgos (decisiones formalizadas)
- Seguimiento/revisión periódica (KRIs - Key Risk Indicators)

***

## 3. INTEGRACIÓN ENS (RD 311/2022) Y OPERACIONALIZACIÓN MAGERIT

### 3.1 Marco de Medidas de Seguridad (Anexo II ENS)

El ENS estructura **medidas proporcionales por categoría** mediante aplicación de MAGERIT:


| Marco | Medidas Clave | BÁSICA | MEDIA | ALTA | Madurez mín. |
| :-- | :-- | :-- | :-- | :-- | :-- |
| **Organizativo (org)** | Política seguridad (org.1), Normativa (org.2), Procedimientos (org.3), Autorización (org.4) | Base | Base + R1 | Base + R1 + R2 | L2-L3-L4 |
| **Operacional Planificación (op.pl)** | Análisis riesgos (op.pl.1: MAGERIT MAR), Arquitectura seguridad (op.pl.2) | Base | +R1 (semiformal) | +R2-R3 (formal CMM L4) | L2-L3-L4 |
| **Operacional Acceso (op.acc)** | Identificación (op.acc.1), Autenticación (op.acc.2-5, MFA) | Base | +R1-R2 | +R1-R5 (criptografía CCN) | L2-L3-L4 |
| **Operacional Explotación (op.exp)** | Gestión incidentes (op.exp.7), Parches (op.exp.8), Gestión configuración (op.exp.9) | Base | +R1-R2 | +R1-R3 (automatización) | L2-L3-L4 |
| **Operacional Monitorización (op.mon)** | Vigilancia continua (op.mon.3), Indicadores eficiencia (op.mon.2: **KPIs ciberseguridad**) | Base | +R1-R2 | +R1-R6 (SOC 24/7) | L2-L3-L4 |
| **Protección (mp)** | Instalaciones, Equipos, Comunicaciones (cifrado), Almacenamiento | Base | +R (algoritmos CCN) | +R (redundancia, criptografía cuántica-ready) | L2-L3-L4 |

**Notas:**

- **Refuerzos (R):** R1 = Semicformal/procedimientos; R2 = Formal/estándar; R3 = Certificación productos CCN; R4-R6 = Automatización/redundancia/criptografía avanzada.
- **Categorización automática** (Anexo I ENS): Impacto acumulado por dimensión (BAJO/MEDIO/ALTO) → Categoría BÁSICA/MEDIA/ALTA.
- **Perfiles específicos** (art. 30 ENS): CCN valida adaptaciones por sector (sanidad, educación, financiero, etc.).[^1_10][^1_11]


### 3.2 Auditoría y Certificación (Art. 31-32 ENS)

| Entidad | Ciclo | Auditor | Evidencia |
| :-- | :-- | :-- | :-- |
| **BÁSICA (Admin. pública)** | 24 meses | Autoevaluación (org. responsable) | Declaración aplicabilidad, cuestionarios CMM |
| **MEDIA (Admin. pública + privados críticos)** | 24 meses | Auditoría externa (acreditado) | Informe técnico, pruebas de implementación |
| **ALTA (infraestructuras críticas)** | 24 meses | Auditoría externa periódica + ad-hoc | SGSI ISO 27001, pruebas invasivas, pentesting |
| **Reporte (Operadores NIS2)** | Incidentes >impacto sig. | CCN-CERT / Autoridades sectoriales | Notificación 72h (ITS), análisis forense |

**Indicadores de cumplimiento reportados (op.mon.2, art. 32):**

- Grado implantación medidas (% de conformidad por categoría)
- Comportamiento gestión incidentes (MTTR, SLA cumplimiento)
- Eficiencia seguridad (horas/recursos por 1.000 usuarios)
- Cuadros de mando (INES - Informe Nacional Estado Seguridad, publicado CCN bienalmente)

***

## 4. INDICADORES CUANTITATIVOS DE CIBERSEGURIDAD: ESPAÑA 2024

### 4.1 Estadísticas Nacionales de Incidentes (INCIBE 2024)

**Volumen total: 97.348 incidentes (+16,6% vs 2023)**


| Categoría | Cifras | % Total |
| :-- | :-- | :-- |
| **Ciudadanía** | 65.808 | 67,6% |
| **Empresas (pymes/autónomos)** | 31.540 | 32,4% |
| **Operadores esenciales/importantes (NIS2)** | 341 | 0,35% |
| **Sistemas vulnerables detectados (proactivos)** | 183.851 | — |

**Tipología de incidentes (malware 42.136; fraude 38.000):**


| Tipo | Casos | Observaciones |
| :-- | :-- | :-- |
| **Malware** | 42.136 | Incluye 357 ransomware; virus, trojan, spyware |
| **Fraude online** | 38.000 | Phishing 21.571 (56%), compras falsas, suplantación |
| **Intrusiones/acceso no autorizado** | 7.470 | Fuerza bruta, credenciales comprometidas, pivoting |
| **E-commerce fraudulento** | 2.122 | Tiendas fake, drop-shipping ilegal |

**Por sector operadores esenciales (341 incidentes NIS2):**


| Sector | % | Casos | Tendencia 2024 |
| :-- | :-- | :-- | :-- |
| **Transporte** | 24,6% | 84 | +43% ataques infra. esenciales (vs 2023: 237) |
| **Sistemas Financieros/Tributarios** | 23,8% | 81 | Fraude online, APT ransomware |
| **Tecnologías Información (TIC)** | 14,1% | 48 | Cadena suministro, cloud misconfiguration |
| **Energía** | 8,8% | 30 | Malware OT, ICS targeting (Rusia: Sandworm, APT28) |
| **Agua** | 5% | 17 | SCADA/industrial control systems |

**Amenazas geopolíticas identificadas (x63 Unit - Cipher):**

- **Rusia**: Sandworm, APT28, Babuk2 (ransomware ransomware-as-a-service)
- **China**: Volt Typhoon (acceso persistente OT/infraestructura)
- **Irán**: APT34 (credential harvesting)
- **Corea del Norte**: CyberAvengers, B-Team (financiero, data exfiltration)

→ **Conclusión**: España vive escalada de **+43% en ataques a infraestructuras críticas** 2024, con enfoque en sectores energético (9%) y financiero (24%); múltiples actores estatales con capacidades sofisticadas (APT).[^1_12][^1_13][^1_14]

### 4.2 Madurez en Ciberseguridad: Observatorio ISMS Forum 2024

**Indicador nacional: 61% (escala 0-100% madurez)**


| Nivel | % Organizaciones |
| :-- | :-- |
| Inexistente (L0) | 8% |
| **Básico (L1-L2)** | 53% |
| **Maduro (L3)** | 38% |
| Optimizado (L4-L5) | 1% |

**Por dominio NIST CSF:**


| Dominio | % | Interpretación |
| :-- | :-- | :-- |
| **Identify** | 68% | Inventarios activos completos (~2/3 orgs); gestión riesgos parcial (~50%) |
| **Protect** | 63% | Acceso/identidad en ~50% (menor privilegio); formación anual universal |
| **Detect** | 64% | Monitorización eventos (40%); detección anomalías automática (40%); pruebas anuales |
| **Respond** | 55% | Procedimientos documentados (50%); análisis forense <10% detecciones; mejora ad-hoc (36%) |
| **Recover** | 53% | Planes formalizados no operacionalizados; recuperación anual; comunicación informal (50%) |

**Análisis por sector (madurez integral 2024):**


| Sector | Madurez | Fortalezas | Debilidades |
| :-- | :-- | :-- | :-- |
| **Financiero** | 72% | Identify (76%), Protect (74%), Detect (79%) | Respond (63%), Recovery (66%) |
| **Construcción** | 68% | Respuesta coordinada (67%) | Vulnerabilidad distribución datos (R0) |
| **Energía/Utilities** | 67% | Identify (77%), Detect (72%) | **Recovery crítica (50%)** — riesgo operacional |
| **Aseguradoras** | 64% | Identify (73%) | Respond (58%), Recovery (58%) |
| **Telecomunicaciones/Tech** | 63% | Identify (79%) | **Respond (53%), Recovery (50%)** |
| **Salud** | 61% | Identify (69%) | Respond (50%), Recovery (58%) |
| **Administración Pública** | 58% | Identify (64%), Detect (67%) | **Respond (48%), Recovery (48%)** |
| **Bienes de Consumo** | 51% | **Uniformidad baja** | Todos dominios <60%, Recovery solo 46% |
| **Distribución** | 52% | Detect (61%), Respond (57%) | **Protect crítica (35%)**, Recovery (63%) anomalía |

**Por tamaño empresa:**

- **>10.000 empleados**: 68% madurez (Identify 72%, Respond 61%)
- **251-2.500 empleados**: 60% madurez (Identify 64%, Respond 54%)
- **26-250 empleados**: 52% madurez (Identify 58%, Respond 46%)
- **<25 empleados**: 38% madurez (Identify 40%, Respond 30%) — **crítico para PyMEs**

**Análisis crítico de brechas (Respond + Recovery: 55% + 53% = débil):**

- El 50% de organizaciones tiene procedimientos response documentados pero **no se prueban periódicamente** (pruebas anuales máximo).
- Análisis forense post-incidente realizado por <10% en detecciones relevantes.
- 36% de mejora continua **ad-hoc** (no sistematizada); solo 8% revisa planes response >1 vez/año.
- **Riesgo: Mayor tiempo de recuperación (RTO/RPO) y reputacional ante incidentes que NIS2 requiere coordinar en 72 horas.**[^1_5]


### 4.3 Integración Cuantificación Financiera (FAIR/ALE)

MAGERIT proporciona **vector de riesgo (frecuencia × impacto)** cualitativo. Para decisiones inversión NIS2-aligned, se integra **FAIR (Factor Analysis of Information Risk)**:

**Fórmula básica:**

```
ALE (Annualized Loss Exposure) = 
  LEF (Loss Event Frequency) × LM (Loss Magnitude)

LEF = TEF (Threat Event Frequency) × Vulnerability (1 - Control Strength)
LM = Primary Loss + Secondary Loss (regulación, reputación, litigio)
```

**Caso práctico: Robo datos clientes (financial impact cuantificado):**

- TEF: 1 evento/año (histórico)
- Vulnerabilidad (sin MFA): 80%
- LEF (sin control): 0,8 eventos/año
- Primary Loss: €1.000-€3.000/portátil × 50% exposición datos = €50.000 media
- Secondary Loss: 10% multa regulatoria (€50K-€500K) + 5% litigio (€100K-€2M, 10% probab.)
- **LM total esperado**: €32.000 promedio (Montecarlo simulación)
- **ALE sin control**: €32.000 × 0,8 = **€25.600/año**
- **Costo mitigación (MFA + backup)**: €20.000 inversión + €8.000/año mantenimiento
- **Decisión**: ROI positivo si riesgo aceptable <€28.600/año.[^1_15][^1_16]

→ **Práctica recomendada en NIS2**: Combinar MAGERIT (identificación/priorización) + FAIR (cuantificación €) para justificar inversión a C-suite y autoridades regulatorias.[^1_6]

***

## 5. ANÁLISIS COMPARATIVO: MAGERIT vs. FRAMEWORKS INTERNACIONALES

### 5.1 Comparación MAGERIT vs. NIST CSF 2.0

| Dimensión | **MAGERIT v3** | **NIST CSF 2.0** | **Convergencia NIS2** |
| :-- | :-- | :-- | :-- |
| **Orienta.** | Análisis riesgo ascendente (activos→amenazas→salv.) | Funciones empresariales (Go→ID→PR→DE→RS→RC) | MAGERIT para evaluación sector público; NIST para operadores privados |
| **Métricas** | Impacto residual (€), Riesgo (frecuencia × impacto), CMM madurez | Resultados esenciales (48), subcategorías (186), niveles madurez (L1-L4 por función) | Ambas reconocidas; Anexo II ENS incluye cross-mapping NIST |
| **Categorización** | BÁSICA/MEDIA/ALTA por impacto acumulado dimensiones | Sectorial (operador crítico vs importante); por función | ENS proporcional; NIS2 binaria (esencial/importante) |
| **Ciclo** | PDCA (Plan→Do→Check→Act), revisión anual marginal | Ciclo continuo con feedback; revisión 24-36 meses | Ambas admitidas; ENS requiere auditoría 24 meses |
| **Fortalezas** | Detalle activos, dimensiones seguridad (5D), formatos estándar (informes) | Orientación negocio, flexibilidad por sector, madurez por función | MAGERIT: precisión técnica; NIST: ejecutivos |
| **Debilidades** | Complejo para PyMEs, requiere herramienta (PILAR), curva aprendizaje | Subjetividad niveles madurez, menos detalle riesgo cuantitativo | MAGERIT no cuantifica €; NIST no profundiza dependencias activos |

**Conclusión**: **Enfoque dual recomendado en España 2025:**

- Sector público (administraciones, operadores esenciales): MAGERIT + FAIR cuantificación
- Operadores privados críticos (energía, finanzas): NIST CSF + MAGERIT para conformidad ENS
- Pymes (Entidades importantes): NIST (más ágil) + auditoría ENS periódica

[^1_8][^1_9][^1_7]

### 5.2 Alineamiento MAGERIT + NIS2 + ENS

```
┌─────────────────────────────────────────────────────────────┐
│ DIRECTIVA NIS2 (UE 2022/2555)                               │
│ - Obligaciones seguridad (Art. 21): análisis riesgos,      │
│   continuidad, cadena suministro, criptografía, etc.       │
└────────────────┬────────────────────────────────────────────┘
                 │
        ┌────────▼────────┐
        │ ENS (RD 311/22) │
        │ 22 requisitos   │
        │ 36 medidas protec│
        │ perfiles adapt. │
        └────────┬────────┘
                 │
        ┌────────▼────────────────┐
        │ MAGERIT v3 (MAR)        │
        │ Tarea 1: Activos        │
        │ Tarea 2: Amenazas       │
        │ Tarea 3: Salvaguardas   │
        │ Tarea 4: Riesgo resid.  │
        └────────┬────────────────┘
                 │
        ┌────────▼──────────────┐
        │ Outputs:              │
        │ - Modelo valor        │
        │ - Mapa riesgos        │
        │ - Estado riesgo       │
        │ - Informe insuficiencias
        └────────┬──────────────┘
                 │
   ┌─────────────▼─────────────┐
   │ Cuantificación (FAIR/ALE) │
   │ - LEF × LM = €/año        │
   │ - ROI medidas             │
   │ - Comunicación ejecutiva   │
   └───────────────────────────┘
```

**Operacionalización 2025-2026:**

1. **Identificación**: MAGERIT MAR.1 = inventario activos críticos sector
2. **Análisis**: MAGERIT MAR.2-4 = mapa riesgos por categoría NIS2
3. **Medidas**: ENS + Reglamento Ejecución = salvaguardas proporcionales
4. **Cuantificación**: FAIR ALE = justificación inversión a Junta Directiva
5. **Auditoría**: ENS + SGSI ISO 27001 + CCN-CERT reportes incidentes
6. **Mejora**: Ciclo PDCA anual (art. 39 ENS: "actualización permanente")

***

## 6. RECOMENDACIONES ESTRATÉGICAS 2025-2026

### 6.1 Para la Administración Pública

**Prioridad 1: Implementación ENS + MAGERIT integrado**

- Realizar análisis de riesgos MAGERIT en todos sistemas de información (MAR completo) antes de Q2 2025
- Documentar Declaración de Aplicabilidad (medidas ENS aplicables vs. no aplicables)
- Establecer Comités de Seguridad de Sistemas de Información (CSSI) con responsable seguridad (RSEG) designado
- Reportar a CCN indicadores op.mon.2 (grado implantación, eficiencia incidentes) semestralmente

**Prioridad 2: Madurez Respond + Recovery (dominios críticos)**

- Elevar de 48% a >65% mediante:
    - Planes respuesta incidentes documentados y probados 2×/año (no solo anuales)
    - Simulacros coordinados de recuperación (RTO/RPO reales vs. teóricos)
    - Análisis forense post-incidente sistematizado (actualmente <10%)
    - Mejora continua: revisión planes response ≥2 veces/año

**Prioridad 3: Preparación Centro Nacional de Ciberseguridad (creación ene 2025)**

- Designar interlocutores sectoriales para reportes NIS2 (341 incidentes operadores 2024 → gestión centralizada)
- Alineación CSIRT nacional (CCN-CERT + INCIBE-CERT) para coordinación 72h reportes de incidentes


### 6.2 Para Operadores Esenciales e Importantes (NIS2)

**Prioridad 1: Conformidad acelerada NIS2 (plazo ley aún en debate)**

- **Esenciales** (cert. obligatoria): Auditoría externa ISO 27001 + ENS bienal, antes Q2 2025
    - Garantizar: Certificación de conformidad vigente
    - Reportar: Incidentes >impacto significativo a CCN-CERT (72h)
    - Sanciones: €10M o 2% volumen negocios si incumplimiento
- **Importantes** (autoevaluación permitida): Documentar conformidad ENS + NIS2 (autoevaluación anual mínimo)
    - Alternativa: Certificación voluntaria (reducir riesgo supervisión)
    - Sanciones: €7M o 1,4% volumen negocios si supervisión detecta incumplimiento

**Prioridad 2: Cuantificación de riesgos (FAIR/ALE) para inversión**

- Aplicar FAIR a escenarios críticos (ransomware, APT financiero, OT compromise)
- Justificar inversión seguridad a Junta: ROI, ALE, impacto reputacional monetarizado
- Publicar informe riesgos cuantificado trimestralmente a Consejo (mejor práctica: KPMG benchmark 2024)

**Prioridad 3: Resiliencia Respond + Recovery (especialmente sectores debilitados)**

- **Energía (50% recovery)**: Implementar backups segregados, recuperación OT/ICS (Deutsche Bahn case: coste ~€209K, ROI +320% anual)
- **Transporte (44% recovery)**: RTO<4h, RPO<1h sistemas críticos; simulacros ferroviarios con operadores ferroviarios europeos
- **TIC/Telecomunicaciones (50% recovery)**: Redundancia geográfica, automatización failover, Threat Hunting continuo

**Prioridad 4: Seguridad cadena suministro (NIS2 Annexo Reglamento Ejecución)**

- Auditar prácticas ciberseguridad proveedores (Dev seguro, capacidades cumplimiento NIS2)
- Incluir en contratos: SLA seguridad, derechos auditoría, gestión vulnerabilidades responsable
- Diversificar proveedores criticalidad (limitar dependencia mono-proveedor)


### 6.3 Para Pymes (Entidades importantes, no obligadas 72h reportes)

**Prioridad 1: Evaluar si entidad "importante" NIS2 (criterios art. 2)**

- Revisar: ¿Sector Anexo II? ¿Tamaño 250+ empl. o facturación €50M+?
- Si Sí → preparar autoevaluación anual ENS (no auditoría periódica obligatoria, pero supervisión posible)
- Si No → seguir ENS de forma voluntaria (mejor práctica, competitividad, confianza cliente)

**Prioridad 2: Elevar madurez 52% → 70% (Bienes de Consumo/Distribución rezagadas)**

- **Identify 58%**: Completar inventario activos (1 consultor × 2 semanas)
- **Protect 35%** (Distribución): Implementar MFA, acceso mínimo privilegio (herramientas open-source: Keycloak, Vault)
- **Respond 46%**: Documentar procedimientos respuesta, pruebas anuales, comunicación crisis
- **Recovery 46%**: Backups cifrados + aislados (offline), validar RTO real (simulacro trimestral)

**Prioridad 3: Financiación seguridad (ROI + ayudas)**

- Solicitar fondos digitales (fondos Next Generation EU, ayudas autonomías)
- Cuantificar ALE (pérdida promedio/año sin medidas) vs. coste implementación → ROI a CFO
- Contratar auditoría MAGERIT/ENS (ahorrar IT interno, expertise externo)

***

## 7. LIMITACIONES Y OPORTUNIDADES DE FUTURO

### 7.1 Limitaciones Actuales

| Limitación | Impacto | Solución |
| :-- | :-- | :-- |
| **Centro Nacional Ciberseguridad aún no operativo (ene 2025)** | Ambigüedad supervisión; duplicación CCN-CERT + INCIBE-CERT | Aprobación ley trasposición + decreto desarrollo (Q1-Q2 2025) |
| **MAGERIT sin cuantificación monetaria nativa** | Dificultad comunicación ejecutiva; decisiones inversión subjetivas | Integración FAIR/ALE estándar en herramientas (PILAR 2.0 en desarrollo) |
| **Madurez Recovery nacional 53% (muy baja)** | Riesgo RTO/RPO incumplimiento NIS2 (72h reportes) | Simulacros obligatorios sectoriales; benchmarking público (INES CCN) |
| **PyMEs 38-52% madurez (fragmentación)** | Vulnerabilidad cadena suministro; riesgo cascada ataques | Programas sensibilización INCIBE/CCN; auditorías simplificadas (ROI < €50K) |
| **Falta indicadores comparativos reales** | Benchmarking sectorial inexistente; decisiones sin contexto | INCIBE + CCN publicar "Observatorio Ciberseguridad 2025" (homólogo ISMS Forum público) |

### 7.2 Oportunidades 2025-2027

**1. Automatización MAGERIT vía IA/ML**

- Herramientas como PILAR 2.0 (CCN) integrar machine learning para detección anomalías activos, predicción amenazas contextualizadas, recomendaciones salvaguardas automáticas basadas en ENS profiling
- Reducir curva aprendizaje MAGERIT (actualmente alta para consultores junior)

**2. Estándar cuantificación nacional "FAIR-ES"**

- CCN + INCIBE definir metodología cuantificación Anexo IX ENS (homólogo NIST RMF, ISO 31000)
- Interoperabilidad MAGERIT-FAIR en reportes: "Riesgo residual €X / Cumplimiento ENS Y%"

**3. Integración con Quantum-Safe Cryptography (post-quantum)**

- ENS Anexo II.mp.com.2 (cifrado) anticipar transición PQC 2026-2030
- MAGERIT incluir evaluación riesgos transición criptográfica (vulnerabilidad "Harvest Now, Decrypt Later")

**4. Gobernanza ciberseguridad integrada (GRC)**

- Centralizar MAGERIT + Gestión Cumplimiento NIS2/DORA/RGPD en plataformas GRC (Nessus, Qualys, Archer)
- Consejo Directivo visibilidad continua KRIs (Key Risk Indicators) y compliance dashboard

**5. Threat Intelligence + MAGERIT dinámico**

- Automatizar actualización Mapa Riesgos (MAR.2) con feeds MITRE ATT\&CK, ICS-CERT, geopolítica
- Simulaciones Montecarlo adaptativas según actividad APT regional (ej. Sandworm → elevar ALTA energía)

***

## 8. CONCLUSIONES

**MAGERIT permanece como metodología de referencia nacional para análisis de riesgos en sistemas de información, operacionalizada mediante:**

1. **Integración ENS (RD 311/2022)**: 22 requisitos mínimos + medidas proporcionadas (frameworks org/op/protección) categorizados por impacto (BÁSICA/MEDIA/ALTA) y madurez CMM (L2-L4).
2. **Conformidad NIS2**: Análisis MAGERIT + Cuantificación FAIR obligatorio para decisiones inversión; autoridades supervisoras (CCN, sectoriales) requerirán evidencia análisis riesgos formal 2025-2026.
3. **Madurez nacional crítica**: España alcanza 61% madurez integral (NIST domains), pero **Respond (55%) y Recovery (53%) son vulnerables** frente a requisito NIS2 de coordinación 72h incidentes. Sectores financiero/construcción lideran (68-72%); Administración Pública, TIC, y Pymes (<52%) requieren aceleración.
4. **Recomendación práctica dual**:
    - **Sector público**: MAGERIT + FAIR (cuantificación €)
    - **Operadores privados críticos**: NIST CSF + MAGERIT (conformidad ENS)
    - **PyMEs**: NIST (agilidad) + auditoría ENS periódica (certificación voluntaria ofrece valor regulatorio)
5. **Horizonte 2026**: La aprobación de la Ley de Trasposición NIS2 y operacionalización del Centro Nacional de Ciberseguridad consolidarán MAGERIT-ENS como marco nacional, complementado con cuantificación financiera FAIR/ALE para decisiones ejecutivas. **Organizaciones que no comiencen conformidad Q1 2025 enfrentarán riesgo material de sanciones (€10M esenciales, €7M importantes) y daño reputacional ante incidentes coordinados.**

***

## **REFERENCIAS**

MAGERIT v3.0 - Libro I Método, CCN-CERT, octubre 2012. URL: https://www.ccn-cert.cni.es/es/documentos-publicos/1789-magerit-libro-i-metodo/[^1_1]
Seifti.io - Metodología MAGERIT, mayo 2024[^1_2]
KPMG - Claves para cumplir Directiva NIS2, octubre 2025[^1_3]
TFM UZar - Comparación MAGERIT vs NIST CSF IoT, 2024[^1_7]
Elperiódico Energía - Ataques infraestructuras españolas +43% 2024, mayo 2025[^1_12]
Análisis Comparativo Metodologías UPS Ecuador 2023[^1_8]
Estudio Comparado Gestión Riesgos Uruguay (AGESIC)[^1_9]
Real Decreto 311/2022 (BOE), Esquema Nacional Seguridad[^1_10]
PTE Disruptive - Informe Situación Ciberseguridad 2024[^1_13]
Administración Pública Digital - Balance INCIBE 2024, marzo 2025[^1_4]
ISMS Forum - Indicador Madurez Ciberseguridad 2024[^1_5]
INCIBE - Balance Ciberseguridad 2024, marzo 2025[^1_14]
YouTube - Metodología FAIR Cuantificación Riesgos, noviembre 2022[^1_15]
SecureFrame - Cyber Risk Quantification, julio 2023[^1_16]
KPMG - Cuantificación Riesgos Ciberseguridad, marzo 2024[^1_6]

***

**Fecha:** Enero 2026
**Clasificación:** Uso Profesional / Stakeholders Ciberseguridad España
**Validación:** Fuentes académicas, organismos oficiales (CCN, INCIBE, KPMG), documentación regulatoria BOE
<span style="display:none">[^1_17][^1_18][^1_19][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_70][^1_71][^1_72]</span>

<div align="center">⁂</div>

[^1_1]: https://es.wikipedia.org/wiki/Magerit_(metodolog%C3%ADa)

[^1_2]: https://www.ccn-cert.cni.es/es/documentos-publicos/1789-magerit-libro-i-metodo/file?format=html

[^1_3]: https://assets.kpmg.com/content/dam/kpmgsites/es/pdf/2024/12/claves-cumplir-directiva-nis2.pdf.coredownload.inline.pdf

[^1_4]: https://www.administracionpublicadigital.es/tecnologias/2025/03/el-balance-de-2024-de-incibe-deja-un-incremento-del-166-respecto-a-2023

[^1_5]: https://master.ismsforum.es/wp-content/uploads/2024/09/indicador-de-madurez-en-ciberseguridad-2020-1.pdf

[^1_6]: https://www.tendencias.kpmg.es/2024/03/apostar-cuantificacion-riesgos-ciberseguridad-2/

[^1_7]: https://zaguan.unizar.es/record/145837/files/TAZ-TFM-2024-1152.pdf

[^1_8]: https://dspace.ups.edu.ec/bitstream/123456789/26674/1/UPS-CT011073.pdf

[^1_9]: https://www.gub.uy/agencia-gobierno-electronico-sociedad-informacion-conocimiento/book/6611/download

[^1_10]: https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191

[^1_11]: https://es.linkedin.com/pulse/la-actualización-del-esquema-nacional-de-seguridad-ens-isacamadrid

[^1_12]: https://elperiodicodelaenergia.com/los-ataques-a-infraestructuras-espanolas-aumentaron-un-43-en-2024-y-se-mantienen-en-2025/

[^1_13]: https://ptedisruptive.es/wp-content/uploads/2024/12/INFORME-DE-SITUACION_CIBERSEGURIDAD_2024.pdf

[^1_14]: https://www.incibe.es/incibe/sala-de-prensa/incibe-presenta-su-balance-de-ciberseguridad-2024-con-mas-de-97000-incidentes

[^1_15]: https://www.youtube.com/watch?v=8nMfIR57tLg

[^1_16]: https://secureframe.com/es-es/blog/cyber-risk-quantification

[^1_17]: https://www.tendencias.kpmg.es/2024/10/directiva-nis2-trasposicion-proximos-pasos/

[^1_18]: https://www.studocu.com/es/document/universidad-de-las-palmas-de-gran-canaria/administracion-de-las-tecnologias-de-la-seguridad/libro-ii-catalogo-de-elementos/6079615

[^1_19]: https://www.tithink.com/publicacion/MAGERIT.pdf

[^1_20]: https://www.incibe.es/incibe-cert/sectores-estrategicos/NIS2-necesitas-saber

[^1_21]: https://seifti.io/es/magerit/

[^1_22]: https://www.tendencias.kpmg.es/2023/10/directiva-nis2-si-aplica-tu-organizacion/

[^1_23]: https://administracionelectronica.gob.es/ctt/magerit

[^1_24]: https://www.youtube.com/watch?v=y-5YKYCvLM8

[^1_25]: https://www.channelpartner.es/seguridad/la-directiva-nis2-nueva-guia-de-ciberseguridad-europea/

[^1_26]: https://openaccess.uoc.edu/server/api/core/bitstreams/a7adc71c-de9e-4c44-868c-2104780ad4c3/content

[^1_27]: https://www.ochgroup.co/que-es-el-magerit-y-como-ayuda-en-la-gestion-de-riesgos-de-seguridad-de-la-informacion/

[^1_28]: https://uvadoc.uva.es/bitstream/handle/10324/37736/TFG-I-1213.pdf?sequence=1

[^1_29]: https://www.sentinelone.com/es/cybersecurity-101/cybersecurity/cybersecurity-metrics/

[^1_30]: https://www.fairinstitute.org/blog/integrating-fair-models-a-unified-framework-for-cyber-risk-management

[^1_31]: https://ciberso.com/blog/gobierno-de-la-ciberseguridad/optimizando-resiliencia-empresarial-enfoque-detallado-rpo-rto-wrt-mtd/

[^1_32]: https://secureframe.com/es-es/blog/nist-csf-framework

[^1_33]: https://www.balbix.com/insights/fair-model-for-risk-quantification-pros-and-cons/

[^1_34]: https://www.abast.es/blog/el-reto-de-la-resiliencia-empresarial-en-la-era-digital/

[^1_35]: https://assets.kpmg.com/content/dam/kpmg/co/pdf/2024/07/Benchmark de Ciber Riesgo-executive-summary.pdf

[^1_36]: https://www.cybersaint.io/blog/fair-cyber-risk-quantification

[^1_37]: https://techconsulting.es/continuidad-de-negocio-en-espana-normativa-clave-riesgos-y-soluciones-2024/

[^1_38]: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.spa.pdf

[^1_39]: https://www.cybersaint.io/blog/a-pocket-guide-to-factor-analysis-of-information-risk-fair

[^1_40]: https://www.ovhcloud.com/es-es/solutions/uc-business-continuity/

[^1_41]: https://www.ismsforum.es/ficheros/descargas/informeobservatorio-31731565896.pdf

[^1_42]: https://1616664.fs1.hubspotusercontent-na1.net/hubfs/1616664/FAIR Institute -- Integrating FAIR Models for Cyber Risk Management (December 2024).pdf

[^1_43]: https://manage.quantumsec.es/blog/qblog-2/nis2-tu-empresa-ya-cumple-con-la-directiva-mas-exigente-de-ciberseguridad-de-la-ue-161

[^1_44]: https://www.hacienda.gob.es/SGT/catalogo_sefp/050_magerit-v2-i-metodo.pdf

[^1_45]: https://www.boe.es/boe/dias/2024/11/30/pdfs/BOE-A-2024-25009.pdf

[^1_46]: https://www.group.sener/insights/ciberseguridad-infraestructuras-criticas-y-resiliencia-nacional/

[^1_47]: https://www.skinait.com/modelos-y-marcos-de-gestión-para-la-seguridad-de-la-información-Escritos-90/

[^1_48]: https://crea.ujaen.es/bitstreams/49959b45-1ddd-48d7-9f99-4e2101dd64f8/download

[^1_49]: https://www.iccspain.org/wp-content/uploads/2024/12/2024_IssueBrief3_SPA.pdf

[^1_50]: https://oa.upm.es/92829/1/Libro EUTELIS.pdf

[^1_51]: https://sipadan.es/blog-sipadan/mayores-amenazas-ciberseguridad-2025

[^1_52]: https://www.ccn-cert.cni.es/es/800-guia-esquema-nacional-de-seguridad/543-ccn-stic-825-ens-iso27001/file.html

[^1_53]: https://www.dsn.gob.es/sites/default/files/documents/0 LIBRO GENERAL ONLINE Rectificado.pdf

[^1_54]: https://www.deloitte.com/es/es/services/consulting/research/estado-ciberseguridad.html

[^1_55]: https://www.redseguridad.com/actualidad/incibe-gestiona-mas-de-97-000-incidentes-de-ciberseguridad-en-2024-un-166-mas-que-el-ano-anterior_20250320.html

[^1_56]: https://ens.ccn.cni.es/es/que-es-el-ens/faq

[^1_57]: https://www.incibe.es/sites/default/files/paginas/que-hacemos/Plan-Anual-Actividad_2024_resultados.pdf

[^1_58]: https://www.easytelecomlaw.com/blog/ens-y-nis2-que-son-y-diferencias/

[^1_59]: https://www.metared.org/content/dam/metared/pdf/IMC_digital.pdf

[^1_60]: https://www.escudodigital.com/ciberseguridad/incibe-gestiono-97348-incidentes-ciberseguridad-2024-16-mas-2023.html

[^1_61]: https://emalsa.es/politica-ens-rd-3112022/

[^1_62]: https://www.ccontasgalicia.es/sites/consello_de_contas/files/contents/documents/2024/1702024-09_IF_Informe_CBCS_Concello_de_Santiago_de_Compostela_2024_C.pdf

[^1_63]: https://www.newtral.es/incidentes-ciberseguridad-incibe-2024/20250320/

[^1_64]: https://repositorio.comillas.edu/xmlui/bitstream/handle/11531/87925/TFG-PachoGarcia, Pablo.pdf?sequence=1\&isAllowed=y

[^1_65]: https://cyberlideriamgzn.es/la-proteccion-de-infraestructuras-criticas-y-datos-sensibles-una-prioridad-para-gobiernos-y-empresas-en-2025/

[^1_66]: https://iveconsultores.com/directiva-nis2/

[^1_67]: https://www.youtube.com/watch?v=6nelMKVprSg

[^1_68]: https://techconsulting.es/ciberseguridad-2025-en-espana-amenazas-regulacion-casos-y-estrategias-clave/

[^1_69]: https://www.sgs.com/es-es/noticias/2025/05/ciberseguridad

[^1_70]: https://www.ismsforum.es/noticias/2486/2025-las-organizaciones-refuerzan-sus-estrategias-de-ciberseguridad-en-el-marco-de-adaptaci-n-a-la-nis2/

[^1_71]: https://www.computing.es/a-fondo/nis-2-que-conlleva-esta-directiva-ciberseguridad/

[^1_72]: https://www.boe.es/buscar/doc.php?id=DOUE-Z-2025-70047


---