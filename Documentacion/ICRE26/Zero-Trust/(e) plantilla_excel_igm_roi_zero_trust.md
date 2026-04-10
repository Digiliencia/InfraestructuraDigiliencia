# Plantilla de Excel para cálculo de IGM y ROI Zero Trust

## 1. Estructura general del archivo

Se recomienda crear un libro de Excel con las siguientes hojas:  
- `Respuestas` – datos crudos por organización.  
- `Ponderaciones` – pesos por pregunta y por pilar.  
- `IGM` – cálculo del Índice Global de Madurez.  
- `ROI` – cálculo del retorno de la inversión.  
- `Diccionario` – descripción de cada campo y escala.  

## 2. Hoja `Respuestas`

Columnas sugeridas:  
- A: ID_Organizacion  
- B: Pais  
- C: Sector  
- D: Tamano  
- E: Tipo_Organizacion (publica/privada/otro)  
- F: NIS2_Aplicable (Si/No)  
- G: ENS_Aplicable (Si/No)  

A partir de la columna H, una columna por cada pregunta cerrada, codificada numéricamente (0–4):  
- H: P2_1  
- I: P2_2  
- ...  
- (continuar hasta cubrir todas las preguntas de madurez relevantes).  

Para preguntas cuantitativas:  
- Columna específica para nº incidentes, coste, inversión, etc. (P11_1, P11_2, P11_3, P11_4, ...).  

## 3. Hoja `Ponderaciones`

Tabla con columnas:  
- Pregunta (ej.: P3_1, P3_2, ...).  
- Pilar (Identidad, Dispositivos, Red, Aplicaciones, Datos, Transversal).  
- Peso_Pregunta (ej.: 1, 2, 3).  
- Comentario.  

Otra tabla con ponderaciones por pilar:  
- Pilar | Peso_Pilar  
- Identidad | 0,25  
- Dispositivos | 0,15  
- Red | 0,20  
- Aplicaciones | 0,20  
- Datos | 0,20  

## 4. Hoja `IGM`

### 4.1. Cálculo de puntuación por pilar

Para cada organización (fila), crear columnas que calculen la media ponderada por pilar. Ejemplo (en Excel, suponiendo respuestas en `Respuestas` y ponderaciones en `Ponderaciones`):  

- Columna `Identidad_Score`:  
  - Usar `SUMAPRODUCTO` entre respuestas de preguntas de identidad y sus pesos, dividido por la suma de pesos.  
- Repetir para `Dispositivos_Score`, `Red_Score`, `Aplicaciones_Score`, `Datos_Score`.  

### 4.2. Cálculo del IGM total

- Columna `IGM_Raw`:  
  - `=Identidad_Score*Peso_Identidad + Dispositivos_Score*Peso_Dispositivos + Red_Score*Peso_Red + Aplicaciones_Score*Peso_Aplicaciones + Datos_Score*Peso_Datos`.  
- Columna `IGM_0_100`:  
  - `=IGM_Raw * 25` (si las puntuaciones por pilar están en 0–4).  

### 4.3. Clasificación por niveles de madurez

Crear una columna `IGM_Nivel` con categorías:  
- 0–24: Inicial.  
- 25–49: Básico.  
- 50–74: Intermedio.  
- 75–89: Avanzado.  
- 90–100: Excelente.  

Se puede usar una fórmula `SI` anidada o `BUSCARV` con tabla de rangos.

## 5. Hoja `ROI`

### 5.1. Datos de entrada

Por organización:  
- `Num_Incidentes` (P11_1).  
- `Num_Incidentes_ZT_Limita` (P11_2).  
- `Coste_Incidentes_Total` (P11_3).  
- `Inversion_ZT` (P11_4).  

### 5.2. Variables derivadas

- `Coste_Medio_Incidente`:  
  - `=SI(Num_Incidentes>0; Coste_Incidentes_Total/Num_Incidentes; 0)`.  
- `Proporcion_Incidentes_Limitados`:  
  - `=SI(Num_Incidentes>0; Num_Incidentes_ZT_Limita/Num_Incidentes; 0)`.  

Opcionalmente, se puede estimar un escenario “sin Zero Trust” suponiendo que los incidentes limitados habrían tenido un coste mayor (por ejemplo, multiplicador 1,5–2x basado en estudios). [web:18][web:26]

### 5.3. Cálculo de beneficios atribuibles a Zero Trust (modelo simple)

Definir una celda con un parámetro `Multiplicador_Impacto` (ej.: 1,5).  

Para cada organización:  
- `Coste_Evitado_ZT`:  
  - `=Coste_Medio_Incidente * (Multiplicador_Impacto - 1) * Num_Incidentes_ZT_Limita`.  

### 5.4. Cálculo del ROI (%)

- `ROI_ZT`:  
  - `=SI(Inversion_ZT>0; (Coste_Evitado_ZT - Inversion_ZT)/Inversion_ZT*100; "N/D")`.  

Se pueden incluir gráficos para visualizar la relación entre IGM e ROI.

## 6. Hoja `Diccionario`

Incluir:  
- Nombre de campo.  
- Descripción.  
- Tipo de dato.  
- Rango de valores.  
- Pilar y norma relacionada (para trazabilidad).  