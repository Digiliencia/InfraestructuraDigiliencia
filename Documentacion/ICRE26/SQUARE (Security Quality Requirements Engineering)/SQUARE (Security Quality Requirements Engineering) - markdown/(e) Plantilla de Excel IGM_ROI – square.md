# Plantilla de Excel para cálculo de IGM y ROI  
## Especificación para implementación

> Este documento describe la estructura recomendada de un libro Excel  
> que permita calcular automáticamente el Índice Global de Madurez (IGM)  
> y estimaciones de ROI asociadas a la ingeniería de requisitos de seguridad.

---

## 1. Estructura del libro

Se recomiendan las siguientes hojas:

1. `Respuestas` – Registro de respuestas codificadas por organización.  
2. `Codificación` – Tablas de mapeo entre opciones de respuesta y valores numéricos.  
3. `IGM` – Cálculo de dimensiones y del Índice Global de Madurez.  
4. `ROI` – Cálculo y escenarios de ROI.  
5. `Parametros` – Pesos, supuestos y constantes (costes, factores, etc.).

---

## 2. Hoja “Respuestas”

Columnas mínimas:

- `Org_ID` – Identificador anónimo de organización.  
- `Sector` – Sector según P0.1.  
- `Tamano` – Tamaño según P0.2.  
- `Ambito` – Ámbito geográfico según P0.3.  
- Columnas para cada pregunta cerrada: `P1_1`, `P1_2`, …, `P9_3`, etc.  

Cada celda debe contener el código de respuesta (por ejemplo, un número entero) según la hoja `Codificación`.

---

## 3. Hoja “Codificación”

Para cada pregunta, una pequeña tabla:

| Pregunta | Código opción | Descripción opción                                       | Valor numérico |
|----------|---------------|----------------------------------------------------------|----------------|
| P3_1     | 1             | > 90 %                                                   | 4              |
| P3_1     | 2             | 70–90 %                                                  | 3              |
| P3_1     | 3             | 40–69 %                                                  | 2              |
| P3_1     | 4             | 10–39 %                                                  | 1              |
| P3_1     | 5             | < 10 %                                                   | 0              |
| P3_1     | 9             | No se sabe                                               | (en blanco)    |

La implementación práctica puede hacerse con funciones de búsqueda (por ejemplo, `BUSCARV`/`XLOOKUP`), creando una columna derivada por cada pregunta en la hoja `Respuestas` con su valor numérico asociado.

---

## 4. Hoja “IGM”

### 4.1. Estructura básica

Para cada organización (fila de `Respuestas`), se crearán columnas:

- Valores numéricos por pregunta: `P1_1_val`, `P1_2_val`, etc.  
- Puntaciones de dimensión: `GOV`, `RISK`, `REQ`, `MET`, `CAP`.  
- `IGM` – Índice Global de Madurez.

### 4.2. Fórmulas ejemplo

Supongamos:  
- `GOV` se calcula como media de P1.1–P1.6 y P5.1–P5.4.  
- `RISK` a partir de P2.1–P2.5 y P6.1–P6.3.  
- `REQ` a partir de P3.1–P3.6.  
- `MET` a partir de P4.1–P4.5 y P8.3.  
- `CAP` a partir de P7.1–P7.3 y P9.1–P9.3.

Ejemplo de cálculo para GOV (en pseudo‑fórmula):

```text
GOV_raw = PROMEDIO( P1_1_val : P1_6_val, P5_1_val : P5_4_val )
GOV = GOV_raw / 4 * 100
```

(Asumiendo que el valor máximo posible para cada pregunta es 4.)

Ejemplo de IGM:

```text
IGM = 0,2*GOV + 0,25*RISK + 0,25*REQ + 0,15*MET + 0,15*CAP
```

Los pesos (0,2; 0,25; etc.) pueden referenciarse a celdas de la hoja `Parametros` para poder ajustarlos sin modificar fórmulas.

---

## 5. Hoja “ROI”

### 5.1. Datos de entrada

Por organización, se sugieren columnas:

- `Coste_requisitos` – Costes anuales estimados del proceso de requisitos de seguridad.  
- `Beneficios_incidentes` – Ahorros por incidentes evitados/mitigados.  
- `Beneficios_retrabajo` – Ahorros por reducción de retrabajo.  
- `Beneficios_auditoria` – Ahorros por auditorías/certificaciones más eficientes.  
- `Beneficios_total` – Suma de beneficios (columna calculada).  

### 5.2. Fórmulas

```text
Beneficios_total = Beneficios_incidentes + Beneficios_retrabajo + Beneficios_auditoria

ROI = (Beneficios_total - Coste_requisitos) / Coste_requisitos
```

Se pueden crear columnas de escenarios (optimista, conservador, pesimista) multiplicando los beneficios por factores almacenados en la hoja `Parametros`.

---

## 6. Hoja “Parametros”

Ejemplos de parámetros:

- Pesos de dimensiones: `w_GOV`, `w_RISK`, `w_REQ`, `w_MET`, `w_CAP`.  
- Factores para escenarios ROI: `Escenario_optimista`, `Escenario_conservador`, `Escenario_pesimista`.  
- Valores máximos posibles por dimensión, si difieren del estándar.

---

## 7. Visualizaciones recomendadas

Aunque no se incluyen directamente en esta especificación, se sugieren:

- Gráficos radar para comparar dimensiones del IGM por organización o sector.  
- Histogramas del IGM global.  
- Diagramas de dispersión (IGM vs. número de incidentes, IGM vs. ROI, etc.).  

El objetivo es permitir que un tablero de mando resuma, a golpe de vista, quién está en el “lejano oeste digital” y quién se acerca al “monasterio cartujo”.

---