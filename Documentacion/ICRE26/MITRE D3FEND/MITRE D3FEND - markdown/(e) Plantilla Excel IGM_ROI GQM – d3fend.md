# (e) Plantilla de Excel para cálculo de IGM y ROI basada en GQM + PRAGMATIC

## 1. Hojas propuestas

1. Definición_Métricas: listado de métricas (M1.x–M5.x) con definición, fórmula y ponderaciones GQM/PRAGMATIC.
2. Datos_Organización: valores de métricas por organización.
3. Cálculo_IGM: cálculo del Índice Global de Madurez a partir de métricas ponderadas.
4. Cálculo_ROI: estimación de retorno de inversión ligada a mejoras en métricas clave.
5. Resumen_Sectorial: agregados por sector, tamaño y ámbito.

## 2. Hoja "Definición_Métricas"

Columnas sugeridas:

- Código_Métrica (M1.1, M2.1, etc.).
- Descripción.
- Fórmula de cálculo.
- Unidad (%, minutos, horas, índice 0–1, etc.).
- Objetivo_GQM (G1–G5).
- Peso_en_IGM (0–1).
- PRED, REL, ACC, GEN, SIG, PRE, OPO, IND, REN (valores 1–5).

Los pesos en el IGM pueden asignarse, por ejemplo:

- Cobertura (M1.x): 30 % del IGM.
- Latencia (M2.x): 25 %.
- Eficacia (M3.x): 15 %.
- Telemetría (M4.x): 15 %.
- OT/ICS (M5.x): 15 % (aplicable sólo a organizaciones OT).[web:5][web:18][web:21]

## 3. Hoja "Datos_Organización"

Columnas por organización:

- ID_Organización.
- Sector.
- Tamaño.
- Ámbito.
- Valores de M1.1 a M5.4 según aplique.

Cada métrica se introduce en su unidad nativa (porcentajes, tiempos, tasas), y se normaliza en la hoja de cálculo del IGM.

## 4. Hoja "Cálculo_IGM"

Para cada organización:

1. Normalizar cada métrica a un rango 0–1 (por ejemplo, aplicando funciones de valor donde valores más altos son mejores, salvo en tiempos donde se invierte la escala).
2. Multiplicar cada métrica normalizada por su peso en el IGM.
3. Sumar las métricas ponderadas para obtener un IGM en escala 0–100.

Puede incluirse un desglose por familia:

- IGM_Cobertura.
- IGM_Latencia.
- IGM_Eficacia.
- IGM_Telemetría.
- IGM_OT.

## 5. Hoja "Cálculo_ROI"

Se reutilizan variables del diseño anterior (coste de proyectos, reducción de MTTD/MTTR, reducción de incidentes, coste medio de incidente), con un matiz: se puede asociar cada iniciativa a las métricas que impacta.

Por ejemplo:

- Proyecto A (mejora de detección endpoint): impacto esperado en M1.1, M2.1, M2.3.
- Proyecto B (instrumentación OT): impacto esperado en M4.1, M5.1, M5.2.

El ROI se calcula como:

- Beneficio_Horas_Evitadas = (Reducción_MTTD + Reducción_MTTR) * Número_Incidentes * Coste_Medio_Hora_Impacto.
- Beneficio_Incidentes_Evitados = Reducción_Frecuencia * Coste_Medio_Incidente.
- Beneficio_Total = Beneficio_Horas_Evitadas + Beneficio_Incidentes_Evitados.
- ROI = (Beneficio_Total - Coste_Proyecto) / Coste_Proyecto.

Se añade, además, un campo ∆IGM por iniciativa (incremento esperado del IGM) para valorar proyectos no sólo por retorno económico, sino por mejora global de madurez.[web:5][web:18][web:21]

## 6. Hoja "Resumen_Sectorial"

Proporciona, para cada sector y tamaño de organización:

- IGM medio y distribución.
- Valores medios de las métricas clave (M1.1, M2.1, M5.1, etc.).
- Porcentaje de organizaciones por rango de IGM.

Esta hoja alimenta directamente el reporte ejecutivo y puede convertirse en la base de indicadores nacionales o sectoriales de resiliencia.[web:17][web:20][web:23]