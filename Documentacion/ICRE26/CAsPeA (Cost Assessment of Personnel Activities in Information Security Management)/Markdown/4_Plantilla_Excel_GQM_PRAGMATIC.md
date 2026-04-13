# PLANTILLA EXCEL: CÁLCULO IGM Y ROI (Guía de Implementación)
## Con Integración GQM+PRAGMATIC

**Versión:** 2.1  
**Plataforma:** Excel, Google Sheets  
**Propósito:** Automatizar GQM → PRAGMATIC → Decisión ejecutiva  

---

## ESTRUCTURA 12 HOJAS

### HOJA 1: ENTRADA DATOS + CONTROL CALIDAD

```
A1: "KIT CRA-CYBER GQM+PRAGMATIC v2.1"
A2: "Organización: [ENTRADA]"
A3: "Evaluador: [ENTRADA]"
A4: "Fecha: [HOY()]"
A5: "Email contacto: [ENTRADA]"

SECCIÓN: DATOS ENCUESTA (A8:C37)
─────────────────────────────────
Copiar 58 respuestas de Google Forms:
- Preguntas P1.1 a P6.7
- Formato: Pregunta | Opción Seleccionada | Puntuación Numérica
- Sistema validación: Todos valores deben estar en rango esperado

VALIDACIONES AUTOMÁTICAS (D8:D37):
=IF(C8="", "⚠️ FALTA RESPUESTA", "✓")
```

### HOJA 2: MATRIZ GQM GOALS→QUESTIONS→METRICS

```
Columnas: Goal | Question | Métrica | Fuente Datos | Validación PRAGMATIC | Puntuación

Fila 4: Goal 1 (Cumpl. NIS2)
  Q1.1 → M1.1 (% controles) → P1.5, P6.1 → PRAGMATIC Relevante=4/4
  
Fila 5: Goal 2 (CAsPeA)
  Q2.1 → M2.1 (Coste €) → P6.4 → PRAGMATIC Genuino=4/4

[etc. para 30+ métricas mapeadas a Goals]

CÁLCULO AUTOMÁTICO:
Σ(PRAGMATIC scores) / N = Calidad Métrica Media
Si >3.5 → Métrica VÁLIDA para usar en decisión
Si <3.0 → Métrica a REVISAR o COMPLEMENTAR
```

### HOJA 3: CÁLCULOS CAsPeA DESGLOSADO

```
TABLA PRINCIPAL:
Encabezados: Rol | FTE | Salario Anual (€) | Beneficios (%) | Tasa Horaria | Horas Seg/Año | Coste Neto (€)

Datos entrada (editable por usuario):
A4: CISO              B4: [1.0]    C4: [75000]    D4: [0.25]    E4: =C4/1800    F4: [1800]    G4: =B4*C4*(1+D4)
A5: Arquitecto Sec    B5: [2.0]    C5: [60000]    D5: [0.25]    E5: =C5/1800    F5: [1800]    G5: =B5*C5*(1+D5)
A6: Admin IT (20% seg) B6: [8.0]   C6: [40000]    D6: [0.25]    E6: =C6/1800    F6: [360]     G6: =B6*(C6/1800)*F6
... [Rows adicionales para cada rol]

TOTALES (Fila N):
AN: "TOTAL"          BN: =SUM(B4:Bn-1)
                     CN: "Coste Total Personas"
                     GN: =SUM(G4:Gn-1)

DISTRIBUIR A NIST CSF (Fila N+5):
Govern:   % dedicación × GN
Identify: % dedicación × GN
Protect:  % dedicación × GN
Detect:   % dedicación × GN
Respond:  % dedicación × GN
Recover:  % dedicación × GN
TOTAL:    =SUM(Govern:Recover) [validación = GN]
```

### HOJA 4: BENCHMARKING + COMPARATIVA SECTORIAL

```
TABLA DATOS REFERENCIA (pre-cargada):
Sector | Muestra | Coste Mediano (€K) | €/Empleado Mediano | Percentil 25% | Percentil 75% | IMG Mediano

Financiero  | 45 | 1.220 | 2.440 | 890 | 1.800 | 62
Sanitario   | 38 | 680  | 1.360 | 420 | 1.100 | 52
Energía     | 28 | 920  | 1.840 | 620 | 1.400 | 58
... [resto sectores]

ANÁLISIS MI ORGANIZACIÓN:
A10: "Mi sector identificado:"        B10: ='HOJA 1'!A2 [Entrada]
A11: "Mi coste total anual:"          B11: ='HOJA 3'!GN
A12: "Empleados con acceso IT:"       B12: [ENTRADA desde P1.2]
A13: "Mi coste/empleado:"             B13: =B11/B12

COMPARATIVA BENCHMARKING:
A15: "Mediana sector"                 B15: =VLOOKUP(B10, tabla_ref, 3, FALSE)
A16: "Mi posición (%):"               B16: =B13/B15*100
A17: "Recomendación:"                 B17: =IF(B16<70%, "CRÍTICO: Presupuesto bajo", 
                                             IF(B16>130%, "ALTO: Presupuesto alto", 
                                             "ADECUADO: Alineado con sector"))

COLOR CONDICIONAL (B16):
- <70% = ROJO (insuficiente)
- 70-100% = NARANJA (bajo)
- 100-130% = VERDE (adecuado)
- >130% = AMARILLO (alto)
```

### HOJA 5: EVALUACIÓN MADUREZ (IMG)

```
TABLA: TIER MADUREZ POR FUNCIÓN NIST CSF

Encabezados: Función | % Controles Impl. | Tier Estimado (1-4) | Puntuación (0-100) | Brecha vs Tier 3

Datos entrada (desde encuesta P6.1):
A4: Govern        B4: [85%]      C4: [3.2]      D4: =(B4*100/100+C4*20)/2      E4: =(60-D4)
A5: Identify      B5: [72%]      C5: [2.5]      D5: =(B5*100+C5*20)/2           E5: =(60-D5)
A6: Protect       B6: [78%]      C6: [2.8]      D6: =(B6*100+C6*20)/2           E6: =(60-D6)
A7: Detect        B7: [48%]      C7: [1.9]      D7: =(B7*100+C7*20)/2           E7: =(60-D7)
A8: Respond       B8: [42%]      C8: [1.7]      D8: =(B8*100+C8*20)/2           E8: =(60-D8)
A9: Recover       B9: [35%]      C9: [1.5]      D9: =(B9*100+C9*20)/2           E9: =(60-D9)

CÁLCULOS FINALES:
A11: "IMG GENERAL"           D11: =AVERAGE(D4:D9)      E11: Rango 0-100
A12: "Tier equivalente"      D12: =IF(D11<20, "Tier 1", IF(D11<40, "Tier 1-2", ...))
A13: "Brecha total vs Tier 3" D13: =MAX(SUM(E4:E9), 0)
A14: "Meses a Tier 3"        D14: =INT(D13/5) [asumiendo 5pp mejora/mes]

GRÁFICO RADAR (visualización):
6 ejes (funciones NIST) × Puntuación 0-100
Overlay: Línea "Objetivo Tier 3 = 60" como referencia
```

### HOJA 6: ANÁLISIS INCIDENTES E ROI

```
TABLA: HISTORIAL INCIDENTES (Última 3 años si datos)

Encabezados: Año | Tipo Incidente | Cantidad | Coste Promedio (€) | Coste Total | Tasa Cambio YoY

Datos entrada (desde encuesta P6.2):
A4: 2024 | Malware       | [15]  | [35000]   | =B4*D4 | 
A5: 2024 | Phishing      | [28]  | [5000]    | =B5*D5 |
A6: 2024 | Ransomware    | [3]   | [250000]  | =B6*D6 |
A7: 2024 | Data Breach   | [2]   | [500000]  | =B7*D7 |
... [2023, 2022 si datos]

TOTALES POR AÑO:
A13: "2024 TOTAL"  B13: =SUM(B4:B12)  G13: =SUM(G4:G12)  H13: [Trending]
A14: "2023 TOTAL"  B14: =SUM(...)     G14: =SUM(...)     H14: =(G13-G14)/G14*100

ROI CALCULATION:
─────────────────

A16: "ESCENARIO SIN CONTROLES (Baseline)"
A17: "  Incidentes anuales históricos (promedio 5 años)" B17: [15]
A18: "  Coste promedio incidente"                        B18: [240000]
A19: "  Pérdida anual esperada"                          B19: =B17*B18

A21: "ESCENARIO CON CONTROLES ACTUALES"
A22: "  Reducción incidentes conseguida (%)"            B22: [60%]
A23: "  Incidentes residuales"                          B23: =B17*(1-B22%)
A24: "  Pérdida residual"                               B24: =B23*B18
A25: "  Pérdida EVITADA"                                B25: =B19-B24

A27: "CÁLCULO ROI"
A28: "  Coste total inversión anual (CAsPeA)"          B28: ='HOJA 3'!GN
A29: "  Herramientas + licencias"                       B29: [ENTRADA: €150K]
A30: "  Consultoría + formación"                        B30: [ENTRADA: €80K]
A31: "  INVERSIÓN TOTAL"                                B31: =B28+B29+B30

A33: "  Beneficio neto (Pérdida evitada - Inversión)"  B33: =B25-B31
A34: "  ROI (%)"                                         B34: =(B33/B31)*100
A35: "  Payback Period (meses)"                         B35: =(B31/B25)*12
A36: "  Break-even análisis"                            B36: =IF(B34>0, "RENTABLE ✓", "NO RENTABLE ✗")

FORMATO CONDICIONAL:
B34: Si >100% → VERDE
     Si 0-100% → AMARILLO
     Si <0% → ROJO
```

### HOJA 7: MAPEO GQM+PRAGMATIC (Validación Calidad)

```
Tabla: Cada Métrica × 9 Criterios PRAGMATIC

Encabezados: Métrica | Predictivo | Relevante | Accionable | Genuino | Significativo | Preciso | Oportuno | Independiente | Rentable | MEDIA | Recomendación

Datos (escala 1-4):
A4: M2.1 (CAsPeA)           | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | =AVERAGE(B4:J4) | =IF(K4>3.5, "IMPLEMENTAR", "REVISAR")
A5: M4.1 (MTTD)             | 4 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 4 | =AVERAGE(B5:J5) | ...
A6: M6.1 (IMG)              | 4 | 4 | 3 | 2 | 4 | 2 | 3 | 3 | 2 | =AVERAGE(B6:J6) | ...

RESUMEN:
A13: "Métricas VÁLIDAS (≥3.5)"     B13: =COUNTIF(K4:K12, "IMPLEMENTAR")
A14: "Métricas REVISAR (<3.0)"     B14: =COUNTIF(K4:K12, "REVISAR")
A15: "Calidad promedio PRAGMATIC"  B15: =AVERAGE(K4:K12)
```

### HOJA 8: DASHBOARD EJECUTIVO

```
Crear visualizaciones interactivas:

ZONA SUPERIOR (Métricas clave):
┌─────────────┬──────────────┬──────────────┐
│ IMG: [60]   │ ROI: [145%]  │ CAsPeA: €350K│
│ Tier 2-3    │ Payback: 8mo │ vs Sector: +12% │
└─────────────┴──────────────┴──────────────┘

GRÁFICOS:
1. Radar: Madurez por función NIST (6 ejes)
2. Barras: Coste por función NIST
3. Líneas: Trending incidentes (3-5 años)
4. Caja (Box plot): Posición vs pares sector
5. Gantt: Roadmap remediación (próximos 12 meses)

TABLA RESUMEN:
Función | Cobertura % | Tier | Coste | Brecha vs Tier3 | Prioridad
Govern  |    85%     | 3.2  | €65K  |     -5pp        |    ✓
Detect  |    48%     | 1.9  | €42K  |     -32pp       | 🔴 CRÍTICA
```

### HOJA 9: RECOMENDACIONES AUTOMÁTICAS

```
LÓGICA DE DECISIÓN (usando IF statements):

SI IMG < 40:
  "CRÍTICO: Invertir inmediatamente en controles de Identify/Detect"
SINO SI IMG 40-60:
  "ACCIÓN RECOMENDADA: Roadmap de 12-18 meses a Tier 3"
SINO SI IMG > 60:
  "EN MARCHA: Mantener y optimizar; evaluar transición Tier 4"

SI ROI < 0:
  "RIESGO: Inversión actual no justificada; revisar supuestos"
SINO SI ROI 0-50%:
  "ACEPTABLE: ROI positivo pero bajo; considerar optimizar"
SINO SI ROI > 50%:
  "RECOMENDADO: ROI saludable; proceder con plan"

SI MTTD > 120:
  "BRECHA NIS2: MTTD debe <60 min; prioritario automatización SIEM"
```

### HOJA 10: EXPORTACIÓN REPORTES

```
Botones (macros o hipervínculos):

[1] GENERAR RESUMEN EJECUTIVO (1 pág)
    Output: PDF con IMG, ROI, TOP 3 recomendaciones
    
[2] GENERAR INFORME COMPLETO (10-15 págs)
    Output: PDF con tablas, gráficos, análisis completo
    
[3] GENERAR PLANILLA AUDITORÍA
    Output: Excel con todas métricas desglosadas
    
[4] COMPARATIVA SECTOR
    Output: PDF benchmarking vs pares
```

### HOJA 11: DICCIONARIO + FÓRMULAS

```
Referencia rápida de definiciones:
- IMG: Índice Madurez General (0-100)
- CAsPeA: Coste Assessment Personas Security
- MTTD: Mean Time To Detect (minutos)
- MTTR: Mean Time To Respond (minutos)
- ROI: Return on Investment (%)
- Payback: Tiempo recuperación inversión (meses)

Fórmulas clave guardadas para referencia
```

### HOJA 12: CONTROL DE VERSIÓN + AUDITORÍA

```
A1: "LOG DE AUDITORÍA"
A3: Fecha | Usuario | Cambios | Versión

Auto-registro cada vez que se modifica datos críticos
(P3 compatible con GDPR auditoría)
```

---

## INSTRUCCIONES DE USO PASO A PASO

1. **Descargar Template** desde repositorio
2. **Completar HOJA 1** con datos organización
3. **Copiar respuestas encuesta** a HOJA 1
4. **Ejecutar validaciones** (HOJA 1, columna D)
5. **Revisar Dashboard** (HOJA 8)
6. **Exportar reportes** (HOJA 10)

---

*Plantilla Excel GQM+PRAGMATIC v2.1 — Guía de Implementación*