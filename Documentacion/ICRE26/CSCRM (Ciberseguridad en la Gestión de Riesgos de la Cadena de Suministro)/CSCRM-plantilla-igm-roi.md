# Plantilla IGM y ROI — Cálculo del Índice de Gestión de Madurez CSCRM
### Descripción funcional para implementación en Microsoft Excel / Google Sheets
**Versión 1.0 · Documento (e) del Kit de Encuesta CSCRM**

---

> *"Lo que no se mide no se gestiona. Y lo que no se gestiona en ciberseguridad de la cadena de suministro, eventualmente manda una factura de 4,33 millones de euros."*

---

## 1. Estructura General del Libro Excel

El archivo `CSCRM_IGM_ROI_v1.xlsx` se organiza en **8 hojas de cálculo**:

| N.º Hoja | Nombre | Función |
|----------|--------|---------|
| 1 | `PORTADA` | Identificación, instrucciones, versión |
| 2 | `DATOS_ENCUESTA` | Entrada de respuestas por pregunta |
| 3 | `PUNTUACION_DOMINIO` | Cálculo automático de subíndices por dominio |
| 4 | `IGM_GLOBAL` | Cálculo del IGM ponderado y semáforo de madurez |
| 5 | `BENCHMARK` | Comparativa con valores de referencia europeos (ENISA 2025) |
| 6 | `ROI_CSCRM` | Estimación del retorno de la inversión en CSCRM |
| 7 | `HOJA_RUTA` | Generación automática de plan de acción priorizado |
| 8 | `DASHBOARD` | Panel ejecutivo con gráficos de radar, semáforos y KPIs |

---

## 2. Hoja 1 — PORTADA

**Campos de identificación:**

```
[A1] ENCUESTA CSCRM ESPAÑA 2026 — CALCULADORA IGM / ROI
[A3] Organización: [campo editable]
[A4] Sector: [desplegable: lista sectores NIS2]
[A5] Tamaño: [desplegable: micro/pequeña/mediana/grande/corporación]
[A6] Fecha de cumplimentación: [campo fecha]
[A7] Responsable: [campo editable]
[A8] Versión del cuestionario: 1.0
[A10] INSTRUCCIONES:
[A11] 1. Cumplimente la hoja DATOS_ENCUESTA con las respuestas de su organización.
[A12] 2. El IGM se calculará automáticamente en la hoja IGM_GLOBAL.
[A13] 3. La hoja BENCHMARK muestra su posición relativa frente al sector.
[A14] 4. La hoja ROI_CSCRM estima el impacto económico de mejorar su madurez.
[A15] 5. La hoja HOJA_RUTA genera un plan de acción priorizado basado en sus brechas.
```

---

## 3. Hoja 2 — DATOS_ENCUESTA

### Estructura de columnas:

| Columna | Contenido |
|---------|-----------|
| A | Código de pregunta (P0.1, P1.1, etc.) |
| B | Texto resumido de la pregunta |
| C | Bloque temático |
| D | Dominio CSCRM (Gobernanza / Identificación / Protección / Detección / Resiliencia) |
| E | **Respuesta seleccionada** (entrada del usuario — celda editable) |
| F | Escala de respuesta (L0-L5 / Sí-No / Escala numérica) |
| G | Valor numérico asignado automáticamente a la respuesta (0-5) |
| H | Peso relativo de la pregunta dentro del dominio (%) |
| I | Puntuación ponderada = G × H |
| J | Indicador IMC correspondiente |
| K | Marco normativo primario |

### Tabla de conversión de respuestas a valores numéricos:

**Preguntas con escala L0-L5 (directas):**
```
L0 = 0 | L1 = 1 | L2 = 2 | L3 = 3 | L4 = 4 | L5 = 5
```

**Preguntas de selección única (conversión a escala 0-5):**

| Pregunta | Opción | Valor |
|----------|--------|-------|
| P1.3 (Formación Alta Dirección) | Regular con simulaciones | 5 |
| | Ocasional por incidentes | 3 |
| | Solo informes escritos | 2 |
| | Solo equipo técnico | 1 |
| | No, todavía en Comité de Presupuesto | 0 |
| P1.4 (Comité CSCRM) | Multidisciplinar completo | 5 |
| | Solo TI/ciberseguridad | 3 |
| | Dentro de comité general | 2 |
| | Caso a caso | 1 |
| | No existe | 0 |
| P1.5 (Presupuesto CSCRM) | > 20% | 5 |
| | 10-20% | 4 |
| | 5-10% | 3 |
| | < 5% | 1 |
| | Sin partida específica | 0 |
| | Desconocido | 0 |
| P4.7 (Tiempo detección) | < 24 horas | 5 |
| | 1-7 días | 4 |
| | 1 semana-1 mes | 3 |
| | 1-6 meses | 1 |
| | > 6 meses | 0 |
| | No medido / No detectado | 0 |
| P11.1 (Autoevaluación 1-10) | 9-10 | 5 |
| | 7-8 | 4 |
| | 5-6 | 3 |
| | 3-4 | 1 |
| | 1-2 | 0 |

**Preguntas de selección múltiple (scoring por número de opciones seleccionadas):**
```
Fórmula: VALOR = MIN(5, CONTAR.SI(rango_respuesta, "SELECCIONADO") × (5 / total_opciones_relevantes))
```

---

## 4. Hoja 3 — PUNTUACION_DOMINIO

### Cálculo de subíndices por dominio:

```
IGM-G (Gobernanza) = SUMA.PRODUCTO(valores_bloque_I; pesos_bloque_I) / SUMA(pesos_bloque_I)
Preguntas incluidas: P1.1, P1.2, P1.3, P1.4, P1.5, P1.6, P1.7, P1.8

IGM-I (Identificación y Evaluación) = SUMA.PRODUCTO(valores_bloque_II; pesos_bloque_II) / SUMA(pesos_bloque_II)
Preguntas incluidas: P2.1, P2.2, P2.3, P2.4, P2.5, P2.6, P2.7, P2.8

IGM-P (Protección y Controles Técnicos) = SUMA.PRODUCTO(valores_bloques_III_VII_VIII; pesos) / SUMA(pesos)
Preguntas incluidas: P3.1-P3.6, P7.1-P7.8, P8.1-P8.5

IGM-D (Detección y Supervisión) = SUMA.PRODUCTO(valores_bloque_IV; pesos_bloque_IV) / SUMA(pesos_bloque_IV)
Preguntas incluidas: P4.1, P4.2, P4.3, P4.4, P4.5, P4.6, P4.7

IGM-R (Respuesta, Recuperación y Resiliencia) = SUMA.PRODUCTO(valores_bloques_V_VI_IX; pesos) / SUMA(pesos)
Preguntas incluidas: P5.1-P5.4, P6.1-P6.3, P9.1-P9.4
```

### Subíndices temáticos emergentes:

```
IGM-SBOM = PROMEDIO(P7.1, P7.2) → escala 0-5
IGM-PQC  = PROMEDIO(P7.3, P7.4) → escala 0-5
IGM-IA   = PROMEDIO(P7.5, P7.6, P7.7, P7.8) → escala 0-5
IGM-ZT   = PROMEDIO(P8.1, P8.2, P8.3, P8.4, P8.5) → escala 0-5
```

**Visualización recomendada en esta hoja:**
- Gráfico de barras horizontales mostrando los 5 dominios con código de color (rojo <2; naranja 2-3; amarillo 3-4; verde >4)
- Tabla de brechas: columna "Valor actual" | "Umbral objetivo" | "Brecha" | "Prioridad"

---

## 5. Hoja 4 — IGM_GLOBAL

### Fórmula del IGM ponderado:

```
IGM = (IGM-G × 0,20) + (IGM-I × 0,20) + (IGM-P × 0,25) + (IGM-D × 0,20) + (IGM-R × 0,15)
```

### Tabla de semáforo de madurez (formato condicional):

| Rango IGM | Color | Nivel | Mensaje automático |
|-----------|-------|-------|--------------------|
| 0,0 – 1,0 | 🔴 Rojo | Crítico | "Acción inmediata requerida. Riesgo sistémico elevado." |
| 1,1 – 2,0 | 🟠 Naranja | Inicial | "Establecer gobernanza básica en 90 días." |
| 2,1 – 3,0 | 🟡 Amarillo | En desarrollo | "Completar contratos, monitorización y respuesta." |
| 3,1 – 4,0 | 🟢 Verde claro | Avanzado | "Integrar SBOM, PQC y evaluaciones n-tier." |
| 4,1 – 5,0 | 💚 Verde | Optimizando | "Liderar iniciativas sectoriales; preparar PQC." |

### Gráfico radar (pentágono de dominios):
- 5 ejes: Gobernanza / Identificación / Protección / Detección / Resiliencia
- Serie 1 (azul): Valores actuales de la organización
- Serie 2 (gris discontinuo): Benchmark europeo ENISA 2025
- Serie 3 (verde claro): Objetivo L3 mínimo NIS2

---

## 6. Hoja 5 — BENCHMARK

### Valores de referencia (fuentes: ENISA NIS Investments 2025, ENISA Good Practices 2023, Cipher/Prosegur 2026):

| Indicador | España (estimado) | Media UE | Percentil 75 UE | Objetivo NIS2 |
|-----------|-------------------|----------|-----------------|---------------|
| % org. con política CSCRM formal | ~60% | ~72% | ~90% | 100% |
| % org. con inventario proveedores TIC | ~55% | ~68% | ~85% | 100% |
| % org. con evaluación pre-contrato | ~40% | ~47% | ~70% | 80% |
| % contratos con cláusulas ciberseguridad | ~45% | ~61% | ~80% | 90% |
| % org. con monitorización continua | ~35% | ~43% | ~65% | 70% |
| % org. con PRI que incluye cadena de suministro | ~30% | ~38% | ~60% | 75% |
| % org. que exige SBOM | ~15% | ~22% | ~40% | 50% (CRA) |
| % org. con evaluación PQC iniciada | ~8% | ~12% | ~25% | 30% (2026) |
| Tiempo medio detección incidente CS (días) | ~254 | ~220 | ~90 | <60 |
| % org. con BCP probado (escenarios proveedor) | ~25% | ~35% | ~58% | 60% |

**Instrucciones para la hoja:**
- Columna A: Indicador
- Columna B: Valor de la organización (vinculado a PUNTUACION_DOMINIO)
- Columna C: Valor benchmark España (hardcoded con actualización anual)
- Columna D: Valor benchmark UE medio
- Columna E: Percentil 75 UE
- Columna F: Objetivo NIS2/ENS
- Columna G: Diferencia vs. benchmark España (B-C); formato condicional (verde si ≥0, rojo si <0)
- Columna H: Percentil estimado de la organización en la distribución española (calculado mediante interpolación)

---

## 7. Hoja 6 — ROI_CSCRM

### Modelo de estimación de ROI basado en la reducción del riesgo esperado

#### Paso 1 — Estimación del riesgo anual sin mejora CSCRM (ALE base)

```
[C5]  Número de proveedores TIC críticos (N_prov):                [entrada usuario]
[C6]  Probabilidad anual de incidente por proveedor (p_incidente): 0,08 (benchmark: 8% anual)
[C7]  Coste medio por incidente CS (M€):                          4,33  (Cipher/Prosegur 2026)
[C8]  Factor de impacto por nivel de madurez IGM actual:
      SI(IGM<2; 1,5; SI(IGM<3; 1,2; SI(IGM<4; 1,0; 0,7)))

[C10] ALE_base = N_prov × p_incidente × Coste_medio × Factor_impacto
      Fórmula: =C5 * C6 * C7 * C8 * 1000000
```

#### Paso 2 — Estimación del riesgo anual con mejora CSCRM (ALE mejorado)

```
[C15] Nivel de madurez IGM objetivo (introducido por usuario):     [entrada]
[C16] Reducción de probabilidad estimada por nivel de madurez:
      BUSCARV(IGM_objetivo; tabla_reduccion; 2; VERDADERO)

      Tabla de reducción (basada en FAIR Institute 2025 + ENISA):
      IGM 1→2: reducción 15% | IGM 2→3: 25% | IGM 3→4: 35% | IGM 4→5: 45%

[C18] ALE_mejorado = ALE_base × (1 - Reduccion_acumulada)
```

#### Paso 3 — Estimación de la inversión requerida (CAPEX + OPEX anual)

```
[C25] Coste herramientas evaluación/monitorización proveedores:     [entrada]
[C26] Coste consultoría (gap analysis, cuestionarios, auditorías): [entrada]
[C27] Coste formación del personal:                                 [entrada]
[C28] Coste adaptación contractual (horas legales internas):        [entrada]
[C29] Coste herramientas PAM / Zero Trust para proveedores:         [entrada]
[C30] TOTAL Inversión CSCRM (año 1):     =SUMA(C25:C29)
[C31] TOTAL Inversión CSCRM (año 2-3):   =C30 * 0,4  (estimado: 40% del año 1 = mantenimiento)
```

#### Paso 4 — Cálculo del ROI y período de recuperación

```
[C38] Reducción ALE = ALE_base - ALE_mejorado
[C39] ROI año 1 = (Reduccion_ALE - Inversion_año1) / Inversion_año1 × 100
[C40] ROI año 3 (acumulado) = (Reduccion_ALE × 3 - Inversion_total_3años) / Inversion_total_3años × 100
[C41] Período de recuperación (meses) = Inversion_año1 / (Reduccion_ALE / 12)
[C42] VAN a 3 años (tasa descuento 8%) = VNA(8%; Reduccion_ALE; Reduccion_ALE; Reduccion_ALE) - Inversion_año1
```

#### Tabla resumen ROI (generada automáticamente):

| Métrica | Valor calculado |
|---------|----------------|
| ALE actual (riesgo anual sin mejora) | [calculado] M€ |
| ALE mejorado (con programa CSCRM) | [calculado] M€ |
| Reducción anual del riesgo esperado | [calculado] M€ |
| Inversión total año 1 | [entrada] M€ |
| ROI año 1 | [calculado] % |
| ROI acumulado año 3 | [calculado] % |
| Período de recuperación | [calculado] meses |
| VAN a 3 años | [calculado] M€ |

---

## 8. Hoja 7 — HOJA_RUTA

### Generación automática del plan de acción CSCRM

Esta hoja genera automáticamente un plan de acción priorizado basado en las brechas identificadas en PUNTUACION_DOMINIO, ordenado por:
1. **Criticidad normativa** (controles obligatorios primero: ENS, NIS2, DORA)
2. **Impacto en IGM** (acciones que más mejoran el IGM)
3. **Facilidad de implementación** (esfuerzo estimado: bajo/medio/alto)

#### Estructura de la tabla de acciones:

| Col. | Contenido |
|------|-----------|
| A | Código acción (CSCRM-A1... CSCRM-D5) |
| B | Pregunta origen (Px.x) |
| C | Descripción de la acción de mejora |
| D | Dominio CSCRM |
| E | Valor actual (L0-L5) |
| F | Objetivo recomendado |
| G | Brecha (F-E) |
| H | Impacto en IGM (si se completa esta acción) |
| I | Obligatoriedad normativa (✅ Obligatorio / 📋 Recomendado / 🔜 Emergente) |
| J | Esfuerzo estimado (bajo/medio/alto) |
| K | Plazo recomendado (inmediato <30d / corto 90d / medio 6m / largo 12m) |
| L | Responsable sugerido |
| M | Estado (campo editable: Pendiente / En curso / Completado) |
| N | Fecha objetivo (campo editable) |

#### Lógica de priorización (columna automática "Prioridad"):
```
Prioridad = (Brecha × 2) + (Impacto_IGM × 3) + (SI(Obligatorio; 5; SI(Recomendado; 2; 0))) - (SI(Esfuerzo="alto"; 2; SI(Esfuerzo="medio"; 1; 0)))
```

---

## 9. Hoja 8 — DASHBOARD

### Panel ejecutivo (una sola página imprimible en A3)

**Componente 1 — Semáforo IGM global** (celda grande con formato condicional color)
```
IGM: [valor] / 5,0 — Nivel: [texto nivel] — [emoji semáforo]
```

**Componente 2 — Gráfico radar pentagonal** (5 dominios)
- Valores actuales vs. benchmark UE vs. objetivo NIS2

**Componente 3 — Tabla de subíndices** (6 filas: 5 dominios + IGM global)
| Dominio | Valor | Benchmark UE | Gap | Semáforo |
|---------|-------|-------------|-----|----------|

**Componente 4 — Top 5 acciones prioritarias** (vinculado a HOJA_RUTA, filtrado por las 5 primeras)

**Componente 5 — Métricas emergentes**
| Indicador | Valor | Estado |
|-----------|-------|--------|
| IGM-SBOM | [val] | [semáforo] |
| IGM-PQC | [val] | [semáforo] |
| IGM-IA | [val] | [semáforo] |
| IGM-ZT | [val] | [semáforo] |

**Componente 6 — ROI estimado** (caja resumen)
```
Reducción riesgo anual estimada: [X] M€
Inversión requerida año 1: [Y] M€
ROI año 1: [Z]% | Período recuperación: [N] meses
```

---

## 10. Notas de Implementación

### Configuración de la hoja de cálculo:
- Proteger todas las celdas de fórmulas (solo editables las celdas marcadas en amarillo)
- Validación de datos en celdas de entrada (listas desplegables para opciones L0-L5 y respuestas categóricas)
- Formato condicional aplicado a todas las celdas de puntuación (verde ≥4, amarillo 2-3, rojo ≤1)
- Contraseña de protección de hoja: recomendado para versiones institucionales
- Idioma de fórmulas: español (SUMA, PROMEDIO, SI, BUSCARV, SUMA.PRODUCTO, VNA)

### Actualización de benchmarks:
- Los valores de la hoja BENCHMARK deben actualizarse anualmente con los datos del informe ENISA NIS Investments del año en curso
- Fuente primaria para benchmarks nacionales: Balance de Ciberseguridad anual de INCIBE

### Compatibilidad:
- Microsoft Excel 365 / 2019 / 2021 (PC y Mac)
- Google Sheets (con adaptación de algunas funciones: BUSCARV → VLOOKUP, VNA → NPV)
- LibreOffice Calc (compatibilidad parcial; requiere verificación de fórmulas avanzadas)

---

*© 2026 · Plantilla IGM/ROI CSCRM España · Documento (e) del Kit de Encuesta*
*Referencias para valores de benchmark: ENISA NIS Investments 2025 · ENISA Good Practices SC 2023 · Cipher/Prosegur Supply Chain Report 2026 · FAIR Institute State of Cyber Risk Management 2025*
