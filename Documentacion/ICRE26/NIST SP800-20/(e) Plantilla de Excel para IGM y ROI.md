# Plantilla de Excel para Cálculo de IGM y ROI

## 1. Hoja "DatosEncuesta"

Columnas sugeridas:
- ID_Organizacion
- Sector
- Tamano
- Rol_Respondente
- P2_1, P2_2, ..., P10_5 (cada pregunta codificada numéricamente)
- Comentarios

## 2. Hoja "Codificacion"

Definir la correspondencia entre respuestas y valores numéricos para cada pregunta.

Ejemplo:
- Para respuestas tipo madurez (No, Parcial, Definido, Gestionado): 0, 1, 2, 3
- Para escalas 1-5: usar directamente 1-5

## 3. Hoja "IGM"

Construir el Índice Global de Madurez (IGM) como suma ponderada (o media ponderada) de varios subíndices:

- Gobernanza (por ejemplo, P2_1 a P2_6)
- Controles e incidentes (P4_x, P5_x, P6_x)
- Cultura y capacidad (P7_x)
- Riesgo e impacto (P8_x)

Cada subíndice puede definirse como:

IGM_Gobernanza = PROMEDIO(P2_1: P2_6 normalizados)

El IGM total puede definirse como:

IGM_Total = 0,25 * IGM_Gobernanza + 0,35 * IGM_Controles + 0,20 * IGM_Cultura + 0,20 * IGM_Riesgo

## 4. Hoja "ROI"

Para cada organización, recoger:
- Coste_Anual_Ciberseguridad
- Perdidas_Incidentes_Anuales (estimadas)
- Perdidas_Incidentes_Escenario_Sin_Mejora (modelo)

Definir:

- Reduccion_Perdidas = Perdidas_Incidentes_Escenario_Sin_Mejora - Perdidas_Incidentes_Anuales
- ROI_Simple = (Reduccion_Perdidas - Coste_Anual_Ciberseguridad) / Coste_Anual_Ciberseguridad

Se pueden añadir variantes, como:
- ROI_Ajustado_Riesgo, incorporando probabilidad de escenarios
- Payback (años necesarios para "amortizar" inversiones)

## 5. Hoja "CuadrosMando"

Incluir gráficos y tablas dinámicas que muestren:
- Distribución del IGM por sector
- Relación entre IGM y número de incidentes
- Relación entre IGM y porcentaje de presupuesto de TI dedicado a ciberseguridad
- Relación entre IGM y ROI estimado