# 📊 PLANTILLA EXCEL — IGM-CIA y ROI de Ciberseguridad
## Especificación Completa para Implementación en Excel 365 / Google Sheets
### GQM+PRAGMATIC CIA Triad Framework — España 2025

---

> *"Un spreadsheet de ciberseguridad bien construido es el puente entre el CISO
> que habla de riesgos técnicos y el CFO que habla de euros. Sin ese puente,
> ambos vivirán en islas distintas hasta que el incidente los reúna involuntariamente."*

---

## ÍNDICE DE HOJAS DEL LIBRO EXCEL

| # | Nombre Hoja | Tipo | Propósito |
|---|---|---|---|
| 1 | `00_INICIO` | Dashboard | Instrucciones y navegación |
| 2 | `01_DATOS_RAW` | Entrada | Captura de valores brutos de métricas |
| 3 | `02_CODIFICACION` | Procesamiento | Normalización y Score por métrica |
| 4 | `03_IGM_CIA` | Cálculo | Índice Global de Madurez CIA |
| 5 | `04_BENCHMARK` | Comparación | Benchmarking sectorial y temporal |
| 6 | `05_ROI_FAIR` | Modelado | Análisis de Retorno sobre Inversión en Seguridad |
| 7 | `06_ALE_ROSI` | Cálculo | ALE, SLE, ARO y ROSI |
| 8 | `07_DASHBOARD` | Visualización | Dashboard ejecutivo integrado |
| 9 | `08_ROADMAP` | Planificación | Hoja de ruta de implementación con tracking |

---

## HOJA 1: `00_INICIO`

### Estructura

```
A1:  LOGO ORGANIZACIÓN [placeholder imagen]
B1:  [NOMBRE ORGANIZACIÓN]
C1:  Versión del modelo: GQM+PRAGMATIC CIA Triad v2025

A3:  INSTRUCCIONES DE USO
A5:  1. Comience por la hoja 01_DATOS_RAW e introduzca los valores de cada métrica
A6:  2. La hoja 02_CODIFICACION normaliza automáticamente los valores (no editar)
A7:  3. La hoja 03_IGM_CIA calcula el índice global (seleccione sector en B3)
A8:  4. Introduzca el presupuesto y escenarios de riesgo en 05_ROI_FAIR y 06_ALE_ROSI
A9:  5. El 07_DASHBOARD se actualiza automáticamente

A12: HIPERVÍNCULOS DE NAVEGACIÓN RÁPIDA
A13: → 01 Datos Raw     [Ctrl+Click → hoja 01_DATOS_RAW]
A14: → 03 IGM-CIA       [Ctrl+Click → hoja 03_IGM_CIA]
A15: → 05 ROI FAIR      [Ctrl+Click → hoja 05_ROI_FAIR]
A16: → 07 Dashboard     [Ctrl+Click → hoja 07_DASHBOARD]

A20: METADATOS
A21: Fecha de último cálculo: =HOY()
A22: Período de evaluación: [campo editable]
A23: Responsable: [campo editable]
A24: Próxima revisión: =FECHA(AÑO(A21)+0, MES(A21)+1, DÍA(A21))
```

---

## HOJA 2: `01_DATOS_RAW`

### Estructura de columnas

| Col | Campo | Tipo | Descripción |
|---|---|---|---|
| A | ID_Métrica | Texto | M-C01a, M-I02a, etc. |
| B | Nombre_Métrica | Texto | Descripción completa |
| C | Pilar | Desplegable | C / I / A / CIANA |
| D | Objetivo_GQM | Texto | OBJ-NAC-01 a 06 |
| E | Pregunta_GQM | Texto | Pregunta operacional |
| F | Fórmula | Texto | Descripción de fórmula |
| G | Unidad | Texto | %, días, horas, ratio, 0/1, escala |
| H | **Valor_Actual** | **Número — INPUT PRINCIPAL** | Valor medido en período |
| I | Fecha_Medición | Fecha | =HOY() sugerido |
| J | Fuente_Datos | Texto | Sistema fuente del dato |
| K | Umbral_Critico | Número | Valor que activa alerta roja |
| L | Umbral_Objetivo | Número | Valor objetivo (verde) |
| M | Dirección | Desplegable | MAYOR_MEJOR / MENOR_MEJOR |
| N | Frecuencia | Texto | Diaria/Semanal/Mensual/etc. |
| O | PRAGMATIC_Score | Número | Score 0-27 del indicador |
| P | Notas | Texto | Observaciones del responsable |

### Datos pre-cargados (plantilla) — 45 filas (una por sub-métrica)

```excel
Fila 2: M-C01a | MFA Coverage Rate (%) | C | OBJ-NAC-01 | ¿Qué % de cuentas activas tiene MFA? | (Cuentas MFA/Total)×100 | % | [INPUT] | =HOY() | IAM/AAD | 70 | 99 | MAYOR_MEJOR | Mensual | 25 |
Fila 3: M-C01b | Phishing-Resistant MFA Rate (%) | C | OBJ-NAC-01 | ¿Qué % de MFA es resistente al phishing? | (FIDO2/Total MFA)×100 | % | [INPUT] | =HOY() | IAM | 30 | 80 | MAYOR_MEJOR | Mensual | 25 |
Fila 4: M-C01c | MFA Bypass Attempt Rate | C | OBJ-NAC-01 | ¿Cuántos bypass de MFA se detectan? | Alertas/Total intentos | ratio | [INPUT] | =HOY() | SIEM | 0.01 | 0 | MENOR_MEJOR | Semanal | 25 |
... [continúa para las 45 sub-métricas]
```

### Validación de datos en columna H

```excel
Para columnas de tipo %: Validación datos > Decimal > Entre 0 y 100
Para columnas de tipo días: Validación datos > Número entero > Mayor que 0
Para columnas de tipo ratio 0-1: Validación datos > Decimal > Entre 0 y 1
Para columnas de tipo escala: Validación datos > Número entero > Entre 0 y 5

Formato condicional en columna H (por fila):
=SI(M2="MAYOR_MEJOR",
  SI(H2>=L2, "VERDE",         ← ≥ umbral objetivo
   SI(H2>=K2, "AMARILLO",     ← entre crítico y objetivo
    "ROJO")),                  ← por debajo del crítico
  SI(H2<=L2, "VERDE",
   SI(H2<=K2, "AMARILLO",
    "ROJO")))
```

---

## HOJA 3: `02_CODIFICACION`

### Propósito
Transforma los valores brutos de `01_DATOS_RAW` en scores normalizados 0-5 para el cálculo del IGM-CIA. **No editar directamente** — se actualiza automáticamente.

### Fórmula de normalización universal

```excel
Columna A: ID_Métrica (=01_DATOS_RAW!A2 hacia abajo)
Columna B: Valor_Actual (=01_DATOS_RAW!H2)
Columna C: Umbral_Critico (=01_DATOS_RAW!K2)
Columna D: Umbral_Objetivo (=01_DATOS_RAW!L2)
Columna E: Dirección (=01_DATOS_RAW!M2)
Columna F: PRAGMATIC_Score (=01_DATOS_RAW!O2)
Columna G: Peso_PRAGMATIC (=SI(F2>=24,1.2,SI(F2>=18,1.0,SI(F2>=12,0.8,0.5))))

Columna H: Score_Normalizado (0-5) — Fórmula principal:
=SI(E2="MAYOR_MEJOR",
  SI(B2>=D2*1.1, 5,
   SI(B2>=D2, 4,
    SI(B2>=(C2+(D2-C2)*0.75), 3,
     SI(B2>=(C2+(D2-C2)*0.5), 2,
      SI(B2>=C2, 1, 0))))),
  SI(B2<=D2*0.9, 5,
   SI(B2<=D2, 4,
    SI(B2<=(D2+(C2-D2)*0.25), 3,
     SI(B2<=(D2+(C2-D2)*0.5), 2,
      SI(B2<=C2, 1, 0))))))

Columna I: Score_Ponderado = H2 * G2
Columna J: Semáforo = SI(H2>=4,"🟢",SI(H2>=2,"🟡","🔴"))
Columna K: Tendencia = SI(B2>DESPLAZAMIENTO(B2,-1,0),"⬆️",SI(B2<DESPLAZAMIENTO(B2,-1,0),"⬇️","➡️"))
```

---

## HOJA 4: `03_IGM_CIA`

### Panel de configuración sectorial

```excel
B2: Sector organizacional → Desplegable:
    [Financiero_DORA | Salud | Infraestructura_Critica | AAPP | PYME | Defensa]

B3: Año de evaluación → Numérico: 2025
B4: Trimestre → Desplegable: [Q1 | Q2 | Q3 | Q4]

Tabla de pesos por sector (vinculada a B2):
Sector          | w_C  | w_I  | w_A  | w_CIANA
Financiero_DORA | 0,25 | 0,25 | 0,40 | 0,10
Salud           | 0,40 | 0,25 | 0,25 | 0,10
Infra_Critica   | 0,20 | 0,25 | 0,45 | 0,10
AAPP            | 0,30 | 0,30 | 0,30 | 0,10
PYME            | 0,35 | 0,25 | 0,30 | 0,10
Defensa         | 0,30 | 0,30 | 0,20 | 0,20
```

### Cálculo de scores por pilar

```excel
D10: IGM_C = PROMEDIO.SI(02_CODIFICACION!A:A,"M-C*",02_CODIFICACION!I:I)
     [PROMEDIO.SI filtra filas cuyo ID empieza por M-C y promedia Score_Ponderado]
     Fórmula alternativa: =SUMAR.SI(A:A,"M-C*",I:I)/CONTAR.SI(A:A,"M-C*")

D11: IGM_I = PROMEDIO.SI(02_CODIFICACION!A:A,"M-I*",02_CODIFICACION!I:I)
D12: IGM_A = PROMEDIO.SI(02_CODIFICACION!A:A,"M-A*",02_CODIFICACION!I:I)
D13: IGM_CIANA = PROMEDIO.SI(02_CODIFICACION!A:A,"M-AT*",02_CODIFICACION!I:I)

[Recuperar pesos del sector seleccionado]
E10: w_C = BUSCARV(B2, TablasPesos, 2, FALSO)
E11: w_I = BUSCARV(B2, TablasPesos, 3, FALSO)
E12: w_A = BUSCARV(B2, TablasPesos, 4, FALSO)
E13: w_CIANA = BUSCARV(B2, TablasPesos, 5, FALSO)

[IGM-CIA Global]
D16: IGM_CIA = D10*E10 + D11*E11 + D12*E12 + D13*E13

[Nivel de madurez]
D17: Nivel = SI(D16>=4,"Optimizado",SI(D16>=3,"Gestionado",
              SI(D16>=2,"Definido",SI(D16>=1,"Formativo","Inicial"))))
D18: Color = SI(D16>=4,"🟢",SI(D16>=2,"🟡","🔴"))
```

### Gráfico de radar integrado (Gráfico de araña)

```excel
Rango de datos para gráfico de radar:
Categorías: C3:C6 ["Confidencialidad","Integridad","Disponibilidad","CIANA"]
Serie Actual: D10:D13
Serie Objetivo: {4,4,4,4} (línea de referencia)
Serie Benchmark sector: [vinculado a hoja 04_BENCHMARK]

Título: "IGM-CIA — " & B2 & " — " & B3 & " Q" & B4
Tipo gráfico: Radar con marcadores
Escala: 0-5
Colores: Azul oscuro (Actual) | Gris (Objetivo) | Verde (Benchmark)
```

---

## HOJA 5: `05_ROI_FAIR`

### Panel de entradas FAIR (Factor Analysis of Information Risk)

```excel
SECCIÓN A — ACTIVOS Y ESCENARIOS DE RIESGO

A3:  Nombre del activo de información: [campo libre]
B3:  Clasificación ENS: Desplegable [Bajo | Medio | Alto | Crítico]
C3:  Valor del activo (€): [campo numérico]

A7:  ESCENARIO DE RIESGO 1 (Principal amenaza)
A8:  Descripción amenaza: [campo libre - ej. "Ransomware en sistemas ERP"]
A9:  Probabilidad de ocurrencia anual (ARO): [0,0 - 1,0]
A10: Factor de exposición (EF %): [0-100% del activo afectado]
A11: Tiempo de inactividad estimado (horas): [campo numérico]
A12: Coste por hora de inactividad (€/h): [campo numérico]

SECCIÓN B — CÁLCULOS ALE (Annual Loss Expectancy)

B15: SLE (Single Loss Expectancy):
     =C3*(A10/100) + A11*A12 + [Costes_Notificacion_RGPD] + [Costes_Forenses]
     Componentes del SLE:
     - Daño directo al activo: =C3*(A10/100)
     - Coste de inactividad: =A11*A12
     - Costes de notificación RGPD/NIS2: [campo editable — mínimo 50.000€]
     - Costes forenses y recuperación: [campo editable]
     - Daño reputacional estimado: [campo editable — multiplicador opcional]

B16: ALE (Annual Loss Expectancy):
     =A9 * B15
     [Comentario: ALE es el coste esperado promedio anual de este escenario]

SECCIÓN C — INVERSIÓN EN CONTROL

C20: Nombre del control: [ej. "Plataforma PAM + MFA resistente phishing"]
C21: CAPEX del control (€): [inversión inicial]
C22: OPEX anual del control (€): [coste de operación anual]
C23: Reducción de probabilidad esperada (Δ ARO %): [0-100%]
C24: Reducción de impacto esperada (Δ EF %): [0-100%]

C27: ALE_antes = B16 [referencia]
C28: ARO_nuevo = A9 * (1 - C23/100)
C29: EF_nuevo = A10 * (1 - C24/100)
C30: SLE_nuevo = C3*(C29/100) + A11*A12*(1-C23/100) + [Costes fijos restantes]
C31: ALE_despues = C28 * C30

SECCIÓN D — ROSI (Return on Security Investment)

D35: Beneficio_anual = C27 - C31   [Reducción del ALE]
D36: TCO_3anos = C21 + C22*3       [Total Cost of Ownership 3 años]
D37: ROSI = (D35*3 - TCO_3anos) / TCO_3anos * 100
     [ROSI positivo = inversión justificada]
D38: Payback_meses = C21 / (D35/12)
     [Meses para recuperar inversión inicial]

D40: VAN_3anos = D35/(1+0.08)^1 + D35/(1+0.08)^2 + D35/(1+0.08)^3 - C21
     [Valor Actual Neto a tasa de descuento del 8% (tasa corporativa sugerida)]
D41: TIR_aproximada = [función TIR de Excel sobre flujos de caja anuales]
     =TIR({-C21; D35-C22; D35-C22; D35-C22})
```

### Tabla de escenarios de riesgo predefinidos (España 2025)

```excel
ESCENARIOS PRE-CARGADOS (ajustar probabilidades a sector):

| # | Escenario | ARO_ref | EF_ref | Coste_Base_ref | Marco |
|---|---|---|---|---|---|
| 1 | Ransomware corporativo | 0,15 | 60% | 2.730.000€ | Verizon 2025 |
| 2 | Brecha datos RGPD notificable | 0,25 | 30% | 4.440.000€ | IBM 2025 |
| 3 | Compromiso cuentas privilegiadas | 0,20 | 45% | 3.200.000€ | Verizon 2025 |
| 4 | Ataque supply chain / tercero | 0,12 | 50% | 2.900.000€ | ENISA 2025 |
| 5 | DDoS a servicios críticos | 0,30 | 25% | 800.000€ | INCIBE 2025 |
| 6 | Phishing + BEC | 0,40 | 15% | 620.000€ | Verizon 2025 |
| 7 | Exfiltración por insider | 0,08 | 70% | 5.200.000€ | Ponemon 2024 |
| 8 | Vulnerabilidad edge/VPN explotada | 0,35 | 40% | 1.800.000€ | Verizon 2025 |

Notas sobre las referencias:
- Coste_Base_ref: coste medio global del tipo de incidente
- ARO_ref: probabilidad anual de ocurrencia de referencia (ajustar por sector y país)
- Los datos para España pueden ser ~0,6× los valores globales IBM (PBI ajustado)
```

---

## HOJA 6: `06_ALE_ROSI`

### Consolidación multi-escenario

```excel
TABLA RESUMEN DE TODOS LOS ESCENARIOS

| Escenario | ALE_antes | ALE_despues | Inversión | ROSI | Payback | Prioridad |
|---|---|---|---|---|---|---|
| Ransomware | =05_ROI_FAIR!C27 | =05_ROI_FAIR!C31 | =05_ROI_FAIR!C21 | =05_ROI_FAIR!D37 | =05_ROI_FAIR!D38 | [auto-calc] |
[... tablas vinculadas a múltiples instancias del modelo por escenario]

TOTAL ALE PORTFOLIO: =SUMA(C_column)  ← Riesgo total anual sin inversiones
TOTAL INVERSIÓN PLAN: =SUMA(E_column) ← Inversión total propuesta
ROSI PORTFOLIO: =(SUMA(B)-SUMA(C))/SUMA(E)*100

ANÁLISIS DE SENSIBILIDAD:
Tabla de dos variables (Datos > Análisis Y si > Tabla de datos)
Variable fila: ARO (0,05 a 0,50 en intervalos de 0,05)
Variable columna: Inversión (50%−150% del presupuesto base)
Resultado: ROSI resultante en cada celda de la tabla

GRÁFICO COMPARATIVO (Barras apiladas):
Serie 1: ALE antes de controles
Serie 2: ALE después de controles
Serie 3: Coste total controles
Eje secundario: ROSI (%)
```

---

## HOJA 7: `07_DASHBOARD`

### Layout del Dashboard Ejecutivo (para pantalla 1920×1080)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  DASHBOARD IGM-CIA | [ORG] | [FECHA] | [SECTOR]                             ║
╠══════════════╦══════════════╦══════════════╦══════════════╗═════════════════╣
║ IGM-CIA      ║ IGM_C        ║ IGM_I        ║ IGM_A        ║ IGM_CIANA       ║
║ [GRAN KPI]   ║ [KPI]        ║ [KPI]        ║ [KPI]        ║ [KPI]           ║
║ 3,42 / 5,0   ║ 3,1          ║ 3,8          ║ 3,4          ║ 3,2             ║
║ 🟡 DEFINIDO  ║ 🟡           ║ 🟡           ║ 🟡           ║ 🟡             ║
╠══════════════╩══════════════╩══════════════╩══════════════╩═════════════════╣
║                    ║                              ║                          ║
║  GRÁFICO RADAR     ║   TOP 5 MÉTRICAS EN ROJO    ║   TENDENCIA IGM 12M      ║
║  CIA Triad         ║   (Acción inmediata)        ║   (Gráfico línea)        ║
║  [Araña 5 ejes]    ║   • M-I02c: CVE>30d         ║                          ║
║                    ║   • M-C02a: Orphan Accts    ║                          ║
║                    ║   • M-A05b: Backup Isolation║                          ║
║                    ║   • M-AT02d: Exec Training  ║                          ║
║                    ║   • M-C06b: AI Policy       ║                          ║
╠════════════════════╬══════════════════════════════╩══════════════════════════╣
║  ALE PORTFOLIO     ║   ROSI POR CONTROL                                      ║
║  €4,8M/año riesgo  ║   [Gráfico barras horizontales: ROSI % por control]    ║
║  €1,2M inversión   ║   MFA resistente phishing: 340%                        ║
║  ROSI: 280%        ║   PAM + grabación sesiones: 215%                       ║
╚════════════════════╩════════════════════════════════════════════════════════╝
```

### KPIs dinámicos — Fórmulas

```excel
IGM-CIA Global:  =03_IGM_CIA!D16  (con formato 0,00)
IGM_C:           =03_IGM_CIA!D10
IGM_I:           =03_IGM_CIA!D11
IGM_A:           =03_IGM_CIA!D12
IGM_CIANA:       =03_IGM_CIA!D13
Nivel:           =03_IGM_CIA!D17
Semáforo:        =03_IGM_CIA!D18
ALE_Portfolio:   =06_ALE_ROSI!C_Total
ROSI_Portfolio:  =06_ALE_ROSI!ROSI_Portfolio

Top 5 Métricas Críticas:
=INDICE(01_DATOS_RAW!B:B, COINCIDIR(K.ESIMO.MENOR(02_CODIFICACION!H:H,1), 02_CODIFICACION!H:H, 0))
[Repetir con K.ESIMO.MENOR(...,2) hasta 5]
```

---

## HOJA 8: `08_ROADMAP`

### Tracking de implementación de controles

```excel
COLUMNAS:

A: ID_Control     → Referencia al indicador PRAGMATIC (M-C01a, etc.)
B: Control        → Nombre del control a implementar
C: Prioridad      → [Inmediato | Urgente | Corto | Medio | Largo]
D: Fase           → [1 | 2 | 3 | 4]
E: Responsable    → [campo texto libre]
F: Fecha_Inicio   → [fecha]
G: Fecha_Objetivo → [fecha]
H: Estado         → Desplegable [No_Iniciado | En_Curso | Completado | Bloqueado]
I: % Avance       → Numérico 0-100
J: PRAGMATIC_Score → Referencia automática
K: Score_Actual   → Referencia a 02_CODIFICACION!H
L: Score_Esperado → [campo numérico — score previsto al completar control]
M: Delta_IGM_Estimado → =(L-K)*BUSCARV(A,TablasPesos,2,FALSO)/IndicadoresPilar
N: Coste_Estimado → [numérico €]
O: ROSI_Estimado  → Referencia a 05_ROI_FAIR por fila
P: Notas          → [campo libre]

GRÁFICO GANTT (Formato condicional como Gantt):
Columnas Q:AZ representan meses (Q=Mes1, R=Mes2, etc.)
=SI(Y(Q$1>=F2, Q$1<=G2), 1, 0)  → Formato condicional: 1=color según Estado

RESUMEN ROADMAP:
Total controles: =CONTAR(A:A)
Completados: =CONTAR.SI(H:H,"Completado")
En curso: =CONTAR.SI(H:H,"En_Curso")
% Plan completado: =CONTAR.SI(H:H,"Completado")/CONTAR(H:H)*100
Inversión comprometida: =SUMAR.SI(H:H,"En_Curso",N:N)+SUMAR.SI(H:H,"No_Iniciado",N:N)
Delta IGM-CIA proyectado: =SUMA(M:M)
IGM-CIA objetivo 12m: =03_IGM_CIA!D16 + SUMAR.SI(H:H,"<>Bloqueado",M:M)
```

---

## CONFIGURACIÓN TÉCNICA EXCEL 365

### Tablas estructuradas recomendadas

```excel
Nombre de tabla         | Hoja             | Rango
------------------------|------------------|------------------
tbl_Metricas           | 01_DATOS_RAW     | $A$1:$P$50
tbl_Codificacion       | 02_CODIFICACION  | $A$1:$K$50
tbl_IGM                | 03_IGM_CIA       | $A$1:$E$20
tbl_Benchmark          | 04_BENCHMARK     | $A$1:$H$10
tbl_Escenarios         | 05_ROI_FAIR      | $A$7:$I$15
tbl_ALE_Portfolio      | 06_ALE_ROSI      | $A$1:$P$20
tbl_Roadmap            | 08_ROADMAP       | $A$1:$AZ$60
```

### Nombres de rango definidos

```excel
Nombre            | Referencia
------------------|----------------------------------
IGM_Global        | =03_IGM_CIA!$D$16
IGM_C             | =03_IGM_CIA!$D$10
IGM_I             | =03_IGM_CIA!$D$11
IGM_A             | =03_IGM_CIA!$D$12
IGM_CIANA         | =03_IGM_CIA!$D$13
Sector_Actual     | =03_IGM_CIA!$B$2
ALE_Total         | =06_ALE_ROSI!$C$Total
ROSI_Portfolio    | =06_ALE_ROSI!$ROSI_Portfolio
TablasPesos       | =03_IGM_CIA!$H$5:$M$12
```

### Macros VBA recomendadas (módulo basico)

```vba
' Macro 1: Actualizar fecha de último cálculo
Sub ActualizarFechas()
    Sheets("00_INICIO").Range("A21").Value = Now()
    MsgBox "Dashboard actualizado: " & Format(Now(), "dd/mm/yyyy hh:mm"), vbInformation
End Sub

' Macro 2: Exportar dashboard como PDF
Sub ExportarDashboardPDF()
    Dim ruta As String
    ruta = Environ("USERPROFILE") & "\Desktop\IGM_CIA_" & _
           Format(Now(), "YYYYMMDD") & ".pdf"
    Sheets("07_DASHBOARD").ExportAsFixedFormat _
        Type:=xlTypePDF, Filename:=ruta, Quality:=xlQualityStandard
    MsgBox "PDF exportado en: " & ruta, vbInformation
End Sub

' Macro 3: Reset de valores raw (para nuevo período)
Sub NuevoPeriodo()
    If MsgBox("¿Iniciar nuevo período? Los valores actuales se moverán a BENCHMARK.", _
              vbYesNo) = vbYes Then
        ' Copiar valores actuales a columna histórica en BENCHMARK
        Sheets("04_BENCHMARK").Range("C2:C50").Value = _
            Sheets("01_DATOS_RAW").Range("H2:H50").Value
        ' Limpiar columna H de datos raw
        Sheets("01_DATOS_RAW").Range("H2:H50").ClearContents
        MsgBox "Nuevo período iniciado. Introduzca los nuevos valores en 01_DATOS_RAW.", vbInformation
    End If
End Sub
```

---

## INSTRUCCIONES DE IMPLEMENTACIÓN EN GOOGLE SHEETS

Para equipos que prefieren Google Sheets sobre Excel:

```
1. Crear libro en Google Sheets con las 9 pestañas descritas
2. Reemplazar funciones Excel:
   - BUSCARV → BUSCARV (idéntica en Sheets)
   - COINCIDIR → COINCIDIR (idéntica)
   - K.ESIMO.MENOR → K.ESIMO.MENOR (idéntica)
   - TIR → IRR en inglés / TIR en español
   - DESPLAZAMIENTO → DESREF
3. Para macros: usar Google Apps Script en lugar de VBA
4. Para export PDF: Archivo > Descargar > PDF
5. Compartir con equipo: derechos de edición solo en columna H de 01_DATOS_RAW
6. Proteger hojas de cálculo (02_CODIFICACION, 03_IGM_CIA): permisos solo lectura
```

---

*Plantilla Excel IGM-CIA + ROI v2025 · Basada en: FAIR (Factor Analysis of Information Risk), NIST SP 800-55 R1, ISO/IEC 27004:2016, ROSI Model (Gordon & Loeb), COSO ERM, Verizon DBIR 2025, IBM Cost of Data Breach 2025*
