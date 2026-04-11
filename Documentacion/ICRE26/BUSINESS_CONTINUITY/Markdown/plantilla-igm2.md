# Plantilla de Excel para cálculo de IGM nacional y ROI de programas de resiliencia

Esta plantilla conceptual describe cómo construir, en Excel (o herramienta equivalente), un **modelo de indicadores nacionales de BCM/ciber‑resiliencia** que permita:

- Calcular un **Índice Global de Madurez/Resiliencia (IGM)** del país o territorio.
- Calcular **Índices por Dimensión (ID)** (gobernanza, capacidades, rendimiento, impacto, ecosistema).
- Relacionar estos índices con un análisis básico de **ROI** de programas o iniciativas nacionales.

Los indicadores base son IND‑01 a IND‑14, definidos en el marco GQM.

---

## 1. Estructura propuesta del libro

Hojas recomendadas:

1. `Catalogo_Indicadores`
2. `Datos_Anuales`
3. `Calculos_Indices`
4. `ROI_Programas`
5. `Cuadro_Mando_Nacional`

Se pueden añadir hojas adicionales (por ejemplo, detalle por sector o CCAA) según necesidades.

---

## 2. Hoja «Catalogo_Indicadores»

Contiene la definición de cada indicador y su pertenencia a dimensiones de resiliencia.

Columnas sugeridas:

- `Codigo_IND`: IND-01, IND-02, …, IND-14.
- `Nombre_Corto`: título resumido del indicador.
- `Descripcion`: descripción algo más detallada.
- `Dimension`: GOV (gobernanza), CAP (capacidades), REND (rendimiento), IMP (impacto), ECO (ecosistema/cultura).
- `Fuente_Principal`: organismo responsable del dato.
- `Unidad`: %, días, nº, posición, índice, etc.
- `Escala_Referencia`: rango esperado (por ejemplo, 0–100, 0–10, «Tier 1–5»…).
- `Sentido`: `+` si más es mejor, `-` si menos es mejor.
- `Peso_Dimension`: peso del indicador dentro de su dimensión.
- `Peso_IGM`: peso del indicador dentro del índice global.

Ejemplo de filas:

| Codigo_IND | Nombre_Corto | Dimension | Fuente_Principal | Unidad | Sentido | Peso_Dimension | Peso_IGM |
|---|---|---|---|---|---|---|---|
| IND-01 | Estrategia nacional vigente | GOV | Presidencia / DSN | Binario (0/1) | + | 1 | 1 |
| IND-05 | % OSE con BCP probado | CAP | Autoridades NIS2 sectoriales | % | + | 2 | 3 |
| IND-08 | MTTR servicios esenciales | REND | Reguladores sectoriales / CERTs | Horas | - | 3 | 4 |

> Consejo: asignar pesos más altos a indicadores estructuralmente más relevantes (por ejemplo, IND‑05, IND‑06, IND‑08, IND‑11, IND‑14) y mantener suma de pesos por dimensión y global normalizada (por ejemplo, suma de `Peso_IGM` = 100).

---

## 3. Hoja «Datos_Anuales»

Recoge los valores de cada indicador por año, y opcionalmente por ámbito territorial (nacional, CCAA) o sector.

Columnas mínimas:

- `Anio`.
- `Ambito` (por ejemplo, ES‑Nacional, ES‑CCAA‑X, u otro código territorial).
- `Codigo_IND`.
- `Valor_Bruto` (valor numérico o codificado del indicador).

Columnas opcionales:

- `Fuente_Detalle` (enlace o referencia al informe que aporta el dato).
- `Calidad_Dato` (escala 1–3 o A/B/C para señalar confiabilidad).

Ejemplo:

| Anio | Ambito | Codigo_IND | Valor_Bruto |
|---|---|---|---|
| 2025 | ES-Nacional | IND-05 | 68,5 |
| 2025 | ES-Nacional | IND-08 | 5,2 |
| 2025 | ES-Nacional | IND-13 | 420 |

---

## 4. Hoja «Calculos_Indices»

Esta hoja transforma los valores brutos en **valores normalizados** y calcula:

- Índices por dimensión (`ID_GOV`, `ID_CAP`, `ID_REND`, `ID_IMP`, `ID_ECO`).
- Índice global (`IGM_Nacional`).

### 4.1. Normalización de indicadores

Se recomienda crear, en `Calculos_Indices`, una tabla que para cada combinación `Anio` + `Ambito` + `Codigo_IND` calcule:

- `Valor_Normalizado`: valor en una escala común (por ejemplo 0–100).

Estrategias de normalización típicas:

- Para indicadores «más es mejor» (%) o tasas:

  `Valor_Normalizado = MIN(Valor_Bruto, Umbral_Max) / Umbral_Max * 100`

- Para indicadores «menos es mejor» (por ejemplo, MTTR, días en modo degradado):

  `Valor_Normalizado = MAX(0; (Umbral_Max - Valor_Bruto) / (Umbral_Max - Umbral_Min)) * 100`

  Donde `Umbral_Min` sería el valor «ideal» (por ejemplo, 0 horas) y `Umbral_Max` el valor a partir del cual se considera inaceptable.

Los umbrales pueden definirse en una pequeña tabla de parámetros.

### 4.2. Cálculo de índices por dimensión

Para cada `Anio` + `Ambito` + `Dimension`:

- Índice de dimensión (por ejemplo, `ID_CAP`):

  `ID_CAP = SUMAPRODUCTO(Valor_Normalizado_IND_CAP; Peso_Dimension_IND_CAP) / SUMA(Peso_Dimension_IND_CAP)`

En pseudocódigo Excel:

```text
=SUMAPRODUCTO(
  (tblCalculos[Anio]=$A2)*
  (tblCalculos[Ambito]=$B2)*
  (tblCalculos[Dimension]="CAP")*
  tblCalculos[Valor_Normalizado]*
  tblCalculos[Peso_Dimension]
) /
SUMAPRODUCTO(
  (tblCalculos[Anio]=$A2)*
  (tblCalculos[Ambito]=$B2)*
  (tblCalculos[Dimension]="CAP")*
  tblCalculos[Peso_Dimension]
)
```

### 4.3. Cálculo del IGM nacional

Para cada `Anio` + `Ambito`:

- **Opción A – Media ponderada directa de todos los indicadores:**

```text
IGM = SUMAPRODUCTO(
  (tblCalculos[Anio]=$A2)*
  (tblCalculos[Ambito]=$B2)*
  tblCalculos[Valor_Normalizado]*
  tblCalculos[Peso_IGM]
) /
SUMAPRODUCTO(
  (tblCalculos[Anio]=$A2)*
  (tblCalculos[Ambito]=$B2)*
  tblCalculos[Peso_IGM]
)
```

- **Opción B – Media simple de los índices de dimensión:**

```text
IGM = PROMEDIO(ID_GOV; ID_CAP; ID_REND; ID_IMP; ID_ECO)
```

---

## 5. Hoja «ROI_Programas»

Relaciona iniciativas o programas nacionales (por ejemplo, nuevo CSIRT sectorial, plan de formación masiva, refuerzo ENS) con:

- Su coste estimado.
- Su impacto esperado en indicadores/índices.
- El ROI aproximado en términos de pérdidas evitadas.

Columnas sugeridas:

- `ID_Programa`.
- `Nombre_Programa`.
- `Descripcion_Breve`.
- `Dimension_Principal` (GOV, CAP, REND, IMP, ECO).
- `Indicadores_Impactados` (lista o códigos separados por comas: IND-05, IND-08, etc.).
- `Coste_Total` (en horizonte de análisis, p.ej. 3–5 años).
- `Beneficio_Economico_Estimado` (pérdidas evitadas en el mismo horizonte).
- `ROI` = `(Beneficio_Economico_Estimado - Coste_Total) / Coste_Total`.
- `Incremento_Esperado_IGM` (estimación cualitativa o cuantitativa tras la implantación).

La exactitud de los beneficios será siempre aproximada, pero el ejercicio ayuda a:

- Ordenar programas por impacto esperado en resiliencia vs. coste.
- Dar argumentos económicos a las priorizaciones políticas.

---

## 6. Hoja «Cuadro_Mando_Nacional»

Presenta de forma amigable los resultados para decisores.

Elementos recomendados:

1. **Visión global:**
   - Gráfico de barras o velocímetro con IGM por año.
   - Comparativa de IGM entre ámbitos (por ejemplo, nacional vs. CCAA).

2. **Desglose por dimensión:**
   - Gráfico radar con ID_GOV, ID_CAP, ID_REND, ID_IMP, ID_ECO.
   - Gráficos de columnas por dimensión mostrando evolución temporal.

3. **Indicadores clave:**
   - Tabla con IND‑05, IND‑06, IND‑08, IND‑11, IND‑14, resaltando valores actuales, objetivo y tendencia.

4. **Mapa territorial (si aplica):**
   - Mapa de CCAA coloreado por IGM o por algún índice de dimensión.

5. **Lista de programas prioritarios (de `ROI_Programas`):**
   - Ordenados por ROI o por impacto esperado en IGM.

---

## 7. Buenas prácticas de implementación

- **Trazabilidad:** usa referencias estructuradas (tablas con nombre, celdas con nombre) para que el libro sea mantenible.
- **Documentación:** añade una hoja `Notas_Metodologicas` con:
  - Definiciones de cada indicador.
  - Umbrales de normalización.
  - Fuentes de datos y sus limitaciones.
- **Gobernanza del dato:** acuerda quién es responsable de actualizar cada indicador, con qué frecuencia y bajo qué controles de calidad.
- **Versionado:** mantén control de versiones del fichero (o almacénalo en un repositorio) para poder reconstruir series históricas y cambios de metodología.

Con este diseño, el Excel deja de ser «otra hoja con números» y se convierte en un **instrumento de política pública**: conecta indicadores GQM con decisiones, y permite evaluar si el dinero invertido en resiliencia nacional se traduce en mejoras tangibles.
