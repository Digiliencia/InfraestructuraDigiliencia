# Plantilla de Excel para cálculo de IGM y ROI (versión KEV)

Esta plantilla describe la estructura recomendada de un libro Excel para:

- Calcular el **Índice Global de Madurez (IGM)** y los subíndices por dimensión (GOV, VUL, PEN, SIEM, AWR, MET).
- Integrar la lógica GQM+PRAGMATIC.
- Facilitar la estimación del **ROI** de iniciativas de mejora centradas en KEV y gestión de vulnerabilidades.

No contiene macros ni fórmulas exóticas: todo puede hacerse con funciones estándar de Excel (SUMAPRODUCTO, PROMEDIO, SUMA, etc.).

---

## 1. Hojas recomendadas

1. `Diccionario`
2. `Respuestas`
3. `Ponderaciones`
4. `IGM_Organizaciones`
5. `Resumen_Segmentos`
6. `ROI`
7. (Opcional) `PRAGMATIC` – resumen de puntuación PRAGMATIC por métrica.

---

## 2. Hoja «Diccionario»

Contiene el inventario de preguntas de la encuesta.

**Columnas sugeridas:**

| Columna | Contenido |
|---------|-----------|
| A: ID_Pregunta | Código único (PERF-01, GOV-01, VUL-01, etc.). |
| B: Bloque | PERF, GOV, VUL, PEN, SIEM, AWR, MET, IMP. |
| C: Texto_Pregunta | Redacción abreviada para referencia interna. |
| D: Tipo | Opción única, múltiple, Likert, numérica, abierta. |
| E: Escala_Min | Valor mínimo codificado (por ejemplo, 1). |
| F: Escala_Max | Valor máximo codificado (por ejemplo, 4 o 5). |
| G: Sentido | "Directo" (más es mejor) o "Inverso" (más es peor). |

Esta hoja sirve de diccionario de datos para todo el libro.

---

## 3. Hoja «Respuestas»

Cada fila representa una organización/unidad evaluada. Cada columna, una variable.

**Columnas sugeridas:**

| Columna | Contenido |
|---------|-----------|
| A: ID_Organizacion | Identificador pseudonimizado. |
| B: Nombre_Organizacion | Opcional (o código). |
| C: Sector | Etiqueta de sector (alineada con NIS2/ENS). |
| D: Tamano | Tramo (Micro, Pequeña, Mediana, Grande). |
| E: Ambito | Local, nacional, UE, global. |
| F en adelante | Una columna por pregunta (GOV-01, GOV-02, …) con valor numérico ya codificado. |

**Recomendaciones:**

- Mantener una fila por organización.
- Evitar información personal o sensible.
- Asegurar que todas las preguntas obligatorias se han codificado.

---

## 4. Hoja «Ponderaciones»

Define el peso relativo de cada pregunta dentro de su bloque y el peso de cada bloque dentro del IGM.

**Tabla 1 – Ponderación por pregunta**

| Columna | Contenido |
|---------|-----------|
| A: ID_Pregunta | Igual que en `Diccionario`. |
| B: Bloque | GOV, VUL, PEN, SIEM, AWR, MET. |
| C: Peso_Pregunta | Peso relativo dentro del bloque (la suma por bloque = 1). |

**Tabla 2 – Ponderación por bloque**

| Bloque | Peso_Bloque sugerido |
|--------|----------------------|
| GOV | 0,15 |
| VUL | 0,25 |
| PEN | 0,15 |
| SIEM | 0,20 |
| AWR | 0,15 |
| MET | 0,10 |

Ajustable según prioridades; documentar cualquier cambio.

---

## 5. Hoja «IGM_Organizaciones»

Aquí se calculan subíndices por bloque y el IGM global.

**Columnas sugeridas:**

| Columna | Contenido |
|---------|-----------|
| A: ID_Organizacion | Referencia a `Respuestas!A:A`. |
| B: Sector | =`Respuestas!C:C`. |
| C: Tamano | =`Respuestas!D:D`. |
| D: Ambito | =`Respuestas!E:E`. |
| E: IGM_GOV | Subíndice Gobierno. |
| F: IGM_VUL | Subíndice Vulnerabilidades/KEV. |
| G: IGM_PEN | Subíndice Pentesting. |
| H: IGM_SIEM | Subíndice SIEM/monitorización. |
| I: IGM_AWR | Subíndice Capacitación. |
| J: IGM_MET | Subíndice Métricas/ROI. |
| K: IGM_Global | Índice Global de Madurez. |

### 5.1 Cálculo de subíndices

Ejemplo (bloque GOV):

1. Definir un rango nombrado `Peso_GOV` en `Ponderaciones` con los pesos de las preguntas GOV.
2. Definir un rango `Resp_GOV_orgX` (fila de respuestas GOV para una organización).

Fórmula tipo (para una organización en fila 2):

```excel
=SUMAPRODUCTO(Resp_GOV_org2; Peso_GOV) / SUMA(Peso_GOV)
```

Puede replicarse por bloque (VUL, PEN, SIEM, AWR, MET) cambiando los rangos.

### 5.2 Normalización a escala 0–100

Si la escala de las respuestas es, por ejemplo, 1–4:

```excel
= (Subindice_Bruto - 1) / (4 - 1) * 100
```

De este modo, todos los bloques quedan en una escala común (0–100).

### 5.3 Cálculo del IGM Global

Suponiendo que los pesos de bloque están en una pequeña tabla auxiliar o en celdas nombradas (`Peso_GOV`, `Peso_VUL`, etc.), se puede usar:

```excel
= IGM_GOV * Peso_GOV
+ IGM_VUL * Peso_VUL
+ IGM_PEN * Peso_PEN
+ IGM_SIEM * Peso_SIEM
+ IGM_AWR * Peso_AWR
+ IGM_MET * Peso_MET
```

O, de forma compacta, con `SUMAPRODUCTO` sobre un rango que contenga los subíndices y otro con los pesos.

---

## 6. Hoja «Resumen_Segmentos»

Usada para análisis agregados y gráficos.

Elementos recomendados:

- Tablas dinámicas:
  - Filas: Sector, Tamaño, Ámbito.
  - Valores: PROMEDIO de IGM_Global, IGM_VUL, IGM_SIEM, etc.
- Gráficos:
  - Barras comparando sectores.
  - Radar comparando subíndices por segmento.

Esta hoja es la fuente natural de material para el reporte ejecutivo.

---

## 7. Hoja «ROI»

Permite estimar el retorno de iniciativas de mejora identificadas a partir de los resultados (por ejemplo, «automatizar correlación KEV–activos», «reforzar SOC 24x7», etc.).

**Columnas sugeridas:**

| Columna | Contenido |
|---------|-----------|
| A: ID_Iniciativa | Código (ROI-01, ROI-02…). |
| B: Descripcion | Descripción resumida. |
| C: Dimension | GOV, VUL, PEN, SIEM, AWR, MET (bloque al que contribuye). |
| D: Coste_Anual | Coste estimado anual (en euros). |
| E: Perdida_Esperada_Actual | Pérdida económica anual esperada antes de la iniciativa. |
| F: Perdida_Esperada_Prevista | Pérdida esperada tras la iniciativa. |
| G: Ahorro_Anual | =E – F. |
| H: ROI | = (G - D) / D. |

**Interpretación:**

- ROI > 0: la iniciativa se justifica económicamente (ahorro superior al coste).
- ROI ≈ 0: decisión de gestión (puede primar cumplimiento/regulación). |
- ROI < 0: iniciativa discutible salvo motivos regulatorios o reputacionales fuertes.

---

## 8. Hoja opcional «PRAGMATIC»

Si se desea reflejar también la evaluación PRAGMATIC de las métricas KEV a nivel de país:

| Métrica | P | R | A | G | M | P2 | O | I | C | Total |
|--------|---|---|---|---|---|----|---|---|---|-------|
| E1 | … | … | … | … | … | … | … | … | … | … |
| R1 | … | … | … | … | … | … | … | … | … | … |
| etc. |   |   |   |   |   |    |   |   |   |   |

No interviene en el cálculo del IGM, pero documenta la «calidad intrínseca» de las métricas de exposición/respuesta/impacto.

---

## 9. Buenas prácticas generales

- Proteger las hojas con fórmulas críticas (especialmente `Ponderaciones`, `IGM_Organizaciones` y `ROI`).
- Documentar versión y fecha del modelo en una celda visible (por ejemplo, en `Diccionario`).
- Usar rangos con nombre para reducir errores al modificar el libro.
- Mantener una copia «maestra» solo lectura y trabajar sobre copias para cada oleada de encuestas.

Con esta plantilla, el Excel deja de ser un ente caprichoso y se convierte en un aliado: los números tendrán sentido, las comparaciones serán coherentes y, lo más importante, cualquier persona razonablemente familiarizada con hojas de cálculo podrá seguir la lógica sin necesidad de invocar espíritus de la auditoría.
