# PLANTILLA EXCEL: CÁLCULO DE IGM Y ROI

**Guía para Implementación de Spreadsheet de Medición y Análisis de Retorno**

**Versión**: 1.0  
**Fecha**: Enero 21, 2026  
**Formato**: Especificación Markdown para Excel/Google Sheets  
**Objetivo**: Automatizar cálculo de Índice de Gestión de Madurez (IGM) y ROI

---

## INTRODUCCIÓN

Este documento describe las fórmulas y estructura de una plantilla Excel para:

1. **IGM (Índice de Gestión de Madurez)**: Score BSIMM15 en escala 0-100
2. **ROI (Return on Investment)**: Retorno por inversión en cada iniciativa
3. **KPI Dashboard**: Seguimiento trimestral de progreso
4. **Comparativo**: Baseline vs. Target vs. Actual

---

## ESTRUCTURA DE HOJAS EXCEL

### Hoja 1: DATOS DE ENTRADA (Input Sheet)

#### Columna A-E: Actividades BSIMM15

```
| A: ID | B: Actividad | C: Práctica | D: PRAGMATIC | E: Status |
|-------|---|---|---|---|
| SM1.1 | Crear Estrategia | Strategy | 81 | Q1 |
| SM1.2 | Medir Éxito | Strategy | 88 | Q1 |
| SM1.4 | Checkpoints | Strategy | 89 | Q1 |
| PC2.2 | Policy Enforce | Process | 84 | Q1 |
| EM1.3 | Dashboard | Metrics | 84 | Q2 |
| CR1.4 | SAST Tools | Code Review | 91 | Q1 |
| CR1.5 | SCA | Code Review | 88 | Q2 |
| AA1.1 | Threat Model | Architecture | 81 | Q2 |
| CM1.1 | IR Interface | Compliance | 87 | Q1 |
| ST1.1 | DAST | Testing | 81 | Q2 |
| ST2.1 | Pentesting | Testing | 77 | Q3 |
| DM1.1 | Infra Auto | Deployment | 89 | Q1 |
| DM2.2 | SBOM Risk | Deployment | 76 | Q3 |
| ... | ... | ... | ... | ... |
```

#### Columna F-J: Scorecard de Implementación

```
| F: Baseline | G: Target | H: Actual | I: % Progress | J: Owner |
|---|---|---|---|---|
| 0 | 1 | 0 | 0% | John (CISO) |
| 0 | 1 | 1 | 100% | Maria (Dev) |
| 0 | 1 | 1 | 100% | Carlos (Ops) |
| 0 | 1 | 0 | 0% | Ana (Audit) |
| 0 | 1 | 0 | 0% | Luis (Metrics) |
| 0 | 1 | 1 | 100% | Maria (SAST) |
| 0 | 1 | 0 | 0% | Pedro (Supply Chain) |
| 0 | 1 | 0 | 0% | Sofia (Design) |
| 0 | 1 | 1 | 100% | Carlos (IR) |
| 0 | 1 | 0 | 0% | Miguel (Testing) |
| 0 | 1 | 0 | 0% | Miguel (Pentest) |
| 0 | 1 | 1 | 100% | Carlos (Infra) |
| 0 | 1 | 0 | 0% | Pedro (Supply) |
```

#### Columna K-O: Datos Financieros

```
| K: Cost Estimate | L: Actual Cost | M: Cost Status | N: Budget Variance | O: Notes |
|---|---|---|---|---|
| €5,000 | €4,800 | On-track | -4% | Internal effort |
| €3,000 | €3,200 | On-track | +7% | Tool license |
| €2,000 | €2,100 | On-track | +5% | Implementation |
| €1,500 | €0 | Not started | N/A | Pending |
| €2,500 | €0 | Not started | N/A | Q2 |
| €3,000 | €3,100 | On-track | +3% | SAST tuning |
| €20,000 | €0 | Not started | N/A | Q2 |
| €8,000 | €0 | Not started | N/A | Q2 |
| €4,000 | €4,200 | On-track | +5% | IR playbook |
| €5,000 | €0 | Not started | N/A | Q2 |
| €12,000 | €0 | Not started | N/A | Q3 |
| €8,000 | €8,500 | Over budget | +6% | IaC tools |
| €15,000 | €0 | Not started | N/A | Q3 |
```

---

### Hoja 2: IGM CALCULATION (Score Calculation)

#### Sección A: Cálculo por Dominio

```
DOMINIO: GOVERNANCE

| Actividad | ID | PRAGMATIC | Implementada (S/N) | Score |
|---|---|---|---|---|
| Strategy & Metrics | SM* | 85 (avg) | S (4/8) | 42.5 |
| Process Compliance | PC* | 82 (avg) | S (1/2) | 41 |
| Organization | O* | 80 (avg) | N (0/2) | 0 |
| Enforce Metrics | EM* | 81 (avg) | N (0/3) | 0 |
| **SUBTOTAL GOVERNANCE** | | | | **83.5 / 4 = 20.9 pts** |

DOMINIO: INTELLIGENCE

| Práctica | Score Actual | Score Target | Progress |
|---|---|---|---|
| Code Review (CR) | 28 | 29 | 97% |
| Architecture (AA) | 8 | 10 | 80% |
| Compliance (CM) | 9 | 10 | 90% |
| Secure Dev (SG) | 0 | 8 | 0% |
| **SUBTOTAL INTELLIGENCE** | **45** | **57** | **79%** |

DOMINIO: SSDL TOUCHPOINTS

| Práctica | Score Actual | Score Target | Progress |
|---|---|---|---|
| Security Testing | 8 | 15 | 53% |
| **SUBTOTAL TOUCHPOINTS** | **8** | **15** | **53%** |

DOMINIO: DEPLOYMENT

| Práctica | Score Actual | Score Target | Progress |
|---|---|---|---|
| Deployment Management | 10 | 18 | 56% |
| **SUBTOTAL DEPLOYMENT** | **10** | **18** | **56%** |

**GRAND TOTAL IGM**:
- **Baseline**: 56 puntos (L2)
- **Actual Q1**: 56 + 20.9 = **76.9 puntos** (L3)
- **Target 2026**: 70 puntos (L3)
- **Status**: On-track
```

#### Sección B: Escala de Madurez

```
| Score | Nivel | Descripción | Status |
|-------|-------|---|---|
| 0-20 | L0 | Inexistente | ❌ |
| 21-40 | L1 | Iniciado (ad-hoc) | ❌ |
| 41-60 | L2 | Establecido (documented) | ✅ Baseline |
| 61-80 | L3 | Operativo (measured) | ⚠️ Target |
| 81-95 | L4 | Gestionado (managed) | ⚠️ Aspiración |
| 96-100 | L5 | Optimizado (optimized) | ❌ |
```

#### Sección C: Comparativo Trimestral

```
| Trimestre | Score Baseline | Score Actual | Delta | % Progress | On-Track |
|---|---|---|---|---|---|
| Q0 (Baseline) | — | 56 | — | — | — |
| Q1 2026 | 56 | 71 | +15 | +27% | ✅ |
| Q2 2026 | 56 | 81 | +25 | +45% | ✅ |
| Q3 2026 | 56 | 88 | +32 | +57% | ⚠️ |
| Q4 2026 | 56 | 90+ | +34+ | +60%+ | ✅ |
| Target | — | 70 | +14 | +25% | ✅ |
```

---

### Hoja 3: ROI ANALYSIS (Return on Investment)

#### Sección A: Análisis por Iniciativa

```
INICIATIVA: CR1.4 SAST Tools Implementation

| Concepto | Valor | Fórmula |
|----------|-------|---------|
| **INVERSIÓN** | | |
| Herramientas (licencia anual) | €6,000 | Fixed cost |
| Implementación/Training | €2,000 | Internal hours |
| Integración CI/CD | €1,500 | External service |
| Maintenance anual | €1,500 | Support |
| **TOTAL INVERSIÓN ANUAL** | **€11,000** | Sum |

| Beneficio | Estimado | Cálculo |
|-----------|----------|---------|
| **BENEFICIOS** | | |
| Vulnerabilidades detectadas (evitadas en prod) | 45/año | 87.6% coverage × code volume |
| Costo típico breach por vuln no detectada | €50,000 | Industry average |
| Breach evitados (esperado) | 3/año | 45 vuln × 6.7% conversion |
| Costo breach evitado | €150,000/año | 3 breach × €50k |
| Costo remedición reducida | €30,000/año | Faster detection → lower cost |
| Downtime prevenido | €25,000/año | 2 incidents × €12.5k |
| **TOTAL BENEFICIOS ANUALES** | **€205,000** | Sum |

| Métrica | Valor |
|--------|-------|
| **ROI %** | **(205,000 - 11,000) / 11,000 × 100** = **1,864%** |
| **Payback Period** | **11,000 / (205,000 / 12)** = **0.65 meses** |
| **NPV (Net Present Value)** | €194,000 (Year 1) |
| **IRR (Internal Rate of Return)** | **1,864%** |
| **Status** | ✅ **EXCELENTE ROI** |
```

#### Sección B: Consolidado Multi-Iniciativas

```
ROADMAP CONSOLIDADO 2026

| Iniciativa | Q | Costo | Beneficio Anual | ROI | Payback |
|---|---|---|---|---|---|
| SAST Tools | Q1 | €11k | €205k | 1,864% | 0.6 m |
| Checkpoints | Q1 | €5k | €80k | 1,500% | 0.7 m |
| Dashboard | Q1 | €2k | €40k | 1,900% | 0.6 m |
| Infra Auto | Q1 | €8k | €95k | 1,087% | 1.0 m |
| **Q1 TOTAL** | | **€26k** | **€420k** | **1,515%** | **0.7 m** |
| FAIR | Q2 | €15k | €120k | 700% | 1.5 m |
| SCA | Q2 | €20k | €150k | 650% | 1.6 m |
| SOAR | Q2 | €30k | €200k | 567% | 1.8 m |
| **Q2 TOTAL** | | **€65k** | **€470k** | **623%** | **1.6 m** |
| Pentesting | Q3 | €12k | €90k | 650% | 1.6 m |
| SBOM | Q3 | €15k | €80k | 433% | 2.2 m |
| Red Team | Q3 | €50k | €150k | 200% | 4.0 m |
| **Q3 TOTAL** | | **€77k** | **€320k** | **315%** | **2.9 m** |
| **TOTAL 2026** | | **€168k** | **€1.21M** | **619%** | **3.3 m** |
| **TOTAL WITH BASELINE** | | **€258k** | **€1.21M** | **368%** | **2.5 m** |
```

#### Sección C: Análisis Sensibilidad (Scenarios)

```
ESCENARIO 1: OPTIMISTA (Beneficios +30%)

| Métrica | Baseline | Optimista |
|---------|----------|-----------|
| Total Inversión | €258k | €258k |
| Total Beneficios | €1.21M | €1.57M |
| ROI | 368% | 508% |
| Payback | 2.5 m | 1.9 m |

ESCENARIO 2: PESIMISTA (Beneficios -30%)

| Métrica | Baseline | Pesimista |
|---------|----------|-----------|
| Total Inversión | €258k | €258k |
| Total Beneficios | €1.21M | €0.85M |
| ROI | 368% | 229% |
| Payback | 2.5 m | 3.6 m |

ESCENARIO 3: CONSERVADOR (Beneficios -50%)

| Métrica | Baseline | Conservador |
|---------|----------|-----------|
| Total Inversión | €258k | €258k |
| Total Beneficios | €1.21M | €0.60M |
| ROI | 368% | 133% |
| Payback | 2.5 m | 5.2 m |

**CONCLUSIÓN**: Incluso en escenario pesimista, ROI > 100%
```

---

### Hoja 4: KPI DASHBOARD (Seguimiento)

#### Sección A: KPI Principales

```
TRIMESTRE: Q1 2026

| KPI | Baseline | Target Q1 | Actual Q1 | % Progress | On-Track | Variance |
|-----|----------|-----------|-----------|-----------|----------|----------|
| Score IGM | 56 | 71 | 71 | 100% | ✅ | 0 |
| MTTD Crítico (días) | 5 | 3 | 3 | 100% | ✅ | 0 |
| SAST Coverage % | 45% | 85% | 88% | 104% | ✅ | +3% |
| Apps Checkpoints % | 30% | 90% | 92% | 102% | ✅ | +2% |
| IR Playbook (S/N) | N | S | S | 100% | ✅ | — |
| Training Completion % | 48% | 75% | 72% | 96% | ✅ | -3% |
| NIS2 Readiness % | 45% | 60% | 62% | 103% | ✅ | +2% |
| Presupuesto Gastado | — | €26k | €24.5k | 94% | ✅ | -€1.5k |
| Budget Variance % | — | ±5% | -6% | — | ✅ | Within tolerance |
```

#### Sección B: Gráficos (Recomendaciones)

```
**Gráfico 1: IGM Trending (Línea)**
- Eje X: Trimestres (Q0, Q1, Q2, Q3, Q4)
- Eje Y: Score IGM (0-100)
- Series: Baseline (56), Target (70), Actual (56→71→81...)
- Tipo: Línea con puntos

**Gráfico 2: KPI Speedometer (Gauge)**
- Centro: 71/100 (IGM actual)
- Rango: 0-100
- Colores: Rojo (0-40), Amarillo (40-70), Verde (70-100)

**Gráfico 3: Presupuesto vs. Actual (Columnas)**
- Eje X: Trimestres (Q1, Q2, Q3, Q4)
- Eje Y: Euros (0-€100k)
- Series: Budget (azul), Actual (verde), Variance (naranja)

**Gráfico 4: Implementación Progress (Barra Horizontal)**
- Actividades por estado: Not Started, In Progress, Completed
- Colores: Rojo, Amarillo, Verde
- Porcentaje: X/Y completadas
```

---

### Hoja 5: FINANCIAL SUMMARY (Resumen Financiero)

#### Sección A: Budget Tracking

```
PRESUPUESTO ANUAL 2026

| Rubro | Q1 | Q2 | Q3 | Q4 | Total | Budget | Variance |
|-------|----|----|----|----|-------|--------|----------|
| Tools & Software | €12k | €25k | €35k | €10k | €82k | €85k | -€3k (-3%) |
| Consulting & Ext Services | €8k | €30k | €35k | €5k | €78k | €75k | +€3k (+4%) |
| Internal Resources | €6k | €15k | €25k | €15k | €61k | €60k | +€1k (+2%) |
| Training & Awareness | €2k | €5k | €8k | €10k | €25k | €25k | €0 (0%) |
| Contingency (10%) | €2k | €8k | €11k | €4k | €25k | €25k | €0 (0%) |
| **TOTAL** | **€26k** | **€70k** | **€77k** | **€37k** | **€258k** | **€258k** | **€0 (0%)** |
| **Burn Rate** | €26k | €96k | €173k | €210k | — | — | — |

**Status**: On budget, on time
```

#### Sección B: Retorno por Trimestre

```
| Trimestre | Inversión Incremental | Beneficios Estimados | ROI Trimestral | ROI Acumulado |
|-----------|----------------------|-------------------|----------------|---|
| Q1 | €26k | €420k | 1,515% | 1,515% |
| Q2 | €44k | €470k | 968% | 1,182% |
| Q3 | €77k | €320k | 315% | 720% |
| Q4 | €37k | €90k | 143% | 368% |
| **TOTAL** | **€258k** | **€1.21M** | — | **368%** |
```

---

### Hoja 6: ASSUMPTIONS & NOTES

```
SUPUESTOS CRÍTICOS

| Supuesto | Valor | Justificación | Risk |
|----------|-------|---|---|
| Vulnerabilidades detectadas/año | 45 | 87.6% SAST coverage × typical volume | Medium |
| Costo breach promedio | €50k | Industry standard Spain | Low |
| Breach conversion rate | 6.7% | 3 of 45 vuln not detected → breach | High |
| MTTD improvement | 5→3 días | Better tooling + training | Low |
| Team adoption rate | 85% | Training effectiveness | Medium |
| Tool implementation success | 90% | Vendor support + internal expertise | Low |
| Sustained benefits Year 2+ | 80% | Ongoing tool use, team retention | Medium |

SENSIBILIDAD CRÍTICA

- Si breach rate = 10% (no 6.7%): ROI sube a 550%
- Si breach rate = 3% (no 6.7%): ROI baja a 200%
- Si MTTD no mejora: ROI baja a 180%

RECOMENDACIÓN: Monitorear breach rate trimestral
```

---

## INSTRUCCIONES TÉCNICAS DE IMPLEMENTACIÓN

### Paso 1: Crear Hoja 1 (Input)

1. Copiar tabla actividades BSIMM15 (columnas A-E)
2. Agregar datos entrada (columnas F-O)
3. Usar validación de datos para Status (dropdown Q1/Q2/Q3/Q4)
4. Usar formato condicional: Status completado = verde

### Paso 2: Crear Hoja 2 (IGM)

1. Crear SUMIF para agrupar por práctica
2. Crear fórmula PRAGMATIC Score = SUMPRODUCT(implementadas × PRAGMATIC) / COUNT(actividades)
3. Gráfico línea: Baseline vs Target vs Actual
4. Actualizar automático desde Hoja 1

### Paso 3: Crear Hoja 3 (ROI)

1. Tabla costos: Fixed + Variable por iniciativa
2. Beneficios: Manual estimate × industry standard
3. ROI = (Beneficios - Costos) / Costos × 100
4. Tablas de sensibilidad: Formulas con IF para 3 escenarios

### Paso 4: Crear Hoja 4 (Dashboard)

1. KPI principales como formulas referencias a Hoja 2
2. Gráficos: 4 tipos como descrito
3. Actual updating from Hoja 1
4. Conditional formatting: Rojo < 50%, Amarillo 50-80%, Verde > 80%

### Paso 5: Vincular todo

1. Hoja 1 es "source of truth"
2. Hojas 2-5 usan referencias y formulas
3. Dashboard actualiza automático cuando se cambian datos entrada
4. Exportar gráficos para reportes trimestrales

---

## FÓRMULAS EXCEL CLAVE

### Fórmula 1: IGM Score

```
=SUMPRODUCT((Hoja1.F:F=1)*(Hoja1.D:D))/COUNTA(Hoja1.B:B)

Donde:
- Hoja1.F:F = Implementada (S/N) convertida a 1/0
- Hoja1.D:D = PRAGMATIC score
- COUNTA = # total actividades
Resultado: Score ponderado 0-100
```

### Fórmula 2: ROI %

```
=((Beneficios_Anuales - Costos_Anuales) / Costos_Anuales) * 100

Donde:
- Beneficios_Anuales = Sum(vulnerabilidades_detectadas × costo_breach)
- Costos_Anuales = Sum(inversión_herramientas + servicios + recursos)
Resultado: Porcentaje ROI
```

### Fórmula 3: Payback Period (meses)

```
=Costos_Totales / (Beneficios_Anuales / 12)

Donde:
- Beneficios_Anuales / 12 = Beneficios mensuales promedio
Resultado: Meses hasta recuperar inversión
```

### Fórmula 4: Progress %

```
=COUNTIF(Hoja1.H:H,1) / COUNTA(Hoja1.B:B) * 100

Donde:
- COUNTIF(...,1) = Actividades completadas
- COUNTA(...) = Total actividades
Resultado: Porcentaje avance
```

---

## EXPORTACIÓN Y REPORTING

### Generación de Reportes Trimestales

1. **Reporte Ejecutivo**: 
   - Screenshot de Dashboard (Hoja 4)
   - Tabla KPI (Hoja 4, Sección A)
   - Financial Summary (Hoja 5)

2. **Reporte Técnico**:
   - Tabla Implementación (Hoja 1, filtered for Q)
   - IGM Trending (Gráfico Hoja 2)
   - ROI Analysis (Hoja 3)

3. **Reporte Auditoría**:
   - Mapeo Normativo (documento separado)
   - Completitud % por dominio
   - Status de remedición

---

## CONCLUSIÓN

Esta plantilla Excel proporciona:

✅ **Automatización**: Cálculo IGM, ROI, KPIs en tiempo real  
✅ **Visibilidad**: Dashboard ejecutivo con gráficos  
✅ **Trazabilidad**: Conexión datos entrada → IGM → ROI  
✅ **Análisis**: Sensibilidad, escenarios, breakeven  
✅ **Reporting**: Exportación automática de reportes  

**Tiempo de setup**: 2-3 horas  
**Mantenimiento trimestral**: 30 min para actualizar datos entrada

---

**FIN DE LA PLANTILLA EXCEL**