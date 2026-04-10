# 📊 PLANTILLA DE CÁLCULO IGM Y ROI
## Encuesta FAICP 2025–2026: Especificación para Excel / LibreOffice Calc / Google Sheets

---

> *"Lo que no se mide no se gestiona. Lo que se mide sin fórmula no se compara. Y lo que se compara sin contexto produce ansiedad bien estructurada."*

**Versión:** 1.0 — Abril 2026 | **Formato destino:** .xlsx / LibreOffice / Google Sheets

---

## ESTRUCTURA DEL LIBRO DE TRABAJO

```
📁 FAICP_IGM_ROI_Calculator_v1.xlsx
├── 📋 HOJA 1: Datos_Encuesta       → Entrada de datos crudos por organización
├── 📊 HOJA 2: Calculo_IGM          → Cálculo automático del IGM-FAICP
├── 💰 HOJA 3: Calculo_ROI          → Modelo ROSI para inversiones ciber-IA
├── 🗺️  HOJA 4: Benchmark_CCAA      → Comparativa territorial interactiva
├── 📈 HOJA 5: Dashboard            → Panel de indicadores consolidado
└── 📖 HOJA 6: Instrucciones        → Guía de uso y glosario
```

---

## HOJA 1 — DATOS_ENCUESTA

### Estructura de columnas (una fila = una organización)

| Col. | Campo | Tipo | Valores |
|------|-------|------|---------|
| A | ID_Org | Numérico | 1, 2, 3... (anonimizado) |
| B | Fecha_Respuesta | Fecha | DD/MM/AAAA |
| C | Cargo | Categórico | 1-10 (ver P0.1) |
| D | CCAA | Categórico | 1-19 (ver P0.2) |
| E | Sector | Categórico | 1-15 (ver P0.3) |
| F | Tamaño | Ordinal | 1-6 (ver P0.4) |
| G | NIS2_Status | Categórico | 1-4 (ver P0.5) |
| H | Presupuesto_TIC_Pct | Ordinal | 1-6 (ver P0.6) |
| I–N | P1.1–P1.6 (Gobernar) | Ordinal/Convertido | 1-5 |
| O–S | P2.1–P2.5 (Identificar) | Ordinal/Convertido | 1-5 |
| T–Y | P3.1–P3.6 (Proteger) | Ordinal/Convertido | 1-5 |
| Z–AD | P4.1–P4.5 (Detectar) | Ordinal/Convertido | 1-5 |
| AE–AH | P5.1–P5.4 (Responder) | Ordinal/Convertido | 1-5 |
| AI–AK | P6.1–P6.3 (Recuperar) | Ordinal/Convertido | 1-5 |
| AL | P10.1 Madurez_Autopercibida | Numérico | 1-10 (÷2 para escala 1-5) |

---

## HOJA 2 — CALCULO_IGM

### Fórmulas por Sub-índice

**Sub-índice Gobernar (IGM_GV) — Peso: 0.20**
```excel
=PROMEDIO(Datos_Encuesta!I[fila]:Datos_Encuesta!N[fila])
```

**Sub-índice Identificar (IGM_ID) — Peso: 0.20**
```excel
=PROMEDIO(Datos_Encuesta!O[fila]:Datos_Encuesta!S[fila])
```

**Sub-índice Proteger (IGM_PR) — Peso: 0.25**
```excel
=PROMEDIO(Datos_Encuesta!T[fila]:Datos_Encuesta!Y[fila])
```

**Sub-índice Detectar (IGM_DE) — Peso: 0.15**
```excel
=PROMEDIO(Datos_Encuesta!Z[fila]:Datos_Encuesta!AD[fila])
```

**Sub-índice Responder (IGM_RS) — Peso: 0.10**
```excel
=PROMEDIO(Datos_Encuesta!AE[fila]:Datos_Encuesta!AH[fila])
```

**Sub-índice Recuperar (IGM_RC) — Peso: 0.10**
```excel
=PROMEDIO(Datos_Encuesta!AI[fila]:Datos_Encuesta!AK[fila])
```

**IGM-FAICP Total**
```excel
=(0.20*IGM_GV)+(0.20*IGM_ID)+(0.25*IGM_PR)+(0.15*IGM_DE)+(0.10*IGM_RS)+(0.10*IGM_RC)
```

**Nivel de Madurez (etiqueta)**
```excel
=SI(IGM_TOTAL<1.5,"CRÍTICO",SI(IGM_TOTAL<2.5,"EMERGENTE",SI(IGM_TOTAL<3.5,"DESARROLLADO",SI(IGM_TOTAL<4.5,"AVANZADO","LÍDER"))))
```

**Brecha Percepción-Realidad**
```excel
=(Datos_Encuesta!AL[fila]/2) - IGM_TOTAL
```
*Valores positivos = sobreestimación (lo más habitual)*

### Indicadores Agregados (análisis muestral)

```excel
IGM_Media_Nacional   = PROMEDIO([rango IGM_TOTAL])
IGM_Mediana_Nacional = MEDIANA([rango IGM_TOTAL])
IGM_DesvTip          = DESVEST([rango IGM_TOTAL])
IGM_IC95_Superior    = Media + (1.96 * DesvTip / RAIZ(N))
IGM_IC95_Inferior    = Media - (1.96 * DesvTip / RAIZ(N))
IGM_Por_CCAA         = PROMEDIO.SI(col_CCAA, [código_CCAA], [rango IGM_TOTAL])
IGM_Por_Sector       = PROMEDIO.SI(col_Sector, [código_sector], [rango IGM_TOTAL])
```

---

## HOJA 3 — CALCULO_ROI (Metodología ROSI + FAIR)

### Sección A: Cuantificación del Riesgo Base

| Campo | Descripción | Fórmula / Input |
|-------|-------------|-----------------|
| LEF | Frecuencia anual de incidentes IA relevantes | Input manual (ej: 0.5 = 1 cada 2 años) |
| SLEF_IA | Frecuencia ajustada por factor de amenaza IA (+26% INCIBE 2025) | `=LEF * 1.26` |
| LM | Coste estimado por incidente (€) | Input manual |
| ALE_Base | Annual Loss Expectancy sin controles | `=LEF * LM` |
| ALE_IA | ALE con factor de amenaza IA | `=SLEF_IA * LM` |

**Coste de referencia (IBM Cost of Data Breach 2025):**
- Enterprise (>1.000 emp.): ~4.9M$ / incidente
- PYME (<50 emp.): ~120.000€ / incidente
- Premium IA adversarial (ENISA estimación): multiplicar × 1.15

### Sección B: Riesgo Residual

| Campo | Descripción | Fórmula |
|-------|-------------|---------|
| Risk_Reduction_Factor | Factor de reducción por nivel IGM (tabla lookup) | Ver tabla abajo |
| ALE_Residual | ALE tras controles FAICP | `=ALE_IA * (1 - Risk_Reduction_Factor)` |
| Riesgo_Evitado_Anual | Pérdida evitada | `=ALE_IA - ALE_Residual` |

**Tabla IGM → Factor de Reducción de Riesgo** *(basada en Ponemon/IBM)*

| Rango IGM | Nivel | Factor Reducción |
|-----------|-------|-----------------|
| 1.0 – 1.5 | Crítico | 5% |
| 1.5 – 2.5 | Emergente | 15% |
| 2.5 – 3.5 | Desarrollado | 35% |
| 3.5 – 4.5 | Avanzado | 55% |
| 4.5 – 5.0 | Líder | 75% |

### Sección C: Cálculo ROSI

| Campo | Descripción | Fórmula |
|-------|-------------|---------|
| Inversion_Ciber_IA_Anual | Inversión anual total en controles FAICP | Input manual |
| ROSI | Return on Security Investment (%) | `=(Riesgo_Evitado - Inversion) / Inversion * 100` |
| Payback_Años | Años para recuperar inversión | `=Inversion / Riesgo_Evitado_Anual` |
| NPV_5años | Valor Actual Neto a 5 años (descuento 8%) | `=VNA(0.08, [Riesgo_Evitado × 5 celdas]) - Inversion` |

**Benchmarks ROSI sector seguridad (Ponemon Institute):** 138%–215%

---

## HOJA 4 — BENCHMARK_CCAA

```
Filas:    17 CCAA + Ceuta/Melilla
Columnas: IGM_GV | IGM_ID | IGM_PR | IGM_DE | IGM_RS | IGM_RC | IGM_Total | N_Orgs | Gap_vs_Nacional | Ranking
```

**Formato condicional (semáforo automático):**
- 🔴 Rojo: IGM < 2.5 (Crítico/Emergente)
- 🟡 Amarillo: IGM 2.5–3.5 (Desarrollado)
- 🟢 Verde: IGM > 3.5 (Avanzado/Líder)

---

## HOJA 5 — DASHBOARD (Panel KPI)

**Gráficos recomendados:**
1. **Radar (spider chart)** — 6 funciones FAICP vs. benchmarks nacionales e internacionales
2. **Mapa coroplético** — IGM por CCAA (Power Map o Bing Maps)
3. **Barras apiladas** — Distribución de niveles (Crítico/Emergente/Desarrollado/Avanzado/Líder) por sector
4. **Scatter plot** — Presupuesto ciber (eje X) vs. IGM (eje Y) con línea de tendencia
5. **Waterfall chart** — Brechas vs. nivel objetivo por función
6. **Velocímetro** — IGM Nacional como indicador principal

---

## HOJA 6 — INSTRUCCIONES

### Pasos de uso

1. Exportar respuestas de plataforma de encuesta (CSV) y pegar en Hoja 1
2. Aplicar tabla de conversión para preguntas categóricas a valores numéricos 1-5
3. Ejecutar macro de validación para detectar valores fuera de rango
4. Los cálculos IGM (Hoja 2) son automáticos una vez importados los datos
5. Completar manualmente en Hoja 3: LEF, LM e Inversión_Ciber_IA_Anual
6. Presionar F9 para refrescar tablas dinámicas y gráficos del Dashboard

### Macro de validación (VBA)

```vba
Sub ValidarDatosEncuesta()
    Dim ws As Worksheet
    Dim errores As Integer
    errores = 0
    Set ws = Sheets("Datos_Encuesta")
    For i = 2 To ws.UsedRange.Rows.Count
        For j = 9 To 37  ' Columnas I a AK (preguntas secciones 1-6)
            If ws.Cells(i, j).Value < 1 Or ws.Cells(i, j).Value > 5 Then
                ws.Cells(i, j).Interior.Color = RGB(255, 0, 0)
                errores = errores + 1
            End If
        Next j
    Next i
    MsgBox "Validación completa. Valores fuera de rango: " & errores
End Sub
```

---

*Kit FAICP 2025–2026 · Documento (e) · Versión 1.0 · Abril 2026*
*ROSI: FAIR Institute, Ponemon Institute, ISO/IEC 27005, ENISA Risk Management Framework*
