# Plantilla Excel – IGM + ROI con enfoque GQM/PRAGMATIC

## 1. Hojas recomendadas

1. `Catalogo_Metricas` – definición de M1–M16 y puntuaciones PRAGMATIC.  
2. `Datos_Tecnicos` – valores de cada métrica para la entidad (y, opcionalmente, para años previos).  
3. `IGM_Dominios` – cálculo del Índice Global de Madurez por dominio G1–G5.  
4. `ROI_TLPT` – cálculo económico de ROI basado en M14–M16.  
5. `PRAGMATIC_Score` (opcional) – evaluación de calidad de cada métrica.

## 2. Hoja `Catalogo_Metricas`

Columnas sugeridas:

- `ID_Metrica` (M1, M2, …, M16).  
- `Nombre_Metrica` (texto breve).  
- `Goal` (G1–G5).  
- `Dominio` (Cobertura, Metodología, Operaciones, Remediación, Gobernanza, Economía).  
- `Definicion` (resumen operativo).  
- `Unidad`.  
- `PRAGMATIC_P`, `PRAGMATIC_R`, `PRAGMATIC_A`, `PRAGMATIC_G`, `PRAGMATIC_M`, `PRAGMATIC_P2`, `PRAGMATIC_T`, `PRAGMATIC_I`, `PRAGMATIC_C` (0–3).  

Con estos campos es posible:

- Documentar claramente cada métrica.  
- Analizar qué métricas conviene priorizar (más puntuación PRAGMATIC global).

## 3. Hoja `Datos_Tecnicos`

Columnas sugeridas:

- `ID_Metrica`.  
- `Periodo` (Año, ciclo TLPT, etc.).  
- `Valor_Bruto` (p.ej. 0,75; 12 horas; 40 %).  
- `Valor_Normalizado_0_100` (si aplica).  
- `Goal` (referencia a `Catalogo_Metricas`).  
- `Dominio`.

Ejemplo de normalización para métricas de tipo “más alto = mejor”:

- `Valor_Normalizado_0_100 = (Valor_Bruto / Valor_Objetivo) * 100`, truncando en 100.

Para métricas de tipo “más bajo = mejor” (ej. MTTD, MTTR, nº hallazgos):

- `Valor_Normalizado_0_100 = (Valor_Objetivo / Valor_Bruto) * 100`, con tope en 100, y ajustes de mínimos.

## 4. Hoja `IGM_Dominios`

Columnas sugeridas:

- `Dominio` (Cobertura, Metodología, Operaciones, Remediación, Gobernanza, Economía).  
- `Peso_Dominio` (suma 1, p.ej.: Cobertura 0,15; Metodología 0,15; Operaciones 0,25; Remediación 0,2; Gobernanza 0,15; Economía 0,10).  
- `Puntuacion_Media_0_100` (promedio de `Valor_Normalizado_0_100` de las métricas del dominio).  
- `Contribucion_IGM` = `Peso_Dominio * Puntuacion_Media_0_100`.

`IGM_Global` = suma de `Contribucion_IGM` (0–100).

Con este enfoque, G1–G5 se materializan a través de dominios y métricas concretas.

## 5. Hoja `ROI_TLPT`

Entrada:

- `Costo_Ejercicio` (coste del TLPT: proveedores, dedicación interna).  
- `Costo_Remediacion` (coste de las acciones derivadas del TLPT).  
- `Beneficios_Economicos` = `Perdidas_Previstas_Evitadas + Ahorros_Regulatorios` (vinculado con M15).  
- `Periodo_Analisis` (años para los que se estima la reducción de pérdidas).

Cálculos básicos:

- `Coste_Total` = `Costo_Ejercicio + Costo_Remediacion`.  
- `ROI_TLPT` (M16) = `(Beneficios_Economicos - Coste_Total) / Coste_Total`.

Se puede añadir:

- `Payback` (años para recuperar el coste).  
- Escenarios optimista / base / conservador, con diferentes supuestos sobre pérdidas evitadas.

## 6. Hoja `PRAGMATIC_Score` (opcional)

- Calcular para cada métrica la media de sus puntuaciones PRAGMATIC (0–3).  
- Usar un gráfico de burbujas o radar para visualizar qué métricas son más robustas.  
- Decidir, por ejemplo, que solo se usarán para reporting ejecutivo aquellas métricas con media PRAGMATIC ≥ 2.
