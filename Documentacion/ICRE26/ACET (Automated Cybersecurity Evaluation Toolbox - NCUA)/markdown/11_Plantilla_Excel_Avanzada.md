# PLANTILLA EXCEL AVANZADA: CALCULADORA IGM + ROI + GQM
## Especificaciones Técnicas Completas para Implementación

**Versión:** 3.0 | **Actualización:** Enero 2026 | **Compatibilidad:** Excel 2016+, Google Sheets, LibreOffice Calc

---

## ESTRUCTURA TOTAL: 8 HOJAS DE TRABAJO

```
PLANTILLA EXCEL PROFESIONAL ACET-GQM-PRAGMATIC
│
├─ HOJA 1: INPUT
│  └─ Ingesta respuestas encuesta (60 preguntas)
│     Estructura: ID | Pregunta | Opción Respuesta | Puntos | Dominio | GQM_Level | PRAGMATIC_Score
│
├─ HOJA 2: SCORING
│  └─ Cálculos automáticos de IGM por dominio
│     Tablas: Resumen dominio | Índices complementarios | KRIs
│
├─ HOJA 3: GQM_MAPPING
│  └─ Trazabilidad Goal→Question→Metric
│     Estructura: BG_ID | SG_ID | MG_ID | Q_ID | Métrica | Score |Nivel
│
├─ HOJA 4: PRAGMATIC_EVAL
│  └─ Evaluación 9 criterios PRAGMATIC para cada métrica
│     Tabla: Métrica | P | R | A | G | S | Pr | O | I | Re | Score | %
│
├─ HOJA 5: BENCHMARKING
│  └─ Comparativa vs. sector, nacional
│     Tablas: Benchmark comparativo | Radar data | Gap analysis
│
├─ HOJA 6: ROI_ANALYSIS
│  └─ Análisis retorno inversión
│     Tabla: Control | Inversión | Beneficio | Payback | ROI% | Prioridad
│
├─ HOJA 7: NORMATIVE_MAPPING
│  └─ Trazabilidad pregunta → requisito normativo
│     Tabla: Pregunta | NIST | ENS | NIS2 | GDPR | ISO | Artículos
│
└─ HOJA 8: DASHBOARD_EXECUTIVE
   └─ Resumen ejecutivo visual
      Elementos: IGM gauge | Radar NIST | KRIs | Roadmap | ROI summary
```

---

## HOJA 1: INPUT (Datos Encuesta)

### Estructura de Columnas

```
A: ID_PREGUNTA (Ej. P1.1.1)
B: PREGUNTA_TEXTO (Ej. "¿Existe política ciberseguridad?")
C: DOMINIO (GV, ID, PR, DE, RS, RC)
D: OPCION_RESPUESTA (Desplegable: Sí, Parcialmente, No, NA, DK)
E: PUNTOS (Fórmula automática)
F: NIVEL_GQM (Fórmula VLOOKUP a nivel jerárquico)
G: SCORE_PRAGMATIC (Fórmula referencia HOJA4)
H: VALIDADO (Checkbox: ✓/✗)
```

### Fórmula Columna E (PUNTOS)

```excel
=SWITCH(D2,
  "Sí",3,
  "Parcialmente",2,
  "No",1,
  "NA",NA(),
  "DK",2.5,
  "")
```

**Nota:** Escala 0-3 (compatible con PRAGMATIC 0-3)

### Fórmula Columna F (NIVEL_GQM)

```excel
=VLOOKUP(A2,HOJA3!$A:$B,2,FALSE)
```

Referencia a HOJA 3 para determinar nivel GQM de pregunta.

### Fórmula Columna G (SCORE_PRAGMATIC)

```excel
=VLOOKUP(A2,HOJA4!$A:$K,11,FALSE)
```

Trae score PRAGMATIC de evaluación en HOJA 4.

### Validación Hoja 1

```
Rango: D2:D61
Tipo: Lista
Opciones: Sí, Parcialmente, No, NA, DK
Mensaje de error: "Seleccionar opción válida"
```

---

## HOJA 2: SCORING (Cálculos IGM)

### 2.1 Tabla Resumen por Dominio (Celdas A1:G10)

```
DOMINIO    | PREGUNTAS | PROMEDIO | NIVEL | BENCHMARK_SECTOR | GAP
-----------|-----------|----------|-------|------------------|-----
GV         | 6         | 75%      | INT   | 78%              | -3%
ID         | 6         | 80%      | INT   | 82%              | -2%
PR         | 6         | 70%      | EVO   | 75%              | -5%
DE         | 5         | 65%      | EVO   | 70%              | -5%
RS         | 5         | 72%      | INT   | 71%              | +1%
RC         | 5         | 60%      | EVO   | 68%              | -8%
-----------|-----------|----------|-------|------------------|-----
IGM TOTAL  | 36        | 70%      | INT   | 74%              | -4%
```

### Fórmulas

**Columna B (PREGUNTAS):**
```excel
=COUNTIF(INPUT!$C$2:$C$61,"GV")
```

**Columna C (PROMEDIO):**
```excel
=AVERAGEIF(INPUT!$C$2:$C$61,"GV",INPUT!$E$2:$E$61)
```

**Columna D (NIVEL):**
```excel
=IF(C2>90,"INNOVATIVE",
   IF(C2>80,"ADVANCED",
     IF(C2>60,"INTERMEDIATE",
       IF(C2>40,"EVOLVING","BASELINE"))))
```

**Columna E (BENCHMARK):**
```
Referencia manual: Ingresar desde datos INCIBE/ISMS Forum
```

**Columna F (GAP):**
```excel
=C2-E2
```

### 2.2 Cálculo IGM Global Ponderado (Celda A13)

```excel
=(AVERAGEIF(INPUT!$C$2:$C$61,"GV",INPUT!$E$2:$E$61)*0.15) +
 (AVERAGEIF(INPUT!$C$2:$C$61,"ID",INPUT!$E$2:$E$61)*0.15) +
 (AVERAGEIF(INPUT!$C$2:$C$61,"PR",INPUT!$E$2:$E$61)*0.25) +
 (AVERAGEIF(INPUT!$C$2:$C$61,"DE",INPUT!$E$2:$E$61)*0.20) +
 (AVERAGEIF(INPUT!$C$2:$C$61,"RS",INPUT!$E$2:$E$61)*0.15) +
 (AVERAGEIF(INPUT!$C$2:$C$61,"RC",INPUT!$E$2:$E$61)*0.10)
```

**Ponderaciones NIST CSF 2.0:**
- GV (Governance): 15%
- ID (Identify): 15%
- PR (Protect): 25%
- DE (Detect): 20%
- RS (Respond): 15%
- RC (Recover): 10%

### 2.3 Índices Complementarios (Celdas A15:F20)

#### VA Score (Vulnerability Assessment Score)

```excel
=AVERAGEIFS(INPUT!$E$2:$E$61, INPUT!$A$2:$A$61, "P7*")
Target: ≥85%
```

#### SES Score (SIEM Effectiveness Score)

```excel
=AVERAGEIFS(INPUT!$E$2:$E$61, INPUT!$A$2:$A$61, "P8*")
Target: ≥80%
```

#### SATS Score (Security Awareness Training Score)

```excel
=AVERAGEIFS(INPUT!$E$2:$E$61, INPUT!$A$2:$A$61, "P9*")
Target: ≥85%
```

### 2.4 Tabla KRIs Críticos (Celdas A22:F35)

```
KRI | RESPUESTA_PREGUNTA | VALOR_ACTUAL | UMBRAL_CRÍTICO | ESTADO | ACCIÓN
----|-------------------|--------------|----------------|--------|--------
CVE Crítica Sin Parchear | P7.1.3 | 3 | 0 | 🔴 CRÍTICO | Parchear hoy
MTTD | P4.2.1 | 2h 30m | <2h | 🟡 ALERTA | Tune SIEM
FPR (False Positive) | P4.3.1 | 28% | <25% | 🟡 ALERTA | Tune reglas
SIEM Coverage | P4.1.1 | 78% | >85% | 🟡 ALERTA | Expand fuentes
```

#### Fórmula KRI (Ej. CVE Crítica)

```excel
=VALUE(INPUT!E[P7.1.3])
```

---

## HOJA 3: GQM_MAPPING (Trazabilidad Jerárquica)

### Estructura

```
BG_ID | SG_ID | MG_ID | Q_ID | MÉTRICA | SCORE | NIVEL_GQM | PREGUNTA_ASOC
------|-------|-------|------|---------|-------|-----------|---------------
BG-1  | SG-1.1| MG-1.1| Q-1.1| MTTD    | 2/3   | OPERATI   | P4.2.1
BG-1  | SG-1.1| MG-1.1| Q-1.1| SIEM_CV | 2/3   | OPERATI   | P4.1.1
BG-1  | SG-1.2| MG-1.2| Q-1.2| VA_Score| 2.5/3 | OPERATI   | P7.1.1
...
```

### Fórmulas para Cálculo Score

Para cada Q_ID, referencia datos INPUT:

```excel
=AVERAGEIFS(INPUT!$E:$E, INPUT!$A:$A, "P4*")
```

---

## HOJA 4: PRAGMATIC_EVAL (Evaluación 9 Criterios)

### Estructura

```
MÉTRICA | P/3 | R/3 | A/3 | G/3 | S/3 | Pr/3 | O/3 | I/3 | Re/3 | TOTAL/27 | %PRAG | ESTADO
--------|-----|-----|-----|-----|-----|------|-----|-----|------|----------|-------|-------
MTTD    | 3   | 3   | 3   | 2   | 3   | 3    | 3   | 2   | 3    | 25/27    | 93%   | ✓ OK
VA_Score| 3   | 3   | 3   | 3   | 3   | 3    | 3   | 3   | 3    | 27/27    | 100%  | ✓ OK
...
```

### Fórmula Score Total (Columna K)

```excel
=SUM(B2:J2)
```

### Fórmula % PRAGMATIC (Columna L)

```excel
=K2/27*100
```

### Fórmula ESTADO (Columna M)

```excel
=IF(L2>90,"✓ EXCELENTE",
   IF(L2>80,"✓ BUENO",
     IF(L2>70,"⚠️ ACEPTABLE","🔴 POBRE")))
```

---

## HOJA 5: BENCHMARKING (Comparativa)

### Tabla Principal

```
MÉTRICA | IGM_ORG | BENCHMARK_SECTOR | BENCHMARK_NACIONAL | DIFERENCIA
--------|---------|------------------|-------------------|------------
IGM     | 71%     | 76% (Fin)        | 64% (Promedio ES)  | -5% / +7%
GV      | 75%     | 78%              | 70%                | -3% / +5%
ID      | 80%     | 82%              | 72%                | -2% / +8%
...
```

### Fórmulas

```excel
Columna C (Benchmark Sector): Manual input o VLOOKUP a tabla referencia
Columna D (Benchmark Nacional): Manual input (INCIBE data)
Columna E (Diferencia): =B2-C2 (vs. sector) | =B2-D2 (vs. nacional)
```

### Visualización: Radar Chart (Recomendado)

```
Categorías (ejes): GV, ID, PR, DE, RS, RC
Serie 1 (Azul): IGM Organización
Serie 2 (Verde): Benchmark Sector
Serie 3 (Naranja): Benchmark Nacional
```

---

## HOJA 6: ROI_ANALYSIS (Análisis Retorno)

### Tabla Controles + ROI

```
CONTROL | INVERSIÓN | BENEFICIO_ANUAL | PAYBACK(meses) | ROI% | PRIORIDAD
--------|-----------|-----------------|----------------|------|----------
MFA     | €45K      | €60K            | 9              | 33%  | 2
EDR     | €120K     | €200K           | 7              | 67%  | 2
SIEM    | €150K     | €180K           | 10             | 20%  | 3
...
```

### Fórmulas

**Columna D (Payback):**
```excel
=(B2/C2)*12
```

**Columna E (ROI%):**
```excel
=((C2-B2)/B2)*100
```

**Columna F (Prioridad):**
```excel
=RANK(E2,E$2:E$10,0)  [0=DESC orden]
```

### Resumen ROI (Celdas A15:D20)

```
Total Inversión Año 1: €530K
Total Beneficio Estimado: €825K
ROI Promedio: 55%
Payback Period: 8 meses
Beneficio Neto (Año 1): €295K
```

---

## HOJA 7: NORMATIVE_MAPPING (Trazabilidad Normativa)

### Estructura

```
PREGUNTA | PREGUNTA_TEXTO | NIST_CSF | ENS | NIS2 | GDPR | ISO_27001 | ARTÍCULOS
---------|----------------|----------|-----|------|------|-----------|----------
P1.1.1   | Política CS    | ✓ GV-1  | ✓ A.5| ✓18.1| ✓32  | ✓ 5.1     | (Detalle)
P4.2.1   | MTTD <2h       | ✓ DE-4  | ✓ D.4| ✓21  | ✓32  | ✓ 8.4.4   | (Detalle)
...
```

### Validación

```
Cada ✓ en columna NIST/ENS/NIS2/GDPR/ISO = pregunta contribuye a marco
Si Cobertura < 95% en algún marco → GAP identificado
```

---

## HOJA 8: DASHBOARD_EXECUTIVE (Resumen Visual)

### Elementos Incluidos

#### Sección 1: IGM Gauge (Celda A1:C15)

```
Medidor Visual:
┌────────────────┐
│   IGM: 71%     │
│ INTERMEDIATE   │
│ (61-80%)       │
│ [Gauge Chart]  │
│ YTD: +3% ↗️    │
└────────────────┘
```

#### Sección 2: Radar NIST (Celda E1:H15)

```
Categorías: GV, ID, PR, DE, RS, RC
Serie 1: Actual (Azul)
Serie 2: Target (Verde)
Serie 3: Benchmark (Naranja)
```

#### Sección 3: KRIs Críticos (Celda A17:D30)

```
Semáforo:
🔴 CRÍTICO: CVE crítica sin parchear
🟡 ALERTA: MTTD >2h, FPR >25%
🟢 OK: MFA habilitado 92%
```

#### Sección 4: Roadmap Visual (Celda F17:J30)

```
Timeline:
Q1 2026: MFA + Capacitación
Q2 2026: Backups + SIEM
Q3 2026: EDR
Q4 2026: Revisión anual
```

#### Sección 5: ROI Summary (Celda A32:D45)

```
Total Inversión: €530K
ROI Expected: 55%
Payback: 8 meses
Top 3 Quick Wins: Capacitación, Backups, Pentesting
```

---

## VALIDACIONES Y CONTROLES DE CALIDAD

### Validación 1: Completitud

```excel
=COUNTBLANK(INPUT!$D$2:$D$61)
Si > 5 = ALERTA: "Encuesta incompleta"
```

### Validación 2: DK Ratio

```excel
=COUNTIF(INPUT!$D$2:$D$61,"DK")/COUNTA(INPUT!$D$2:$D$61)
Si > 10% = ALERTA: "Desconocimiento alto, validar CISO"
```

### Validación 3: NA Exclusión

```excel
=COUNTIF(INPUT!$D$2:$D$61,NA())
Incluir en resumen pero no ponderar
```

### Validación 4: Desviaciones

```excel
Si IGM ↑ >5% en 1 mes = INVESTIGAR: ¿Cambio real o sesgo?
```

---

## INSTRUCCIONES IMPLEMENTACIÓN

### Paso 1: Crear Estructura Base
1. Crear libro Excel nuevo (8 hojas nombradas)
2. Copiar headers de cada hoja desde esta plantilla

### Paso 2: Configurar Validaciones
1. Aplicar listas desplegables Columna D (INPUT)
2. Aplicar formatos condicionales (KRIs, PRAGMATIC)

### Paso 3: Implementar Fórmulas
1. Copiar fórmulas desde cada sección
2. Ajustar referencias ($A$2:$A$61 según rango real)

### Paso 4: Importar Datos
1. Exportar respuestas encuesta a CSV
2. Copiar/pegar en Hoja INPUT
3. Verificar automáticos cálculos en SCORING

### Paso 5: Generar Reportes
1. Dashboard: Copiar gráficos a PowerPoint
2. Benchmarking: Enviar a comparativa sector
3. ROI: Presentar a CFO para aprobación presupuesto

---

**Plantilla lista para uso. Descarga, personaliza, implementa.**

