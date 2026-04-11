# PLANTILLA EXCEL: CÁLCULO DE IGM (ÍNDICE DE GOBERNANZA MADUREZ) Y ROI
## Guía Markdown para Implementación en Spreadsheet

**Versión**: 2.0  
**Fecha**: Enero 2026  
**Clasificación**: Profesional | Herramienta Técnica  
**Propósito**: Calcular madurez organizacional en gobernanza IA y ROI de remediación  
**Software Recomendado**: Google Sheets, Excel, Numbers (plantilla compatible con todos)

---

## I. DESCRIPCIÓN GENERAL

Esta plantilla Excel/Sheets calcula dos métricas integrales:

1. **IGM (Índice de Gobernanza Madurez)**: Puntuación 1.0-5.0 de madurez NIST AI RMF
2. **ROI (Return on Investment)**: Beneficio financiero de remediación de gaps

**Estructura**: 5 hojas (sheets) interconectadas

---

## II. HOJA 1: SCORING INDICADORES (Input)

### Propósito
Entrada de puntuaciones de 12 indicadores principales

### Estructura de Columnas

```
| Fila | Columna A | Columna B | Columna C | Columna D | Columna E |
|-----|----------|----------|----------|----------|----------|
| 1   | Módulo   | Indicador| Peso (%) | Puntuación | Puntaje Ponderado |
|     |          |          | (recomendado) | (1-5) | (B×C) |
|-----|----------|----------|----------|----------|----------|
| 2   | GOVERN   | 1.1 Política Formal | 8% | [USER INPUT] | =D2*C2 |
| 3   | GOVERN   | 1.2 RACI Matrix | 8% | [USER INPUT] | =D3*C3 |
| 4   | GOVERN   | 1.3 Risk Tolerance | 8% | [USER INPUT] | =D4*C4 |
| 5   | GOVERN   | 1.4 IA Inventory | 8% | [USER INPUT] | =D5*C5 |
| 6   | MAP      | 2.1 Stakeholder Impact | 8% | [USER INPUT] | =D6*C6 |
| 7   | MAP      | 2.2 Risk Matrix | 8% | [USER INPUT] | =D7*C7 |
| 8   | MEASURE  | 3.1 Accuracy Monitoring | 8% | [USER INPUT] | =D8*C8 |
| 9   | MEASURE  | 3.2 Fairness Audit | 9% | [USER INPUT] | =D9*C9 |
| 10  | MEASURE  | 3.3 Explainability | 8% | [USER INPUT] | =D10*C10 |
| 11  | MEASURE  | 3.4 Security MTTD | 8% | [USER INPUT] | =D11*C11 |
| 12  | MANAGE   | 4.1 MTTR Remediation | 9% | [USER INPUT] | =D12*C12 |
| 13  | MANAGE   | 4.2 Validation % | 8% | [USER INPUT] | =D13*C13 |
|-----|----------|----------|----------|----------|----------|
| 14  | TOTAL    | IGM (Índice Gobernanza Madurez) | 100% | = | =SUM(E2:E13) |
```

### Fórmulas en Columna E (Puntaje Ponderado)

```
Fila 2: =D2*C2   (si D2=3, C2=0.08 → E2 = 0.24)
Fila 3: =D3*C3
...
Fila 13: =D13*C13

Total (E14): =SUM(E2:E13)
```

### Explicación de Pesos

**Pesos Predeterminados (100% total)**:
- GOVERN: 32% (4 indicadores × 8%)
- MAP: 16% (2 indicadores × 8%)
- MEASURE: 33% (3×8% + 1×9% fairness critical)
- MANAGE: 19% (1×9% critical + 1×8%)

**Lógica de Pesos**:
- MEASURE tiene mayor peso: Medición es acción; gobernanza es soporte
- Fairness (3.2) y MTTR (4.1) son críticos (9% cada uno) → compliance + remediación

**Customización Permitida**: 
- Cambiar pesos según prioritario organizacional
- Ej: "Fairness muy crítico" → aumentar a 12%; reducir otros proporcionalmente
- Constraint: Total = 100%

### Validación de Entrada

```
Validaciones Excel a implementar:

Para columna D (Puntuación 1-5):
├─ Data Validation: Whole number
├─ Minimum: 1
├─ Maximum: 5
└─ Show error message: "Puntuación debe estar entre 1 y 5"

Para columna C (Peso %):
├─ Data Validation: Decimal
├─ Minimum: 0
├─ Maximum: 1 (representa 100%)
└─ Cell format: Percentage
```

---

## III. HOJA 2: ANÁLISIS DE GAPS (Processed)

### Propósito
Identificar gaps y priorizarlos; calcula "brecha a target"

### Estructura

```
| Fila | Columna A | B | C | D | E | F |
|-----|----------|---|---|---|----|-----|
| 1   | Indicador | Scoring Actual | Target | Gap | Prioridad | Esfuerzo |
|-----|----------|---|---|---|----|-----|
| 2   | 1.1 Policy| 3 | 4 | -1 | 2 | Bajo |
| 3   | 1.2 RACI | 2 | 3 | -1 | 1 | Bajo |
| 4   | 1.3 RiskTol | 2 | 4 | -2 | 1 | Medio |
| 5   | 1.4 Invent | 2.5 | 4 | -1.5 | 1 | Bajo |
| ... | ... | ... | ... | ... | ... | ... |
|-----|----------|---|---|---|----|-----|
| 14  | TOTAL IGM | 2.48 | 3.5 | -1.02 | | |
```

### Fórmulas

```
Columna D (Gap): =C2-B2  (Target - Actual)
Columna E (Prioridad): 
  =IF(D2<-1.5, 1, IF(D2<-0.75, 2, 3))
  (Gap >1.5 = Prioridad 1; 0.75-1.5 = P2; <0.75 = P3)

Columna F (Esfuerzo):
  Manual based on domain knowledge
  Values: "Bajo (<40h)", "Medio (40-200h)", "Alto (>200h)"
```

### Visualización

Gráfico recomendado: **Waterfall** (actual → target, mostrando gaps)

```
Target (5.0)
     ├─ Gap MEASURE (largest)
     ├─ Gap MANAGE
     ├─ Gap MAP
     └─ Actual (2.48)
```

---

## IV. HOJA 3: CÁLCULO ROI (Risk-Based)

### Propósito
Cuantificar beneficio financiero de cerrar gaps (FAIR model)

### Estructura - Baseline Risk Assessment

```
| Fila | Elemento | Valor | Fórmula/Justificación |
|-----|----------|-------|----------------------|
| 1   | COMPONENTE: Risk Event Frequency (LEF) |
| 2   | Annual Incidents Baseline (actual/extrapolado) | 3 | |
|     | Justificación: 2024 data España: 97.348 incidentes |
|     | Aplicable a sector financiero/público: ~3/año |
| 3   | Probability each incident = Loss (%) | 30% | ~30% de incidents → actual breach |
| 4   | Loss Event Frequency (LEF) = B2*B3 | 0.9 | = 3 × 0.30 |
|-----|----------|-------|----------------------|
| 5   | COMPONENTE: Loss Magnitude (LM) |
| 6   | Direct costs per incident (€) | €500K | |
|     | Breakdown: | | |
|     | - Forensics/IR: €100K | | |
|     | - Regulatory fine (small): €100K | | |
|     | - Compliance effort: €150K | | |
|     | - Customer notification: €50K | | |
|     | - Staff time: €100K | | |
| 7   | Indirect costs (reputational, lost revenue) (€) | €1.5M | |
|     | Estimate: 6-month customer loss 3% × €100M ARR | | |
| 8   | Total Loss per incident (€) | €2M | = B6 + B7 |
|-----|----------|-------|----------------------|
| 9   | RESULT: Annual Loss Expectancy (ALE) |
| 10  | ALE (Risk Quantified) = LEF × LM | €1.8M | = B4 × B8 |
|     | Interpretation: Expected loss if no changes | | |
|-----|----------|-------|----------------------|
| 11  | RESULT: Risk Reduction from Remediations |
| 12  | SIEM ML implementation → MTTD 4h→15min | 45% risk ↓ | Detection speed |
| 13  | Fairness audits → fair systems → avoid fines | 40% risk ↓ | Regulatory compliance |
| 14  | Enhanced training → phishing clicks 25%→5% | 20% risk ↓ | Employee safety |
| 15  | Combined Risk Reduction = | 75% | Conservative: (45+40+20)/3 |
|-----|----------|-------|----------------------|
| 16  | New ALE (Post-Remediations) | €450K | = B10 * (1 - 0.75) |
|     | Annual savings = € 1.8M - €450K | €1.35M | Risk eliminated |
```

### Fórmulas

```
B4: LEF = =B2*B3          (Annual incidents × probability)
B10: ALE = =B4*B8         (LEF × Loss Magnitude)
B15: Risk Reduction = [LOOKUP based on remediation type]
B16: New ALE = =B10*(1-B15)
Savings = =B10-B16
```

---

### Estructura - Investment Requirements

```
| Fila | Remediación | Costo | Timeline | MTTR Improvement |
|-----|-----------|-------|----------|------------------|
| 18  | PRIORITY 1 | | | |
| 19  | 1.1 Policy formalization | €20K | 2 sem | 0 (governance) |
| 20  | 1.2 RACI documentation | €5K | 2 sem | 0 (governance) |
| 21  | 1.3 Risk tolerance scales | €10K | 2 sem | 0 (governance) |
| 22  | 3.2 Fairness audit platform | €80K | 4 sem | 5% risk ↓ |
| 23  | 4.1 SIEM ML implementation | €150K | 12 sem | 40% risk ↓ |
| 24  | 3.4 Security MTTD deployment | €100K | 8 sem | 20% risk ↓ |
|-----|-----------|-------|----------|------------------|
| 25  | SUBTOTAL P1 (First 12 weeks) | €365K | | |
|-----|-----------|-------|----------|------------------|
| 26  | PRIORITY 2 | | | |
| 27  | 3.1 Accuracy monitoring | €40K | 8 sem | 5% risk ↓ |
| 28  | 2.1 Stakeholder assessment | €30K | 6 sem | 2% risk ↓ |
| 29  | Advanced training program | €50K | 12 sem | 3% risk ↓ |
|-----|-----------|-------|----------|------------------|
| 30  | SUBTOTAL P2 | €120K | | |
|-----|-----------|-------|----------|------------------|
| 31  | TOTAL INVESTMENT YEAR 1 | €485K | | |
```

### Fórmulas

```
B25: =SUM(B19:B24)        (Total Priority 1)
B30: =SUM(B27:B29)        (Total Priority 2)
B31: =B25+B30             (Grand total)
```

---

### Estructura - ROI Calculation

```
| Fila | Métrica | Valor | Cálculo |
|-----|---------|-------|---------|
| 33  | ANNUAL SAVINGS (Risk reduction) | €1.35M | From Section 3 |
| 34  | YEAR 1 INVESTMENT | €485K | From Section 4 |
| 35  | NET BENEFIT YEAR 1 | €865K | =B33-B34 |
| 36  | ROI YEAR 1 (%) | 178% | =(B35/B34)*100 |
|-----|---------|-------|---------|
| 37  | PAYBACK PERIOD (months) | 4.3 | =(B34/B33)*12 |
|-----|---------|-------|---------|
| 38  | 3-YEAR PROJECTION | | |
| 39  | Cumulative savings (3 years) | €4.05M | =B33*3 |
| 40  | Ongoing investment (maintenance) | €150K/año | SIEM, training |
| 41  | Net 3-year benefit | €3.6M | =B39-(B34+B40*3) |
| 42  | 3-Year ROI | 643% | =(B41/(B34+B40*3))*100 |
|-----|---------|-------|---------|
```

### Fórmulas

```
B35: =B33-B34
B36: =(B35/B34)*100
B37: =(B34/B33)*12         (Payback in months)
B39: =B33*3
B41: =B39-(B34+B40*3)
B42: =(B41/(B34+B40*3))*100
```

### Validación de Números

```
Sanity checks Excel:

1. LEF >0 and <1 (probability of incident per year): 
   =IF(AND(B4>0,B4<1),"OK","Check LEF")

2. Loss Magnitude >0:
   =IF(B8>0,"OK","Loss cannot be negative")

3. ALE (B10) = LEF × LM:
   =IF(ABS(B10-B4*B8)<100,"OK","Check ALE calculation")

4. ROI positive after 3 years:
   =IF(B42>0,"Positive ROI","Negative ROI - reconsider")
```

---

## V. HOJA 4: DASHBOARD EJECUTIVO (Visualización)

### Propósito
Resumen visual para presentation a Board

### Elementos del Dashboard

**1. IGM Gauge (KPI visual)**
```
Formato: Bullet chart o gauge
├─ Minimum: 1.0 (Ad-hoc)
├─ Target: 3.5 (Definido+)
├─ Excellent: 4.5 (Cuantificado)
└─ Actual: [Dynamic, pulls from Hoja 1, B14]

Example visual: 
    1.0 ----[●]------------- 3.5 ----------- 4.5 --- 5.0
    (Actual 2.48 at 49% progress to target 3.5)
```

**2. IGM por Módulo (Breakout)**
```
Gráfico: Horizontal bar chart
├─ GOVERN:    2.5/5.0 ██████░░░░
├─ MAP:       3.0/5.0 ██████░░░░
├─ MEASURE:   2.0/5.0 ████░░░░░░
├─ MANAGE:    2.5/5.0 █████░░░░░
└─ OVERALL:   2.48/5.0 [bullet chart]

Data source: Average of indicators per module (Hoja 1)
```

**3. ROI Waterfall**
```
Gráfico: Waterfall chart
├─ Starting Risk (ALE):       €1.8M [upward]
├─ Fairness remediations:   -€400K [downward]
├─ SIEM ML improvement:     -€720K [downward]
├─ Training enhancement:    -€230K [downward]
└─ Ending Risk (New ALE):     €450K [final]

Label: "Annual Risk Reduction: €1.35M"
```

**4. Payback Period Timeline**
```
Gráfico: Line chart
X-axis: Months (0-36)
Y-axis: Cumulative savings (€M)
├─ Investment spend (downward): -€485K (Year 1)
├─ Cumulative savings (upward): +€1.35M/año
├─ Payback point: Month 4.3 (crossover)
└─ 3-year net benefit: €3.6M

Label: "ROI 643% over 3 years; Payback in 4.3 months"
```

**5. Gap Priority Matrix (Heatmap)**
```
Gráfico: Scatter plot (Criticality vs. Effort)

      Criticidad (Impact)
      ↑ High
      |
      | [Fairness]  [SIEM ML]
  Med |  [RACI]     [MTTR]      [Training]
      | [Policy]
      | 
   Low|________________→ Effort
            Low    Med   High

Color coding:
- Red (top-left): High criticality, low effort = QUICK WINS
- Orange (top-right): High criticality, high effort = STRATEGIC
- Yellow (middle): Medium = ROADMAP
- Green (bottom): Low priority = BACKLOG
```

---

## VI. HOJA 5: ASSUMPTIONS & SENSITIVITY ANALYSIS

### Propósito
Document assumptions and test robustness of ROI

### Structure

```
| Elemento | Baseline | Optimistic | Pessimistic | Impact on ROI |
|----------|----------|-----------|------------|--------------|
| Annual Incidents | 3 | 2 | 5 | ±25% |
| Breach Probability (%) | 30% | 20% | 50% | ±35% |
| Loss per incident (€) | €2M | €1.5M | €3M | ±20% |
| Risk reduction % | 75% | 85% | 60% | ±30% |
| Implementation cost | €485K | €400K | €600K | ±15% |
| Timeline (months) | 12 | 8 | 16 | ±20% |
|----------|----------|-----------|------------|--------------|
| SCENARIO OUTCOMES | | | | |
| Base Case ROI | 178% | 280% | 95% | — |
| 3-Year ROI | 643% | 850% | 420% | — |
```

### Sensitivity Table (Tornado Diagram)

```
Shows which assumptions most impact ROI:

Risk Reduction %:    ← 95% --- 178% --- 260% → (range: 165pp)
Loss per Incident:   ← 115% --- 178% --- 240% → (range: 125pp)
Annual Incidents:    ← 125% --- 178% --- 235% → (range: 110pp)
Implementation Cost: ← 160% --- 178% --- 195% → (range: 35pp)
Breach Probability:  ← 165% --- 178% --- 190% → (range: 25pp)

Interpretation: "Risk Reduction %" is most critical assumption
(largest impact on ROI). If wrong, ROI could be 95%-260%
```

### Assumptions Documentation

```
Key assumptions underlying ROI calculation:

1. Annual Incidents: 3/año
   - Source: INCIBE data España (97,348 total 2024 / 30K+ organizations)
   - Applicability: Financial sector, >1000 employees, IA exposure
   - Risk if wrong: ±25% on ROI if incidents actually 2-5/año

2. Breach Probability: 30%
   - Source: Industry surveys (Verizon, Mandiant)
   - Assumption: "Incident" ≠ "Breach"; 30% escalate to breach
   - Risk if wrong: ±35% on ROI if probability 15-50%

3. Loss per Incident: €2M average
   - Components:
     * Direct: €500K (IR, forensics, notification)
     * Indirect: €1.5M (6 months customer churn 3%)
   - Sensitivity: €1.5M-€3M realistic range
   - Risk: If breach affects small subset, loss could be €500K only

4. Risk Reduction: 75% from remediations
   - Breakdown:
     * SIEM MTTD improvement: 45% reduction
     * Fairness audits: 40% reduction
     * Training: 20% reduction
     * Combined (conservative overlap): 75%
   - Risk: If implementations less effective, could be 50%

5. Implementation Cost: €485K (Year 1)
   - Based on market rates: SIEM €100-150K, fairness audit €50-100K, etc.
   - Assumption: No major delays or scope creep
   - Risk: 20% overruns typical (€600K possible)

6. Timeline: 12 months full implementation
   - P1: 3 months (quick wins)
   - P2: 6 months (strategic initiatives)
   - Assumes 2 dedicated FTE equivalent
   - Risk: Could extend if resource constraints
```

---

## VII. INSTRUCCIONES DE IMPLEMENTACIÓN

### Paso 1: Crear estructura en Excel/Sheets

```
1. Crear 5 hojas (tabs): Scoring, Gaps, ROI, Dashboard, Assumptions
2. En "Scoring": 
   - Importar 12 indicadores (copiar de Hoja 1)
   - Crear columnas A-E (Módulo, Indicador, Peso, Scoring, Ponderado)
   - Aplicar data validation (puntuación 1-5)
   - Crear fórmulas suma (E14)
3. En "Gaps":
   - Crear columnas (Indicador, Actual, Target, Gap, Prioridad, Esfuerzo)
   - Pull data from "Scoring" (actual) y manual target entry
   - Crear fórmulas gap y prioridad
   - Crear waterfall chart
4. En "ROI":
   - Secciones: LEF, LM, ALE, Remediations, Investment, ROI Calc
   - Aplicar fórmulas FAIR model
   - Validar resultados sensatos
5. En "Dashboard":
   - 4 visualizations (Gauge IGM, Bar per módulo, Waterfall ROI, Payback timeline)
   - Link a datos "Scoring" y "ROI" (dynamic)
   - Crear scatter plot gap priority
6. En "Assumptions":
   - Tabla baseline/optimistic/pessimistic
   - Tornado sensitivity chart
   - Documentation de assumptions
```

### Paso 2: Entrada de Datos

```
1. Ejecutar encuesta GQM en 12 indicadores (de Encuesta_Integral_Ciberseguridad_IA.md)
2. Registrar puntuación 1-5 per indicador en columna D de "Scoring"
3. Validar entrada (rango 1-5)
4. Auto-calcula IGM global (E14) y visualizaciones (Dashboard)
5. Revisar gaps (Hoja "Gaps")
6. Estimar costos de remediación (Hoja "ROI")
7. Review ROI (esperado >100% Year 1 si gaps críticos)
```

### Paso 3: Presentación a Board

```
Usar "Dashboard" sheet:
1. Show IGM gauge: "We're at 2.48; target is 3.5 by Dec 2026"
2. Show module breakdown: "MEASURE is our biggest gap (2.0/5.0)"
3. Show ROI: "€1.35M annual savings; 178% ROI; 4.3 month payback"
4. Show gap priority: "These 5 remediations give us 75% risk reduction"
5. Risk: "If we don't act, expected annual loss is €1.8M"
6. Timeline: "12 months to full implementation; €485K investment"
7. Ask for approval of investment + executive sponsorship
```

---

## VIII. VALIDACIONES Y CONTROLES

### Pre-Submission Checklist

```
☐ All 12 indicators scored (no blanks in column D)
☐ Scores between 1-5 (data validation passed)
☐ Weights sum to 100% (column C total = 1.0)
☐ IGM calculated (E14 populated)
☐ Gaps analyzed (Hoja "Gaps" complete)
☐ LEF, LM, ALE calculated reasonably
   └─ LEF: 0-1 (probability per year)
   └─ LM: €500K-€5M (realistic loss)
   └─ ALE: €100K-€5M (depends on organization size)
☐ Remediations identify cost + timeline
☐ ROI calculated; sanity checks:
   └─ Year 1 ROI >0% (positive payback)
   └─ Payback period <18 months
   └─ 3-year ROI >100%
☐ Dashboard refreshes dynamically (no hardcoded values)
☐ Assumptions documented; sensitivity analysis reviewed
```

---

**Fin de Plantilla Excel**

*Documento de guía para implementación*  
*Enero 2026 | Profesional | España*

