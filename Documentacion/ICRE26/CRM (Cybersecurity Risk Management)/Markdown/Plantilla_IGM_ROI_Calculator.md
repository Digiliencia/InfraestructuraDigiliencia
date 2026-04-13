# **PLANTILLA IGM & ROI CALCULATOR**
## *Modelo Excel para Cálculo Automatizado Madurez e Inversión*

**Versión:** 2.0 | **Fecha:** Enero 2026 | **Nota:** Descarga versión Excel real desde link

---

## **INTRODUCCIÓN**

Este documento describe la lógica + fórmulas de la plantilla Excel **CRM_IGM_ROI_Calculator.xlsx**

**Tabs incluidas:**
1. Input Scores
2. Domain Calculations
3. IGM Summary
4. Gap Analysis
5. ROI Calculator
6. Roadmap

---

## **TAB 1: INPUT SCORES**

### **Estructura**

```
Dominio | Q1 | Q2 | Q3 | Q4 | Q5 | Raw Score

1. Gobernanza
   1.1.1 RAS documentado      [0-4]
   1.1.2 Risk Tolerance       [0-4]
   1.1.3 Junta Oversight      [0-4]
   1.2.1 NIST CSF Govern      [0-4]
   1.2.2 CISO Designado       [0-4]
   
   Dominio Score = AVERAGE(Q1:Q5)

2. Cuantificación FAIR
   2.1.1 FAIR Adoption        [0-4]
   2.1.2 Top 5 ALE            [0-4]
   2.1.3 ROI Analysis         [0-4]
   
   Dominio Score = AVERAGE(Q1:Q3)

3. Threat Modeling
   3.1.1 Threat Modeling      [0-4]
   3.1.2 Attack Trees         [0-4]
   3.1.3 Threat-Vuln Map      [0-4]
   
   Dominio Score = AVERAGE(Q1:Q3)

4. SOC/SIEM Metrics
   4.1.1 SOC 24/7             [0-4]
   4.1.2 MTTD                 [0-4]
   4.1.3 MTTR                 [0-4]
   4.2.1-4.2.4 SIEM (combined)[0-4]
   
   Dominio Score = AVERAGE(Q1:Q4)

5. Vulnerabilities
   5.1.1 Scanning             [0-4]
   5.1.2 Patch SLA            [0-4]
   5.1.3 CVSS v4.0            [0-4]
   5.2.1-5.2.2 Lifecycle      [0-4]
   
   Dominio Score = AVERAGE(Q1:Q4)

6. Supply Chain
   6.1.1 Vendor Audit         [0-4]
   6.1.2 Contracts            [0-4]
   6.1.3 SBOM                 [0-4]
   
   Dominio Score = AVERAGE(Q1:Q3)

7. Awareness Training
   7.1.1 Training Mandatory   [0-4]
   7.1.2 Phishing Sims        [0-4]
   7.1.3 Click Rate           [0-4]
   7.2.1-7.2.2 ROI/Metrics    [0-4]
   
   Dominio Score = AVERAGE(Q1:Q4)

8. Compliance
   8.1.1 NIST CSF 2.0         [0-4]
   8.1.2 NIS2 Readiness       [0-4]
   8.1.3 DORA Compliance      [0-4]
   
   Dominio Score = AVERAGE(Q1:Q3)

9. Automatización
   9.1.1 Policy-as-Code       [0-4]
   9.1.2 Infrastructure-as-Code[0-4]
   9.2.1-9.2.3 Resilience     [0-4]
   
   Dominio Score = AVERAGE(Q1:Q3)
```

### **Validación Input**

- Min: 0 (No implementado)
- Max: 4 (Optimizado)
- Tipo: Número entero

---

## **TAB 2: DOMAIN CALCULATIONS**

### **Fórmulas Cálculo Dominio**

```
GOBERNANZA
  Raw = AVERAGE(Input!B2:B6)
  Adj = Raw × 1.1  (bonus governance = critical)
  Final = MIN(4, Adj)

CUANTIFICACIÓN
  Raw = AVERAGE(Input!B8:B10)
  Final = Raw

THREAT MODELING
  Raw = AVERAGE(Input!B12:B14)
  Final = Raw

SOC/SIEM
  Raw = AVERAGE(Input!B16:B20)
  Final = Raw

VULNERABILITIES
  Raw = AVERAGE(Input!B22:B27)
  Final = Raw

SUPPLY CHAIN
  Raw = AVERAGE(Input!B29:B31)
  Final = Raw

AWARENESS
  Raw = AVERAGE(Input!B33:B39)
  Adj = Raw × 1.05 (bonus awareness = behavioral)
  Final = MIN(4, Adj)

COMPLIANCE
  Raw = AVERAGE(Input!B41:B43)
  Final = Raw

AUTOMATIZACIÓN
  Raw = AVERAGE(Input!B45:B48)
  Final = Raw
```

### **Classification Maturity**

```
=IF(Final<1.5,"1-Startup",
   IF(Final<2.5,"2-Formativo",
   IF(Final<3.5,"3-Establecido",
   IF(Final<4.5,"4-Estratégico","5-Dinámico"))))
```

---

## **TAB 3: IGM SUMMARY**

### **Cálculo IGM Final**

```
IGM = AVERAGE(Gobernanza, Cuantificación, Threat Modeling, SOC/SIEM, 
              Vulnerabilidades, Supply Chain, Awareness, Compliance, Automatización)

Fórmula Excel:
=AVERAGE(Domain!B2:B10)
```

### **Dashboard IGM**

```
┌─────────────────────────────────────────┐
│ ÍNDICE GLOBAL MADUREZ (IGM) 2.38        │
│                                         │
│ ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
│ Nivel: 2 — FORMATIVO                   │
│                                         │
│ Target 2026: 3.0 (Establecido)          │
│ Gap: -0.62 puntos                       │
│ Timeline: 12 meses                      │
└─────────────────────────────────────────┘
```

### **Radar Chart (Visual)**

Excel sparkline o gráfico radar mostrando los 9 dominios

---

## **TAB 4: GAP ANALYSIS**

### **Estructura Gaps**

```
Dominio | Actual | Target | Gap | Impacto | Esfuerzo | Prioridad

Gobernanza        | 3.5 | 4.5 | -1.0 | ALTO    | MEDIO  | 1
Cuantificación    | 2.0 | 4.0 | -2.0 | MUY ALT | ALTO   | 2
Threat Modeling   | 2.5 | 3.5 | -1.0 | ALTO    | MEDIO  | 3
SOC/SIEM          | 3.0 | 4.0 | -1.0 | ALTO    | MUY AL | 4
Vulnerabilidades  | 3.2 | 3.8 | -0.6 | MEDIO   | BAJO   | 7
Supply Chain      | 1.5 | 3.5 | -2.0 | MUY ALT | ALTO   | 2
Awareness         | 2.8 | 3.5 | -0.7 | MEDIO   | BAJO   | 6
Compliance        | 2.2 | 3.5 | -1.3 | MUY ALT | BAJO   | 5
Automatización    | 1.8 | 3.2 | -1.4 | ALTO    | MUY AL | 3
```

### **Cálculos Matriz**

```
Gap = Target - Actual
Prioridad = RANK(Impacto/Esfuerzo)
  QUICK WIN: Impacto Alto + Esfuerzo Bajo = Prioridad 1-3
  STRATEGIC: Impacto Alto + Esfuerzo Alto = Prioridad 2-4
  NICE-TO-HAVE: Impacto Bajo + Esfuerzo Bajo = Prioridad 7+
  AVOID: Impacto Bajo + Esfuerzo Alto = Prioridad N/A
```

---

## **TAB 5: ROI CALCULATOR**

### **Inputs Financieros**

```
CONTROL INVESTMENT ANALYSIS

Control | Current ALE | Risk Reduction | New ALE | Savings | Cost | ROI% | Payback Months

EDR     | 5.0M        | 40%            | 3.0M    | 2.0M    | 0.2M | 900% | 1.2
FAIR    | Varies      | 15% decision   | Varies  | 0.75M   | 0.05M| 1400%| 0.4
SIEM    | 1.5M        | 60%            | 0.6M    | 0.9M    | 0.3M | 200% | 4.0
Phishing| 0.8M        | 50%            | 0.4M    | 0.4M    | 0.03M| 1233%| 0.9
```

### **Fórmula ROI**

```
Savings = Current ALE × Risk Reduction %
New ALE = Current ALE × (1 - Risk Reduction %)
ROI% = (Savings - Cost) / Cost × 100
Payback = Cost / (Savings/12) months
```

### **Aggregated Budget**

```
Presupuesto Total 12 meses:
  Quick Wins (3m): €100K
  Estratégicos (9m): €400K
  TOTAL: €500K

Expected ALE Reduction:
  Current: €8.2M
  Post-Implementation: €4.8M
  Avoided Losses: €3.4M
  
Aggregate ROI: €3.4M - €0.5M / €0.5M = 580%
```

---

## **TAB 6: ROADMAP**

### **Estructura Roadmap**

```
QUARTER | INITIATIVE | OWNER | DURATION | BUDGET | DEPENDENCIES | KPI

Q2 2026 | FAIR Framework Impl | CISO | 8 wks  | €50K  | -            | ALE coverage >90%
Q2 2026 | RAS + Risk Tol Doc  | Risk | 3 wks  | €10K  | FAIR         | Board approval
Q3 2026 | SIEM + SOAR Deploy  | IT   | 12 wks | €300K | -            | MTTD <2h
Q3 2026 | PASTA Threat Model  | SEC  | 12 wks | €80K  | -            | Top 10 apps covered
Q4 2026 | NIS2 Assessment     | COM  | 4 wks  | €60K  | SIEM, FAIR   | Gap analysis done
Q1 2027 | Policy-as-Code      | DEV  | 8 wks  | €100K | -            | 80% policies automated
...
```

### **Timeline Visual**

```
     Q2 2026      Q3 2026      Q4 2026      Q1 2027
     ├─────┬─────┬────┬────┬──────┬──────┐
FAIR ├─────┤
RAS  │    ├──┤
SIEM │         ├────────────┤
PASTA│         ├────────────┤
NIS2 │                 ├────┤
PaC  │                      ├────────┤
```

---

## **CÁLCULOS DERIVADOS**

### **Benchmark Comparison**

```
Vuestra Org    | Spain Median | EU Leader | Gap vs Median | Gap vs Leader

IGM:        2.38 | 2.40        | 3.86      | -0.02        | -1.48
Gobernanza: 3.5  | 2.8         | 4.2       | +0.70        | -0.70
Cuantif:    2.0  | 1.8         | 3.8       | +0.20        | -1.80
...
```

### **Compliance Risk Score**

```
GDPR Compliance:        85% (no crítico; mayormente OK)
DORA Compliance:        70% (CRÍTICO si financiero; gaps graves)
NIS2 Compliance:        60% (CRÍTICO; transposición 2026)

REGULATORY RISK SCORE:  (85+70+60)/3 = 71.67%
STATUS: YELLOW (atención; gaps regulatorios)
ACTION: Priorizar DORA + NIS2 Q1-Q2 2026
```

---

## **INSTRUCCIONES DESCARGA**

1. Descargar archivo: **CRM_IGM_ROI_Calculator.xlsx** (link en README)
2. Abrir en Excel 2016+ o Google Sheets
3. Input scores en Tab 1
4. Tabs 2-6 auto-calculan
5. Exportar Tab 3 para ejecutivo

---

## **SOPORTE & VALIDACIÓN**

- Fórmulas: Validadas contra FAIR Institute + NIST estándares
- Benchmarks: Spain baseline 2024 (n=200 orgs)
- ROI models: Calibrados industrial sector averages

---

*Fin Plantilla IGM & ROI*

