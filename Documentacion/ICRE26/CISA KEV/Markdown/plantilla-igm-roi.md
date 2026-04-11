# Plantilla de Excel para cálculo de IGM y ROI

Este documento describe una estructura recomendada de libro Excel para procesar los resultados de la encuesta, calcular el **Índice Global de Madurez (IGM)** y estimar el **ROI** de las iniciativas de mejora.

La idea es que pueda implementarse sin magia negra: solo con fórmulas estándar de Excel.

---

## 1. Estructura general del libro

Se recomiendan, como mínimo, las siguientes hojas:

1. `Diccionario`
2. `Respuestas`
3. `Ponderaciones`
4. `IGM_Organizaciones`
5. `Resumen_Segmentos`
6. `ROI`

---

## 2. Hoja «Diccionario»

Tabla sugerida (una fila por pregunta de la encuesta):

| Columna | Descripción |
|---------|-------------|
| A: ID_Pregunta | Código único (por ejemplo, GOV-01, VUL-03…). |
| B: Bloque | Dimensión a la que pertenece (GOV, VUL, PEN, SIEM, AWR, MET, PERF). |
| C: Texto_Pregunta | Redacción abreviada de la pregunta. |
| D: Tipo | Tipo de respuesta (opción única, múltiple, escala Likert, numérica). |
| E: Escala_Min | Valor numérico mínimo (por ejemplo, 1). |
| F: Escala_Max | Valor numérico máximo (por ejemplo, 4 o 5). |
| G: Sentido | «Directo» (más es mejor) o «Inverso» (más es peor, para invertir la escala). |

Esta hoja sirve como referencia para el resto del libro.

---

## 3. Hoja «Respuestas»

Cada fila representa **una organización** (o una unidad organizativa, si se segmenta así). Cada columna, una variable.

Columnas recomendadas:

| Columna | Contenido |
|---------|-----------|
| A: ID_Organizacion | Identificador único (código interno, nunca datos sensibles). |
| B: Nombre_Organizacion | Opcional, o bien código anonimizado. |
| C: Sector | Código o etiqueta de sector. |
| D: Tamaño | Tramo de tamaño (por ejemplo, Pequeña, Mediana, Grande). |
| E: Ambito | Nacional, internacional, etc. |
| F en adelante | Una columna por cada pregunta (GOV-01, GOV-02, …), con valores numéricos según la codificación definida. |

### 3.1 Codificación de respuestas

- Para preguntas tipo Likert (por ejemplo, de «No existe» a «Totalmente implantado»), asigne valores 1–4 o 1–5.
- Para preguntas con opciones cualitativas, mapéelas a un valor de madurez (por ejemplo, a=1, b=2, c=3, d=4).
- Documente esta codificación en la hoja `Diccionario` o en una pestaña adicional si desea más detalle.

---

## 4. Hoja «Ponderaciones»

Esta hoja define el peso relativo de cada pregunta en el cálculo del IGM y de los subíndices.

Tabla sugerida:

| Columna | Descripción |
|---------|-------------|
| A: ID_Pregunta | Código idéntico al de `Diccionario`. |
| B: Bloque | GOV, VUL, PEN, SIEM, AWR, MET, PERF. |
| C: Peso_Bloque | Peso global del bloque en el IGM (por ejemplo, GOV=0,15; VUL=0,25…). |
| D: Peso_Pregunta | Peso relativo de la pregunta dentro de su bloque (puede normalizarse para que la suma por bloque sea 1). |

### 4.1 Sugerencia de pesos por bloque

A modo orientativo (ajustable según criterio):

- Gobierno y estrategia (GOV): 15 %
- Gestión operativa de vulnerabilidades y KEV (VUL): 25 %
- Pruebas de penetración (PEN): 15 %
- SIEM y monitorización (SIEM): 20 %
- Capacitación y cultura (AWR): 15 %
- Métricas y ROI (MET): 10 %

La suma debe ser 100 %.

---

## 5. Hoja «IGM_Organizaciones»

En esta hoja se calculan los índices de madurez por organización.

Columnas sugeridas:

| Columna | Contenido |
|---------|-----------|
| A: ID_Organizacion | Referencia a `Respuestas!A:A`. |
| B: Sector | Referencia a `Respuestas!C:C`. |
| C: Tamaño | Referencia a `Respuestas!D:D`. |
| D: Ambito | Referencia a `Respuestas!E:E`. |
| E: IGM_GOV | Índice de madurez del bloque Gobierno. |
| F: IGM_VUL | Índice de madurez del bloque Vulnerabilidades/KEV. |
| G: IGM_PEN | Índice de madurez del bloque Pentesting. |
| H: IGM_SIEM | Índice de madurez del bloque SIEM. |
| I: IGM_AWR | Índice de madurez del bloque Capacitación. |
| J: IGM_MET | Índice de madurez del bloque Métricas/ROI. |
| K: IGM_Global | Índice global ponderado. |

### 5.1 Cálculo de subíndices por bloque

Supongamos que en `Respuestas` las columnas GOV-01 a GOV-06 están en las columnas G:L.

Para una organización concreta (fila 2 en `Respuestas` y fila 2 en `IGM_Organizaciones`):

- Cree en `Ponderaciones` un rango con las preguntas GOV y sus `Peso_Pregunta`.
- Use una fórmula tipo `SUMAPRODUCTO`:

```excel
=SUMAPRODUCTO(
  (Ponderaciones!$A$2:$A$7="GOV-01")*(Respuestas!G2),
  Ponderaciones!$D$2:$D$7
)
```

En la práctica, lo más cómodo es definir **rangos nombrados**:

- `Resp_GOV` (todas las celdas de GOV-01..GOV-0X de la organización).
- `Peso_GOV` (pesos de esas preguntas).

Ejemplo de fórmula genérica por bloque:

```excel
=SUMAPRODUCTO(Resp_GOV; Peso_GOV) / SUMA(Peso_GOV)
```

Repita el esquema para VUL, PEN, SIEM, AWR y MET.

### 5.2 Cálculo del IGM global

Si disponemos de los subíndices y de los `Peso_Bloque` en la hoja `Ponderaciones`, se puede usar otra `SUMAPRODUCTO`:

```excel
=SUMAPRODUCTO(
  {IGM_GOV; IGM_VUL; IGM_PEN; IGM_SIEM; IGM_AWR; IGM_MET};
  {Peso_GOV; Peso_VUL; Peso_PEN; Peso_SIEM; Peso_AWR; Peso_MET}
)
```

O, si se prefiere, construir una tabla auxiliar con bloques y pesos y referirse a ella.

---

## 6. Hoja «Resumen_Segmentos»

En esta hoja se generan estadísticas agregadas por sector, tamaño, ámbito, etc.

Elementos recomendados:

- Tabla dinámica con:
  - Filas: Sector, Tamaño, Ambito.
  - Valores: media de IGM_Global, media de IGM_VUL, etc.
- Gráficos derivados:
  - Barras comparando sectores.
  - Gráficos de radar comparando subíndices por segmento.

Esta hoja es la fuente natural de gráficos para el reporte ejecutivo.

---

## 7. Hoja «ROI»

El objetivo de esta hoja es estimar el **retorno de inversión** de iniciativas de mejora derivadas de la encuesta.

### 7.1 Estructura sugerida

| Columna | Contenido |
|---------|-----------|
| A: ID_Iniciativa | Código de iniciativa (por ejemplo, ROI-01, ROI-02…). |
| B: Descripcion | Descripción breve de la iniciativa (por ejemplo, «Automatizar cruce KEV–inventario»). |
| C: Dimension | Bloque principal al que contribuye (GOV, VUL, SIEM, etc.). |
| D: Coste_Anual | Coste estimado anual de la iniciativa (en euros). |
| E: Perdida_Esperada_Actual | Pérdida económica esperada anual actual (antes de la iniciativa). |
| F: Perdida_Esperada_Prevista | Pérdida esperada anual tras la iniciativa. |
| G: Ahorro_Anual | Diferencia (Perdida_Esperada_Actual – Perdida_Esperada_Prevista). |
| H: ROI | Métrica de retorno. |

### 7.2 Fórmulas clave

En G2 (primer registro de iniciativas):

```excel
=E2 - F2
```

En H2 (ROI clásico, expresado como fracción):

```excel
=(G2 - D2) / D2
```

Interpretación:

- Valor positivo: la iniciativa genera ahorro neto frente a su coste.
- Valor negativo: la iniciativa, en las condiciones supuestas, no se justifica económicamente (aunque puede tener otros beneficios cualitativos o regulatorios).

### 7.3 Uso prudente del ROI

- No se incluyen valores numéricos predefinidos: deben estimarse en función del contexto de cada organización.
- Es útil apoyarse en análisis de riesgo (por ejemplo, modelos tipo ALE) para cuantificar las pérdidas esperadas asociadas a incidentes aprovechando vulnerabilidades KEV.

---

## 8. Buenas prácticas de implementación

- Documentar siempre la **versión de la encuesta** y del modelo de ponderaciones usada en el libro.
- Proteger con contraseña las hojas que contengan fórmulas delicadas, para evitar «mejoras» accidentales.
- Mantener una copia de solo lectura como referencia maestra.
- Utilizar nombres de rango para facilitar el mantenimiento (menos referencias A1 que descifrar).

---

Con esta plantilla conceptual, el libro Excel se convierte en un aliado y no en un jefe caprichoso: las matemáticas quedan claras, las ponderaciones son explícitas y los resultados pueden explicarse sin necesidad de invocar a fuerzas sobrenaturales de la hoja de cálculo.
