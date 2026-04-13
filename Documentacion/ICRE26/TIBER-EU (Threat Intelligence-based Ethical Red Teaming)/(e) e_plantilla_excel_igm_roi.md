# Plantilla de Excel para Cálculo de IGM y ROI  
## Diseño lógico para implementación en Excel/LibreOffice

---

## 1. Estructura de la hoja de cálculo

Se propone un libro con las siguientes hojas:

1. `DatosEncuesta` – Respuestas crudas por entidad.  
2. `Codificacion` – Tablas de mapeo de respuestas a valores 0–5.  
3. `IGM_Entidad` – Cálculo del Índice Global de Madurez por entidad.  
4. `IGM_Sector` – Agregados sectoriales.  
5. `ROI_TIBER` – Estimación de ROI.  

---

## 2. Hoja `DatosEncuesta`

### 2.1. Columnas básicas

- `Entidad_ID` – Código anonimizado de la entidad.  
- `Subsector` – Banca, seguros, mercado, proveedor, etc.  
- `Tamano` – Muy grande/Grande/Mediana/Pequeña.  

### 2.2. Columnas por pregunta

Una columna por cada ID de pregunta del modelo de encuesta, por ejemplo:

- `P2_1` – Inventario formal de CIFs (categoría textual).  
- `P2_2` – Madurez CIFs (0–5).  
- `P2_4` – Banda de % CIFs cubiertas.  
- `P3_3` – Alineamiento TTIR (0–5).  
- `P5_2` – Categoría MTTD.  
- `P5_3` – Categoría MTTR.  
- `P6_3` – % recomendaciones críticas implementadas.  
- etc.

Las respuestas abiertas pueden almacenarse, pero no se utilizan para los cálculos automáticos.

---

## 3. Hoja `Codificacion`

### 3.1. Mapas de categorías a valores

Ejemplo de tabla para `P2_4` (cobertura CIFs):

| Categoria_P2_4 | Valor_P2_4 |
|----------------|-----------|
| 0–20 % | 1 |
| 21–40 % | 2 |
| 41–60 % | 3 |
| 61–80 % | 4 |
| >80 % | 5 |

Ejemplo para categorías de MTTD (`P5_2`):

| Categoria_P5_2 | Valor_P5_2 |
|----------------|-----------|
| < 1 h | 5 |
| 1–24 h | 4 |
| 1–7 días | 3 |
| > 7 días | 2 |
| No detectado | 0 |

Cada categoría de pregunta se mapea a un valor numérico 0–5.

### 3.2. Fórmula tipo

En `IGM_Entidad`, para obtener el valor numérico, se usará una búsqueda:

```text
=BUSCARV(DatosEncuesta!C2; Codificacion!A:B; 2; FALSO)
```

(Adaptar rangos y funciones según idioma/configuración de Excel.)

---

## 4. Hoja `IGM_Entidad`

### 4.1. Dimensiones

Para cada entidad (fila), se definen columnas:

- `GOV` – Gobernanza y CIFs.  
- `TI` – Inteligencia de amenazas.  
- `RT` – Red Team y escenarios.  
- `BLUE` – Detección y respuesta.  
- `PRP` – Purple teaming y remediación.  
- `IGM_Total` – Índice Global de Madurez.

### 4.2. Cálculo por dimensión

Ejemplo de cálculo de `GOV`:

- `GOV` = media de valores numéricos asociados a: `P2_1`, `P2_2`, `P2_3`, `P2_4`, `P2_6`, `P6_5`.  

En Excel:

```text
=PROMEDIO(SI.ERROR({Valor_P2_1;Valor_P2_2;Valor_P2_3;Valor_P2_4;Valor_P2_6;Valor_P6_5}; ""))
```

(Usar celdas concretas según diseño; se pueden emplear rangos nombrados.)

### 4.3. Cálculo del IGM total

Asumiendo pesos iguales:

```text
= PROMEDIO(GOV; TI; RT; BLUE; PRP)
```

Si se desean pesos distintos:

```text
= (GOV*Peso_GOV + TI*Peso_TI + RT*Peso_RT + BLUE*Peso_BLUE + PRP*Peso_PRP) / SOMA_PESOS
```

Donde los pesos se definen en una pequeña tabla (por ejemplo, todos = 1).

---

## 5. Hoja `IGM_Sector`

### 5.1. Estadísticos básicos

- Media, mediana, desviación estándar para cada dimensión y para `IGM_Total`.  
- Desglose por subsector y tamaño usando tablas dinámicas.

### 5.2. Gráficos sugeridos

- Diagrama de caja (boxplot) de IGM por subsector.  
- Gráfico radar por dimensión para entidades representativas.  
- Gráfico de barras apiladas de % CIFs cubiertas.

---

## 6. Hoja `ROI_TIBER`

### 6.1. Datos de entrada

Por entidad:

- `Coste_TIBER` – Coste total del ejercicio (monetario).  
  - Desglose: coste proveedor TI, coste RTT, horas internas estimadas, otros.  
- `Reduccion_Probabilidad` – Estimación (%) de reducción en probabilidad de incidentes graves gracias a TIBER.  
- `Reduccion_Impacto` – Estimación (%) de reducción en impacto medio (económico) de incidentes.  
- `Riesgo_Base` – Estimación del riesgo anual esperado antes de TIBER (en unidades monetarias).  

### 6.2. Cálculos

1. **Riesgo Esperado tras TIBER**:

```text
= Riesgo_Base * (1 - Reduccion_Probabilidad) * (1 - Reduccion_Impacto)
```

2. **Beneficio Esperado**:

```text
= Riesgo_Base - Riesgo_Esperado_tras_TIBER
```

3. **ROI**:

```text
= (Beneficio_Esperado - Coste_TIBER) / Coste_TIBER
```

### 6.3. Interpretación

- ROI > 0: beneficios estimados > costes.  
- ROI entre 0 y -0,5: mejora relevante pero costosa; revisar supuestos.  
- ROI < -0,5: probablemente se están infravalorando beneficios o sobrevalorando costes (o la ejecución del ejercicio fue poco provechosa).

---

_Fin de la Plantilla Excel lógica._