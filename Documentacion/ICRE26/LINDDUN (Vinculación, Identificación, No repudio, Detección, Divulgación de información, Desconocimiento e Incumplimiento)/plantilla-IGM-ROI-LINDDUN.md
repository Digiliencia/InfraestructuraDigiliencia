# 📊 PLANTILLA IGM Y ROI — DESCRIPCIÓN TÉCNICA PARA IMPLEMENTACIÓN EN EXCEL
## Kit de Encuesta LINDDUN/LIINE4DU 2025–2026
### Especificación funcional completa · Lista para implementar en Microsoft Excel o Google Sheets

---

> *"Lo que no se mide, no se gestiona. Lo que no se gestiona en privacidad, eventualmente lo gestiona la AEPD por usted —y con sus propias tarifas."*

---

## ESTRUCTURA GENERAL DEL LIBRO EXCEL

El libro de cálculo se organiza en **8 hojas (pestañas)**, diseñadas para ser utilizadas en secuencia pero también de forma independiente:

| Hoja | Nombre | Función |
|------|--------|---------|
| 1 | `CONFIG` | Configuración: nombre de organización, fecha, sector, responsable |
| 2 | `RESPUESTAS` | Entrada de datos: registro de respuestas por módulo e ítem |
| 3 | `IGM_CALCULO` | Cálculo automático del Índice de Madurez Global y por módulo |
| 4 | `RADAR_CHART` | Gráfico radar de madurez por indicador LINDDUN |
| 5 | `ROI_PRIVACIDAD` | Calculadora de ROI: coste de no cumplimiento vs. inversión |
| 6 | `BENCHMARKING` | Comparación con percentiles sectoriales (datos 2025) |
| 7 | `PLAN_MEJORA` | Generador automático de plan de acción priorizado |
| 8 | `NOTAS_AUDITORIA` | Registro de evidencias y notas del facilitador |

---

## HOJA 1: CONFIG — Configuración del Diagnóstico

### Campos requeridos:

```
A1: [LOGO] — Celda para imagen del logo (insertar imagen)
B1: "KIT DE DIAGNÓSTICO LINDDUN/LIINE4DU 2025–2026"

A3: "Organización:"         B3: [Campo libre — texto]
A4: "Sector:"               B4: [Lista desplegable — ver P0.1 encuesta]
A5: "Tamaño:"               B5: [Lista desplegable: <50 / 50-249 / 250-999 / 1000-4999 / 5000+]
A6: "Ámbito territorial:"   B6: [Lista desplegable — ver P0.3 encuesta]
A7: "Fecha diagnóstico:"    B7: [Formato fecha DD/MM/AAAA]
A8: "Facilitador:"          B8: [Campo libre]
A9: "DPO responsable:"      B9: [Campo libre]
A10: "Versión encuesta:"    B10: "v1.0 — Abril 2026" [fijo]

A12: "NIVEL MÍNIMO RECOMENDADO:" 
B12: [Fórmula: =SI(B4="Sanidad y ciencias de la vida";75%;SI(B4="Servicios financieros y seguros";70%;...;60%))]
```

**Colores corporativos sugeridos** (aplicar mediante formato condicional):
- Fondo encabezado: #1B3A6B (azul oscuro institucional)
- Texto encabezado: #FFFFFF (blanco)
- Filas alternas: #F5F7FA (gris muy claro)
- Indicadores de riesgo: #D32F2F (rojo), #F57F17 (naranja), #388E3C (verde)

---

## HOJA 2: RESPUESTAS — Entrada de Datos

### Estructura de la tabla de respuestas:

```
Col A: Código de pregunta (P1.1, P1.2, ... P10.4)
Col B: Módulo (M1–M10)
Col C: Indicador LINDDUN (L / I / NR / D / DD / U / NC / Inaccuracy / Exclusion / Transversal)
Col D: Texto resumido de la pregunta
Col E: Respuesta seleccionada (desplegable: A / B / C / D / E)
Col F: Puntuación automática (=SI(E2="A";1;SI(E2="B";2;SI(E2="C";3;SI(E2="D";4;SI(E2="E";5;0))))))
Col G: Nivel de riesgo (formato condicional: A/B = 🔴, C = 🟡, D/E = 🟢)
Col H: Evidencia documental (campo libre: nombre del documento que respalda la respuesta)
Col I: Fecha de la evidencia
Col J: Observaciones del facilitador
```

### Validación de datos (reglas de integridad):
- Col E: Solo acepta A, B, C, D o E (lista desplegable, no editable a mano)
- Col F: Calculada automáticamente, bloqueada para edición
- Col I: Solo acepta fechas válidas, alerta si fecha > 24 meses ("⚠️ Evidencia desactualizada")

### Tabla de módulos y pesos (oculta, referenciada por IGM_CALCULO):

```
M1 - Linking:           Peso = 10%;  N_items = 5
M2 - Identifying:       Peso = 12%;  N_items = 4
M3 - Non-repudiation:   Peso = 8%;   N_items = 4
M4 - Detecting:         Peso = 8%;   N_items = 4
M5 - Data Disclosure:   Peso = 15%;  N_items = 5
M6 - Unawareness:       Peso = 12%;  N_items = 5
M7 - Non-compliance:    Peso = 15%;  N_items = 5
M8 - Inaccuracy/Excl.:  Peso = 8%;   N_items = 3
M9 - Gobernanza:        Peso = 7%;   N_items = 3
M10 - Tecnología IA:    Peso = 5%;   N_items = 4
```

---

## HOJA 3: IGM_CALCULO — Índice de Madurez Global

### Panel de resultados principales:

```
┌─────────────────────────────────────────────────────────────────┐
│  ÍNDICE DE MADUREZ GLOBAL (IGM)                                 │
│  ══════════════════════════════════════════════════════         │
│  IGM TOTAL:  [██████░░░░] 63.2%   Nivel: MEDIO 🟡               │
│  Nivel mínimo recomendado (sector): 60%  ✅ Superado             │
│  Gap hasta nivel Alto (75%): -11.8 puntos                       │
└─────────────────────────────────────────────────────────────────┘
```

### Tabla de puntuaciones por módulo:

```
Col A: Módulo
Col B: Indicador LINDDUN
Col C: Puntuación media del módulo (1–5)
Col D: Porcentaje de madurez del módulo (=C/5*100%)
Col E: Peso del módulo
Col F: Contribución ponderada al IGM (=D*E)
Col G: Semáforo visual (formato condicional por rangos)
Col H: Número de ítems en nivel A/B ("⚠️ ítems de riesgo alto")
Col I: Variación respecto al diagnóstico anterior (si existe)
```

### Fórmula IGM implementada en Excel:

```excel
IGM = SUMAPRODUCTO(D2:D11; E2:E11)

Donde:
- D2:D11 = Vector de porcentajes de madurez por módulo
- E2:E11 = Vector de pesos por módulo
```

### Clasificación automática:

```excel
=SI(IGM<40%;"🔴 MUY BAJO - Riesgo regulatorio inmediato";
  SI(IGM<60%;"🟠 BAJO - Cumplimiento formal insuficiente";
    SI(IGM<75%;"🟡 MEDIO - Cumplimiento básico, mejoras necesarias";
      SI(IGM<90%;"🟢 ALTO - Buenas prácticas implementadas";
        "💚 MUY ALTO - Excelencia en privacidad"))))
```

---

## HOJA 4: RADAR_CHART — Visualización de Madurez

### Instrucciones para el gráfico radar:

**Datos de entrada** (tabla de 10 filas × 3 columnas):
```
Col A: Nombre del módulo (M1–M10)
Col B: Puntuación actual (0–5)
Col C: Nivel mínimo recomendado para el sector (0–5) [línea de referencia]
```

**Configuración del gráfico en Excel**:
1. Seleccionar rango A:C con encabezados
2. Insertar > Gráfico > Radial (o "Spider chart") → Seleccionar tipo "Radial relleno"
3. Serie 1 (puntuación actual): color #1B3A6B con transparencia 40%
4. Serie 2 (nivel mínimo): línea discontinua roja #D32F2F, sin relleno
5. Título: "Perfil de Madurez LINDDUN — [Nombre organización] — [Fecha]"
6. Escala: 0 a 5, con marcas en 1, 2, 3, 4, 5

**Interpretación visual**:
- Área **azul grande y equilibrada**: organización con madurez alta y homogénea
- Área **azul pequeña o desequilibrada**: áreas críticas identificadas como prioridad de mejora
- Puntos **por debajo de la línea roja**: módulos bajo el umbral mínimo recomendado

---

## HOJA 5: ROI_PRIVACIDAD — Calculadora de Retorno de la Inversión

### Sección A: Coste de No Cumplimiento (CNC)

**Estimación de sanciones potenciales** (basada en infracciones detectadas en la encuesta):

```
Col A: Tipo de infracción potencial (basado en ítems con respuesta A/B)
Col B: Artículo RGPD/AI Act infringido
Col C: Sanción máxima legal (€)
Col D: Factor de probabilidad (estimación: Baja=10% / Media=30% / Alta=60% / Muy Alta=80%)
Col E: Factor de gravedad organizacional (pequeña=0.5 / mediana=1.0 / grande=2.0 / gran empresa=4.0)
Col F: Sanción esperada ajustada (=C*D*E)

Total CNC = SUMA(F:F)
```

**Costes directos adicionales** (campos editables):

```
- Coste estimado de respuesta a brecha (notificación, gestión, comunicación): [€]
- Coste estimado de litigios y reclamaciones de interesados: [€]
- Coste de daño reputacional (estimado como % de facturación): [%]
- Coste de suspensión operativa (como en caso AENA): [€/día × días estimados]
- Coste de medidas correctoras ordenadas por AEPD: [€]

SUBTOTAL COSTES DIRECTOS = SUMA de los anteriores
TOTAL CNC = Sanciones esperadas + Costes directos
```

### Sección B: Inversión en Cumplimiento (IC)

**Presupuesto de mejora estimado** (categorías editables):

```
B1: DPO (interno o externo): [€/año]
B2: Herramientas de gestión de privacidad (OneTrust, Privacera, etc.): [€/año]
B3: Formación y concienciación: [€/año]
B4: Consultoría y auditorías externas: [€/proyecto]
B5: Implementación técnica PbD (Privacy by Design en proyectos): [% presupuesto TI]
B6: Herramientas de automatización LINDDUN (PILLAR, etc.): [€/año]
B7: Certificaciones (ISO 27701, ENS): [€/ciclo]

TOTAL IC = SUMA(B1:B7)
```

### Sección C: Cálculo del ROI

```excel
ROI_PRIVACIDAD (%) = ((CNC_Total - IC_Total) / IC_Total) × 100

Periodo_Recuperacion (meses) = IC_Total / (CNC_Total / 12)

Beneficio_Neto_3años = (CNC_Total × 3) - (IC_Total × 3)
```

### Panel de resultados ROI:

```
┌─────────────────────────────────────────────────────────────┐
│  ANÁLISIS COSTE-BENEFICIO DE PRIVACIDAD                     │
│  ═══════════════════════════════════════════════════════    │
│  Coste de No Cumplimiento (CNC anual):     [€ XXX.XXX]      │
│  Inversión en Cumplimiento (IC anual):     [€ XX.XXX]       │
│  ─────────────────────────────────────────────────────      │
│  ROI de la Inversión en Privacidad:        [XXX%] 📈         │
│  Período de recuperación de la inversión:  [X,X meses]      │
│  Beneficio neto proyectado (3 años):       [€ XXX.XXX]      │
└─────────────────────────────────────────────────────────────┘
```

**Nota metodológica**: El CNC es una estimación conservadora basada en probabilidades estadísticas de sanciones. No constituye asesoramiento jurídico. Para cálculos de riesgo legal, consultar con abogado especializado.

---

## HOJA 6: BENCHMARKING — Comparación Sectorial

### Tabla de percentiles sectoriales 2025–2026

*(Datos de referencia del Observatorio de la Privacidad — ISMS Forum España 2025 e informes ENISA)*

```
Col A: Módulo LINDDUN
Col B: IGM de la organización (vinculado a IGM_CALCULO)
Col C: Percentil 25 (sector)  → "Cuartil inferior"
Col D: Percentil 50 (sector)  → "Mediana sectorial"
Col E: Percentil 75 (sector)  → "Cuartil superior (buenas prácticas)"
Col F: Mejor práctica sectorial → "Referente del sector"
Col G: Posición relativa (=SI(B<C;"Por debajo del 25%";SI(B<D;"Entre 25-50%";SI(B<E;"Entre 50-75%";"Top 25%"))))
```

### Gráfico de posicionamiento:

Gráfico de barras agrupadas con:
- Barra azul oscuro: puntuación de la organización
- Barra gris claro: mediana sectorial
- Línea roja punteada: nivel mínimo recomendado

---

## HOJA 7: PLAN_MEJORA — Generador de Plan de Acción

### Generación automática basada en respuestas:

El plan de mejora se genera automáticamente a partir de todos los ítems con respuesta A o B, ordenados por:
1. **Nivel de riesgo regulatorio** (🔴 primero, ⚠️ segundo)
2. **Peso del módulo** en el IGM
3. **Facilidad de implementación** (estimada por tipo de medida)

### Estructura de cada acción del plan:

```
Col A: Prioridad (1–N, calculada automáticamente)
Col B: Pregunta origen (P1.1, P2.2, etc.)
Col C: Módulo / Indicador LINDDUN
Col D: Respuesta actual (A/B)
Col E: Nivel objetivo recomendado (C/D/E)
Col F: Acción de mejora recomendada (texto pre-cargado por ítem)
Col G: Normativa implicada (RGPD Art. / AI Act Art. / NIS2 Art.)
Col H: Plazo recomendado (Inmediato / 3 meses / 6 meses / 12 meses)
Col I: Responsable sugerido (DPO / CISO / CTO / Legal / Negocio)
Col J: Recursos estimados (€ orientativo)
Col K: Estado (Pendiente / En curso / Completada) — editable
Col L: Fecha prevista de completación
Col M: Fecha real de completación
```

### Resumen del plan:

```
Total acciones identificadas: [N]
- Prioridad INMEDIATA (riesgo 🔴): [N]
- Prioridad ALTA (≤3 meses): [N]
- Prioridad MEDIA (≤6 meses): [N]
- Prioridad BAJA (≤12 meses): [N]

Presupuesto total estimado: [€]
IGM proyectado tras implementación: [X%]
```

---

## HOJA 8: NOTAS_AUDITORIA — Registro de Evidencias

### Tabla de evidencias por módulo:

```
Col A: Código pregunta
Col B: Tipo de evidencia (Documento / Política / Sistema / Entrevista / Test técnico)
Col C: Nombre del documento/evidencia
Col D: Fecha del documento
Col E: Responsable del documento
Col F: Ubicación (ruta de archivo o URL interna)
Col G: Estado de vigencia (Vigente / Desactualizado / Pendiente de crear)
Col H: Observaciones del facilitador
```

---

## INSTRUCCIONES DE IMPLEMENTACIÓN

### En Microsoft Excel (365 o 2021+):

1. Crear un nuevo libro con las 8 hojas descritas.
2. Nombrar las pestañas exactamente como se indica.
3. Implementar las fórmulas de la Hoja 3 (IGM_CALCULO) antes que el resto.
4. Crear los rangos con nombre (`NombreRango`) para facilitar las referencias entre hojas.
5. Proteger las hojas de fórmulas (Revisar > Proteger hoja) dejando desbloqueadas solo las celdas de entrada de datos.
6. Configurar los formatos condicionales para los semáforos visuales.
7. Crear el gráfico radar en la Hoja 4 a partir de los datos calculados en Hoja 3.

### En Google Sheets:

Los mismos pasos son aplicables. El gráfico radar en Google Sheets requiere instalar el complemento "Chart Studio" o "Vega Chart" ya que los gráficos radar nativos tienen limitaciones de formato.

### Compatibilidad:
- Microsoft Excel 365: Compatibilidad total (incluyendo gráficos SparkLines en el panel IGM)
- Microsoft Excel 2019/2021: Compatible (verificar disponibilidad de fórmulas dinámicas)
- Google Sheets: Compatible con adaptaciones menores en gráficos
- LibreOffice Calc: Compatible con adaptaciones en fórmulas de formato condicional

---

## FÓRMULAS CLAVE — REFERENCIA RÁPIDA

```excel
// IGM Global (Hoja 3, celda B20)
=SUMAPRODUCTO(D2:D11; E2:E11)

// Puntuación por módulo (ejemplo Módulo 1, Hoja 3)
=PROMEDIO(RESPUESTAS!F2:F6)  // Ítems P1.1 a P1.5

// Clasificación automática IGM
=ELEGIR(COINCIDIR(B20;{0%;40%;60%;75%;90%;100%};1);"🔴 Muy Bajo";"🟠 Bajo";"🟡 Medio";"🟢 Alto";"💚 Muy Alto")

// ROI de privacidad (Hoja 5)
=((CNC_Total - IC_Total) / IC_Total) * 100

// Período de recuperación en meses
=IC_Total / (CNC_Total / 12)

// Número de ítems en riesgo alto (respuesta A o B)
=CONTAR.SI(RESPUESTAS!E:E;"A") + CONTAR.SI(RESPUESTAS!E:E;"B")

// Plan de mejora: priorización automática
// (requiere Power Query o fórmulas de ordenamiento dinámico en Excel 365)
=ORDENARPOR(tabla_acciones; columna_riesgo; -1; columna_peso; -1)
```

---

*Especificación técnica elaborada para implementación en Microsoft Excel 365 o Google Sheets. Versión 1.0 — Abril 2026. Compatible con plantillas de gestión de riesgos del ENS y con la metodología de EIPDs de la AEPD.*
