# Plantilla de Excel para cálculo de IGM y ROI

> Descripción conceptual de una hoja Excel lista para implementar a partir de las respuestas de la encuesta.[web:29][web:44][web:46]

---

## 1. Estructura general de la hoja

Se recomienda un libro Excel con las siguientes pestañas:

1. `Encuesta` – Registro de respuestas por organización.  
2. `Ponderaciones` – Pesos de dominios y preguntas.  
3. `Cálculos_IGM` – Cálculo del Índice Global de Madurez y subíndices.  
4. `Cálculos_ROI` – Estimaciones de ROI en ciberseguridad.  
5. `Resultados` – Cuadros de mando y resúmenes.

---

## 2. Hoja “Encuesta”

Columnas sugeridas:

- `ID_Org`  
- `Nombre_Org`  
- `Sector`  
- `Tamaño`  
- `Ámbito`  
- `P1_1_1`, `P1_1_2`, … hasta `P8_3`  

Cada columna de pregunta almacena un **valor numérico codificado** según las escalas definidas en la guía metodológica (por ejemplo, de 0 a 4, 0 a 5, etc.).

---

## 3. Hoja “Ponderaciones”

Columnas:

- `Dominio` (Gobierno, Riesgo, Seguridad, Cambios, Servicios, Continuidad, Monitorización)  
- `Peso_Dominio` (por defecto, todos = 1 o pesos ajustados según criticidad)  
- `Pregunta` (ej. P1_1_1)  
- `Peso_Pregunta` (peso relativo de la pregunta dentro del dominio)  
- `Máx_Puntuación_Pregunta` (valor máximo posible en la escala codificada)

Esto permite ajustar la influencia relativa de cada pregunta y dominio en el IGM.

---

## 4. Hoja “Cálculos_IGM”

### 4.1. Cálculo de puntuación por pregunta normalizada

Para cada organización (fila) y pregunta (columna), se puede calcular:

- `Punt_Pregunta_Norm = Valor_Respuesta / Máx_Puntuación_Pregunta`

### 4.2. Puntuación por dominio

Para cada dominio \(d\):

\[
M_d = \frac{\sum (Punt\_Pregunta\_Norm \cdot Peso\_Pregunta)}{\sum Peso\_Pregunta} \times 5
\]

Es decir, una media ponderada de puntuaciones normalizadas escalada a 0‑5.

### 4.3. Índice Global de Madurez (IGM)

Para cada organización:

\[
IGM = \frac{\sum (M_d \cdot Peso\_Dominio)}{\sum Peso\_Dominio}
\]

El resultado puede representarse en escala 0‑5 o 0‑100 (multiplicando por 20).

---

## 5. Hoja “Cálculos_ROI”

Aunque la encuesta no es un registro financiero, permite estimar un ROI aproximado modelando:

- `Incidentes_Graves_Antes`  
- `Incidentes_Graves_Después`  
- `Coste_Medio_Incidente`  
- `Coste_Iniciativas_Seguridad` (acumulado)  
- `Reducción_Tiempo_Parada` (en horas)  
- `Coste_Hora_Negocio`  

Ejemplo de fórmula de beneficios estimados:

\[
Beneficio\_Incidentes = (Incidentes\_Graves\_Antes - Incidentes\_Graves\_Después) \times Coste\_Medio\_Incidente
\]

\[
Beneficio\_Continuidad = Reducción\_Tiempo\_Parada \times Coste\_Hora\_Negocio
\]

\[
Beneficio\_Total = Beneficio\_Incidentes + Beneficio\_Continuidad
\]

\[
ROI = \frac{Beneficio\_Total}{Coste\_Iniciativas\_Seguridad}
\]

Las variables pueden alimentarse de datos internos o de estimaciones complementarias, no solo de la encuesta. La encuesta ayuda a **explicar** el porqué de una mejora (por ejemplo, mejor SOC, mejor continuidad, mejor gestión de riesgos).

---

## 6. Hoja “Resultados”

Se recomiendan:

- Gráficos radar con los valores de \(M_d\) por dominio.  
- Histogramas del IGM por sector.  
- Tablas de organización con: IGM, M_d por dominio, valor de ROI (si se dispone de datos).

Esto permite elaborar informes ejecutivos de forma rápida y visual.