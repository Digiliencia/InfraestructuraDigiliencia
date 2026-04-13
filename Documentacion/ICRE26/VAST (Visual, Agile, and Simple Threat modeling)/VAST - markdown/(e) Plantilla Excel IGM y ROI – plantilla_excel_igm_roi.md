# Plantilla de Excel para Cálculo de IGM y ROI

> Este documento describe cómo estructurar un libro de Excel para calcular el Índice Global de Madurez (IGM) y el ROI de ciberseguridad a partir de las respuestas a la encuesta.

---

## 1. Estructura del libro de Excel

Se recomienda un libro con, al menos, las siguientes hojas:

1. `Respuestas`
2. `Puntuaciones`
3. `IGM`
4. `ROI`
5. `Parametros`

---

## 2. Hoja `Respuestas`

Columnas sugeridas (por filas, una organización):

- `ID_Org` – Identificador anónimo de la organización.
- `Sector`
- `Tamano`
- `Tipo_Org`
- `Rol_Respuesta`

Y columnas para cada pregunta cerrada:

- `P1`, `P2`, ..., `P36` (P37 es comentario abierto y puede ir en una columna de texto aparte).

Las respuestas pueden codificarse como:

- Para opciones únicas: códigos numéricos (1, 2, 3, 4, 5).
- Para opciones múltiples: listas separadas por comas o columnas auxiliares (por ejemplo, `P3_ISO27001 = 1/0`).

---

## 3. Hoja `Puntuaciones`

Objetivo: traducir respuestas a puntos por pregunta.

### 3.1. Tabla de puntuación por pregunta

Ejemplo (solo para algunas preguntas):

- Columnas:
  - `Pregunta`
  - `Codigo_Respuesta`
  - `Descripcion`
  - `Puntos`

Ejemplo de filas:

- `P1`, `1`, `Aprobada y revisión anual`, `4`
- `P1`, `2`, `Aprobada sin revisión`, `3`
- `P1`, `3`, `Borrador informal`, `2`
- `P1`, `4`, `No existe`, `0`

Para cada pregunta se define una tabla similar.

### 3.2. Funciones de búsqueda

En la hoja `Respuestas`, para cada `P1`, `P2`, etc., se puede crear columnas auxiliares:

- `P1_Puntos`, `P2_Puntos`, etc.

Usando fórmulas tipo:

- `=BUSCARV(P1;Tabla_P1;Col_Puntos;FALSO)`

O bien, si se usa una tabla única:

- `=INDICE(Puntuaciones!$D:$D;COINCIDIR(1;(Puntuaciones!$A:$A="P1")*(Puntuaciones!$B:$B=P1);0))`

(ajustando rangos y usando fórmulas matriciales o funciones modernas como `XLOOKUP`).

---

## 4. Hoja `IGM`

### 4.1. Asignación de preguntas a bloques

En la hoja `Parametros`, definir:

- Bloque `GOV`: P1, P2, P3, P4.
- Bloque `INV`: P5, P6, P7, P8.
- Bloque `THR`: P9, P10, P11, P12, P13, P14, P15.
- Bloque `MET`: P16, P17, P18, P19, P20.
- Bloque `VUL`: P21, P22, P23, P24, P25.
- Bloque `RES`: P26, P27, P28, P29.
- Bloque `TAL`: P30, P31, P32, P33.
- (P34, P35, P36 pueden utilizarse para análisis cualitativo o ponderaciones de prioridades, si se desea incorporarlas).

### 4.2. Cálculo de puntuación por bloque

En `IGM`, por organización:

- Columnas:
  - `ID_Org`
  - `GOV_Puntos`
  - `INV_Puntos`
  - `THR_Puntos`
  - `MET_Puntos`
  - `VUL_Puntos`
  - `RES_Puntos`
  - `TAL_Puntos`
  - `IGM`

Ejemplo de fórmula para `GOV_Puntos`:

- `=SUMA(Respuestas!P1_Puntos;Respuestas!P2_Puntos;Respuestas!P3_Puntos;Respuestas!P4_Puntos)`

Para normalizar:

- `GOV_Normalizado = GOV_Puntos / GOV_Maximo * 100`

Donde `GOV_Maximo` es la suma de las puntuaciones máximas de P1–P4 (definida en `Parametros`).

### 4.3. Cálculo del IGM

Suponiendo pesos en `Parametros`:

- `w_GOV`, `w_INV`, `w_THR`, `w_MET`, `w_VUL`, `w_RES`, `w_TAL`.

Fórmula:

- `IGM = w_GOV*GOV_Normalizado + w_INV*INV_Normalizado + ... + w_THR*THR_Normalizado + ...`

Los pesos deben sumar 1 (o 100 %).

---

## 5. Hoja `ROI`

### 5.1. Datos requeridos

Añadir en `Respuestas` o en una hoja especial:

- `Coste_Tecnologias` (anual).
- `Coste_Personal_Ciber`.
- `Coste_Servicios_Externos`.
- `Coste_Formacion`.
- `Perdidas_Incidentes_Pre` (estimadas antes de inversiones).
- `Perdidas_Incidentes_Post` (estimadas después).
- `Multas_Sanciones_Evitadas` (estimación).
- `Otros_Beneficios` (por ejemplo, reducción de interrupciones).

### 5.2. Cálculo

En `ROI`, por organización:

- `Coste_Total = Coste_Tecnologias + Coste_Personal_Ciber + Coste_Servicios_Externos + Coste_Formacion`
- `Beneficio_Estimado = (Perdidas_Incidentes_Pre – Perdidas_Incidentes_Post) + Multas_Sanciones_Evitadas + Otros_Beneficios`
- `ROI = (Beneficio_Estimado – Coste_Total) / Coste_Total`

Formato como porcentaje.

### 5.3. Relación con el IGM

Se puede crear una tabla o gráfico que muestre:

- `IGM` (eje X)
- `ROI` (eje Y)

Para analizar tendencias: por ejemplo, si a partir de cierto nivel de madurez los retornos marginales disminuyen, o si existe una “zona óptima”.

---

## 6. Hoja `Parametros`

Sugerencias:

- Tabla con:
  - Pregunta, Puntuación máxima, Bloque, Peso relativo.
- Tabla con:
  - Bloque, Peso en IGM (por ejemplo, GOV 0,15; THR 0,20; etc.).
- Opcional:
  - Valores de referencia por sector (para análisis de desviación).

---

## 7. Visualizaciones recomendadas

- Gráfico de radar (o araña) por bloques de madurez.
- Histogramas de IGM por sector.
- Gráficos de dispersión IGM vs. ROI.
- Boxplots de IGM por tamaño de organización.

Todo ello para hacer que las conclusiones sean tan visibles que hasta el último escéptico en la sala de dirección vea las diferencias.
