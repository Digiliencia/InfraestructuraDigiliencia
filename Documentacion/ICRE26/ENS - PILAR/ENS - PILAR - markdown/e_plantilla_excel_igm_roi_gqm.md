# Plantilla Excel para IGM y ROI con GQM + PRAGMATIC

> Extensión de la plantilla de IGM y ROI para incorporar el mapeo GQM y la calificación PRAGMATIC de cada métrica.

---

## 1. Hojas propuestas

1. `CatalogoMetricas` – Definición GQM y PRAGMATIC de cada métrica.  
2. `DatosPILAR` – Exportaciones o extractos de resultados de PILAR (riesgos, madurez, etc.).  
3. `CalculoMetricas` – Cálculo numérico de cada métrica.  
4. `IGM_Dimensiones` – Cálculo del Índice Global de Madurez por dimensiones.  
5. `ROI_Proyectos` – Estimación del ROI de proyectos de seguridad.  

---

## 2. Hoja `CatalogoMetricas`

Columnas sugeridas:

- A: ID Métrica (ej. M1.1, M2.2, M3.4)  
- B: Descripción breve  
- C: Objetivo GQM (G1, G2, G3)  
- D: Pregunta asociada (Q1.1, Q2.2, etc.)  
- E: Fórmula lógica (en términos de datos PILAR)  
- F: Unidad (0–10, %, €, etc.)  
- G–O: P, R, A, G, M, A (Preciso), T, I, C (puntuaciones 1–5)  
- P: PRAGMATIC total (suma o media)  
- Q: Incluir en panel (Sí/No, en función de umbral PRAGMATIC)  
- R: Dimensión IGM principal asociada (1–5)  

Ejemplo de fila para M2.2:

- A: M2.2  
- B: % salvaguardas en verde  
- C: G2  
- D: Q2.2  
- E: Nº medidas con semáforo verde / Nº total medidas aplicables * 100  
- F: %  
- G–O: puntuaciones PRAGMATIC  
- P: cálculo total  
- Q: fórmula condicional (P ≥ umbral)  
- R: 3 (madurez de salvaguardas y controles)

---

## 3. Hoja `DatosPILAR`

Esta hoja debe contener:

- Tablas importadas de PILAR:  
  - Riesgo repercutido/acumulado por activo/dominio/amenaza.  
  - Niveles de madurez L0–L5 por salvaguarda y dominio.  
  - Recomendación 0–10 por salvaguarda y dominio.  
  - Estado de semáforo por medida.  

Columnas típicas:

- A: ID activo / dominio / medida  
- B: Tipo (activo esencial, soporte, salvaguarda, control ENS, etc.)  
- C: Dimensión de seguridad (C, I, D, etc., si aplica)  
- D: Riesgo repercutido/acumulado (0–10)  
- E: Madurez L0–L5  
- F: Recomendación (0–10)  
- G: Estado semáforo (verde/amarillo/rojo/gris)  
- H: Etiquetas adicionales (dominio, sistema, obligatoriedad ENS, etc.)

---

## 4. Hoja `CalculoMetricas`

Para cada métrica del catálogo:

- A: ID Métrica  
- B: Fórmula Excel implementada (referenciando `DatosPILAR`)  
- C: Valor calculado  
- D: Observaciones (por ejemplo, interpretación o limitaciones)

Ejemplo simplificado:

- Para M1.2 (% activos esenciales con riesgo alto):  
  - Contar activos esenciales con `Riesgo repercutido ≥ 7` y dividir por el número total de activos esenciales.

---

## 5. Hoja `IGM_Dimensiones`

Se reutiliza la lógica ya descrita para el IGM, conectando ahora:

- Cada pregunta/indicador de encuesta (si se mantiene) y  
- Cada métrica PILAR de la hoja `CalculoMetricas`.

Las dimensiones pueden ajustarse para incluir explícitamente:

1. Riesgo residual (M1.x).  
2. Madurez de salvaguardas y controles (M2.x).  
3. Cobertura ENS y priorización (M3.x).  
4. Ciclo de vida y continuidad (métricas adicionales).  
5. Cultura y gobierno (métricas de encuesta).

El cálculo del IGM sigue siendo una media ponderada de las dimensiones, pero puede incorporar tanto percepciones (encuesta) como datos técnicos (PILAR).

---

## 6. Hoja `ROI_Proyectos`

Se alinean los proyectos con métricas GQM:

- A: Proyecto/medida.  
- B: Coste total.  
- C: Métricas afectadas (ej. M1.2, M2.2, M3.3).  
- D: Δ esperado en cada métrica (por ejemplo, reducción del % de activos en riesgo alto).  
- E: Traducción del Δ riesgo a reducción de pérdidas esperada (en €).  
- F: ROI % y Payback, como en la plantilla general de ROI.

Esta hoja puede apoyarse en supuestos parametrizables (por ejemplo, valor monetario de un punto de riesgo reducido en activos de cierto tipo).

---

## 7. Buenas prácticas

- Mantener consistente el catálogo de métricas GQM con el diseño de paneles y reportes.  
- Documentar los supuestos de conversión riesgo → pérdida económica.  
- Utilizar la puntuación PRAGMATIC para decidir qué métricas se dejan en segundo plano cuando la complejidad crece.
