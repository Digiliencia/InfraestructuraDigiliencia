# PLANTILLA DE EXCEL PARA CÁLCULO DEL IGM-DREAD Y ROI DE CIBERSEGURIDAD
## Especificación Técnica Completa para Implementación en Microsoft Excel / LibreOffice Calc
### Kit de Encuesta DREAD · Edición 2025–2026

---

> *"Lo que no se mide, no se gestiona. Lo que no se gestiona, se deteriora. Y lo que se deteriora en ciberseguridad, eventualmente sale en los titulares."*

---

## ESTRUCTURA DEL LIBRO DE EXCEL

El libro de cálculo `DREAD_IGM_ROI_Calculator_2026.xlsx` se organiza en **9 hojas de trabajo** con la siguiente estructura:

```
DREAD_IGM_ROI_Calculator_2026.xlsx
├── 00_PORTADA
├── 01_DATOS_ENCUESTA
├── 02_IGM_POR_DIMENSION
├── 03_IGM_GLOBAL_PONDERADO
├── 04_BENCHMARKING_SECTORIAL
├── 05_ROI_CIBERSEGURIDAD
├── 06_SCORING_DREAD_AMENAZAS
├── 07_DASHBOARD_EJECUTIVO
└── 08_INSTRUCCIONES
```

---

## HOJA 00_PORTADA

**Propósito:** Identificación del documento, metadatos y control de versiones.

| Celda | Contenido | Tipo | Notas |
|-------|-----------|------|-------|
| B2 | Logo organización | Imagen | Insertar imagen; dimensiones 200x80 px recomendado |
| B5 | Nombre de la organización | Texto libre | |
| B6 | CIF/NIF | Texto libre | Opcional para anonimización |
| B7 | Sector (lista desplegable) | Validación lista | Opciones: ver P0.1 de la encuesta |
| B8 | Tamaño organización | Validación lista | Opciones: ver P0.2 |
| B9 | Responsable del análisis | Texto libre | |
| B10 | Cargo | Texto libre | |
| B11 | Fecha de evaluación | Fecha | Formato DD/MM/AAAA |
| B12 | Versión del documento | Texto | v1.0 por defecto |
| B15 | CLASIFICACIÓN DEL DOCUMENTO | Lista desplegable | USO INTERNO / CONFIDENCIAL / RESTRINGIDO |

**Celda de resumen ejecutivo (B20–B25):**
- IGM-DREAD Global (referencia automática desde hoja 03)
- Nivel de madurez (fórmula IF sobre IGM-DREAD)
- Puntuación más baja por dimensión (MIN de las 5 dimensiones)
- Dimensión crítica prioritaria (INDEX/MATCH sobre MIN)
- ROI estimado de las inversiones en ciberseguridad (referencia desde hoja 05)

---

## HOJA 01_DATOS_ENCUESTA

**Propósito:** Entrada de datos brutos de la encuesta. Una fila por encuestado/organización.

### Estructura de columnas

| Col | Campo | Tipo de dato | Valores permitidos | Notas |
|-----|-------|-------------|-------------------|-------|
| A | ID_Encuestado | Número | 1, 2, 3... | Autogenerado |
| B | Fecha_Respuesta | Fecha | DD/MM/AAAA | |
| C | Sector | Lista | 1–12 (según P0.1) | Usar codificación numérica |
| D | Tamaño | Lista | 1–6 (según P0.2) | |
| E | Rol | Lista | 1–8 (según P0.3) | |
| F | Madurez_Percibida | Número | 1–5 | P0.4 |
| G | Operador_NIS2 | Lista | 0=No / 1=Esencial / 2=Importante / 3=En_proceso | P0.5 |
| H–L | P1.1 a P1.4 | Número | 1–6 | Bloque 1 |
| M–R | P2.1 a P2.5 | Número | 1–6 | Bloque 2 — Daño |
| S–X | P3.1 a P3.5 | Número | 1–6 | Bloque 3 — Reproducibilidad |
| Y–AD | P4.1 a P4.5 | Número | 1–6 | Bloque 4 — Explotabilidad |
| AE–AI | P5.1 a P5.5 | Número | 1–6 | Bloque 5 — Usuarios Afectados |
| AJ–AM | P6.1 a P6.4 | Número | 1–6 | Bloque 6 — Descubribilidad |
| AN–AR | P7.1 a P7.5 | Número | 1–6 | Bloque 7 — Automatización |
| AS–AW | P8.1 a P8.5 | Número | 1–6 | Bloque 8 — Frameworks |
| AX–AZ | P9.1 a P9.3 | Número | 1–6 | Bloque 9 — Escala nacional |
| BA–BD | P10.1 a P10.4 | Número | 1–6 | Bloque 10 — Cultura |
| BE–BG | P11.1 a P11.3 | Número | 1–6 | Bloque 11 — Prospectiva |

**Fórmulas de validación de datos:**
```excel
=IF(COUNTA(M2:R2)=6, "✓ COMPLETO", "⚠ INCOMPLETO — "&(6-COUNTA(M2:R2))&" campos vacíos")
```

**Fórmula de consistencia cruzada (P0.4 vs. P7.1):**
```excel
=IF(ABS(F2-AN2)>2, "⚠ REVISAR: Madurez percibida y automatización inconsistentes", "✓ OK")
```

---

## HOJA 02_IGM_POR_DIMENSION

**Propósito:** Calcular el score de madurez para cada una de las cinco dimensiones DREAD.

### Fórmulas de cálculo por dimensión

**Dimensión D — Daño:**
```excel
Score_D = AVERAGE(M2:R2)  [media de P2.1 a P2.5, escala 1-6 renormalizada a 1-5]
```
Fórmula de renormalización de escala 1–6 a escala 1–5:
```excel
=((valor_raw - 1) / (6 - 1)) * (5 - 1) + 1
```

**Dimensión R — Reproducibilidad:**
```excel
Score_R = AVERAGE(S2:X2)  [media de P3.1 a P3.5]
```

**Dimensión E — Explotabilidad:**
```excel
Score_E = AVERAGE(Y2:AD2)  [media de P4.1 a P4.5]
```

**Dimensión A — Usuarios Afectados:**
```excel
Score_A = AVERAGE(AE2:AI2)  [media de P5.1 a P5.5]
```

**Dimensión Disc — Descubribilidad:**
```excel
Score_Disc = AVERAGE(AJ2:AM2)  [media de P6.1 a P6.4]
```

### Tabla de resultados (por organización)

| Columna | Fórmula | Descripción |
|---------|---------|-------------|
| C | =Score_D | Madurez Daño |
| D | =Score_R | Madurez Reproducibilidad |
| E | =Score_E | Madurez Explotabilidad |
| F | =Score_A | Madurez Usuarios Afectados |
| G | =Score_Disc | Madurez Descubribilidad |
| H | =MIN(C2:G2) | Dimensión más débil (valor) |
| I | =INDEX({"D","R","E","A","Disc"},MATCH(MIN(C2:G2),C2:G2,0)) | Dimensión más débil (nombre) |
| J | =MAX(C2:G2) | Dimensión más fuerte (valor) |

### Gráfico de radar por organización

**Instrucciones para crear el gráfico de radar (Spider Chart):**
1. Seleccionar C2:G2 (los 5 scores de dimensión)
2. Insertar → Gráfico → Radar → Radar con marcadores
3. Títulos de eje: D, R, E, A, Disc
4. Escala: 1 a 5
5. Añadir línea de referencia al valor 3.0 (línea de madurez "Definido")
6. Color de relleno: degradado azul-cian para valores ≥ 3.0; naranja para < 3.0

---

## HOJA 03_IGM_GLOBAL_PONDERADO

**Propósito:** Calcular el Índice Global de Madurez DREAD (IGM-DREAD) con pesos diferenciados.

### Tabla de pesos configurables

| Fila | Dimensión | Peso por defecto | Peso sectorial (editable) | Justificación |
|------|-----------|-----------------|--------------------------|---------------|
| 3 | D — Daño | 0.25 | [celda editable amarilla] | Mayor impacto en negocio y regulación |
| 4 | R — Reproducibilidad | 0.15 | [celda editable amarilla] | Proxy de madurez exploit |
| 5 | E — Explotabilidad | 0.20 | [celda editable amarilla] | Democratización del ataque por IA |
| 6 | A — Usuarios Afectados | 0.25 | [celda editable amarilla] | Escala ciudadana, NIS2 |
| 7 | Disc — Descubribilidad | 0.15 | [celda editable amarilla] | Menor por controversia metodológica |
| 8 | **TOTAL** | **1.00** | =SUM(C3:C7) — validación | Debe sumar exactamente 1.00 |

**Validación de suma de pesos:**
```excel
=IF(SUM(C3:C7)=1, "✓ PESOS OK", "⚠ ERROR: Los pesos suman "&SUM(C3:C7)&" (deben sumar 1.00)")
```

### Fórmula del IGM-DREAD

```excel
IGM_DREAD = SUMPRODUCT(Score_D:Score_Disc, Peso_D:Peso_Disc)
```

Implementación en Excel:
```excel
=SUMPRODUCT(C3:C7, Hoja02!C2:G2)
```

### Presets de pesos por sector (tabla de referencia)

| Sector | w_D | w_R | w_E | w_A | w_Disc | Justificación |
|--------|-----|-----|-----|-----|--------|---------------|
| Infraestructuras críticas (energía, agua) | 0.35 | 0.10 | 0.15 | 0.30 | 0.10 | Impacto físico y ciudadano prioritario |
| Sector financiero (DORA) | 0.30 | 0.15 | 0.20 | 0.25 | 0.10 | DORA: impacto financiero sistémico |
| Administración Pública (ENS) | 0.25 | 0.15 | 0.20 | 0.25 | 0.15 | Equilibrio entre dimensiones ENS |
| Salud / Hospitales | 0.35 | 0.10 | 0.20 | 0.30 | 0.05 | Vidas humanas + datos GDPR Art.9 |
| PYME tecnológica | 0.20 | 0.20 | 0.25 | 0.20 | 0.15 | Alta explotabilidad, menor escala A |
| Defecto (genérico) | 0.25 | 0.15 | 0.20 | 0.25 | 0.15 | Equilibrio metodológico |

**Fórmula de interpretación del nivel de madurez:**
```excel
=IFS(
  IGM_DREAD < 2.0, "🔴 INEXISTENTE — Acción urgente requerida",
  IGM_DREAD < 3.0, "🟠 INICIAL — Formalización prioritaria",
  IGM_DREAD < 4.0, "🟡 EN DESARROLLO — Integración con frameworks",
  IGM_DREAD < 5.0, "🟢 GESTIONADO — Automatización y reporting",
  IGM_DREAD = 5.0, "⭐ OPTIMIZADO — Referencia del sector"
)
```

---

## HOJA 04_BENCHMARKING_SECTORIAL

**Propósito:** Comparar el IGM-DREAD de la organización con el promedio de su sector (datos de la encuesta agregada).

### Tabla de benchmarks sectoriales (a completar con datos de la encuesta)

| Sector | n | IGM_D | IGM_R | IGM_E | IGM_A | IGM_Disc | IGM_Global | Percentil 25 | Mediana | Percentil 75 |
|--------|---|-------|-------|-------|-------|---------|-----------|-------------|---------|-------------|
| Administración Pública | [dato encuesta] | | | | | | | | | |
| Sector financiero | [dato encuesta] | | | | | | | | | |
| Energía/Agua | [dato encuesta] | | | | | | | | | |
| Salud | [dato encuesta] | | | | | | | | | |
| Gran empresa | [dato encuesta] | | | | | | | | | |
| PYME | [dato encuesta] | | | | | | | | | |

**Fórmula de posición relativa de la organización en su sector:**
```excel
=PERCENTRANK(rango_IGM_sector, IGM_organizacion, 2)
```

**Indicador semáforo de posición relativa:**
```excel
=IF(PERCENTRANK(...)>=0.75, "🟢 TOP CUARTIL", 
  IF(PERCENTRANK(...)>=0.5, "🟡 SOBRE MEDIANA",
    IF(PERCENTRANK(...)>=0.25, "🟠 BAJO MEDIANA", "🔴 CUARTIL INFERIOR")))
```

---

## HOJA 05_ROI_CIBERSEGURIDAD

**Propósito:** Calcular el retorno sobre la inversión (ROI) de las iniciativas de ciberseguridad vinculadas a la mejora del IGM-DREAD.

### Modelo de cálculo de ROI

#### Sección A — Costes actuales del ciberriesgo (ALE - Annualized Loss Expectancy)

```
ALE = ARO × SLE

Donde:
- ARO (Annual Rate of Occurrence) = frecuencia anual esperada de incidentes significativos
- SLE (Single Loss Expectancy) = pérdida esperada por incidente
```

| Parámetro | Celda | Fórmula / Entrada | Fuente de referencia |
|-----------|-------|------------------|---------------------|
| Nº incidentes significativos (últimos 2 años) | B5 | Entrada manual | Dato interno / P2.3 |
| ARO estimado | B6 | =B5/2 | Media anual |
| Coste medio por incidente (€) | B7 | Entrada manual | Coste real o benchmark INCIBE 2025 |
| SLE estimado | B8 | =B7 | Para un único tipo de incidente |
| **ALE actual** | **B9** | **=B6*B8** | |
| Coste de sanciones regulatorias esperado (anual) | B10 | Entrada manual | Estimación legal / benchmark GDPR |
| Coste reputacional estimado (€/año) | B11 | Entrada manual | Ver nota metodológica |
| **Coste total del riesgo (CTR)** | **B12** | **=B9+B10+B11** | |

**Nota metodológica sobre coste reputacional:**
Para organizaciones B2C o de servicios al ciudadano, puede estimarse como:
```
Coste_reputacional = N_clientes × Tasa_churn_incidente × LTV_cliente
```

#### Sección B — Inversión en mejora (CAPEX + OPEX)

| Iniciativa | Inversión CAPEX (€) | OPEX anual (€) | Mejora IGM esperada (Δ) | Dimensión DREAD impactada |
|-----------|---------------------|----------------|------------------------|--------------------------|
| Herramienta SIEM/SOAR | [entrada] | [entrada] | [entrada] | D, R, E, A, Disc |
| Formación y concienciación | [entrada] | [entrada] | [entrada] | E (reducción) |
| Programa de gestión de vulnerabilidades | [entrada] | [entrada] | [entrada] | R, E |
| Red team / pentest anual | [entrada] | [entrada] | [entrada] | Disc, E |
| Threat Intelligence feeds | [entrada] | [entrada] | [entrada] | R, E, Disc |
| Automatización de scoring (ML) | [entrada] | [entrada] | [entrada] | Todos |
| BCP/DRP refuerzo | [entrada] | [entrada] | [entrada] | D, A |
| **TOTAL inversión** | **=SUM(...)** | **=SUM(...)** | | |

#### Sección C — ALE post-inversión y cálculo del ROI

```excel
ALE_reducida = ALE_actual × (1 - Factor_reduccion_riesgo)
```

**Factor de reducción de riesgo por nivel de mejora del IGM:**
```excel
=IF(Delta_IGM >= 1.5, 0.60,
  IF(Delta_IGM >= 1.0, 0.45,
    IF(Delta_IGM >= 0.5, 0.30,
      IF(Delta_IGM >= 0.25, 0.15, 0.05))))
```
*(Basado en benchmarks de reducción de riesgo por mejora de madurez — adaptados de FAIR Institute 2024)*

**Fórmulas de ROI:**
```excel
Beneficio_anual = ALE_actual - ALE_reducida
ROI_anual (%) = (Beneficio_anual - OPEX_total) / (CAPEX_total + OPEX_total) × 100
Payback_period (años) = CAPEX_total / (Beneficio_anual - OPEX_total)
NPV_3_años = NPV(tasa_descuento, flujos_anuales_3_años) - CAPEX_total
```

Fórmula Excel para NPV:
```excel
=NPV(B_tasa_descuento, Beneficio_anual_Y1, Beneficio_anual_Y2, Beneficio_anual_Y3) - CAPEX_total
```

#### Sección D — Presentación del ROI para el Consejo de Administración

**Tabla resumen ejecutivo automática:**

| Métrica | Antes | Después | Variación |
|---------|-------|---------|-----------|
| IGM-DREAD global | =ref_IGM_actual | =ref_IGM_target | =DELTA con flecha ↑↓ |
| ALE (€/año) | =ALE_actual | =ALE_reducida | =-ALE_reduccion |
| ROI de la inversión | — | =ROI_anual% | |
| Payback (años) | — | =Payback | |
| NPV 3 años (€) | — | =NPV_3_años | |
| Reducción de riesgo | — | =Factor_reduccion% | |

---

## HOJA 06_SCORING_DREAD_AMENAZAS

**Propósito:** Hoja de trabajo para el scoring DREAD de amenazas específicas identificadas en la organización.

### Plantilla de scoring por amenaza

| Col | Campo | Tipo | Descripción |
|-----|-------|------|-------------|
| A | ID_Amenaza | Texto | Ej: AME-001 |
| B | Nombre_Amenaza | Texto | Ej: Ransomware via phishing |
| C | STRIDE_Categoria | Lista | Spoofing / Tampering / Repudiation / Info Disclosure / DoS / EoP |
| D | CVE_asociado | Texto | Opcional; formato CVE-AAAA-NNNNN |
| E | EPSS_score | Número 0–1 | Consultar FIRST API; actualizar semanalmente |
| F | D_score | Número 1–10 | Daño potencial (criterios según rúbrica) |
| G | R_score | Número 1–10 | Reproducibilidad (o = 10×EPSS si CVE disponible) |
| H | E_score | Número 1–10 | Explotabilidad (o = inverso_CVSS_AC) |
| I | A_score | Número 1–10 | Usuarios Afectados (% usuarios × 10) |
| J | Disc_score | Número 1–10 | Descubribilidad (o fijar = 10) |
| K | DREAD_media | Fórmula | =AVERAGE(F:J) |
| L | DREAD_ponderado | Fórmula | =SUMPRODUCT(F:J, pesos_desde_H03) |
| M | Nivel_riesgo | Fórmula IFS | Crítico / Alto / Medio / Bajo |
| N | Prioridad | Fórmula RANK | =RANK(L2, $L$2:$L$100, 0) |
| O | Propietario | Texto | Responsable de la amenaza |
| P | Fecha_evaluacion | Fecha | |
| Q | Estado_mitigacion | Lista | Pendiente / En curso / Mitigado / Aceptado |
| R | Fecha_revision | Fecha | =P2+revisión_días (ej: +30 para crítico, +90 para medio) |

**Fórmula automática de prioridad de revisión:**
```excel
=IF(M2="Crítico", TODAY()+7, IF(M2="Alto", TODAY()+30, IF(M2="Medio", TODAY()+90, TODAY()+180)))
```

**Formato condicional para columna M (Nivel de riesgo):**
- "Crítico" → Fondo rojo, texto blanco, negrita
- "Alto" → Fondo naranja, texto negro
- "Medio" → Fondo amarillo, texto negro
- "Bajo" → Fondo verde claro, texto negro

---

## HOJA 07_DASHBOARD_EJECUTIVO

**Propósito:** Visualización consolidada para presentación al Consejo de Administración / CISO.

### Elementos del dashboard (disposición sugerida 3×2 panels)

**Panel 1 — IGM-DREAD Global (celda grande, gauge chart)**
```excel
Valor: =Hoja03!IGM_Global
Semáforo: formato condicional según IFS de madurez
```

**Panel 2 — Gráfico de radar por dimensión DREAD**
- Spider chart con los 5 scores de dimensión
- Línea de referencia en 3.0 (nivel "Definido")
- Eje secundario con nombre de dimensión

**Panel 3 — Top 5 Amenazas (tabla dinámica)**
- Fuente: Hoja 06
- Ordenadas por DREAD_ponderado DESC
- Columnas: Nombre, Nivel, Score, Estado_mitigación, Propietario

**Panel 4 — Comparativa sectorial (gráfico de barras)**
- IGM organización vs. media sector vs. top cuartil sector
- Fuente: Hoja 04

**Panel 5 — ROI resumen (tabla KPIs)**
- ALE actual vs. ALE reducida
- ROI % de la inversión en ciberseguridad
- Payback period

**Panel 6 — Evolución temporal IGM (gráfico de línea)**
- Eje X: trimestres/semestres de evaluación pasados
- Eje Y: IGM-DREAD global y por dimensión
- Tendencia proyectada a 12 meses

### Controles interactivos del dashboard

- **Botón "Actualizar datos"**: macro VBA que recalcula todo el libro
- **Segmentador de sector**: filtra benchmarking sectorial por tipo de organización
- **Selector de preset de pesos**: menú desplegable que carga pesos sectoriales predefinidos (Hoja 03)
- **Botón "Exportar a PDF"**: genera PDF del dashboard para distribución

---

## HOJA 08_INSTRUCCIONES

**Propósito:** Guía de uso paso a paso para el usuario no técnico del libro de Excel.

### Pasos de uso

1. **Abrir el libro** y habilitar macros si aparece el aviso de seguridad de Excel.
2. **Completar la Hoja 00_PORTADA** con los datos de la organización.
3. **Introducir las respuestas de la encuesta** en la Hoja 01_DATOS_ENCUESTA (una fila por organización encuestada; si es autoevaluación de una sola organización, usar la fila 2).
4. **Revisar la Hoja 02** para verificar que los scores por dimensión se han calculado correctamente.
5. **En la Hoja 03**, seleccionar el preset de pesos adecuado para el sector o ajustar manualmente los pesos.
6. **En la Hoja 05**, introducir los datos de costes e inversiones para calcular el ROI.
7. **En la Hoja 06**, registrar las amenazas identificadas en la organización para el scoring DREAD.
8. **Consultar la Hoja 07** para el dashboard ejecutivo listo para presentar.

### Código de colores de las celdas

| Color | Significado |
|-------|-------------|
| 🟡 Amarillo | Celda de entrada de datos (editable) |
| ⬜ Blanco | Celda calculada automáticamente (NO editar) |
| 🟢 Verde claro | Resultado positivo / objetivo alcanzado |
| 🟠 Naranja | Resultado de alerta / mejora recomendada |
| 🔴 Rojo | Resultado crítico / acción urgente |
| 🔵 Azul claro | Referencia cruzada a otra hoja |

---

*Kit de Encuesta DREAD · Plantilla Excel IGM & ROI v1.0 · Abril 2026*
*Implementada con Microsoft Excel 365 / LibreOffice Calc 7.5+*
*Compatible con Google Sheets con adaptaciones menores en las fórmulas de validación*
