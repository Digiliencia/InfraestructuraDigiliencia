# Plantilla Excel GQM-IGM-ROSI
## Especificación Técnica Extendida con Lógica GQM + PRAGMATIC
### Kit GQM-PRAGMATIC v2025.1 — Archivo: `GQM_IGM_ROSI_v2025.xlsx`

---

> *"La hoja de cálculo es el idioma universal del CFO. Esta plantilla es la traducción certificada del ciberriesgo al único idioma que hace que el Consejo preste atención: los euros."*

---

## Resumen de la Plantilla

**Nombre del archivo:** `GQM_IGM_ROSI_v2025.xlsx`
**Hojas (pestañas):** 10 pestañas interconectadas
**Compatibilidad:** Microsoft Excel 365 / Google Sheets / LibreOffice Calc

| # | Pestaña | Color | Propósito |
|---|---------|:-----:|-----------|
| 1 | `🏠 INICIO` | Azul oscuro | Portada, instrucciones, índice de la plantilla |
| 2 | `🎯 GQM_OBJETIVOS` | Verde oscuro | Árbol GQM: ON → OO → Preguntas → Métricas |
| 3 | `📊 MÉTRICAS_50` | Verde | Catálogo de las 50 métricas: valor actual, objetivo, semáforo |
| 4 | `🔬 PRAGMATIC` | Azul | Puntuaciones PRAGMATIC de cada métrica (9 criterios × 50 métricas) |
| 5 | `🧮 IGM_CÁLCULO` | Amarillo | Cálculo del IGM ponderado por componente COSO (5 componentes) |
| 6 | `💰 ALE_FAIR` | Naranja | Módulo de cuantificación del riesgo: ALE / SLE / ARO por escenario |
| 7 | `📈 ROSI_ROI` | Naranja oscuro | ROSI por control y ROI del programa completo |
| 8 | `🚦 DIAGNÓSTICO` | Rojo/Verde | Semáforo de los 14 IATs + plan de mejora priorizado |
| 9 | `📉 DASHBOARD` | Azul claro | Cuadro de mando visual: radar, barras, velocímetro, sparklines |
| 10 | `📝 REPORTE` | Blanco | Borrador de informe ejecutivo generado automáticamente |

---

## Pestaña 2: GQM_OBJETIVOS — Árbol de Trazabilidad

### Estructura de Columnas

| Col | Cabecera | Contenido |
|-----|----------|-----------|
| A | Código_ON | ON-1 … ON-8 |
| B | Objetivo_Nacional | Texto del objetivo nacional/regulatorio |
| C | Fuente_Regulatoria | ENS / NIS2 / DORA / COSO etc. |
| D | Código_OO | OO-1 … OO-10 |
| E | Objetivo_Organizacional | Texto del objetivo organizacional |
| F | Componente_COSO | C-I / C-II / C-III / C-IV / C-V |
| G | Cód_Métrica | M-GOB-01 … M-ROI-05 |
| H | Denominación_Métrica | Nombre completo de la métrica |
| I | Tipo_Métrica | Cuantitativa / Ordinal / Nominal |
| J | Fuente_Datos | SIEM / IAM / Scanner VUL / etc. |

### Fórmulas de Navegación

```excel
// Filtrar todas las métricas del OO-3
=FILTRAR(G2:H51, D2:D51="OO-3", "Sin resultados")

// Contar métricas por componente COSO
=CONTAR.SI(F2:F51, "C-III")

// Ver cadena completa de una métrica
// (desde ON hasta métrica, usando BUSCARV)
=BUSCARV("M-DET-01", G2:J51, 4, FALSO)  // → fuente de datos
```

---

## Pestaña 3: MÉTRICAS_50 — Registro de Valores Actuales

### Estructura de Columnas

| Col | Cabecera | Contenido | Tipo |
|-----|----------|-----------|------|
| A | Cód_Métrica | M-GOB-01 … M-ROI-05 | Texto |
| B | Denominación | Nombre corto | Texto |
| C | Componente_COSO | C-I a C-V | Lista |
| D | Unidad | %, horas, días, €, 0–5, etc. | Texto |
| E | Valor_Actual | Dato actual de la organización | Número |
| F | Valor_Objetivo | Objetivo aprobado por el Consejo | Número |
| G | Benchmark_Sectorial | Referencia externa (IBM, ENISA, CIS) | Número |
| H | Estado_Semáforo | Fórmula automática | Texto |
| I | Puntuación_IGM | Conversión a escala 1–5 | Número |
| J | Es_IAT | Sí / No | Lista |
| K | Fecha_Medición | Fecha del último dato | Fecha |
| L | Fuente_Dato | Sistema o proceso de origen | Texto |
| M | Notas | Campo libre | Texto |

### Fórmulas Clave

```excel
// Semáforo automático (columna H)
// Para métricas donde mayor = mejor (p.ej.: % MFA)
=SI(E2>=F2*0.95,"🟢 ADECUADO",SI(E2>=F2*0.75,"🟡 MEJORABLE","🔴 CRÍTICO"))

// Para métricas donde menor = mejor (p.ej.: MTTD, TTP)
=SI(E2<=F2*1.05,"🟢 ADECUADO",SI(E2<=F2*1.25,"🟡 MEJORABLE","🔴 CRÍTICO"))

// Conversión a escala IGM 1–5 (normalización lineal)
// Para métricas donde mayor = mejor:
=1 + (E2 - min_ref) / (max_ref - min_ref) * 4

// Para métricas donde menor = mejor:
=1 + (max_ref - E2) / (max_ref - min_ref) * 4

// Contar IATs en estado crítico
=CONTAR.SI.CONJUNTO(J2:J51,"Sí",H2:H51,"🔴 CRÍTICO")
```

---

## Pestaña 4: PRAGMATIC — Puntuaciones por Criterio

### Estructura

| Col | Cabecera | Contenido |
|-----|----------|-----------|
| A | Cód_Métrica | M-GOB-01 … M-ROI-05 |
| B | Denominación | Nombre corto |
| C | P_Predictivo | 1–5 |
| D | R_Relevante | 1–5 |
| E | A_Accionable | 1–5 |
| F | G_Genuino | 1–5 |
| G | M_Significativo | 1–5 |
| H | Ac_Preciso | 1–5 |
| I | T_Oportuno | 1–5 |
| J | I_Independiente | 1–5 |
| K | C_Rentable | 1–5 |
| L | Total_PRAGMATIC | Suma automática |
| M | Clasificación | Fórmula según rango |
| N | Recomendación | Texto automático |

### Fórmulas PRAGMATIC

```excel
// Total PRAGMATIC (columna L)
=SUMA(C2:K2)

// Clasificación (columna M)
=SI(L2>=36,"🟦 Premium",SI(L2>=27,"🟢 Aceptable",
 SI(L2>=18,"🟡 Condicional","🔴 Rediseñar")))

// Recomendación automática (columna N)
=SI(L2>=36,"Implementación prioritaria recomendada",
 SI(L2>=27,"Implementar con mejora en criterios débiles",
 SI(L2>=18,"Revisar criterios con puntuación < 3 antes de implementar",
 "Descartar o rediseñar completamente")))

// Promedios por criterio (fila resumen)
=PROMEDIO(C2:C51)  // Media criterio Predictivo
// ... (repetir para cada criterio D:K)

// Criterio más débil
=INDICE({"P","R","A","G","M","Ac","T","I","C"},
  COINCIDIR(MIN(C53:K53),C53:K53,0))
```

---

## Pestaña 5: IGM_CÁLCULO — Índice Global de Madurez

### Estructura del Cálculo

```
┌──────────────────────────────────────────────────────────────────────────┐
│                      CÁLCULO DEL IGM (escala 1–5)                        │
├────────────────────┬────────────┬───────────────┬──────────┬─────────────┤
│ Componente COSO    │ Peso IGM   │ Métricas      │ Prom.    │ Aportación  │
├────────────────────┼────────────┼───────────────┼──────────┼─────────────┤
│ C-I Gobernanza     │   25%      │ M-GOB-01..05  │ =PROM()  │ =Prom×0,25  │
│ C-II Estrategia    │   20%      │ M-EST-01..05  │ =PROM()  │ =Prom×0,20  │
│ C-III Desempeño    │   30%      │ M-DET..RES    │ =PROM()  │ =Prom×0,30  │
│ C-IV Revisión      │   10%      │ M-REV-01..03  │ =PROM()  │ =Prom×0,10  │
│ C-V Reporte        │   15%      │ M-RPT-01..05  │ =PROM()  │ =Prom×0,15  │
├────────────────────┼────────────┼───────────────┼──────────┼─────────────┤
│ **IGM TOTAL**      │  100%      │ 50 métricas   │          │ =SUMA()     │
└────────────────────┴────────────┴───────────────┴──────────┴─────────────┘
```

### Fórmulas IGM

```excel
// IGM Total
=SUMAPRODUCTO(
  {0.25, 0.20, 0.30, 0.10, 0.15},
  {PROM_C1, PROM_C2, PROM_C3, PROM_C4, PROM_C5}
)

// Clasificación del nivel de madurez
=SI(IGM<2,"🔴 CRÍTICO",SI(IGM<3,"🟠 EMERGENTE",
 SI(IGM<4,"🟡 ESTABLECIDO",SI(IGM<4.6,"🟢 AVANZADO","🟦 LÍDER"))))

// Gap vs. benchmark sectorial
=IGM - BENCHMARK_SECTOR

// Puntuación ponderada por PRAGMATIC
// (métricas de mayor PRAGMATIC tienen más peso en el IGM ponderado)
=SUMAPRODUCTO(I2:I51, L2:L51) / SUMA(L2:L51)
```

### Extensión: IGM Ponderado por PRAGMATIC

Esta extensión premium pondera cada métrica no solo por su componente COSO sino también por su puntuación PRAGMATIC, dando más peso a las métricas de mayor calidad metodológica:

```excel
// IGM-P (IGM ponderado por PRAGMATIC)
// Peso_i = (PRAGMATIC_i / SUMA(PRAGMATIC_todos)) × peso_componente
=SUMAPRODUCTO(
  (I2:I51) × (L2:L51 / SUMA(L2:L51)) × (factor_componente)
)
```

---

## Pestaña 6: ALE_FAIR — Cuantificación del Riesgo

### Módulo ALE Simplificado

Para cada escenario de riesgo (se recomienda modelar entre 3 y 10 escenarios):

| Campo | Fórmula / Instrucción |
|-------|----------------------|
| Nombre del escenario | Texto libre (p.ej.: "Ransomware en sistemas ERP") |
| Descripción | Texto descriptivo del escenario adverso |
| SLE_Directo (€) | Coste de restauración + forense + interrupción operativa |
| SLE_Indirecto (€) | Multas regulatorias + daño reputacional + litigios |
| SLE_Total | `=SLE_Directo + SLE_Indirecto` |
| ARO (eventos/año) | Frecuencia anual estimada (puede ser < 1 si es raro) |
| ALE_SIN_CONTROL (€) | `=SLE_Total × ARO` |
| Reducción_Control (%) | Efectividad estimada del control principal (0%–100%) |
| ALE_CON_CONTROL (€) | `=ALE_SIN × (1 - Reducción_%)` |
| Riesgo_Reducido (€) | `=ALE_SIN - ALE_CON` |

### Módulo FAIR Extendido (opcional)

Para organizaciones con madurez en cuantificación del riesgo, el módulo FAIR incluye:

```excel
// Frecuencia de contacto (FC) — estimación basada en inteligencia de amenazas
// Probabilidad de acción (PA) — base: datos de campañas de phishing/intrusión
// Capacidad del actor de amenaza (TCA) — escala MITRE ATT&CK
// Dificultad de resistencia (RS) — basada en puntuaciones de controles

// LEF = FC × PA    (frecuencia de pérdida probable)
// PLM = f(TCA, RS) (magnitud de pérdida probable, distribución lognormal)
// Risk = LEF × PLM (distribución de resultado de pérdida)

// En Excel simplificado (sin Monte Carlo):
=FC_estimada × PA_estimada × PLM_central
```

---

## Pestaña 7: ROSI_ROI — Retorno sobre la Inversión

### Cálculo del ROSI por Control

```excel
// ROSI de un control específico
= (ALE_SIN_control - ALE_CON_control - Coste_anual_control)
  / Coste_anual_control × 100

// ROSI del programa completo
= (ALE_SIN_total - ALE_CON_total - Inversión_total_ciber)
  / Inversión_total_ciber × 100

// Payback period del control (meses)
= Coste_control / ((ALE_SIN - ALE_CON) / 12)

// Ratio de cobertura (inversión como % del riesgo asumido)
= (Inversión_total_ciber / ALE_SIN_total) × 100
```

### Cuadro de Mando ROI Ejecutivo

```
┌─────────────────────────────────────────────────────────────┐
│              CUADRO EJECUTIVO DE ROI CIBER                   │
├────────────────────────┬────────────────────────────────────┤
│ Inversión total ciber  │ = SUMA(costes_todos_controles)     │
│ ALE total SIN programa │ = SUMA(ALE_sin por escenario)      │
│ ALE total CON programa │ = SUMA(ALE_con por escenario)      │
│ Riesgo total reducido  │ = ALE_sin_total - ALE_con_total    │
│ ROSI del programa      │ = (reducción - inversión)/inversión│
│ Payback period         │ = inversión / (reducción / 12) mes │
│ Ratio inversión/ALE    │ = inversión / ALE_sin × 100        │
│ IGM actual             │ = referencia a IGM_CÁLCULO!IGM     │
│ IGM objetivo (12m)     │ = campo editable                   │
└────────────────────────┴────────────────────────────────────┘
```

---

## Pestaña 8: DIAGNÓSTICO — Semáforo de IATs

### Los 14 Indicadores de Alerta Temprana (IATs)

Cada IAT tiene su fila con:
- Código métrica (referencia a MÉTRICAS_50)
- Valor actual (enlazado automáticamente)
- Semáforo (🔴🟡🟢)
- Acción recomendada (texto automático por rango)
- Responsable sugerido
- Plazo recomendado (0–90 / 3–12 / 12–24 meses)

```excel
// Generar plan de mejora priorizado automáticamente
=SI(H2="🔴 CRÍTICO","0–90 días — Acción urgente — Responsable: CISO/CTO",
 SI(H2="🟡 MEJORABLE","3–12 meses — Planificar — Responsable: CISO",
 "Mantener — Monitorizar trimestralmente"))
```

---

## Pestaña 9: DASHBOARD — Cuadro de Mando Visual

### Gráficos Especificados

1. **Radar COSO (Spider Chart):** 5 ejes (C-I a C-V), valor actual vs. benchmark sectorial
2. **Velocímetro IGM:** Gauge 1–5 con zonas cromáticas y aguja en valor actual
3. **Grid semáforo 14 IATs:** Matriz 7×2 de celdas con formato condicional
4. **Barras ROSI por control:** Barras horizontales ordenadas por ROSI descendente
5. **Barras PRAGMATIC por criterio:** Media de los 9 criterios con línea de umbral ≥ 3
6. **Dispersión PRAGMATIC vs. IGM por métrica:** Scatter chart (50 puntos)
7. **Sparklines de evolución:** Líneas de evolución del IGM en evaluaciones anteriores
8. **Treemap de riesgo:** ALE por escenario (tamaño = magnitud del riesgo)

---

## Pestaña 10: REPORTE — Borrador Ejecutivo Automático

```excel
// Título dinámico
="INFORME GQM-CIBER — "&INICIO!B3&" — "&TEXTO(HOY(),"MMMM YYYY")

// Párrafo IGM
="La organización "&INICIO!B3&" alcanza un IGM de "&TEXTO(IGM_CÁLCULO!B20,"0.0")&
 " sobre 5.0, correspondiente al nivel "&IGM_CÁLCULO!B21&
 ". De los 14 indicadores de alerta temprana, "&DIAGNÓSTICO!B3&
 " se encuentran en estado crítico y requieren acción en los próximos 90 días."

// Párrafo ROSI
="El programa de ciberseguridad obtiene un ROSI de "&TEXTO(ROSI_ROI!B25,"0%")&
 " con un payback period de "&TEXTO(ROSI_ROI!B26,"0")&" meses. "&
 "El riesgo anual reducido por el programa es de €"&TEXTO(ROSI_ROI!B24,"#,##0")&"."
```

---

*Plantilla Excel GQM-IGM-ROSI — Kit GQM-PRAGMATIC v2025.1 | Abril 2026*
*Metodología: GQM (Basili 1994) · PRAGMATIC (Brotby & Hinson 2013) · ALE/SLE/ARO (NIST SP 800-30) · FAIR (OpenFAIR 2023) · COSO ERM 2017*
