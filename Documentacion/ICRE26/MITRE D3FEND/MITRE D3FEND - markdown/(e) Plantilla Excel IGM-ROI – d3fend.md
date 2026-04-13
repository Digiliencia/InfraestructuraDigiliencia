# (e) Plantilla de Excel para cálculo de IGM y ROI (descripción)

## 1. Estructura general del libro

Se propone un libro de Excel con las siguientes hojas:

1. Respuestas: volcado de las respuestas de cada organización.
2. Pesos_IGM: definición de pesos y escalas para el Índice Global de Madurez.
3. Cálculo_IGM: cálculo automático del IGM por organización.
4. Cálculo_ROI: estimación del ROI de iniciativas de seguridad.
5. Resumen_Sectorial: agregación de resultados por sector y tamaño.

## 2. Hoja "Respuestas"

Columnas sugeridas:

- ID_Organización
- Sector
- Tamaño
- Rol_Respondente
- P7 a P46 (codificación numérica de cada respuesta cerrada)

Las respuestas se codificarán en escalas numéricas; por ejemplo, en la pregunta 7 (conocimiento de D3FEND):

- 0 = Nunca lo he oído mencionar
- 1 = Me suena vagamente
- 2 = Lo conocen algunas personas clave
- 3 = Está integrado en algunos procesos
- 4 = Forma parte explícita de nuestra metodología

## 3. Hoja "Pesos_IGM"

Definir para cada bloque un peso relativo en el IGM:

- Adopción ATT&CK/D3FEND (P7–P11): peso 20 %.
- Modelado y CAD (P12–P15): peso 15 %.
- Cobertura ATT&CK–D3FEND (P16–P21): peso 20 %.
- Métricas operativas (P22–P29): peso 20 %.
- OT/ICS (P30–P32): peso 10 % (aplicable sólo a organizaciones OT).
- Integración normativa (P33–P35): peso 10 %.
- Gobierno y talento (P40–P43): peso 5 %.

Cada pregunta tendrá además un peso interno dentro de su bloque (por ejemplo, igualitario o ajustado según criterio experto).

## 4. Hoja "Cálculo_IGM"

Para cada organización:

1. Normalizar las respuestas de cada pregunta a una escala 0–1 (valor_respuesta / valor_máximo).
2. Calcular el promedio por bloque temático.
3. Multiplicar el promedio por el peso del bloque.
4. Sumar los resultados de todos los bloques para obtener el IGM en una escala 0–100.

Se pueden añadir:

- Rangos de madurez (por ejemplo, 0–20 muy bajo, 21–40 bajo, 41–60 medio, 61–80 alto, 81–100 muy alto).
- Visualizaciones (gráficos de radar por bloque, histogramas de IGM por sector).

## 5. Hoja "Cálculo_ROI"

Variables sugeridas:

- Coste_Proyecto: costes directos de un proyecto de seguridad (CAPEX + OPEX a 3–5 años).
- Reducción_MTTD: diferencia en MTTD antes/después del proyecto (minutos u horas).
- Reducción_MTTR: diferencia en MTTR.
- Reducción_Frecuencia: reducción estimada de número de incidentes anuales.
- Coste_Medio_Incidente: coste estimado (directo + indirecto) por incidente.

Cálculos básicos:

- Beneficio_Horas_Evitadas = (Reducción_MTTD + Reducción_MTTR) * Número_Incidentes * Coste_Medio_Hora_Impacto.
- Beneficio_Incidentes_Evitados = Reducción_Frecuencia * Coste_Medio_Incidente.
- Beneficio_Total = Beneficio_Horas_Evitadas + Beneficio_Incidentes_Evitados.
- ROI = (Beneficio_Total - Coste_Proyecto) / Coste_Proyecto.

Este enfoque puede refinarse con técnicas actuariales más sofisticadas, pero ofrece un punto de partida razonable para ligar métricas D3FEND (tiempos, frecuencias, coberturas) con resultados económicos.[web:5][web:18][web:21]

## 6. Hoja "Resumen_Sectorial"

Cálculos propuestos:

- IGM medio por sector.
- Distribución de IGM por tamaño de organización.
- Porcentaje de organizaciones que miden MTTD, MTTR, coberturas ATT&CK–D3FEND.[web:18][web:21]
- Gráficos comparativos entre sectores.

Esta hoja permite construir, casi sin querer, el argumento para políticas públicas, prioridades de inversión y, con un poco de suerte, alguna que otra reflexión incómoda en consejos de administración.