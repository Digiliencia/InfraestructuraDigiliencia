# Plantilla de Excel para cálculo de IGM y ROI (GQM + PRAGMATIC)

> Versión orientada a implementar el modelo de indicadores COBIT integrados con GQM y PRAGMATIC.[web:29][web:24][web:61]

---

## 1. Estructura del libro Excel

Se recomiendan las siguientes hojas:

1. `Encuesta` – Respuestas codificadas de la encuesta COBIT.  
2. `Métricas` – Definición de métricas (GQM) y codificación.  
3. `PRAGMATIC` – Matriz de evaluación PRAGMATIC y scores.  
4. `Ponderaciones` – Pesos por dominio y por métrica.  
5. `Cálculos_IGM` – Cálculo de subíndices y del Índice Global de Madurez.  
6. `Cálculos_ROI` – Estimación de ROI en ciberseguridad.  
7. `Resultados` – Cuadros de mando y gráficos.

---

## 2. Hoja “Encuesta”

Columnas mínimas:

- `ID_Org`  
- `Nombre_Org`  
- `Sector`  
- `Tamaño`  
- `Ámbito`  
- `P1_1_1`, `P1_1_2`, … `P8_3`  

Cada columna de pregunta contiene el **valor numérico** de la respuesta (por ejemplo, 0–4, 0–5, porcentaje).

---

## 3. Hoja “Métricas”

Columnas sugeridas:

- `Metrica_ID` (M1.1, M1.2, etc.)  
- `Descripción`  
- `Pregunta_asociada` (P1_1_1, etc.)  
- `Dominio_COBIT` (EDM03, APO12…)  
- `Goal_GQM` (G1–G7)  
- `Escala_Min`  
- `Escala_Max`  
- `Tipo` (frecuencia, porcentaje, ordinal, continuo)

Ejemplo de fila:

- `M1.1`, “Nº reuniones/año con ciberseguridad en la agenda”, `P1_1_1`, `EDM03`, `G1`, `0`, `12`, `frecuencia`.

---

## 4. Hoja “PRAGMATIC”

Columnas:

- `Metrica_ID`  
- `P_Predictivo`  
- `R_Relevante`  
- `A_Accionable`  
- `G_Genuino`  
- `M_Significativo`  
- `A_Preciso`  
- `T_Oportuno`  
- `I_Independiente`  
- `C_Rentable`  
- `Score_Total` (por ejemplo, suma de las nueve anteriores)

Se pueden importar los valores iniciales de la **Matriz de Evaluación PRAGMATIC** y ajustarlos según el consenso de expertos.

---

## 5. Hoja “Ponderaciones”

Columnas:

- `Dominio` (Gobierno, Riesgo, Seguridad, Cambios, Servicios, Continuidad, Monitorización)  
- `Peso_Dominio` (por ejemplo, 1 por defecto; se puede dar más peso a dominios críticos)  
- `Metrica_ID`  
- `Peso_Metrica` (peso relativo dentro del dominio)  
- `Score_PRAGMATIC` (referencia desde la hoja PRAGMATIC)

Se puede definir un **Peso_Efectivo** como:

\[
Peso\_Efectivo = Peso\_Metrica \times \frac{Score\_PRAGMATIC}{Score\_Máx}
\]

para que las métricas con mejor calidad PRAGMATIC pesen más en el IGM.

---

## 6. Hoja “Cálculos_IGM”

### 6.1. Normalización de métricas

Para cada organización y métrica, calcular:

- `Valor_Norm = (Valor_Respuesta – Escala_Min) / (Escala_Max – Escala_Min)`

clampado a [0,1] en caso de valores extremos.

### 6.2. Puntuación por dominio

Para cada dominio \(d\):

\[
M_d = \frac{\sum (Valor\_Norm_{m} \cdot Peso\_Efectivo_{m})}{\sum Peso\_Efectivo_{m}} \times 5
\]

donde \(m\) recorre las métricas del dominio \(d\).

### 6.3. Índice Global de Madurez (IGM)

\[
IGM = \frac{\sum (M_d \cdot Peso\_Dominio)}{\sum Peso\_Dominio}
\]

Se puede expresar en:

- Escala **0–5** directamente, o  
- Escala **0–100** (multiplicando por 20).

---

## 7. Hoja “Cálculos_ROI”

Variables por organización (pueden provenir de la encuesta extendida o de datos internos):

- `Incidentes_Graves_Antes`  
- `Incidentes_Graves_Después`  
- `Coste_Medio_Incidente`  
- `Horas_Parada_Antes`  
- `Horas_Parada_Después`  
- `Coste_Hora_Negocio`  
- `Coste_Iniciativas_Seguridad` (por periodo analizado)

Fórmulas:

\[
Beneficio\_Incidentes = (Incidentes\_Graves\_Antes - Incidentes\_Graves\_Después) \times Coste\_Medio\_Incidente
\]

\[
Beneficio\_Continuidad = (Horas\_Parada\_Antes - Horas\_Parada\_Después) \times Coste\_Hora\_Negocio
\]

\[
Beneficio\_Total = Beneficio\_Incidentes + Beneficio\_Continuidad
\]

\[
ROI = \frac{Beneficio\_Total}{Coste\_Iniciativas\_Seguridad}
\]

La mejora en métricas como MTTD, MTTR, % vulnerabilidades en plazo, pruebas de BCP/DRP, etc., sirve para **explicar** la mejora de resultados.

---

## 8. Hoja “Resultados”

Elementos recomendados:

- Tabla por organización: IGM, M_d por dominio, Score_PRAGMATIC medio de métricas usadas, ROI (si se dispone).  
- Gráficos:

  - Radar de M_d por dominio.  
  - Histogramas del IGM por sector.  
  - Dispersión IGM vs ROI (cuando sea posible).

Esta hoja se alimenta directamente del resto y está pensada para exportar gráficos a informes.

---

_Fin de la plantilla._