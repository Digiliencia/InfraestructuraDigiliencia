# 📊 PLANTILLA GQM+PRAGMATIC — CALCULADORA IGM Y ROI
## Especificación Técnica para Implementación en Excel/Google Sheets
### Kit GQM + PRAGMATIC · LINDDUN/LIINE4DU · España 2025–2026 · Versión 1.0

---

> *"Un índice de madurez sin fórmula es una opinión. Un ROI de privacidad sin datos es un deseo. Esta plantilla convierte ambas cosas en instrumentos de gestión con los que se puede —por fin— discutir de privacidad en una reunión de presupuestos sin que nadie cambie de tema."*

---

## ESTRUCTURA DEL LIBRO DE CÁLCULO — 10 HOJAS

| Hoja | Nombre | Función principal |
|------|--------|--------------------|
| 1 | `CONFIG_GQM` | Configuración: organización, sector, objetivos GQM activos |
| 2 | `METRICAS_GQM` | Catálogo completo de métricas GQM con resultados medidos |
| 3 | `PRAGMATIC_EVAL` | Evaluación PRAGMATIC de cada métrica activa |
| 4 | `IGM_CALCULO` | Cálculo del Índice de Madurez Global ponderado |
| 5 | `RADAR_GQM` | Visualización radar de madurez por indicador LINDDUN |
| 6 | `ROI_PRIVACIDAD` | Calculadora ROI: coste de no cumplimiento vs. inversión |
| 7 | `PLAN_MEJORA_GQM` | Plan de acción priorizado por riesgo PRAGMATIC |
| 8 | `BENCHMARKING` | Comparación sectorial y posicionamiento relativo |
| 9 | `TRAZABILIDAD` | Trazabilidad GQM: objetivo → pregunta → métrica → norma |
| 10 | `AUDITORIA` | Registro de evidencias y notas del facilitador |

---

## HOJA 1: CONFIG_GQM — Configuración del Diagnóstico

### Estructura de celdas:

```
A1: [LOGO — celda para imagen]
B1: "DIAGNÓSTICO GQM+PRAGMATIC — LINDDUN/LIINE4DU 2025–2026"

A3: "Organización:"           B3: [campo libre]
A4: "Sector:"                 B4: [desplegable — ver lista sectores P0.1]
A5: "Tamaño (empleados):"     B5: [desplegable: <50 / 50–249 / 250–999 / ≥1000]
A6: "Ámbito territorial:"     B6: [desplegable: Local / Regional / Nacional / Internacional]
A7: "Fecha diagnóstico:"      B7: [fecha DD/MM/AAAA]
A8: "DPO responsable:"        B8: [campo libre]
A9: "CISO responsable:"       B9: [campo libre]
A10: "Versión metodología:"   B10: "GQM+PRAGMATIC v1.0 / LINDDUN v2.0 / LIINE4DU 1.0" [fijo]

A12: "UMBRALES POR SECTOR:"
A13: "IGM mínimo recomendado:"
B13: [fórmula: =SI(B4="Sanidad";75%;SI(B4="Financiero";70%;SI(B4="Adm. Pública";70%;60%)))]

A15: "MÉTRICAS ACTIVAS EN ESTE DIAGNÓSTICO:"
[Tabla de selección: para cada una de las 21 métricas del catálogo, columna de casilla Sí/No]
```

### Lista de sectores disponibles para el desplegable:
1. Sanidad y ciencias de la vida
2. Servicios financieros y seguros
3. Administración Pública y Defensa
4. Educación e investigación
5. Telecomunicaciones y medios
6. Energía e infraestructuras críticas
7. Comercio electrónico y retail
8. Industria y manufactura
9. Transporte y logística
10. Tecnología e IA

---

## HOJA 2: METRICAS_GQM — Catálogo y Resultados de Medición

### Estructura de columnas:

```
Col A: Código métrica (L-M1, L-M2, ... EX-M3)
Col B: Indicador LINDDUN (L / I / NR / D / DD / U / NC / IN / EX)
Col C: Descripción resumida de la métrica
Col D: Fórmula de cálculo (texto descriptivo de la fórmula)
Col E: Unidad de medida (%, ratio, escala 0–10, días, horas, número entero)
Col F: Umbral mínimo/máximo (valor objetivo)
Col G: Valor medido (entrada manual o fórmula si está automatizado)
Col H: Estado del umbral (fórmula automática: SUPERADO / INCUMPLIDO / NO MEDIDO)
Col I: Semáforo (formato condicional: 🟢 si superado / 🔴 si incumplido / ⚪ si no medido)
Col J: Tendencia respecto diagnóstico anterior (↑ mejora / → estable / ↓ empeora)
Col K: Fecha de medición
Col L: Fuente de datos (sistema del que proviene el dato)
Col M: Responsable de medición
Col N: Observaciones del medidor
```

### Tabla pre-cargada de métricas (valores umbral):

| Col A | Col C | Col E | Col F (Umbral) |
|-------|-------|-------|----------------|
| L-M1 | % tratamientos con DFD actualizado | % | ≥ 80% |
| L-M2 | % quasi-identificadores no controlados | % | ≤ 10% |
| L-M3 | ICAV (Índice Controles Anti-Vinculación) | Escala 0–10 | ≥ 7.0 |
| L-M4 | TTDL (horas detección vinculación no autorizada) | Horas | ≤ 72h |
| L-M5 | % modelos ML con EIPD de linking | % | ≥ 100% |
| I-M1 | K-anonimato mínimo de datasets publicados | Entero k | ≥ 5 |
| I-M3 | FAR biométrica (False Acceptance Rate) | % | ≤ 0.01% |
| I-M5 | Epsilon (ε) de privacidad diferencial | Número real | ≤ 8 |
| NR-M1 | Completitud de logs de acceso a datos personales | % | ≥ 99.5% |
| NR-M4 | TMRS (días respuesta a solicitud de supresión) | Días | ≤ 30 días |
| D-M1 | IPV videovigilancia (0–10) | Escala 0–10 | ≥ 8.0 |
| D-M5 | % empleados informados de monitorización | % | ≥ 100% |
| DD-M1 | % encargados con DPA vigente y auditado | % | ≥ 100% |
| DD-M3 | % prompts IA con datos personales detectados | % | ≤ 2% |
| DD-M5 | IMD (Índice Minimización de Datos) | % | ≥ 95% |
| U-M1 | ILPP (Legibilidad política privacidad — Flesch) | Puntos 0–100 | ≥ 60 |
| U-M2 | % derechos ARCO+ atendidos en ≤ 30 días | % | ≥ 100% |
| U-M3 | % consentimientos válidos (4 requisitos Art.7) | % | ≥ 100% |
| NC-M3 | % brechas notificadas a AEPD en ≤ 72h | % | ≥ 100% |
| NC-M5 | IPAA (Índice Preparación AI Act) | Escala 0–10 | ≥ 6.0 |
| IN-M3 | DIR (Disparate Impact Ratio) | Ratio 0–1 | ≥ 0.80 |

### Fórmula de estado de umbral (Col H):

```excel
// Para métricas donde "mayor es mejor" (ej. L-M1 ≥ 80%)
=SI(G2="";"⚪ NO MEDIDO";SI(G2>=F2;"🟢 SUPERADO";"🔴 INCUMPLIDO"))

// Para métricas donde "menor es mejor" (ej. L-M4 ≤ 72h)
=SI(G2="";"⚪ NO MEDIDO";SI(G2<=F2;"🟢 SUPERADO";"🔴 INCUMPLIDO"))
```

---

## HOJA 3: PRAGMATIC_EVAL — Evaluación de Calidad de Métricas

### Estructura de la tabla de evaluación PRAGMATIC:

```
Col A: Código métrica
Col B: P — Predictivo (0–10) [campo editable]
Col C: R — Relevante (0–10) [campo editable]
Col D: A — Accionable (0–10) [campo editable]
Col E: G — Genuino (0–10) [campo editable]
Col F: M — Meaningful/Significativo (0–10) [campo editable]
Col G: A2 — Accurate/Preciso (0–10) [campo editable]
Col H: T — Timely/Oportuno (0–10) [campo editable]
Col I: I — Independiente (0–10) [campo editable]
Col J: C — Cheap/Rentable (0–10) [campo editable]
Col K: Total PRAGMATIC (=PROMEDIO(B:J)) [fórmula automática]
Col L: Calificación (=SI(K>=8;"⭐⭐⭐ Excelente";SI(K>=6.5;"⭐⭐ Buena";SI(K>=5;"⭐ Aceptable";"❌ Revisar"))))
Col M: Criterio más débil (=COINCIDIR(MIN(B:J);B:J;0) → nombre del criterio)
Col N: Acción de mejora recomendada (campo libre)
```

### Pre-cargado con evaluaciones del catálogo:

Los valores de B a J para cada métrica se pre-cargan con las puntuaciones del catálogo PRAGMATIC (ver archivo `matriz-PRAGMATIC-LINDDUN.md`). El evaluador puede ajustar las puntuaciones según el contexto específico de su organización.

### Panel de análisis PRAGMATIC:

```
Métrica con mayor puntuación PRAGMATIC:  [NC-M3: 9.00] ← fórmula automática
Métrica con menor puntuación PRAGMATIC:  [=métrica con PRAGMATIC_total mínimo]
Criterio más débil en todo el catálogo:  [C — Rentable: media X.XX] ← PROMEDIO por columna
Métricas con puntuación < 6.5 (revisar): [N] ← CONTAR.SI(K:K;"<6.5")
Métricas excelentes (≥ 8.0):             [N] ← CONTAR.SI(K:K;">=8")
```

---

## HOJA 4: IGM_CALCULO — Índice de Madurez Global

### Metodología de cálculo del IGM GQM

El IGM GQM es una evolución del IGM estándar que incorpora la calidad PRAGMATIC de cada métrica como factor de ponderación adicional:

**Fórmula IGM estándar** (sin ajuste PRAGMATIC):

\[
IGM = \sum_{j=1}^{9} w_j \cdot M_j
\]

**Fórmula IGM ajustada por PRAGMATIC** (versión avanzada):

\[
IGM_{PRAGMATIC} = \frac{\sum_{j=1}^{9} w_j \cdot M_j \cdot Q_j}{\sum_{j=1}^{9} w_j \cdot Q_j}
\]

Donde:
- \(w_j\) = Peso del módulo j (ver tabla de pesos)
- \(M_j\) = Madurez media del módulo j (media de puntuaciones de métricas activas, escala 0–1)
- \(Q_j\) = Puntuación PRAGMATIC media de las métricas del módulo j (escala 0–10)

La fórmula IGM ajustada da más peso a los módulos cuyas métricas tienen mayor calidad (según PRAGMATIC), penalizando módulos cuyas métricas son de calidad dudosa.

### Tabla de pesos por módulo/indicador:

```
Indicador L  — Linking:            Peso = 10%   Justificación: Riesgo fundacional de perfilado
Indicador I  — Identifying:        Peso = 12%   Justificación: Obligaciones biometría + anonimización
Indicador NR — Non-repudiation:    Peso = 8%    Justificación: Trazabilidad y gestión de derechos
Indicador D  — Detecting:          Peso = 8%    Justificación: Videovigilancia + monitorización laboral
Indicador DD — Data Disclosure:    Peso = 15%   Justificación: Encargados + transferencias + IA gen.
Indicador U  — Unawareness:        Peso = 12%   Justificación: Transparencia + consentimiento + ARCO
Indicador NC — Non-compliance:     Peso = 15%   Justificación: Brechas + EIPDs + AI Act
Indicador IN — Inaccuracy:         Peso = 10%   Justificación: Exactitud + sesgo algorítmico
Indicador EX — Exclusion:          Peso = 5%    Justificación: Accesibilidad (emergente)
Gobernanza (transversal):          Peso = 5%    Justificación: Madurez organizacional general
                                   ──────────
                                   TOTAL = 100%
```

### Normalización de métricas (0–1 para el cálculo IGM):

Las métricas tienen unidades heterogéneas. Se normalizan mediante la siguiente función:

```excel
// Para métricas "mayor es mejor" (ej. L-M1: umbral ≥ 80%)
M_normalizada = MIN(Valor_medido / Umbral_mínimo; 1)

// Para métricas "menor es mejor" (ej. L-M4: umbral ≤ 72h)
M_normalizada = MIN(Umbral_máximo / Valor_medido; 1)
// Si el valor medido es 0, M_normalizada = 1

// Para métricas con escala propia (ej. I-M5: ε ≤ 8)
M_normalizada = MIN(Umbral / Valor; 1)

// Para métricas de ratio (ej. IN-M3: DIR ≥ 0.80)
M_normalizada = MIN(Valor / Umbral; 1)
```

### Panel de resultados IGM:

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ÍNDICE DE MADUREZ GLOBAL — GQM + PRAGMATIC                             │
│  ═══════════════════════════════════════════════════════════════         │
│  IGM ESTÁNDAR:       [██████████░░░░] 68.4%    Nivel: MEDIO 🟡           │
│  IGM PRAGMATIC ADJ.: [████████░░░░░░] 71.2%    Nivel: MEDIO-ALTO 🟡     │
│  Diferencia PRAGMATIC: +2.8%  (sus métricas de mejor calidad tiran ↑)   │
│                                                                          │
│  Umbral mínimo sector: [60%] ✅ Superado                                 │
│  Gap hasta ALTO (75%): -3.8 puntos                                       │
│  Gap hasta EXCELENTE (90%): -18.8 puntos                                 │
│                                                                          │
│  Métricas INCUMPLIDAS (🔴): [N] de [M activas]                           │
│  Métricas NO MEDIDAS (⚪):  [N] de [M activas]                           │
└─────────────────────────────────────────────────────────────────────────┘
```

### Tabla detallada por indicador:

```
Col A: Indicador LINDDUN
Col B: N.º métricas activas en el indicador
Col C: N.º métricas con valor medido
Col D: N.º métricas incumplidas (🔴)
Col E: Madurez media normalizada (0–1)
Col F: Peso del indicador (%)
Col G: Contribución ponderada al IGM (=E*F)
Col H: Calidad PRAGMATIC media del indicador
Col I: IGM ajustado PRAGMATIC del indicador
Col J: Semáforo de madurez por indicador
```

---

## HOJA 5: RADAR_GQM — Visualización de Madurez

### Gráfico Radar de Doble Serie:

**Datos de entrada** (tabla 9 filas × 4 columnas):

```
Col A: Indicador LINDDUN (L, I, NR, D, DD, U, NC, IN, EX)
Col B: Madurez actual normalizada (0–1) → multiplicar por 5 para escala 0–5
Col C: Umbral mínimo recomendado (sector-específico, escala 0–5)
Col D: Puntuación PRAGMATIC media (0–10) → dividir por 2 para escala 0–5
```

**Tres series en el radar**:
1. **Serie Azul** (relleno, transparencia 30%): Madurez actual
2. **Serie Roja** (línea discontinua, sin relleno): Umbral mínimo del sector
3. **Serie Gris** (línea punteada, sin relleno): Calidad PRAGMATIC de las métricas

**Instrucción de creación en Excel**:
1. Seleccionar rango A:D con encabezados
2. Insertar → Gráfico → Radial → Radial con marcadores
3. Añadir las tres series; configurar colores según especificación
4. Escala: 0 a 5 (marcas en 1, 2, 3, 4, 5)
5. Título: "Perfil GQM+PRAGMATIC — [Organización] — [Fecha]"

**Interpretación del triple radar**:
- Cuanto mayor la separación entre la serie azul y la roja: mayor brecha de madurez
- Cuanto mayor la serie gris respecto a la azul: el problema no es de medición sino de ejecución
- Cuanto menor la serie gris respecto a las otras: las métricas de ese indicador son de baja calidad PRAGMATIC y deben revisarse

---

## HOJA 6: ROI_PRIVACIDAD — Calculadora de Retorno

*(Misma estructura que la versión anterior del Kit, con las siguientes adiciones específicas GQM+PRAGMATIC)*

### Adición A: Coste de medición por métrica

```
Col A: Código métrica
Col B: Coste anual estimado de recogida y análisis de la métrica (€)
Col C: Puntuación PRAGMATIC C (Rentable) de la métrica
Col D: Valor informativo estimado (€ de decisiones mejoradas o sanciones evitadas por contar con esta métrica)
Col E: ROI específico de la métrica (=(D-B)/B*100)
Col F: ¿Incluir en el cuadro de mando? (SI si ROI >0 o C≥7; NO si ROI <0 y C<5)
```

### Fórmulas ROI de privacidad:

**ROI de la inversión en cumplimiento**:

\[
ROI_{privacidad} = \frac{CNC_{total} - IC_{total}}{IC_{total}} \times 100
\]

**ROI ajustado por PRAGMATIC** (coste de medición incluido):

\[
ROI_{GQM} = \frac{CNC_{total} - (IC_{total} + CM_{total})}{IC_{total} + CM_{total}} \times 100
\]

Donde:
- \(CNC_{total}\) = Coste Total de No Cumplimiento (sanciones esperadas + costes directos)
- \(IC_{total}\) = Inversión Total en Cumplimiento (DPO, herramientas, formación, etc.)
- \(CM_{total}\) = Coste Total de Medición (suma del coste de recogida de todas las métricas)

**En Excel**:

```excel
ROI_GQM = ((CNC_Total - (IC_Total + CM_Total)) / (IC_Total + CM_Total)) * 100

// Período de recuperación (meses)
Payback = (IC_Total + CM_Total) / (CNC_Total / 12)

// Beneficio neto proyectado 3 años
BN_3años = (CNC_Total * 3) - ((IC_Total + CM_Total) * 3)
```

### Panel ROI completo:

```
┌──────────────────────────────────────────────────────────────────┐
│  ANÁLISIS COSTE-BENEFICIO GQM+PRAGMATIC                          │
│  ════════════════════════════════════════════════════════         │
│  Coste de No Cumplimiento (CNC anual):        [€ XXX.XXX]        │
│  Inversión en Cumplimiento (IC anual):        [€ XX.XXX]         │
│  Coste de Medición GQM (CM anual):            [€ X.XXX]          │
│  ──────────────────────────────────────────────────────          │
│  ROI Privacidad Estándar:                     [XXX%]             │
│  ROI GQM Ajustado (incluye coste medición):   [XXX%]             │
│  Diferencia: La medición rigurosa "cuesta"    [€ X.XXX/año]      │
│  Pero aporta en precisión de decisiones:      [€ XX.XXX/año]     │
│  ──────────────────────────────────────────────────────          │
│  Período de recuperación:                     [X,X meses]        │
│  Beneficio neto proyectado (3 años):          [€ XXX.XXX]        │
└──────────────────────────────────────────────────────────────────┘
```

---

## HOJA 7: PLAN_MEJORA_GQM — Plan de Acción Priorizado

### Priorización basada en tres dimensiones GQM+PRAGMATIC:

El plan de mejora se genera para todas las métricas con estado 🔴 INCUMPLIDO, ordenadas por:

**Fórmula de Puntuación de Prioridad (PP)**:

\[
PP_i = w_R \cdot \text{Riesgo}_i + w_P \cdot PRAGMATIC_i + w_F \cdot \text{Facilidad}_i
\]

Donde:
- \(\text{Riesgo}_i\) = Nivel de riesgo regulatorio (Crítico=4, Alto=3, Medio=2, Bajo=1)
- \(PRAGMATIC_i\) = Puntuación PRAGMATIC total de la métrica (0–10, normalizada a 0–4)
- \(\text{Facilidad}_i\) = Facilidad de implementación (Muy fácil=4, Fácil=3, Moderada=2, Compleja=1)
- \(w_R = 0.50, w_P = 0.30, w_F = 0.20\) (pesos por defecto; ajustables en CONFIG_GQM)

### Estructura del plan de mejora:

```
Col A: Prioridad (calculada automáticamente por PP)
Col B: Código métrica
Col C: Indicador LINDDUN
Col D: Descripción del incumplimiento detectado
Col E: Nivel de riesgo regulatorio
Col F: Puntuación PRAGMATIC
Col G: Puntuación de Prioridad (PP) total
Col H: Acción de mejora específica [pre-cargado por métrica]
Col I: Normativa que obliga a esta acción [pre-cargado desde mapeo normativo]
Col J: Plazo recomendado [pre-cargado: Inmediato/3m/6m/12m]
Col K: Responsable sugerido [DPO/CISO/CTO/Legal/Negocio]
Col L: Coste estimado (€) [campo editable]
Col M: Mejora estimada en IGM si se implementa (+X puntos) [campo editable]
Col N: Estado [editable: Pendiente/En curso/Completada]
Col O: Fecha prevista de completación [editable]
Col P: Fecha real de completación [editable]
```

---

## HOJA 8: BENCHMARKING — Posicionamiento Sectorial

*(Estructura equivalente a la versión estándar del Kit, con datos sectoriales de referencia de ISMS Forum España 2025 e ENISA Threat Landscape 2025)*

---

## HOJA 9: TRAZABILIDAD — Cadena GQM Completa

### Visualización de la cadena de trazabilidad:

Esta hoja presenta la cadena completa GQM como árbol:

```
[OBJ-ES-1: Cumplir RGPD] ──────────────────────────────────────────────────────
    │
    ├── [OBJ-NC: Demostrar cumplimiento continuo] ─────────────────────────────
    │       │
    │       ├── Q-NC-1: ¿Dispone la organización de un sistema de gestión? ────
    │       │       └── NC-M1 (IMC) | Umbral ≥ 7 | PRAGMATIC: 7.56 | 🟢/🔴
    │       │
    │       ├── Q-NC-2: ¿Cómo responde la organización a brechas? ─────────────
    │       │       ├── NC-M3 (% brechas ≤72h) | Umbral ≥100% | PRAGMATIC: 9.00 | 🟢/🔴
    │       │       └── NC-M4 (TMNB) | Umbral ≤72h | PRAGMATIC: 8.44 | 🟢/🔴
    │       │
    │       └── Q-NC-3: ¿Está preparada la organización para el AI Act? ───────
    │               └── NC-M5 (IPAA) | Umbral ≥6 | PRAGMATIC: 8.00 | 🟢/🔴
    │
    └── [OBJ-U: Garantizar transparencia activa] ─────────────────────────────
            ├── Q-U-1: ¿Son comprensibles las políticas de privacidad? ────────
            │       └── U-M1 (ILPP) | Umbral ≥60 | PRAGMATIC: 7.78 | 🟢/🔴
            ├── Q-U-2: ¿Es válido el consentimiento recabado? ────────────────
            │       └── U-M3 (% consentimientos) | Umbral ≥100% | PRAGMATIC: 8.00 | 🟢/🔴
            └── Q-U-3: ¿Está formado el personal? ────────────────────────────
                    └── U-M5 (% formados) | Umbral ≥90% | PRAGMATIC: (ver catálogo)
```

---

## HOJA 10: AUDITORIA — Registro de Evidencias

*(Estructura equivalente a la versión estándar del Kit, con campo adicional para la fuente de datos de cada métrica GQM)*

---

## INSTRUCCIONES COMPLETAS DE IMPLEMENTACIÓN

### Paso 1 — Preparación (1–2 días):
1. Crear libro Excel con las 10 hojas nombradas exactamente como se indica
2. Configurar paleta de colores institucional en Diseño de libro
3. Pre-cargar los valores umbrales de la Hoja 2 (METRICAS_GQM) desde la tabla anterior
4. Pre-cargar los valores PRAGMATIC de la Hoja 3 desde `matriz-PRAGMATIC-LINDDUN.md`
5. Configurar las fórmulas de cálculo IGM en la Hoja 4

### Paso 2 — Recolección de datos (1–4 semanas):
1. Identificar la fuente de datos para cada métrica activa (Hoja 2, Col L)
2. Recopilar los valores de cada métrica de sus fuentes (SIEM, sistemas de gestión de derechos, DPO tools, etc.)
3. Introducir valores medidos en la Hoja 2 (Col G)
4. Ajustar puntuaciones PRAGMATIC si el contexto organizacional difiere del catálogo (Hoja 3)

### Paso 3 — Análisis y reporte (1–3 días):
1. Verificar el cálculo del IGM en la Hoja 4
2. Generar el radar en la Hoja 5
3. Calcular el ROI en la Hoja 6
4. Revisar el Plan de Mejora generado automáticamente en la Hoja 7
5. Comparar con benchmarking sectorial en la Hoja 8

### Fórmulas adicionales de referencia rápida:

```excel
// IGM Estándar
=SUMAPRODUCTO(E2:E10; F2:F10)

// IGM Ajustado PRAGMATIC
=SUMAPRODUCTO(E2:E10*H2:H10;F2:F10)/SUMAPRODUCTO(F2:F10;H2:H10)

// N.º métricas incumplidas
=CONTAR.SI(METRICAS_GQM!H2:H22;"🔴 INCUMPLIDO")

// N.º métricas no medidas
=CONTAR.SI(METRICAS_GQM!H2:H22;"⚪ NO MEDIDO")

// Puntuación de Prioridad del Plan de Mejora
=(PLAN_MEJORA_GQM!E2*0.5) + (PLAN_MEJORA_GQM!F2/10*4*0.3) + (PLAN_MEJORA_GQM!facilidad*0.2)

// ROI GQM Ajustado
=((ROI_PRIVACIDAD!CNC_Total-(ROI_PRIVACIDAD!IC_Total+ROI_PRIVACIDAD!CM_Total))/(ROI_PRIVACIDAD!IC_Total+ROI_PRIVACIDAD!CM_Total))*100
```

---

*Especificación técnica elaborada para implementación en Microsoft Excel 365 / Google Sheets. Compatibilidad: Excel 2019+, Google Sheets (adaptaciones menores en gráficos), LibreOffice Calc 7.x. Versión 1.0 — Abril 2026.*
