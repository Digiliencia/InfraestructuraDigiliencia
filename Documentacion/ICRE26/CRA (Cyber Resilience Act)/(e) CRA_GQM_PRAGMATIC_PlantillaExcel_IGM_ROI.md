# Plantilla Excel – IGM y ROI con dimensiones GQM + PRAGMATIC

> Extiende la plantilla anterior de IGM/ROI para integrar objetivos GQM y métricas nacionales PRAGMATIC.

---

## 1. Hojas propuestas

1. `Datos_Encuesta` – Respuestas codificadas (igual que en el kit base).  
2. `Codificacion_Preguntas` – Tablas de codificación de cada ítem.  
3. `Calculo_IGM` – Índice Global de Madurez y subíndices.  
4. `Mapeo_GQM` – Asociación de preguntas a objetivos GQM y métricas nacionales.  
5. `Calculo_ROI` – Estimaciones de coste, pérdidas evitables y ROI.  
6. `Dashboard_Nacional` – Visualización de métricas agregadas alineadas con GQM.

---

## 2. Hoja `Datos_Encuesta`

Idéntica al modelo base:

- Columnas: `ID_Organizacion`, `Sector`, `Tamaño`, `P1`…`P37` (codificadas).  
- Opcional: `Pais`, `Region`, `CriticidadSectorial`.

---

## 3. Hoja `Codificacion_Preguntas`

Para cada pregunta, tabla con:

- Columna A: `Pregunta`.  
- Columna B: `Valor_Texto`.  
- Columna C: `Valor_Codigo` (0–3 ó 0–5).  
- Columna D: `Peso` (si se quiere diferenciar impacto dentro de una misma dimensión).

Excel puede usar BUSCARV/XLOOKUP para mapear respuestas textuales a códigos.

---

## 4. Hoja `Calculo_IGM`

### 4.1 Dimensiones por columnas

Por ejemplo:

- `GOV` (Gobernanza y estrategia)  
- `COV` (Cobertura y conformidad)  
- `VULN` (Vulnerabilidades e incidentes)  
- `DATA` (Métricas y datos)  
- `CAP` (Capacidades y cultura)  
- `IGM` (índice global, 0–100)

Cada dimensión se calcula como:

- `GOV` = PROMEDIO(normalizados(P5,P6,P7,P8,P26,P30)) * 100  
- `COV` = PROMEDIO(normalizados(P9,P10,P11,P12,P13,P14,P15,P16)) * 100  
- etc.

La **normalización** consiste en `Valor_Codigo / Valor_Maximo_Pregunta`.

### 4.2 Integración GQM

Se añade para cada organización:

- `G1_Score`, `G2_Score`, `G3_Score`, `G4_Score`, `G5_Score`.

Estos pueden derivarse de los mismos grupos de preguntas, pero agrupados por objetivo GQM:

- `G2_Score` pondera especialmente P9–P16 (productos) y las partes de P27 que se refieren a métricas de productos.  
- `G3_Score` pondera P17–P24, P33–P34.  
- etc.

---

## 5. Hoja `Mapeo_GQM`

Contiene la tabla:

- `Pregunta`, `Objetivo_GQM`, `Metrica_Nacional`, `Peso_en_Objetivo`.

Ejemplo de fila:

- P18 | G3 | M5.1 | 0,15

Esto permite construir fórmulas del tipo:

- `G3_Score` = SUMAPRODUCTO(Valores_Normalizados_P17:P24, Pesos_G3_P17:P24) * 100

---

## 6. Hoja `Calculo_ROI`

### 6.1 Entradas clave

- `Presupuesto_TIC` (si se dispone, por organización).  
- `Pct_Ciberseguridad` (derivado de P31).  
- `Pct_CRA` (derivado de P32).  
- `Incidentes_Evitables` (P33).  
- `Impacto_Incidentes` (P34, convertido al valor medio del rango).  
- `IGM` (de `Calculo_IGM`).

### 6.2 Escenarios de reducción de pérdidas

Se definen supuestos:

- Escenario Base: reducción esperable de pérdidas del 10 % por cada 10 puntos de IGM ganados por encima de un umbral (por ejemplo, 40).  
- Escenario Conservador / Optimista, modificando el factor.

En Excel:

- `Delta_IGM` = MAX(0; IGM - 40).  
- `Factor_Reduccion` = MIN(0,5; Delta_IGM / 100 * 0,5)  → máximo 50 % de reducción.  
- `Perdida_Evitable` = `Impacto_Incidentes` * `Factor_Reduccion`.  
- `Presupuesto_CRA` = `Presupuesto_TIC` * `Pct_Ciberseguridad` * `Pct_CRA`.  
- `ROI_Ratio` = `Perdida_Evitable` / `Presupuesto_CRA`.

---

## 7. Hoja `Dashboard_Nacional`

Agrega datos por:

- Sector.  
- Tamaño.  
- Región.  

Ejemplos de visualizaciones:

- Mapa de calor de `G2_Score` y `G3_Score` por sector.  
- Gráfico de dispersión `IGM` vs `ROI_Ratio`.  
- Gráfico de barras de `M6.1` (deuda de vulnerabilidades) por sector crítico.

El cuadro de mando puede alimentarse directamente con Power BI u otra herramienta, pero esta hoja sirve como puente.
