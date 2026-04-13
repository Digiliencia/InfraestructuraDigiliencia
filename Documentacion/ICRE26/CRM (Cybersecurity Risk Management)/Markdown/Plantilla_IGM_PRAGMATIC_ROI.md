# **PLANTILLA IGM + PRAGMATIC + ROI CALCULATOR**
## *Excel para Cálculo Automatizado de Indicadores CRM*

**Versión:** 2.0 | **Fecha:** Enero 2026 | **Descripción:** Lógica + fórmulas para implementar en Excel

---

## **TABS INCLUIDAS (6 total)**

### **TAB 1: INPUT INDICATORS**

Entrada de datos para 25 indicadores principales:

```
GOBERNANZA (5 indicadores)
  ├─ RAS Documentado (Yes/No)
  ├─ CISO reporta CEO (Yes/No)
  ├─ Risk Tolerance Defined (Yes/No)
  ├─ Junta Oversight Frequency (Anual/Trimestral/Mensual/Continua)
  └─ IGM Target (0-4.0)

CUANTIFICACIÓN (3 indicadores)
  ├─ ALE Top 5 Risks (€ amount)
  ├─ ROI Analysis % (0-1000%)
  └─ FAIR Adoption (Yes/Partial/No)

THREAT MODELING (3 indicadores)
  ├─ PASTA Coverage % (0-100%)
  ├─ Attack Trees Completed (0-100%)
  └─ Threat-Vuln Mapping (Yes/No)

SOC/SIEM (4 indicadores)
  ├─ MTTD Actual (minutes)
  ├─ MTTD Target (minutes)
  ├─ MTTR Actual (hours)
  └─ MTTR Target (hours)

VULNERABILITIES (4 indicadores)
  ├─ Scanning Frequency (days)
  ├─ Patch % <7d Críticos (0-100%)
  ├─ CVSS Version (3.1/4.0)
  └─ Patch SLA Compliance % (0-100%)

SUPPLY CHAIN (3 indicadores)
  ├─ Vendor Audit % (0-100%)
  ├─ Contracts Security Clauses (Yes/No)
  └─ SBOM Maintained (Yes/No/Partial)

AWARENESS (3 indicadores)
  ├─ Phishing Click Rate % (0-100%)
  ├─ Phishing Report Rate % (0-100%)
  └─ Training Completion % (0-100%)

COMPLIANCE (3 indicadores)
  ├─ GDPR Compliance % (0-100%)
  ├─ DORA Compliance % (0-100%)
  └─ NIS2 Readiness % (0-100%)

AUTOMATION (2 indicadores)
  ├─ Policy-as-Code % (0-100%)
  └─ Infrastructure-as-Code % (0-100%)
```

**Validación Input:**
- Numéricos: 0-5 o 0-100% según tipo
- Texto: Yes/No/Partial
- Timestamps: automatic system date

---

### **TAB 2: PRAGMATIC SCORING**

Calificación automática 9 criterios × 25 indicadores:

```
FÓRMULA POR CRITERIO:

P (Predictivo) = IF(indicator_correlates_breach, 4, 2)
R (Relevante) = IF(stakeholder_importance="HIGH", 5, 3)
A (Accionable) = IF(decision_trigger_defined, 4, 2)
G (Genuino) = IF(metric_gaming_resistant, 5, 2)
M (Significativo) = IF(material_impact, 5, 2)
A (Preciso) = IF(operationally_defined, 5, 2)
T (Oportuno) = IF(frequency_sufficient, 5, 2)
I (Independiente) = IF(standalone_metric, 5, 2)
C (Rentable) = IF(cost_justified, 5, 1)

PRAGMATIC_SCORE_PER_METRIC = AVERAGE(P:C)
```

**Output:** Matrix 25 filas × 10 columnas (9 criterios + score)

---

### **TAB 3: GQM MAPPING**

Trazabilidad Indicador → Goal → Question → Metric:

```
ESTRUCTURA:

Indicador | Goal | Question | Métrica | Responsable | Frecuencia | Target | Actual | GAP | Status

Ejemplo:
MTTD | G4 (Detectar rápido) | ¿MTTD <30 min? | 48h actual | SOC Mgr | Daily | 30 min | 48 min | +18 | RED
```

---

### **TAB 4: COMPLIANCE SCORECARD**

Scoring cumplimiento regulatorio:

```
REGULACIÓN | INDICADORES CLAVE | CUMPLIMIENTO % | SANCIONES POTENCIAL | STATUS | TIMELINE

GDPR:
  ├─ Indicadores: RAS, MTTD, Patch %, Training, Audit trail
  ├─ Score: 85% (4/5 cumplidos)
  ├─ Sanción: €1-5M (estimate)
  ├─ Status: YELLOW (gaps minor)
  └─ Timeline: Q2 2026 → 95%

DORA (Financial only):
  ├─ Indicadores: RAS, ALE, MTTR, Vendor audit
  ├─ Score: 70% (3/5 cumplidos)
  ├─ Sanción: €5-10M (si aplicable)
  ├─ Status: RED (gaps críticos RTO/RPO)
  └─ Timeline: Q1 2026 → 100% obligatorio

NIS2 (Pre-Transposición):
  ├─ Indicadores: IGM, CISO, RAS, Incident 24h, Supply chain
  ├─ Score: 60% (2.5/5 cumplidos)
  ├─ Sanción: €10M (essential) / €7M (important)
  ├─ Status: ORANGE (transposición pending)
  └─ Timeline: Quarterly updates hasta Q1 2026
```

**Fórmula:**
```
COMPLIANCE_SCORE = (Indicadores cumplidos / Total) × 100

IF compliance >90% THEN "GREEN" (low risk)
ELSE IF compliance >70% THEN "YELLOW" (moderate)
ELSE IF compliance >50% THEN "ORANGE" (high)
ELSE "RED" (critical)
```

---

### **TAB 5: ROI CALCULATOR**

Análisis inversión → ahorro → payback:

```
CONTROL INVESTMENT ANALYSIS:

Control | Current ALE | Risk Reduction % | New ALE | Savings | Investment | ROI % | Payback (m)

SIEM:        €1.5M        60%              €0.6M    €0.9M    €300K        300%   4.0
EDR:         €5.0M        40%              €3.0M    €2.0M    €200K        900%   1.2
FAIR:        Varies       15%              Varies   €0.75M   €50K         1400%  0.4
Phishing:    €0.8M        50%              €0.4M    €0.4M    €30K         1233%  0.9
Supply Chain €2.0M        30%              €1.4M    €0.6M    €100K        500%   2.0

TOTALES:     €9.3M        ~40%             €5.4M    €3.9M    €680K        574%   1.4

NPV 5 AÑOS (8% discount) = €15.2M
```

**Fórmulas:**
```
Savings = Current_ALE × Risk_Reduction_%
New_ALE = Current_ALE × (1 - Risk_Reduction_%)
ROI_Percent = ((Savings - Cost) / Cost) × 100
Payback_Months = Cost / (Savings / 12)
NPV = SUM(Annual_Benefit × (1 + Discount)^(-Year)) - Initial_Cost
```

---

### **TAB 6: DASHBOARD EXECUTIVE**

Resumen visual para junta:

```
┌─────────────────────────────────────────────────────┐
│ CYBERSECURITY MATURITY DASHBOARD                    │
├─────────────────────────────────────────────────────┤
│                                                     │
│ IGM OVERALL SCORE: 2.38 → TARGET 3.5              │
│ ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░           │
│ Level: 2 — FORMATIVO                               │
│ Gap: -1.12 puntos (18 meses to close)             │
│                                                     │
├─ COMPLIANCE STATUS ─────────────────────────────┤
│ GDPR:  ██████████░░░░░░░░░░░░░░ 85%  🟡 YELLOW  │
│ DORA:  ███████░░░░░░░░░░░░░░░░░░░░░ 70%  🔴 RED │
│ NIS2:  ██████░░░░░░░░░░░░░░░░░░░░░░░░ 60%  🔴 RED │
│                                                     │
├─ TOP KPIs ──────────────────────────────────────┤
│ MTTD:           48h → target 30 min  🔴           │
│ MTTR Critical:  7h  → target 4h     🔴           │
│ Patch % <7d:    92% → target 95%    🟡           │
│ Phishing Click: 8%  → target 5%     🟡           │
│                                                     │
├─ FINANCIAL IMPACT ───────────────────────────────┤
│ Current ALE:       €8.2M annually               │
│ Post-Investment:   €4.8M annually               │
│ Savings:           €3.4M (41% reduction)        │
│ Investment 12m:    €680K                        │
│ ROI:               574% | Payback 1.4m          │
│ NPV 5-year:        €15.2M                        │
│                                                     │
├─ PRIORITY ACTIONS (NEXT 90 DAYS) ──────────────┤
│ 1. ✅ MTTD improvement (SIEM+SOAR)              │
│ 2. ✅ FAIR quantification                       │
│ 3. ✅ Patch SLA enforcement                     │
│ 4. ⚠️  NIS2 gap assessment                      │
│ 5. ⚠️  Vendor audit program                     │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## **FORMULACIONES CLAVE**

### **IGM Calculation (Tab 6)**

```Excel
=AVERAGE(
  Gobernanza_Score,
  Cuantificacion_Score,
  ThreatModeling_Score,
  SOC_Score,
  Vulnerabilities_Score,
  SupplyChain_Score,
  Awareness_Score,
  Compliance_Score,
  Automation_Score
)

Domain_Score = AVERAGE(Indicators_in_Domain)
Maturity_Level = IF(IGM<1.5,"Startup",IF(IGM<2.5,"Formativo",IF(IGM<3.5,"Establecido",IF(IGM<4.5,"Estratégico","Dinámico"))))
```

### **PRAGMATIC Score Calculation**

```Excel
=AVERAGE(P, R, A, G, M, A, T, I, C)

Recommendation = IF(PRAGMATIC<3,"No Implementar",IF(PRAGMATIC<3.5,"Mejorar",IF(PRAGMATIC<4,"Aceptable","Fuerte")))
```

### **Compliance Score Calculation**

```Excel
=COUNTIF(Indicadores_Cumplimiento,"Yes") / COUNTA(Indicadores_Cumplimiento) * 100

Sancion_Potencial = IF(Compliance<50%, "€10-20M", IF(Compliance<80%, "€5-10M", IF(Compliance<95%, "€1-5M", "€0")))
```

---

## **INSTRUCCIONES DESCARGA & IMPLEMENTACIÓN**

1. **Descargar:** CRM_IGM_PRAGMATIC_ROI_Calculator.xlsx
2. **Input:** Rellenar Tab 1 (25 indicadores)
3. **Auto-Calculate:** Tabs 2-6 calculan automáticamente
4. **Export:** Tab 6 lista para presentación ejecutiva
5. **Monthly Update:** Actualizar indicadores mes a mes

**Tiempo implementación:** 2-3 horas inicial + 1h mensual

---

## **BENCHMARK DATA INCLUIDA**

Archivo contiene datos baseline:
- **España 2024 median** (n=200 orgs)
- **EU leaders** (Netherlands, Germany, Finland)
- **Financial sector comparables**
- **Historical trends** (2022-2026)

Permite benchmarking automático vs peers.

---

*Fin Plantilla IGM + PRAGMATIC + ROI Calculator*

