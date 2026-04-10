# Plantilla de Excel para cálculo de IGM y ROI integrando GQM + PRAGMATIC

Esta plantilla extiende la versión anterior de cálculo de Índice Global de Madurez (IGM) y ROI con:

- Un vínculo explícito a los objetivos GQM.  
- Una tabla de puntuaciones PRAGMATIC por métrica. [web:44][web:52]

## 1. Hojas recomendadas

1. `RESPUESTAS_ENCUESTA` – Captura codificada de respuestas (P1_1, P2_1, etc.).  
2. `CATALOGO_METRICAS` – Lista de métricas (M‑*) con su definición, fórmula y objetivo GQM asociado.  
3. `PRAGMATIC` – Puntuaciones PRAGMATIC (P, R, A, G, M, A2, T, I, C) para cada métrica.  
4. `PONDERACIONES` – Pesos por bloque GQM y por métrica en el cálculo del IGM.  
5. `CALCULO_SUBINDICES` – Cálculo de subíndices por objetivo GQM/familia.  
6. `CALCULO_IGM` – Cálculo del IGM global.  
7. `DATOS_ECONOMICOS` – Costes de seguridad, pérdidas, etc.  
8. `CALCULO_ROI` – Cálculo de ROI y métricas económicas asociadas.  
9. `CUADRO_MANDO` – Resumen visual.

## 2. Hoja CATALOGO_METRICAS

Estructura sugerida:

| ID_Metrica     | Nombre corto                 | Descripción                                    | Objetivo_GQM | Fórmula (texto)                      | Unidad | Fuente de datos principal |
|----------------|------------------------------|------------------------------------------------|-------------|--------------------------------------|--------|---------------------------|
| M‑MAD‑SCORE    | Madurez SGSI                 | Puntuación global de madurez SGSI             | G‑MAD‑1     | Resultado evaluación madurez / max  | %      | Auditoría SGSI / GRC      |
| M‑RISK‑TREATED | Riesgos tratados en plazo    | % riesgos tratados dentro del plazo definido  | G‑RISK‑1    | (Riesgos en plazo / Total tratados) | %      | Herramienta riesgos       |
| M‑TECH‑CRIT‑MTTR| MTTR vulnerabilidades crit. | Tiempo medio de corrección vulns. críticas    | G‑TECH‑1    | Media(tiempo cierre vulns. críticas)| horas  | Gestor de vulnerabilidades|
| ...            | ...                          | ...                                            | ...         | ...                                  | ...    | ...                       |

Cada métrica se vincula a un objetivo GQM concreto.

## 3. Hoja PRAGMATIC

Estructura:

| ID_Metrica     | P | R | A | G | M | A2 | T | I | C | PRAGMATIC_SCORE |
|----------------|---|---|---|---|---|----|---|---|---|-----------------|
| M‑MAD‑SCORE    | 3 | 5 | 4 | 4 | 5 | 4  | 3 | 3 | 3 | =PROMEDIO(B2:J2) |
| M‑RISK‑TREATED | 4 | 5 | 5 | 4 | 4 | 4  | 4 | 3 | 3 | ...             |
| M‑TECH‑CRIT‑MTTR| 5| 5 | 5 | 4 | 4 | 4  | 4 | 3 | 3 | ...             |
| ...            |   |   |   |   |   |    |   |   |   |                 |

Opciones:

- Usar la media simple de los nueve criterios.  
- Excluir C (Cheap) o darle menor peso si se prefiere priorizar calidad sobre coste.

## 4. Hoja PONDERACIONES

Añadir, además de los pesos por bloque, un factor basado en PRAGMATIC:

| ID_Metrica     | Objetivo_GQM | Peso_GQM | PRAGMATIC_SCORE | Peso_final |
|----------------|-------------|----------|------------------|-----------|
| M‑RISK‑TREATED | G‑RISK‑1    | 0,25     | 4,3              | =0,25*(4,3/5) |
| M‑TECH‑CRIT‑MTTR| G‑TECH‑1   | 0,30     | 4,5              | =0,30*(4,5/5) |
| ...            | ...         | ...      | ...              | ...       |

La idea es que las métricas con mejor puntuación PRAGMATIC pesen más en el IGM, incentivando el uso de indicadores de alta calidad.

## 5. Hoja CALCULO_SUBINDICES

Para cada organización:

- Calcular los valores de cada métrica (por ejemplo, a partir de las respuestas de la encuesta o datos internos).  
- Normalizar, si procede, los valores a escala 0–1.  
- Agrupar por objetivo GQM (por ejemplo, G‑RISK‑1) usando los `Peso_final` de cada métrica.

Ejemplo de fórmula de subíndice:

`SUBINDICE_G_RISK_1 = SUMAPRODUCTO(Valores_normalizados_métricas_riesgo; Pesos_finales_riesgo) / SUMA(Pesos_finales_riesgo)`

## 6. Hoja CALCULO_IGM

Definir pesos por objetivo GQM (por ejemplo, más peso a G‑RISK‑1, G‑TECH‑1 y G‑INC‑1) y calcular el IGM:

`IGM = SUMAPRODUCTO(Subíndices_GQM; Pesos_objetivos)`

Transformar a porcentaje o a escala 1–5 según se prefiera para reporte.

## 7. Hoja DATOS_ECONOMICOS y CALCULO_ROI

Se mantiene el esquema ya propuesto:

- Coste de seguridad anual.  
- Pérdidas por incidentes.  
- Estimación de pérdidas evitadas.  
- Cálculo de ROI: `(Pérdidas evitadas - Coste seguridad) / Coste seguridad`.

Es posible conectar determinadas métricas GQM con el modelo económico (por ejemplo, MTTR reducido → menos horas de indisponibilidad → menos pérdidas), pero eso ya forma parte de un análisis coste‑beneficio más detallado.

## 8. Hoja CUADRO_MANDO

Debe mostrar:

- IGM y subíndices por objetivo GQM.  
- Perfil PRAGMATIC medio de las métricas utilizadas.  
- Relación entre IGM y indicadores económicos.  
- Segmentaciones por sector, tamaño, tipo de entidad, etc.

La idea es que la dirección pueda ver, de un vistazo, tanto el nivel de madurez como la “salud” del sistema de métricas que lo soporta.