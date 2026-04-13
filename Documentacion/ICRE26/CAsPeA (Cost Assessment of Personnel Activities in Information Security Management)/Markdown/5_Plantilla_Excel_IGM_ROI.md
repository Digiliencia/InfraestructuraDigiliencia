# PLANTILLA EXCEL PARA CÁLCULO DE IGM Y ROI
## Guía de Implementación en Hojas de Cálculo

**Versión:** 2.1  
**Formato recomendado:** Excel, Google Sheets  
**Propósito:** Automatizar cálculos CAsPeA, IGM, ROI desde respuestas de encuesta  

---

## ESTRUCTURA DE HOJAS (Workbook)

### HOJA 1: DATOS BÁSICOS

```
A1: "EVALUACIÓN DE MADUREZ CIBERSEGURIDAD"
A3: "Organización:"  B3: [ENTRADA USUARIO]
A4: "Sector:"        B4: [DROPDOWN: Financiero/Sanitario/...]
A5: "Tamaño:"        B5: [ENTRADA: Número empleados]
A6: "Fecha encuesta:"B6: [FECHA HOY()]

Proteger hoja para evitar cambios accidentales
```

---

### HOJA 2: DATOS CAsPeA (Personal + Costes)

```
Tabla: PERSONAL DEDICADO A SEGURIDAD

Encabezados (Fila 3):
A3: "Rol"
B3: "FTE"
C3: "Salario Anual (€)"
D3: "Beneficios (%)"
E3: "Tasa Horaria (€)"  [Fórmula: =C/1800]
F3: "Horas/Año Seg"
G3: "Coste Anual (€)"  [Fórmula: =B*C*(1+D%)]

Datos (Filas 4+):
A4: "CISO/Director"
B4: [ENTRADA] 
C4: [ENTRADA] 
D4: 0.25  [25% beneficios]
E4: =C4/1800
F4: [ENTRADA o 1800 si dedicado 100%]
G4: =B4*C4*(1+D4)

... (Repetir para cada rol: Arquitecto, Analista SIEM, etc.)

Fila N (Total):
AN: "TOTAL FTE"      BN: =SUM(B4:Bn-1)
CN: "COSTE TOTAL"    GN: =SUM(G4:Gn-1)
```

**Nota:** Si personal compartido (IT 20% tiempo seguridad):
```
A10: "Personal IT no dedicado"
B10: 8 (FTE totales IT)
F10: 360 (20% × 1800h)  [No multiplicar por B10]
G10: =8 * (Salario_promedio_IT / 1800) * 360
```

---

### HOJA 3: ASIGNACIÓN A NIST CSF

```
Tabla: COSTES POR FUNCIÓN NIST CSF

Encabezados:
A: "Función NIST"
B: "% Dedicación"
C: "Coste Asignado (€)"  [Fórmula: ='HOJA 2'!GN * B]

Datos:
A4: "Govern"          B4: [ENTRADA %]  C4: =SUM('HOJA 2'!G:G)*B4
A5: "Identify"        B5: [ENTRADA %]  C5: =SUM('HOJA 2'!G:G)*B5
A6: "Protect"         B6: [ENTRADA %]  C6: =SUM('HOJA 2'!G:G)*B6
A7: "Detect"          B7: [ENTRADA %]  C7: =SUM('HOJA 2'!G:G)*B7
A8: "Respond"         B8: [ENTRADA %]  C8: =SUM('HOJA 2'!G:G)*B8
A9: "Recover"         B9: [ENTRADA %]  C9: =SUM('HOJA 2'!G:G)*B9

Total:
A11: "TOTAL"          B11: =SUM(B4:B9) [VALIDACIÓN: debe = 100%]
                      C11: =SUM(C4:C9)
```

---

### HOJA 4: CÁLCULOS CASPEA NORMALIZADOS

```
Tabla: BENCHMARKING

A3: "Coste Total Anual"           B3: ='HOJA 2'!GN
A4: "Empleados con acceso IT"     B4: [ENTRADA desde P1.3 encuesta]
A5: "Coste/Empleado Protegido"    B5: =B3/B4

A7: "Comparativa Sector"
A8: "Sector identificado"         B8: ='DATOS BÁSICOS'!B4
A9: "Mediana sector (€/empleado)" B9: [LOOKUP tabla de referencia]
A10: "Percentil (%)."              B10: [CÁLCULO: dónde está vs mediana]
A11: "Recomendación"              B11: [IF B5<B9*0.7; "AUMENTAR"; 
                                         IF B5>B9*1.3; "REDUCIR"; "OK"]

A13: "Análisis CAsPeA por Rol"
A14: [Crear gráfico de Pareto: rol vs coste, para identificar partidas dominantes]
```

---

### HOJA 5: MÉTRICAS DE MADUREZ (IGM)

```
Tabla: EVALUACIÓN NIST CSF POR FUNCIÓN

Encabezados (Fila 3):
A: "Función"
B: "% Controles Implementados"  [Entrada desde P6.1 encuesta]
C: "Tier Estimado (1-4)"         [Entrada desde P6.1 encuesta]
D: "Puntuación Función"          [Fórmula: =(B+C*20)/2]

Datos:
A4: "Govern"     B4: [%]  C4: [Tier]  D4: =(B4+C4*20)/2
A5: "Identify"   B5: [%]  C5: [Tier]  D5: =(B5+C5*20)/2
A6: "Protect"    B6: [%]  C6: [Tier]  D6: =(B6+C6*20)/2
A7: "Detect"     B7: [%]  C7: [Tier]  D7: =(B7+C7*20)/2
A8: "Respond"    B8: [%]  C8: [Tier]  D8: =(B8+C8*20)/2
A9: "Recover"    B9: [%]  C9: [Tier]  D9: =(B9+C9*20)/2

Cálculos:
A11: "IMG (Índice Madurez General)" B11: =AVERAGE(D4:D9) [Rango 0-100]
A12: "Nivel equivalente"             B12: [IF B11<20;"Nivel 1";
                                           IF B11<40;"Nivel 1-2";...]

Interpretación:
A14: "Estado actual"  B14: [Descripción basada en IMG]
A15: "Brecha vs Tier 3 (60)" B15: =MAX(60-B11;0) [cuántos puntos para llegar a Tier 3]
```

---

### HOJA 6: ANÁLISIS DE INCIDENTES E ROI

```
Tabla: HISTORIAL INCIDENTES (últimos 12 meses)

Encabezados (Fila 3):
A: "Tipo Incidente"
B: "Cantidad (2024)"      [Entrada P6.2]
C: "Coste Promedio (€)"   [Entrada P6.2]
D: "Coste Total"          [Fórmula: =B*C]

Datos:
A4: "Malware"        B4: [ENTRADA]  C4: [ENTRADA]  D4: =B4*C4
A5: "Phishing"       B5: [ENTRADA]  C5: [ENTRADA]  D5: =B5*C5
A6: "Ransomware"     B6: [ENTRADA]  C6: [ENTRADA]  D6: =B6*C6
A7: "Breach datos"   B7: [ENTRADA]  C7: [ENTRADA]  D7: =B7*C7
... (Otros tipos)

Totales:
A12: "TOTAL INCIDENTES"  B12: =SUM(B4:B11)
A13: "PÉRDIDA TOTAL"     D13: =SUM(D4:D11)

---

CÁLCULO DE ROI:

A15: "ROI CUANTIFICADO"
A16: "Coste inversión anual"                B16: ='HOJA 2'!GN

A18: "Escenario SIN CONTROLES (baseline)"
A19: "Incidentes anuales históricos"        B19: [LOOKUP histórico 5 años]
A20: "Coste promedio incidente"             B20: =D13/B12
A21: "Pérdida anual esperada"               B21: =B19*B20

A23: "Escenario CON CONTROLES (actual)"
A24: "Incidentes actuales reducidos (%)"    B24: [Estimación conservadora: 60-70%]
A25: "Incidentes residuales"                B25: =B19*(1-B24%)
A26: "Pérdida residual"                     B26: =B25*B20
A27: "Pérdida EVITADA"                      B27: =B21-B26

A29: "CÁLCULO ROI"
A30: "Beneficio neto (Pérdida evitada - Inversión)" B30: =B27-B16
A31: "ROI (%)"                                       B31: =(B30/B16)*100
A32: "Payback Period (meses)"                        B32: =(B16/B30)*12

A34: "Interpretación:"
A35: [IF B31>30%;"ROI SALUDABLE (>30%)"; IF B31>0;"ROI POSITIVO pero bajo"; "ROI NEGATIVO"]
```

**Nota sobre conservadurismo:** Usar estimación 60-70% reducción es conservador. Algunos estudios sugieren 80-90%, pero es preferible subestimar para justificación sólida.

---

### HOJA 7: COMPARATIVA CON PARES (Benchmarking)

```
Tabla: DATOS DE REFERENCIA SECTORIAL (PRE-CARGADOS)

Encabezados:
A: "Sector"
B: "n (muestra)"
C: "Coste Mediano (€)"
D: "Coste/Empleado Mediano"
E: "IQR Bajo"
F: "IQR Alto"
G: "IMG Mediano"

Ejemplo datos (Año 2024):
A2: "Financiero"      B2: 32  C2: 1220000  D2: 2440  E2: 890000  F2: 1800000  G2: 62
A3: "Sanitario"       B3: 28  C3: 680000   D3: 1360  E3: 420000  F3: 1100000  G3: 52
A4: "Energía"         B4: 25  C4: 920000   D4: 1840  E4: 620000  F4: 1400000  G4: 58
... (resto sectores)

Cálculos para MI ORGANIZACIÓN:
A10: "Mi Coste/Empleado"        B10: ='HOJA 4'!B5
A11: "Sector referencia"         B11: ='DATOS BÁSICOS'!B4
A12: "Mediana sector"            B12: =VLOOKUP(B11;A2:G9;4;FALSE)
A13: "Posición vs mediana (%)"   B13: =(B10/B12)*100
A14: "Percentil estimado"        B14: [Manual o PERCENTILE_INC si datos completos]

Recomendación:
A16: [IF B13<70%;
     "CRÍTICO: Presupuesto significativamente bajo vs peers. Riesgo aumentado.";
     IF B13>130%;
     "ALTO: Presupuesto superior a peers. Revisar si eficiente.";
     "ADECUADO: Presupuesto alineado con sector"]
```

---

### HOJA 8: DASHBOARD EJECUTIVO

```
Crear dashboard visual con:

1. MÉTRICAS PRINCIPALES (tarjetas grandes)
   - IMG: [Número grande, color: Rojo si <40, Naranja si <60, Verde si >=60]
   - ROI (%): [Número grande, color: Verde si >30%, Naranja si 0-30%, Rojo si <0%]
   - Coste/Empleado: [Número, con comparativa vs sector]

2. GRÁFICOS
   - Gráfico de radar: Madurez por función NIST (6 ejes)
   - Gráfico de barras: Coste por función NIST
   - Gráfico de tendencia: Incidentes históricos (si datos 3+ años)
   - Gráfico de caja: Posición vs pares sector

3. TABLA RESUMEN
   Función | % Controles | Tier | Coste | Brecha vs Tier3
   Govern  |    62%      |  2.5 | €65K  | -18 pp
   ... (resto funciones)

4. RECOMENDACIONES (texto)
   "Prioridad 1: Función RESPOND (Tier 1.7 vs objetivo 3.0)"
   "Prioridad 2: Automatización SIEM para reducir MTTD"
   "Inversión sugerida: €150K próximo año (18 meses ROI)"
```

---

## VALIDACIÓN Y CONTROL DE DATOS

```
Hoja 9: VALIDACIÓN

A1: "CHEQUEOS DE INTEGRIDAD"

Fórmulas de validación:
=IF('HOJA 3'!B11<>1;"ERROR: % no suma 100%";"OK")
=IF('HOJA 5'!B11>100;"ERROR: IMG no puede >100%";"OK")
=IF('HOJA 4'!B5>5000;"ALERTA: Coste/empleado muy alto, revisar";"OK")
=IF('HOJA 6'!B12=0;"ALERTA: Cero incidentes reportados, revisar validez";"OK")

Reportes de error automáticos a celda resumen
```

---

## EXPORTACIÓN Y REPORTES

```
Hoja 10: EXPORTACIÓN

Crear botones (macros Excel o fórmulas TEXTJOIN) para generar:

1. RESUMEN EJECUTIVO (1 página)
   - IMG, ROI, recomendaciones clave
   - Exportar a PDF

2. INFORME DETALLADO (5-10 páginas)
   - Incluir tablas, gráficos, análisis
   - Exportar a WORD o PDF

3. DATOS PARA AUDITORÍA
   - CAsPeA desglosado por rol
   - Benchmarking sector
   - Mapeo normativo (si NIS2/DORA/ENS)
   - Exportar a Excel limpio
```

---

## INSTRUCCIONES DE IMPLEMENTACIÓN

1. **Descargar template Excel en blanco desde repositorio**
2. **Cargar respuestas de encuesta** → Copiar a Hoja 2 (datos brutos)
3. **Ejecutar validaciones** → Hoja 9 debe mostrar "OK"
4. **Revisar Dashboard** → Hoja 8 debe mostrar gráficos
5. **Exportar reportes** → PDF ejecutivo + Excel detallado

---

*Plantilla Excel CRA-Cyber v2.1 — Guía de Implementación*