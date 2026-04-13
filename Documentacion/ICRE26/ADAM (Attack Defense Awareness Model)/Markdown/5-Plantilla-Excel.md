# PLANTILLA EXCEL: CÁLCULO IGM Y ROI
## Guía de Implementación en Hoja de Cálculo

**Versión:** 1.0 | Enero 2026  
**Plataformas Compatibles:** Excel, Google Sheets, LibreOffice Calc

---

## ESTRUCTURA DE LA PLANTILLA

### Hoja 1: "DATOS ENCUESTA"

| Columna | Descripción | Tipo |
|---------|-------------|------|
| A | Número Pregunta (1-50) | ID |
| B | Sección (Gobernanza, Identificación, etc.) | Texto |
| C | Pregunta Literal | Texto |
| D | Respuesta Seleccionada (A/B/C/D/E) | Dropdown |
| E | Puntuación Automática (0-5) | Fórmula |
| F | Dominio NIST (GV/ID/PR/DE/RS/RC) | Referencia |
| G | Factor Ponderación | Decimal |
| H | Puntuación Ponderada | Fórmula |

**Fórmulas Ejemplo:**

```
Columna E (Puntuación 0-5):
=IF(D2="Inexistente",0, IF(D2="Inicial",1, IF(D2="Gestionada",2, 
   IF(D2="Definida",3, IF(D2="Optimizada",4,0)))))

Columna H (Ponderada):
=E2*G2
```

---

### Hoja 2: "CÁLCULO IGM"

| Campo | Fórmula | Ejemplo |
|-------|---------|---------|
| **Dominio GV (Gobernar)** | =PROMEDIO(H2:H6)*Ponderación GV | 2.8 |
| **Dominio ID (Identificar)** | =PROMEDIO(H7:H12)*Ponderación ID | 3.2 |
| **Dominio PR (Proteger)** | =PROMEDIO(H13:H20)*Ponderación PR | 3.0 |
| **Dominio DE (Detectar)** | =PROMEDIO(H21:H26)*Ponderación DE | 2.5 |
| **Dominio RS (Responder)** | =PROMEDIO(H27:H30)*Ponderación RS | 3.1 |
| **Dominio RC (Recuperar)** | =PROMEDIO(H31:H34)*Ponderación RC | 2.9 |
| **IGM Total** | =(GV+ID+PR+DE+RS+RC)/6 | **2.92** |
| **Maturity Level** | =IF(IGM<1.6,0, IF(IGM<2.5,1, IF(IGM<3.5,2, IF(IGM<4.1,3,4)))) | **2 (Gestionada)** |
| **Riesgo Residual (%)** | =IF(Maturity=0,80, IF(Maturity=1,70, IF(Maturity=2,50, IF(Maturity=3,30,10)))) | **50%** |

---

### Hoja 3: "ANÁLISIS COMPARATIVO"

**Estructura:**

| Dominio | Puntuación Actual | Benchmark Sector | Gap | Percentil Posición |
|---------|------------------|------------------|-----|-------------------|
| GV | 2.8 | 3.2 | -0.4 (-12.5%) | P25 |
| ID | 3.2 | 3.0 | +0.2 (+6.7%) | P75 |
| PR | 3.0 | 3.1 | -0.1 (-3.2%) | P40 |
| DE | 2.5 | 3.3 | -0.8 (-24.2%) | P10 |
| RS | 3.1 | 3.0 | +0.1 (+3.3%) | P60 |
| RC | 2.9 | 2.8 | +0.1 (+3.6%) | P65 |
| **IGM** | **2.92** | **3.07** | **-0.15 (-4.9%)** | **P40** |

**Fórmulas:**

```
Columna Gap:
=Puntuación_Actual - Benchmark

Columna Percentil:
=PERCENTRANK.INC(Rango_Benchmark, Puntuación_Actual)
```

---

### Hoja 4: "CÁLCULO ROI"

**Escenario 1: Implementación EDR/XDR**

| Item | Fórmula | Valor |
|------|---------|-------|
| **Riesgo Anual (ALE)** | TEF × TCap × (1-RS) × LM | €2,000,000 |
| **Costo Solución Año 1** | Licencias + Impl + Training | €150,000 |
| **Reducción Riesgo (%)** | % histórico del control | 80% |
| **Riesgo Mitigado (€)** | ALE × Reducción | €1,600,000 |
| **Beneficio Neto** | Riesgo Mitigado - Costo | €1,450,000 |
| **ROSI (%)** | (Beneficio Neto / Costo) × 100 | **967%** |
| **Payback (días)** | (Costo / (Beneficio Neto / 365)) | **34 días** |

**Fórmulas Excel:**

```
ALE: =TEF * TCap * (1-RS) * LM

ROSI: =(Riesgo_Mitigado - Costo) / Costo * 100

Payback: = Costo / (Beneficio_Neto / 365)
```

---

**Escenario 2: Implementación SIEM**

| Item | Fórmula | Valor |
|------|---------|-------|
| **Eventos/Segundo (EPS)** | Estimación o histórico | 3,000 EPS |
| **Costo Licencia (€/EPS/año)** | Mercado | €100/EPS |
| **Costo Implementación** | Global + Integración | €150,000 |
| **Costo Operación Anual** | SIEM + SOC (si aplicable) | €200,000 |
| **Costo Total Año 1** | Licencias + Impl + Op | €500,000 |
| **Beneficios Cuantificables** | MTTD reduction + Forensics acceleration | €2,000,000 |
| **ROSI** | (Beneficios - Costo) / Costo | **300%** |

---

### Hoja 5: "ROADMAP 18 MESES"

**Estructura:**

| Q | Inicitativa | Inversión | IGM Esperado | Beneficio Acumulado | ROI Proyectado |
|---|-------------|-----------|--------------|-------------------|-----------------|
| Q1 | Quick Wins (MFA, Policy) | €100k | 2.92 → 3.20 | €500k | 400% |
| Q2-Q3 | Strategic (SIEM, Pentest) | €400k | 3.20 → 3.90 | €2M + €1.5M | 600-700% |
| Q4-Q6 | Optimization (Red Team, ZT) | €300k | 3.90 → 4.10 | €3M + €1M | 500-800% |
| **Total 18m** | **12 inicitativas** | **€800k** | **→ 4.10** | **€7M+ acumulado** | **600-800%** |

---

### Hoja 6: "DASHBOARD EJECUTIVO"

**Componentes Visuales Recomendados:**

1. **Gauge Chart: IGM General**
   - Rango: 0-5
   - Zonas: Rojo <2, Amarillo 2-3, Verde 3-4, Azul >4

2. **Radar Chart: Dominios NIST**
   - 6 ejes (GV, ID, PR, DE, RS, RC)
   - Zona exterior = Benchmark
   - Zona interior = Actual
   - Visualiza gaps inmediatamente

3. **Bar Chart: Vulnerabilidades Pendientes**
   - Críticas, Altas, Medias, Bajas
   - Target vs. Actual

4. **KPI Cards:**
   - MTTD: 2.5h (target <1h)
   - Incidents/Year: 5 (trending ↓)
   - Compliance: 92% (vs target >95%)
   - ROI Acumulado: €3.2M

5. **Timeline: Roadmap Visual**
   - Hitos Q1-Q6
   - IGM growth trajectory
   - Investment vs benefit

---

## IMPLEMENTACIÓN PASO A PASO

### Paso 1: Descargar Plantilla Base
- Google Sheets Template: [Link de ejemplo]
- Excel Template: [Link de ejemplo]

### Paso 2: Rellenar Datos Encuesta
- 50 preguntas × Respuesta (A/B/C/D/E)
- Sistema automático convierte a 0-5

### Paso 3: Validar Datos
- Verificar no hay campos vacíos
- Cross-check con evidencia (certificados, reportes)

### Paso 4: Generar IGM
- Hoja "Cálculo IGM" auto-calcula
- Asignar a Maturity Level
- Identificar gaps principales

### Paso 5: Crear Roadmap
- Seleccionar iniciativas rápido-impacto (Q1)
- Planificar estratégicas (Q2-Q3)
- Optimización sostenible (Q4-Q6)

### Paso 6: Presentar Ejecutiva
- Dashboard visual (1 página)
- ROI + Roadmap (2 páginas)
- Recomendaciones específicas (1 página)

---

## CASOS DE USO

### UC1: Benchmarking Interno Trimestral
- Rellenar encuesta cada Q
- Comparar IGM vs Q anterior
- Visualizar tendencias

### UC2: Auditoría Externa
- Proporcionar plantilla pre-rellenada
- Auditor valida y ajusta
- IGM independiente como score de entrada

### UC3: Investment Business Case
- Usar ROI Sheet para justificar presupuesto
- Presentar IGM actual → proyectado
- CFO ve "payback en 34 días"

### UC4: Supply Chain Risk
- Entregar a proveedores críticos
- Recopilar IGM de terceros
- Identificar riesgos de proveedores débiles

---

## LIMITACIONES Y NOTAS

1. **Datos auto-reportados:** Requieren validación externa (auditoría)
2. **Ponderaciones:** Pueden ajustarse por industria/regulación
3. **Benchmarks:** Actualizar anualmente con datos de mercado
4. **No es predictor:** IGM es "fotografía", no garantiza evitar incidente próximo
5. **Confidencialidad:** Plantilla contiene datos sensibles (no compartir públicamente)

---

**Fin de Plantilla Excel**

*Descargar archivo Excel en: [URL de repositorio]*
