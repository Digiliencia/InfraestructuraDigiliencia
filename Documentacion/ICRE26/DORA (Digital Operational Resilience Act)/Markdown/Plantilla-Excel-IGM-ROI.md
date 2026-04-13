# PLANTILLA EXCEL: CÁLCULO DE IGM (ÍNDICE GESTIÓN MADUREZ) Y ROI
## Framework de Implementación y Análisis Financiero

**Versión:** 1.0  
**Fecha:** Enero 2026  
**Clasificación:** Profesional — Herramienta de Análisis Financiero  
**Formato:** Plantilla Excel con Fórmulas  

---

## INTRODUCCIÓN

Esta plantilla proporciona:

1. **Cálculo de IGM (Índice de Gestión de Madurez)** conforme escala DORA (1-5)
2. **Análisis de ROI (Return on Security Investment) / ROSI**
3. **Comparación costo-beneficio** de iniciativas de seguridad
4. **Payback period** y justificación presupuestaria
5. **Integración con score PRAGMATIC** de métricas

---

## PARTE 1: STRUCTURE DE LA PLANTILLA EXCEL

### Hoja 1: "Dashboard IGM"

**Propósito:** Vista consolidada del Índice de Gestión de Madurez DORA

```
┌─────────────────────────────────────────────────────────┐
│ DASHBOARD IGM - CYBERSECURITY MATURITY DORA 2026        │
├─────────────────────────────────────────────────────────┤
│                                                           │
│ Institución: [Nombre Banco]          Período: Q1 2026   │
│ Supervisor: [CRO/CISO]               Fecha: Enero 20    │
│                                                           │
├─────────────────────────────────────────────────────────┤
│ RESUMEN IGM CONSOLIDADO                                  │
├─────────────────────────────────────────────────────────┤
│ Pilar 1: Gobernanza                 Score: 3.2/5.0     │
│ Pilar 2: Gestión Riesgos            Score: 2.8/5.0     │
│ Pilar 3: Gestión Incidentes         Score: 3.5/5.0     │
│ Pilar 4: Resiliencia Operativa      Score: 2.9/5.0     │
│ Pilar 5: Gestión Terceros           Score: 2.6/5.0     │
│                                                           │
│ IGM PROMEDIO PONDERADO:             3.00/5.0 (MANAGED)  │
│                                                           │
│ Tendencia Q4 2025 → Q1 2026:        +0.15 (positiva)   │
│                                                           │
├─────────────────────────────────────────────────────────┤
│ ROADMAP PROYECTADO                                       │
├─────────────────────────────────────────────────────────┤
│ Objetivo Q3 2026:                   IGM ≥ 3.5 (MANAGED) │
│ Objetivo Q4 2026:                   IGM ≥ 3.8 (INTEGRATED)
│ Iniciativas prioritarias:            Fase 1 (Q1-Q2)     │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

**Columnas recomendadas:**

| Columna | Contenido | Ejemplo |
|---------|-----------|---------|
| A | Pilar DORA | Gobernanza; Riesgos; Incidentes; etc. |
| B | Indicador | MTTD; Patch Rate; Vendor Coverage |
| C | Score Actual | 3.2 (1-5 escala) |
| D | Score Target Q3 | 4.0 |
| E | Tendencia | ↑↓→ |
| F | Gap | -0.8 |
| G | Responsable | CISO; CRO |
| H | Status | On-track; At-risk; Delayed |

**Fórmula IGM Ponderado:**
```
IGM = (Gobernanza×0.25 + Riesgos×0.20 + Incidentes×0.25 + Resiliencia×0.20 + Terceros×0.10)
```

---

### Hoja 2: "Cálculo ROI / ROSI"

**Propósito:** Análisis financiero de inversiones seguridad

```
┌──────────────────────────────────────────────────────────────┐
│ CÁLCULO ROI / ROSI - INICIATIVAS SEGURIDAD 2025-2026        │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│ INICIATIVA 1: Implementación SIEM Enterprise                 │
│ ──────────────────────────────────────────────────────────   │
│                                                                │
│ COSTOS (2 años):                                              │
│   Setup/Implementation:        €80,000                        │
│   Software Licenses (2 años):  €120,000                       │
│   Staff (FTE analyst):          €200,000 (€50K/año × 2)      │
│   Training:                     €20,000                        │
│   ────────────────────────────────────────                   │
│   COSTO TOTAL:                €420,000                        │
│                                                                │
│ BENEFICIOS (2 años):                                          │
│   MTTD mejora:                 €150,000 avoided losses       │
│   Patch acceleration:          €200,000 avoided losses       │
│   Incident prevention:         €500,000 avoided losses       │
│   ────────────────────────────────────────                   │
│   BENEFICIO TOTAL:            €850,000                        │
│                                                                │
│ ROI / ROSI CALCULATION:                                       │
│   ROSI = (Beneficio - Costo) / Costo × 100%                 │
│   ROSI = (€850,000 - €420,000) / €420,000 × 100%            │
│   ROSI = €430,000 / €420,000 × 100%                         │
│   ROSI = 102.4% ← Return on Security Investment             │
│                                                                │
│ PAYBACK PERIOD:                                               │
│   = Costo Total / Beneficio Anual                            │
│   = €420,000 / €425,000 anual                                │
│   = 11.8 meses (justificable)                                │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

**Estructura detallada:**

| Sección | Elementos | Notas |
|---------|-----------|-------|
| **Costos** | Capital (hardware, licenses) <br> Operacional (staff, training) <br> Mantenimiento (annual) | Incluir 2-3 años visibilidad |
| **Beneficios** | Avoided breach costs <br> Reduced downtime <br> Efficiency gains <br> Compliance avoidance | Usar modelo ALE (Annualized Loss Expectancy) |
| **Métricas Clave** | ROSI (%) <br> Payback (months) <br> NPV (Net Present Value) <br> IRR (Internal Rate Return) | Calcular todos para visibilidad completa |

**Fórmulas clave:**

```
ALE (Annualized Loss Expectancy):
  ALE = SLE (Single Loss Expectancy) × ARO (Annual Rate Occurrence)
  Ejemplo: €500K breach × 0.2 annual prob = €100K ALE

ROSI (Return on Security Investment):
  ROSI = (ALE_before - ALE_after - Annual_Cost) / Annual_Cost × 100%
  Ejemplo: (€100K - €20K - €50K) / €50K = 60% ROSI

Payback Period (meses):
  Payback = Costo_Total_2años / (Beneficio_anual)
  Ejemplo: €420K / €210K anual = 2 años

NPV (Net Present Value, discount rate 10%):
  NPV = Σ[Beneficio_anual / (1+rate)^year] - Costo_inicial
```

---

### Hoja 3: "Estimación ALE por Incidente"

**Propósito:** Calcular Annual Loss Expectancy por tipo incidente

```
┌──────────────────────────────────────────────────────────────┐
│ ANNUALIZED LOSS EXPECTANCY (ALE) - INCIDENTE TIPOS           │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│ TIPO INCIDENTE: Ransomware Attack (Datos Cliente)           │
│ ──────────────────────────────────────────────────────────   │
│                                                                │
│ SLE (Single Loss Expectancy) Components:                      │
│   Direct Costs:                                               │
│     - Ransom payment (avg):              €500,000            │
│     - Recovery/IT costs:                 €300,000            │
│     - Incident response team:            €150,000            │
│   Indirect Costs:                                             │
│     - Downtime (€50K/hour × 24h):       €1,200,000           │
│     - Regulatory fines (GDPR 4%):        €2,000,000 (est)    │
│     - Reputational damage:               €1,500,000 (est)    │
│   ────────────────────────────────────                       │
│   SLE TOTAL:                            €5,650,000           │
│                                                                │
│ ARO (Annual Rate of Occurrence):                              │
│   Ransomware probability (financial):    0.15 (15% annual)   │
│   [Fuente: CyberEdge 2024: 80% atacados; financiero ~15%]   │
│                                                                │
│ ALE CALCULATION:                                              │
│   ALE = SLE × ARO                                             │
│   ALE = €5,650,000 × 0.15                                    │
│   ALE = €847,500 annual exposure                              │
│                                                                │
│ CONTROL MITIGATION:                                           │
│   SIEM + Detection:     Reduce ARO → 0.05 (67% reduction)    │
│   EDR + Response:       Reduce SLE → €2,500,000 (56% reduction)
│   ────────────────────────────────────                       │
│   NEW ALE = €2,500,000 × 0.05 = €125,000                    │
│                                                                │
│ ALE REDUCTION:                                                │
│   €847,500 - €125,000 = €722,500 annual benefit             │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

**Template para múltiples incidentes:**

| Tipo Incidente | SLE (€) | ARO (%) | ALE (€) | Mitigation | New ALE (€) | Reduction (€) |
|---|---|---|---|---|---|---|
| Ransomware | 5,650K | 15% | 847K | SIEM+EDR | 125K | 722K |
| Data Breach | 3,200K | 8% | 256K | Encryption | 45K | 211K |
| Phishing | 800K | 25% | 200K | Training | 80K | 120K |
| DDoS | 1,500K | 5% | 75K | CDN+WAF | 15K | 60K |
| Insider Threat | 2,100K | 3% | 63K | DLP | 20K | 43K |
| **TOTAL ALE** | — | — | **1,441K** | — | **285K** | **1,156K** |

---

### Hoja 4: "Roadmap de Inversión"

**Propósito:** Desglose presupuestario por fase de implementación

```
┌──────────────────────────────────────────────────────────────┐
│ ROADMAP DE INVERSIÓN - FASES 1-3 (2026)                      │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│ FASE 1 (Q1-Q2 2026): Score PRAGMATIC ≥ 4.5 [CRÍTICO]        │
│ ──────────────────────────────────────────────────────────   │
│ Iniciativa                      Costo    ROSI    Payback     │
│                                                                │
│ 1. Implementar SIEM             €150K    102%    11.8m       │
│ 2. Automated Incident Notif.    €50K     250%    2.8m        │
│ 3. Vulnerability Scanning       €60K     180%    5.1m        │
│ 4. TLPT (Red Team)              €200K    120%    18.2m       │
│ ────────────────────────────────────────────────────────    │
│ SUBTOTAL FASE 1:                €460K    138%    9.5m avg    │
│ Presupuesto Aprobado Q1:        €250K (Fase 1a)             │
│ Presupuesto Solicitado Q2:      €210K (Fase 1b)             │
│ ALE Reduction Q1-Q2:            €890K annual avoidance      │
│                                                                │
│ FASE 2 (Q2-Q3 2026): Score PRAGMATIC 4.0-4.5 [RECOMENDADO] │
│ ──────────────────────────────────────────────────────────   │
│ Iniciativa                      Costo    ROSI    Payback     │
│                                                                │
│ 1. Encryption Implementation    €120K    165%    8.6m        │
│ 2. BC/DR Testing Platform       €80K     140%    8.5m        │
│ 3. Phishing Simulation (annual) €50K     190%    3.1m        │
│ 4. TPRM Platform                €70K     155%    9.2m        │
│ ────────────────────────────────────────────────────────    │
│ SUBTOTAL FASE 2:                €320K    163%    7.4m avg    │
│ ALE Reduction Q2-Q3:            €520K annual avoidance      │
│                                                                │
│ FASE 3 (Q3-Q4 2026): Score PRAGMATIC 3.5-4.0 [DESEABLE]    │
│ ──────────────────────────────────────────────────────────   │
│ Iniciativa                      Costo    ROSI    Payback     │
│                                                                │
│ 1. Risk Quantification (FAIR)   €40K     200%    2.4m        │
│ 2. GRC Platform Enhancement     €60K     145%    8.3m        │
│ 3. Board Dashboard/Reporting    €30K     180%    2.0m        │
│ ────────────────────────────────────────────────────────    │
│ SUBTOTAL FASE 3:                €130K    175%    4.2m avg    │
│ ALE Reduction Q3-Q4:            €285K annual avoidance      │
│                                                                │
│ ────────────────────────────────────────────────────────    │
│ INVERSIÓN TOTAL 3 FASES:        €910K                        │
│ ALE REDUCTION TOTAL ANUAL:      €1,695K                      │
│ ROI PORTFOLIO 2 AÑOS:           186% (€1,910K net benefit)  │
│ PAYBACK PERIOD PORTFOLIO:       6.5 meses promedio           │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

**Detalles Matriz Presupuestaria:**

| Período | Iniciativa | Línea Presupuesto | Costo | Status | ALE Impact |
|---------|---|---|---|---|---|
| Q1 2026 | SIEM | Capital-IT | €150K | Approved | -€450K/año |
| Q1 2026 | Incident Automation | Operations | €50K | Approved | -€200K/año |
| Q2 2026 | Vulnerability | Operational | €60K | Proposed | -€240K/año |
| Q2 2026 | TLPT | Consulting | €200K | Proposed | -€300K/año |
| **Total Fase 1** | — | — | **€460K** | — | **-€1,190K/año** |

---

## PARTE 2: FÓRMULAS EXCEL ESPECÍFICAS

### Fórmula 1: Cálculo IGM por Pilar

```excel
=IFERROR(AVERAGE(Indicadores_Pilar_X), "N/A")
```

Ejemplo:
```excel
=AVERAGE(B2:B5)  ← Promedia 4 indicadores del Pilar Gobernanza
```

---

### Fórmula 2: IGM Ponderado

```excel
=Gobernanza*0.25 + Riesgos*0.20 + Incidentes*0.25 + Resiliencia*0.20 + Terceros*0.10
```

En Excel:
```excel
=B10*0.25 + B11*0.20 + B12*0.25 + B13*0.20 + B14*0.10
```

---

### Fórmula 3: ALE Calculation

```excel
=SLE * ARO
```

En Excel (con inputs):
```excel
=C2 * D2  ← SLE en C2, ARO (%) en D2
```

---

### Fórmula 4: ALE Reduction

```excel
=(ALE_Before - ALE_After)
```

En Excel:
```excel
=E2 - E3
```

---

### Fórmula 5: ROSI Calculation

```excel
=(Beneficio_Total - Costo_Total) / Costo_Total * 100
```

En Excel:
```excel
=(F2-C2)/C2*100
```

Interpretación:
- ROSI > 100% = Excelente (dinero recuperado + ganancia)
- ROSI 50-100% = Bueno (dinero recuperado + algo de ganancia)
- ROSI < 50% = Marginal (parcialmente recuperado)
- ROSI < 0% = No recomendable

---

### Fórmula 6: Payback Period

```excel
=Costo_Total / (Beneficio_Anual)
```

En Excel (resultado en años):
```excel
=C2 / (F2/2)  ← Si F2 es beneficio 2-años; divide por 2 para anual
```

O para meses:
```excel
=(C2 / (F2/2)) * 12
```

---

### Fórmula 7: NPV (Net Present Value)

```excel
=NPV(discount_rate, Year1_benefit, Year2_benefit, ...) - Initial_Cost
```

En Excel (discount rate 10%):
```excel
=NPV(0.10, C3:C5) - C2  ← C2 es costo inicial; C3:C5 son beneficios años 1-3
```

---

## PARTE 3: EJEMPLOS DE CÁLCULO COMPLETO

### Ejemplo 1: Iniciativa SIEM

**Inputs:**

| Parámetro | Valor |
|-----------|-------|
| Setup Costs | €80,000 |
| Annual Software | €60,000 (€30K/año × 2) |
| Staff (FTE Analyst) | €100,000 (€50K/año × 2) |
| Training | €20,000 |
| **COSTO TOTAL 2 AÑOS** | **€260,000** |

| Beneficio | Valor |
|-----------|-------|
| ALE Reduction (MTTD improve) | €450,000 (€225K/año) |
| Patch Acceleration Avoidance | €240,000 (€120K/año) |
| Incident Prevention | €300,000 (€150K/año) |
| **BENEFICIO TOTAL 2 AÑOS** | **€990,000** |

**Cálculos:**

```
ROSI = (€990,000 - €260,000) / €260,000 × 100%
     = €730,000 / €260,000 × 100%
     = 280.8% ← EXCELENTE

Payback = €260,000 / (€495,000 anual)
        = 0.525 años
        = 6.3 meses ← RÁPIDO
```

**Conclusión:** Invertir en SIEM es altamente recomendado; payback 6+ meses.

---

### Ejemplo 2: Iniciativa TLPT (Red Team Testing)

**Inputs:**

| Parámetro | Valor |
|-----------|-------|
| Red Team Engagement (bienal) | €200,000 |
| Follow-up Remediation | €100,000 |
| **COSTO TOTAL 2 AÑOS** | **€300,000** |

| Beneficio | Valor |
|-----------|-------|
| Prevented Critical Breach | €1,500,000 (65% prob × €2.3M avg breach) |
| Reduced Audit Findings | €150,000 |
| Improved Governance | €100,000 (intangible) |
| **BENEFICIO ESTIMADO** | **€1,750,000** |

**Cálculos:**

```
ROSI = (€1,750,000 - €300,000) / €300,000 × 100%
     = €1,450,000 / €300,000 × 100%
     = 483% ← EXCEPCIONAL

Payback = €300,000 / (€875,000 anual)
        = 0.343 años
        = 4.1 meses ← MUY RÁPIDO
```

**Conclusión:** TLPT tiene ROI excepcional; obligatorio para DORA compliance.

---

## PARTE 4: INTEGRACIÓN CON SCORE PRAGMATIC

**Cómo usar PRAGMATIC score en análisis ROI:**

```
IF Score_PRAGMATIC ≥ 4.5:
  → Métrica RECOMENDADA para inversión
  → Usa beneficios "high confidence"
  → Payback típico: <12 meses
  
IF Score_PRAGMATIC 3.5-4.5:
  → Métrica ACEPTABLE
  → Usa beneficios "medium confidence"
  → Payback típico: 12-24 meses
  
IF Score_PRAGMATIC < 3.5:
  → Métrica DÉBIL
  → No recomendada para inversión
  → Reemplazar con alternativa mejor
```

**Matriz de Decisión ROI × PRAGMATIC:**

| Score PRAGMATIC | ROSI Mínimo | Inversión | Status |
|---|---|---|---|
| ≥4.5 | 100%+ | OK | Implementar |
| 4.0-4.5 | 75%+ | Review | Implementar si ROSI >100% |
| 3.5-4.0 | 50%+ | Caution | Solo si ROSI >150% |
| <3.5 | N/A | Avoid | Reemplazar |

---

## USO PRÁCTICO

### Para Presentar a Junta Directiva:

1. ✓ Mostrar Hoja "Dashboard IGM"
2. ✓ Presentar ROI summary (ROSI %, Payback meses)
3. ✓ Usar Hoja "Roadmap Inversión" con timeline Q1-Q4
4. ✓ Destacar "ALE Reduction Anual" (€1.6M avoidance)

### Para CFO / Finance:

1. ✓ Foco en Payback Period (<12 meses ideal)
2. ✓ NPV calculation (5-year horizon)
3. ✓ Budget allocation by Fase (Approved/Requested)
4. ✓ Cash flow impact (setup vs operational costs)

### Para CISO / Operations:

1. ✓ Foco en Indicadores mejora (IGM trending +0.15)
2. ✓ Pilar-level scores (qué necesita atención)
3. ✓ Roadmap priorización (Fase 1 crítica)
4. ✓ Responsibility matrix (quién ejecuta qué)

---

**Fin de la Plantilla Excel**

*Enero 2026 — Herramienta de Análisis Financiero DORA*

