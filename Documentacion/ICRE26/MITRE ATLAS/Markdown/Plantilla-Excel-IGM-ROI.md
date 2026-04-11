# PLANTILLA EXCEL: CÁLCULO IGM (ÍNDICE GESTIÓN MADUREZ) + ROI
## Hoja de cálculo para implementación indicadores MITRE ATLAS

**Versión:** 1.0  
**Formato:** Descripción Markdown (implementable en Excel/Google Sheets)  
**Clasificación:** Público - Operacional

---

## INTRODUCCIÓN

Esta plantilla permite **calcular automáticamente:**
1. **IGM (Índice de Gestión de Madurez):** Score 0-100 ciberseguridad IA
2. **ROI (Return on Investment):** Impacto económico inversión seguridad
3. **Benchmarking:** Posición vs. pares sectoriales
4. **Trendline:** Evolución madurez trimestral/anual

---

## ESTRUCTURA PLANTILLA EXCEL

### HOJA 1: "INPUT_Respuestas"

Recolecta respuestas encuesta (escala 1-5) para 13 módulos:

```
Columnas: 
A: Empresa
B: Sector (Financiero/Manufactura/Telecom/Salud/Energía/Defensa/Educación)
C: Tamaño (PYME/Mediana/Grande)
D-P: Módulos 1-13 (escala 1-5 respuestas)

Fila 1: Encabezados
Fila 2+: Datos por organización

Ejemplo:
| Empresa | Sector | Tamaño | M1_Gov | M2_Map | M3_Vuln | M4_Prot | M5_SIEM | M6_Resp | M7_Acceso | M8_ATLAS | M9_Sumini | M10_Regul | M11_Train | M12_BCP | M13_RIA |
|---------|--------|--------|--------|--------|---------|---------|---------|---------|----------|----------|-----------|-----------|----------|---------|---------|
| BancoX | Financiero | Grande | 4 | 4 | 3 | 5 | 4 | 4 | 4 | 3 | 3 | 5 | 4 | 5 | 4 |
| ManuY | Manufactura | Mediana | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 1 |
```

### HOJA 2: "IGM_CALCULO"

**Fórmula Principal IGM:**

```
IGM = [(M1 + M2 + M3 + M4 + M5 + M6 + M7 + M8 + M9 + M10 + M11 + M12 + M13) / (13 × 5)] × 100
```

**Implementación Excel:**
```
Columna A: Empresa
Columna B: IGM_Score = (SUM(D2:P2) / 65) * 100
Columna C: IGM_Categoría = IF(B2 >= 80, "Muy Fuerte", IF(B2 >= 60, "Fuerte", IF(B2 >= 40, "Moderado", "Débil")))
Columna D: Percentil = PERCENTRANK(IGM_Score, $B$2:$B$100)
Columna E: Brecha_vs_Mediana = B2 - MEDIAN($B$2:$B$100)
```

**Tabla Conversión Scores:**

| IGM Score | Categoría | Características | Acción Recomendada |
|-----------|-----------|-----------------|-------------------|
| 81-100 | **Muy Fuerte** | Defensas maduras, detección continua, gobernanza excelente | Mantener + mejorar eficiencia |
| 61-80 | **Fuerte** | Defensas operativas, plan mejora en progreso | Acelerar roadmap |
| 41-60 | **Moderado** | Defensas básicas, brechas identificadas | Acción urgente (12 meses) |
| 21-40 | **Débil** | Defensas insuficientes, riesgos críticos | Acción inmediata (3-6 meses) |
| 0-20 | **Crítico** | Sin defensas significativas | Intervención reguladora |

### HOJA 3: "SUB_SCORES"

Calcula scores por función NIST CSF:

```
Estructura:
Columna A: Empresa
Columna B: GOVERN = AVERAGE(M1, M2, M3) → Score 0-100
Columna C: MAP = AVERAGE(M4, M5) → Score 0-100
Columna D: MEASURE = AVERAGE(M6, M7, M8) → Score 0-100
Columna E: MANAGE = AVERAGE(M9, M10) → Score 0-100
Columna F: Función Débil = MIN(B:E) → Identifica área prioritaria

Fórmulas:
B2: =AVERAGE(D2:F2)*20 (normalize 1-5 scale a 0-100)
C2: =AVERAGE(G2:H2)*20
D2: =AVERAGE(I2:K2)*20
E2: =AVERAGE(L2:M2)*20
F2: =SMALL(B2:E2, 1) (encuentra score más bajo)
```

| Función NIST | Módulos Inclusos | Score Cálculo | Interpretación |
|--------------|-----------------|---------------|-----------------|
| **GOVERN** | M1, M2, M3 (Gov, Policies, Presupuesto) | Average × 20 | Gobernanza + visión estratégica |
| **MAP** | M4, M5 (Assets, Vulns) | Average × 20 | Conocimiento riesgos |
| **MEASURE** | M6, M7, M8 (SIEM, IRP, Acceso) | Average × 20 | Detección + monitoreo |
| **MANAGE** | M9, M10 (ATLAS, Supply chain) | Average × 20 | Respuesta + resiliencia |

### HOJA 4: "BENCHMARKING"

Comparativa vs. pares (por sector + tamaño):

```
Columnas:
A: Empresa
B: IGM_Score (from Hoja 2)
C: Sector
D: Tamaño
E: Percentil_Sector = PERCENTRANK(IF($C$2:$C$100=C2, $B$2:$B$100))
F: Mediana_Sector = MEDIAN(IF($C$2:$C$100=C2, $B$2:$B$100))
G: Brecha_Mediana = B2 - F2
H: Top3_Pares = Concatenar empresas score similar ±5
I: Oportunidad = IF(G2 < 0, "Mejorar", "Liderazgo")

Tabla Resultado:
| Empresa | IGM | Sector | Tamaño | Percentil | Mediana Sector | Brecha | Status |
|---------|-----|--------|--------|-----------|----------------|--------|--------|
| BancoX | 75 | Financiero | Grande | P75 | 68 | +7 | Liderazgo |
| ManuY | 38 | Manufactura | Mediana | P25 | 45 | -7 | Mejora Urgente |
```

### HOJA 5: "CÁLCULO_ROI"

**Impacto económico inversión seguridad IA:**

```
Inputs:
A: Empresa
B: IGM_Actual = Current score
C: IGM_Target = Objetivo (ej. 70)
D: Inversión_Anual = Budget seguridad IA (€)
E: Ingresos_Org = Revenue anual (€)
F: % Exposición = % revenue en sistemas IA
G: Costo_Incidente_Promedio = Average incident cost (€)
H: Probabilidad_Incidente_Actual = Risk probability current
I: Probabilidad_Incidente_Meta = Risk probability post-mejora

Fórmulas Cálculo ROI:

Exposición Riesgo (€):
J: = E × F × G (valor en riesgo)

Reducción Riesgo (probabilidad):
K: = H - I (mejora probabilidad)

Impacto Económico:
L: = J × K (€ ahorrados por reducción riesgo)

ROI (%):
M: = (L - D) / D × 100

Payback Period (meses):
N: = IF(L > 0, (D / L) × 12, ">24")

Tabla Salida ROI:
| Empresa | Budget IA | Ingresos | Risk Exposure (€) | Reduction Prob | Economic Impact (€) | ROI (%) | Payback (meses) |
|---------|-----------|----------|------------------|----------------|---------------------|---------|-----------------|
| BancoX | €500k | €2.5B | €500M | 15% | €75M | 14,900% | 0.8 |
| ManuY | €50k | €150M | €15M | 20% | €3M | 5,900% | 0.2 |
```

**Interpretación ROI:**
- **ROI > 1000%:** Inversión altamente rentable (típico ciberseguridad)
- **Payback < 1 mes:** Recuperación casi inmediata
- **Economic Impact >> Budget:** Justificación inversión clara

### HOJA 6: "TRENDLINE_ANUAL"

Seguimiento evolución madurez (trimestral/anual):

```
Estructura Temporal:
Filas: Empresas
Columnas: 
A: Empresa
B: IGM_Q1_2026
C: IGM_Q2_2026
D: IGM_Q3_2026
E: IGM_Q4_2026
F: Mejora_Anual = E - B
G: Tasa_Mejora_Trimestral = AVERAGE(Diferencias trimestrales)
H: Proyección_2027 = E + (G × 4)
I: En_Track_vs_Meta = IF(H >= Meta_2027, "Sí", "No")

Gráfico Recomendado:
- Línea con marcadores por trimestre
- Línea meta (ej. 70/100) como referencia
- Sombreado verde (arriba meta) / rojo (abajo meta)

Tabla Trendline:
| Empresa | Q1_2026 | Q2_2026 | Q3_2026 | Q4_2026 | Mejora_Anual | Proyección_2027 | Track? |
|---------|---------|---------|---------|---------|--------------|-----------------|--------|
| BancoX | 65 | 68 | 71 | 75 | +10 | 85 | Sí |
| ManuY | 35 | 38 | 40 | 42 | +7 | 56 | No |
```

### HOJA 7: "INDICADORES_ATLAS_DETALLE"

Desagregación de 24 métricas ATLAS (M1.1-M4.5):

```
Estructura:
Fila 1: Encabezados
Columnas:
A: Question (Q1-Q4)
B: Métrica (M#.#)
C: Nombre Métrica
D: Fórmula
E: Valor_Medido
F: Unidad
G: Target_2026
H: Target_2027
I: Gap_Actual
J: Priority (Alta/Media/Baja)

Implementación:
E2: =IF(C2="M1.1", COUNTIF(Incidentes, Táctica) / Count(Total), ...)
G2: =IF(C2="M3.1", 4, IF(C2="M1.1", 0.8, ...)) (targets por métrica)
I2: =E2 - G2 (diferencia vs. objetivo)

Tabla Indicadores:
| Q | M | Nombre | Valor | Unidad | Target 26 | Gap | Priority |
|---|---|--------|-------|--------|-----------|-----|----------|
| Q1 | M1.1 | Prev Tácticas | 45% | % | 80% | -35% | Alta |
| Q2 | M2.1 | Score Madurez | 65 | 0-100 | 70 | -5 | Alta |
| Q3 | M3.1 | MTTD | 6.2 | horas | 4 | +2.2 | Alta |
| Q4 | M4.1 | Conformidad AI Act | 72% | % | 90% | -18% | Alta |
```

### HOJA 8: "DASHBOARD_EJECUTIVO"

Resumen visual para boards:

```
Estructura Recomendada (para exportar PowerPoint):

Sección 1: KPI's Clave (grandes números)
- IGM Score General: [Score_Actual]/100
- Empresas Críticas: [Count < 40]/[Total]
- MTTD Promedio: [MTTD_avg] horas
- Conformidad Regulatoria: [% Conformidad]%

Sección 2: Gráficos
- Pie Chart: Distribución scores (Verde >80, Amarillo 60-80, Rojo <60)
- Bar Chart: IGM por sector (comparativa)
- Línea: Trendline IGM últimos 4 trimestres
- Scatter: ROI vs. IGM (identificar outliers)

Sección 3: Tablas Resumen
- Top 5 Orgs (liderazgo)
- Bottom 5 Orgs (intervención)
- Brechas Principales (por función NIST)
- Recomendaciones Top-3 (acciones más impactantes)

Fórmulas Agregadas:
IGM_Promedio = AVERAGE(B2:B500)
Median_IGM = MEDIAN(B2:B500)
Std_Deviation = STDEV(B2:B500)
% Crítico = COUNTIF(B2:B500, "<40") / COUNT(B2:B500)
```

---

## GUÍA IMPLEMENTACIÓN PASO A PASO

### Paso 1: Configurar Datos Base
1. Crear archivo Excel/Google Sheets
2. Hoja 1 "INPUT": Copiar respuestas encuesta (escala 1-5)
3. Validar rango datos (no blancos, valores 1-5)

### Paso 2: Generar Scores
1. Ir Hoja 2 "IGM_CALCULO"
2. Copiar fórmula IGM = (SUM/65)*100 en columna B
3. Extender a todas filas (Ctrl+D)
4. Verificar scores 0-100 rango

### Paso 3: Benchmarking
1. Filtrar Hoja 4 por sector
2. Calcular percentiles (PERCENTRANK)
3. Identificar gaps vs. mediana

### Paso 4: ROI Analysis
1. Ingresar presupuesto + revenue (Hoja 5)
2. Estimar % exposición sistemas IA
3. Calcular ROI automático

### Paso 5: Dashboard
1. Crear gráficos (Charts → Data → Format)
2. Enlazar a Hoja 8 Dashboard
3. Configurar refresh automático (Data → Query)

---

## VALIDACIONES + CONTROLES DE CALIDAD

```
Validación 1: Rango Datos
IF(OR(D2:P2 < 1, D2:P2 > 5), ERROR "Valor fuera rango 1-5", OK)

Validación 2: Sin Blancos
IF(COUNTBLANK(D2:P2) > 0, ERROR "Datos faltantes", OK)

Validación 3: Inconsistencia Lógica
IF(M6_SIEM = 1 AND M3_1_MTTD < 8, WARNING "SIEM inexistente pero MTTD bajo?")

Validación 4: Sesgo Sector
IF(PERCENTILE(B2:B100, 10) = PERCENTILE(B2:B100, 90), 
   WARNING "Mala distribución datos sector")
```

---

## EXPORTACIÓN + REPORTES AUTOMATIZADOS

**Generar reporte automatizado:**

```
Power Query / Google Sheets Script:
1. Query datos INPUT
2. Calcular IGM + ROI
3. Filtrar por sector/tamaño/percentil
4. Generar tablas + gráficos
5. Exportar PDF con formatos automáticos

Salida estándar:
- Cover page (logo + fecha)
- Executive summary (KPI's clave)
- Tablas detalladas (todas empresas/sectores)
- Gráficos benchmarking
- Recomendaciones personalizadas por org
- Apéndices (metadatos + metodología)
```

---

## DESCARGA + IMPLEMENTACIÓN

**Archivo Excel referencia:**
```
Nombre: Plantilla_IGM_ROI_ATLAS_2026.xlsx
Hojas: 8 (INPUT, CALCULO, SUBSCORE, BENCHMARK, ROI, TRENDLINE, DETALLE, DASHBOARD)
Tamaño: ~500 filas, 30 columnas
Compatible: Excel 2016+, Google Sheets, LibreOffice
```

**Próximos pasos:**
1. Descargar plantilla
2. Completar Hoja 1 "INPUT" con respuestas encuesta
3. Ejecutar macros / refresh queries
4. Exportar resultados dashboard
5. Presentar a stakeholders con gráficos automáticos

---

**Documento preparado:** Enero 2026  
**Clasificación:** Público - Operacional  
**Versión:** 1.0 (baseline implementación)

