# Plantilla Excel para Cálculo de IGM y ROI en Ciberseguridad

> Esta descripción está pensada para que puedas recrear el modelo en Excel (o similar) sin sobresaltos.

---

## 1. Estructura general del libro

Se recomienda un libro con, al menos, las siguientes hojas:

1. `Respuestas` – Volcado de las respuestas de la encuesta (por organización).  
2. `Ponderaciones` – Tabla de pesos por bloque y mapeo de respuestas a puntos.  
3. `IGM` – Cálculo del Índice Global de Madurez y de índices parciales.  
4. `ROI` – Cálculo de indicadores económicos y ROI.  
5. `Dashboards` – Gráficos y cuadros de mando ejecutivos.

---

## 2. Hoja “Respuestas”

Columnas principales:

- `Org_ID` – Identificador de la organización (o código anonimizado).  
- `Sector` – Sector principal.  
- `Tamaño` – Tramo de empleados.  
- Columnas para cada pregunta, por ejemplo:  
  - `Q1_1`, `Q1_2`, ..., `Q12_3`.

Cada `Qx_y` almacenará un **código numérico** que represente la opción elegida; por ejemplo:

- 0 = inexistente / mínimo.  
- 1, 2, 3, 4 = niveles crecientes de madurez o cobertura.

---

## 3. Hoja “Ponderaciones”

### 3.1. Tabla de puntuación de respuestas

Para cada pregunta:

- Columna `Pregunta` (ej. `Q1_1`).  
- Columna `Descripción breve`.  
- Columnas `Opción_0`, `Opción_1`, ... con su **puntuación** (0–4, 0–5, etc.).

Ejemplo:

| Pregunta | Opción | Descripción opción | Puntuación |
| --- | --- | --- | --- |
| Q4_2 | 0 | 0–20 % cuentas críticas con MFA | 0 |
| Q4_2 | 1 | 21–50 % | 1 |
| Q4_2 | 2 | 51–80 % | 2 |
| Q4_2 | 3 | 81–95 % | 3 |
| Q4_2 | 4 | 96–100 % | 4 |

### 3.2. Tabla de ponderaciones por bloque

Definir:

| Bloque | Código preguntas | Peso_Bloque |
| --- | --- | --- |
| Gobernanza | Q1_1–Q1_5 | 0,15 |
| Marcos | Q2_1–Q2_4 | 0,05 |
| Activos y vulnerabilidades | Q3_1–Q3_4 | 0,10 |
| Accesos | Q4_1–Q4_3 | 0,10 |
| Datos | Q5_1–Q5_4 | 0,10 |
| Monitorización y respuesta | Q6_1–Q6_4 | 0,15 |
| Formación y cultura | Q7_1–Q7_4 | 0,10 |
| Proveedores | Q8_1–Q8_3 | 0,10 |
| Documentación | Q9_1–Q9_3 | 0,05 |
| Métricas | Q10_1–Q10_3 | 0,05 |
| Inversión y ROI | Q11_1–Q11_3 | 0,05 |
| Percepción | Q12_1–Q12_3 | 0,0 (opcional, sólo analítica cualitativa) |

Los pesos pueden ajustarse según sector.

---

## 4. Hoja “IGM”

### 4.1. Cálculo de puntuación por pregunta

En esta hoja, mediante funciones `BUSCARV` / `XLOOKUP`, se traduce:

- `Qx_y (código)` → `Puntuación_Qx_y`.

Por ejemplo, en una columna `P_Q1_1`:

```text
=BUSCARV(Respuestas!Q1_1; Ponderaciones!Tabla_Puntuaciones;4;FALSO)
```

### 4.2. Cálculo de puntuación por bloque

Para cada bloque:

1. Calcular la **media de puntuación** de sus preguntas.  
2. Normalizar esa media a un rango 0–1 (por ejemplo, puntuación máxima teórica / real).

Ejemplo (bloque Gobernanza, 5 preguntas con máximo 4 puntos):

- `Punt_Gobernanza = PROMEDIO(P_Q1_1:P_Q1_5)`  
- `Norm_Gobernanza = Punt_Gobernanza / 4`

### 4.3. Cálculo del Índice Global de Madurez (IGM)

Para cada organización:

```text
IGM = SUMPRODUCT( {Norm_Gobernanza; Norm_Marcos; ...}; {Peso_Gobernanza; Peso_Marcos; ...} ) * 100
```

De este modo, `IGM` queda en escala 0–100.

### 4.4. Índices parciales

Definir, por ejemplo:

- `IGC` (Gobernanza y Cultura) = combinación de bloques 1, 2, 7, 10, 11.  
- `ITEC` (Técnico) = combinación de bloques 3, 4, 5, 6.  
- `ICAS` (Cadena de Suministro) = bloque 8.  
- `IRES` (Resiliencia) = bloques 6, 9, 10.

Cada uno se calcula con la misma lógica: media ponderada de bloques relevantes, escalada a 0–100.

---

## 5. Hoja “ROI”

### 5.1. Entradas necesarias

Por organización y periodo (ej. año):

- `IGM_t0` – IGM en el año base.  
- `IGM_t1` – IGM en el año actual.  
- `Coste_Ciber_t1` – Inversión en ciberseguridad en el periodo.  
- `Incidentes_t0`, `Incidentes_t1` – Número / coste de incidentes relevantes.  
- `Pérdidas_t0`, `Pérdidas_t1` – Coste económico de incidentes (en euros).  

Opcional:

- `Ciberseguro_prima_t0`, `Ciberseguro_prima_t1`.  
- `Ingresos_contratos_sensibles` (ej. contratos que exigen madurez mínima).

### 5.2. Cálculo de beneficios

Ejemplo de beneficios estimados:

- `Beneficio_Incidentes = Pérdidas_t0 - Pérdidas_t1` (si hay reducción).  
- `Beneficio_Seguro = Ciberseguro_prima_t0 - Ciberseguro_prima_t1` (si se reduce).  
- `Beneficio_Contratos = Incremento_neto_ingresos_en_contratos_vinculados_a_madurez`.

Beneficio total:

```text
Beneficio_Total = Beneficio_Incidentes + Beneficio_Seguro + Beneficio_Contratos
```

### 5.3. Cálculo de ROI

```text
ROI = (Beneficio_Total - Coste_Ciber_t1) / Coste_Ciber_t1
```

También puede expresarse en porcentaje:

```text
ROI_% = ROI * 100
```

### 5.4. Relación con el IGM

Se pueden construir gráficos que muestren:

- Evolución del IGM frente a la evolución de pérdidas e inversión.  
- Organizaciones con similar inversión pero diferente IGM (eficiencia relativa).  
- Sectores donde pequeñas mejoras de IGM producen grandes reducciones de pérdidas.

---

## 6. Hoja “Dashboards”

Se recomiendan gráficos como:

- Distribución del IGM por sector y tamaño.  
- Mapas de calor por bloque de madurez.  
- Dispersión IGM vs. pérdidas de incidentes.  
- Evolución temporal del IGM por organización o sector.

---

_Fin de la descripción de la plantilla Excel. El resto es cuestión de fórmulas, paciencia y algún café._