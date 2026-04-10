# Plantilla Excel (Descripción) – Cálculo de IGM y ROI con GQM + PRAGMATIC

## 1. Hojas recomendadas

- **Hoja 1 – Métricas ATT&CK** (valores por organización/sector/país).  
- **Hoja 2 – PRAGMATIC** (puntuación de calidad de cada métrica).  
- **Hoja 3 – IGM (Índice Global de Madurez)**.  
- **Hoja 4 – ROI de iniciativas ATT&CK‑driven**.  
- **Hoja 5 – Resumen Ejecutivo / Gráficos.**

---

## 2. Hoja 1 – Métricas ATT&CK

Columnas:

- A: ID Métrica (I1, I2, I3, … I11).  
- B: Nombre (p. ej. Cobertura tácticas prioritarias).  
- C: Unidad de medida (%, horas, índice, etc.).  
- D: Valor actual (organización/sector/país).  
- E: Valor objetivo.  
- F: Brecha (Fórmula: `=E2-D2`).  
- G: Observaciones.

Cada fila = una métrica (I1–I11).

---

## 3. Hoja 2 – PRAGMATIC

Columnas:

- A: ID Métrica (I1–I11).  
- B: Nombre.  
- C: P (Predictivo).  
- D: R (Relevante).  
- E: A (Accionable).  
- F: G (Genuino).  
- G: M (Meaningful).  
- H: P2 (Preciso).  
- I: T (Oportuno).  
- J: I2 (Independiente).  
- K: C (Cost‑effective).  
- L: Total PRAGMATIC (0–45).  
- M: Media PRAGMATIC (0–5).

Fórmulas:

- En L2: `=SUMA(C2:K2)`  
- En M2: `=L2/9`

Se puede añadir una columna **N: Peso PRAGMATIC** (normalización), por ejemplo:

- Calcular suma total de M (medias PRAGMATIC) en una celda (por ejemplo M15): `=SUMA(M2:M12)`  
- En N2: `=M2/$M$15`

Esto permite ponderar el IGM por la “calidad” de cada métrica.

---

## 4. Hoja 3 – IGM (Índice Global de Madurez)

### 4.1 Estructura

- A: ID Métrica (I1–I11).  
- B: Nombre.  
- C: Valor actual (replicado de Hoja 1).  
- D: Normalización (si es necesario, p. ej., pasar % a escala 0–5).  
- E: Peso GQM (importancia estratégica, 0–1).  
- F: Peso PRAGMATIC (desde Hoja 2, columna N).  
- G: Peso combinado = E × F.  
- H: Contribución = D × G.

### 4.2 Fórmulas ejemplo

- D2: Normalización (ejemplo para una métrica % con objetivo 100 %):  
  `=MIN(5; (C2/100)*5)`  

- G2: `=E2*F2`  

- H2: `=D2*G2`  

El **IGM Global** (por ejemplo en H20):  
`=SUMA(H2:H12)`

---

## 5. Hoja 4 – ROI de iniciativas ATT&CK‑driven

### 5.1 Estructura

Por iniciativa (fila):

- A: ID iniciativa.  
- B: Nombre (p. ej., “Mejorar cobertura técnicas credenciales sector salud”).  
- C: Métrica(s) afectada(s) (texto: I2, I3, I6…).  
- D: IGM antes (promedio ponderado de métricas afectadas).  
- E: IGM después (estimado / medido tras proyecto).  
- F: ΔIGM = E – D.  
- G: RAE antes (Riesgo Anual Esperado, en €).  
- H: RAE después (est.: aplicando % reducción basado en ΔIGM).  
- I: Reducción de riesgo = G – H.  
- J: Coste iniciativa (en €).  
- K: ROI = (I – J) / J.

### 5.2 Fórmulas ejemplo

- F2: `=E2-D2`  
- I2: `=G2-H2`  
- K2: `=(I2-J2)/J2`

La fórmula que relaciona ΔIGM con reducción de RAE será específica de cada país/sector, apoyándose idealmente en datos de incidentes y estudios sectoriales (por ejemplo, distribución de incidentes y costes por táctica en ENISA ETL 2025).[web:66][web:61]

---

## 6. Hoja 5 – Resumen Ejecutivo

Elementos:

- Tabla con:
  - IGM Global.  
  - 3–5 métricas con mayor peso combinado.  
- Gráfico de barras:
  - Valor actual vs objetivo de métricas clave (I2, I3, I6, I8, I11).  
- Gráfico de burbujas:
  - Eje X: Peso combinado GQM+PRAGMATIC.  
  - Eje Y: Brecha (objetivo – actual).  
  - Tamaño burbuja: coste estimado de mejora.

Esta hoja sirve de base visual para el reporte ejecutivo.