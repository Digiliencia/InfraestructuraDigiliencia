# Plantilla Excel para cálculo de IGM y ROI bajo enfoque GQM + PRAGMATIC

Versión 1.0 – 2026

## 1. Estructura de la hoja de cálculo

Se recomienda estructurar el libro de trabajo en, al menos, las siguientes hojas:

1. `Meta_Diccionario` – Definición de objetivos GQM, métricas e IDs.  
2. `Datos_Organizaciones` – Respuestas y métricas calculadas por organización.  
3. `Ponderaciones` – Pesos por métrica y dimensión.  
4. `IGM_Resultados` – Cálculo de subíndices e IGM global.  
5. `ROI` – Cálculo del retorno de inversión basado en cambio de madurez y pérdida esperada.  
6. `Graficos` – Visualizaciones para informes y presentaciones.

## 2. Hoja “Meta_Diccionario”

Columnas sugeridas:

- `Objetivo_GQM` (p. ej. GOB-1, RIESGO-1).  
- `Metrica_ID` (p. ej. GOB-1.1.a).  
- `Descripción` (texto).  
- `Dominio` (Gobernanza, Riesgo, Cumplimiento, Cap+Res, Inversión).  
- `Unidad` (% org., nº sectores, etc.).  
- `Fuente` (Encuesta GRC, otras estadísticas).  
- `Normativa_relacionada` (resumen de mapeo).

Esta hoja sirve como diccionario de indicadores para mantener coherencia entre versiones.

## 3. Hoja “Datos_Organizaciones”

Cada fila representa una organización encuestada. Columnas:

- `ID_Org`  
- `Sector`  
- `Tamaño`  
- `Criticidad` (por ejemplo, 1–3 según NIS2).  
- Luego, una columna por métrica relevante, por ejemplo:

  - `GOB_1_1_a` – 1 si la organización tiene estrategia aprobada en últimos 3 años, 0 si no.  
  - `GOB_1_2_a` – 1 si CISO con acceso regular al consejo, 0 si no.  
  - `CAP_1_1_a` – 0–4 según nivel de cobertura MFA (segmentado y normalizado).  
  - Etc.

En muchos casos, la métrica será una transformación de respuestas de opción múltiple (por ejemplo, asignando puntajes).

## 4. Hoja “Ponderaciones”

Tabla con:

- `Metrica_ID`  
- `Dimension` (IG_GOB, IG_RIESGO, IG_CUMP, IG_CAPRES, IG_INV).  
- `Peso_en_dimension` (0–1, suma por dimensión = 1).  
- `Peso_global` (opcional).

Ejemplo:

| Metrica_ID | Dimension | Peso_en_dimension |
|------------|-----------|-------------------|
| GOB-1.1.a  | IG_GOB    | 0,25              |
| GOB-1.2.a  | IG_GOB    | 0,25              |
| GOB-1.3.a  | IG_GOB    | 0,50              |

Los pesos pueden ajustarse según relevancia normativa y PRAGMATIC.

## 5. Hoja “IGM_Resultados”

### 5.1. Cálculo de subíndices por dimensión

Para cada organización:

- Seleccionar las métricas asociadas a cada dimensión (según `Ponderaciones`).  
- Calcular subíndice como media ponderada:

`IG_GOB_raw = SUMPRODUCT(Valores_métricas_GOB; Pesos_métricas_GOB) / SUM(Pesos_métricas_GOB)`

Repetir para RIESGO, CUMP, CAPRES, INV.

### 5.2. Normalización

Definir, para cada dimensión, el valor máximo posible teórico (`Max_GOB`, etc.). Luego:

`IG_GOB = IG_GOB_raw * (100 / Max_GOB)`

De este modo, cada subíndice se expresa en escala 0–100.

### 5.3. Índice Global de Madurez (IGM)

Definir pesos para cada dimensión (por ejemplo):

- GOB: 20 %  
- RIESGO: 20 %  
- CUMP: 20 %  
- CAPRES: 30 %  
- INV: 10 %

Entonces:

`IGM = IG_GOB*0,2 + IG_RIESGO*0,2 + IG_CUMP*0,2 + IG_CAPRES*0,3 + IG_INV*0,1`

Esta fórmula puede ajustarse según prioridades nacionales o sectoriales.

## 6. Hoja “ROI”

### 6.1. Variables clave

Por organización y año (si se disponen datos longitudinales):

- `IGM_t0`, `IGM_t1` – Índices de madurez en dos momentos.  
- `Coste_Ciber_t0`, `Coste_Ciber_t1` – Coste anual de ciberseguridad.  
- `Incidentes_Graves_t0`, `Incidentes_Graves_t1` – Número y/o coste estimado de incidentes graves.  
- `ALE_t0`, `ALE_t1` – Pérdida anual esperada, si está disponible.

### 6.2. Modelo simple de beneficio

Cuando se dispone de ALE:

- `Beneficio = ALE_t0 – ALE_t1`  
- `Inversion = Coste_Ciber_t1 – Coste_Ciber_t0` (o solo Coste_Ciber_t1 si se analiza un año)  
- `ROI = (Beneficio – Inversion) / Inversion`

Cuando no se dispone de ALE, puede usarse un modelo aproximado:

- Suponer que un aumento ΔIGM reduce proporcionalmente la probabilidad de incidentes graves dentro de un rango prudente.  
- Estimar la pérdida media de un incidente grave a partir de históricos sectoriales.  
- Derivar un beneficio aproximado como `Beneficio ≈ ΔProbabilidad * L * Número_esperado_incidentes`.

### 6.3. Enfoques de sensibilidad

La hoja puede incluir tres escenarios (optimista, conservador, pesimista) ajustando:

- Probabilidad de incidentes.  
- Costes por incidente.  
- Relación entre IGM y probabilidad.

Los parámetros se concentran en una tabla de supuestos para facilitar su revisión.

## 7. Hoja “Graficos”

Gráficos recomendados:

- Barras: IGM medio por sector.  
- Dispersión: IGM vs. % presupuesto TIC en ciberseguridad.  
- Burbujas: criticidad vs. madurez vs. tamaño de organización.  
- Líneas: evolución temporal de IGM para organizaciones o sectores que repitan encuesta.

Estos gráficos alimentan directamente la plantilla de reporte ejecutivo.

## 8. Relación con GQM + PRAGMATIC

La plantilla de Excel no inventa métricas por su cuenta: solo implementa y agrega las definidas en el marco GQM y filtradas por PRAGMATIC. Toda nueva métrica que se quiera añadir debe estar primero descrita en `Meta_Diccionario` y mapeada normativamente, evitando así la proliferación de indicadores de dudosa utilidad.