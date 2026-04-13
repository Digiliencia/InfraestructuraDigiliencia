# PLANTILLA EXCEL: CÁLCULO IGM Y ROI INDICADORES CIBERSEGURIDAD-IA
## Implementación Step-by-Step en Excel

**Versión:** 1.0 | **Fecha:** Enero 2026  
**Contexto:** Cálculo Índice Gestión Métricas (IGM) + ROI para 9 Indicadores  
**Software:** Microsoft Excel / Google Sheets compatible

---

## INTRODUCCIÓN: IGM (ÍNDICE DE GESTIÓN DE MÉTRICAS)

El IGM es una métrica compuesta (0-100) que integra:
1. **Puntuación PRAGMATIC** (9 criterios, avg)
2. **Madurez GQM** (Nivel 0-5 capturado)
3. **Compliance Normativo** (% cumplimiento vs regulaciones)
4. **Implementación Operacional** (% deployed vs target)

**Fórmula IGM:**
```
IGM = (PRAGMATIC_Score × 0.40) + (GQM_Maturity × 20) + (Compliance_% × 0.30) + (Implementation_% × 0.10)
      × 100 / (0.40 + 0.30 + 0.10 + 0.20)
```

**Rango Interpretación:**
- 0-25: Inicial (Nivel 1-2)
- 26-50: Definido (Nivel 2-3)
- 51-75: Gestionado (Nivel 3-4)
- 76-100: Optimizado (Nivel 4-5)

---

## SECCIÓN 1: ESTRUCTURA PLANTILLA EXCEL

### HOJA 1: "Dashboard"

**Propósito:** Visión ejecutiva consolidada

**Estructura Filas/Columnas:**

```
┌─────────────────────────────────────────────────────────────────────┐
│ DASHBOARD EJECUTIVO - INDICADORES CIBERSEGURIDAD-IA ESPAÑA 2026      │
├─────────────────────────────────────────────────────────────────────┤
│ Fecha Actualización: [Celda: A2] = TODAY()                          │
│ Período: [Q1 2026]  Organización: [Editable]                        │
└─────────────────────────────────────────────────────────────────────┘

Fila 5-6: Encabezados

| A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|
| Indicador | GQM Level (0-5) | PRAGMATIC Avg | Compliance % | Deployment % | IGM Score (0-100) | ROI Year 1 (€) | Payback Period (meses) | Estado | Prioridad |
|---|---|---|---|---|---|---|---|---|---|

Filas 7-15: Datos por indicador

| 1. AI-Detection | [3] | [4.3] | [80%] | [60%] | [IGM_FORMULA] | [ROI_FORMULA] | [PAYBACK_FORMULA] | 🟢 On Track | P1 |
| 2. Vuln.Mgmt | [3] | [4.4] | [70%] | [50%] | [IGM_FORMULA] | [ROI_FORMULA] | [PAYBACK_FORMULA] | 🟢 On Track | P1 |
| 3. Deepfake | [2] | [3.1] | [40%] | [20%] | [IGM_FORMULA] | [ROI_FORMULA] | [PAYBACK_FORMULA] | 🟡 Monitor | P3 |
| 4. SIEM+Hunt | [3] | [4.4] | [60%] | [40%] | [IGM_FORMULA] | [ROI_FORMULA] | [PAYBACK_FORMULA] | 🟢 On Track | P1 |
| 5. Training | [2] | [4.2] | [80%] | [70%] | [IGM_FORMULA] | [ROI_FORMULA] | [PAYBACK_FORMULA] | 🟢 On Track | P1 |
| 6. Compliance | [2] | [3.7] | [100%] | [80%] | [IGM_FORMULA] | [ROI_FORMULA] | [PAYBACK_FORMULA] | 🟢 On Track | P2 |
| 7. Supply Chain | [1] | [4.0] | [50%] | [30%] | [IGM_FORMULA] | [ROI_FORMULA] | [PAYBACK_FORMULA] | 🟡 Monitor | P3 |
| 8. Incident Response | [2] | [4.6] | [60%] | [40%] | [IGM_FORMULA] | [ROI_FORMULA] | [PAYBACK_FORMULA] | 🟢 On Track | P1 |
| 9. Governance | [3] | [4.2] | [80%] | [90%] | [IGM_FORMULA] | [ROI_FORMULA] | [PAYBACK_FORMULA] | 🟢 On Track | P1 |
|---|---|---|---|---|---|---|---|---|---|
| PROMEDIO TOTAL | [=AVERAGE(B7:B15)] | [=AVERAGE(C7:C15)] | [=AVERAGE(D7:D15)] | [=AVERAGE(E7:E15)] | [=AVERAGE(F7:F15)] | [=SUM(G7:G15)] | [=AVERAGE(H7:H15)] | | |

Fila 17: Métricas de Impacto

| Métrica | Valor |
|---------|-------|
| Portfolio IGM Promedio | [=AVERAGE(F7:F15)] |
| Investment Total Year 1 | €1.9M [=SUM("Costs"!B:B)] |
| Expected ROI Year 1 | 26% [=(SUM(G7:G15)/1900000)] |
| Break-even (meses) | 18 |
| Cumulative ROI 3-year | €3.2M |
| Regulatory Compliance Avg | [=AVERAGE(D7:D15)]% |

```

---

### HOJA 2: "Detalle Indicadores"

**Propósito:** Nivel de detalle por indicador (9 hojas separadas, una por indicador)

**Ejemplo para Indicador 1 (AI-Detection):**

```
┌─────────────────────────────────────────────────────────────┐
│ INDICADOR 1: AI-THREAT DETECTION COVERAGE                   │
├─────────────────────────────────────────────────────────────┤

FILA 1-4: Metadatos
| Nombre Indicador | AI-Threat Detection Coverage |
| Código | IND-001 |
| GQM Goal | Reducir MTTD 181 días → <24 horas |
| Status | Green (🟢) |

FILA 6-10: PRAGMATIC Scores (Importado de Matriz PRAGMATIC)
| Criterio | Score (1-5) | Evidencia | Fuente |
| P - Predictivo | 5 | MTTD reduction = breach cost reduction | CNCS data |
| R - Relevante | 5 | NIS2 mandated | Regulatory |
| A - Accionable | 4 | Clear thresholds: <24h = goal met | Internal SLA |
| G - Genuino | 5 | Mide outcome real (no proxy) | SIEM telemetry |
| M - Significativo | 5 | Board-level importance | Strategic plan |
| P - Preciso | 4 | Timestamps en SIEM | Technical spec |
| T - Oportuno | 5 | Real-time SIEM data | Continuous |
| I - Independiente | 4 | Affected by threat sophistication | Threat landscape |
| C - Rentable | 3 | SIEM cost €180K annually | Budget |
| PRAGMATIC AVG | 4.3 | | |

FILA 12-16: GQM Madurez (Escala 0-5)
| Level 0 - Inexistente | [ ] Not implemented |
| Level 1 - Inicial | [ ] Ad-hoc |
| Level 2 - Repetible | [ ] Inconsistent |
| Level 3 - Definido | [✓] Selected (Current) |
| Level 4 - Gestionado | [ ] Cuantitativamente medido |
| Level 5 - Optimizado | [ ] Continuous innovation |

CURRENT LEVEL: 3
TARGET LEVEL: 5
TIMELINE TO TARGET: 12 meses

FILA 18-22: Compliance Normativo
| Normativa | Requisito | Cumplimiento | Gap | Plazo |
| NIS2 Art.17 | Coverage ≥80% essential entities | 80% ✓ | 0% | Agosto 2026 |
| Plan Nacional L4.3 | MTTD <24 horas | 15% (MTTD 50d actual) | -85% | Q4 2026 |
| ISO 27001 A.16.1.5 | Monitoring systems required | 70% | -30% | Ongoing |
| EU AI Act Art.37 | Risk assessment documented | 60% | -40% | 2026 |
| COMPLIANCE AVG | | 56% | | |

FILA 24-28: Implementación Operacional (Current State)
| Componente | Target | Current | % Deployed | Inversión |
| SIEM Deployment | 100% | 70% | 70% | €150K invested |
| ML Correlation Engine | 100% | 40% | 40% | €80K needed |
| Threat Intel Integration | 100% | 30% | 30% | €50K needed |
| Alert Tuning/Optimization | 100% | 20% | 20% | €30K needed |
| DEPLOYMENT AVG | | | 40% | €310K total Phase 1 |

FILA 30-32: IGM Calculation
| Formula Component | Value | Weight | Weighted |
| PRAGMATIC Score (4.3) | 4.3 | 40% | 1.72 |
| GQM Level (3 → 20 pts) | 20 | 30% | 6.0 |
| Compliance % (56%) | 56 | 20% | 11.2 |
| Deployment % (40%) | 40 | 10% | 4.0 |
| IGM SCORE | 62.92 | | = Nivel 4 (Gestionado) |

FILA 34-36: Métricas Clave
| Métrica | Baseline | Target 2026 | Progreso |
| MTTD (días) | 50 | <24 | En progreso |
| Coverage % | 60% | 95% | 67% complete |
| False Positive Rate | 30% | <15% | En progreso |

```

---

### HOJA 3: "Costs & ROI"

**Propósito:** Desglose costos CapEx/OpEx + cálculo ROI

```
┌─────────────────────────────────────────────────────────────┐
│ COSTS & ROI ANALYSIS - YEAR 1 (2026)                         │
├─────────────────────────────────────────────────────────────┘

FILA 1-4: Resumen Ejecutivo ROI

| Métrica | Valor |
|---------|-------|
| Total Investment Year 1 | €1,900,000 |
| Expected Cost Avoidance | €500,000 - €2,000,000 |
| ROI Estimated | 26% - 105% |
| Payback Period | 12-18 meses |

FILA 6-30: Desglose por Indicador (Capex + Opex)

| Indicador | Elemento | Tipo | Cantidad | Unit Cost | Total Year 1 |
|-----------|----------|------|----------|-----------|--------------|
| **1. AI-Detection** | SIEM Enhancement | CapEx | 1 | €150,000 | €150,000 |
| | SIEM Annual License | OpEx | 1 | €100,000 | €100,000 |
| | ML Model Training | CapEx | 200 hrs | €300/hr | €60,000 |
| | SOC Analyst (0.5 FTE) | OpEx | 0.5 | €75,000 | €37,500 |
| | **Subtotal IND-1** | | | | **€347,500** |
| | | | | | |
| **2. Vuln.Mgmt** | Scanning Tools (license upgrade) | CapEx | 1 | €80,000 | €80,000 |
| | Annual Maintenance | OpEx | 1 | €40,000 | €40,000 |
| | SBOM Integration | CapEx | 1 | €60,000 | €60,000 |
| | VA Analyst (0.5 FTE) | OpEx | 0.5 | €75,000 | €37,500 |
| | **Subtotal IND-2** | | | | **€217,500** |
| | | | | | |
| **3. Deepfake** | Pilot Technology (first year) | CapEx | 1 | €200,000 | €200,000 |
| | Deployment (deferred to 2027) | CapEx | 0 | - | €0 |
| | **Subtotal IND-3** | | | | **€200,000** |
| | | | | | |
| **4. SIEM+Hunting** | Threat Hunting Platform | CapEx | 1 | €150,000 | €150,000 |
| | Annual License | OpEx | 1 | €80,000 | €80,000 |
| | Threat Hunting Team (1.5 FTE) | OpEx | 1.5 | €75,000 | €112,500 |
| | **Subtotal IND-4** | | | | **€342,500** |
| | | | | | |
| **5. Training** | Phishing Simulator Upgrade | CapEx | 1 | €40,000 | €40,000 |
| | Annual License | OpEx | 1 | €25,000 | €25,000 |
| | Training Content Development | CapEx | 1 | €15,000 | €15,000 |
| | **Subtotal IND-5** | | | | **€80,000** |
| | | | | | |
| **6. Compliance** | NIS2 Assessment (external) | CapEx | 1 | €80,000 | €80,000 |
| | Compliance Officer (0.3 FTE) | OpEx | 0.3 | €75,000 | €22,500 |
| | EU AI Act Gap Analysis | CapEx | 1 | €50,000 | €50,000 |
| | **Subtotal IND-6** | | | | **€152,500** |
| | | | | | |
| **7. Supply Chain** | SBOM Tools | CapEx | 1 | €120,000 | €120,000 |
| | Vendor Assessment Program | CapEx | 1 | €40,000 | €40,000 |
| | **Subtotal IND-7** | | | | **€160,000** |
| | | | | | |
| **8. Incident Response** | SOAR Platform | CapEx | 1 | €200,000 | €200,000 |
| | Annual Subscription | OpEx | 1 | €100,000 | €100,000 |
| | Playbook Development | CapEx | 200 hrs | €300/hr | €60,000 |
| | IR Team (0.5 FTE) | OpEx | 0.5 | €75,000 | €37,500 |
| | **Subtotal IND-8** | | | | **€397,500** |
| | | | | | |
| **9. Governance** | Governance Assessment | CapEx | 1 | €30,000 | €30,000 |
| | Board Reporting Tools | CapEx | 1 | €15,000 | €15,000 |
| | **Subtotal IND-9** | | | | **€45,000** |
| | | | | | |
| | **TOTAL CAPEX (2026)** | | | | **€1,155,000** |
| | **TOTAL OPEX (2026)** | | | | **€745,000** |
| | **TOTAL INVESTMENT (2026)** | | | | **€1,900,000** |

FILA 32-50: ROI Calculation

| Scenario | Baseline Assumption | Calculation |
|----------|-------------------|-------------|
| **CONSERVATIVE Scenario** | 1 breach prevented (annual) | |
| Incident Cost Avoided | 1 × €500,000 = | €500,000 |
| Implementation Cost | | €1,900,000 |
| Net Benefit Year 1 | | -€1,400,000 |
| Year 2-3 Cumulative | €500K × 2 additional breaches prevented = | €1,000,000 |
| 3-Year ROI | | -€400,000 (break-even year 4) |
| | | |
| **REALISTIC Scenario** | 40% incident reduction + 20% faster response | |
| Incident Cost Avoidance | 2 incidents prevented × €500K = | €1,000,000 |
| Response Time Savings | 100 incidents × €10K cost reduction = | €1,000,000 |
| Total Annual Benefit | | €2,000,000 |
| Implementation Cost | | €1,900,000 |
| Net Benefit Year 1 | | €100,000 |
| Year 2-3 Cumulative | €2M × 2 years = | €4,000,000 |
| 3-Year ROI | | 110% |
| Payback Period | | ~11 months |
| | | |
| **OPTIMISTIC Scenario** | Industry peer benchmark (Gartner) | |
| Incident Cost Avoidance | 3 incidents prevented × €750K avg = | €2,250,000 |
| Response Efficiency Gains | 150 hrs analyst time saved × €300/hr = | €45,000 |
| Regulatory Penalty Avoidance | Estimated €250K-€500K range = | €250,000 |
| Total Annual Benefit | | €2,545,000 |
| Net Benefit Year 1 | | €645,000 |
| Payback Period | | ~9 months |

FILA 52-54: Sensitivity Analysis

| Variable | -20% | Base | +20% | Impact on ROI |
|----------|------|------|------|---------------|
| Incident Cost | €400K | €500K | €600K | ±€200K on Year 1 |
| Breach Probability | -40% reduction | -20% | 0% | ±€1M on Year 1 |
| Implementation Timeline | +3 months | On-track | -2 months | ±€300K on Year 1 |

```

---

### HOJA 4: "Maturity Trajectory"

**Propósito:** Proyección de madurez 18-24 meses

```
┌─────────────────────────────────────────────────────────────┐
│ MATURITY TRAJECTORY PROJECTION (2026-2027)                  │
├─────────────────────────────────────────────────────────────┘

FILA 1-4: Timeline Overview

| Fase | Período | Indicadores | Target IGM | Investment |
|------|---------|-----------|-----------|-----------|
| **Phase 1: Foundation** | Q1 2026 | 9 (Governance baseline) | 50 | €0 (internal) |
| **Phase 2: Critical Immediate** | Q1-Q2 2026 | 1,2,4,5,8 + 9 cont. | 60 | €1.2M |
| **Phase 3: Mandated** | Q2-Q3 2026 | 6 (Compliance) | 70 | €150K |
| **Phase 4: Secondary** | Q3-Q4 2026 | 3 (Deepfake) | 65 | €500K |
| **Phase 5: Advanced** | Q4 2026-Q1 2027 | 7 (Supply Chain) | 75 | €350K |
| **Phase 6: Optimization** | 2027 | All 9 integrated | 85 | €400K |

FILA 6-15: Quarter-by-Quarter IGM Projection

| Indicador | Q4 2025 (Baseline) | Q1 2026 | Q2 2026 | Q3 2026 | Q4 2026 | Q1 2027 | Q2 2027 |
|-----------|------------------|--------|--------|--------|--------|--------|--------|
| 1. AI-Detection | 35 | 45 | 55 | 65 | 75 | 80 | 85 |
| 2. Vuln.Mgmt | 40 | 50 | 60 | 70 | 75 | 80 | 85 |
| 3. Deepfake | 15 | 20 | 25 | 30 | 40 | 50 | 60 |
| 4. SIEM+Hunt | 30 | 40 | 55 | 70 | 75 | 80 | 85 |
| 5. Training | 45 | 55 | 65 | 70 | 75 | 80 | 85 |
| 6. Compliance | 50 | 60 | 75 | 85 | 90 | 92 | 95 |
| 7. Supply Chain | 20 | 25 | 30 | 40 | 55 | 70 | 75 |
| 8. Incident Response | 35 | 50 | 65 | 75 | 80 | 85 | 90 |
| 9. Governance | 55 | 70 | 75 | 80 | 85 | 88 | 90 |
| **PORTFOLIO AVG** | **38** | **46** | **57** | **69** | **76** | **81** | **86** |

FILA 17-19: Interpretación por Nivel

| Portfolio IGM | Nivel | Características |
|---------------|-------|------------------|
| 0-25 | 1 - Inicial | Ad-hoc; no processes; high risk |
| 26-50 | 2 - Repetible | Processes emerging; inconsistent execution |
| 51-75 | 3 - Definido | Formal processes; consistent execution; board aware |
| 76-100 | 4-5 - Gestionado/Optimizado | Automated; metrics-driven; continuous improvement |

FILA 21-25: Key Milestones

| Hito | Fecha | Indicador(es) | Criterio Éxito | Responsable |
|------|-------|---------------|----------------|-----------|
| Governance Formalization | 31-Mar-2026 | 9 | CISO reporting to CEO | CISO |
| NIS2 Assessment Complete | 15-Jun-2026 | 1,2,6 | 80% compliance documented | Risk Head |
| SIEM Operationalization | 30-Jun-2026 | 1,4 | <24h MTTD for 80% of incidents | CTO |
| Phishing Campaign Launch | 15-Apr-2026 | 5 | Baseline click-rate <15% | Security Awareness Lead |
| Incident Response First Playbook | 31-May-2026 | 8 | MTTR <1 hour (automated) | IR Lead |
| EU AI Act Gap Resolution | 31-Aug-2026 | 6 | 90% gaps remediated | Compliance Officer |
| Supply Chain SBOM Pilot | 30-Sep-2026 | 7 | 50% vendor SBOMs collected | Procurement Lead |

```

---

### HOJA 5: "Raw Data Input"

**Propósito:** Entrada de datos brutos para cálculos

```
┌─────────────────────────────────────────────────────────────┐
│ RAW DATA INPUT - MEASUREMENT SHEET                          │
├─────────────────────────────────────────────────────────────┘

Instrucciones: Actualizar mensualmente con datos más recientes

FILA 1-5: Metadata

| Parameter | Value |
|-----------|-------|
| Organization | [ORGANIZATION NAME] |
| Assessment Date | [DATE] |
| Assessor | [NAME] |
| Review Status | [Draft / Final] |

FILA 7-50: Metric Raw Values (por indicador)

## Indicador 1: AI-Detection

| Métrica | Formula | Current Value | Data Source | Last Update |
|---------|---------|---------------|------------|--------------|
| Coverage % (M1.1) | (Assets con ML-IDS / Total assets críticos) × 100 | 60% | SIEM inventory | Jan 2026 |
| MTTD días (M1.2) | Avg(Detection_time - Event_time) | 50 días | Incident logs | Jan 2026 |
| FP Rate % (M1.3) | (False_alerts / Total_alerts) × 100 | 28% | SIEM metrics | Jan 2026 |
| Model Accuracy % (M1.4) | Correct_predictions / Total | 87% | Model testing | Jan 2026 |

## Indicador 2: Vulnerability Management

| Métrica | Formula | Current Value | Data Source | Last Update |
|---------|---------|---------------|------------|--------------|
| Scanning Coverage % (M2.1) | (Systems scanned / Total systems) × 100 | 55% | VA tools | Jan 2026 |
| MTTR días (M2.2) | Avg(Remediation - Detection) | 22 días | Ticketing | Jan 2026 |
| SLA Compliance % (M2.3) | (On-time / Total) × 100 | 72% | Ticketing | Jan 2026 |
| Risk Score (M2.4) | (Criticality × Exploitability × Threat) / 10 | 6.5 | Risk platform | Jan 2026 |

[... Repeat para Indicadores 3-9 ...]

```

---

## SECCIÓN 2: FORMULAS EXCEL PREDEFINIDAS

### Fórmula IGM (Copiar en celda F7 para Indicador 1)

```excel
=ROUND(((C7*0.4)+(B7*20)+(D7*0.3)+(E7*0.1))*100/1,0)
```

**Donde:**
- C7 = PRAGMATIC Score (4.3 en Indicador 1)
- B7 = GQM Level converted to points (Nivel 3 = 20 puntos)
- D7 = Compliance % (80% en Indicador 1)
- E7 = Deployment % (60% en Indicador 1)

**Resultado:** IGM = 63 (Nivel 3-4: Definido/Gestionado)

### Fórmula ROI Year 1

```excel
=(SUM(G7:G15) - 1900000) / 1900000
```

**Donde:**
- G7:G15 = Beneficios por indicador (incident cost avoidance)
- 1,900,000 = Investment total

**Resultado:** ROI %= (2,000,000 - 1,900,000) / 1,900,000 = 5.3%

### Fórmula Payback Period (meses)

```excel
=ROUND(12 / ((G7:G15 / 12) / 1900000), 1)
```

**Resultado:** ~11 meses (REALISTIC scenario)

### Fórmula Portfolio IGM Avg

```excel
=AVERAGE(F7:F15)
```

---

## SECCIÓN 3: INSTRUCCIONES IMPLEMENTACIÓN

### Paso 1: Crear Estructura Base en Excel

1. Descargar template en blanco
2. Crear 5 hojas: Dashboard, Detalle, Costs, Trajectory, Raw Data
3. Copiar encabezados desde este documento

### Paso 2: Alimentar Datos Brutos

1. En hoja "Raw Data Input", entrar valores actuales para cada métrica
2. Utilizar timestamps SIEM, ticketing systems, audit reports como source of truth
3. Validar datos con stakeholders (CISO, CTO, Risk Head)

### Paso 3: Ejecutar Cálculos

1. Abrir hoja "Dashboard"
2. Fórmulas IGM (F7:F15) calcularán automáticamente
3. ROI (G7:G15) calcularán basados en Costs sheet
4. Payback period (H7:H15) calcularán automáticamente

### Paso 4: Actualizar Mensualmente

- Q1 2026: Baseline measurements
- Q2 2026: Re-assessment post Phase 2 implementation
- Q3-Q4 2026: Continuous tracking
- 2027: Advanced optimization tracking

---

**FIN DE PLANTILLA EXCEL**

