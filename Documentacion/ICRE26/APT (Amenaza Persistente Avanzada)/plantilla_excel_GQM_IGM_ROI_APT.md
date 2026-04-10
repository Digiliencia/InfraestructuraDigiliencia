# Plantilla de Excel para cálculo del Índice Global de Madurez (IGM) y ROI de ciberseguridad  
*(basada exclusivamente en las métricas aprobadas por GQM + PRAGMATIC)*

## 1. Estructura del libro de trabajo

Se recomiendan **cuatro hojas**:

| Hoja | Propósito |
|------|-----------|
| **1_Respuestas** | Registro bruto de las respuestas de cada organización (una fila por entidad). |
| **2_Puntuaciones** | Conversión de respuestas a valores numéricos según la tabla de puntuación GQM. |
| **3_IGM_Cálculo** | Cálculo de sub‑índices por bloque y del IGM global. |
| **4_ROI_Escenarios** | Estimación del ROI bajo diferentes hipótesis de pérdida evitada. |

## 2. Hoja 1_Respuestas

| Columna | Descripción | Ejemplo |
|---------|-------------|---------|
| A | `ID_Org` (código alfanumérico único) | `ESP001` |
| B | `Sector` (energía, sanidad, TIC, etc.) | `TIC` |
| C | `Tamaño` (rango de empleados) | `250‑999` |
| D | `Ámbito` (local/nacional/UE/global) | `Nacional` |
| E | `Fecha_resp` (dd/mm/aaaa) | `02/04/2026` |
| F‑AO | `Preg_1` … `Preg_42` (texto de la respuesta tal como se selecciona en la encuesta) | `Sí, aprobada por el máximo órgano de gobierno` |
*(Las columnas F‑AO pueden ser listas desplegables con las opciones exactas de cada pregunta para asegurar consistencia.)*

## 3. Hoja 2_Puntuaciones

Se copian las columnas A‑E de **1_Respuestas** y se añaden columnas de puntuación para cada pregunta que contribuye al IGM o al ROI.

### 3.1. Reglas de conversión (ejemplos)

| Pregunta | Tipo de respuesta | Puntuación numérica |
|----------|------------------|---------------------|
| **P6** (estrategia formal) | Selección simple | Máximo órgano de gobierno = 3 <br> Dirección intermedia = 2 <br> En elaboración = 1 <br> Prácticas dispersas / No existe = 0 |
| **P7** (alineamiento con marcos) | Selección múltiple | Cada marco marcado suma 1 (máx. 6) → luego se normaliza a 0‑3 dividiendo por 2 y redondeando hacia abajo. |
| **P8** (cumplimiento NIS2) | Selección simple | Completamente alineados = 3 <br> Parcialmente alineados = 2 <br> Fase inicial = 1 <br> No aplica / No evaluado = 0 |
| **P9** (revisión periódica) | Selección simple | Anual con reporte al máximo órgano = 3 <br> Cada 2‑3 años = 2 <br> Solo tras incidente = 1 <br> Sin periodicidad = 0 |
| **P10** (participación Consejo) | Selección simple | Recurrente ≥4 veces/año = 3 <br> 1‑3 veces/año = 2 <br> Solo tras incidente grave = 1 <br> No se informa = 0 |
| **P11** (mapa de riesgos con APT) | Selección simple | Sí, con escenarios = 3 <br> Sí, pero diluido = 2 <br> En elaboración = 1 <br> No = 0 |
| **P12** (frecuencia actualización riesgo) | Selección simple | Anual = 3 <br> Cada 2‑3 años = 2 <br> Tras cambios significativos = 1 <br> No sistemática = 0 |
| **P13.1‑P13.6**, **P22.1‑P22.5**, **P27.1‑P27.3** | Escala 0‑3 (directa) | Valor tal cual (0‑3) |
| **P14** (cuantificación económica) | Selección simple | Metodología formal (FAIR, etc.) = 3 <br> Estimaciones numéricas aproximadas = 2 <br> Solo escalas cualitativas = 1 <br> No se realiza = 0 |
| **P15** (integración continuidad) | Selección simple | Totalmente integrado = 3 <br> Parcialmente integrado = 2 <br> Mencionado sin desarrollo = 1 <br> No integrado = 0 |
| **P16‑P20**, **P21**, **P23‑P24**, **P25‑P26**, **P28‑P32**, **P33‑P36**, **P37‑P39**, **P40‑P41** | Según su tipo (selección simple/múltiple, escala, etc.) – aplicar reglas análogas a las anteriores. |
| **P42** (comentario abierto) | No se puntúa (se deja como texto libre). | — |

> **Implementación**: usar fórmulas `=SI()` o `=BUSCARV()` para convertir texto en número. Por ejemplo, para P6:  
> `=SI(ESNUMERO(ENCONTRAR("máximo órgano de gobierno",F2));3;SI(ESNUMERO(ENCONTRAR("dirección intermedia",F2));2;SI(ESNUMERO(ENCONTRAR("en elaboración",F2));1;0)))`

### 3.2. Columnas de puntuación sugeridas

| Columna | Pregunta(s) | Comentario |
|---------|-------------|------------|
| AP | P6_Punt | puntuación 0‑3 |
| AQ | P7_Punt | puntuación 0‑3 (normalizada) |
| AR | P8_Punt | 0‑3 |
| AS | P9_Punt | 0‑3 |
| AT | P10_Punt | 0‑3 |
| AU | P11_Punt | 0‑3 |
| AV | P12_Punt | 0‑3 |
| AW‑BA | P13.1‑P13.6_Punt | 0‑3 cada una |
| BB‑BF | P22.1‑P22.5_Punt | 0‑3 cada una |
| BG‑BI | P27.1‑P27.3_Punt | 0‑3 cada una |
| BJ | P14_Punt | 0‑3 |
| BK | P15_Punt | 0‑3 |
| BL‑… | (otros ítems que alimentan el IGM) | según regla |
| BN | P33_Punt (inversión % TI) | convertir categoría a 0‑3 (p.ej. <5 %=0, 5‑9 %=1, 10‑14 %=2, ≥15 %=3) |
| BO | P34_Punt (existe modelo ROI) | Sí=2, En análisis=1, No=0 |
| BP | P35_Punt (usa IGM formal) | Sí=2, En valoración=1, No=0 |
| BQ | P36_Punt (inversión tras incidentes) | Aumentó claramente=2, Aumentó tras sector=1, Estable=0, Reducida=‑1 (ajustar escala) |
| … | (continuar según necesiten) | |

> **Nota**: Las columnas que no contribuyen al IGM (por ejemplo, datos de perfil) pueden dejarse sin puntuación o asignarles un peso 0 en el cálculo posterior.

## 4. Hoja 3_IGM_Cálculo

### 4.1. Definición de bloques y preguntas que los forman  
*(Los números de columna corresponden a las de la hoja **2_Puntuaciones**; ajuste si su hoja tiene distinto orden.)*

| Bloque | Preguntas (columnas) | Descripción breve |
|--------|----------------------|-------------------|
| **B1_Gobernanza** | AP (P6), AQ (P7), AR (P8), AS (P9), AT (P10) | Estrategia, alineamiento, cumplimiento, revisión, participación del Consejo. |
| **B2_Riesgo** | AU (P11), AV (P12), AW‑BA (P13.1‑P13.6), BB (P14), BK (P15) | Mapa de riesgos, frecuencia actualización, métricas MTTD/MTTR/MTTP/%phishing/TTPs, cuantificación económica, integración continuidad. |
| **B3_Vectores_Entrada** | P16‑P20 (columnas correspondientes según su hoja) – se pueden resumir en una columna *Punt_Vectores* = promedio de sus puntuaciones. |
| **B4_Detección** | BG‑BI (P27.1‑P27.3) + BB‑BF (P22.1‑P22.5) – promedio ponderado (peso 0.6 para TTPs, 0.4 para métricas de respuesta). |
| **B5_Respuesta** | (Ya incluida en B4 como parte de la detección; si se prefiere separar, usar P25‑P28). |
| **B6_Cultura** | P29‑P32 (columnas de su hoja). |
| **B7_Inversión** | BN (P33), BO (P34), BP (P35), BQ (P36). |
| **B8_Colaboración** | P37‑P39. |
| **B9_Futuro** | P40‑P41. |

### 4.2. Cálculo de sub‑índices bloque

Para cada bloque *b*:
