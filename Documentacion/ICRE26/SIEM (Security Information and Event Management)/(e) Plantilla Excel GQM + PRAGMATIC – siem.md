# Plantilla de Excel para GQM + PRAGMATIC, IGM y ROI

> Descripción estructurada para implementar el modelo en Excel/LibreOffice.

---

## 1. Estructura del libro

Hojas recomendadas:

1. `Objetivos_GQM`
2. `PRAGMATIC`
3. `IGM`
4. `ROI`

---

## 2. Hoja `Objetivos_GQM`

Cada fila representa una métrica derivada de un objetivo y una pregunta.

Columnas sugeridas:

- `ID_G` – p. ej., G1, G2…
- `Descripcion_G`
- `ID_Q` – p. ej., Q1.1, Q1.2…
- `Descripcion_Q`
- `ID_M` – p. ej., M1.1, M2.3…
- `Descripcion_M`
- `Formula_M` – descripción en texto de cómo se calcula.
- `Unidad` – minutos, %, €, etc.
- `Fuente_Datos` – SIEM, ticketing, CMDB, herramienta de riesgo.
- `Periodicidad` – diaria, semanal, mensual, trimestral.

---

## 3. Hoja `PRAGMATIC`

Cada fila es una métrica (ID_M).

Columnas:

- `ID_M`
- `Descripcion_M`
- `P_Predictivo` (0–3)
- `R_Relevante` (0–3)
- `A_Accionable` (0–3)
- `G_Genuino` (0–3)
- `M_Significativo` (0–3)
- `P2_Preciso` (0–3)
- `T_Oportuno` (0–3)
- `I_Independiente` (0–3)
- `C_Rentable` (0–3)
- `Score_Total` = SUMA de los 9 criterios.
- `Seleccionada_KPI` – Sí/No según umbral definido (por ejemplo, Score_Total ≥ 18).

Opcional:

- `Comentario` – justificación cualitativa de las puntuaciones.

---

## 4. Hoja `IGM`

Objetivo: calcular índices de madurez usando solo métricas con buena puntuación PRAGMATIC.

### 4.1 Entradas

- Referencias a las métricas (ID_M) seleccionadas como KPI.
- Valores de dichas métricas por organización (pueden provenir de la hoja de datos de la encuesta).

### 4.2 Cálculos

Definir subíndices (columnas):

- `IGM_G1` – madurez ligada a objetivos de detección/respuesta.
- `IGM_G2` – madurez en cumplimiento de notificación.
- `IGM_G3` – madurez en calidad y cobertura.
- `IGM_G4` – madurez en IA/automatización.
- `IGM_G5` – madurez en integración con riesgo/ROI.

Para cada subíndice:

- Normalizar las métricas a una escala 0–5 o 0–100.
- Calcular una media ponderada de las métricas seleccionadas.

IGM global por organización:

```text
IGM_Global = (IGM_G1*w1 + IGM_G2*w2 + IGM_G3*w3 + IGM_G4*w4 + IGM_G5*w5) /
             (w1 + w2 + w3 + w4 + w5)
```

donde `w1…w5` son pesos configurables.

---

## 5. Hoja `ROI`

Recicla la estructura de ROI de la plantilla anterior, añadiendo referencia a métricas GQM + PRAGMATIC.

Columnas por organización:

- `Coste_Total_SIEM_SOC_Anual`
- `Beneficio_Total_Estimado` (pérdidas evitadas + ahorro por reducción de tiempos).
- `ROI_Anual` = (`Beneficio_Total_Estimado` – `Coste_Total_SIEM_SOC_Anual`) / `Coste_Total_SIEM_SOC_Anual`.
- `Periodo_Retorno` (años).
- `Metricas_Clave_Respaldando_ROI` – listado de ID_M utilizados (M1.1, M2.2, M5.3, etc.).

---

## 6. Notas de implementación

- Mantener listas desplegables para ID_G, ID_Q, ID_M para evitar errores.
- Proteger las celdas de fórmulas críticas.
- Documentar en una hoja adicional (`Metodologia`) las definiciones exactas de cada métrica.

---

_Fin de la plantilla descriptiva._