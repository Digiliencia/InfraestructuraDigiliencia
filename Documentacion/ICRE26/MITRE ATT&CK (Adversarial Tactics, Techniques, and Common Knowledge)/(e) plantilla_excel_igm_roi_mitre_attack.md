# Plantilla (descripción) para Excel: Cálculo de IGM y ROI MITRE ATT&CK

## 1. Hojas propuestas

- **Hoja 1 – Respuestas**  
- **Hoja 2 – Cálculo IGM**  
- **Hoja 3 – Cálculo ROI**  
- **Hoja 4 – Resumen Ejecutivo**

---

## 2. Hoja 1 – Respuestas

Columnas:

- A: ID Pregunta (G1, G2, C1, etc.)  
- B: Bloque (Gobierno, Cobertura, Calidad, etc.)  
- C: Descripción breve de la pregunta  
- D: Puntuación (0–5)  
- E: Comentarios

Cada fila corresponde a una pregunta de la encuesta.

---

## 3. Hoja 2 – Cálculo IGM

### 3.1 Estructura

- A: Bloque (G, C, Q, T, A, I, E, F, H)  
- B: Descripción  
- C: Número de preguntas en el bloque  
- D: Suma de puntuaciones (vinculada a Hoja 1)  
- E: IGM_Bloque = D / C  
- F: Peso asignado (en %)  
- G: Contribución al IGM Global = E * F

### 3.2 Fórmulas ejemplo

Supongamos:

- Respuestas en Hoja1!A:E  
- Bloque G (Gobierno) incluye preguntas G1–G4.

En Hoja 2:

- En D2 (Suma de bloque G):  
  `=SUMAR.SI(Hoja1!B:B;"Gobierno";Hoja1!D:D)`  

- En C2 (Número de preguntas bloque G):  
  `=CONTAR.SI(Hoja1!B:B;"Gobierno")`  

- En E2 (IGM_Gobierno):  
  `=D2/C2`  

- En F2 (Peso, por ejemplo 0,15)  

- En G2 (Contribución):  
  `=E2*F2`  

El **IGM Global** en Hoja 2 (por ejemplo en G20):  
`=SUMA(G2:G10)`

---

## 4. Hoja 3 – Cálculo ROI

### 4.1 Estructura

Para cada iniciativa (fila):

- A: ID iniciativa  
- B: Descripción (p. ej., “Mejorar cobertura Lateral Movement”)  
- C: Bloques afectados (texto)  
- D: IGM antes (media de bloques relevantes)  
- E: IGM después (estimado/medido)  
- F: ΔIGM = E – D  
- G: Riesgo Anual Esperado (RAE) antes (en €)  
- H: RAE después (estimado)  
- I: Reducción de riesgo = G – H  
- J: Coste de la iniciativa (en €)  
- K: ROI = (I – J) / J

### 4.2 Fórmulas ejemplo

- En F2: `=E2-D2`  
- En I2: `=G2-H2`  
- En K2: `=(I2-J2)/J2`

La plantilla deja a la organización la parametrización de cómo relaciona ΔIGM con reducción de RAE, apoyándose en datos externos (por ejemplo, porcentaje de incidentes asociados a determinadas tácticas según ENISA 2025, o estudios sectoriales).[web:66][web:61]

---

## 5. Hoja 4 – Resumen Ejecutivo

Elementos:

- Tabla con IGM Global y por bloque.  
- Gráfico de radar (IGM por bloque).  
- Gráfico de barras (ΔIGM antes/después de iniciativas clave).  
- Tabla de iniciativas con mayor ROI.  

Estos elementos pueden copiarse a la plantilla de PowerPoint.