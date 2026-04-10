# (e) Plantilla de Excel GQM + PRAGMATIC para cálculo de IGM y ROI (descripción)

## 1. Estructura recomendada del libro Excel

Se propone un libro con las siguientes hojas:

1. `Objetivos_GQM`: listado de objetivos, preguntas y métricas.
2. `Def_Metricas`: ficha técnica y PRAGMATIC de cada métrica.
3. `Datos_Operacionales`: captura periódica de datos brutos por organización/unidad.
4. `Calculos_IGM`: agregación de métricas GQM en subíndices e IGM.
5. `Calculos_ROI`: modelo de retorno de la inversión.
6. `Dashboard_Ejecutivo`: visualización integrada.

## 2. Hoja `Objetivos_GQM`

Columnas sugeridas:
- A: Código de objetivo (G1–G8).
- B: Descripción del objetivo.
- C: Código de pregunta (Q1.1, Q1.2, etc.).
- D: Texto de la pregunta.
- E: Código de métrica asociada (M1.1, M1.2, etc.).
- F: Nombre de la métrica.

Esta hoja permite asegurar trazabilidad: cualquier métrica usada en el IGM o en el ROI debe estar vinculada a objetivos explícitos.

## 3. Hoja `Def_Metricas`

Columnas sugeridas:
- A: Código de métrica (M1.1, M2.2, etc.).
- B: Nombre corto.
- C: Descripción.
- D: Fórmula de cálculo.
- E: Unidad (%, nº, días, €…).
- F: Frecuencia (mensual, trimestral, anual).
- G: Responsable de generación.
- H: Fuentes de datos (SIEM, CMDB, HR, etc.).
- I–Q: Puntuaciones PRAGMATIC (P, R, A, G, M, P2, T, I2, C).
- R: Nota PRAGMATIC total (por ejemplo, suma o media de I–Q).

Se recomienda establecer un umbral mínimo de calidad (p.ej. nota media ≥ 2) para que una métrica pueda entrar en el cuadro de mando ejecutivo.

## 4. Hoja `Datos_Operacionales`

Filas:
- Una fila por combinación (Organización/Unidad, Periodo).

Columnas:
- A: Identificador de organización/unidad.
- B: Periodo (año, trimestre, mes).
- C en adelante: columnas para cada métrica (M1.1, M1.2, …).

Las fórmulas pueden extraer algunos valores automáticamente desde otras fuentes (vinculadas o importadas) o introducirse manualmente si no existe integración.

## 5. Hoja `Calculos_IGM`

### 5.1. Agregación por objetivos y bloques

- Definir una tabla de asignación de métricas a bloques o dominios (Gobernanza, Riesgos, Datos, etc.).
- Calcular para cada combinación (organización, periodo) la puntuación normalizada de cada métrica, si procede (por ejemplo, % expresados como 0–1).

### 5.2. Cálculo de subíndices

Para cada dominio, calcular un subíndice como media (simple o ponderada) de las métricas asignadas. La ponderación puede guiarse por la nota PRAGMATIC (más peso a las métricas de mayor calidad).

Por ejemplo:

`Subindice_Riesgos = SUMAPRODUCTO(Puntuaciones_Metricas_Riesgo; Pesos_Metricas_Riesgo)`

### 5.3. Cálculo del IGM

El IGM global se obtiene como media ponderada de los subíndices:

`IGM = 100 × SUMAPRODUCTO(Subindices; Pesos_Subindices)`

Donde los pesos pueden seguir la lógica de riesgo (más peso a incidentes, riesgos y monitorización) y adaptarse a regulaciones sectoriales.

## 6. Hoja `Calculos_ROI`

### 6.1. Entradas

- Costes directos del AIMS y de controles de IA segura (personal, herramientas, consultoría, certificaciones).
- Métricas de incidentes (M3.1, M3.2, M6.2, M5.2), con historiales antes/después de las principales iniciativas.
- Estimaciones de coste medio por incidente y por hora de interrupción/recuperación.

### 6.2. Modelo de cálculo

- Estimar incidentes evitados o mitigados comparando escenarios (por ejemplo, número de incidentes antes y después de ciertas mejoras, corregido por volumen de actividad o exposición).
- Traducir esas diferencias a euros usando el coste medio por incidente.

Fórmula simplificada:

`Beneficio_Anual ≈ (Incidentes_Base – Incidentes_Actuales) × Coste_Medio_Incidente + Reduccion_Tiempo_Recuperacion × Coste_Hora_Interrupcion`

`ROI = (Beneficio_Anual – Costes_Anuales_AIMS) / Costes_Anuales_AIMS`

Es prudente acompañar el cálculo con rangos (escenario conservador, medio, optimista) para reflejar la incertidumbre.

## 7. Hoja `Dashboard_Ejecutivo`

Elementos recomendados:

- Gráfico de barras con IGM por organización/unidad y periodo.
- Gráfico radar con subíndices para la organización principal.
- Líneas de tendencia de métricas clave (M2.2 MTTR-IA, M3.2 MTTD/MTTC, M4.1 % modelos con detección de drift, M7.2 % personal formado).
- Indicadores de ROI con escenarios.

Los gráficos deben apoyarse en una narrativa que explique causalidades plausibles (“al incrementar la cobertura de monitorización, reducimos el tiempo de detección y observamos menor impacto medio por incidente”).
