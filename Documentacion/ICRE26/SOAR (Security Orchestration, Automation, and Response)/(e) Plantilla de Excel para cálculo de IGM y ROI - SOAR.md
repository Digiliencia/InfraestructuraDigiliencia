# Plantilla para Excel – Cálculo de IGM (Indicador Global de Madurez) y ROI de SOAR

## 1. Estructura de hojas

Se recomiendan al menos 3 hojas:

1. **RESUMEN** – Resultados agregados (IGM, ROI estimado, semáforos).  
2. **DATOS_ENCUESTA** – Registro de respuestas por organización.  
3. **CALCULOS** – Cálculo de puntuaciones por eje e indicadores derivativos.

## 2. Hoja DATOS_ENCUESTA

Columnas sugeridas (cada fila = una organización):

- `ID_ORG`
- `Sector`
- `Tamaño`
- `Tipo_Org` (público/privado, NIS2/ENS)
- `P5_Estrategia_SOAR` … `P40_IA`
- Campos codificados según las opciones de respuesta (por ejemplo, 1–5).

Ejemplo de codificación:

- P37 (madurez)  
  - Inicial → 1  
  - Básico → 2  
  - Intermedio → 3  
  - Avanzado → 4  
  - Líder → 5

- P18 (impacto MTTD/MTTR)  
  - Empeoramiento → 1  
  - Mejora < 10 % → 2  
  - Mejora 10–30 % → 3  
  - Mejora 30–50 % → 4  
  - Mejora > 50 % → 5

## 3. Hoja CALCULOS

### 3.1. Ejes de madurez (0–100)

Defina columnas para cada eje:

- `Gobierno_Estrategia`  
- `Operacion_Cobertura`  
- `Metricas_Calidad`  
- `Regulacion_Reporting`  
- `Impacto_ROI`  
- `Futuro_Innovacion`

Ejemplo de construcción (pseudo‑fórmula):

- `Gobierno_Estrategia` = PROMEDIO( P5, P7, P8 ) normalizado a 0–100.  
  Si cada pregunta está en escala 1–5:  
  - En Excel: `=(PROMEDIO(P5:P8)-1)/4*100`

- `Operacion_Cobertura` = PROMEDIO( P9, P10, P11, P26, P27, P28 ) normalizado.  
- `Metricas_Calidad` = PROMEDIO( P14, P15, P16, P17, P19, P20, P21, P22, P23, P24 ).  
- `Regulacion_Reporting` = PROMEDIO( P29, P30, P31, P32 ).  
- `Impacto_ROI` = PROMEDIO( P33, P34, P35, P36, P18 ).  
- `Futuro_Innovacion` = PROMEDIO( P37, P38, P39, P40 ).

**Nota:** Ajuste el rango de columnas a las que haya codificado como numéricas.

### 3.2. Cálculo del IGM

En columna `IGM`:

- Fórmula simple de ponderación uniforme:  

  `IGM = PROMEDIO(Gobierno_Estrategia; Operacion_Cobertura; Metricas_Calidad; Regulacion_Reporting; Impacto_ROI; Futuro_Innovacion)`

Si se desea ponderar más la operación y las métricas (por ejemplo, 30 % cada una):

- `IGM = 0,15*Gobierno_Estrategia + 0,30*Operacion_Cobertura + 0,30*Metricas_Calidad + 0,10*Regulacion_Reporting + 0,10*Impacto_ROI + 0,05*Futuro_Innovacion`

### 3.3. Categorías de madurez

En columnas auxiliares:

- `Categoria_IGM` (texto):

  - `=SI(IGM<20;"Inicial";SI(IGM<40;"Básica";SI(IGM<60;"Intermedia";SI(IGM<80;"Avanzada";"Líder"))))`

### 3.4. Cálculo simple de ROI de SOAR

Defina columnas adicionales en `DATOS_ENCUESTA` (o `CALCULOS`):

- `Coste_Incidentes_Pre_SOAR` (estimado anual).  
- `Coste_Incidentes_Post_SOAR` (estimado anual actual).  
- `Inversion_SOAR` (costes de licencias, implantación, operación anual).  

En `CALCULOS`:

- `Ahorro_Anual` = `Coste_Incidentes_Pre_SOAR - Coste_Incidentes_Post_SOAR`  
- `ROI_SOAR` = `Ahorro_Anual / Inversion_SOAR`

Para facilitar interpretación:

- `ROI_SOAR_%` = `ROI_SOAR * 100`

Opcionalmente, puede utilizar P18 (impacto en MTTD/MTTR) como factor para estimar el ahorro cuando no haya datos económicos completos:

- `Coste_Incidentes_Post_SOAR` ≈ `Coste_Incidentes_Pre_SOAR * (1 - Mejora_Estimada)`

donde `Mejora_Estimada` se derivaría de la codificación de P18 (por ejemplo, Mejora 30–50 % → 0,4).

## 4. Hoja RESUMEN

Incluya:

- Gráficos de barras con distribución de IGM por sector.  
- Mapas de calor por eje (Gobierno, Operación, etc.).  
- Tabla con ROI medio estimado por sector / tamaño.  
- Indicadores clave:  
  - % de organizaciones que miden MTTD/MTTR.  
  - % con automatización superior al 50 % de alertas.  
  - % que calculan ROI formalmente.

El diseño visual puede adaptarse a la identidad corporativa, pero conviene mantener semáforos (rojo/ámbar/verde) para rangos de IGM y ROI.

## 5. Personalización

La plantilla puede ampliarse para:

- Incluir análisis por comunidad autónoma.  
- Incorporar parámetros de coste por incidente procedentes de estudios externos.  
- Simular escenarios de inversión adicional en SOAR (análisis “what‑if”).