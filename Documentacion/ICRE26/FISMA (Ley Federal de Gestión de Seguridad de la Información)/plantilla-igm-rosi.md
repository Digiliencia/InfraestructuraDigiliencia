# PLANTILLA DE CÁLCULO: IGM y ROI EN CIBERSEGURIDAD
## Índice Global de Madurez (IGM) y Retorno sobre la Inversión en Seguridad (ROSI)
### Kit de Encuesta FISMA 2025 — Hoja de cálculo descrita en Markdown (lista para implementar en Excel / LibreOffice Calc / Google Sheets)

---

> *"Lo que no se puede medir, no se puede gestionar. Y lo que no se puede gestionar, ciertamente ya no se puede asegurar."*
> — Adaptación libre de Peter Drucker, con perdón del maestro.

---

## INSTRUCCIONES DE IMPLEMENTACIÓN

Este documento describe con precisión el diseño de todas las hojas de cálculo del fichero `FISMA_IGM_ROSI_Calculator.xlsx`. Cada sección corresponde a una pestaña diferente del libro de Excel. Los valores entre **[VARIABLE]** son celdas de entrada que el usuario debe completar; las celdas con fórmulas están descritas entre corchetes con la notación Excel estándar.

**Pestañas del libro:**
1. `INICIO` — Portada e instrucciones
2. `DATOS_ORG` — Datos de la organización
3. `RESPUESTAS` — Codificación de respuestas de la encuesta
4. `IGM_CALCULO` — Cálculo del Índice Global de Madurez
5. `ROSI_CALCULO` — Cálculo del Retorno sobre Inversión en Seguridad
6. `DASHBOARD` — Panel de visualización de resultados
7. `BENCHMARKS` — Tabla de referencia con datos sectoriales
8. `POA_M` — Plan de Acción y Mejora con priorización automática

---

## PESTAÑA 1: INICIO

**Diseño:**
- Cabecera con logo institucional (celda fusionada A1:H3)
- Título: "Kit de Cálculo FISMA 2025 — IGM y ROSI"
- Versión: 1.0 | Fecha: Abril 2026
- Instrucciones de uso resumidas (celdas A5:H20)
- Índice de pestañas con hipervínculos (celdas A22:B30)
- Advertencia de datos: "Los resultados de este calculador son orientativos. Para evaluaciones formales, consultar con el CCN o un auditor certificado ENS."

---

## PESTAÑA 2: DATOS_ORG (Datos de la Organización)

| Celda | Campo | Tipo de dato | Ejemplo |
|---|---|---|---|
| B2 | Nombre / Código organización | Texto | "CC.AA. - Consejería Salud - COD001" |
| B3 | Comunidad Autónoma | Lista desplegable (17 CC.AA. + Ceuta + Melilla) | "Castilla y León" |
| B4 | Tipo de entidad | Lista desplegable | "AAPP Autonómica" |
| B5 | Sector | Lista desplegable (18 sectores NIS2 + Otros) | "Administración pública" |
| B6 | Tamaño (nº empleados) | Número entero | 3.500 |
| B7 | Fecha de la encuesta | Fecha | 09/04/2026 |
| B8 | Nombre del respondente (opcional) | Texto | "Anónimo" |
| B9 | Rol del respondente | Lista desplegable | "CISO" |
| B10 | Presupuesto TI anual (€) | Número | 4.500.000 |
| B11 | Presupuesto ciberseguridad (€) | Número | 450.000 |
| B12 | **% presupuesto cyber / TI [=B11/B10]** | Fórmula | **=B11/B10** (formato %) |
| B13 | Perfil de ponderación | Lista desplegable | "AAPP estándar / Infraestructura Crítica / PYME" |

---

## PESTAÑA 3: RESPUESTAS (Codificación de respuestas)

**Estructura:** Una fila por pregunta; columnas para número de pregunta, texto resumido, respuesta seleccionada (A/B/C/D/E) y puntuación calculada.

| Col A | Col B | Col C | Col D | Col E |
|---|---|---|---|---|
| N° Pregunta | Texto resumido | Respuesta (A-E) | Puntuación base | Módulo |
| P1 | Política Seguridad aprobada | [VARIABLE: lista A-E] | =SI(C2="A",5,SI(C2="B",3,SI(C2="C",2,SI(C2="D",1,1)))) | Módulo I |
| P2 | Participación órgano directivo | [VARIABLE] | =SI(C3="A",5,SI(C3="B",4,SI(C3="C",3,SI(C3="D",2,1)))) | Módulo I |
| P3 | Estrategia gestión riesgo | [VARIABLE] | =SI(C4="A",5,SI(C4="B",3,SI(C4="C",2,SI(C4="D",1,1)))) | Módulo I |
| ... | ... (filas P1 a P55) | ... | ... | ... |

**Tabla de conversión A-E → Puntuación (por defecto, ajustable):**

| Respuesta | Puntuación base | Nivel FISMA |
|---|---|---|
| A | 5 | Optimized / Managed & Measurable |
| B | 4 | Managed & Measurable |
| C | 3 | Consistently Implemented |
| D | 2 | Defined |
| E | 1 | Ad Hoc |

*Nota: Para preguntas donde la escala A-E no es estrictamente ordinal, se ajusta la fórmula individualmente en la columna D.*

---

## PESTAÑA 4: IGM_CALCULO (Cálculo del Índice Global de Madurez)

### Sección 4.1 — Puntuaciones por Módulo

| Módulo | Preguntas incluidas | Puntuación media | Ponderación AAPP | Puntuación ponderada |
|---|---|---|---|---|
| I — Gobernanza | P1:P5 | =PROMEDIO(Respuestas!D2:D6) | 15% | =C × D |
| II — C-SCRM | P6:P10 | =PROMEDIO(Respuestas!D7:D11) | 10% | =C × D |
| III — Gestión Riesgos/Activos | P11:P14 | =PROMEDIO(Respuestas!D12:D15) | 10% | =C × D |
| IV — Gestión Configuración | P15:P18 | =PROMEDIO(Respuestas!D16:D19) | 8% | =C × D |
| V — IDAM / Zero Trust | P19:P23 | =PROMEDIO(Respuestas!D20:D24) | 12% | =C × D |
| VI — Protección Datos | P24:P27 | =PROMEDIO(Respuestas!D25:D28) | 10% | =C × D |
| VII — Formación | P28:P30 | =PROMEDIO(Respuestas!D29:D31) | 5% | =C × D |
| VIII — Monitorización | P31:P35 | =PROMEDIO(Respuestas!D32:D36) | 12% | =C × D |
| IX — Respuesta Incidentes | P36:P40 | =PROMEDIO(Respuestas!D37:D41) | 10% | =C × D |
| X — Continuidad | P41:P44 | =PROMEDIO(Respuestas!D42:D45) | 8% | =C × D |
| **TOTAL** | P1:P44 | — | 100% | **=SUMA(E2:E11)** → IGM |

### Sección 4.2 — Interpretación del IGM

```
Celda B15: IGM = [fórmula =E12 de la tabla anterior]
Celda B16: Nivel = =SI(B15>=4.5,"Optimized",SI(B15>=3.5,"Managed & Measurable",
           SI(B15>=2.5,"Consistently Implemented",SI(B15>=1.5,"Defined","Ad Hoc"))))
Celda B17: Efectivo = =SI(B15>=3.5,"✓ SÍ (≥ umbral FISMA)","✗ NO (< umbral efectividad)")
Celda B18: Brecha hasta L4 = =MAX(0, 3.5 - B15)
Celda B19: Brecha hasta L5 = =MAX(0, 5.0 - B15)
```

### Sección 4.3 — Gráfico Radar por Módulo (instrucciones)

**Tipo de gráfico:** Gráfico de radar (telaraña) con 10 ejes (un eje por módulo).
**Datos:** Puntuaciones medias de cada módulo (columna C de la tabla anterior).
**Líneas:** 
- Línea 1 (azul): Puntuaciones actuales de la organización.
- Línea 2 (roja punteada): Umbral de efectividad FISMA = 3.5 en todos los ejes.
- Línea 3 (verde punteada): Nivel Optimized = 5.0 en todos los ejes.

**Configuración:**
- Escala de cada eje: 0 a 5
- Marcas en: 1, 2, 3, 3.5 (umbral), 4, 5
- Leyenda: "Puntuación Actual | Umbral Efectividad FISMA (L4) | Optimized (L5)"

---

## PESTAÑA 5: ROSI_CALCULO (Cálculo del Retorno sobre la Inversión)

### Sección 5.1 — Inputs de Riesgo Anual

| Celda | Variable | Descripción | Fórmula / Valor |
|---|---|---|---|
| B2 | ARO_ransomware | Probabilidad anual ocurrencia ransomware | [VARIABLE: 0-1; ej: 0.15 = 15% anual] |
| B3 | SLE_ransomware | Impacto económico estimado un incidente ransomware (€) | [VARIABLE: ej: 350.000] |
| B4 | ALE_ransomware_antes | ALE antes de mejoras | =B2 × B3 |
| B5 | ARO_phishing | Probabilidad anual incidente phishing significativo | [VARIABLE: ej: 0.35] |
| B6 | SLE_phishing | Impacto económico estimado (€) | [VARIABLE: ej: 45.000] |
| B7 | ALE_phishing_antes | ALE antes de mejoras | =B5 × B6 |
| B8 | ARO_breach_datos | Probabilidad anual fuga de datos | [VARIABLE: ej: 0.12] |
| B9 | SLE_breach_datos | Impacto (incl. sanciones RGPD, gestión crisis, notificaciones) | [VARIABLE: ej: 250.000] |
| B10 | ALE_breach_antes | ALE antes de mejoras | =B8 × B9 |
| **B11** | **ALE_TOTAL_antes** | **Pérdida esperada anual total (antes de mejoras)** | **=B4+B7+B10** |

### Sección 5.2 — Factores de Reducción de Riesgo por Nivel de Madurez

*Basado en la estimación NIST NICE Framework y ENISA benchmarks: cada incremento de nivel reduce el riesgo residual en ~30-35%.*

| De nivel | A nivel | Factor reducción riesgo estimado |
|---|---|---|
| L1 (Ad Hoc) | L2 (Defined) | 20% |
| L2 | L3 (Consistently Impl.) | 30% |
| L3 | L4 (Managed & Meas.) | 40% |
| L4 | L5 (Optimized) | 20% |
| **L1 → L4 (total)** | | **~65-70%** |

```
Celda B15: IGM_actual = [referencia a IGM_CALCULO!B15]
Celda B16: IGM_objetivo = [VARIABLE: nivel objetivo; por defecto 3.5]
Celda B17: Factor_reduccion = =SI(B15<1.5,0.65,SI(B15<2.5,0.55,SI(B15<3.5,0.40,SI(B15<4.5,0.20,0))))
Celda B18: ALE_TOTAL_despues = =B11 × (1 - B17)
```

### Sección 5.3 — Coste de los Controles e Inversión en Mejoras

| Celda | Variable | Descripción | Fórmula / Valor |
|---|---|---|---|
| B22 | Coste_controles_actuales | Presupuesto ciberseguridad actual (€/año) | =DATOS_ORG!B11 |
| B23 | Inversión_mejora_estimada | Inversión adicional estimada para alcanzar IGM objetivo | [VARIABLE: ej: 180.000] |
| B24 | Coste_total_controles | Coste total año 1 (actuales + mejora) | =B22 + B23 |

### Sección 5.4 — Cálculo ROSI

```
Celda B27: ROSI_año1 = =(ALE_antes - ALE_despues - Inversión_mejora) / Inversión_mejora
           = =(B11 - B18 - B23) / B23
           (Formato: porcentaje; ejemplo típico: 180% - 350%)

Celda B28: Payback_meses = =B23 / ((B11 - B18) / 12)
           (Tiempo en meses para recuperar la inversión)

Celda B29: Ahorro_neto_año1 = =(B11 - B18) - B23

Celda B30: VAN_3años = =VNA(0.08, B29, B29*1.05, B29*1.10) - B23
           (Valor Actual Neto a 3 años con tasa descuento 8% y crecimiento 5-10% anual)
```

### Sección 5.5 — Análisis de Sensibilidad

**Tabla de sensibilidad ROSI (valores de ROSI según variación ARO e IGM_objetivo):**

| ARO total \ IGM objetivo | L3 (2.5) | L4 (3.5) | L5 (5.0) |
|---|---|---|---|
| ARO bajo (10%) | Calcular | Calcular | Calcular |
| ARO medio (25%) | Calcular | **ROSI base** | Calcular |
| ARO alto (50%) | Calcular | Calcular | Calcular |

*Implementación: tabla de datos de Excel (Datos → Análisis hipotético → Tabla de datos) con B2 como variable fila y B16 como variable columna.*

---

## PESTAÑA 6: DASHBOARD (Panel de Visualización)

### Elementos del dashboard (disposición sugerida):

**Fila 1 (KPIs principales):**
- Tarjeta 1: IGM actual (número grande, color semáforo: rojo<2.5, amarillo 2.5-3.5, verde>3.5)
- Tarjeta 2: Nivel de madurez (texto: Ad Hoc / Defined / Cons. Impl. / Managed / Optimized)
- Tarjeta 3: ¿Efectivo? (SÍ/NO con icono)
- Tarjeta 4: ROSI estimado (porcentaje)

**Fila 2 (Gráficos):**
- Gráfico radar 10 ejes: puntuaciones por módulo vs. umbral L4 vs. L5
- Gráfico de barras horizontales: puntuación por módulo (ordenado de menor a mayor)

**Fila 3 (Tablas de acción):**
- Top 3 módulos con menor puntuación (candidatos a mejora prioritaria)
- Estimación de inversión para subir cada módulo deficitario de nivel actual a L4

**Fila 4 (Información de contexto):**
- Benchmarks sectoriales (referencia a pestaña BENCHMARKS)
- Fecha del análisis y datos de la organización

---

## PESTAÑA 7: BENCHMARKS (Datos de Referencia Sectorial)

| Sector | IGM medio estimado España 2025 | % entidades en L4+ | Incidentes/año (media) | Presupuesto cyber/TI medio |
|---|---|---|---|---|
| AAPP Autonómica | 2.8 | 22% | 45 | 6.5% |
| AAPP Local (>20k hab.) | 2.2 | 8% | 18 | 4.2% |
| Sanidad pública | 2.6 | 18% | 62 | 7.1% |
| Educación pública | 2.1 | 9% | 28 | 3.8% |
| Infraestructura crítica | 3.4 | 48% | 89 | 11.3% |
| Empresa privada mediana | 2.5 | 15% | 22 | 8.2% |
| Referencia FISMA (media federal EE.UU. FY2025) | 3.7 | 71% | — | 14.5% |
| Referencia ENISA top quartile EU | 3.6 | 65% | — | 12.0% |

*Nota: Los datos de benchmarks España 2025 son estimaciones basadas en informes INCIBE, CCN-CERT e ENISA NIS Investments 2025. Se actualizarán con los resultados empíricos de la encuesta.*

---

## PESTAÑA 8: POA_M (Plan de Acción y Mejora)

### Estructura de la tabla POA&M (Plan of Action & Milestones):

| Col | Nombre | Tipo | Descripción |
|---|---|---|---|
| A | ID_acción | Texto | POA-001, POA-002… |
| B | Módulo | Lista | Módulo I a X |
| C | Pregunta origen | Texto | P1, P3, P6… |
| D | Deficiencia identificada | Texto | Descripción de la brecha |
| E | Nivel actual | Número 1-5 | [Auto-referencia desde RESPUESTAS] |
| F | Nivel objetivo | Número 1-5 | [VARIABLE] |
| G | Acción de mejora | Texto | Descripción detallada de la acción |
| H | Recursos necesarios (€) | Número | [VARIABLE] |
| I | Responsable | Texto | [VARIABLE] |
| J | Fecha inicio | Fecha | [VARIABLE] |
| K | Fecha fin objetivo | Fecha | [VARIABLE] |
| L | Estado | Lista | En planificación / En curso / Completada / Retrasada |
| M | % Completado | Número 0-100 | [VARIABLE] |
| N | Prioridad calculada | Fórmula | =SI((F-E)*(Ponderación_módulo)>0.4,"Alta","Media/Baja") |
| O | Impacto en IGM estimado | Fórmula | =(F-E)*Ponderación_módulo/100 |

### Fórmula de priorización automática:

```
Columna N (Prioridad) para cada fila i:
=SI(Y(E_i < 3.5, (F_i - E_i) * Ponderacion_modulo >= 0.3), "CRÍTICA",
   SI(Y(E_i < 3.5, (F_i - E_i) * Ponderacion_modulo >= 0.1), "ALTA",
   SI(E_i < 3.5, "MEDIA", "BAJA")))
```

### Resumen ejecutivo POA&M (celdas B2:E10):

```
Total acciones: =CONTARA(A15:A1000)
Acciones críticas: =CONTAR.SI(N15:N1000,"CRÍTICA")
Acciones en curso: =CONTAR.SI(L15:L1000,"En curso")
Inversión total estimada: =SUMA(H15:H1000)
Impacto IGM total estimado: =SUMA(O15:O1000)
IGM proyectado post-POA&M: =[IGM_CALCULO!B15] + SUMA(O15:O1000)
```

---

## INSTRUCCIONES FINALES DE IMPLEMENTACIÓN

### Pasos para crear el fichero Excel desde este documento:

1. **Crear libro nuevo** con 8 pestañas nombradas exactamente como se indica.
2. **Pestaña INICIO**: Insertar texto de bienvenida, instrucciones y tabla de índice con hipervínculos a cada pestaña.
3. **Pestaña DATOS_ORG**: Crear los 13 campos de entrada con validación de datos (listas desplegables donde se indica).
4. **Pestaña RESPUESTAS**: Crear tabla de 60 filas (P1 a P60) con columnas A-E. En columna D, insertar las fórmulas SI anidadas para cada pregunta.
5. **Pestaña IGM_CALCULO**: Crear la tabla de 10 módulos con referencias a PROMEDIO de las celdas correspondientes en RESPUESTAS. Insertar el gráfico radar tras la tabla.
6. **Pestaña ROSI_CALCULO**: Crear las 5 secciones descritas con las fórmulas indicadas. Insertar la tabla de sensibilidad con la función "Tabla de datos" de Excel.
7. **Pestaña DASHBOARD**: Insertar tarjetas KPI con formato condicional de colores (rojo/amarillo/verde). Vincular gráficos a las datos de IGM_CALCULO y ROSI_CALCULO.
8. **Pestaña BENCHMARKS**: Introducir la tabla de datos sectoriales. Añadir columna de referencia visual (iconos ▲▼) para comparación con IGM de la organización.
9. **Pestaña POA_M**: Crear la tabla con validación de datos y fórmulas de priorización automática.
10. **Proteger celdas de fórmulas**: Bloquear celdas con fórmulas; desbloquear sólo las celdas de entrada [VARIABLE].

### Formatos recomendados:

- Escala de color para IGM: Rojo (#FF4444) < 2.5 | Ámbar (#FFAA00) 2.5-3.5 | Verde (#44AA44) > 3.5
- Fuente principal: Calibri o Segoe UI, 11pt
- Cabeceras: fondo azul oscuro (#003366), texto blanco, negrita
- Filas alternas: fondo gris claro (#F5F5F5)

---

*Kit de Encuesta FISMA 2025 — Plantilla IGM y ROSI · Versión 1.0 · Abril 2026*
