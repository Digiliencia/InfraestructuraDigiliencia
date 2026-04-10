# Plantilla de Excel para cálculo de IGM y ROI SASE (descripción técnica)

> Especificación en Markdown de una hoja de cálculo diseñada para implementar el Índice Global de Madurez (IGM) y el cálculo de ROI asociado a SASE.

---

## 1. Estructura general del libro de Excel

Se recomienda un libro con, al menos, las siguientes hojas:

1. **"Respuestas"**: volcado de las respuestas de la encuesta (una fila por organización, una columna por pregunta).
2. **"IGM"**: cálculos del Índice Global de Madurez por dimensión y total.
3. **"ROI"**: modelo de costes, beneficios y cálculo de ROI.
4. **"Parámetros"**: ponderaciones, escalas, factores económicos (coste medio de incidente, hora de trabajo, etc.).

---

## 2. Hoja "Respuestas"

Cada fila representa una organización encuestada. Cada columna representa una pregunta codificada.

### 2.1. Columnas mínimas

- `ID_Org` – Identificador único de organización.
- `Sector` – Sector principal (texto o código).
- `Tamano` – Tamaño (categoría G4).
- `Teletrabajo` – Categoría G5.
- `A1`…`H4` – Respuestas codificadas a preguntas cerradas (se recomienda usar valores 1–4 para escalas ordinales).
- `O1`…`O5` – Respuestas abiertas (texto libre), no usadas en cálculos automáticos.

Ejemplo de codificación para respuestas tipo 0–25/26–50/51–75/76–100:

- 1 → 0–25 %.
- 2 → 26–50 %.
- 3 → 51–75 %.
- 4 → 76–100 %.

---

## 3. Hoja "Parámetros"

### 3.1. Ponderaciones del IGM

Tabla sugerida:

| Dimensión                           | Peso sugerido |
|-------------------------------------|---------------|
| Arquitectura SASE/SSE              | 0,20          |
| Identidad y Zero Trust             | 0,20          |
| Rendimiento y experiencia (QoE)    | 0,15          |
| Seguridad, detección y respuesta   | 0,15          |
| Cumplimiento ENS/NIS2 y gobierno   | 0,15          |
| Continuidad de negocio y resiliencia | 0,10        |
| Indicadores de negocio y ROI       | 0,05          |

### 3.2. Mapeo de preguntas a dimensiones

- Arquitectura SASE/SSE → A1, A2, A3, A4.
- Identidad y Zero Trust → B1, B2, B3, B4, B5.
- Rendimiento y experiencia → C1, C2, C3, C4.
- Seguridad, detección y respuesta → D1, D2, D3, D4, D5.
- Cumplimiento ENS/NIS2 y gobierno → E1, E2, E3, E4, F3, F4.
- Continuidad de negocio y resiliencia → G1, G2, G3.
- Indicadores de negocio y ROI → H1, H2, H3, H4, F1, F2.

### 3.3. Parámetros económicos (ejemplos)

- `CosteIncidenteMayor` – coste medio estimado de un incidente mayor (en euros).
- `CosteHoraTrabajo` – coste medio horario de un empleado afectado.
- `IncidentesAnuales` – incidentes anuales antes de SASE.
- `ReduccionIncidentes` – porcentaje estimado de reducción de incidentes gracias a SASE.
- `HorasAhorroOperativo` – horas de operación ahorradas al año por consolidación.
- `CosteLicenciasHeredadas` – coste anual de licencias sustituidas por SASE.

Estos parámetros se adaptarán a cada organización o estudio.

---

## 4. Hoja "IGM"

### 4.1. Cálculos por dimensión (por organización)

Suponiendo que la fila 2 de "Respuestas" es la primera organización, la lógica general puede ser:

1. Para cada dimensión, calcular la media simple de las respuestas (valores 1–4) de las preguntas asociadas.
2. Reescalar esa media al rango 0–100 con la fórmula:

- `IGM_Dimension = (MediaRespuestas - 1) / (4 - 1) * 100`.

Ejemplo en Excel (para Arquitectura SASE/SSE):

- En `IGM!B2`: `=PROMEDIO(Respuestas!A1_Org:A4_Org)` (sustituir por las celdas que contienen A1:A4 codificadas).
- En `IGM!C2`: `=((B2-1)/3)*100` → valor 0–100 para Arquitectura.

(En práctica, se utilizarán referencias explícitas, p.ej. `Respuestas!E2:H2` para A1:A4).

### 4.2. Cálculo del IGM total

Suponiendo:

- `IGM_Arq` en columna C.
- `IGM_IdZt` en D.
- `IGM_QoE` en E.
- `IGM_Sec` en F.
- `IGM_Cumpl` en G.
- `IGM_Cont` en H.
- `IGM_Neg` en I.

Y pesos en hoja "Parámetros" (`Parámetros!B2:B8`), la fórmula podría ser:

- En `IGM!J2`: `=C2*Parámetros!B2 + D2*Parámetros!B3 + E2*Parámetros!B4 + F2*Parámetros!B5 + G2*Parámetros!B6 + H2*Parámetros!B7 + I2*Parámetros!B8`.

Se recomienda dividir entre la suma de pesos (siempre 1, si no se han modificado) para mantener el rango 0–100.

### 4.3. Agregados

- Promedios de IGM por sector, tamaño, tipo de organización, etc. usando tablas dinámicas.

---

## 5. Hoja "ROI"

### 5.1. Estructura básica

Se proponen las siguientes secciones (filas o bloques):

1. **Costes anuales asociados a SASE**:
   - Licencias SASE/SSE/SD‑WAN.
   - Proyectos de implantación y migración.
   - Costes de operación (FTE dedicados, soporte, formación).
   - Otros costes (consultoría, auditoría específica, etc.).

2. **Beneficios anuales “duros” (ahorros directamente cuantificables)**:
   - Licencias heredadas evitadas (firewalls, VPN, proxies, etc.).
   - Ahorro en enlaces WAN y equipamiento de red.
   - Reducción de horas de operación y soporte (consolidación, automatización).

3. **Beneficios anuales “blandos” (coste evitado y productividad)**:
   - Reducción de incidentes mayores (número * coste medio de incidente).
   - Reducción de tiempo de inactividad (horas * coste hora de trabajo * número de usuarios afectados).
   - Mejora de productividad de usuarios remotos (horas/año ganadas por persona * número de usuarios * coste hora).

### 5.2. Celdas y fórmulas orientativas

Supongamos:

- `ROI!B2:B10` → costes individuales; `ROI!B11` → `CostesTotales`.
- `ROI!C2:C10` → beneficios individuales; `ROI!C11` → `BeneficiosTotales`.

Fórmulas:

- `CostesTotales` (`ROI!B11`): `=SUMA(B2:B10)`.
- `BeneficiosTotales` (`ROI!C11`): `=SUMA(C2:C10)`.
- `ROI%` (`ROI!D11`): `=((C11-B11)/B11)*100`.

Ejemplos de cálculo de beneficios:

- Reducción de incidentes mayores: `=Parámetros!IncidentesAnuales * Parmetros!ReduccionIncidentes * Parmetros!CosteIncidenteMayor`.
- Reducción de tiempo de inactividad: `=HorasEvIt * Parmetros!CosteHoraTrabajo * UsuariosAfectados`.

### 5.3. Enlace con el IGM

Opcionalmente, se puede añadir una tabla que relacione rangos de IGM con supuestos de beneficios:

- IGM < 40 → beneficios moderados (modelo incipiente).
- IGM 40–70 → beneficios medios.
- IGM > 70 → beneficios altos (optimización y consolidación).

Esto permite construir escenarios (pesimista, base, optimista) de ROI según la madurez alcanzada.

---

## 6. Visualizaciones sugeridas

- **Gráfico radar** con las dimensiones del IGM (Arquitectura, Identidad, QoE, Seguridad, Cumplimiento, Continuidad, Negocio).
- **Barras apiladas** comparando CostesTotales vs. BeneficiosTotales.
- **Diagrama de dispersión** IGM total vs. ROI% para analizar la relación entre madurez y retorno.

---

## 7. Notas prácticas

- La plantilla está pensada para ser un **punto de partida**, no un dogma: ajuste rangos, ponderaciones y categorías a la realidad de su sector.
- Documente las hipótesis de coste evitado y productividad para que las discusiones con finanzas no se conviertan en debates teológicos.
- Revise anualmente parámetros económicos y pesos del IGM; SASE evoluciona, las amenazas también, y la hoja Excel debe seguirles el ritmo.