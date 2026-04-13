# Plantilla de Excel
## Cálculo del Índice Global de Madurez (IGM) y ROI de Cumplimiento

Este documento describe cómo estructurar una hoja de cálculo para:

1. Calcular el IGM a partir de las respuestas de la encuesta.
2. Estimar el ROI de iniciativas de seguridad y cumplimiento.

---

## 1. Estructura general del libro Excel

Se recomienda crear, como mínimo, las siguientes hojas:

- `Respuestas`
- `Escalas`
- `IGM`
- `ROI`

### 1.1. Hoja `Respuestas`

Columnas sugeridas:

- `A`: Nº de pregunta
- `B`: Código de pregunta (p. ej. GOB_1_1_1)
- `C`: Bloque (Gobernanza, Riesgo, etc.)
- `D`: Texto abreviado de la pregunta
- `E`: Respuesta seleccionada (texto)
- `F`: Valor numérico asignado (0–1)

Cada fila corresponde a una pregunta de la encuesta.

### 1.2. Hoja `Escalas`

Definir tablas de mapeo entre respuestas y valores:

Ejemplo tabla tipo (para preguntas de madurez con 5 opciones):

- Columna `A`: Bloque / Tipo de pregunta
- Columna `B`: Opción de respuesta (texto exacto)
- Columna `C`: Valor de madurez (0; 0,25; 0,5; 0,75; 1)

Para preguntas de porcentaje:

- `0–25 %` → 0,125
- `26–50 %` → 0,375
- `51–75 %` → 0,625
- `76–95 %` → 0,855
- `96–100 %` → 0,98

Usar `BUSCARV`/`XLOOKUP` para convertir texto en valor numérico.

---

## 2. Hoja `IGM` – Cálculo del Índice Global de Madurez

### 2.1. Definir pesos por bloque

Crear tabla:

- Columna `A`: Bloque (Gobernanza, Riesgo_EIPD, Medidas_Técnicas, Brechas, Terceros, Formación, Métricas, Resultados_Regulatorios, Innovación_IA)
- Columna `B`: Peso (suma 1)

Ejemplo:

- Gobernanza: 0,15
- Riesgo_EIPD: 0,15
- Medidas_Técnicas: 0,20
- Brechas: 0,15
- Terceros: 0,10
- Formación: 0,10
- Métricas: 0,10
- Resultados_Regulatorios: 0,03
- Innovación_IA: 0,02

### 2.2. Cálculo de medias por bloque

Por cada bloque:

- Filtrar filas de `Respuestas` por bloque.
- Calcular la media de la columna `F` (valor numérico).

Ejemplo de fórmula (si valores están en `Respuestas!F:F` y bloques en `Respuestas!C:C`):

```text
=PROMEDIO.SI(Respuestas!C:C;"Gobernanza";Respuestas!F:F)
```

Repetir para cada bloque.

### 2.3. Cálculo del IGM global

En la hoja `IGM`:

- Para cada bloque, multiplicar media del bloque × peso.
- Sumar todos los productos.

Ejemplo:

```text
=SUMA(Media_Gobernanza*Peso_Gobernanza;
      Media_Riesgo*Peso_Riesgo;
      ... ;
      Media_Innovacion*Peso_Innovacion)
```

Convertir el resultado a porcentaje (0–100 %) para presentación.

### 2.4. Niveles de madurez

Definir una tabla de interpretación:

- 0–24 %: Reactivo
- 25–49 %: Básico
- 50–69 %: Intermedio
- 70–84 %: Avanzado
- 85–100 %: Líder

Usar `SI` anidados o `BUSCARV` para devolver la etiqueta de nivel a partir del IGM.

---

## 3. Hoja `ROI` – Cálculo de retorno de la inversión

El ROI se calculará por iniciativa o conjunto de iniciativas.

### 3.1. Estructura de tabla por iniciativa

Columnas sugeridas:

- `A`: ID de iniciativa
- `B`: Descripción (p. ej. “Implantación de MFA completa”)
- `C`: Bloques afectados (p. ej. Medidas_Técnicas, Brechas)
- `D`: Coste de inversión inicial (CAPEX)
- `E`: Coste operativo anual (OPEX)
- `F`: Horizonte temporal (años)
- `G`: Probabilidad de incidente antes de la iniciativa
- `H`: Probabilidad de incidente después de la iniciativa
- `I`: Impacto medio de incidente (monetario)
- `J`: Nº esperado de incidentes antes (por año) = G * 1 (o volumen)
- `K`: Nº esperado de incidentes después (por año) = H * 1
- `L`: Coste esperado anual antes = J * I
- `M`: Coste esperado anual después = K * I
- `N`: Ahorro anual esperado = L – M
- `O`: Ahorro total horizonte = N * F
- `P`: Coste total horizonte = D + (E * F)
- `Q`: ROI = (O – P) / P

### 3.2. Estimación de probabilidades e impactos

Las probabilidades y el impacto pueden basarse en:

- Históricos internos (nº de incidentes/año, coste medio). [web:12]
- Benchmarks sectoriales (informes de brechas y costes). [web:12]
- Juicio experto (consenso de CISO, DPO, Riesgos).

Ejemplo sencillo:

- Antes de MFA: probabilidad anual de intrusión con acceso a datos = 0,20.
- Después de MFA: probabilidad reducida a 0,05.

Con un impacto medio estimado de 500.000 €, el ahorro anual esperado
es significativo.

### 3.3. Relación con el IGM

Opcionalmente, se puede:

- Registrar el IGM antes y después de la iniciativa.
- Estimar cuánto aumenta el IGM por bloque.
- Relacionar aumento de IGM con reducción de riesgo y ROI.

Esto permite construir narrativas del tipo:
“Un aumento de 0,15 puntos en madurez de Medidas Técnicas se traduce
en una reducción del 40 % en la probabilidad de incidentes críticos.”

---

## 4. Visualizaciones recomendadas

En la hoja `IGM`:

- Gráfico radar con madurez por bloque.
- Barras comparando IGM por unidades de negocio o años.
- Semáforos por bloque (rojo/ámbar/verde).

En la hoja `ROI`:

- Barras comparando ROI por iniciativa.
- Curva de ahorro acumulado vs costes acumulados.

---

## 5. Notas prácticas

- Documentar en una pestaña `Supuestos` las fuentes de datos para impactos y probabilidades.
- Versionar el libro (v1, v2, etc.) para evitar arqueología Excel.
- Recordar que toda cifra de ROI es una simplificación, no un oráculo.