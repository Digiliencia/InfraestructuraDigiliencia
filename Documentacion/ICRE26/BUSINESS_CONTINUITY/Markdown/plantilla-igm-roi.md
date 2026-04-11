# Plantilla de Excel para cálculo de IGM y ROI

Este documento describe cómo construir, en Excel (o herramienta similar), una plantilla para:

- Calcular un **Índice Global de Madurez (IGM)** y **Índices de Madurez por Dominio (IMD)** a partir de las respuestas de la encuesta.
- Estimar de forma sencilla el **ROI (retorno de la inversión)** de iniciativas de mejora en ciberseguridad, continuidad de negocio y ciber‑resiliencia.

---

## 1. Estructura general del libro de Excel

Se recomiendan al menos las siguientes hojas:

1. `Diccionario_Preguntas`
2. `Datos_Respuestas`
3. `Calculos_Madurez`
4. `ROI_Costes_Beneficios`
5. `Cuadro_Mando`

Puedes añadir más hojas (por ejemplo, detalle por año o por unidad organizativa) según tus necesidades.

---

## 2. Hoja «Diccionario_Preguntas»

Contiene la definición de todas las preguntas de la encuesta y los parámetros necesarios para el cálculo de índices.

Columnas sugeridas:

- `Codigo_Pregunta`: por ejemplo, GOV-01, BCM-03, etc.
- `Dominio`: GOV, RISK, VULN, PENT, SIEM, BCM, DRP, AWARE, MET, ROI, SUP, ECO, ORG.
- `Subdominio` (opcional): gobierno, estrategia, análisis de riesgos, etc.
- `Texto_Pregunta`: enunciado resumido de la pregunta.
- `Tipo_Respuesta`: por ejemplo, Likert_4, Likert_5, Seleccion_Unica, Seleccion_Multiple.
- `Valor_Min`: valor numérico mínimo de la escala (por ejemplo, 0).
- `Valor_Max`: valor numérico máximo (por ejemplo, 3 para una escala de 4 niveles: a–d).
- `Peso_Dominio`: peso relativo de la pregunta dentro de su dominio (por ejemplo, 1 por defecto).
- `Peso_IGM`: peso relativo de la pregunta dentro del índice global (por defecto, igual a `Peso_Dominio`, pero puede afinarse).

Ejemplo de fila:

| Codigo_Pregunta | Dominio | Subdominio | Texto_Pregunta | Tipo_Respuesta | Valor_Min | Valor_Max | Peso_Dominio | Peso_IGM |
|---|---|---|---|---|---|---|---|---|
| BCM-03 | BCM | RTO_RPO | Definición de objetivos de recuperación | Likert_4 | 0 | 3 | 1 | 1 |

---

## 3. Hoja «Datos_Respuestas»

Registra las respuestas de cada organización (o unidad) a cada pregunta.

Columnas sugeridas:

- `ID_Org`: identificador de la organización (código anónimo si se quiere comparativa).
- `Nombre_Org` (opcional si se requiere anonimato).
- `Sector`: por ejemplo, salud, energía, administración pública, financiero, industria, etc.
- `Pais_Region`: por ejemplo, ES‑Nacional, ES‑CCAA, UE, etc.
- `Codigo_Pregunta`.
- `Respuesta_Codificada`: valor numérico correspondiente a la opción elegida.
- `Fecha_Encuesta`.

Ejemplo de filas:

| ID_Org | Nombre_Org | Sector | Pais_Region | Codigo_Pregunta | Respuesta_Codificada | Fecha_Encuesta |
|---|---|---|---|---|---|---|
| ORG001 | Org Salud Norte | Salud | ES‑CCAA | BCM-03 | 2 | 2026‑03‑15 |
| ORG001 | Org Salud Norte | Salud | ES‑CCAA | GOV-01 | 3 | 2026‑03‑15 |

Se recomienda usar **validación de datos** para limitar las respuestas numéricas al rango permitido (`Valor_Min` – `Valor_Max`).

---

## 4. Cálculo de índices de madurez

### 4.1. Hoja «Calculos_Madurez»

Esta hoja calculará:

- Índices de Madurez por Dominio (IMD) para cada organización.
- Índice Global de Madurez (IGM) para cada organización.

Estructura sugerida:

- Fila de encabezados:
  - `ID_Org`
  - `Nombre_Org`
  - `Sector`
  - `Pais_Region`
  - `IMD_GOV`, `IMD_RISK`, `IMD_VULN`, `IMD_PENT`, `IMD_SIEM`, `IMD_BCM`, `IMD_DRP`, `IMD_AWARE`, `IMD_MET`, `IMD_ROI`, `IMD_SUP`, `IMD_ECO`
  - `IGM_Global`

#### 4.1.1. Cálculo de IMD por dominio

Para un dominio dado (por ejemplo, BCM), el IMD puede calcularse como **media ponderada** de las respuestas numéricas asociadas a las preguntas de ese dominio.

Supongamos:

- `Datos_Respuestas` está en una tabla estructurada llamada `tblRespuestas`.
- `Diccionario_Preguntas` está en una tabla llamada `tblPreguntas`.

Para calcular el IMD_BCM de la organización en la celda, por ejemplo, `E2`:

1. En una columna auxiliar (opcional) de `tblRespuestas`, puedes traer el `Dominio` usando `BUSCARV` o `XLOOKUP`.
2. En `Calculos_Madurez!E2` (IMD_BCM), podrías usar algo como (en Excel moderno con `SUMAR.SI.CONJUNTO`):

   `=SUMAR.SI.CONJUNTO(tblRespuestas[Respuesta_Codificada], tblRespuestas[ID_Org], $A2, tblRespuestas[Dominio], "BCM") / CONTAR.SI.CONJUNTO(tblRespuestas[ID_Org], $A2, tblRespuestas[Dominio], "BCM")`

Si usas pesos por pregunta (`Peso_Dominio`), la fórmula sería un `SUMAPRODUCTO`:

- Añade a `tblRespuestas` una columna `Peso_Dominio` con un `BUSCARV` a `tblPreguntas`.
- Fórmula tipo:

  `=SUMAPRODUCTO((tblRespuestas[ID_Org]=$A2)*(tblRespuestas[Dominio]="BCM")*tblRespuestas[Respuesta_Codificada]*tblRespuestas[Peso_Dominio]) / SUMAPRODUCTO((tblRespuestas[ID_Org]=$A2)*(tblRespuestas[Dominio]="BCM")*tblRespuestas[Peso_Dominio])`

#### 4.1.2. Cálculo del IGM Global

El IGM puede definirse como una media ponderada de los IMD o directamente de todas las respuestas considerando `Peso_IGM`.

**Opción A – media de dominios:**

`=PROMEDIO(E2:P2)`  
(suponiendo que `E2:P2` contienen los IMD de todos los dominios para la organización)

**Opción B – media ponderada directa por pregunta (más precisa):**

En una celda de `Calculos_Madurez` para cada organización (por ejemplo, `Q2`):

`=SUMAPRODUCTO((tblRespuestas[ID_Org]=$A2)*tblRespuestas[Respuesta_Codificada]*tblRespuestas[Peso_IGM]) / SUMAPRODUCTO((tblRespuestas[ID_Org]=$A2)*tblRespuestas[Peso_IGM])`

Valores típicos de IGM tras normalizar a 0–3 pueden expresarse en 0–100 mediante:

`IGM_Normalizado = IGM * (100 / Valor_Max)`  
(por ejemplo, `=*celda_IGM*100/3` para escala 0–3).

---

## 5. Modelado de ROI en la hoja «ROI_Costes_Beneficios»

La idea es disponer de una hoja sencilla para comparar:

- Costes de iniciativas de mejora (inversiones, OPEX adicional).
- Beneficios esperados (pérdidas evitadas, reducción de downtime, mejora de IGM).

### 5.1. Estructura recomendada

Columnas sugeridas:

- `ID_Iniciativa`.
- `Nombre_Iniciativa`.
- `Dominio_Principal` (BCM, SIEM, VULN, etc.).
- `Descripcion_Breve`.
- `Coste_Anual` (moneda local).
- `Coste_Inicial` (si aplica, CAPEX).
- `Horizonte_Anios`.
- `Perdida_Anual_Estimada_Sin_Iniciativa` (pérdida económica media esperada sin implantar la mejora).
- `Reduccion_%_Perdida` (porcentaje de reducción de dicha pérdida esperada gracias a la iniciativa).
- `Beneficio_Anual_Estimado` (campo calculado).
- `ROI_Total` (campo calculado).

### 5.2. Fórmulas básicas

- `Beneficio_Anual_Estimado`:

  `=Perdida_Anual_Estimada_Sin_Iniciativa * Reduccion_%_Perdida`

- `Coste_Total` (en una columna auxiliar):

  `=Coste_Inicial + Coste_Anual * Horizonte_Anios`

- `Beneficio_Total`:  

  `=Beneficio_Anual_Estimado * Horizonte_Anios`

- `ROI_Total`:

  `=(Beneficio_Total - Coste_Total) / Coste_Total`

Puedes expresar el ROI en porcentaje formateando la celda como `%`.

### 5.3. Relación con los índices de madurez

Opcionalmente, se puede añadir una columna:

- `Incremento_Esperado_IMD` (por ejemplo, +0,3 en IMD_BCM).

Y usar esta información para priorizar iniciativas no sólo por ROI económico, sino también por **impacto en madurez**.

---

## 6. Hoja «Cuadro_Mando»

Esta hoja es la cara amable del modelo: gráficos y tablas resumidas para consumo ejecutivo.

Elementos recomendados:

1. **Tabla resumen por organización**:
   - ID_Org, Nombre_Org, Sector, IGM_Global y principales IMD.

2. **Gráficos de radar** (uno por organización o comparativos) mostrando IMD por dominio.

3. **Gráficos de barras** comparando:
   - IGM por sector.
   - IMD por dominio entre organizaciones.

4. **Semáforos de madurez**:
   - Definir umbrales (por ejemplo, 0–1 rojo, 1–2 ámbar, 2–3 verde) y usar formato condicional para colorear celdas.

5. **Listado de iniciativas priorizadas** (tomadas de `ROI_Costes_Beneficios`) ordenadas por ROI, impacto en madurez o riesgo cubierto.

---

## 7. Consejos prácticos

- Empieza simple: escala de 0–3, pesos iguales y unas pocas iniciativas en la hoja de ROI. Podrás sofisticar el modelo más adelante.
- Documenta en comentarios de celda las asunciones utilizadas (por ejemplo, cómo se ha estimado la pérdida anual esperada).
- Revisa de forma conjunta las salidas del modelo con los responsables de riesgos, ciberseguridad y finanzas para validar que los resultados «cuadran con la realidad».

---

Con esta plantilla tendrás una base sólida para **cuantificar la madurez** (IGM/IMD) y **conectar las decisiones de inversión con su retorno esperado**, tanto en términos económicos como de resiliencia.
