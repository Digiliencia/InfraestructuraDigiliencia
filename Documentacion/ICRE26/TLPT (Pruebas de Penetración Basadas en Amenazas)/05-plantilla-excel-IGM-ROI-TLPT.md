# Plantilla de Excel para cálculo de IGM y ROI de TLPT

## 1. Estructura de hojas

Se recomiendan al menos 4 hojas:

1. `Catalogo_Preguntas`  
2. `Respuestas_Entidad`  
3. `IGM_Dominios`  
4. `ROI_TLPT`

## 2. Hoja `Catalogo_Preguntas`

Columnas sugeridas:

- `ID_Pregunta` (p.ej., P04, P05, etc.)  
- `Bloque` (Gobierno, Alcance, Metodología, Operaciones, Remediación, Cultura)  
- `Texto_Pregunta`  
- `Opcion` (1, 2, 3, 4...)  
- `Descripcion_Opcion` (resumen de la opción de respuesta)  
- `Puntuacion_0_3` (0, 1, 2, 3)  

Cada fila representa una opción de respuesta con su puntuación.  

## 3. Hoja `Respuestas_Entidad`

Columnas sugeridas:

- `ID_Pregunta`  
- `Respuesta_Marcada` (número de opción elegida)  
- `Puntuacion_0_3` (BUSCARV en `Catalogo_Preguntas`)  
- `Bloque` (arrastrado desde catálogo)

Ejemplo de fórmula:  

- En `Puntuacion_0_3`, usar una fórmula tipo:  
  - `=BUSCARX(1; (Catalogo_Preguntas!A:A=ID_Pregunta)*(Catalogo_Preguntas!D:D=Respuesta_Marcada); Catalogo_Preguntas!F:F)`  

(Adaptar a la versión de Excel; se puede usar BUSCARV/ÍNDICE+COINCIDIR).

## 4. Hoja `IGM_Dominios`

Columnas sugeridas:

- `Bloque`  
- `Peso_Bloque` (p.ej., Gobierno 15%, Alcance 20%, Metodología 20%, Operaciones 25%, Remediación 15%, Cultura 5%)  
- `Puntuacion_Media_0_3` (promedio de puntuaciones 0–3 de las preguntas del bloque)  
- `Puntuacion_Normalizada_0_100` = `Puntuacion_Media_0_3 * 100 / 3`  
- `Contribucion_IGM` = `Puntuacion_Normalizada_0_100 * Peso_Bloque`

En una celda resumen, `IGM_Global` = suma de `Contribucion_IGM` de todos los bloques.

## 5. Hoja `ROI_TLPT`

### 5.1 Variables de entrada

Columnas/celdas de entrada:

- `Coste_TLPT` (honorarios Red Team, TTI, gestión interna, otros).  
- `Coste_Acciones_Remediacion` (CAPEX/OPEX de proyectos derivados del TLPT).  
- `Perdidas_Previstas_Evitadas` (estimación, basada en reducción de probabilidad/impacto de incidentes, usando modelos de riesgo operativ).  
- `Ahorros_Regulatorios` (multas evitadas, capital regulatorio optimizado, etc., si procede).[web:26]  

### 5.2 Cálculo simplificado de ROI

- `Beneficio_Total` = `Perdidas_Previstas_Evitadas + Ahorros_Regulatorios`  
- `Coste_Total` = `Coste_TLPT + Coste_Acciones_Remediacion`  

ROI clásico:

- `ROI_TLPT` = `(Beneficio_Total - Coste_Total) / Coste_Total`

Para facilitar lectura, crear celdas con:

- ROI en porcentaje (formato %).  
- Interpretación cualitativa (usar fórmula con `SI` anidados):  
  - ROI < 0 → “ROI aparente negativo (revisar supuestos y horizonte temporal)”.  
  - 0–50% → “ROI moderado: resiliencia como seguro razonable”.  
  - >50% → “ROI alto: TLPT claramente rentable según los supuestos”.

### 5.3 Vinculación con IGM

Se puede añadir un gráfico que compare:

- `IGM_Global` vs. `ROI_TLPT`.  
- Cambios de IGM entre ciclos vs. variaciones en pérdidas reales por incidentes, para apoyar la narrativa de que la resiliencia “paga” a medio plazo.
