# Plantilla de Excel para Cálculo de IGM y ROI de Seguridad (ENS–INES)

> Descripción en Markdown de una hoja de cálculo lista para implementar en Excel (o equivalente).

---

## 1. Estructura general del archivo Excel

Se recomienda un libro con las siguientes hojas:

1. `Datos_Encuesta`: volcado estructurado de respuestas por organización.  
2. `IGM_Madurez`: cálculo del Índice Global de Madurez.  
3. `ROI_Seguridad`: estimaciones de retorno de inversión.  
4. `Cuadros_Mando`: tablas y gráficos resumen para reportes.  

---

## 2. Hoja `Datos_Encuesta`

Cada fila representa una organización (o unidad). Las columnas incluyen:

- Identificadores:  
  - `Org_ID`, `Nombre_Org`, `Sector`, `Tamaño`, `Categoria_Predominante_ENS`.  

- Variables de madurez (preguntas 36–42):  
  - `Mad_Riesgos`, `Mad_Identidades`, `Mad_Incidentes`, `Mad_Continuidad`, `Mad_Proveedores`, `Mad_Formacion`, `Mad_Metricas` (valores 1–5).  

- Recursos e inversión (preguntas 48–49):  
  - `Pct_Presupuesto_Seguridad` (en %).  
  - `FTE_Seguridad` (personas equivalentes a jornada completa).  

- Percepción de ROI (pregunta 51):  
  - `ROI_Percibido` (codificar: 1 = muy bajo, 2 = bajo, 3 = razonable, 4 = claramente positivo).  

- Métricas de incidentes (resumen opcional):  
  - `Num_Incidentes_Graves` (últimos 12 meses).  
  - `MTTD_Medio_Horas`, `MTTR_Medio_Horas`, `MTTR_Recuperacion_Horas` (si se dispone).  

Adicionalmente, se pueden importar otras respuestas que interesen al análisis (p. ej. existencia de política aprobada, uso de INES como herramienta de gestión).

---

## 3. Hoja `IGM_Madurez`

### 3.1. Cálculo de IGM por dominio

Para cada organización:

- `IGM_Riesgos` = `Mad_Riesgos`.  
- `IGM_Identidades` = `Mad_Identidades`.  
- `IGM_Incidentes` = `Mad_Incidentes`.  
- `IGM_Continuidad` = `Mad_Continuidad`.  
- `IGM_Proveedores` = `Mad_Proveedores`.  
- `IGM_Formacion` = `Mad_Formacion`.  
- `IGM_Metricas` = `Mad_Metricas`.  

Son simplemente las puntuaciones en escala 1–5; la utilidad está en compararlas entre organizaciones y en el tiempo.

### 3.2. Índice Global de Madurez (IGM_Global)

Se propone la siguiente fórmula base:

- `IGM_Global` = promedio ponderado de los siete dominios.  

Por ejemplo (en pseudofórmula Excel):

- `IGM_Global = (Mad_Riesgos + Mad_Identidades + Mad_Incidentes + Mad_Continuidad + Mad_Proveedores + Mad_Formacion + Mad_Metricas) / 7`.  

Opcionalmente, se pueden introducir ponderaciones (por ejemplo, valor doble para riesgos e incidentes) si así lo justifica la estrategia.

### 3.3. Clasificación por niveles

Se puede derivar una etiqueta cualitativa:

- 1.0–1.9: “Inicial”.  
- 2.0–2.9: “Básico”.  
- 3.0–3.4: “Intermedio”.  
- 3.5–4.4: “Avanzado”.  
- 4.5–5.0: “Líder / Optimizado”.

La hoja puede usar reglas de formato condicional (semáforos) para facilitar la lectura visual.

---

## 4. Hoja `ROI_Seguridad`

El objetivo es aproximar un ROI de seguridad a partir de:

- Inversión: porcentaje del presupuesto TIC y FTE dedicados.  
- Beneficios: incidentes evitados o mitigados, tanto en frecuencia como en impacto.

### 4.1. Variables básicas

Por organización:

- `Gasto_TIC_Total` (opcional, si se conoce).  
- `Gasto_Seguridad` = `Gasto_TIC_Total * Pct_Presupuesto_Seguridad`.  
- `Coste_Medio_Incidente_Grave` (estimado; se puede fijar un valor estándar sectorial).  
- `Num_Incidentes_Graves_Evitados` (estimación basada en comparativa histórica o benchmarking).  

Cuando no haya datos suficientes, se pueden definir escenarios:

- Conservador: se asume que la seguridad ha evitado X incidentes graves.  
- Moderado y agresivo: valores mayores de X.

### 4.2. Fórmulas de ROI

Se puede utilizar una forma básica:

- `Beneficio_Estimado` = `Num_Incidentes_Graves_Evitados * Coste_Medio_Incidente_Grave`.  
- `ROI_Basico` = `(Beneficio_Estimado - Gasto_Seguridad) / Gasto_Seguridad`.  

La hoja puede incluir también:

- `IGM_Global` (importado de la otra hoja) para explorar correlaciones entre madurez y ROI percibido.  
- Gráficos de dispersión (IGM vs. ROI) para ilustrar tendencias.

### 4.3. Integración con percepción de ROI

Usar `ROI_Percibido` como contraste:

- Ver si organizaciones con alto IGM tienden a percibir el ROI como más positivo.  
- Detectar casos con alta inversión pero baja percepción de retorno (o viceversa).

---

## 5. Hoja `Cuadros_Mando`

Esta hoja puede incluir:

- Gráfico de distribución de IGM_Global por sector y tamaño.  
- Gráfico de radar de madurez por dominio para una organización tipo.  
- Gráficos de barras de porcentaje de presupuesto en seguridad por grupo.  
- Gráficos de dispersión entre `IGM_Global` y `Num_Incidentes_Graves` o `ROI_Basico`.

---

## 6. Notas prácticas

- No es necesario disponer de todos los datos para empezar; la plantilla debe tolerar celdas vacías.  
- Conviene documentar claramente cualquier supuesto (por ejemplo, coste medio de incidente).  
- La plantilla puede evolucionar a medida que la organización disponga de métricas más precisas (especialmente si integra datos de INES y de herramientas de gestión de incidentes).

> La idea no es reducir la ciberseguridad a un par de celdas mágicas, sino poner números razonables donde antes solo había impresiones vagas.