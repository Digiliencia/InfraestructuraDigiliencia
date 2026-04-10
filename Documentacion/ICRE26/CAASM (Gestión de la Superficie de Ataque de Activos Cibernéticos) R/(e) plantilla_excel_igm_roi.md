# Plantilla de Excel para Cálculo de IGM y ROI CAASM

> Esta plantilla describe la estructura recomendada de un fichero Excel para calcular el **Índice Global de Madurez (IGM)** y estimar el **ROI de iniciativas CAASM** a partir de los resultados de la encuesta.

---

## 1. Estructura general de la hoja

Se recomienda un libro con al menos cuatro hojas:

1. `Respuestas` – Codificación numérica de las respuestas de la encuesta.  
2. `Índices` – Cálculo de índices parciales e IGM.  
3. `ROI` – Cálculo de beneficios, costes y retorno.  
4. `Parámetros` – Pesos, umbrales y supuestos.

---

## 2. Hoja “Respuestas”

Columnas sugeridas:

- A: ID Organización  
- B: Sector  
- C: Tamaño  
- D: Rol del respondente  
- E…: Pregunta_1.1.1, Pregunta_1.1.2, etc., con valores NUMÉRICOS (1–4, 1–5).

Ejemplo de codificación (columna E – Pregunta 1.1.1):

- 4 → Casi total  
- 3 → Alta  
- 2 → Limitada  
- 1 → Muy baja

Se recomendaría añadir una fila explicando la escala, o bien documentarla en la hoja `Parámetros`.

---

## 3. Hoja “Índices”

### 3.1 Definición de grupos

En `Parámetros` (o en la parte superior de `Índices`) definir:

- Rango de celdas que corresponden a cada bloque:  
  - Visibilidad (IVA): lista de columnas de `Respuestas`.  
  - Higiene (IHC)  
  - Exposición/priorización (IEP)  
  - Remediación/automatización (IRA)  
  - Cumplimiento/reporting (ICR)  
  - Gobernanza/cultura (IGC)

### 3.2 Cálculo de índices parciales

Para cada organización (fila):

- IVA = PROMEDIO de las respuestas codificadas de las preguntas de visibilidad.  
- IHC = PROMEDIO de las respuestas del bloque de higiene.  
- IEP = PROMEDIO del bloque exposición/priorización.  
- IRA = PROMEDIO del bloque remediación/automatización.  
- ICR = PROMEDIO del bloque cumplimiento.  
- IGC = PROMEDIO del bloque gobernanza.

Se puede usar:

- `=PROMEDIO(conjunto_de_celdas)`  

Asegurar que celdas vacías (sin respuesta) no distorsionan el cálculo (usar `PROMEDIO.SI` o mecanismos equivalentes si es necesario).

### 3.3 Normalización (opcional)

Si se emplean escalas distintas (por ejemplo, algunas preguntas a 1–4 y otras a 1–5), normalizar cada respuesta a un rango común (por ejemplo, 0–100):

- Valor_normalizado = (Valor_observado – Valor_mínimo) / (Valor_máximo – Valor_mínimo) * 100

Así, cada índice se expresa como porcentaje (0–100).

### 3.4 Cálculo del IGM

En `Parámetros`, definir pesos (por defecto):

- Peso_IVA = 0,20  
- Peso_IHC = 0,20  
- Peso_IEP = 0,20  
- Peso_IRA = 0,20  
- Peso_ICR = 0,10  
- Peso_IGC = 0,10

Para cada organización:

- IGM = IVA * Peso_IVA + IHC * Peso_IHC + IEP * Peso_IEP + IRA * Peso_IRA + ICR * Peso_ICR + IGC * Peso_IGC

Si los índices ya están normalizados a 0–100, el IGM también lo estará (0–100).

---

## 4. Hoja “ROI”

El ROI de iniciativas CAASM es siempre una aproximación, pero puede estimarse comparando:

- **Costes**: licencias, servicios, personal, proyectos de integración.  
- **Beneficios**: reducción esperada de incidentes, reducción de tiempos de remediación, menores multas/regulatorios, ahorro de esfuerzo en auditorías.

### 4.1 Variables básicas

Columnas sugeridas:

- A: ID Organización  
- B: Coste anual CAASM (euros)  
- C: Reducción estimada de incidentes significativos (número por año)  
- D: Coste medio de un incidente significativo (euros)  
- E: Ahorro anual por reducción de incidentes = C * D  
- F: Ahorro anual por reducción de esfuerzo en auditorías (euros)  
- G: Otras eficiencias cuantificadas (euros)  
- H: Beneficios totales anuales = E + F + G  
- I: ROI simple = (H – B) / B

### 4.2 Ejemplo de cálculo

Si:

- Coste anual CAASM = 200.000 €  
- Reducción estimada de 2 incidentes/año  
- Coste medio incidente = 250.000 €  
- Ahorro en auditorías = 50.000 €  
- Otras eficiencias = 0 €

Entonces:

- E = 2 * 250.000 = 500.000 €  
- H = 500.000 + 50.000 = 550.000 €  
- ROI = (550.000 – 200.000) / 200.000 = 1,75 (175 %)

---

## 5. Hoja “Parámetros”

Incluir:

- Escalas de codificación para cada pregunta.  
- Pesos de cada índice en el IGM.  
- Supuestos sobre coste medio de incidentes, tiempo de dedicación liberado, etc.  
- Umbrales de interpretación (por ejemplo, IGM < 40 = bajo; 40–60 = medio; 60–80 = alto; > 80 = muy alto).

---

## 6. Visualizaciones sugeridas

En la misma hoja de Excel (o en una adicional):

- Gráfico radar comparando IVA, IHC, IEP, IRA, ICR, IGC.  
- Barras comparando IGM por unidad o por sector.  
- Gráficos de dispersión IGM vs ROI.

---

Fin de la plantilla descriptiva.