# PLANTILLA EXCEL: CÁLCULO MADUREZ Y ROI - ENCUESTA CIBERSEGURIDAD ORGANIZACIONAL
## Implementación Step-by-Step para 7 Módulos

**Versión:** 1.0 | **Fecha:** Enero 2026  
**Contexto:** Encuesta Integral Ciberseguridad (Gobernanza, VM, SIEM, Acceso, Capacitación, IR, Estrategia)  
**Software:** Microsoft Excel / Google Sheets compatible

---

## INTRODUCCIÓN: ÍNDICE DE MADUREZ CIBERSEGURIDAD (IMC)

El IMC es métrica compuesta (0-100) que integra:

1. **Puntuación Promedio Módulos** (7 módulos, escala 0-100)
2. **Compliance Normativo** (NIS2, ISO, GDPR alignment %)
3. **Implementación Operacional** (% deployed vs target)
4. **Sostenibilidad** (recursos, presupuesto, governance)

**Fórmula IMC:**
```
IMC = (Promedio_Módulos × 0.50) + (Compliance%  × 0.30) + (Implementation% × 0.20)

Rango:
0-25: Inicial (Nivel 1)
26-50: Repetible (Nivel 2)
51-75: Definido (Nivel 3)
76-100: Gestionado/Optimizado (Nivel 4-5)
```

---

## ESTRUCTURA PLANTILLA EXCEL

### HOJA 1: Dashboard Ejecutivo

```
┌──────────────────────────────────────────────────────────┐
│ DASHBOARD MADUREZ CIBERSEGURIDAD - 7 MÓDULOS             │
├──────────────────────────────────────────────────────────┤

FILA 1-3: Metadatos
| Organización: [Editable] |
| Fecha Assessment: [DATE] |
| Período: [Q1 2026] |

FILA 5-6: Encabezados Principales

| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| Módulo | Score Actual (0-100) | Nivel GQM (0-5) | Compliance % | Implementation % | IMC Calculado | Estado | Prioridad |
|---|---|---|---|---|---|---|---|

FILA 7-13: Datos por Módulo

| 1. Gobernanza | [_] | [_] | [_] | [_] | [=FORMULA] | 🟢 | P1 |
| 2. Vulnerabilidades | [_] | [_] | [_] | [_] | [=FORMULA] | 🟢 | P1 |
| 3. SIEM | [_] | [_] | [_] | [_] | [=FORMULA] | 🟡 | P2 |
| 4. Acceso & Identidad | [_] | [_] | [_] | [_] | [=FORMULA] | 🟢 | P1 |
| 5. Capacitación | [_] | [_] | [_] | [_] | [=FORMULA] | 🟢 | P1 |
| 6. Respuesta Incidentes | [_] | [_] | [_] | [_] | [=FORMULA] | 🟡 | P2 |
| 7. Estrategia Integrada | [_] | [_] | [_] | [_] | [=FORMULA] | 🟡 | P3 |

FILA 15: Totales Consolidados

| PROMEDIO PORTFOLIO | [=AVERAGE(B7:B13)] | [=AVERAGE(C7:C13)] | [=AVERAGE(D7:D13)] | [=AVERAGE(E7:E13)] | [=FORMULA_IMC] | [STATUS] | [PRIORIDAD] |

FILA 17-20: Métricas Ejecutivas

| Métrica | Valor | Benchmark | Gap |
|---------|-------|-----------|-----|
| IMC Promedio | [45] | 40 (industry) | +5pp |
| Compliance Normativo | 72% | 80% (requerido) | -8pp CRÍTICO |
| Implementation Avg | 55% | 60% | -5pp |
| Regulatory Readiness | AMBER | GREEN target | 12 meses a goal |

FILA 22-24: Proyección Simplificada

| Período | IMC Proyectado | Nivel | Timeline |
|---------|---------------|-------|----------|
| Q1 2026 (Actual) | 45 | Nivel 2 | Today |
| Q4 2026 | 62 | Nivel 3 | 9 meses |
| Q1 2027 | 75 | Nivel 3-4 | 12 meses |
```

---

### HOJA 2-8: Detalle por Módulo (7 hojas, 1 por módulo)

**Ejemplo Módulo 1: Gobernanza**

```
┌──────────────────────────────────────────────┐
│ MÓDULO 1: GOBERNANZA Y LIDERAZGO             │
├──────────────────────────────────────────────┤

FILA 1-4: Metadata

| Nombre | Gobernanza y Liderazgo Ciberseguridad |
| # Preguntas | 5 (1.1-1.5) |
| Score Actual | [_] / 100 |
| Plazo Crítico | Agosto 2026 (NIS2) |

FILA 6-12: Preguntas Detalladas

| Pregunta | Respuesta Usuario | Puntos | Normativa Clave | Validación |
|----------|-----------------|--------|-----------------|-----------|
| 1.1: Estado CISO | Nivel 3 (COO reporting) | 50 | NIS2 Art.17 | ✓ |
| 1.2: Revisión Estrategia | Trimestral | 40 | NIS2 Art.17 | ✓ |
| 1.3: Política Documentada | Sí, comunicada | 50 | NIS2 Art.17 | ✓ |
| 1.4: Presupuesto Alineado | Risk-mapped | 45 | NIS2 Art.17 | ⚠ |
| 1.5: % IT Budget | 5% | 35 | Plan Nacional | ⚠ |

FILA 14-16: Score Agregado

| Promedio Módulo | (50+40+50+45+35)/5 = | 44 puntos | Nivel 2-3 |
| Compliance vs NIS2 | 5/5 alineados | 100% | ✓ |
| Implementation % | 4/5 operacional | 80% | ✓ |

FILA 18-20: Insights & Recomendaciones

| Fortaleza | CISO governance structure established (reporta COO) |
| Gap | Budget allocation 5% vs target 8%; need €500K additional |
| Acción | Presupuesto increase negotiation Q1 2026 |
| Timeline | Complete by Q2 2026 |
| Owner | CISO + CFO |

[Repetir estructura para Módulos 2-7]
```

---

### HOJA 9: Costs & ROI Analysis

```
┌──────────────────────────────────────────────┐
│ COSTS & ROI - YEAR 1 INVESTMENT              │
├──────────────────────────────────────────────┘

FILA 1-3: Resumen Ejecutivo

| Inversión Total Year 1 | €2.1M |
| ROI Esperado | 35-60% |
| Payback Period | 18-24 meses |

FILA 5-30: Desglose Presupuesto por Módulo

| Módulo | Elemento | Tipo | Costo Year 1 | Beneficio Anual |
|--------|----------|------|-------------|-----------------|
| **1. Gobernanza** | Governance restructuring | OpEx | €50K | €200K (efficiency) |
| | Board training | Training | €30K | €100K (visibility) |
| **2. Vulnerabilidades** | Scanning tools upgrade | CapEx | €120K | €400K (breach prevention) |
| | VM analyst (1 FTE) | OpEx | €75K | €300K (faster remediation) |
| | Automated patching | CapEx | €150K | €600K (downtime reduction) |
| **3. SIEM** | SIEM license + infra | CapEx/OpEx | €200K | €500K (detection capability) |
| | SOC analyst (1 FTE) | OpEx | €75K | €300K (coverage 24/7) |
| **4. Acceso** | Identity platform | CapEx | €180K | €250K (breach reduction) |
| | MFA rollout | CapEx | €60K | €150K (unauthorized access ↓) |
| **5. Capacitación** | LMS upgrade | CapEx | €40K | €100K (culture) |
| | Training programs | OpEx | €80K | €250K (incident reduction) |
| **6. IR** | SOAR platform | CapEx | €150K | €800K (MTTR reduction) |
| | IR team (0.5 FTE) | OpEx | €50K | €300K (faster response) |
| **7. Estrategia** | Governance consultant | OpEx | €100K | €200K (roadmap clarity) |
| | Risk assessment | OpEx | €60K | €150K (prioritization) |
| | **TOTAL** | | **€1,320K** | **€4,500K** |

FILA 32-40: ROI Scenarios

| Scenario | Investment | Benefits | Net Year 1 | Payback | 3-Year ROI |
|----------|-----------|----------|-----------|---------|-----------|
| **Conservative** | €1.32M | €2M (1 incident prevented) | +€680K | 8 meses | 180% |
| **Realistic** | €1.32M | €3M (2 incidents + efficiency) | +€1.68M | 5 meses | 280% |
| **Optimistic** | €1.32M | €4.5M (3 incidents + culture) | +€3.18M | 4 meses | 400% |

FILA 42-45: Sensitivity Analysis

| Variable | -20% | Base | +20% | Impact on ROI |
|----------|------|------|------|---------------|
| Incident Cost | €400K | €500K | €600K | -€50K / +€50K |
| Incidents Prevented | 1 | 2 | 3 | -€500K / +€500K |
| Implementation Timeline | 15 mo | 12 mo | 9 mo | -€200K / +€200K |

FILA 47-50: Risk Factors

| Risk | Probability | Impact | Mitigation |
|------|-----------|--------|-----------|
| Delayed vendor delivery | 30% | 2-3 mo slip | Engage vendors early |
| Staff turnover | 20% | Loss momentum | Cross-training |
| Scope creep | 40% | 20% budget overrun | Strict change control |
```

---

### HOJA 10: Maturity Trajectory (18-36 meses)

```
┌──────────────────────────────────────────────┐
│ TRAJECTORY PROYECCIÓN - 18-36 MESES         │
├──────────────────────────────────────────────┘

FILA 1-3: Timeline Overview

| Fase | Período | Módulos Foco | Target IMC | Investment |
|------|---------|-------------|-----------|-----------|
| 1 - Foundation | Q1 2026 | 1,7 (Governance base) | 50 | €0 (internal) |
| 2 - Core Operations | Q2-Q3 2026 | 2,3,4,5 (technical) | 65 | €1.2M |
| 3 - Optimization | Q4 2026 | 1-7 all (integration) | 75 | €200K |
| 4 - Advanced | 2027 | All (automation, AI) | 85+ | €500K |

FILA 5-15: Quarter-by-Quarter Projection

| Módulo | Q4 2025 | Q1 2026 | Q2 2026 | Q3 2026 | Q4 2026 | Q1 2027 |
|--------|---------|---------|---------|---------|---------|---------|
| 1. Gobernanza | 40 | 50 | 60 | 70 | 80 | 85 |
| 2. Vulnerabilidades | 35 | 40 | 55 | 70 | 75 | 80 |
| 3. SIEM | 30 | 35 | 50 | 65 | 75 | 80 |
| 4. Acceso | 45 | 55 | 65 | 75 | 80 | 85 |
| 5. Capacitación | 50 | 60 | 70 | 75 | 80 | 82 |
| 6. Respuesta Incidentes | 40 | 50 | 60 | 72 | 80 | 85 |
| 7. Estrategia | 35 | 45 | 55 | 65 | 75 | 80 |
| **PORTFOLIO AVG** | **39** | **48** | **60** | **70** | **78** | **83** |
| **IMC PROYECTADO** | **39** | **48** | **60** | **70** | **78** | **83** |

FILA 17-20: Hitos Clave

| Fecha | Hito | Indicador Éxito | Responsable |
|-------|------|-----------------|-----------|
| 31-Mar-2026 | Governance foundation complete | CISO reporting to CEO | CISO |
| 30-Jun-2026 | Core operations Phase 2 complete | MTTD <48h; MTTR <20d | CTO |
| 31-Aug-2026 | NIS2 compliance achieved | 95%+ vs requirements | Compliance |
| 31-Dec-2026 | Portfolio IMC >75 | Level 3-4 operacional | Executive Team |

FILA 22-25: Success Metrics 2026

| Métrica | Baseline | Target 2026 | Progress Indicator |
|---------|----------|-----------|------------------|
| IMC Global | 39 | 78 | 2pp/month trend |
| NIS2 Readiness | 72% | 95%+ | Gap closure % |
| Compliance Avg | 65% | 85%+ | All 7 modules |
| Implementation Avg | 50% | 85%+ | Deployed systems |
```

---

### HOJA 11: Raw Data Input

```
┌──────────────────────────────────────────────┐
│ RAW DATA ENTRY - MONTHLY UPDATE SHEET        │
├──────────────────────────────────────────────┘

Instrucciones: Actualizar mensualmente con datos más recientes de operaciones

FILA 1-5: Metadata

| Parameter | Value |
|-----------|-------|
| Organization | [ORG NAME] |
| Data Collection Date | [DATE] |
| Data Owner | [ROLE] |
| Next Review | [DATE + 30d] |

FILA 7-50: Respuestas Preguntas por Módulo

## MÓDULO 1: GOBERNANZA (Preguntas 1.1-1.5)

| Pregunta | Respuesta (0-5 or %) | Data Source | Validación | Notas |
|----------|-------------------|------------|-----------|-------|
| 1.1: Estado CISO | 3 (COO reporting) | Org chart | ✓ | Formal since Jan 2026 |
| 1.2: Revisión Estrategia | Trimestral | Board minutes | ✓ | Last: Dec 2025 |
| 1.3: Política Documentada | Sí, 90% distributed | LMS / Email tracking | ⚠ | Pending Q1 refresh |
| 1.4: Presupuesto Alineado | Risk-mapped 5 áreas | Budget spreadsheet | ✓ | Need formalization |
| 1.5: IT Budget % | 5% | Financial systems | ✓ | Target: 8% by Q4 |

## MÓDULO 2: VULNERABILIDADES (Preguntas 2.1-2.9)

| Pregunta | Respuesta | Data Source | Validación | Notas |
|----------|----------|------------|-----------|-------|
| 2.1: VM Maturity | Nivel 2-3 | Assessment | ✓ | Scanning quarterly, need continuous |
| 2.2: % SLA Compliance | 72% | Ticketing system | ✓ | 15 day SLA for critical |
| 2.3: Threat Intel | Partial correlation | Analyst notes | ⚠ | No formal integration |
| 2.4: Pen Test Frequency | Annual | Audit reports | ✓ | Last: Q4 2025 |
| 2.5: PT Methodology | OWASP-based | Assessment docs | ✓ | Professional firm |
| 2.6: MTTR Critical | 22 días | VM system | ✓ | Target <15 days |
| 2.7: Retest Validation | 85% critical | Testing records | ✓ | Improving |
| 2.8: % Apps Tested | 60% | VM reports | ⚠ | Need 80%+ |
| 2.9: Test Scope | 7/8 elements | Scope document | ✓ | Missing: OT/industrial |

[Repetir estructura para Módulos 3-7]
```

---

## FÓRMULAS EXCEL PREDEFINIDAS

### Fórmula IMC (Celda F15 Dashboard)

```excel
=ROUND((AVERAGE(B7:B13)*0.50)+(AVERAGE(D7:D13)*0.30)+(AVERAGE(E7:E13)*0.20),0)
```

**Componentes:**
- B7:B13 = Score promedio módulos (0-100)
- D7:D13 = Compliance % promedio
- E7:E13 = Implementation % promedio
- Pesos: 50% operacional + 30% compliance + 20% deployment

### Fórmula ROI Realistic (Hoja Costs)

```excel
=((Investment * Expected_Benefit_Multiple) - Investment) / Investment * 100
```

Ejemplo: (€1.32M × 2.27) - €1.32M / €1.32M = 127% ROI Year 1

### Fórmula Payback Period (Meses)

```excel
=ROUND(12 / ((Annual_Benefit / 12) / Investment),1)
```

Ejemplo: 12 / ((€3M/12) / €1.32M) = 5.3 meses

---

## INSTRUCCIONES IMPLEMENTACIÓN

### Paso 1: Crear estructura (1 hora)

1. Descargar template vacío
2. Renombrar hojas: Dashboard, Mod1-7, Costs, Trajectory, RawData
3. Copiar encabezados desde este documento

### Paso 2: Alimentar datos (2 semanas)

1. En "RawData" sheet, entrar respuestas preguntas encuesta (51 items)
2. Fuentes: SIEM, ticketing, audit reports, surveys
3. Validar con stakeholders (CISO, CTO, Risk)

### Paso 3: Ejecutar cálculos (1 hora)

1. Dashboard sheet calcula automáticamente IMC
2. Trajectory proyecta forward 18 meses
3. ROI scenarios muestran financial impact

### Paso 4: Actualizar mensualmente (2 horas/month)

- Q1 2026: Baseline measurements
- Q2-Q4 2026: Monthly data refresh
- 2027: Quarterly rollups

---

**FIN DE PLANTILLA EXCEL**

