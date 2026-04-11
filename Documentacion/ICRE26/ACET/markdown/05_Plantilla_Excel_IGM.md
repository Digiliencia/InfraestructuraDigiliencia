# PLANTILLA EXCEL: CALCULADORA DE IGM Y ROI
## Especificaciones Técnicas para Implementación en Hoja de Cálculo

**Versión:** 2.0 | **Formato:** Microsoft Excel / Google Sheets | **Complejidad:** Intermedia

---

## 1. ESTRUCTURA GENERAL

La plantilla incluye **4 hojas principales**:

1. **INPUT** – Respuestas de encuesta (manual o importadas)
2. **SCORING** – Cálculo automático de IGM, dominios, KRIs/KPIs
3. **BENCHMARKING** – Comparativa vs. sector, territorio
4. **ROI_ANALYSIS** – Calculadora de retorno de inversión por control

---

## 2. HOJA 1: INPUT (Respuestas de Encuesta)

### Estructura de Columnas

```
| A | B | C | D | E | F |
|---|---|---|---|---|---|
| ID | Pregunta | Opciones | Respuesta | Puntos | Dominio |
```

### Filas: Ejemplo de 60 preguntas

```
Fila 1: Headers
├─ A1: "ID"
├─ B1: "Pregunta"
├─ C1: "Opciones"
├─ D1: "Respuesta"
├─ E1: "Puntos"
└─ F1: "Dominio"

Fila 2-5: BLOQUE I - GOBIERNO (GV)
├─ A2: "P1.1.1"
├─ B2: "¿Política de ciberseguridad formalizada?"
├─ C2: "Sí, Parcial, No, NA, DK"
├─ D2: [Desplegable con opciones]
├─ E2: [Fórmula: BUSCAR(D2, {...}, {...})] → automático calcula 100/50/0/excluido/25
└─ F2: "GV"

Fila 6-10: BLOQUE II - IDENTIFICAR (ID)
...
```

### Fórmula para Cálculo de Puntos (Columna E)

```excel
=IF(D2="Sí",100,IF(D2="Parcialmente",50,IF(D2="No",0,IF(D2="NA",NA(),IF(D2="DK",25,"")))))
```

O simplificado con SWITCH (Excel 365):

```excel
=SWITCH(D2,"Sí",100,"Parcialmente",50,"No",0,"NA",NA(),"DK",25,"")
```

### Validación de Datos en Columna D

```
Tipo: Lista
Fuente: Sí, Parcialmente, No, NA, DK
Permitir lista: SÍ
Mostrar alerta: SÍ
```

---

## 3. HOJA 2: SCORING (Cálculos Automáticos)

### 3.1 Resumen por Dominio (Tabla 5x6)

```
| Dominio | Preguntas | Promedio | Nivel | Benchm. | Gap |
|---------|-----------|----------|-------|---------|-----|
| GV | 4 | 75% | Intermediate | 78% | -3% |
| ID | 5 | 80% | Intermediate | 82% | -2% |
| PR | 20 | 70% | Evolving | 75% | -5% |
| DE | 8 | 65% | Evolving | 70% | -5% |
| RS | 10 | 72% | Intermediate | 71% | +1% |
| RC | 6 | 60% | Evolving | 68% | -8% |
```

### Fórmulas Cálculo Promedio por Dominio

**Celda B10 (Promedio GV):**

```excel
=AVERAGE(IF($F$2:$F$61="GV",$E$2:$E$61))
```

(Fórmula matriz: Ctrl+Shift+Enter en Excel)

O alternativo con AVERAGEIF:

```excel
=AVERAGEIF($F$2:$F$61,"GV",$E$2:$E$61)
```

**Celda C10 (Nivel de Madurez):**

```excel
=IF(B10>95,"Innovative",IF(B10>80,"Advanced",IF(B10>60,"Intermediate",IF(B10>40,"Evolving",IF(B10>20,"Baseline","Ad Hoc")))))
```

### 3.2 Cálculo IGM Global (Ponderado)

**Ubicación: Celda F12 "IGM Final"**

```excel
=SUMPRODUCT([Promedio_GV]*0.20, [Promedio_ID]*0.15, [Promedio_PR]*0.25, 
            [Promedio_DE]*0.15, [Promedio_RS]*0.15, [Promedio_RC]*0.10)
```

O manual con referencias:

```excel
=(B10*0.20)+(B11*0.15)+(B12*0.25)+(B13*0.15)+(B14*0.15)+(B15*0.10)
```

### 3.3 Cálculo de Índices Complementarios

**Celda F14: Vulnerability Assessment Score (VAS)**

```
Preguntas asociadas: 7.1.1, 7.1.2, 7.1.3, 7.2.1, 7.2.2, 7.3.1

=AVERAGE(Puntos_P7.1.1, Puntos_P7.1.2, Puntos_P7.1.3, 
         Puntos_P7.2.1, Puntos_P7.2.2, Puntos_P7.3.1)

Fórmula Excel:
=AVERAGEIFS($E$2:$E$61, $A$2:$A$61, "P7*")
```

**Celda F15: SIEM Effectiveness Score (SES)**

```
Preguntas asociadas: 8.1.1, 8.1.2, 8.1.3, 8.2.1, 8.2.2, 8.3.1, 8.4.1

=AVERAGE(E[8.1.1:8.4.1])

Con ponderación:
=(E_8.1.1*0.25 + E_8.2.1*0.35 + E_8.3.1*0.20 + E_8.4.1*0.20)
```

**Celda F16: Security Awareness Training Score (SATS)**

```
Preguntas asociadas: 9.1.1, 9.1.2, 9.2.1, 9.2.2, 9.3.1, 9.4.1

=(E_9.1.1*0.25 + E_9.2.1*0.35 + E_9.3.1*0.25 + E_9.4.1*0.15)
```

### 3.4 KRIs y KPIs (Extractos de Respuestas Específicas)

**Tabla KRIs (Cuadrante Abajo)**

```
| KRI | Pregunta Fuente | Valor Actual | Umbral Crítico | Estado |
|-----|-----------------|--------------|----------------|--------|
| % CVE Sin Parchear | P7.1.4 | 8% | >5% | ⚠️ CRÍTICO |
| Phish Click Rate | P9.2.1 | 18% | >20% | ✓ OK |
| Cobertura SIEM | P8.1.1 | 75% | <80% | ⚠️ ALERTA |
| MTTD | P4.2.1 | 240 min | >120 min | ⚠️ ALERTA |
| Controles No Evaluados | P2.2.2 | 12% | >10% | ⚠️ CRÍTICO |
```

**Fórmulas Ejemplo (KRI "Cobertura SIEM"):**

```excel
Celda A25: =Valor_Respuesta_P8.1.1
Celda B25: =IF(A25>80,"✓ OK", IF(A25>60,"⚠️ ALERTA","🔴 CRÍTICO"))
```

---

## 4. HOJA 3: BENCHMARKING

### 4.1 Tabla Comparativa

```
| Métrica | IGM Organización | Benchmark Sector | Benchmark Nacional | Diferencia |
|---------|-----------------|------------------|-------------------|-----------|
| IGM Global | 71% | 76% (Financiero) | 64% (Media ES) | -5% / +7% |
| Dominio GV | 75% | 78% | 70% | -3% / +5% |
| Dominio ID | 80% | 82% | 72% | -2% / +8% |
| Dominio PR | 70% | 75% | 68% | -5% / +2% |
| MTTD | 2h 15min | 1h 30min | 3h | -45min / +45min |
| SIEM Coverage | 75% | 85% | 65% | -10% / +10% |
```

**Origen de Datos Benchmark (Manual):**

```
Fila 1: Headers
Fila 2-7: Filas de datos

Métrica (A): NIST CSF Dominios + Métricas clave
IGM Org (B): Referencias a SCORING!B10:B15
Sector (C): Valores según tabla sector:
  - IF(Sector="Financiero", 76%, IF(Sector="Sanitario", 68%, ...))
Nacional (D): Promedio nacional España 2025 = 64%
Difer (E): =B-C (si negativo, estamos rezagados)
```

### 4.2 Visualización: Radar Chart

**Crear radar con datos:**

```
Categorías: GV, ID, PR, DE, RS, RC
Serie 1: Puntuaciones Organización (desde SCORING)
Serie 2: Benchmark Sector
Serie 3: Benchmark Nacional

Tipo Chart: XY Scatter con líneas conectadas (para simular radar)
O: Usar herramienta nativa si es Excel 2019+
```

---

## 5. HOJA 4: ROI_ANALYSIS

### 5.1 Tabla de Controles con ROI

```
| Control | Inversión | Beneficio Anual | Payback (meses) | ROI % | Prioridad |
|---------|-----------|-----------------|-----------------|-------|-----------|
| MFA | €45.000 | €60.000 | 9 | 33% | 1 |
| EDR | €120.000 | €200.000 | 7 | 67% | 2 |
| SIEM | €150.000 | €180.000 | 10 | 20% | 3 |
| Capacitación | €30.000 | €90.000 | 4 | 200% | 1 |
| Backups Automatizados | €25.000 | €75.000 | 4 | 200% | 1 |
| CISO Dedicado | €80.000 | €120.000 | 8 | 50% | 2 |
| Pentesting Anual | €40.000 | €120.000 | 4 | 200% | 1 |
```

### 5.2 Fórmulas ROI

**Celda C2: Beneficio Anual (Manual Input)**

```
Entrada: Usuario ingresa beneficio estimado (€)
Fuente: FAIR methodology
Ejemplo: MFA reduce riesgo de breach por compromiso credencial
  - Riesgo Original: 25% × €300K = €75K
  - Riesgo Residual: 5% × €300K = €15K
  - Beneficio: €75K - €15K = €60K
```

**Celda D2: Payback Period**

```excel
=IF(B2=0, 0, ROUND((B2/C2)*12, 1))

Explicación: (Inversión / Beneficio Anual) × 12 meses = Meses hasta recuperar inversión
```

**Celda E2: ROI %**

```excel
=IF(B2=0, 0, ROUND((C2-B2)/B2*100, 1))

Explicación: ((Beneficio - Inversión) / Inversión) × 100 = % retorno
```

**Celda F2: Prioridad**

```excel
=IF(E2>100, 1, IF(E2>50, 2, IF(E2>20, 3, 4)))

Lógica: ROI >100% = Prioridad 1, >50% = 2, >20% = 3, resto = 4
```

### 5.3 Matriz Impacto × Esfuerzo (Opcional)

```
Cuadrante 1 (Bajo Esfuerzo, Alto Impacto): IMPLEMENTAR YA
  - Capacitación
  - MFA básico
  - Pentesting

Cuadrante 2 (Alto Esfuerzo, Alto Impacto): PLANIFICAR
  - SIEM
  - EDR
  - Infrastructure modernization

Cuadrante 3 (Bajo Esfuerzo, Bajo Impacto): HACER CUANDO TENGAS TIEMPO
  - Documentación menor
  - Actualizaciones políticas

Cuadrante 4 (Alto Esfuerzo, Bajo Impacto): EVITAR
  - Redespliegues innecesarios
```

**Fórmula Impacto (1-5):**

```excel
Celda G2: =ROUND(VLOOKUP(A2, ControlImpactMatrix, 2, FALSE), 0)
```

**Fórmula Esfuerzo (1-5):**

```excel
Celda H2: =ROUND(VLOOKUP(A2, ControlEffortMatrix, 2, FALSE), 0)
```

---

## 6. HOJA 5: DASHBOARD (Resumen Ejecutivo)

### Layout Sugerido

```
┌────────────────────────────────────────────────┐
│          CYBERSECURITY MATURITY DASHBOARD       │
├─────────────────┬──────────────────────────────┤
│ IGM: 71%        │ Nivel: INTERMEDIATE          │
│ Cambio YTD: +3% │ Trend: ↗️ Positivo           │
├─────────────────┼──────────────────────────────┤
│ GV: 75%    ID: 80%    PR: 70%                 │
│ DE: 65%    RS: 72%    RC: 60%                 │
├─────────────────┼──────────────────────────────┤
│ MTTD: 2h 15min  │ MTTR: 6h 30min              │
│ VAS: 72%        │ SES: 68%        SATS: 75%   │
├─────────────────┼──────────────────────────────┤
│ Top 3 Brechas:  │ Presupuesto Sugerido:       │
│ 1. RC (60%)     │ €150K (año 1)               │
│ 2. DE (65%)     │ ROI esperado: 45%           │
│ 3. PR (70%)     │ Payback: 8 meses            │
└────────────────┴──────────────────────────────┘
```

### Elementos del Dashboard

**Medidor IGM (Gauge Chart):**

```
Rango Colores:
- 0-40%: Rojo 🔴
- 40-60%: Amarillo 🟡
- 60-80%: Verde Claro 🟢
- 80-100%: Verde Oscuro 🟢🟢
```

**Gráfico Radar:**

- Series: IGM Actual, Target, Benchmark
- Categorías: GV, ID, PR, DE, RS, RC

**Tabla KRIs:**

- Mostrar top 5 KRIs con alertas (rojo/amarillo/verde)

---

## 7. VALIDACIÓN DE DATOS

### Checks Automáticos (Sheet: VALIDATION)

```excel
Celda A1: =COUNTBLANK($D$2:$D$61)
Interpretación: Si >10 respuestas vacías, ALERTA

Celda B1: =COUNTIF($D$2:$D$61,"DK")/COUNTA($D$2:$D$61)
Interpretación: Si >10% DK, penalizar IGM

Celda C1: =COUNTIF($E$2:$E$61,NA())
Interpretación: Contar NA (preguntas no aplicables)
```

### Regla: Descuento por DK

```excel
IGM_Ajustado = IGM_Inicial - (# DK sin validar × 0.5%)
```

---

## 8. EJEMPLO DE CÁLCULO MANUAL (Para Validar Fórmulas)

### Escenario: 4 Preguntas GV, 1 Respuesta Cada Una

```
P1.1.1: Sí              → 100 pts
P1.1.2: Parcialmente    → 50 pts
P1.1.3: Sí              → 100 pts
P1.1.4: No              → 0 pts

Promedio GV = (100+50+100+0) / 4 = 62,5%

Asignación Nivel: 62,5% está en rango 60-80% = "Intermediate"
```

### Cálculo IGM con 6 Dominios (Hipotético)

```
GV: 75% × 0,20 = 15 puntos
ID: 80% × 0,15 = 12 puntos
PR: 70% × 0,25 = 17,5 puntos
DE: 65% × 0,15 = 9,75 puntos
RS: 72% × 0,15 = 10,8 puntos
RC: 60% × 0,10 = 6 puntos

IGM = 15+12+17,5+9,75+10,8+6 = 71,05%
Nivel = "Intermediate" (entre 60-80%)
```

---

## 9. INSTRUCCIONES DESCARGA E IMPLEMENTACIÓN

### Opción A: Microsoft Excel

1. Crear libro nuevo (Excel 2016+)
2. Copiar estructura de 5 hojas
3. Importar fórmulas desde templates
4. Probar con datos de ejemplo
5. Validar cálculos manuales vs. fórmulas

### Opción B: Google Sheets

1. Crear Google Sheet nuevo
2. Compartir estructura similar
3. Usar ARRAYFORMULA para cálculos dinámicos
4. Ventaja: Colaborativo, sincronización en tiempo real

### Opción C: Power BI / Tableau

1. Conectar a base de datos respuestas
2. Crear visualizaciones interactivas
3. Dashboards en tiempo real
4. Más robusto para organizaciones grandes

---

## 10. EXPORTACIÓN DE RESULTADOS

### Generación de Reporte Automático

```
Encabezado: Nombre Org, Fecha Encuesta, Respondentes
Secciones:
1. IGM Resumen (Gauge)
2. Radar NIST CSF
3. Tabla Benchmarking
4. KRIs Críticos
5. Roadmap Recomendado (de ROI_Analysis)
6. Apéndice: Respuestas Detalladas
```

**Generación:** Macro VBA que exporta a PDF

```vba
Sub ExportarReporte()
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("DASHBOARD")
    ws.PrintOut ToFile:="IGM_Reporte_[Fecha].pdf"
End Sub
```

---

**Esta plantilla proporciona estructura completa para transformar respuestas de encuesta en análisis cuantitativos profesionales.**

