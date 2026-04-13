# Plantilla de Excel para cálculo de IGM y ROI (extensión GQM + PRAGMATIC)  
## Especificación técnica

---

## 1. Estructura de hojas

Se recomiendan las siguientes hojas:

1. `Respuestas` – Datos de la encuesta (preguntas) y codificación básica.  
2. `Métricas` – Cálculo de métricas M1.x, M2.x, M3.x a partir de respuestas.  
3. `PRAGMATIC` – Matriz de evaluación PRAGMATIC por métrica (opcionalmente fija).  
4. `IGM` – Cálculo de dimensiones GOV, RISK, REQ, MET, CAP e IGM global.  
5. `ROI` – Cálculo de costes, beneficios y ROI de requisitos de seguridad.  
6. `Parámetros` – Pesos de dimensiones, umbrales y constantes.

---

## 2. Hoja “Respuestas”

Columnas mínimas:

- `Org_ID` – Identificador anónimo de organización.  
- `Sector` – Categoría (NIS2, AA.PP., etc.).  
- `Tamano` – Tamaño.  
- Columnas de respuestas a la encuesta: `P1_1`, `P1_2`, … `P9_3`.  

Codificación:

- Cada celda de pregunta contiene un código numérico de opción (por ejemplo, 1–5).  
- Se pueden utilizar listas desplegables para garantizar consistencia.

---

## 3. Hoja “Métricas”

### 3.1. Derivación de métricas M1.x y M2.x

Se crean columnas calculadas por organización:

- `M1_1` Cobertura funciones críticas.  
- `M1_2` Cobertura amenazas alto impacto.  
- `M1_3` % requisitos bien formados.  
- `M1_4` % requisitos sin observaciones.  
- `M1_5` Iteraciones de revisión (media).  

- `M2_1` Activos críticos sin requisitos.  
- `M2_2` % riesgos alto impacto con requisito esencial.  
- `M2_3` % requisitos mapeados a normativa.  
- `M2_4` Frecuencia de revisión tras incidentes.  
- `M2_5` Índice de Gestión de Mandato (IGM).

Las fórmulas exactas dependerán de cómo se hayan codificado las respuestas. Por ejemplo:

```text
M1_1 = mapa(P3_1_val) a un porcentaje aproximado
```

Si se prefiere precisión, las organizaciones pueden introducir directamente porcentajes en columnas auxiliares (por ejemplo, `%funciones_con_req`) y usarlos en las fórmulas.

### 3.2. Métricas M3.x (económicas)

Columnas:

- `Coste_requisitos` (M3_1).  
- `Beneficios_incidentes` (M3_2).  
- `Beneficios_retrabajo` (M3_3).  
- `Beneficios_auditoria` (M3_4).  
- `Beneficios_total` = suma de anteriores.  
- `ROI` (M3_5) = `(Beneficios_total - Coste_requisitos) / Coste_requisitos`.  

La métrica M3_6 (correlación entre IGM y resultados) se calculará posteriormente a nivel agregado, no por fila.

---

## 4. Hoja “PRAGMATIC”

### 4.1. Tabla de criterios por métrica

Estructura:

| Métrica | P (Predictivo) | R (Relevante) | A (Accionable) | G (Genuino) | M (Significativo) | P2 (Preciso) | T (Oportuno) | I (Independiente) | C (Rentable) | Total |
|--------|-----------------|---------------|----------------|-------------|-------------------|--------------|--------------|-------------------|-------------|-------|

Se rellenan los valores 0–2 para cada métrica según la matriz PRAGMATIC. La suma `Total` se calcula con una simple suma de columnas.

### 4.2. Uso en selección de métricas

La hoja `Parámetros` puede incluir umbrales, por ejemplo:

- `PRAGMATIC_min_nucleo` = 15.

En la hoja `Métricas` o `IGM`, se puede usar una fórmula para marcar qué métricas pertenecen al cuadro de mando principal:

```text
Es_nucleo = SI(PRAGMATIC_Total >= PRAGMATIC_min_nucleo; "Sí"; "No")
```

---

## 5. Hoja “IGM”

### 5.1. Dimensiones

Se calculan cinco dimensiones por organización (como en el kit de encuesta):

- `GOV` – Gobernanza del proceso de requisitos.  
- `RISK` – Riesgos, activos y trazabilidad.  
- `REQ` – Cobertura y calidad de requisitos.  
- `MET` – Métricas y mejora continua.  
- `CAP` – Capacidades y cultura.

Cada dimensión es una media de las preguntas asociadas (transformadas a escala 0–100) o de métricas intermedias, según el nivel de refinamiento.

### 5.2. Cálculo genérico

Ejemplo:

```text
GOV_raw = PROMEDIO( P1_1_val : P1_6_val, P5_1_val : P5_4_val )
GOV = GOV_raw / 4 * 100
```

Sucesivamente para RISK, REQ, MET, CAP.

### 5.3. Cálculo del IGM

En `Parámetros` se definen pesos:

- `w_GOV`, `w_RISK`, `w_REQ`, `w_MET`, `w_CAP`.

En `IGM`:

```text
IGM = w_GOV*GOV + w_RISK*RISK + w_REQ*REQ + w_MET*MET + w_CAP*CAP
```

El resultado puede redondearse con `REDONDEAR(IGM; 1)`.

---

## 6. Hoja “ROI”

Además de los cálculos por organización:

- Se pueden incluir gráficos de dispersión ROI vs. IGM.  
- Tablas dinámicas por sector, tamaño, etc.  
- Escenarios (optimista, conservador, pesimista) mediante multiplicadores de beneficios almacenados en `Parámetros`.

---

## 7. Hoja “Parámetros”

Campos sugeridos:

- Pesos IGM: `w_GOV`, `w_RISK`, `w_REQ`, `w_MET`, `w_CAP`.  
- Umbral PRAGMATIC para métricas núcleo.  
- Factores escenario ROI (`factor_opt`, `factor_cons`, `factor_pes`).  
- Límites de clasificación de madurez (por ejemplo, 0–19, 20–39, etc.).

---

## 8. Consideraciones prácticas

- Es recomendable proteger fórmulas críticas para evitar ediciones accidentales.  
- Se pueden crear vistas específicas para organizaciones (solo su fila) y vistas agregadas para responsables nacionales.  
- Siempre que sea posible, automatice la carga de datos desde herramientas ALM o de gestión de requisitos, para reducir el coste de recopilación.

---