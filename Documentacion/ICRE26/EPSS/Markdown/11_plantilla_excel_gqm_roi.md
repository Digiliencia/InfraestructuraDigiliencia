# PLANTILLA EXCEL PARA IGM, ROI Y SEGUIMIENTO GQM+PRAGMATIC
## Herramientas Cuantitativas con Cálculos Integrados

**Versión:** 1.0  
**Fecha:** Enero 2026  
**Instrucciones:** Reproducir estructura en Google Sheets o Excel

---

## HOJA 1: SCORING GQM+ PRAGMATIC

### Estructura Entrada de Datos

```
EVALUACIÓN GQM+PRAGMATIC - MÉTRICAS EPSS
Organización: ________________    Fecha: ________
Evaluador: ________________       Periodo: ______

SECCIÓN A: GESTIÓN VULNERABILIDADES
────────────────────────────────────────────────────────────

MÉTRICA A1: Cobertura EPSS (% CVEs con EPSS score)
─────────────────────────────────────────────────────
Valor Actual:            _____ %
Valor Target (NIS2):     _____ % (recomendado 80%+)
GQM Level (Predictivo, Relevante, ...): Predictivo(8) Relevante(9) ...
PRAGMATIC Score: ____/10

[Repetir para A2, A3, B1, C1, D1, E1...]

TOTAL PRAGMATIC POR SECCIÓN:
Sección A (Vulnerabilidades): _____/10
Sección B (SIEM):             _____/10
Sección C (Incidentes):       _____/10
Sección D (Capacitación):     _____/10
Sección E (Gobernanza):       _____/10

IGM GLOBAL = (Sec.A + Sec.B + Sec.C + Sec.D + Sec.E) / 5 = ______/10
```

### Fórmulas Excel Recomendadas

```
Para promediar PRAGMATIC por sección (asumiendo celdas B2:B10):
=AVERAGE(B2:B10)

Para clasificación automática IGM:
=IF(IGM>=9,"Excelente",IF(IGM>=8,"Muy Buena",IF(IGM>=7,"Buena",IF(IGM>=6,"Aceptable",IF(IGM>=5,"Deficiente","Crítica")))))

Para color condicional formato:
Valor >= 8.5 → Verde Oscuro
Valor 7.0-8.4 → Verde Claro
Valor 5.5-6.9 → Amarillo
Valor < 5.5 → Rojo
```

---

## HOJA 2: TRAZABILIDAD GQM

### Matriz Objetivo → Pregunta → Métrica → Pragmatic

```
Nivel 1: OBJETIVO
├─ OB-1: Reducir MTTR vulnerabilidades críticas
│
├─ Nivel 2: PREGUNTA
│  └─ Q1.1: ¿MTTR actual (EPSS≥0.50)?
│
├─ Nivel 3: MÉTRICA
│  └─ M1.1.1: MTTR_high_EPSS = Σ(fecha_remediation - fecha_detection) 
│              / Count(EPSS≥0.50)
│
├─ Nivel 4: PRAGMATIC SCORES
│  ├─ Predictivo: 6/10
│  ├─ Relevante: 9/10
│  ├─ Accionable: 8/10
│  ├─ Genuino: 7/10
│  ├─ Significativo: 8/10
│  ├─ Preciso: 6/10
│  ├─ Oportuno: 7/10
│  ├─ Independiente: 5/10
│  ├─ Rentable: 10/10
│  └─ PROMEDIO: 7.3/10 ✓ Implementar
│
└─ Nivel 5: REGULACIÓN
   ├─ NIS2 Art. 21(E): ✓ Mapea
   ├─ GDPR Art. 32: ✓ Mapea
   └─ ENS SD.05: ✓ Mapea
```

### Tabla Excel

```
TRAZABILIDAD GQM - TABLA
╔════════════════════════════════════════════════════════════════╗
║ ID  │ OBJETIVO │ PREGUNTA │ MÉTRICA │ PRAGMATIC │ REGULACIÓN ║
╠════════════════════════════════════════════════════════════════╣
║ OB1 │ Reducir  │ Q1.1     │ M1.1.1  │ 7.3/10    │ NIS2 21(E) ║
║     │ MTTR     │          │         │ ✓         │ GDPR 32   ║
║     │          │          │         │           │ ENS SD.05 ║
╚════════════════════════════════════════════════════════════════╝
```

---

## HOJA 3: ANÁLISIS ROI/ROSI PARA GQM+PRAGMATIC

### Lógica de ROI

```
Premisa: Métricas GQM+PRAGMATIC de alta calidad (7.5+/10) 
         generan mejor decision-making → reducen riesgo

PASO 1: Cuantificar Riesgo Actual (ALE - Annual Loss Expectancy)
───────────────────────────────────────────────────────────────

Sin EPSS / sin GQM:
- Data Breach prob 15% × €2M impacto = €300K
- Ransomware prob 8% × €1M = €80K
- Multa NIS2 (incumplimiento) prob 5% × €5M = €250K
                                    ─────────────
                          ALE Total: €630K/año

CON EPSS + GQM+PRAGMATIC:
- Probabilidades ↓ porque priorización mejor
- Data Breach prob ↓ 15% → 9% (-40% por detección mejor MTTD)
- Ransomware ↓ 8% → 4% (-50% por MTTR mejorado)
- Multa NIS2 ↓ 5% → 1% (-80% por compliance documentado)

New ALE:
- €2M × 9% = €180K
- €1M × 4% = €40K
- €5M × 1% = €50K
           ─────────
           €270K/año

REDUCCIÓN ALE = €630K - €270K = €360K/año
```

### Cálculo ROSI

```
INVERSIÓN EN GQM+PRAGMATIC FRAMEWORK (Año 1):
─────────────────────────────────────────────
- Herramientas EPSS integration:      €50K
- Consultoría GQM+PRAGMATIC setup:    €30K
- Capacitación en equipo:             €15K
- Dashboards/reporting systems:       €20K
                            TOTAL:    €115K

BENEFICIO PROYECTADO (Año 1):
─────────────────────────────
- Reducción ALE:                      €360K
- Menos multas NIS2:                  €200K
- Seguros + prima reduction:          €50K
                            TOTAL:    €610K

ROSI = (Beneficio - Inversión) / Inversión × 100%
     = (€610K - €115K) / €115K × 100%
     = €495K / €115K
     = 430% ✓ EXCELENTE ROI
```

### Tabla Excel ROSI

```
CÁLCULO ROSI GQM+PRAGMATIC
╔═══════════════════════════════════════════════╗
║ Concepto              │ Valor        │ Notas ║
╠═══════════════════════════════════════════════╣
║ ALE Actual (sin GQM)  │ €630K        │      ║
║ ALE Futuro (con GQM)  │ €270K        │      ║
║ Reducción ALE         │ €360K        │ ✓    ║
║ Inversión Año 1       │ €115K        │      ║
║ ROSI                  │ 430%         │ ✓✓✓  ║
║ Payback               │ 3.8 meses    │      ║
╚═══════════════════════════════════════════════╝
```

---

## HOJA 4: DASHBOARD DE SEGUIMIENTO TRIMESTRAL

### KPIs Clave por Trimestre

```
KPI TRACKING - 2026
═════════════════════════════════════════════════════════════

MÉTRICA                      │ Q1 Target │ Q1 Actual │ Q2 Target │ Estado
─────────────────────────────────────────────────────────────────────────
A1: Cobertura EPSS (%)       │  70%      │  ___      │  80%      │ ⭕
A2: MTTR Críticas (días)     │  10       │  ___      │  7        │ ⭕
A3: Efficiency EPSS (%)      │  50%      │  ___      │  65%      │ ⭕
B1: MTTD Incidentes (horas)  │  24       │  ___      │  12       │ ⭕
C1: MTTE Reguladores (horas) │  18       │  ___      │  12       │ ⭕
D1: Phishing Click (%)       │  25%      │  ___      │  15%      │ ⭕
E1: Documentación (%)        │  80%      │  ___      │  95%      │ ⭕

PRAGMATIC SCORE PROMEDIO     │  7.3      │  ___      │  7.8      │ ⭕

IGM GLOBAL                   │  3.1      │  ___      │  3.5      │ ⭕
Clasificación                │ Aceptable │  ___      │ Buena     │ ⭕

Estado: ✓ En Track / ⚠️ Atrás / ❌ Crítico
```

---

## HOJA 5: MATRIZ DE DECISIÓN (Decision Support)

### Acciones Recomendadas por Score

```
SI PRAGMATIC SCORE DE MÉTRICA:

≥ 8.5  → VERDE: Mantener, no cambiar implementación
7.0-8.4 → AMARILLO: Implementar pero mejorar (doc, precisión)
<7.0   → ROJO: Reconsiderar antes de producción

EJEMPLOS ACCIONES:

Métrica A1 (Cobertura) = 8.7 ✓ GREEN
└─ Acción: Mantener API EPSS en VM tool

Métrica A2 (MTTR) = 7.6 ⚠️ YELLOW
└─ Acción: Mejorar precisión timestamps (Git 500)
└─ Deadline: Fin Q1 2026

Métrica B1 (MTTD) = 7.5 ⚠️ YELLOW
└─ Acción: Implementar ML tuning SIEM
└─ Budget requerido: €50K
└─ Timeline: Q2 2026
```

---

## CONCLUSIÓN: ESTRUCTURA EXCEL

Reproducir 5 hojas con fórmulas linking:
1. **Scoring** (entrada de datos)
2. **GQM Trace** (trazabilidad top-down)
3. **ROI/ROSI** (business case)
4. **Dashboard** (KPIs seguimiento)
5. **Decision Support** (accionabilidad)

**Beneficio:** Sistema integrado que muestra:
- ✓ Qué métricas implementar (PRAGMATIC scores)
- ✓ Por qué (GQM objectives)
- ✓ Cuál es el valor (ROSI 430%)
- ✓ Cómo proceder (Dashboard + Decision Matrix)

---

*Plantilla Excel desarrollada por Consorcio de Científicos de Datos y Estrategas de Ciberseguridad*  
*Enero 2026*
