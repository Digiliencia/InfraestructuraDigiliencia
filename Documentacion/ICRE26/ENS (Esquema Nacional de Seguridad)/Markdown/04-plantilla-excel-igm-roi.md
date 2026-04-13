# PLANTILLA EXCEL: CÁLCULO IGM Y ROI
## Sistema Integral de Métricas - Implementación en Hoja de Cálculo

---

## INSTRUCCIONES DE USO

Esta plantilla está diseñada para Microsoft Excel / Google Sheets. Contiene:
1. **Hoja 1: Consolidación de Respuestas**
2. **Hoja 2: Cálculo de IGM**
3. **Hoja 3: Análisis ROI**
4. **Hoja 4: Dashboard Ejecutivo**

---

## HOJA 1: CONSOLIDACIÓN DE RESPUESTAS

### Estructura

```
| Pregunta | Sección | Tema | Respondente_CISO | Respondente_Cumplimiento | Respondente_Auditoría | Media_Ponderada | Peso |
|----------|---------|------|---|---|---|---|---|
| P1 | I | Información Org | - | - | - | - | - |
| P2 | I | Sector | Opción: Energía | Opción: Energía | Opción: Energía | N/A | - |
| P3 | I | Tamaño | 3 (Mediana) | 3 | 3 | 3,0 | 0% |
| P6 | II | Política Seguridad | 4 | 4 | 3 | 3,67 | 5% |
| P7 | II | Objetivos | 3 | 4 | 2 | 3,0 | 5% |
| ... | ... | ... | ... | ... | ... | ... | ... |
| P114 | XI | Tech Emergentes | 3 | 3 | 3 | 3,0 | 1% |
```

### Fórmulas en Hoja 1

**Columna: Media_Ponderada (para preguntas numéricas)**

```excel
=SI(CONTAR(C4:E4)>0, 
    (C4*0,40 + D4*0,20 + E4*0,20) / SI(CONTAR(C4:E4)>0, CONTAR(C4:E4), 1),
    "")
```

**Lógica:**
- CISO (Col C): peso 40%
- Cumplimiento (Col D): peso 20%
- Auditoría (Col E): peso 20%
- Otras areas (si aplica): weights distribuidos

---

## HOJA 2: CÁLCULO DE IGM

### Estructura de Cálculo

```
| Dominio | Pregunta | Puntuación | Peso_Dominio | Contribución |
|---------|----------|-----------|--------------|--------------|
| **Marco Organizativo** | | | **20%** | |
| | P6 | 3,67 | 5% | 0,183 |
| | P7 | 3,0 | 5% | 0,150 |
| | P8 | 2,0 | 5% | 0,100 |
| | P9 | 4,0 | 5% | 0,200 |
| | P10 | 4,0 | 0% | 0,000 |
| | P11 | 3,5 | 0% | 0,000 |
| | P12 | 2,5 | 0% | 0,000 |
| | P13 | 4,0 | 0% | 0,000 |
| | P14 | 3,0 | 0% | 0,000 |
| | P15 | 3,5 | 0% | 0,000 |
| | P16 | 2,5 | 0% | 0,000 |
| **Subtotal Marco Organizativo** | | | | **0,633** |
| | | | | |
| **Marco Operacional** | | | **25%** | |
| | P17-P35 | [Promedio] | 25% | [Cálculo] |
| **Subtotal Marco Operacional** | | | | [Valor] |
| | | | | |
| ... [Dominios 3-6] | | | | |
| | | | | |
| **IGM TOTAL** | | | **100%** | **[Suma Total]** |
```

### Fórmula Principal IGM (Hoja 2, celda global)

```excel
=SUMAPRODUCTO(
  Hoja1!Dominio1_Puntos, Hoja1!Pesos1) +
  SUMAPRODUCTO(Hoja1!Dominio2_Puntos, Hoja1!Pesos2) +
  ... etc
  
=REDONDEAR(
  (SubTotal_MO * 0,20 + SubTotal_MOP * 0,25 + SubTotal_MP * 0,20 + 
   SubTotal_Incidentes * 0,15 + SubTotal_Capacitacion * 0,10 + 
   SubTotal_Gobernanza * 0,10) / 100,
  2)
```

### Interpretación IGM

```
SI(IGM < 2,0, "CRÍTICO", 
SI(IGM < 3,0, "INSUFICIENTE",
SI(IGM < 3,5, "BÁSICO",
SI(IGM < 4,3, "AVANZADO",
"EXCELENCIA"))))
```

---

## HOJA 3: ANÁLISIS ROI

### 3.1 Inputs Financieros

```
| Métrica | Valor | Fórmula/Fuente |
|---------|-------|---|
| **INVERSIÓN** | | |
| Gasto anual actual ciberseguridad (P105) | 150.000€ | INPUT |
| Inversión adicional recomendada (12 meses) | 75.000€ | 50% del presupuesto actual |
| Personal CISO/Seguridad | 120.000€ | P105 desglose |
| Herramientas/Software | 35.000€ | Estimado |
| Servicios externos (auditoría, penetración) | 20.000€ | Estimado |
| **TOTAL INVERSIÓN 2026** | **225.000€** | Suma |
| | | |
| **BENEFICIOS PROYECTADOS** | | |
| Costo promedio actual incidente (P107) | 45.000€ | INPUT |
| Número incidentes actual/año (P51) | 8 | INPUT |
| Costo actual incidentes/año | 360.000€ | 8 × 45K |
| | | |
| Reducción incidentes esperada (mejora madurez 3,2→4,0) | 40% | Benchmarking |
| Incidentes evitados/año | 3,2 | 8 × 40% |
| Costo evitado/año | 144.000€ | 3,2 × 45K |
| | | |
| Reducción costo por incidente (mejor respuesta) | 15% | MTTR mejora |
| Costo reducción/incidente | 6.750€ | 45K × 15% |
| Beneficio reducción por incidente | 54.000€ | 8 × 6.75K |
| | | |
| **BENEFICIO TOTAL ANUAL (Año 1)** | **198.000€** | 144K + 54K |
| Beneficio sostenible (Años 2+) | 250.000€ | Consolidado |
```

### 3.2 Métricas ROI

```
**ROI Simple (Año 1):**
ROI = (Beneficio - Inversión) / Inversión × 100
    = (198.000 - 225.000) / 225.000 × 100
    = -12% (Año 1 puede ser negativo, esperado)

**ROI Acumulado (Años 1-3):**
Año 1: -27.000€
Año 2: +250.000€ (beneficio sostenible)
Año 3: +250.000€

Acumulado 3 años: 473.000€
ROI promedio anual: (473.000 / 675.000) = 70%

**Payback Period:**
PaybackPeriod = Inversión / Beneficio_Anual
              = 225.000 / 250.000
              = 0,9 años ≈ 11 meses (año 2)

**NPV (Valor Presente Neto, tasa descuento 10%):**
NPV = -225.000 + (198.000/1,10^1) + (250.000/1,10^2) + (250.000/1,10^3)
    = -225.000 + 180.000 + 206.612 + 187.829
    = 349.441€

**IRR (Tasa Interna de Retorno):**
IRR = 34% (aproximadamente, usando análisis iterativo)
```

### 3.3 Análisis de Sensibilidad

```
| Escenario | Reducción Incidentes | Costo Evitado | ROI Año 1 | ROI 3 años |
|-----------|---------------------|--------------|-----------|-----------|
| **Pesimista** (20% reducción) | 1,6 | 72.000€ | -65% | 18% |
| **Base** (40% reducción) | 3,2 | 144.000€ | -12% | 70% |
| **Optimista** (60% reducción) | 4,8 | 216.000€ | 41% | 122% |
```

---

## HOJA 4: DASHBOARD EJECUTIVO

### Indicadores Clave

```
╔════════════════════════════════════════════════════════════════╗
║                    CUADRO DE MANDO 2026                       ║
║                   Postura de Ciberseguridad                   ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  IGM Actual               [3,47]              META: 4,0        ║
║  █████████░░░░░░░░░░░░░░ 69% hacia meta      (0,53 pts)       ║
║                                                                ║
║  Dominio de Mayor Brecha: Marco Operacional (2,8 vs 4,0)      ║
║  Dominio de Fortaleza: Gobernanza (4,1)                       ║
║                                                                ║
║  Conformidad ENS:         78%                                  ║
║  Conformidad NIST CSF:    72%                                  ║
║  Conformidad NIS2:        65% (Operador Esencial)             ║
║                                                                ║
║  MTTD Actual:             48 horas         Meta: <24h          ║
║  MTTR Actual:             6 horas          Meta: <4h           ║
║                                                                ║
║  Incidentes año anterior: 8                Tendencia: +16%     ║
║  Tasa exposición datos:   1 incidente      Meta: 0             ║
║                                                                ║
║  Inversión Recomendada:   75.000€/año      ROI Año 1: -12%     ║
║  Payback Period:          11 meses         NPV 3 años: 349K€   ║
║                                                                ║
║  Capacitación Anual:      64%              Meta: 100%          ║
║  Tasa Clics Phishing:     18%              Meta: <10%          ║
║                                                                ║
║  ⚠️  ACCIONES INMEDIATAS:                                       ║
║     1. Implementar SIEM (P69: 1→4, impacto MTTD)              ║
║     2. Programa 100% capacitación (P80: 64%→100%)             ║
║     3. Auditoría externa anual (P101: no→sí)                  ║
║     4. Escalada a Consejo: Presupuesto + Gobernanza           ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
```

### Gráficos Recomendados

1. **Radar Chart (Madurez por Dominio)**
   - Eje: 6 dominios ENS (Marco Org, Operacional, etc.)
   - Valor: Puntuación IGM por dominio (1-5)

2. **Línea de Tendencia (Histórica)**
   - Eje X: Trimestres (Q1 2024 - Q4 2026)
   - Eje Y: IGM (1-5)
   - Mostrar proyección con inversión recomendada

3. **Waterfall (ROI Cálculo)**
   - Inversión (barra negativa)
   - Beneficios direc (barra positiva)
   - Beneficios indirectos (reputación, etc.)
   - ROI Total

---

## FÓRMULAS EXCEL CLAVE

### Validación de Datos

```excel
=CONTAR.SI(Hoja1!C6:C114, "<1") + CONTAR.SI(Hoja1!C6:C114, ">5")
```
Alerta si hay respuestas fuera rango 1-5

### Cálculo Media Móvil (si datos históricos)

```excel
=PROMEDIO(OFFSET(IGM_Actual, -12, 0, 12, 1))  ; Media últimos 12 meses
```

### Cálculo Desviación Estándar

```excel
=DESVEST(C6:C114)  ; Identifica inconsistencias entre respondentes
```

### Indicador Semáforo

```excel
=SI(IGM < 2, "🔴", SI(IGM < 3, "🟠", SI(IGM < 3.5, "🟡", SI(IGM < 4.3, "🟢", "🟢✓"))))
```

---

## PROTECCIÓN DE HOJA

Recomendaciones:
1. **Proteger Hojas 2-4** con contraseña (cálculos no editables)
2. **Permitir edición** solo en Hoja 1 (entrada de datos)
3. **Hacer backup** antes de cada ciclo de encuesta
4. **Control de versiones** (Excel: Archivo → Información → Versiones)

---

## EXPORTACIÓN DE DATOS

### A PowerPoint (Automatizado)

```vbscript
' Macro VBA para exportar tablas a PowerPoint
Sub ExportarAPowePoint()
    ' Copiar rango de datos
    ' Pegar en presentación PowerPoint via OLE
End Sub
```

### A PDF

```
Archivo → Exportar → PDF
- Seleccionar rango IGM Dashboard
- Mantener formato
- Nombre: IGM_Org_2026.pdf
```

---

## ACTUALIZACIÓN TRIMESTRAL

Cada trimestre (Q1, Q2, Q3, Q4):
1. Completar Hoja 1 con datos nuevos
2. Recalcular IGM automáticamente (Hoja 2)
3. Actualizar gráficos (automático)
4. Generar reporte ejecutivo (Hoja 4)
5. Distribuir a stakeholders

---

**Versión:** 1.0  
**Compatibilidad:** Excel 2019+, Google Sheets, LibreOffice Calc  
**Última actualización:** 24 enero 2026
