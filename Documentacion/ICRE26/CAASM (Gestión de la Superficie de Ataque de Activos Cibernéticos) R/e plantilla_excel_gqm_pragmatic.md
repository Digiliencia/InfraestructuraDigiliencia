# Plantilla Excel – Cálculo de IGM y Evaluación PRAGMATIC

Este documento describe una plantilla Excel para:

1. Calcular un **Índice Global de Madurez (IGM)** basado en las métricas GQM CAASM.  
2. Registrar las puntuaciones PRAGMATIC de cada métrica.

---

## 1. Estructura del libro

Se recomiendan al menos cinco hojas:

1. `Métricas` – Valores observados de M1.x, M2.x, etc., por organización o sector.  
2. `Índices` – Cálculo de índices parciales y del IGM.  
3. `PRAGMATIC` – Puntuaciones de calidad por métrica.  
4. `ROI` – Estimaciones de costes y beneficios.  
5. `Parámetros` – Pesos, escalas y definiciones.

---

## 2. Hoja “Métricas”

Columnas sugeridas:

- A: ID Organización / Sector  
- B: M1.1 – % activos críticos descubiertos vs estimados  
- C: M1.2 – Ratio activos no inventariados  
- D: M1.3 – % dominios con inventario integrado  
- E: M2.1 – Nº/% servicios expuestos sin controles mínimos  
- F: M2.2 – % exposiciones alta probabilidad no mitigadas  
- G: M2.3 – Nº activos con combinaciones tóxicas  
- H: M3.1 – MTTR exposiciones críticas (días)  
- I: M3.2 – % exposiciones críticas cerradas en plazo  
- J: M3.3 – % remediaciones automatizadas  
- K: M4.1 – % controles ENS/NIS2 con evidencia automática  
- L: M4.2 – Nº no conformidades ya señaladas  
- M: M5.1 – % entidades que comparten telemetría  
- N: M5.2 – Nº patrones de exposición documentados

---

## 3. Hoja “Índices”

### 3.1 Cálculo de índices parciales

Para cada fila (organización/sector), se calculan índices de 0–100. Se pueden normalizar o invertir según convenga (por ejemplo, menos M2.1 es mejor, por lo que se crea una versión “invertida” como indicador de salud).

Ejemplos:

- IVA (Visibilidad): función de M1.1, M1.2 (invertida), M1.3.  
- IEP (Exposición): función de M2.1 (invertida), M2.2 (invertida), M2.3 (invertida).  
- IRA (Remediación): función de M3.1 (invertida), M3.2, M3.3.  
- ICR (Cumplimiento): función de M4.1, M4.2 (invertida).  
- IGC (Gobernanza): función de M5.1, M5.2.

Se recomienda documentar la fórmula en `Parámetros`, por ejemplo:

- IVA = PROMEDIO( Normalizar(M1.1), 100 - Normalizar(M1.2), Normalizar(M1.3) ).

### 3.2 Cálculo del IGM

Definir pesos en `Parámetros` (por ejemplo):

- Peso_IVA = 0,20  
- Peso_IEP = 0,25  
- Peso_IRA = 0,25  
- Peso_ICR = 0,15  
- Peso_IGC = 0,15  

IGM = IVA*Peso_IVA + IEP*Peso_IEP + IRA*Peso_IRA + ICR*Peso_ICR + IGC*Peso_IGC.

---

## 4. Hoja “PRAGMATIC”

Filas: una por métrica (M1.1, M1.2, …, M5.2).

Columnas:

- A: Métrica  
- B: Descripción  
- C: P – Predictivo (1–5)  
- D: R – Relevante (1–5)  
- E: A – Accionable (1–5)  
- F: G – Genuino (1–5)  
- G: M – Significativo (1–5)  
- H: P2 – Preciso (1–5)  
- I: T – Oportuno (1–5)  
- J: I2 – Independiente (1–5)  
- K: C – Rentable (1–5)  
- L: PRAGMATIC_Score = PROMEDIO(C:K)

Opcional: columna M para comentarios cualitativos.

---

## 5. Hoja “ROI”

Similar a la plantilla anterior de ROI CAASM, se recomienda:

- Costes: licencias, integración, operación.  
- Beneficios: reducción de incidentes, ahorro en auditorías, otros.  
- ROI simple: (Beneficios – Costes) / Costes.

Se puede relacionar el IGM con el ROI para observar tendencias (por ejemplo, si mayor madurez se correlaciona con menor frecuencia de incidentes graves).

---

## 6. Visualizaciones recomendadas

- Gráfico de barras de IGM por organización o sector.  
- Mapa de calor de índices parciales (IVA, IEP, IRA, ICR, IGC).  
- Gráfico de burbujas IGM vs ROI, con tamaño de burbuja representando M2.1 o M3.1.  
- Tabla ordenada por PRAGMATIC_Score para priorizar métricas nacionales.

---

Fin de la plantilla.