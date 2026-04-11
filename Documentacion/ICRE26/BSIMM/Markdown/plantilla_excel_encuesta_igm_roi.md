# (e) PLANTILLA EXCEL: CÁLCULO DE IGM Y ROI PARA ENCUESTA

**Guía Completa para Implementación de Spreadsheet Automático**

**Versión**: 1.0  
**Fecha**: Enero 21, 2026  
**Alcance**: 68 preguntas, 8 módulos, análisis financiero  
**Objetivo**: Automatizar IGM (Índice de Gestión de Madurez) y ROI

---

## ARQUITECTURA GENERAL

### 6 Hojas Excel Especificadas

```
Hoja 1: INPUT DATA (Respuestas encuesta 68 preguntas)
Hoja 2: IGM CALCULATION (Cálculo automático índice madurez)
Hoja 3: ROI ANALYSIS (Análisis retorno inversión)
Hoja 4: KPI DASHBOARD (Seguimiento trimestral)
Hoja 5: FINANCIAL SUMMARY (Presupuesto vs. actual)
Hoja 6: ASSUMPTIONS & NOTES (Supuestos y cálculos)
```

---

## HOJA 1: INPUT DATA

### Estructura de Columnas

```
| A: ID | B: Pregunta | C: Sección | D: Peso | E: Respuesta | F: Owner |
|-------|---|---|---|---|---|
| P1.1 | ¿Política formal SSI? | Gobernanza | 15% | SÍ | CISO |
| P1.2 | ¿Roles definidos? | Gobernanza | 15% | SÍ | CISO |
| P1.3 | ¿Revisión anual? | Gobernanza | 10% | PARCIAL | CISO |
| P1.4 | ¿Comité SSI? | Gobernanza | 15% | NO | CTO |
| ... | ... | ... | ... | ... | ... |
```

### Validación de Datos

- **Respuesta**: Dropdown [SÍ / PARCIAL / NO / N/A]
- **Valores numéricos**: SÍ=1, PARCIAL=0.5, NO=0, N/A=omitir

### Ejemplo de 10 preguntas (primeras)

```
P1.1, Política formal, Gobernanza, 0.15, SÍ, CISO
P1.2, Roles definidos, Gobernanza, 0.15, SÍ, CISO
P1.3, Revisión anual, Gobernanza, 0.10, PARCIAL, CISO
P1.4, Comité SSI, Gobernanza, 0.15, NO, CTO
P1.5, Mapeo normativo, Gobernanza, 0.10, SÍ, CISO
P2.1, Inventario activos, Activos, 0.15, SÍ, CTO
P2.2, Clasificación criticidad, Activos, 0.10, PARCIAL, CTO
P2.3, Owner asignado, Activos, 0.10, SÍ, CTO
P2.4, Monitoreo cambios, Activos, 0.08, PARCIAL, SOC
P2.5, Auditoría acceso, Activos, 0.12, NO, SOC
```

---

## HOJA 2: IGM CALCULATION

### Sección A: Cálculo por Sección

```
SECCIÓN 1: GOBERNANZA

| Pregunta | Respuesta (0-1) | Peso | Puntuación Ponderada |
|----------|---|---|---|
| P1.1 | 1 | 0.15 | 0.15 |
| P1.2 | 1 | 0.15 | 0.15 |
| P1.3 | 0.5 | 0.10 | 0.05 |
| P1.4 | 0 | 0.15 | 0 |
| P1.5 | 1 | 0.10 | 0.10 |

SUBTOTAL GOBERNANZA = (0.15+0.15+0.05+0+0.10) / (0.15+0.15+0.10+0.15+0.10) = 0.45 / 0.65 = **69.2%**
```

**Fórmula Excel**:
```
=SUMPRODUCT(Respuesta_Col × Peso_Col) / SUM(Peso_Col) × 100
```

### Sección B: IGM Total

```
| Sección | Score % | Peso | Contribución |
|---------|---|---|---|
| 1. Gobernanza | 69.2 | 15% | 10.4 |
| 2. Activos | 75.3 | 10% | 7.5 |
| 3. Vulnerabilidades | 62.1 | 15% | 9.3 |
| 4. Testing | 55.0 | 10% | 5.5 |
| 5. SIEM | 48.7 | 15% | 7.3 |
| 6. Respuesta Incidentes | 71.4 | 15% | 10.7 |
| 7. Capacitación | 58.3 | 10% | 5.8 |
| 8. Supply Chain | 42.9 | 10% | 4.3 |

**IGM TOTAL = SUM(Contribución) = 60.8 / 100 (L3 Operativo)**
```

### Sección C: Escala de Madurez

```
| Rango IGM | Nivel | Descripción | Status |
|-----------|-------|---|---|
| 0-20 | L0 | Inexistente | ❌ Crítico |
| 21-40 | L1 | Ad-hoc | ❌ Riesgo alto |
| 41-60 | L2 | Documentado | ⚠️ Cumplimiento básico |
| 61-80 | L3 | Operativo | ✅ Compliant NIS2 |
| 81-95 | L4 | Gestionado | ✅ Excelencia |
| 96-100 | L5 | Optimizado | ✅ Best-in-class |

RESULTADO: Score 60.8 = L3 (Operativo, Cumpliant NIS2)
```

### Sección D: Comparativo Trimestral

```
| Trimestre | Score | Delta | % Mejora | Status |
|-----------|-------|-------|----------|--------|
| Q0 Baseline | 45.2 | — | — | — |
| Q1 | 60.8 | +15.6 | +34.5% | ✅ On-track |
| Q2 Target | 70 | +24.8 | +54.9% | ✅ On-track |
| Q3 Target | 80 | +34.8 | +77% | ⏳ En progreso |
| Q4 Target | 90+ | +44.8+ | +99%+ | 🎯 Meta |

Fórmula: =IGM_Actual - IGM_Baseline
```

---

## HOJA 3: ROI ANALYSIS

### Sección A: Beneficios por Iniciativa

```
INICIATIVA: Implementar SAST Tools + Checkpoints CI/CD

COSTOS:
| Concepto | Monto |
|----------|-------|
| Licencias SAST | €6,000/año |
| Implementación CI/CD | €2,000 |
| Training equipo | €1,500 |
| Mantenimiento | €1,500 |
| TOTAL INVERSIÓN | **€11,000** |

BENEFICIOS:
| Beneficio | Cantidad | Valor Unitario | Total |
|-----------|----------|---|---|
| Vulnerabilidades detectadas (vs 0) | 45/año | - | - |
| Breach evitados (prev antes prod) | 3/año | €50,000 | €150,000 |
| Remedición más rápida | -60% MTTR | €30k ahorrados | €30,000 |
| Downtime prevenido | 2 incidentes | €12,500 | €25,000 |
| TOTAL BENEFICIOS ANUALES | | | **€205,000** |

ROI = (205,000 - 11,000) / 11,000 × 100 = **1,863%**
Payback Period = 11,000 / (205,000/12) = **0.64 meses**
```

### Sección B: Consolidado 2026

```
| Trimestre | Iniciativa | Costo | Beneficio | ROI | Payback |
|-----------|---|---|---|---|---|
| Q1 | SAST + Checkpoints | €11k | €205k | 1,863% | 0.6m |
| Q1 | SIEM Setup | €8k | €95k | 1,087% | 1.0m |
| Q1 | Dashboard Exec | €2k | €40k | 1,900% | 0.6m |
| Q1 | IR Playbook | €4k | €50k | 1,150% | 0.9m |
| **Q1 TOTAL** | | **€25k** | **€390k** | **1,460%** | **0.7m** |
| Q2 | FAIR Framework | €15k | €120k | 700% | 1.5m |
| Q2 | SCA Implementation | €20k | €150k | 650% | 1.6m |
| Q2 | Pentesting Program | €12k | €90k | 650% | 1.6m |
| **Q2 TOTAL** | | **€47k** | **€360k** | **665%** | **1.5m** |
| Q3 | SOAR Integration | €30k | €200k | 567% | 1.8m |
| Q3 | Red Team Exercise | €25k | €120k | 380% | 2.5m |
| **Q3 TOTAL** | | **€55k** | **€320k** | **482%** | **2.1m** |
| Q4 | Automation + Optimization | €20k | €80k | 300% | 3.0m |
| **Q4 TOTAL** | | **€20k** | **€80k** | **300%** | **3.0m** |
| **2026 TOTAL** | | **€147k** | **€1.15M** | **682%** | **1.5m** |
```

### Sección C: Análisis Sensibilidad

```
ESCENARIO 1: OPTIMISTA (+30% beneficios)

| Métrica | Baseline | Optimista |
|---------|----------|-----------|
| Beneficios 2026 | €1.15M | €1.49M |
| Costos 2026 | €147k | €147k |
| ROI | 682% | 912% |
| Payback | 1.5m | 1.2m |

ESCENARIO 2: PESIMISTA (-30% beneficios)

| Métrica | Baseline | Pesimista |
|---------|----------|-----------|
| Beneficios 2026 | €1.15M | €0.81M |
| Costos 2026 | €147k | €147k |
| ROI | 682% | 451% |
| Payback | 1.5m | 2.2m |

ESCENARIO 3: CONSERVADOR (-50% beneficios)

| Métrica | Baseline | Conservador |
|---------|----------|---|
| Beneficios 2026 | €1.15M | €0.58M |
| Costos 2026 | €147k | €147k |
| ROI | 682% | 294% |
| Payback | 1.5m | 3.0m |

CONCLUSIÓN: Incluso en escenario conservador, ROI >200%
```

---

## HOJA 4: KPI DASHBOARD

### Sección A: KPI Principales

```
TRIMESTRE: Q1 2026 (Real vs Target)

| KPI | Baseline | Target Q1 | Actual Q1 | % Progress | Status |
|-----|----------|-----------|-----------|-----------|--------|
| IGM Score | 45.2 | 60 | 60.8 | 102% | ✅ |
| MTTD (días) | 5 | 3 | 2.8 | 107% | ✅ |
| Vulnerabilidades resueltas % | 60% | 85% | 88% | 104% | ✅ |
| SAST Coverage % | 45% | 85% | 88% | 104% | ✅ |
| Apps bajo control % | 30% | 80% | 82% | 103% | ✅ |
| Training Completion % | 48% | 75% | 72% | 96% | ⚠️ |
| Presupuesto utilizado | — | €25k | €23.5k | 94% | ✅ |
| NIS2 Readiness % | 45% | 65% | 62% | 95% | ✅ |
```

### Sección B: Gráficos Recomendados

```
1. IGM TRENDING (Línea)
   - Eje X: Trimestres (Q0, Q1, Q2, Q3, Q4)
   - Eje Y: IGM Score (0-100)
   - Series: Baseline, Target, Actual
   - Tipo: Línea con marcadores

2. KPI SPEEDOMETER (Gauge)
   - Centro: 60.8
   - Rango: 0-100
   - Colores: Rojo (0-40), Amarillo (40-70), Verde (70-100)

3. PRESUPUESTO vs ACTUAL (Columnas)
   - Eje X: Trimestres (Q1, Q2, Q3, Q4)
   - Eje Y: Euros (0-€50k)
   - Series: Budget (azul), Actual (verde)

4. IMPLEMENTACIÓN PROGRESS (Barras Apiladas)
   - Not Started (rojo), In Progress (amarillo), Completed (verde)
   - Total: 8 módulos / 68 preguntas

5. SECCIONES POR MADUREZ (Radar)
   - Ejes: 8 secciones (Gobernanza, Activos, Vuln, etc.)
   - Rango: 0-100 por sección
```

---

## HOJA 5: FINANCIAL SUMMARY

### Sección A: Budget Tracking

```
PRESUPUESTO ANUAL 2026

| Rubro | Q1 | Q2 | Q3 | Q4 | Total | Budget | Variance |
|-------|----|----|----|----|-------|--------|----------|
| Herramientas Software | €8k | €10k | €12k | €5k | €35k | €35k | €0 (0%) |
| Servicios Externos | €10k | €20k | €25k | €10k | €65k | €65k | €0 (0%) |
| Recursos Internos | €5k | €10k | €15k | €8k | €38k | €40k | -€2k (-5%) |
| Training & Awareness | €2k | €3k | €2k | €3k | €10k | €10k | €0 (0%) |
| Contingency (10%) | €3k | €4k | €6k | €3k | €16k | €16k | €0 (0%) |
| **TOTAL** | **€28k** | **€47k** | **€60k** | **€29k** | **€164k** | **€166k** | **-€2k (-1%)** |
| **Burn Rate Acumulado** | €28k | €75k | €135k | €164k | — | — | — |
```

### Sección B: Retorno por Trimestre

```
| Trimestre | Inversión | Beneficios | ROI % | ROI Acumulado |
|-----------|-----------|-----------|-------|---|
| Q1 | €28k | €390k | 1,293% | 1,293% |
| Q2 | €47k | €360k | 666% | 906% |
| Q3 | €60k | €320k | 433% | 712% |
| Q4 | €29k | €80k | 176% | 682% |
| **TOTAL 2026** | **€164k** | **€1.15M** | — | **682%** |

Fórmula: =(Beneficios_Q - Inversión_Q) / Inversión_Q × 100
```

---

## HOJA 6: ASSUMPTIONS & NOTES

### Supuestos Críticos

```
| Supuesto | Valor | Justificación | Risk |
|----------|-------|---|---|
| Vulnerabilidades detectadas/año | 45 | SAST coverage típica × volumen código | Medio |
| Costo promedio breach España | €50k | Benchmark ENISA 2025 | Bajo |
| Conversion rate vulnerabilidades a breach | 6.7% | 3 de 45 no detectadas | Alto |
| MTTD improvement | 5d → 3d | SIEM + SOC training | Bajo |
| Adoption rate equipo | 85% | Resistencia al cambio típica 15% | Medio |
| Éxito herramientas | 90% | Vendor support + competencia interna | Bajo |
| Beneficios sostenibles Y2+ | 80% | Rotación equipo + fatiga | Medio |

SENSIBILIDAD CRÍTICA:
- Si conversion rate = 10%: ROI sube a 850%
- Si conversion rate = 3%: ROI baja a 450%
- Si MTTD no mejora: ROI baja a 350%

RECOMENDACIÓN: Monitorear conversion rate de vulnerabilidades a breach trimestral
```

---

## INSTRUCCIONES IMPLEMENTACIÓN TÉCNICA

### Paso 1: Crear Hoja 1 (Input)

1. Copiar estructura tabla (A-F) para 68 preguntas
2. Usar validación datos: Dropdown [SÍ/PARCIAL/NO/N/A]
3. Aplicar formato condicional: SÍ=verde, PARCIAL=amarillo, NO=rojo
4. Congelar header (fila 1)

### Paso 2: Crear Hoja 2 (IGM)

1. Usar SUMPRODUCT para cálculo por sección
2. Fórmula: =SUMPRODUCT(Respuesta × Peso) / SUM(Peso) × 100
3. Crear tabla resumen IGM total
4. Gráfico línea: Baseline vs Target vs Actual
5. Configurar refresh automático desde Hoja 1

### Paso 3: Crear Hoja 3 (ROI)

1. Tabla costos: Fixed + Variable por iniciativa
2. Beneficios: Manual estimate × benchmark
3. ROI = (Beneficios - Costos) / Costos × 100
4. Sensibilidad: 3 escenarios (optimista/base/pesimista)

### Paso 4: Crear Hoja 4 (Dashboard)

1. KPIs principales como formulas références a Hoja 2
2. 5 gráficos: Trending, Speedometer, Budget, Progress, Radar
3. Actualización automática desde Hoja 1
4. Conditional formatting: Rojo <50%, Amarillo 50-80%, Verde >80%

### Paso 5: Vincular todo

1. Hoja 1 es "source of truth"
2. Hojas 2-5 usan referencias y formulas
3. Dashboard actualiza automático cuando cambian datos entrada
4. Exportar gráficos para reportes trimestrales

---

## FÓRMULAS EXCEL CLAVE

### Fórmula 1: IGM Score

```
=SUMPRODUCT((Hoja1.E:E=1)*(Hoja1.D:D))/COUNTA(Hoja1.B:B)*100

Donde:
- Hoja1.E:E = Respuesta convertida a 1/0.5/0
- Hoja1.D:D = Peso pregunta
- COUNTA = # preguntas
Resultado: Score 0-100
```

### Fórmula 2: ROI %

```
=((Beneficios_Anuales - Costos_Anuales) / Costos_Anuales) * 100

Donde:
- Beneficios = Sum(vulnerabilidades × €50k conversion)
- Costos = Sum(inversión herramientas + servicios)
Resultado: Porcentaje ROI (ej: 682%)
```

### Fórmula 3: Payback Period (meses)

```
=Costos_Totales / (Beneficios_Anuales / 12)

Resultado: Meses hasta recuperar inversión (ej: 1.5 meses)
```

### Fórmula 4: Progress %

```
=COUNTIF(Hoja1.E:E,"SÍ") / COUNTA(Hoja1.B:B) * 100

Resultado: % preguntas respondidas SÍ
```

---

## EXPORTACIÓN Y REPORTING

### Reportes Automáticos

1. **Reporte Ejecutivo Trimestral**
   - Screenshot Dashboard (Hoja 4)
   - Tabla KPI
   - Financial Summary
   - Formato: 1 página PDF

2. **Reporte Técnico Detallado**
   - IGM por sección
   - Brecha analysis
   - ROI por iniciativa
   - Formato: 3 páginas Excel

3. **Reporte Auditoría**
   - Completitud % por sección
   - Trazabilidad a NIS2/GDPR
   - Status remedición
   - Formato: Compliance report

---

## CONCLUSIÓN

Esta plantilla Excel proporciona:

✅ Automatización: Cálculo IGM, ROI, KPIs en tiempo real  
✅ Visibilidad: Dashboard ejecutivo con 5 gráficos  
✅ Trazabilidad: Conexión datos entrada → IGM → ROI  
✅ Análisis: Sensibilidad, escenarios, payback  
✅ Reporting: Exportación automática de reportes  

**Tiempo setup**: 4-6 horas (primera vez)  
**Mantenimiento trimestral**: 1 hora para actualizar datos

---

**FIN DE LA PLANTILLA EXCEL**