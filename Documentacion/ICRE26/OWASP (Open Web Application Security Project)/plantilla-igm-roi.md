# Plantilla de Excel para cálculo de IGM y ROI – Descripción técnica

> Este documento describe cómo implementar en Excel (o equivalente) una hoja de cálculo para calcular el Índice Global de Madurez (IGM) y una estimación de ROI de seguridad a partir de las respuestas de la encuesta OWASP 2025 – España.

---

## 1. Estructura general del libro de Excel

Se recomienda un libro con, al menos, las siguientes hojas:

1. `Datos_brutos` – Respuestas codificadas de la encuesta.
2. `Codificacion` – Tablas con la codificación de opciones de respuesta a valores numéricos (0–100, etc.).
3. `IGM_Organizacion` – Cálculo del IGM y subíndices por organización.
4. `ROI` – Cálculo del ROI de seguridad.
5. `Parametros` – Parámetros globales (ponderaciones, umbrales, costes, etc.).

---

## 2. Hoja `Datos_brutos`

### 2.1. Columnas mínimas

- Columna A: `ID_Organizacion` (identificador anonimizado).
- Columna B: `Sector` (texto o código).
- Columna C: `Tamano` (categoría de tamaño).
- Columnas posteriores: una columna por pregunta de la encuesta, con el valor de la opción elegida.

Ejemplo de cabeceras a partir de la columna D:

- `P2_1`, `P2_2`, …, `P3_1`, `P3_2`, …, `P9_3`.

### 2.2. Formato de valores

- Se recomienda almacenar el **código numérico** asociado a cada respuesta (por ejemplo, 0,1,2,3,4) según la tabla de la hoja `Codificacion`.
- Para preguntas de respuesta múltiple, se pueden usar varias columnas (por ejemplo, `P6_2_A`, `P6_2_B`, etc.) con valores binarios (0/1).

---

## 3. Hoja `Codificacion`

Esta hoja define cómo se traduce cada opción en un valor numérico y, en su caso, en un valor normalizado 0–100.

### 3.1. Ejemplo de tabla de codificación para preguntas de porcentaje

| Pregunta | Opcion_texto | Codigo | Valor_0_100 |
|----------|--------------|--------|-------------|
| P3_5 | 0–7 días | 4 | 100 |
| P3_5 | 8–30 días | 3 | 75 |
| P3_5 | 31–90 días | 2 | 50 |
| P3_5 | >90 días | 1 | 25 |
| P3_5 | No se mide | 0 | 0 |

### 3.2. Ejemplo de codificación para niveles ASVS

| Pregunta | Opcion_texto | Codigo | Valor_0_100 |
|----------|--------------|--------|-------------|
| P5_3 | 76–100 % apps críticas Nivel 2 | 4 | 100 |
| P5_3 | 51–75 % | 3 | 75 |
| P5_3 | 26–50 % | 2 | 50 |
| P5_3 | 0–25 % | 1 | 25 |
| P5_3 | No se sabe | 0 | 0 |

### 3.3. Uso de funciones

Se pueden utilizar funciones como `BUSCARV` (`VLOOKUP`) o `INDICE`/`COINCIDIR` para obtener el `Valor_0_100` correspondiente a cada respuesta.

---

## 4. Hoja `IGM_Organizacion`

### 4.1. Columnas base

- Columna A: `ID_Organizacion`.
- Columnas B–E: subíndices 0–100:
  - `IGM_Exposicion_OWASP`.
  - `IGM_SAMM`.
  - `IGM_ASVS`.
  - `IGM_Gobernanza_Cultura`.
- Columna F: `IGM_Global` (0–100).

### 4.2. Cálculo de subíndices

Para cada subíndice, se definen las preguntas relevantes y se calcula la media de sus valores normalizados.

Ejemplo para `IGM_Exposicion_OWASP` (bloque 3):

1. En `Parametros`, definir un rango con las preguntas que alimentan este subíndice, por ejemplo `P3_2`, `P3_3`, `P3_4`, `P3_5`, `P3_6`.
2. En `IGM_Organizacion`, para una fila dada (organización):
   - Recuperar de `Datos_brutos` los códigos de respuesta.
   - Traducir a valores 0–100 mediante `BUSCARV` en `Codificacion`.
   - Calcular la media de esos valores.

Ejemplo de fórmula (simplificada) para una organización en fila 2:

```text
=PROMEDIO(
  BUSCARV(Datos_brutos!D2;Codificacion!$A$2:$D$100;4;FALSO);
  BUSCARV(Datos_brutos!E2;Codificacion!$A$2:$D$100;4;FALSO);
  …
)
```

El mismo enfoque se repite para los otros subíndices, cambiando las preguntas incluidas.

### 4.3. Cálculo del IGM global

En la columna `IGM_Global`, para la fila 2:

- Si se desea una media simple:

```text
=PROMEDIO(B2:E2)
```

- Si se desea una media ponderada (con pesos definidos en `Parametros`, por ejemplo en celdas `Parametros!B2:E2`):

```text
=SUMAPRODUCTO(B2:E2;Parametros!B2:E2)/SUMA(Parametros!B2:E2)
```

---

## 5. Hoja `ROI`

### 5.1. Columnas sugeridas

- Columna A: `ID_Organizacion`.
- Columna B: `IGM_Global_Antes` (si se dispone de mediciones históricas).
- Columna C: `IGM_Global_Despues`.
- Columna D: `Delta_IGM` (C – B).
- Columna E: `Coste_Seguridad` (inversiones y costes operativos en el periodo).
- Columna F: `Riesgo_Estimado_Antes` (en euros, basado en modelo propio de la organización).
- Columna G: `Riesgo_Estimado_Despues`.
- Columna H: `Riesgo_Evitado` (F – G).
- Columna I: `ROI_Seguridad`.

### 5.2. Fórmulas clave

- `Delta_IGM` (celda D2):

```text
=C2-B2
```

- `Riesgo_Evitado` (celda H2):

```text
=F2-G2
```

- `ROI_Seguridad` (celda I2):

```text
=SI(E2>0;(H2-E2)/E2;"")
```

> Nota: el cálculo de `Riesgo_Estimado_Antes` y `Riesgo_Estimado_Despues` depende del modelo de la organización (por ejemplo, probabilidad estimada de incidentes x impacto medio). La plantilla deja estos campos para que cada entidad introduzca sus valores.

---

## 6. Hoja `Parametros`

### 6.1. Ponderaciones de subíndices

Ejemplo de tabla:

| Subindice | Peso |
|-----------|------|
| IGM_Exposicion_OWASP | 0,25 |
| IGM_SAMM | 0,25 |
| IGM_ASVS | 0,25 |
| IGM_Gobernanza_Cultura | 0,25 |

Estos valores pueden ajustarse según sector o prioridades.

### 6.2. Umbrales de interpretación del IGM

Ejemplo:

- 0–24 → "Crítico".
- 25–49 → "Bajo".
- 50–74 → "Medio".
- 75–100 → "Alto".

Estos umbrales pueden utilizarse en gráficos de semáforo o dashboards.

---

## 7. Visualizaciones recomendadas

Aunque no forman parte estricta de la plantilla, se recomiendan los siguientes gráficos en Excel o herramientas de BI:

- Barras apiladas de distribución de IGM por sector.
- Boxplots de subíndices para comparar sectores.
- Líneas de tendencia del IGM para organizaciones con series temporales (varios años).
- Diagramas de dispersión IGM vs coste de seguridad, o IGM vs incidentes.

---

## 8. Buenas prácticas de implementación

- Proteger las hojas con fórmulas para evitar cambios accidentales.
- Separar claramente datos de entrada (respuestas de la encuesta) y resultados (IGM, ROI).
- Documentar en comentarios o en una hoja adicional cualquier adaptación sectorial o cambio en ponderaciones.

Esta plantilla pretende ser lo suficientemente concreta como para implementarse sin dolor excesivo, pero lo bastante flexible como para dar cabida a las manías legítimas de cada equipo de riesgos y de cada Excel ninja de la organización.
