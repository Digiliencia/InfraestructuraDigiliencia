# 📊 PLANTILLA EXCEL — CÁLCULO DE IGM Y ROI
## Índice Global de Madurez CIA (IGM-CIA) y Retorno de la Inversión en Ciberseguridad
### CIA Triad Survey Kit 2025 — Especificación para Implementación en Excel / Google Sheets

---

> *"Lo que no se mide con números, se mide con consecuencias.
> Y las consecuencias en ciberseguridad tienen facturas considerablemente más altas que las inversiones preventivas."*

---

## DESCRIPCIÓN GENERAL

Este documento especifica la estructura completa de la plantilla Excel para:
1. **Cálculo automático del IGM-CIA** (Índice Global de Madurez CIA) por organización
2. **Cálculo del IGM sectorial** para benchmarking comparativo
3. **Estimación del ROI/ROSI** (Return on Security Investment) según modelo FAIR
4. **Dashboard ejecutivo** con visualizaciones automáticas

**Implementación recomendada:** Microsoft Excel 365 o Google Sheets  
**Nivel de complejidad:** Intermedio (uso de VLOOKUP, tablas dinámicas, gráficos condicionales)  
**Versiones compatibles:** Excel 2016+, Excel 365, Google Sheets (2025)

---

## ESTRUCTURA DE HOJAS (TABS)

```
📁 CIA_IGM_ROI_Calculator.xlsx
├── 📋 INICIO          → Portada, instrucciones y leyenda de colores
├── 📊 DATOS_RAW       → Importación/volcado de respuestas de encuesta
├── ⚙️ CODIFICACION    → Tabla de conversión respuestas → puntuación (1-5)
├── 🧮 IGM_CALC        → Cálculo automático del IGM-CIA individual
├── 📈 BENCHMARK       → Comparativa sectorial (IGM por sector/tamaño)
├── 💰 ROI_FAIR        → Modelo FAIR simplificado y cálculo ROSI
├── 🎯 DASHBOARD       → Resumen ejecutivo visual con gráficos
└── 📖 REFERENCIAS     → Fuentes, versión y créditos
```

---

## HOJA 1: INICIO

```
Celda A1:  [LOGO/TÍTULO] CIA Triad Survey Kit 2025
Celda A3:  Versión: 2025.1
Celda A4:  Fecha de actualización: Abril 2026
Celda A5:  Basado en: NIST CSF 2.0, ENS RD 311/2022, FAIR Institute 2025

Tabla de leyenda de colores (rango A8:B15):
  🔴 Rojo    IGM 1.0–1.9  → Nivel Crítico
  🟠 Naranja IGM 2.0–2.9  → Nivel Deficiente
  🟡 Amarillo IGM 3.0–3.4 → Nivel En Desarrollo
  🟢 Verde   IGM 3.5–3.9  → Nivel En Desarrollo Avanzado
  🔵 Azul    IGM 4.0–4.4  → Nivel Competente
  ⭐ Morado  IGM 4.5–5.0  → Nivel Líder

Instrucciones de uso (rango A17:B35):
  Paso 1: Importar o introducir respuestas en hoja DATOS_RAW
  Paso 2: Verificar codificación automática en hoja CODIFICACION
  Paso 3: Revisar IGM calculado en hoja IGM_CALC
  Paso 4: Configurar sector y tamaño para benchmarking en BENCHMARK
  Paso 5: Introducir datos financieros en ROI_FAIR
  Paso 6: Exportar DASHBOARD para reporte ejecutivo
```

---

## HOJA 2: DATOS_RAW

### Estructura de columnas (una fila por organización encuestada)

```
Columna  | Campo                    | Tipo          | Validación
---------|--------------------------|---------------|----------------------------------
A        | ID_Encuesta              | Texto (código)| Único, alfanumérico
B        | Fecha_Respuesta          | Fecha         | DD/MM/YYYY
C        | Sector                   | Lista         | [Banca, Salud, Energía, AAPP, TIC, Industria, Transporte, Educación, Otro]
D        | Tamaño                   | Lista         | [Micro, Pequeña, Mediana, Grande, Corporación]
E        | Ambito_Geo               | Lista         | [Local, Nacional, UE, Internacional, Global]
F        | Es_Operador_Esencial     | Lista         | [Sí Esencial, Sí Digitales, En proceso, No, Desconoce]
G        | ENS_Nivel                | Lista         | [Básico, Medio, Alto, Sin certificar, No aplica]
H        | CISO_Existe              | Lista         | [Exclusivo, Parcial, De facto, No existe, vCISO]
I        | Presupuesto_Pct_IT       | Lista         | [<5%, 5-9%, 10-14%, 15-20%, >20%, No desglosado]
J        | P1_1_MFA_Cobertura       | Numérico 1-5  | INT, 1 a 5
K        | P1_2_MFA_Tipo            | Numérico 1-5  | INT, 1 a 5
L        | P1_3_IAM                 | Numérico 1-5  | INT, 1 a 5
M        | P1_4_Revision_Privilegios| Numérico 1-5  | INT, 1 a 5
N        | P1_5_PAM                 | Numérico 1-5  | INT, 1 a 5
O        | P1_6_Min_Privilegio      | Numérico 1-5  | INT, 1 a 5
P        | P1_7_Cifrado_Reposo      | Numérico 1-5  | INT, 1 a 5
Q        | P1_8_Algoritmos          | Numérico 1-5  | INT, 1 a 5
R        | P1_9_PQC                 | Numérico 1-5  | INT, 1 a 5
S        | P1_10_DLP                | Numérico 1-5  | INT, 1 a 5
T        | P1_11_Exfiltracion       | Numérico 1-5  | INT, 1 a 5
U        | P1_12_Clasificacion      | Numérico 1-5  | INT, 1 a 5
V        | P1_13_Inventario         | Numérico 1-5  | INT, 1 a 5
W        | P1_14_ShadowAI           | Numérico 1-5  | INT, 1 a 5
X        | P1_15_Politica_IA        | Numérico 1-5  | INT, 1 a 5
Y        | P1_16_Madurez_C          | Numérico 1-5  | INT, 1 a 5
Z        | P2_1_FIM                 | Numérico 1-5  | INT, 1 a 5
AA       | P2_2_Hash                | Numérico 1-5  | INT, 1 a 5
AB       | P2_3_Parcheo_Critico     | Numérico 1-5  | INT, 1 a 5
AC       | P2_4_Parcheo_Edge        | Numérico 1-5  | INT, 1 a 5
AD       | P2_5_VM_Proceso          | Numérico 1-5  | INT, 1 a 5
AE       | P2_6_Firma_Digital       | Numérico 1-5  | INT, 1 a 5
AF       | P2_7_SIEM_Logs           | Numérico 1-5  | INT, 1 a 5
AG       | P2_8_Retencion_Logs      | Numérico 1-5  | INT, 1 a 5
AH       | P2_9_Forense             | Numérico 1-5  | INT, 1 a 5
AI       | P2_10_SW_Verificacion    | Numérico 1-5  | INT, 1 a 5
AJ       | P2_11_SBOM               | Numérico 1-5  | INT, 1 a 5
AK       | P2_12_Incid_Proveedores  | Numérico 1-5  | INT, 1 a 5 (invertida)
AL       | P2_13_DataPoisoning      | Numérico 1-5  | INT, 1 a 5
AM       | P2_14_Madurez_I          | Numérico 1-5  | INT, 1 a 5
AN       | P3_1_BCP                 | Numérico 1-5  | INT, 1 a 5
AO       | P3_2_DRP_Pruebas         | Numérico 1-5  | INT, 1 a 5
AP       | P3_3_RTO                 | Numérico 1-5  | INT, 1 a 5
AQ       | P3_4_RPO                 | Numérico 1-5  | INT, 1 a 5
AR       | P3_5_Backups             | Numérico 1-5  | INT, 1 a 5
AS       | P3_6_321_Regla           | Numérico 1-5  | INT, 1 a 5
AT       | P3_7_SOC                 | Numérico 1-5  | INT, 1 a 5
AU       | P3_8_MTTD                | Numérico 1-5  | INT, 1 a 5
AV       | P3_9_MTTR                | Numérico 1-5  | INT, 1 a 5
AW       | P3_10_Ransomware_Exp     | Numérico 1-5  | INT, 1 a 5 (invertida)
AX       | P3_11_Postura_Pago       | Numérico 1-5  | INT, 1 a 5
AY       | P3_12_AntiDDoS           | Numérico 1-5  | INT, 1 a 5
AZ       | P3_13_SLA_Uptime         | Numérico 1-5  | INT, 1 a 5
BA       | P3_14_Redundancia        | Numérico 1-5  | INT, 1 a 5
BB       | P3_15_IoT_Inventario     | Numérico 1-5  | INT, 1 a 5
BC       | P3_16_Madurez_A          | Numérico 1-5  | INT, 1 a 5
BD       | P5_1_Frameworks          | Numérico 0-10 | Count de frameworks marcados
BE       | P6_1_Formacion           | Numérico 1-5  | INT, 1 a 5
BF       | P6_2_Phishing_Sim        | Numérico 1-5  | INT, 1 a 5
BG       | P7_1_PQC_Eval            | Numérico 1-5  | INT, 1 a 5
BH       | P7_3_ZeroTrust           | Numérico 1-5  | INT, 1 a 5
BI       | P8_1_Madurez_C_Global    | Numérico 1-5  | INT, 1 a 5
BJ       | P8_1_Madurez_I_Global    | Numérico 1-5  | INT, 1 a 5
BK       | P8_1_Madurez_A_Global    | Numérico 1-5  | INT, 1 a 5
BL       | P8_1_Madurez_Auth_Global | Numérico 1-5  | INT, 1 a 5
```

---

## HOJA 3: CODIFICACION

### Tabla de conversión — ejemplos principales

```
Tabla CODIF_MFA (rango A2:C8):
  Respuesta_Raw                              | Código | Puntuación
  "Menos del 25%"                            |   1    |     1
  "Entre 25% y 50%"                          |   2    |     2
  "Entre 51% y 75%"                          |   3    |     3
  "Entre 76% y 90%"                          |   4    |     4
  "Más del 90%"                              |   5    |   4.5
  "100%, incluidas cuentas privilegiadas"    |   6    |     5

Tabla CODIF_RTO (rango A12:C18):
  Respuesta_Raw                              | Código | Puntuación
  "Menos de 15 minutos"                      |   1    |     5
  "Entre 15 min y 1 hora"                    |   2    |     4
  "Entre 1 y 4 horas"                        |   3    |     3
  "Entre 4 y 24 horas"                       |   4    |     2
  "Más de 24 horas"                          |   5    |     1
  "Sin RTO definido"                         |   6    |     0

Tabla CODIF_PARCHEO (rango A22:C28):
  Respuesta_Raw                              | Código | Puntuación
  "Menos de 24 horas"                        |   1    |     5
  "1 a 7 días"                               |   2    |     4
  "8 a 30 días"                              |   3    |     3
  "31 a 90 días"                             |   4    |     2
  "Más de 90 días"                           |   5    |     1
  "Sin proceso definido"                     |   6    |     0

NOTA: Todas las tablas de codificación se estructuran así.
Ver hoja CODIFICACION para el set completo de 45 tablas.
```

---

## HOJA 4: IGM_CALC — CÁLCULO PRINCIPAL

### Sección A: Puntuaciones por Sub-dominio (Columnas A-E)

```
Fila 1: Encabezados
  A1: ID_Encuesta
  B1: Sector
  C1: Tamaño
  D1: Score_C_Acceso_Identidad    (media P1.1 a P1.6)
  E1: Score_C_Cifrado             (media P1.7 a P1.9)
  F1: Score_C_DLP_Exfiltracion    (media P1.10 a P1.11)
  G1: Score_C_Clasificacion       (media P1.12 a P1.13)
  H1: Score_C_ShadowAI            (media P1.14 a P1.15)
  I1: IGM_C                       (media ponderada D:H)
  J1: Score_I_FIM_Parcheo         (media P2.1 a P2.5)
  K1: Score_I_Custodia_Repudio    (media P2.6 a P2.9)
  L1: Score_I_SupplyChain         (media P2.10 a P2.12)
  M1: Score_I_IA_Integridad       (P2.13)
  N1: IGM_I                       (media ponderada J:M)
  O1: Score_A_Continuidad         (media P3.1 a P3.6)
  P1: Score_A_Incidentes          (media P3.7 a P3.11)
  Q1: Score_A_DDoS_HA             (media P3.12 a P3.14)
  R1: Score_A_IoT                 (P3.15)
  S1: IGM_A                       (media ponderada O:R)
  T1: IGM_CIA                     (media ponderada I, N, S)
  U1: Nivel_Madurez               (texto: Crítico/Deficiente/En desarrollo/Competente/Líder)
  V1: Color_Semaforo              (formato condicional)

Fila 2 en adelante: Datos calculados automáticamente

Fórmula D2 (Score_C_Acceso_Identidad):
  =IFERROR(AVERAGE(DATOS_RAW!J2, DATOS_RAW!K2, DATOS_RAW!L2, DATOS_RAW!M2, DATOS_RAW!N2, DATOS_RAW!O2), "")

Fórmula I2 (IGM_C — ponderación estándar):
  =IFERROR(
    (D2*0.30 + E2*0.25 + F2*0.20 + G2*0.15 + H2*0.10),
  "")

Fórmula T2 (IGM_CIA — ponderación genérica 33/33/34):
  =IFERROR(
    VLOOKUP(B2, PONDERACIONES!$A$2:$D$20, 2, FALSE)*I2 +
    VLOOKUP(B2, PONDERACIONES!$A$2:$D$20, 3, FALSE)*N2 +
    VLOOKUP(B2, PONDERACIONES!$A$2:$D$20, 4, FALSE)*S2,
  "")

Fórmula U2 (Nivel_Madurez):
  =IFS(
    T2>=4.5, "⭐ Líder",
    T2>=4.0, "🔵 Competente",
    T2>=3.5, "🟢 En Desarrollo Avanzado",
    T2>=3.0, "🟡 En Desarrollo",
    T2>=2.0, "🟠 Deficiente",
    T2>=1.0, "🔴 Crítico",
    TRUE,    "⚠️ Sin datos"
  )
```

### Sección B: Tabla de Ponderaciones por Sector (Hoja auxiliar PONDERACIONES)

```
Columna A: Sector
Columna B: w_Confidencialidad
Columna C: w_Integridad
Columna D: w_Disponibilidad

Valores (basados en análisis de riesgo sectorial):
  Banca / Finanzas            → 0.35 | 0.30 | 0.35
  Seguros                     → 0.35 | 0.30 | 0.35
  Salud                       → 0.40 | 0.35 | 0.25
  Energía / Utilities         → 0.25 | 0.30 | 0.45
  Telecomunicaciones / TIC    → 0.30 | 0.30 | 0.40
  Administración Pública      → 0.35 | 0.35 | 0.30
  Industria / Manufactura     → 0.30 | 0.35 | 0.35
  Transporte / Logística      → 0.25 | 0.35 | 0.40
  Educación / Investigación   → 0.38 | 0.32 | 0.30
  Comercio / Distribución     → 0.35 | 0.30 | 0.35
  Defensa / Seguridad         → 0.40 | 0.35 | 0.25
  Genérico / Otro             → 0.33 | 0.33 | 0.34
```

### Sección C: Alertas Automáticas

```
Columna W1: Alertas_Criticas
Fórmula W2:
  =IF(
    OR(
      DATOS_RAW!N2=0,    // PAM: cuentas compartidas
      DATOS_RAW!Q2=1,    // Cifrado: algoritmos legacy
      DATOS_RAW!AB2=0,   // Parcheo: sin proceso
      DATOS_RAW!AO2=0,   // BCP: no existe
      DATOS_RAW!AT2=1,   // SOC: solo por usuarios
      DATOS_RAW!BC2=1    // NIS2: desconoce requisitos
    ),
    "⚠️ ALERTA ROJA — Ver detalles",
    "✅ Sin alertas críticas"
  )
```

---

## HOJA 5: BENCHMARK

### Estructura de tablas dinámicas recomendadas

```
Tabla Dinámica 1: IGM_CIA promedio por SECTOR
  Filas: Sector
  Valores: Promedio de IGM_CIA, IGM_C, IGM_I, IGM_A
  Filtros: Tamaño, Ámbito_Geo
  Visualización: Gráfico de barras agrupadas con línea de referencia

Tabla Dinámica 2: Distribución de niveles de madurez por TAMAÑO
  Filas: Tamaño organizacional
  Columnas: Nivel_Madurez (Crítico/Deficiente/En desarrollo/Competente/Líder)
  Valores: COUNT de organizaciones
  Visualización: Gráfico de barras apiladas 100%

Tabla Dinámica 3: Top 5 subdominios con menor puntuación (áreas de mejora prioritarias)
  Fuente: Medias de cada Score_ sub-dominio
  Orden: Ascendente por puntuación media
  Visualización: Gráfico de barras horizontal (horizontal bar chart)

Fórmulas de benchmarking individual:
  // Percentil de la organización vs. muestra
  =PERCENTRANK.INC(IGM_CALC!T$2:T$500, IGM_CALC!T2, 1)
  // Posición vs. mediana sectorial
  =IGM_CALC!T2 - AVERAGEIF(IGM_CALC!B$2:B$500, IGM_CALC!B2, IGM_CALC!T$2:T$500)
```

---

## HOJA 6: ROI_FAIR — MODELO DE ROI DE CIBERSEGURIDAD

### Sección A: Datos de entrada financieros

```
Celdas de entrada (amarillas):
  B3:  Presupuesto anual ciberseguridad (€)                → Input manual
  B4:  Coste promedio brecha por incidente estimado (€)     → Default: 4.440.000 (IBM 2025)
  B5:  Número de incidentes esperados/año sin controles     → Input manual
  B6:  Número de incidentes esperados/año con controles     → Input manual
  B7:  Factor de reducción de impacto por controles (%)     → Input manual
  B8:  Años de horizonte temporal del análisis              → Default: 3

Celdas de referencia de mercado (grises, no modificables):
  E3:  Coste brecha global IBM 2025: 4.440.000 €
  E4:  Coste brecha USA IBM 2025: 10.220.000 €
  E5:  Coste brecha sector salud: 10.930.000 €
  E6:  Ahorro IA en detección IBM 2025: 1.900.000 €
  E7:  Coste shadow AI adicional: 670.000 €
  E8:  Reducción coste ZT exitoso: -1.500.000 €
```

### Sección B: Cálculos ALE y ROSI

```
B12: ALE_Sin_Controles (Annualized Loss Expectancy sin inversión)
  Fórmula: =B4 * B5
  Descripción: Pérdida esperada anual sin controles de seguridad

B13: ALE_Con_Controles (Annualized Loss Expectancy con inversión)
  Fórmula: =B4 * B6 * (1 - B7/100)
  Descripción: Pérdida esperada anual con controles implementados

B14: Beneficio_Anual_Controles
  Fórmula: =B12 - B13
  Descripción: Reducción de pérdida esperada por controles

B15: ROSI (Return on Security Investment)
  Fórmula: =(B14 - B3) / B3 * 100
  Descripción: % de retorno sobre la inversión en seguridad
  Nota: ROSI > 0% = inversión justificada; ROSI > 100% = excelente ROI

B16: Payback_Meses
  Fórmula: =IF(B14>0, B3/(B14/12), "No hay retorno positivo")
  Descripción: Meses para recuperar la inversión en seguridad

B17: VAN_3anios (Valor Actual Neto a 3 años, tasa descuento 8%)
  Fórmula: =-B3 + (B14/1.08) + (B14/1.08^2) + (B14/1.08^3)
  Descripción: Valor presente del flujo de beneficios de seguridad

B18: Factor_Reduccion_MTTD
  Fórmula: =IF(B8_MTTD_Actual>60, (B8_MTTD_Actual-60)*B4/365*0.5, 0)
  Descripción: Ahorro estimado por reducción de MTTD a < 60 días
  Referencia: IBM 2025 — cada día de reducción MTTD ≈ $18.300 de ahorro
```

### Sección C: Tabla de Sensibilidad

```
Tabla cruzada (rango D20:J30):
  Filas: Variación en frecuencia de incidentes (-50%, -25%, Base, +25%, +50%)
  Columnas: Variación en coste por incidente (-25%, -10%, Base, +10%, +25%)
  Valores: ROSI calculado para cada combinación
  Formato condicional:
    Verde (>100%): =ROSI>100%
    Amarillo (0-100%): =ROSI>=0 Y ROSI<=100
    Rojo (<0%): =ROSI<0
```

### Sección D: Tabla IGM-Riesgo Correlación

```
Cálculo del riesgo residual estimado por nivel IGM (rango A35:D42):

  IGM Range | Nivel          | Factor reducción riesgo | Coste residual estimado
  1.0–1.9   | Crítico        | 0%                      | Coste pleno (ALE base)
  2.0–2.9   | Deficiente     | 20%                     | ALE * 0.80
  3.0–3.4   | En desarrollo  | 40%                     | ALE * 0.60
  3.5–3.9   | En des. Avanz. | 55%                     | ALE * 0.45
  4.0–4.4   | Competente     | 70%                     | ALE * 0.30
  4.5–5.0   | Líder          | 85%                     | ALE * 0.15

Fuente: Adaptado de FAIR Institute State of CRM 2025 y IBM Cost of Data Breach 2025
```

---

## HOJA 7: DASHBOARD

### Visualizaciones a implementar

```
1. RADAR CHART (Gráfico de araña) — Puntuaciones por pilar CIA
   Datos: IGM_C, IGM_I, IGM_A, Score_Auth/Traz, Score_Cultura
   Colores: Azul corporativo para organización; Gris para benchmark sectorial
   Tamaño: Grande (12x12 cm), posición superior izquierda

2. GAUGE CHART (Velocímetro) — IGM-CIA Global
   Valor: IGM_CIA (celda de referencia)
   Rangos coloreados: Rojo (1-2), Naranja (2-3), Amarillo (3-3.5), Verde (3.5-4.5), Azul (4.5-5)
   Posición: Centro superior

3. BAR CHART HORIZONTAL — Top 5 áreas de mejora
   Datos: 5 sub-dominios con menor puntuación
   Orden: Ascendente (peor a mejor)
   Referencia: Línea vertical en valor 3.0 (mínimo aceptable)

4. HEATMAP TABLE — Madurez por control y pilar
   Filas: Cada sub-dominio CIA (15 filas)
   Columnas: Puntuación actual | Benchmark sector | GAP
   Formato condicional tricolor (rojo-amarillo-verde)

5. KPI CARDS (Tarjetas de indicadores clave)
   Card 1: IGM-CIA general con delta vs. año anterior (si disponible)
   Card 2: Número de alertas críticas activas
   Card 3: ROSI estimado (%)
   Card 4: Nivel de madurez (texto con color)
   Card 5: Percentil vs. sector

6. TABLA PLAN DE ACCIÓN (generada automáticamente)
   Columnas: Área | IGM actual | IGM objetivo | Brecha | Acciones recomendadas | Plazo | Marco normativo
   Ordenada por: Brecha descendente (prioridad automática)
   Pre-rellena recomendaciones basadas en puntuación < 3.0
```

---

## GUÍA DE IMPLEMENTACIÓN TÉCNICA

### Paso 1: Configuración inicial
```excel
// Habilitar herramientas de análisis en Excel:
Archivo → Opciones → Complementos → Herramientas para análisis → Aceptar

// Definir nombres de rango para facilitar fórmulas:
Fórmulas → Administrador de nombres → Nuevo:
  IGM_C_Scores     = IGM_CALC!$I$2:$I$5000
  IGM_I_Scores     = IGM_CALC!$N$2:$N$5000
  IGM_A_Scores     = IGM_CALC!$S$2:$S$5000
  IGM_CIA_Scores   = IGM_CALC!$T$2:$T$5000
  Sectores         = DATOS_RAW!$C$2:$C$5000
```

### Paso 2: Importación desde Google Forms / LimeSurvey
```
Los formularios online exportan en .csv o .xlsx.
Proceso de importación:
  1. Exportar respuestas como .csv (UTF-8)
  2. Abrir en Excel con asistente de importación
  3. Mapear columnas a estructura DATOS_RAW
  4. Aplicar tablas de CODIFICACION mediante VLOOKUP
  5. Verificar rangos de validación (1-5)
  6. Refrescar tablas dinámicas (Ctrl+Alt+F5)
```

### Paso 3: Protección de fórmulas
```
Proteger hojas de cálculo (excepto celdas amarillas de entrada):
  Revisar → Proteger hoja → Contraseña → Solo permitir:
    - Seleccionar celdas desbloqueadas
    - Rellenar celdas amarillas (Input)
    - Filtrar (para tablas dinámicas)
```

---

## MÉTRICAS CLAVE CALCULADAS AUTOMÁTICAMENTE

| Métrica | Fórmula | Ubicación | Referencia |
|---|---|---|---|
| IGM_C | Media ponderada sub-dominios C | IGM_CALC col. I | NIST CSF / ENS |
| IGM_I | Media ponderada sub-dominios I | IGM_CALC col. N | ISO 27001 / NIST |
| IGM_A | Media ponderada sub-dominios A | IGM_CALC col. S | DORA / ISO 22301 |
| IGM_CIA | Media ponderada sectorial C+I+A | IGM_CALC col. T | CMMI / C2M2 |
| ALE | Frecuencia × Magnitud pérdida | ROI_FAIR B12 | FAIR Institute |
| ROSI | (Beneficio - Inversión) / Inversión × 100 | ROI_FAIR B15 | FAIR / NIST |
| Payback | Inversión / (Beneficio/12) | ROI_FAIR B16 | Análisis financiero |
| Percentil sectorial | PERCENTRANK vs. muestra sector | BENCHMARK | ENISA NIS Inv. 2025 |
| Alertas críticas | COUNT condición alerta | IGM_CALC col. W | ENS / NIS2 |
| GAP vs. benchmark | IGM individual - IGM mediana sector | BENCHMARK | Análisis comparativo |

---

*Plantilla Excel CIA Triad Survey Kit v2025 · Basada en: FAIR Institute 2025, IBM Cost of Data Breach 2025, ENISA NIS Investments 2025, NIST CSF 2.0, ISO/IEC 27001:2022, C2M2 v2.1*
