# PLANTILLA EXCEL: ANÁLISIS DE RESULTADOS ENCUESTA + CÁLCULO CMI
## Herramienta de Medición y Análisis Financiero de Encuesta DORA

**Versión:** 1.0  
**Fecha:** Enero 2026  
**Clasificación:** Profesional — Template Análisis Cuantitativo  
**Formato:** Plantilla Excel con Fórmulas (descrita en Markdown)

---

## INTRODUCCIÓN

Esta plantilla Excel proporciona:

1. **Tabulación automática** de respuestas encuesta (128 preguntas)
2. **Cálculo de CMI (Cybersecurity Maturity Index)** por módulo y consolidado
3. **Análisis de gaps** vs estándares DORA
4. **Cálculo de ROI/ROSI** de iniciativas remediación
5. **Integración con mapeo normativo** (Artículos DORA)
6. **Reportes ejecutivos** listos para Junta

---

## ESTRUCTURA: 8 HOJAS EXCEL

### **HOJA 1: "Respuestas Encuesta"**

**Propósito:** Entrada de datos respuestas 128 preguntas

```
Estructura:
┌─────────┬──────────┬──────────┬──────────┬──────────┐
│ Pregunta│ Módulo   │ Texto    │ Respuesta│ Art.DORA │
├─────────┼──────────┼──────────┼──────────┼──────────┤
│ 1       │ Governance│ ¿Existe...?│ 4/5    │ Art. 5   │
│ 2       │ Governance│ ¿CISO...?  │ 5/5    │ Art. 5   │
│ 3       │ Governance│ ¿Presupuesto?│ 3/5 │ Art. 5   │
│ ...     │ ...       │ ...       │ ...    │ ...      │
│ 128     │ Resilience│ ¿TLPT...? │ 2/5    │ Art. 26  │
└─────────┴──────────┴──────────┴──────────┴──────────┘

Escala Respuesta:
  1 = Ad-hoc (no existe o es muy básico)
  2 = Developing (implementación incompleta)
  3 = Managed (conforme DORA con gaps menores)
  4 = Integrated (fully aligned DORA)
  5 = Optimized (best-in-class + continuous improvement)
```

**Columnas:**
- A: Número pregunta (1-128)
- B: Módulo (Gobernanza, Riesgos, Incidentes, etc.)
- C: Texto pregunta completo
- D: **Score respuesta (1-5)** [USER INPUT]
- E: Artículo DORA mappeado
- F: Observaciones (opcional)

**Fórmulas:**
```excel
=VLOOKUP(A2, MapeoPreguntasModulos!$A$2:$B$129, 2, FALSE)
  → Busca módulo correspondiente a pregunta
```

---

### **HOJA 2: "Cálculo CMI por Módulo"**

**Propósito:** Agregación de scores por módulo

```
Módulo                      Preguntas    Score Promedio    Score /5.0
──────────────────────────────────────────────────────────────────────
1. Gobernanza               1-16         AVERAGE(D2:D17)   =E2/5*100%
2. Riesgos TIC              17-34        AVERAGE(D18:D35)  =E3/5*100%
3. Incidentes               35-54        AVERAGE(D36:D55)  =E4/5*100%
4. Vulnerabilidades         55-70        AVERAGE(D56:D71)  =E5/5*100%
5. SIEM                     71-90        AVERAGE(D72:D91)  =E6/5*100%
6. Información/Acceso       91-108       AVERAGE(D92:D109) =E7/5*100%
7. Capacitación             109-120      AVERAGE(D110:D121)=E8/5*100%
8. Resiliencia              121-128      AVERAGE(D122:D129)=E9/5*100%
──────────────────────────────────────────────────────────────────────
CMI PROMEDIO PONDERADO:     —            =SUMATORIA(pondera)=CMI/5.0
```

**Ponderación DORA:**
```
Gobernanza:       25% (criticidad governance)
Riesgos:          20% (fundamental risk mgmt)
Incidentes:       20% (response criticality)
Vulnerabilidades: 10% (technical controls)
SIEM:             10% (detection/monitoring)
Seguridad Info:   10% (data protection)
Capacitación:     3%  (awareness secondary)
Resiliencia:      2%  (testing secondary)
```

**Fórmula CMI Ponderado:**
```excel
=(Gobernanza*0.25 + Riesgos*0.20 + Incidentes*0.20 + 
  Vulnerabilidades*0.10 + SIEM*0.10 + SegInfo*0.10 + 
  Capacitacion*0.03 + Resiliencia*0.02)
```

---

### **HOJA 3: "Dashboard CMI"**

**Propósito:** Visualización ejecutiva

```
┌────────────────────────────────────────────────────────────┐
│ ENCUESTA DORA - CYBERSECURITY MATURITY INDEX 2026          │
├────────────────────────────────────────────────────────────┤
│                                                              │
│ Institución: [________]     Período: Q1 2026               │
│ Respondentes: [________]    Fecha: Enero 20, 2026          │
│                                                              │
├────────────────────────────────────────────────────────────┤
│ CMI CONSOLIDADO: 2.8/5.0 (MANAGED - Developing)            │
│                                                              │
│ ▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░ 56%                            │
│                                                              │
│ Tendencia Q4 2025 → Q1 2026:  +0.2 (▲)                     │
│ Target Q3 2026:               3.5/5.0                      │
│                                                              │
├────────────────────────────────────────────────────────────┤
│ CMI POR MÓDULO (Radar Chart):                              │
│                                                              │
│              Gobernanza 3.1                                │
│              /              \                              │
│            /                  \                            │
│    Riesgos 2.6              Incidentes 3.0               │
│        |                        |                         │
│        |                        |                         │
│  Vulnerab 2.4            SIEM 2.7                         │
│        \                        /                         │
│          \                    /                           │
│        SegInfo 2.5 - Capacit 2.3                          │
│                                                              │
│              Resiliencia 2.1                               │
│                                                              │
├────────────────────────────────────────────────────────────┤
│ STATUS POR MÓDULO:                                          │
│                                                              │
│ Gobernanza (3.1):     ▓▓▓░░  Acceptable                    │
│ Riesgos (2.6):        ▓▓░░░  Needs work                    │
│ Incidentes (3.0):     ▓▓▓░░  Acceptable                    │
│ Vulnerab (2.4):       ▓▓░░░  Needs work                    │
│ SIEM (2.7):           ▓▓░░░  Acceptable                    │
│ SegInfo (2.5):        ▓▓░░░  Needs work ⚠                │
│ Capacitac (2.3):      ▓▓░░░  Needs work ⚠                │
│ Resiliencia (2.1):    ▓░░░░  Critical ⚠⚠                  │
│                                                              │
└────────────────────────────────────────────────────────────┘
```

**Elementos:**
- Gauge CMI consolidado (gráfico tipo velocímetro)
- Radar chart (8 módulos)
- Bar charts (status por módulo)
- Traffic light (R/Y/G) por módulo
- Trending línea (CMI histórico)

---

### **HOJA 4: "Análisis de Gaps"**

**Propósito:** Identificación detallada de deficiencias

```
Pregunta  Módulo    Respuesta  Gap  Artículo  Remediación      Prioridad
─────────────────────────────────────────────────────────────────────────
3         Gobierno  3/5        2    Art. 5    Presupuesto      ALTA
          (Score < 4)                         formal Junta
                                              por €500K 2026
                                              
24        Riesgos   2/5        3    Art. 6    Implementar       ALTA
          (Score < 3)                         FAIR methodology
                                              Q2 2026
                                              
52        Incidentes 2/5       3    Art. 18   Validación        MEDIA
          (Score < 3)                         crisis comm plan
                                              external audit
                                              
68        Vulnerab  2/5        3    Art. 24   Amenaza modelo    MEDIA
          (Score < 3)                         STRIDE/PASTA
                                              documentar Q2
                                              
...
```

**Fórmulas:**
```excel
=IF(D2<3, 5-D2, IF(D2<4, 4-D2, 0))
  → Calcula gap (0-5 escala)

=IF(GAP>=3, "ALTA", IF(GAP>=2, "MEDIA", "BAJA"))
  → Prioriza gaps por severidad
```

**Campos:**
- Pregunta número
- Módulo correspondiente
- Respuesta actual (1-5)
- Gap (5 - respuesta)
- Artículo DORA relevante
- Acción remediación
- Prioridad (ALTA/MEDIA/BAJA)
- Propietario asignado
- Fecha target

---

### **HOJA 5: "Roadmap Remediación"**

**Propósito:** Plan de acción con timelines

```
Fase  Acción               Fecha      Responsable  Costo    Impacto
─────────────────────────────────────────────────────────────────────
1     Formalizar          Feb 28,     CISO         €0K      CMI +0.3
      presupuesto         2026        CFO
      ciberseguridad
      
1     Implementar FAIR    Mar 31,     CISO/CRO     €40K     CMI +0.2
      methodology         2026        Riesgos
      
1     Validación externa  Mar 31,     CISO/Audit   €30K     CMI +0.2
      crisis comm plan    2026
      
2     SIEM deployment     Apr 30,     CTO/CISO     €150K    CMI +0.3
      with tuning         2026
      
2     TLPT execution      Jun 30,     CISO/RedTeam €200K    CMI +0.3
                          2026
      
3     Resiliencia         Jul 31,     CTO/BCP      €80K     CMI +0.2
      testing (site       2026
      activation)
      
─────────────────────────────────────────────────────────────────────
PRESUPUESTO TOTAL:                                €500K

IMPACTO ESPERADO:                           CMI 2.8 → 3.8 (+1.0)
TIMELINE:                                   Feb 2026 - Aug 2026

ROI ESTIMADO:                               200%+ (breach prevention)
```

---

### **HOJA 6: "Estimación ALE"**

**Propósito:** Análisis de impacto financiero

```
Tipo Incidente    SLE (€)    ARO (%)    ALE (€)    CMI Impact
─────────────────────────────────────────────────────────────────
Ransomware        5,650K     15%        847K       CMI <2
Data Breach       3,200K     8%         256K       CMI <2
Phishing          800K       25%        200K       CMI <3
DDoS              1,500K     5%         75K        CMI 2-3
Insider Threat    2,100K     3%         63K        CMI <2
Availability      400K       20%        80K        CMI <3
────────────────────────────────────────────────────────────────────
ALE TOTAL ANUAL:                        1,521K

Mit Risk Post-CMI 3.5:
  Ransomware: 15% → 5% (67% reduction)   = 282K (vs 847K)
  Data Breach: 8% → 2% (75% reduction)   = 64K (vs 256K)
  Phishing: 25% → 10% (60% reduction)    = 80K (vs 200K)
  DDoS: 5% → 1% (80% reduction)          = 15K (vs 75K)
  Insider: 3% → 1% (67% reduction)       = 21K (vs 63K)
  Availability: 20% → 5% (75% reduction) = 20K (vs 80K)
──────────────────────────────────────────────────────────
ALE POST-REMEDIATION:                     482K

ANNUAL BENEFIT: 1,521K - 482K = €1,039K annual avoidance
```

**Fórmulas:**
```excel
=SLE * ARO
  → Calcula ALE por tipo

=SUM(ALE_column)
  → Total ALE anual

=(ALE_before - ALE_after) / ALE_before * 100%
  → % Reduction
```

---

### **HOJA 7: "ROI / ROSI Cálculo"**

**Propósito:** Justificación financiera de inversión

```
Iniciativa              Inversión   Beneficio Anual  ROSI%    Payback
──────────────────────────────────────────────────────────────────────
SIEM Implementation     €150K       €450K (ALE red)  200%     4 meses

FAIR Methodology        €40K        €200K (risk      400%     2.4 meses
Implementation                      mitigation)

Vulnerability           €60K        €300K (breach    400%     2.4 meses
Scanning                            prevention)

Crisis Comm Validation  €30K        €150K (conf loss €150K    2.4 meses
                                    avoided)

TLPT Execution          €200K       €600K (critical  200%     4 meses
                                    breach prevent)

Encryption Program      €120K       €400K (data      233%     3.6 meses
                                    protection)

BC/DR Testing           €80K        €250K (recovery  212%     3.8 meses
                                    speed)

Phishing Program        €50K        €150K (incident  200%     4 meses
                                    prevention)
───────────────────────────────────────────────────────────────────────
TOTAL INVESTMENT        €730K       €2,500K annual   242%     avg 3.5m

Portfolio ROI (2 años): (2.5M*2 - €730K) / €730K = 585% EXCEPCIONAL
```

**Fórmula ROSI:**
```excel
ROSI% = (ALE_Reduction - Annual_Cost) / Annual_Cost * 100%

Ejemplo SIEM:
  = (€450K - €75K/año) / €75K * 100%
  = €375K / €75K * 100%
  = 500% ROSI (excelente)
```

---

### **HOJA 8: "Reporte Ejecutivo"**

**Propósito:** Summary para Junta (1 page)

```
╔══════════════════════════════════════════════════════════════════════╗
║           ENCUESTA DORA - REPORTE EJECUTIVO Q1 2026                 ║
║                                                                      ║
║  Institución: [Banco Ejemplo]                     Fecha: Ene 20    ║
║  Respondentes: 12 (CISO, CRO, Compliance, etc.)                    ║
╚══════════════════════════════════════════════════════════════════════╝

HALLAZGOS CLAVE:

  ✓ CMI Actual: 2.8/5.0 (MANAGED - Developing)
  ✓ Tendencia: +0.2 desde Q4 2025 (positivo)
  ✓ Cobertura: 128 preguntas × 100% DORA articles
  ✓ ALE Anual: €1,521K (actual) vs €482K (post-remediation)

PRIORIDADES INMEDIATAS (Fase 1):

  1. Implementar SIEM (€150K) → MTTD <15min, CMI +0.3
  2. FAIR Quantification (€40K) → Risk measurement, CMI +0.2
  3. Validar Crisis Comm (€30K) → External audit, CMI +0.2
  4. TLPT Execution (€200K, Q2) → Resilience testing, CMI +0.3

INVERSIÓN Y RETORNO:

  Total Presupuesto Fase 1-3:  €730K
  ALE Reduction Anual:         €1,039K
  ROSI Portfolio:              242%
  Payback Period:              3.5 meses promedio
  
  ✓ RECOMENDACIÓN: APROBAR presupuesto Fase 1 (€420K, Q1-Q2)

TIMELINE:

  Feb 28:  FAIR training + Governance policy
  Mar 31:  Crisis comm validation
  May 31:  SIEM deployment (MTTD <15min)
  Jun 30:  TLPT execution + Vendor assessments
  Aug 31:  Resiliencia testing; CMI target 3.5

RIESGO:

  Bajo (si roadmap se cumple) → Auditoría supervisora Q3 2026: PROBABLE APROBACIÓN

DECISIONES REQUERIDAS:

  [ ] Aprobar Fase 1 presupuesto €420K
  [ ] Asignar CISO + PMO responsables
  [ ] Establecer CMI 3.5 como objetivo Q3
  [ ] Reportes trimestrales a Junta

```

---

## CÓMO USAR LA PLANTILLA

### **Paso 1: Tabulación (60 min)**
1. Abrir Hoja "Respuestas Encuesta"
2. Rellenar D2:D129 con scores (1-5) de cada pregunta
3. Sistema auto-calcula módulos

### **Paso 2: Análisis (120 min)**
1. Revisar Hoja "Dashboard CMI" → visualización actual
2. Revisar Hoja "Análisis de Gaps" → qué falta
3. Priorizar gaps por DORA Article criticidad

### **Paso 3: Planificación (90 min)**
1. Rellenar Hoja "Roadmap Remediación" → acciones y timelines
2. Estimar costos (usar benchmarks industria)
3. Asignar propietarios (CISO, CRO, CTO, etc.)

### **Paso 4: Financiero (60 min)**
1. Rellenar Hoja "Estimación ALE" → SLE y ARO por tipo incidente
2. Sistema calcula beneficio anual
3. Rellenar Hoja "ROI/ROSI" → inversión vs beneficio

### **Paso 5: Reporting (30 min)**
1. Exportar Hoja "Reporte Ejecutivo" a PowerPoint
2. Exportar gráficos de "Dashboard CMI"
3. Presentar a Junta con datos

---

## FÓRMULAS CLAVE

### CMI Ponderado:
```excel
=(AVERAGE(D2:D17)*0.25 + AVERAGE(D18:D35)*0.20 + 
  AVERAGE(D36:D55)*0.20 + AVERAGE(D56:D71)*0.10 + 
  AVERAGE(D72:D91)*0.10 + AVERAGE(D92:D109)*0.10 + 
  AVERAGE(D110:D121)*0.03 + AVERAGE(D122:D129)*0.02)
```

### ALE Cálculo:
```excel
=C3*D3  ← SLE (C) × ARO (D) = ALE
```

### ROSI:
```excel
=(F3-E3)/E3*100%  ← (Benefit-Cost)/Cost*100
```

### Payback (meses):
```excel
=(E3 / (F3/12))  ← Cost / (AnnualBenefit/12)
```

---

**Fin de la Plantilla Excel**

*Enero 2026 — Herramienta de Análisis Encuesta DORA*

