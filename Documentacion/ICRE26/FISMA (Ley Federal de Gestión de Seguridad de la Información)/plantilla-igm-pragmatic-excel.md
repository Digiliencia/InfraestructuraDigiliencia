# PLANTILLA EXCEL: IGM-PRAGMATIC Y ROSI
## Índice Global de Madurez con Ponderación PRAGMATIC + Retorno sobre Inversión en Seguridad
### Kit GQM+PRAGMATIC FISMA 2025 — Documento (e) · Versión 1.0 · Abril 2026

---

> *"Un IGM ponderado por PRAGMATIC no es lo mismo que un IGM simple. Es la diferencia entre el peso bruto de los activos y su valor en libros: ambos son números, pero uno cuenta para los que saben."*

---

## DESCRIPCIÓN DEL LIBRO EXCEL

**Nombre del fichero:** `FISMA_GQM_PRAGMATIC_IGM_ROSI_v1.xlsx`
**Número de pestañas:** 10
**Compatibilidad:** Microsoft Excel 365 / Google Sheets / LibreOffice Calc 7.x+

### Pestañas del libro:
1. `PORTADA` — Presentación, instrucciones y créditos
2. `DATOS_ORG` — Perfil de la organización
3. `PRAGMATIC_SCORES` — Scores PRAGMATIC por métrica (editables)
4. `RESPUESTAS_GQM` — Respuestas a las preguntas GQM de la encuesta
5. `IGM_SIMPLE` — IGM sin ponderación PRAGMATIC (comparación)
6. `IGM_PRAGMATIC` — **IGM ponderado por scores PRAGMATIC** (módulo central)
7. `ROSI_CALCULO` — Cálculo del Retorno sobre la Inversión en Seguridad
8. `POAM_GQM` — Plan de Acción con trazabilidad GQM
9. `DASHBOARD` — Panel visual integrado con semáforos
10. `BENCHMARKS` — Referencias sectoriales y ENISA/CCN datos 2025

---

## PESTAÑA 1: PORTADA

**Elementos:**
- Título: "Kit GQM+PRAGMATIC FISMA 2025 — Herramienta de Cálculo"
- Subtítulo: "Índice Global de Madurez ponderado por calidad PRAGMATIC + ROSI"
- Versión y fecha: v1.0 · Abril 2026
- Descripción breve del marco teórico (GQM + PRAGMATIC + FISMA FY2025)
- Tabla de atajos de navegación con hipervínculos a cada pestaña
- Instrucciones de uso en 5 pasos
- Disclaimer: "Herramienta orientativa. Los resultados deben ser validados por auditor ENS certificado para efectos normativos formales."

---

## PESTAÑA 2: DATOS_ORG (Perfil de la Organización)

| Fila | Campo | Tipo | Validación |
|---|---|---|---|
| 3 | Nombre / Código organización | Texto libre | — |
| 4 | Comunidad Autónoma | Lista desplegable | 17 CC.AA. + Ceuta + Melilla |
| 5 | Tipo de entidad | Lista | AAPP Autonómica / AAPP Local / AAPP Estatal / Empresa Privada / Infraestructura Crítica |
| 6 | Sector NIS2 | Lista | 18 sectores Anexo I y II NIS2 + Otros |
| 7 | Nº empleados | Número entero | ≥ 1 |
| 8 | Fecha de evaluación | Fecha | Validación formato DD/MM/AAAA |
| 9 | Respondente (rol) | Lista | CISO / CIO / Director / Responsable Seguridad / Consultor / Auditor |
| 10 | Presupuesto TI anual (€) | Número | > 0 |
| 11 | Presupuesto ciberseguridad anual (€) | Número | > 0 |
| 12 | **% cyber/TI** | Fórmula: `=B11/B10` | Formato % |
| 13 | Perfil de ponderación PRAGMATIC | Lista | AAPP estándar / Infraestructura Crítica / PYME / Investigación personalizada |
| 14 | Periodo de referencia de datos | Texto | Ej: "Ejercicio 2025 · Enero-Diciembre" |

---

## PESTAÑA 3: PRAGMATIC_SCORES (Scores Editables por Métrica)

**Propósito:** Permite al evaluador ajustar los scores PRAGMATIC preconfigurados según la realidad de su organización. Los scores por defecto son los del documento (b) de este kit.

### Estructura de la tabla (una fila por métrica):

| Col A | Col B | Col C | Col D | Col E | Col F | Col G | Col H | Col I | Col J | Col K | Col L |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ID Métrica | Nombre | P | R | A | G | M | Ac | T | I | C | **TOTAL** |
| Gov-1 | Cybersecurity Governance Program | [EDIT: def=7] | [EDIT: def=9] | [EDIT: def=8] | [EDIT: def=7] | [EDIT: def=9] | [EDIT: def=7] | [EDIT: def=8] | [EDIT: def=7] | [EDIT: def=8] | `=SUMA(C2:K2)` |
| Gov-2 | Leadership Accountability | 6 | 9 | 8 | 6 | 9 | 6 | 7 | 7 | 8 | `=SUMA(C3:K3)` |
| Gov-3 | Risk Tolerance Statement | 7 | 8 | 7 | 7 | 8 | 7 | 6 | 8 | 9 | `=SUMA(C4:K4)` |
| ... (25 métricas) | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Celdas de resumen (por criterio PRAGMATIC):**
```
B28: Promedio P global   = PROMEDIO(C2:C26)
B29: Promedio R global   = PROMEDIO(D2:D26)
B30: Promedio A global   = PROMEDIO(E2:E26)
B31: Promedio G global   = PROMEDIO(F2:F26)
B32: Promedio M global   = PROMEDIO(G2:G26)
B33: Promedio Ac global  = PROMEDIO(H2:H26)
B34: Promedio T global   = PROMEDIO(I2:I26)
B35: Promedio I global   = PROMEDIO(J2:J26)
B36: Promedio C global   = PROMEDIO(K2:K26)
B37: Score medio global  = PROMEDIO(L2:L26)
B38: Criterio más fuerte = INDICE({"P";"R";"A";"G";"M";"Ac";"T";"I";"C"},COINCIDIR(MAX(B28:B36),B28:B36,0))
B39: Criterio más débil  = INDICE({"P";"R";"A";"G";"M";"Ac";"T";"I";"C"},COINCIDIR(MIN(B28:B36),B28:B36,0))
```

**Columnas adicionales de análisis:**
- Col M: Calificación estrella: `=ELEGIR(TRUNCAR((L2-40)/10)+1,"✗ Inadecuada","★☆☆☆☆ Débil","★★☆☆☆ Aceptable","★★★☆☆ Buena","★★★★☆ Muy buena","★★★★★ Excelente")`
- Col N: Categoría de adopción: `=SI(L2>=71,"A - Inmediata",SI(L2>=61,"B - Con adaptación",SI(L2>=51,"C - Fase 2","D - Rediseñar")))`
- Col O: Criterio más débil de la métrica: función personalizada que identifica el criterio con menor puntuación en la fila

---

## PESTAÑA 4: RESPUESTAS_GQM (Codificación de Respuestas)

**Estructura:** Una fila por pregunta GQM; columnas para ID, pregunta resumida, respuesta seleccionada y puntuación de madurez (1-5).

| Col A | Col B | Col C | Col D | Col E | Col F |
|---|---|---|---|---|---|
| ID | Pregunta resumida | Respuesta (A-E) | Puntuación madurez (1-5) | Módulo GQM | Métrica FISMA vinculada |
| Q-GOV-1 | ¿Existe programa formal gobernanza? | [VARIABLE A-E] | `=SI(C2="A",5,SI(C2="B",4,SI(C2="C",3,SI(C2="D",2,1))))` | GOAL-I | Gov-1 |
| Q-GOV-2 | ¿Dirección toma decisiones con datos? | [VARIABLE] | fórmula análoga | GOAL-I | Gov-2 |
| Q-GOV-3 | ¿Risk tolerance definida y comunicada? | [VARIABLE] | fórmula análoga | GOAL-I | Gov-3 |
| Q-SCRM-1 | ¿Inventario proveedores críticos? | [VARIABLE] | fórmula | GOAL-II | SCRM-1 |
| ... (29 preguntas GQM) | ... | ... | ... | ... | ... |

**Columna G (Puntuación ajustada por PRAGMATIC):**
```
G2 = D2 * (PRAGMATIC_SCORES!L[fila métrica vinculada] / 90)
```
*Esta columna multiplica la puntuación de madurez por el "factor de confianza PRAGMATIC" de la métrica, reduciendo el peso de las métricas menos fiables en el IGM ponderado.*

---

## PESTAÑA 5: IGM_SIMPLE (IGM sin Ponderación PRAGMATIC)

**Propósito:** Calcular el IGM tradicional (sin ajuste PRAGMATIC) para comparar con el IGM ponderado.

### Tabla de puntuaciones por módulo GQM:

| Módulo | Objetivo GQM | Preguntas | Puntuación media | Ponderación | Puntuación ponderada |
|---|---|---|---|---|---|
| GOAL-I | Gobernanza | Q-GOV-1/2/3 | `=PROMEDIO(Respuestas!D2:D4)` | 15% | `=C2*D2` |
| GOAL-II | C-SCRM | Q-SCRM-1/2/3 | `=PROMEDIO(Respuestas!D5:D7)` | 10% | `=C3*D3` |
| GOAL-III | Riesgos/Activos | Q-RA-1/2/3 | `=PROMEDIO(Respuestas!D8:D10)` | 10% | `=C4*D4` |
| GOAL-IV | Configuración | Q-CM-1/2/3 | `=PROMEDIO(Respuestas!D11:D13)` | 8% | `=C5*D5` |
| GOAL-V | IDAM/ZTA | Q-IDAM-1/2/3/4 | `=PROMEDIO(Respuestas!D14:D17)` | 12% | `=C6*D6` |
| GOAL-VI | Datos/Privacidad | Q-DP-1/2/3 | `=PROMEDIO(Respuestas!D18:D20)` | 10% | `=C7*D7` |
| GOAL-VII | Formación | Q-ST-1/2 | `=PROMEDIO(Respuestas!D21:D22)` | 5% | `=C8*D8` |
| GOAL-VIII | Monitorización | Q-ISCM-1/2/3/4 | `=PROMEDIO(Respuestas!D23:D26)` | 12% | `=C9*D9` |
| GOAL-IX | Incidentes | Q-IR-1/2/3 | `=PROMEDIO(Respuestas!D27:D29)` | 10% | `=C10*D10` |
| GOAL-X | Continuidad | Q-CP-1/2 | `=PROMEDIO(Respuestas!D30:D31)` | 8% | `=C11*D11` |
| **IGM SIMPLE** | | | | **100%** | **`=SUMA(E2:E11)`** |

### Interpretación:
```
B15: IGM_simple = =E12
B16: Nivel_simple = =SI(B15>=4.5,"Optimized",SI(B15>=3.5,"Managed",SI(B15>=2.5,"Consistently Impl.",SI(B15>=1.5,"Defined","Ad Hoc"))))
B17: Efectivo_simple = =SI(B15>=3.5,"✓ SÍ (≥ umbral L4)","✗ NO (< umbral L4)")
```

---

## PESTAÑA 6: IGM_PRAGMATIC (Módulo Central — IGM Ponderado)

**Propósito:** El IGM ponderado por PRAGMATIC es la contribución diferencial de este kit. Las métricas con mayor score PRAGMATIC tienen mayor peso en el IGM final, pues son más fiables.

### Fórmula del IGM ponderado por PRAGMATIC:

\[ IGM_{PRAGMATIC} = \frac{\sum_{i=1}^{n} (Puntuacion\_madurez_i \times Ponderacion\_modulo_i \times Factor\_PRAGMATIC_i)}{\sum_{i=1}^{n} (Ponderacion\_modulo_i \times Factor\_PRAGMATIC_i)} \]

Donde `Factor_PRAGMATIC_i = Score_PRAGMATIC_i / 90`

**Implementación en Excel:**

```
Para cada métrica i en columna (una fila por métrica):
Col A: ID Métrica
Col B: Nombre métrica
Col C: Puntuación madurez (de Respuestas_GQM!D)
Col D: Ponderación módulo (fracción del 100%)
Col E: Score PRAGMATIC (de PRAGMATIC_SCORES!L)
Col F: Factor PRAGMATIC = =E2/90
Col G: Numerador = =C2*D2*F2
Col H: Denominador = =D2*F2

Celda B30 (IGM PRAGMATIC):
=SUMA(G2:G26) / SUMA(H2:H26)

Celda B31 (IGM Simple para comparación):
=IGM_SIMPLE!B15

Celda B32 (Diferencia IGM-PRAGMATIC vs IGM-Simple):
=B30-B31
(Positivo → métricas bien medidas compensan; Negativo → métricas débiles inflan el IGM simple)

Celda B33 (Nivel PRAGMATIC):
=SI(B30>=4.5,"Optimized ★★★★★",SI(B30>=3.5,"Managed ★★★★☆",SI(B30>=2.5,"Consistently Impl. ★★★☆☆",SI(B30>=1.5,"Defined ★★☆☆☆","Ad Hoc ★☆☆☆☆"))))

Celda B34 (Efectividad PRAGMATIC):
=SI(B30>=3.5,"✓ EFECTIVO bajo criterios FISMA FY2025","✗ INEFECTIVO — brechas en métricas críticas")
```

### Tabla de desglose por módulo GQM (con factor PRAGMATIC):

| Módulo | IGM simple módulo | Factor PRAGMATIC módulo | IGM ponderado módulo | Diferencia | Interpretación |
|---|---|---|---|---|---|
| GOAL-I Gobernanza | [valor] | [promedio PRAGMATIC módulo/90] | [calculado] | [+/-] | Métricas de gobernanza son [más/menos] fiables que la media |
| GOAL-II C-SCRM | [valor] | [calculado] | [calculado] | [+/-] | ... |
| ... (10 módulos) | ... | ... | ... | ... | ... |

**Tabla de análisis de sensibilidad (qué pasaría si mejoramos los scores PRAGMATIC débiles):**
```
Escenario 1: Todos los criterios G (Genuino) suben a 8/10 → ¿Cuánto cambia el IGM PRAGMATIC?
Escenario 2: Todos los criterios T (Oportuno) suben a 8/10 → Impacto en IGM
Escenario 3: Métricas ZTA-S1/S2 alcanzan score 70+ → Impacto si se implementan correctamente
```
*(Implementar como Tabla de Datos de Excel con las tres celdas de Score como variables de entrada)*

### Gráfico comparativo IGM Simple vs IGM PRAGMATIC:
- Tipo: Gráfico de barras agrupadas horizontal
- Serie 1 (azul): IGM Simple por módulo
- Serie 2 (naranja): IGM PRAGMATIC por módulo
- Línea vertical roja: Umbral L4 = 3.5
- Interpretación: Los módulos donde la barra naranja (PRAGMATIC) es menor que la azul (Simple) son los que tienen métricas menos fiables — el "IGM inflado" visible.

---

## PESTAÑA 7: ROSI_CALCULO

*(Diseño idéntico al documento (e) del Kit FISMA 2025 anterior, con las siguientes adiciones específicas de GQM+PRAGMATIC)*

### Adición 1: Ajuste del ALE por fiabilidad PRAGMATIC

```
Celda B20: Factor_confianza_metricas = PROMEDIO(PRAGMATIC_SCORES!L2:L26) / 90
Celda B21: ALE_ajustado = ALE_total_antes * (2 - Factor_confianza_metricas)
```
*Lógica: si las métricas son poco fiables (score bajo), el riesgo real puede estar subestimado. El ALE ajustado refleja este incertidumbre aumentando el riesgo estimado inversamente proporcional a la fiabilidad de las métricas.*

### Adición 2: ROSI diferencial GQM vs. ROSI simple

```
ROSI_simple = (ALE_antes - ALE_despues - Inversion) / Inversion
ROSI_GQM = (ALE_ajustado - ALE_despues_ajustado - Inversion) / Inversion
ROSI_delta = ROSI_GQM - ROSI_simple
(Positivo → la corrección PRAGMATIC revela mayor rentabilidad real de la inversión)
```

### Adición 3: Inversión prioritaria basada en score PRAGMATIC

```
Tabla de mejoras con mayor ROI de medición:
Para cada métrica en Categoría C (score < 61):
  Coste_mejora_score_PRAGMATIC = [VARIABLE: inversión estimada para mejorar criterios débiles]
  Impacto_en_IGM_PRAGMATIC = (nuevo_score - score_actual) / 90 * Ponderacion_modulo * Puntuacion_madurez
  ROI_de_medicion = Impacto_en_IGM_PRAGMATIC / Coste_mejora_score_PRAGMATIC
```

---

## PESTAÑA 8: POAM_GQM (Plan de Acción con Trazabilidad GQM)

**Estructura ampliada respecto al POA&M estándar — incluye columnas GQM:**

| Col | Nombre | Tipo | Descripción |
|---|---|---|---|
| A | ID_acción | Texto | POA-GQM-001... |
| B | Módulo GQM | Lista | GOAL-I a GOAL-X |
| C | Objetivo GQM | Texto | Referencia al GOAL correspondiente |
| D | Métrica FISMA afectada | Texto | Gov-1, CM-2... |
| E | Score PRAGMATIC actual | Número | [Auto desde PRAGMATIC_SCORES] |
| F | Criterio PRAGMATIC más débil | Texto | [Auto: criterio con menor score] |
| G | Puntuación madurez actual | Número 1-5 | [Auto desde RESPUESTAS_GQM] |
| H | Puntuación madurez objetivo | Número 1-5 | [VARIABLE] |
| I | Acción de mejora (madurez) | Texto | Descripción de la acción |
| J | Acción de mejora (PRAGMATIC) | Texto | Cómo mejorar el criterio débil identificado |
| K | Recursos necesarios (€) | Número | [VARIABLE] |
| L | Responsable | Texto | [VARIABLE] |
| M | Fecha objetivo | Fecha | [VARIABLE] |
| N | Estado | Lista | En planificación / En curso / Completada |
| O | Impacto en IGM-PRAGMATIC | Fórmula | Mejora estimada en puntos de IGM ponderado |
| P | Prioridad combinada | Fórmula | Combina urgencia normativa + impacto IGM + score PRAGMATIC |

**Fórmula de prioridad combinada:**
```
P_combinada = (5 - G_actual) * Ponderacion_modulo * (1 + (90 - E_score_PRAGMATIC)/90)
```
*Las acciones en módulos con mayor ponderación, mayor brecha de madurez Y métricas menos fiables reciben mayor prioridad — porque mejorar la madurez en áreas donde no nos podemos fiar de la medición actual es doblemente urgente.*

---

## PESTAÑA 9: DASHBOARD

### Bloque 1 — KPIs Principales (fila superior):

| Tarjeta | Valor | Color semáforo | Fórmula |
|---|---|---|---|
| IGM PRAGMATIC | [valor /5] | Rojo<2.5 / Ámbar 2.5-3.5 / Verde>3.5 | =IGM_PRAGMATIC!B30 |
| IGM Simple | [valor /5] | Mismo criterio | =IGM_SIMPLE!B15 |
| Diferencia PRAGMATIC vs. Simple | [+/-] | Verde si positivo; rojo si negativo | =IGM_PRAGMATIC!B32 |
| Score PRAGMATIC medio | [valor /90] | Rojo<61 / Ámbar 61-70 / Verde>70 | =PROMEDIO(PRAGMATIC_SCORES!L2:L26) |
| ROSI estimado | [%] | Verde si >100%; ámbar 50-100%; rojo <50% | =ROSI_CALCULO!ROSI_GQM |
| Efectividad general | SÍ/NO | Verde/Rojo | =IGM_PRAGMATIC!B34 |

### Bloque 2 — Gráfico Radar Dual (IGM Simple vs. PRAGMATIC):
*10 ejes (un objetivo GQM por eje); dos series (simple y ponderado); línea umbral L4*

### Bloque 3 — Gráfico PRAGMATIC Radar de 9 Criterios:
*9 ejes (uno por criterio PRAGMATIC); muestra los scores medios de toda la organización*

### Bloque 4 — Clasificación de Métricas por Categoría:
```
Categoría A (Adopción inmediata): =CONTAR.SI(PRAGMATIC_SCORES!N2:N26,"A*")
Categoría B (Con adaptación): =CONTAR.SI(PRAGMATIC_SCORES!N2:N26,"B*")
Categoría C (Fase 2): =CONTAR.SI(PRAGMATIC_SCORES!N2:N26,"C*")
Categoría D (Rediseñar): =CONTAR.SI(PRAGMATIC_SCORES!N2:N26,"D*")
```

### Bloque 5 — Top 5 acciones prioritarias del POA&M-GQM:
*Tabla auto-actualizada con las 5 filas de mayor prioridad combinada del POA_GQM*

---

## PESTAÑA 10: BENCHMARKS

*(Complementa la pestaña BENCHMARKS del Kit base con datos PRAGMATIC específicos)*

| Sector | IGM Simple medio | IGM PRAGMATIC estimado | Score PRAGMATIC medio | Diferencia (inflación métrica) |
|---|---|---|---|---|
| AAPP Autonómica España 2025 | 2.8 | 2.5 | 62 | -0.3 (IGM simple sobreestima) |
| AAPP Local >20k hab. | 2.2 | 1.9 | 55 | -0.3 |
| Sanidad pública | 2.6 | 2.3 | 60 | -0.3 |
| Infraestructura Crítica | 3.4 | 3.2 | 71 | -0.2 |
| Referencia FISMA federal EE.UU. FY2025 | 3.7 | 3.6 | 78 | -0.1 |
| ENISA Top Quartile EU | 3.6 | 3.5 | 75 | -0.1 |

*Nota metodológica: el IGM PRAGMATIC es sistemáticamente inferior al simple porque los criterios G y T son los más débiles en todas las organizaciones — la medición raramente es tan buena como creemos. La brecha se reduce a medida que aumenta la madurez: organizaciones en L4+ tienen mejores herramientas automatizadas, lo que mejora los criterios T y C.*

---

## INSTRUCCIONES DE IMPLEMENTACIÓN (Resumen en 8 pasos)

1. Crear libro con 10 pestañas nombradas exactamente como se indica.
2. **PRAGMATIC_SCORES:** Introducir los 25 × 9 = 225 valores de score (usar valores por defecto del documento b de este kit como punto de partida; ajustar basándose en la realidad de la organización).
3. **DATOS_ORG:** Completar los 14 campos de perfil con validación de datos.
4. **RESPUESTAS_GQM:** Introducir las respuestas A-E de la encuesta GQM; las fórmulas calculan automáticamente las puntuaciones.
5. **IGM_SIMPLE e IGM_PRAGMATIC:** Las fórmulas calculan automáticamente a partir de RESPUESTAS_GQM y PRAGMATIC_SCORES.
6. **ROSI_CALCULO:** Introducir las variables de riesgo (ARO, SLE por tipo de amenaza) e inversión planificada.
7. **POAM_GQM:** Añadir las acciones de mejora; la prioridad combinada se calcula automáticamente.
8. **DASHBOARD:** Todos los valores se actualizan automáticamente desde las pestañas anteriores.

**Protección:** Bloquear todas las celdas de fórmula; desbloquear solo las marcadas como [VARIABLE].

---

*Kit GQM+PRAGMATIC FISMA 2025 — Plantilla Excel IGM-PRAGMATIC y ROSI · Versión 1.0 · Abril 2026*
*Fuentes: Basili et al. (1994) GQM; Brotby & Hinson (2013) PRAGMATIC; FY2025 IG FISMA Metrics v2.0; NIST CSF 2.0*
