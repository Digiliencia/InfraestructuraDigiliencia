# PLANTILLA DE EXCEL: CÁLCULO IGM, ROICS Y DASHBOARD
## Especificaciones Técnicas para Implementar en Excel/Google Sheets

---

## ESTRUCTURA GENERAL DEL ARCHIVO

**Nombre:** `Mercury_Assessment_2026_[Organización].xlsx`

**Sheets recomendadas:** 8 hojas

```
1. RAW_DATA (datos de encuesta)
2. SCORING (cálculos por dominio)
3. METRICS (indicadores principales)
4. FINANCIAL (ROICS y análisis financiero)
5. DASHBOARD (visualización gráficos)
6. NIS2_ROADMAP (plan de conformidad)
7. RECOMMENDATIONS (acciones prioritarias)
8. DOCUMENTATION (referencias y notas)
```

---

## SHEET 1: RAW_DATA (Datos Crudos de Encuesta)

### Estructura

```
Fila 1: Encabezados
Columna A: ResponseID (Ej: R001, R002, ... R009)
Columna B: Respondent Name
Columna C: Respondent Role (CISO, Manager TI, Técnico, etc.)
Columna D: Department
Columna E: Date Response
Columnas F-N: Preguntas GR-M1 a GR-M8 (scores 1-5)
Columnas O-U: Preguntas VUL-M1 a VUL-M7 (scores 1-5)
... (continuar con todos los dominios)
```

### Ejemplo de Datos

```
| ResponseID | Name | Role | Department | Date | GR-M1 | GR-M2 | GR-M3 | ... |
|---|---|---|---|---|---|---|---|---|
| R001 | Juan CISO | CISO | Security | 2026-01-15 | 4 | 2 | 5 | ... |
| R002 | María Manager | Manager | TI | 2026-01-16 | 3 | 2 | 4 | ... |
| R003 | Pedro Tech | Técnico | Infrastructure | 2026-01-17 | 3 | 1 | 4 | ... |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
```

### Validación de Datos

Crear reglas de validación en Excel:
```
- Scores: valores entre 1-5 (números enteros)
- ResponseID: únicos
- Date Response: formato fecha
- Roles: lista desplegable (predefinida)
```

---

## SHEET 2: SCORING (Cálculos por Dominio)

### Estructura

| Dominio | Métrica | R1 | R2 | R3 | R4 | R5 | Media | Desv.Est. | Varianza | Consenso |
|---|---|---|---|---|---|---|---|---|---|---|
| **GR** | GR-M1 | 4 | 3 | 3 | 4 | 5 | 3.8 | 0.84 | 0.7 | ALTO |
| | GR-M2 | 2 | 2 | 1 | 2 | 3 | 2.0 | 0.71 | 0.5 | ALTO |
| | GR-M3 | 5 | 4 | 4 | 5 | 5 | 4.6 | 0.55 | 0.3 | ALTO |
| | **GR Total** | | | | | | **3.5** | | | |
| | | | | | | | | | | |
| **VUL** | VUL-M1 | 5 | 4 | 4 | 5 | 4 | 4.4 | 0.55 | 0.3 | ALTO |
| | VUL-M2 | 3 | 4 | 4 | 3 | 4 | 3.6 | 0.55 | 0.3 | ALTO |
| | VUL-M3 | 4 | 4 | 3 | 4 | 4 | 3.8 | 0.45 | 0.2 | ALTO |
| | **VUL Total** | | | | | | **3.9** | | | |

### Fórmulas en Excel

#### Media (Average)
```
=AVERAGE(R1:R5)
```

#### Desviación Estándar
```
=STDEV.S(R1:R5)  [Sample]
o
=STDEV.P(R1:R5)  [Population]
```

#### Varianza
```
=VAR.S(R1:R5)
```

#### Consenso (Clasificación)
```
=IF(STDEV.S(R1:R5)<0.6,"ALTO",IF(STDEV.S(R1:R5)<0.9,"MEDIO","BAJO"))
```

#### Media por Dominio (Ponderada)
```
Ejemplo para Dominio GR:
=AVERAGE(GR_M1_Media, GR_M2_Media, GR_M3_Media, ..., GR_M8_Media)

Ponderación (si aplica):
=SUMPRODUCT(Scores, Pesos) / SUM(Pesos)
```

---

## SHEET 3: METRICS (Indicadores Principales)

### Estructura

| Indicador | Fórmula | Valor | Objetivo | Brecha | Status |
|---|---|---|---|---|---|
| **IGM (Índice Global de Madurez)** | =AVERAGE(GR, VUL, SIEM, CAP, NORM, CONT, SUPL, RESP, INT, CTRL, REM, AUD) | 3.2 | 4.5 | -1.3 | 🔴 |
| **% Conformidad NIS2** | =(# respuestas ≥3 / 21 medidas) × 100 | 68% | 80% | -12% | 🟠 |
| **Nivel NIST CSF** | =IGM × 6 / 30 | Nivel 3 | Nivel 4 | -1 | 🔴 |
| **ROICS (3 años)** | =(Beneficios - Inversión) / Inversión × 100 | 114% | >50% | +64% | 🟢 |
| **Payback Period** | =Costo Total / Beneficio Anual Promedio | 1.4 años | <2 años | -0.6 | 🟢 |

### Cálculos Detallados

#### 1. IGM (Índice Global de Madurez)

```
IGM = (GR + VUL + SIEM + CAP + NORM + CONT + SUPL + RESP + INT + CTRL + REM + AUD) / 12

Fórmula Excel:
=AVERAGE(Sheet2!GR_Total, Sheet2!VUL_Total, Sheet2!SIEM_Total, 
         Sheet2!CAP_Total, Sheet2!NORM_Total, Sheet2!CONT_Total,
         Sheet2!SUPL_Total, Sheet2!RESP_Total, Sheet2!INT_Total,
         Sheet2!CTRL_Total, Sheet2!REM_Total, Sheet2!AUD_Total)
```

#### 2. Conformidad NIS2 (ICN)

```
ICN = (# preguntas con score ≥3) / (Total preguntas) × 100%

Fórmula Excel (usando COUNTIF):
=COUNTIF(RAW_DATA!F:Z,">=3") / COUNTA(RAW_DATA!F:Z) × 100

O más precisamente (solo preguntas NIS2):
=COUNTIF({GR_P1:GR_P6, VUL_P1:VUL_P7, SIEM_P1:SIEM_P8, ...},">=3") / 
 COUNTA({GR_P1:GR_P6, VUL_P1:VUL_P7, SIEM_P1:SIEM_P8, ...}) × 100
```

#### 3. Nivel NIST CSF

```
NIST_Level = IGM × 6 / 30

Interpretación:
1.0 = Nivel 1 (Ad Hoc)
2.0 = Nivel 2 (Repeatable)
3.0 = Nivel 3 (Defined)
4.0 = Nivel 4 (Managed)
5.0 = Nivel 5 (Optimized)

Fórmula Excel:
=ROUND(Sheet3!IGM × 6 / 30, 1)
```

#### 4. ROICS (Retorno sobre Inversión en Ciberseguridad)

```
ROICS = (Beneficios Total 3 Años - Inversión Total 3 Años) / Inversión Total 3 Años × 100%

Desglose de Beneficios (ejemplo):
- Evitar brechas críticas: €400K × 3 años = €1,200K
- Mejora MTTR (automatización): €100K × 3 años = €300K
- Evitar multas NIS2 (0.5% potencial): €500K × 3 años = €1,500K
- Reducción incidentes: €160K × 3 años = €480K
Total Beneficios 3 años: €3,480K (conservador)

Desglose de Inversión (ejemplo):
- Año 1: €610K (herramientas, personal, training)
- Año 2: €710K (operacional)
- Año 3: €800K (madurez)
Total Inversión 3 años: €2,120K

ROICS = (€3,480K - €2,120K) / €2,120K × 100% = 64.15%

Fórmula Excel (simplificada):
=((Sheet4!Beneficios_Total - Sheet4!Inversion_Total) / Sheet4!Inversion_Total) × 100
```

#### 5. Payback Period

```
Payback = Costo Total Inicial / (Beneficio Anual Promedio)

Ejemplo:
Costo Año 1: €610K
Beneficio Año 1: €1,240K
Payback (Año 1): 610K / 1,240K = 0.49 años (~6 meses)

Si se extiende a 3 años:
Costo promedio anual: €2,120K / 3 = €707K
Beneficio promedio anual: €3,480K / 3 = €1,160K
Payback: €707K / €1,160K = 0.61 años

Fórmula Excel:
=Sheet4!Inversion_Inicial / Sheet4!Beneficio_Anual_Promedio
```

---

## SHEET 4: FINANCIAL (Análisis Financiero)

### Estructura

| Concepto | Año 1 | Año 2 | Año 3 | Total 3 años |
|---|---|---|---|---|
| **INVERSIONES** | | | | |
| Infraestructura (SIEM, FW) | €150K | €50K | €30K | €230K |
| Herramientas (escaneo, SOAR) | €50K | €30K | €20K | €100K |
| Personal (+1 FTE CISO, +1 analista) | €300K | €350K | €400K | €1,050K |
| Capacitación y servicios | €110K | €120K | €150K | €380K |
| Auditoría externa (anual) | €25K | €25K | €25K | €75K |
| Consultoría (GQM, AVRQ) | €20K | €10K | €5K | €35K |
| **TOTAL INVERSIÓN** | **€655K** | **€585K** | **€630K** | **€1,870K** |
| | | | | |
| **BENEFICIOS** | | | | |
| Evitar brechas críticas | €400K | €400K | €400K | €1,200K |
| Mejora MTTR (efficiency) | €100K | €150K | €150K | €400K |
| Evitar multas NIS2 | €500K | €500K | €0K | €1,000K |
| Reducción incidentes | €160K | €160K | €160K | €480K |
| Automación operacional | €30K | €50K | €100K | €180K |
| Confianza clientes | €50K | €100K | €150K | €300K |
| **TOTAL BENEFICIOS** | **€1,240K** | **€1,360K** | **€960K** | **€3,560K** |
| | | | | |
| **NET (Beneficios - Inversión)** | **€585K** | **€775K** | **€330K** | **€1,690K** |
| **ROICS (%)** | 89% | 133% | 52% | **90%** |
| **Payback Period (años)** | 0.53 | N/A | N/A | **1.32** |

### Fórmulas

```
TOTAL INVERSIÓN Año X:
=SUM(Infraestructura:Consultoría)

TOTAL BENEFICIOS Año X:
=SUM(Brechas:Confianza)

NET:
=TOTAL BENEFICIOS - TOTAL INVERSIÓN

ROICS:
=NET / TOTAL INVERSIÓN × 100%

Payback (si es año 1):
=TOTAL INVERSIÓN / TOTAL BENEFICIOS
```

---

## SHEET 5: DASHBOARD (Visualización)

### Gráficos Recomendados

#### 1. Gráfico Radar: IGM por Dominio

```
Tipo: Radar Chart (Gráfico de araña)
Datos: GR, VUL, SIEM, CAP, NORM, CONT, SUPL, RESP, INT, CTRL, REM, AUD
Series 1: Valores actuales (línea azul)
Series 2: Objetivos (línea naranja)
Eje Y: Escala 0-5
Insight: Identifica dominios con brecha
```

#### 2. Gráfico Barras: Conformidad NIS2 por Medida

```
Tipo: Horizontal Bar Chart
Datos: 21 medidas NIS2 vs % implementación
Colores: Verde (≥80%), Amarillo (60-80%), Rojo (<60%)
Insight: Visualiza brechas prioritarias
```

#### 3. Gráfico Líneas: Evolución ROICS 3 años

```
Tipo: Line Chart
Eje X: Meses (1-36)
Eje Y: Beneficio Acumulativo (€)
Series 1: Inversión acumulada
Series 2: Beneficios acumulados
Intersection = Payback Point
Insight: Justificación financiera
```

#### 4. Gráfico Pastel: Distribución de Inversión

```
Tipo: Pie Chart
Datos: Infraestructura, Personal, Herramientas, Otros
Insight: Dónde va el dinero
```

#### 5. Tarjetas de Métricas (KPIs principales)

```
Tarjeta 1: IGM = 3.2 / 5.0 (64%)
Tarjeta 2: Conformidad NIS2 = 68% / 80% (Brecha -12%)
Tarjeta 3: ROICS = 114% (Excelente)
Tarjeta 4: Payback = 1.4 años (Meta <2 años)
```

---

## SHEET 6: NIS2_ROADMAP (Plan de Conformidad)

### Estructura

| Medida NIS2 | Actual | Objetivo | Q1 | Q2 | Q3 | Q4 | Owner | Budget |
|---|---|---|---|---|---|---|---|---|
| 1. Risk Analysis | 40% | 100% | 60% | 80% | 100% | 100% | CISO | €15K |
| 2. Asset Inventory | 70% | 100% | 80% | 100% | 100% | 100% | Manager TI | €10K |
| 3. Access Control | 50% | 100% | 70% | 100% | 100% | 100% | CTO | €20K |
| ... | | | | | | | | |
| **TOTAL** | **35%** | **100%** | **60%** | **80%** | **95%** | **100%** | | **€230K** |

### Fórmulas

```
Hito Trimestral = (Objetivo - Actual) × % progreso + Actual

Q1 Progress: =Actual + (Objetivo - Actual) × 0.20
Q2 Progress: =Actual + (Objetivo - Actual) × 0.50
Q3 Progress: =Actual + (Objetivo - Actual) × 0.80
Q4 Progress: =Objetivo

Total Conformidad Trimestral:
=AVERAGE(Q1_Medida1:Q1_Medida21) para Q1, etc.
```

---

## SHEET 7: RECOMMENDATIONS (Acciones Prioritarias)

### Estructura

| Prioridad | Acción | Dominio | Impacto | Costo | Timeline | Owner | Status |
|---|---|---|---|---|---|---|---|
| 🔴 CRÍTICA | Implementar AVRQ | GR | Alto | €80K | 2 meses | CISO | Backlog |
| 🔴 CRÍTICA | Conformidad NIS2 | NORM | Alto | €150K | 3 meses | Compliance | In Progress |
| 🟠 ALTA | SIEM Tuning | SIEM | Medio | €120K | 2 meses | SOC Manager | Planned |
| 🟡 MEDIA | Capacitación Phishing | CAP | Bajo-Medio | €40K | Continuo | Training | In Progress |

### Cálculos

```
Prioridad automática basada en:
- Brecha regulatoria (NIS2 ≥1.0 = 🔴)
- PRAGMATIC Score (<3.5 = revisión)
- Costo-Beneficio (Beneficio/Costo ratio)

Fórmula:
=IF(AND(NIS2_Brecha>=1, PRAGMATIC_Score>=3.5), "🔴 CRÍTICA",
   IF(AND(NIS2_Brecha<1, PRAGMATIC_Score>=4), "🟠 ALTA",
   IF(PRAGMATIC_Score>=3.5, "🟡 MEDIA", "🟢 BAJA")))
```

---

## SHEET 8: DOCUMENTATION (Referencias y Notas)

### Contenido

```
Sección 1: Definiciones
- IGM: Índice Global de Madurez (promedio de 12 dominios)
- ICN: Índice Conformidad NIS2 (% de medidas implementadas)
- ROICS: Retorno sobre Inversión Ciberseguridad
- PRAGMATIC Score: Evaluación de métrica (1-5)

Sección 2: Metodología
- Fuentes de datos: RAW_DATA sheet
- Supuestos de beneficios: [enumerar]
- Factores de riesgo: [enumerar]

Sección 3: Contactos
- CISO: [Nombre] [Email] [Teléfono]
- CFO: [Nombre] [Email] [Teléfono]
- Data Analyst: [Nombre] [Email] [Teléfono]

Sección 4: Historial de Versiones
- v1.0: Enero 2026 - Creación inicial
- v1.1: Enero 2026 - Ajustes Q1

Sección 5: Referencias
- NIS2: https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- ISO 27001:2022: https://www.iso.org/standard/27001
- NIST CSF v2.0: https://www.nist.gov/cyberframework
```

---

## INSTRUCCIONES DE IMPLEMENTACIÓN

### Paso 1: Crear estructura base
```
1. Crear workbook Excel vacío
2. Renombrar sheets según nombres arriba
3. Crear encabezados y estructura básica
```

### Paso 2: Ingresar datos encuesta
```
1. Distribuir encuesta Mercury (112 preguntas)
2. Consolidar respuestas en RAW_DATA
3. Validar datos (scores 1-5)
```

### Paso 3: Configurar fórmulas
```
1. Sheet SCORING: copiar fórmulas de cálculo
2. Sheet METRICS: vincular a SCORING
3. Sheet FINANCIAL: ingresar datos costos/beneficios
4. Sheet NIS2_ROADMAP: definir hitos trimestrales
```

### Paso 4: Crear visualizaciones
```
1. Gráfico radar: Datos de METRICS
2. Gráfico barras: Datos de NIS2_ROADMAP
3. Gráfico líneas: Datos de FINANCIAL
4. Tabla de KPIs: Dashboard
```

### Paso 5: Validación y reviews
```
1. Revisar sumas y promedios
2. Validar fórmulas (sin circulares)
3. Cross-check vs. encuesta original
4. Presentar a CISO/CFO para validación
```

---

## MEJORES PRÁCTICAS

✓ **Bloquear celdas de fórmula** (evitar cambios accidentales)
✓ **Usar colores para códigos estado** (rojo/amarillo/verde)
✓ **Actualizar mensualmente** (para tracking progreso)
✓ **Backup automático** (Google Drive o OneDrive)
✓ **Permisos de lectura solo** para stakeholders (no edición)
✓ **Documentar supuestos** en hoja Documentation

---

**Fin de Plantilla Excel**

*Versión 2.0 | Enero 2026*