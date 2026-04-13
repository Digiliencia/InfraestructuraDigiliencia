# Plantilla de Excel para IGM y ROI con enfoque GQM + PRAGMATIC  
## Integrando Objetivos ENS, Métricas y Evaluación de Calidad

Esta plantilla extiende la propuesta anterior de IGM/ROI incorporando:

- El mapeo a Objetivos GQM.  
- La evaluación PRAGMATIC de cada métrica. [web:32][web:33]

---

## 1. Hojas recomendadas

1. `Diccionario` – Preguntas, métricas, objetivos GQM, pesos, PRAGMATIC.  
2. `Respuestas` – Datos de la encuesta por organización.  
3. `Métricas` – Cálculo de métricas derivadas (por ejemplo, % implantación).  
4. `PRAGMATIC` – Valoración de calidad de métricas.  
5. `IGM` – Índice Global de Madurez y subíndices.  
6. `ROI` – Cálculo de retorno de inversión.  
7. `Resumen` – Tablas y gráficos.

---

## 2. Hoja `Diccionario`

Columnas sugeridas:

- `COD_PREGUNTA` – Código (ej. GOB_1_1).  
- `OBJETIVO_GQM` – G1…G6.  
- `METRICA` – Nombre de la métrica principal (M1.1, M3.1, etc.).  
- `DESCRIPCION_METRICA` – Texto breve.  
- `VALOR_MIN`, `VALOR_MAX` – Para normalización (0–1).  
- `PESO_IGM` – Peso de la métrica en el IGM.  
- `PESO_SUBINDICE` – Peso en el subíndice de bloque.  
- `P_RED`, `R_RED`, … `C_RED` – Puntuaciones PRAGMATIC (0–3) definidas a priori.  
- `REFERENCIA_ENS_CC NSTIC` – Artículo / guía relevante. [web:30][web:32][web:33]

Esto permite:

- Documentar la lógica de cada métrica.  
- Revisar periódicamente la idoneidad de la métrica según PRAGMATIC.

---

## 3. Hoja `Respuestas`

Igual que en la plantilla anterior:

- Filas = organizaciones.  
- Columnas = metadatos + respuestas codificadas por pregunta.

---

## 4. Hoja `Métricas`

Aquí se calculan las métricas derivadas a partir de varias respuestas (cuando sea necesario).

Ejemplos:

- `M1.1_%_Medidas_ENS` – cálculo a partir de varias preguntas de implantación.  
- `M3.1_%_MFA_Privilegiadas` – ratio entre nº cuentas privilegiadas con MFA / total cuentas privilegiadas.  
- `M4.1_MTTD` – media de diferencias entre “tiempo de detección” y “tiempo de inicio de incidente”.

Cada columna de métrica se conecta con la entrada correspondiente de `Diccionario`.

---

## 5. Hoja `PRAGMATIC`

Objetivo: visualizar qué métricas merecen más confianza o prioridad.

Columnas:

- `METRICA`  
- `P`, `R`, `A`, `G`, `M`, `P2`, `T`, `I`, `C` – valores PRAGMATIC.  
- `PROMEDIO_PRAGMATIC` – media simple o ponderada de los 9 criterios.  

Se pueden crear gráficos tipo radar para ver el perfil PRAGMATIC de cada métrica.

Uso sugerido:

- Establecer un umbral (ej. promedio ≥ 2) para métricas aptas para cuadro de mando ejecutivo.  
- Identificar métricas que requieren mejora (por ejemplo, muy relevantes pero poco precisas u oportunas).

---

## 6. Hoja `IGM`

Idéntica lógica que antes, con un matiz:

- Las métricas con baja puntuación PRAGMATIC pueden recibir un peso `PESO_IGM` menor o incluso temporalmente cero, hasta que se mejoren procesos de medición.

Fórmulas clave:

- Normalización: `VALOR_NORMALIZADO = (VALOR - VALOR_MIN) / (VALOR_MAX - VALOR_MAX)`  
- IGM: `IGM = 100 * SUMAPRODUCTO(VALOR_NORMALIZADO_i; PESO_IGM_i)`

Subíndices:

- `IGM_GOBIERNO`, `IGM_RIESGO`, `IGM_OPERACION`, etc., usando `PESO_SUBINDICE`.

---

## 7. Hoja `ROI`

Se mantienen los componentes:

- Costes de controles, personal, auditorías.  
- Costes de incidentes actuales.  
- Escenarios de mejora (por ejemplo, aumento del IGM o de subíndices concretos).

Con el enfoque GQM:

- Se puede relacionar cada línea de inversión con el objetivo GQM al que contribuye (G1…G6).  
- El indicador de ROI no solo dice “sale a cuenta”, sino “sale a cuenta en términos de G2 (riesgo), G3 (Zero Trust) o G4 (resiliencia)”.

---

## 8. Hoja `Resumen`

Debe poder responder, con un vistazo, a tres preguntas que cualquier dirección sensata debería hacerse:

1. ¿Cuál es nuestro IGM global y por bloques ENS?  
2. ¿En qué métricas clave (MFA, MTTD, % medidas ENS) estamos peor y qué calidad PRAGMATIC tienen?  
3. ¿Qué escenarios de inversión tienen mejor ratio coste/beneficio en términos de reducción de riesgo y cumplimiento ENS?

---

## 9. Notas operativas

- Mantener el `Diccionario` como fuente de verdad: cambios en preguntas, métricas o pesos se registran ahí.  
- Revisar puntuaciones PRAGMATIC al menos una vez al año o tras cambios significativos en procesos de recogida de datos.  
- Asegurar que el modelo Excel se comparte con formato protegido para evitar “creatividades” no controladas en fórmulas críticas.

La plantilla no convierte a nadie en actuario, pero sí ayuda a que las discusiones sobre ENS se apoyen en datos con un pedigrí metodológico visible.