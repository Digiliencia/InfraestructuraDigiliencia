# PLANTILLA EXCEL: ANÁLISIS AUTOMÁTICO IGM + PRAGMATIC + ROI
## Cálculos Indicadores GQM Integrados en Hojas Colaborativas

**Versión:** 3.0 | **Compatibilidad:** Excel 2016+, Google Sheets, Números  
**Hojas Incluidas:** 7 (Datos, Análisis IGM, PRAGMATIC, Brecha Normativa, ROI, KPIs, Referencias)

---

## ESTRUCTURA PLANTILLA EXCEL

### 🟦 HOJA 1: DATOS BRUTOS

**Objeto:** Importar respuestas encuesta + PRAGMATIC scores

```
Columnas:
A - Respondente (CISO, TI, Legal, etc.)
B - Fecha respuesta
C:L - Preguntas 1-75 (escala L1-L5)
M:U - PRAGMATIC scores (P/R/A/G/M/A/T/I/C: escala 1-5)
V - Observaciones cualitativas

Filas: 1 (header) + N respondentes + 1 (media)

Fórmulas:
- Fila media: AVERAGE(C2:C5) para cada pregunta
- Media PRAGMATIC: AVERAGE(M2:M5)
```

**Formato Plantilla:**

| Respondente | Fecha | Q1.1 | Q1.2 | ... | Q10.4 | Predictivo | Relevante | ... | Oportuno | Observaciones |
|-----------|-------|------|------|-----|--------|-----------|-----------|-----|----------|-------------|
| CISO | 24/01/2026 | 4 | 3 | ... | 5 | 5 | 5 | ... | 4 | Buena comprensión |
| TI Jefe | 24/01/2026 | 3 | 3 | ... | 4 | 4 | 4 | ... | 5 | Preocupación SIEM |
| Legal | 25/01/2026 | 4 | 4 | ... | 3 | 5 | 5 | ... | 3 | Enfoque NIS2 |
| **Media** | | **3.7** | **3.3** | ... | **4.0** | **4.7** | **4.7** | ... | **4.0** | |

---

### 🟩 HOJA 2: ANÁLISIS IGM (Índice Global Madurez)

**Objeto:** Cálculo madurez CMM L0-L5 por bloque + general

```
Estructura por bloque:

┌─────────────────────────────────────┐
│ BLOQUE 1: GOBERNANZA (4 preguntas)  │
├─────────────────────────────────────┤
│ Puntuación promedio: 3.2            │
│ Madurez: L3 (Repetible)             │
│ Status: 🟡 Aceptable                │
│ Benchmark: 3.5 (industry: 3.0)      │
│ Gap vs. Target: -0.3 puntos         │
└─────────────────────────────────────┘

FÓRMULAS:
- Promedio Bloque 1: =AVERAGE(C$2:C$5) [preguntas 1.1-1.4]
- Nivel CMM: =IF(Avg<2,"L1",IF(Avg<3,"L2",...)) [mapeo]
- IGM General: =AVERAGE(Promedio_Bloque_1:Promedio_Bloque_10)
- Target ajustado: =IGM_General*1.2 (target +20%)
```

**Tabla Resultados:**

| Bloque | # Preguntas | Promedio | CMM | Status | Benchmark | Gap |
|--------|-----------|----------|-----|--------|-----------|-----|
| 1. Gobernanza | 4 | 3.2 | L3 | 🟡 | 3.0 | +0.2 |
| 2. MAR Riesgos | 8 | 2.8 | L2 | 🔴 | 3.2 | -0.4 |
| 3. Indicadores | 7 | 3.1 | L3 | 🟡 | 3.0 | +0.1 |
| 4. Vulnerabilidades | 9 | 3.5 | L3 | 🟡 | 3.1 | +0.4 |
| 5. SIEM | 12 | 2.5 | L2 | 🔴 | 3.5 | -1.0 |
| 6. Capacitación | 9 | 3.0 | L3 | 🟡 | 2.8 | +0.2 |
| 7. Resiliencia | 10 | 2.9 | L2 | 🔴 | 3.2 | -0.3 |
| 8. Cumplimiento | 10 | 3.4 | L3 | 🟡 | 3.0 | +0.4 |
| 9. Incidentes | 6 | 3.2 | L3 | 🟡 | 3.1 | +0.1 |
| 10. Contexto | 4 | 3.3 | L3 | 🟡 | 3.0 | +0.3 |
| **IGM GENERAL** | **75** | **3.09** | **L3** | **🟡** | **3.09** | **=** |

**Interpretación:**
- 🟢 Verde (L4-L5): Fortaleza competitiva
- 🟡 Amarillo (L2-L3): Aceptable, mejorar
- 🔴 Rojo (L0-L1): Crítico, acción inmediata

---

### 🟪 HOJA 3: PRAGMATIC SCORE

**Objeto:** Matriz 20 indicadores × 9 criterios PRAGMATIC

```
Estructura:

Indicador | Predictivo | Relevante | Accionable | Genuino | Significativo | Preciso | Oportuno | Independiente | Rentable | PRAGMATIC Score | Status

1.1 Cobertura Inventario | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4.4 | ✓ BUENO

2.1 ARO Amenaza | 4 | 5 | 5 | 4 | 4 | 3 | 5 | 4 | 5 | 4.3 | ✓ BUENO

[... 18 indicadores más]

FÓRMULAS:
- PRAGMATIC Score: =AVERAGE(C:K) [media 9 criterios]
- Status: =IF(Avg>4.5,"✓ EXCELENTE",IF(Avg>3.5,"✓ BUENO",...))
- Dashboard: Gráfico Radar (9 ejes = 9 criterios)
```

**Salida Visualización:**

```
PRAGMATIC DISTRIBUTION (20 indicadores)

5.0 |                    ▌
4.5 | ▌▌▌▌▌          ▌▌▌
4.0 | ▌▌▌▌▌▌▌    ▌▌▌▌
3.5 | ▌▌▌▌▌▌▌▌▌▌▌
3.0 | ▌
    └─────────────────────
      Indicadores
      
Promedio: 3.85/5.0 → ACEPTABLE
Target: 4.0+ (92% logrado)
```

---

### 🟫 HOJA 4: BRECHA NORMATIVA

**Objeto:** % Conformidad por requisito NIS2/ENS/ISO 27001

```
Estructura:

Requisito | Indicadores Alineados | Cobertura % | Status | Plan Acción

NIS2 Art 21(a) Análisis Riesgos | 1.1, 2.1, 3.1, 4.1 | 92% | 🟡 | Completar análisis dependencias

NIS2 Art 21(d) Continuidad | 1.4, 7.1-7.3 | 78% | 🟡 | RTO/RPO formales 6m

ENS Med.2 Análisis Amenazas | 2.1-2.4 | 85% | 🟡 | STRIDE threat modeling

ISO A.8.1 Gestión Activos | 1.1-1.3 | 88% | 🟡 | Herramienta CMDB automática

FÓRMULAS:
- Cobertura %: =COUNTIF(indicadores_cumplidos)/Total×100
- Status: Color-code rojo/amarillo/verde por umbral
```

**Tabla Heatmap:**

| Requisito | 2024 | 2025 | 2026 Target | Brecha |
|-----------|------|------|-----------|--------|
| NIS2 Art 21(a) | 75% | 88% | 95% | -7% |
| NIS2 Art 21(d) | 60% | 78% | 90% | -12% |
| NIS2 Art 21(g) | 82% | 85% | 95% | -10% |
| ENS Med.1-6 | 68% | 82% | 95% | -13% |
| ISO 27001 | 70% | 88% | 95% | -7% |
| **PROMEDIO** | **71%** | **84%** | **94%** | **-10%** |

---

### 🟥 HOJA 5: ROI SALVAGUARDAS

**Objeto:** Análisis financiero inversiones ciberseguridad (FAIR/ALE)

```
Estructura por salvaguarda:

Salvaguarda | Costo Implantación | Costo Anual | ALE Reducción | Payback Meses | NPV 3años | ROI %

SIEM centralizado | €50K | €30K/año | €364K | 1.6m | €892K | 1784%

RTO/RPO formales | €75K | €15K/año | €140K | 6.4m | €325K | 433%

SOC 24/7 | €0K | €120K/año | €70K | - | €-150K | -125% (NO HACER)

Penetesting anual | €20K | €5K/año | €100K | 2.4m | €265K | 1325%

FÓRMULAS:
- Payback = Costo Implantación / (ALE Reducción / 12)
- NPV = SUM(CF_año1, CF_año2, CF_año3) discounted @ 8%
- ROI % = (Beneficio neto 3 años / Costo total) × 100

CF_año1 = ALE_reducción - Costo_anual - Amortización_implantación
CF_año2-3 = ALE_reducción - Costo_anual
```

**Salida Bubble Chart:**

```
ROI SALVAGUARDAS (Costo × Impacto × Plazo)

Alto impacto     │ ●SIEM        ●Pentesting
                │ (€364K red)  (€100K red)
Impacto ALE      │
                │ ●RTO/RPO
                │ (€140K red)
Bajo impacto     │              ●SOC24/7 ✗
                │              (bajo ROI)
                └────────────────────────────
                Costo inversión (bajo → alto)

Recomendación: Invertir SIEM + Pentesting (ROI >1000%)
```

---

### 🟦 HOJA 6: KPIs EJECUTIVOS

**Objeto:** Dashboard 1-página para presentación Junta Directiva

```
Layout PowerPoint-style:

┌────────────────────────────────────────┐
│ SCORECARD CIBERSEGURIDAD 2026          │
├────────────────────────────────────────┤
│                                        │
│ IGM Madurez:    62% (L3 Repetible)    │ [Gauge]
│ Target 12m:     75% (L4 Gestionado)   │
│ Gap:            +13 puntos             │
│                                        │
│ PRAGMATIC Score: 3.85/5.0 (ACEPTABLE) │ [Gauge]
│ Indicadores B+:   75% (15/20)         │
│                                        │
│ Conformidad NIS2: 82% (AMARILLO)      │ [Traffic light]
│ Riesgos Críticos: 3 requisitos        │
│                                        │
│ ALE Residual:    €480K/año            │ [vs target €400K]
│ ROI 2025:        €890K (POSITIVO)     │ [Arrow up]
│                                        │
│ Plan Acción 2026:                     │
│  ✓ Completado 60% (18/30 acciones)   │ [Progress bar]
│  ⏳ En progreso 30%                   │
│  🔲 Pendiente 10%                     │
│                                        │
└────────────────────────────────────────┘

FÓRMULAS (auto-refresh):
- IGM: Formula de HOJA 2
- PRAGMATIC: Formula de HOJA 3
- Brecha: Formula de HOJA 4
- ALE: Formula de HOJA 5
- Plan Acción: VLOOKUP de tracking spreadsheet
```

---

### 🟩 HOJA 7: REFERENCIAS & VALIDACIÓN

**Objeto:** Tablas lookup, constantes, validación datos

```
SECCIÓN 1: Tablas Lookup

Escala CMM Mapping:
Promedio 1.0-1.5 → L1 Ad hoc
Promedio 1.6-2.5 → L2 Repetible
Promedio 2.6-3.5 → L3 Definido
Promedio 3.6-4.5 → L4 Gestionado
Promedio 4.6-5.0 → L5 Optimizado

PRAGMATIC Status Mapping:
Score <2.6 → 🔴 DEFICIENTE
Score 2.6-3.5 → 🟡 ACEPTABLE
Score >3.5 → 🟢 BUENO

SECCIÓN 2: Constantes

ALE_Target: €400,000/año
Descuento_NPV: 8%
Horizonte_ROI: 3 años
Benchmark_IGM: 3.09 (industria promedio)

SECCIÓN 3: Validación Datos

- Lista desplegable preguntas (1-75)
- Lista desplegable PRAGMATIC criterios (P/R/A/G/M/A/T/I/C)
- Validación rango respuesta (1-5)
- Alert si celda >5 o <1
```

---

## INSTRUCCIONES IMPLEMENTACIÓN

### Paso 1: Descargar plantilla Excel
```
Archivo: 12-template-excel-gqm-pragmatic.xlsx
```

### Paso 2: Rellenar HOJA 1 (Datos Brutos)
```
1. Importar respuestas encuesta (75 preguntas, 3-5 respondentes)
2. Añadir PRAGMATIC scores para cada respondente (9 criterios)
3. Validar escala (1-5 todas columnas)
4. Añadir observaciones cualitativas
```

### Paso 3: Ejecutar fórmulas
```
- Hojas 2-7 recalculan automáticamente
- Gráficos se actualizan en tiempo real
- No editar hojas 2-7 (fórmulas protegidas)
```

### Paso 4: Interpretar resultados
```
IGM < 3.0: Crítico, acción inmediata
3.0-3.5: Aceptable, mejorar
>3.5: Bueno, mantener y optimizar

ROI <12m: Invertir ahora
ROI 12-36m: Priorizar
ROI >36m o negativo: Considerar después
```

---

## MACROS OPCIONALES (Excel VBA)

### Macro 1: Auto-refresh Gráficos
```vba
Sub RefreshCharts()
  ActiveSheet.Shapes.Range(Array("Chart1")).Select
  Selection.Chart.Refresh
End Sub
```

### Macro 2: Generar Reporte PDF
```vba
Sub ExportToPDF()
  ActiveSheet.ExportAsFixedFormat FileFormat:=xlTypePDF, _
  Filename:="Reporte_Ciberseguridad_" & Format(Date(), "yyyymmdd")
End Sub
```

---

**© 2026 Plantilla Excel GQM+PRAGMATIC | Consorcio Ciberseguridad**  
*Análisis automático 7 hojas integradas: indicadores, madurez, calidad, conformidad, ROI, ejecutivo.*
