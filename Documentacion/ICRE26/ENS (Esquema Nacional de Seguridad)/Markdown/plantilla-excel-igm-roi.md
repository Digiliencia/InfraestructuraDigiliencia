# PLANTILLA EXCEL: CÁLCULO IGM Y ROI
## Sistema Integral de Gestión de Métricas - Implementación Funcional

---

## DESCRIPCIÓN GENERAL

Esta plantilla Excel contiene **4 hojas de trabajo** interconectadas para:

1. **Consolidar respuestas** de múltiples respondentes (ponderadas)
2. **Calcular IGM automáticamente** (Índice Gestión Madurez 1.0-5.0)
3. **Analizar ROI** cuantificado (Año 1-3, NPV, IRR, Payback)
4. **Generar Dashboard Ejecutivo** (gráficos, KPIs, alertas)

---

## HOJA 1: CONSOLIDACIÓN DE RESPUESTAS

### Estructura

```
Columnas:
├─ A: Número Pregunta (P1-P114)
├─ B: Sección (I-XI)
├─ C: Tema
├─ D: Respondente CISO (1-5)
├─ E: Respondente Cumplimiento (1-5)
├─ F: Respondente Auditoría (1-5)
├─ G: Respondente Ejecutivo (1-5)
├─ H: Respondente RRHH (1-5)
├─ I: Media Ponderada (fórmula)
└─ J: Peso Dominio (%)
```

### Fórmula Media Ponderada

```excel
=SI(CONTAR(D2:H2)>0,
  (D2*0,40 + E2*0,20 + F2*0,20 + G2*0,1 + H2*0,1),
  "")
```

**Pesos:**
- CISO: 40% (mayor expertise técnica)
- Cumplimiento: 20% (perspectiva regulatoria)
- Auditoría: 20% (validación independiente)
- Ejecutivo: 10% (perspectiva negocio)
- RRHH: 10% (concienciación)

### Validación

```excel
=SI(O(D2<1;D2>5;E2<1;E2>5;F2<1;F2>5),"⚠️ ERROR RANGO";I2)
```

---

## HOJA 2: CÁLCULO IGM

### Estructura por Dominio

```
DOMINIO 1: Marco Organizativo (20% peso)
├─ P6-P16: 11 preguntas
├─ Puntuación promedio dominio: =PROMEDIO(I6:I16)
└─ Contribución: =Puntuación × 0,20

DOMINIO 2: Marco Operacional (25% peso)
├─ P17-P35: 19 preguntas
├─ Puntuación promedio dominio: =PROMEDIO(I17:I35)
└─ Contribución: =Puntuación × 0,25

DOMINIO 3: Medidas Protección (20% peso)
├─ P36-P50: 15 preguntas
├─ Puntuación promedio dominio: =PROMEDIO(I36:I50)
└─ Contribución: =Puntuación × 0,20

DOMINIO 4: Incidentes (15% peso)
├─ P46-P68: 23 preguntas
├─ Puntuación promedio dominio: =PROMEDIO(I46:I68)
└─ Contribución: =Puntuación × 0,15

DOMINIO 5: Capacitación (10% peso)
├─ P79-P94: 16 preguntas
├─ Puntuación promedio dominio: =PROMEDIO(I79:I94)
└─ Contribución: =Puntuación × 0,10

DOMINIO 6: Gobernanza (10% peso)
├─ P95-P104: 10 preguntas
├─ Puntuación promedio dominio: =PROMEDIO(I95:I104)
└─ Contribución: =Puntuación × 0,10
```

### Fórmula IGM Global

```excel
=REDONDEAR(
  (Promedio_MO*0,20 + Promedio_MOP*0,25 + Promedio_MP*0,20 + 
   Promedio_Incidentes*0,15 + Promedio_Capacitacion*0,10 + 
   Promedio_Gobernanza*0,10) / 100,
  2)
```

**Resultado:** IGM 1.0 - 5.0

### Interpretación IGM

```excel
=SI(IGM<2,0,"CRÍTICO",
   SI(IGM<3,0,"INSUFICIENTE",
      SI(IGM<3,5,"BÁSICO",
         SI(IGM<4,3,"AVANZADO","EXCELENCIA"))))
```

### Benchmark

```
IGM 1.0-1.9: CRÍTICO (riesgo extremo) → Intervención urgente
IGM 2.0-2.9: INSUFICIENTE (riesgo alto) → Plan acelerado
IGM 3.0-3.4: BÁSICO (riesgo medio) → Maduración anual
IGM 3.5-4.2: AVANZADO (riesgo bajo) → Consolidación
IGM 4.3-5.0: EXCELENCIA (mínimo riesgo) → Liderazgo
```

---

## HOJA 3: ANÁLISIS ROI

### Inputs Financieros

```
SECCIÓN A: INVERSIÓN
├─ Gasto actual ciberseguridad (P105): €
├─ Inversión adicional recomendada (12 meses): €
│  ├─ Personal (CISO/Analistas): €
│  ├─ Herramientas/Software (SIEM): €
│  ├─ Servicios externos (Auditoría): €
│  └─ Formación: €
└─ TOTAL INVERSIÓN 2026: € [Suma automática]

SECCIÓN B: BENEFICIOS DIRECTOS
├─ Costo promedio incidente actual (P107): €
├─ Número incidentes/año (P51): N
├─ Costo total incidentes/año: € [Cálculo: N × Costo]
├─ Reducción esperada incidentes: %
├─ Incidentes evitados/año: N [Cálculo: N × %]
├─ Costo evitado/año: € [Cálculo: Incidentes evitados × Costo]
├─ Reducción costo/incidente (MTTR mejora): %
├─ Ahorro MTTR/incidente: € [Cálculo: Costo × %]
├─ Beneficio total reducción MTTR: € [Cálculo: Incidentes × Ahorro]
└─ BENEFICIO TOTAL AÑO 1: € [Cálculo: Evitados + Ahorro]

SECCIÓN C: BENEFICIOS SOSTENIBLES (AÑO 2+)
└─ Beneficio anual después inversión inicial: €
   [Típico: +40% reducción incidentes permanente]
```

### Fórmulas ROI

```excel
ROI_Año1 = (Beneficio_Y1 - Inversión) / Inversión × 100

ROI_Acumulado_3años = (Beneficio_Y1 + Beneficio_Y2 + Beneficio_Y3 - Inversión) / Inversión × 100

Payback_Period = Inversión / Beneficio_Anual [en meses ÷ 12]

NPV = -Inversión + (Beneficio_Y1/1.10^1) + (Beneficio_Y2/1.10^2) + (Beneficio_Y3/1.10^3)

IRR = [Cálculo iterativo: tasa donde NPV = 0]
```

### Análisis Sensibilidad

```
┌─────────────────────────────────────────────────────┐
│ ESCENARIOS DE REDUCCIÓN INCIDENTES                 │
├─────────────────────────────────────────────────────┤
│ Pesimista (20% reducción)  → ROI Año 1: -65%      │
│ Base (40% reducción)       → ROI Año 1: -12%      │
│ Optimista (60% reducción)  → ROI Año 1: +41%      │
│ Muy Optimista (80%)        → ROI Año 1: +94%      │
└─────────────────────────────────────────────────────┘
```

---

## HOJA 4: DASHBOARD EJECUTIVO

### KPIs Principales

```
╔════════════════════════════════════════════════════╗
║ INDICADOR                VALOR      META    ESTADO ║
╠════════════════════════════════════════════════════╣
║ IGM Actual               3,47 / 5,0 → 4,0  🟡 75% ║
║ Brecha a Meta            0,53 puntos              ║
║                                                    ║
║ MTTD (Detección)         48h        <24h  🔴 ALTO ║
║ MTTR (Resolución)        6h         <4h   🟠 MED ║
║ Incidentes/Año           8          <4    🔴 ALTO ║
║                                                    ║
║ Conformidad ENS          78%        95%   🟠 MED ║
║ Conformidad NIS2         65%        90%   🔴 ALTO ║
║                                                    ║
║ Capacitación Cobertura   64%        100%  🟠 MED ║
║ Tasa Phishing Clicks     18%        <10%  🟠 MED ║
║                                                    ║
║ Presupuesto Actual       150K€      225K€ ⚠️ -33% ║
║ Inversión Recomendada    +75K€                     ║
║ ROI Año 1                -12%       Break-even     ║
║ ROI Año 2+               +150K€/año Sostenible     ║
║ Payback Period           11 meses   <12 meses ✓   ║
╚════════════════════════════════════════════════════╝
```

### Gráficos Recomendados

```
1. RADAR CHART (Madurez por Dominio)
   ├─ Ejes: 6 dominios ENS
   ├─ Valores: IGM por dominio (1-5)
   └─ Línea objetivo: 4,0

2. LINE CHART (Histórica + Proyección)
   ├─ Eje X: Trimestres (Q1 2024 - Q4 2027)
   ├─ Eje Y: IGM (1-5)
   ├─ Línea histórica: (si datos 2024)
   └─ Línea proyectada: Escenario con inversión

3. WATERFALL CHART (ROI Cálculo)
   ├─ Inversión (barra negativa)
   ├─ Incidentes evitados (barra positiva)
   ├─ MTTR reducción (barra positiva)
   └─ ROI Total (resultado)

4. HEAT MAP (Estado por Dominio)
   ├─ Rojo: IGM < 2,5
   ├─ Naranja: IGM 2,5-3,4
   ├─ Amarillo: IGM 3,5-3,9
   └─ Verde: IGM 4,0+
```

### Alertas Automáticas

```excel
=SI(IGM<2,5;"🔴 CRÍTICO - Acción urgente";"")
=SI(Y(MTTD>48;SIEM_Implementado=NO);"⚠️ SIEM requiere inversión";"")
=SI(Capacitación<50%;"🔴 Formación insuficiente";"")
=SI(ROI_Año1<-20%;"⚠️ ROI negativo Año 1";"✓ ROI aceptable")
```

---

## PROTECCIÓN Y CONTROL DE ACCESO

### Hojas Protegidas

```
Hoja 1 (Consolidación): Editable (input respondentes)
Hoja 2 (IGM): Protegida (cálculos automáticos)
Hoja 3 (ROI): Protegida (cálculos automáticos)
Hoja 4 (Dashboard): Protegida (visualización)
```

### Fórmula Protección

```excel
Herramientas → Proteger Hoja
├─ Contraseña: [solicitar a CISO]
├─ Permitir: Seleccionar celdas desbloqueadas
└─ Restringir: Modificar fórmulas
```

---

## EXPORTACIÓN Y REPORTES

### A PowerPoint

```
Hoja 4 Dashboard → Copiar rango
PowerPoint → Pegar especial (Imagen) en Diapositiva
```

### A PDF

```
Archivo → Exportar como PDF
├─ Seleccionar rangos: Hoja 2 (IGM), Hoja 3 (ROI), Hoja 4 (Dashboard)
├─ Nombre: IGM_ROI_Org_2026.pdf
└─ Guardar
```

### Control de Versiones

```
Excel → Archivo → Info → Versiones
├─ Guardar versión tras cada análisis
├─ Nombrar: "IGM_2026_Q1", "IGM_2026_Q2", etc.
└─ Comparar cambios trimestrales
```

---

## ACTUALIZACIÓN TRIMESTRAL

```
Q1 (Mar):  Línea base → Hoja 1 inicial
Q2 (Jun):  Seguimiento → Copiar Hoja 1, cambiar respondentes
Q3 (Sep):  Avance → Comparar Q1 vs Q3
Q4 (Dic):  Final año → Análisis anual + Proyección 2027
```

---

## EJEMPLOS DE VALORES

```
Presupuesto Actual: 150.000€ / año
Inversión Adicional: 75.000€ / año
├─ SIEM: 60.000€
├─ Capacitación: 25.000€
└─ Auditoría + otros: 15.000€

Costo Incidente Promedio: 45.000€
Incidentes/Año: 8 (tendencia +16%)

Escenario Base:
├─ Reducción 40% → 3,2 incidentes evitados
├─ Beneficio evitados: 144.000€
├─ MTTR mejora 2h: 54.000€ ahorro
└─ Total Beneficio Año 1: 198.000€

ROI Resultado:
├─ Año 1: -12% (inversión pesada)
├─ Año 2: +150.000€ sostenible
├─ NPV 3 años: 349.441€
├─ IRR: 34%
└─ Payback: 11 meses
```

---

## REFERENCIA RÁPIDA

| Acción | Dónde | Cómo |
|--------|-------|------|
| Ingresar respuestas | Hoja 1, Col D-H | Números 1-5 |
| Ver IGM actual | Hoja 2, Celda B2 | Valor automático |
| Calcular ROI | Hoja 3, Celda B20 | Inputs automáticos |
| Dashboard visual | Hoja 4 | Gráficos dinámicos |
| Generar reporte | Hoja 4 | Copiar a PowerPoint |

---

**Versión:** 1.0  
**Compatible:** Excel 2019+, Google Sheets, LibreOffice Calc  
**Última actualización:** 24 enero 2026
