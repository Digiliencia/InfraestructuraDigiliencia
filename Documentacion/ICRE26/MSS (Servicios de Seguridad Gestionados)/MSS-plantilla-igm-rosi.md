# 📊 PLANTILLA DE CÁLCULO IGM-MSS Y ROI DE CIBERSEGURIDAD
## Encuesta MSS — Instrucciones de Implementación en Hoja de Cálculo
### Lógica de Puntuación, Fórmulas y Visualización
#### Versión 1.0 — Abril 2026

---

> *"Una hoja de cálculo de ciberseguridad que no produce un número incómodo para alguien en la organización probablemente no está midiendo nada relevante."*

---

## INTRODUCCIÓN

Este documento describe la arquitectura completa de la Plantilla Excel/Calc para el cálculo automático del **Índice de Madurez Global MSS (IGM-MSS)** y el **Retorno sobre la Inversión en Seguridad (ROSI)**. La plantilla está diseñada para ser implementada en Microsoft Excel (365/2019+) o LibreOffice Calc 7.x.

**Archivo recomendado:** `MSS_IGM_ROSI_Calculator_v1.0.xlsx`
**Hojas (pestañas) de trabajo:** 8 hojas interconectadas

---

## ARQUITECTURA DE LA PLANTILLA: 8 HOJAS DE TRABAJO

### HOJA 1 — «Respuestas_Encuesta»
*Panel de entrada de datos: aquí se introducen las respuestas de la encuesta*

#### Estructura de la hoja

| Columna | Contenido | Tipo de dato |
|---------|-----------|--------------|
| A | Código de pregunta (P0.1, P0.2…) | Texto |
| B | Texto resumido de la pregunta | Texto |
| C | Bloque temático (B0–B12) | Texto |
| D | Respuesta seleccionada (código numérico 1-6) | Número entero |
| E | Texto de la respuesta seleccionada | Texto (auto-completado con BUSCARV) |
| F | Puntuación asignada (0-4) | Número (auto-calculado) |
| G | Pilar IGM-MSS al que pertenece (P-I a P-V) | Texto |
| H | Peso de la pregunta en el pilar | Porcentaje |
| I | ¿Obligatoria? (S/N) | Booleano |
| J | ¿Respondida? (S/N, auto-calculada) | Booleano |

#### Tablas de conversión respuesta → puntuación (para cada pregunta)

La puntuación de cada respuesta se define en la Hoja 2 (Tabla_Puntuaciones) y se recupera con BUSCARV:

```excel
=BUSCARV(D5, Tabla_Puntuaciones[Código_Respuesta], Tabla_Puntuaciones[Puntuación], FALSO)
```

**Ejemplo — P3.2 (MTTD):**

| Código respuesta | Texto | Puntuación |
|-----------------|-------|-----------|
| 1 | Menos de 15 minutos | 4 |
| 2 | Entre 15 minutos y 1 hora | 3 |
| 3 | Entre 1 y 4 horas | 3 |
| 4 | Entre 4 y 24 horas | 2 |
| 5 | Entre 1 y 7 días | 1 |
| 6 | Más de 7 días | 0 |
| 7 | No disponemos de datos de MTTD | 0 |

**Ejemplo — P6.3 (MFA):**

| Código respuesta | Texto | Puntuación |
|-----------------|-------|-----------|
| 1 | MFA obligatorio para todos los usuarios | 4 |
| 2 | MFA para usuarios privilegiados y accesos críticos | 3 |
| 3 | MFA disponible pero opcional (<70% adopción) | 2 |
| 4 | MFA solo para accesos remotos | 1 |
| 5 | Sin MFA: contraseñas únicas | 0 |
| 6 | Migrando sin fecha comprometida | 1 |

---

### HOJA 2 — «Tabla_Puntuaciones»
*Base de datos de conversión respuesta → puntuación para todas las preguntas*

**Estructura:**

| Col A | Col B | Col C | Col D | Col E |
|-------|-------|-------|-------|-------|
| Pregunta_ID | Respuesta_Código | Respuesta_Texto | Puntuación (0-4) | Justificación |

Esta hoja contiene la tabla maestra de puntuación para las 55 preguntas × hasta 7 opciones = hasta 385 filas de conversión. Es la «tabla de decisión» central del instrumento.

**Fragmento ilustrativo (no exhaustivo):**

| Pregunta_ID | Respuesta_Código | Respuesta_Texto (resumida) | Puntuación | Justificación |
|-------------|-----------------|---------------------------|-----------|---------------|
| P1.1 | 1 | Aprobada por Consejo, revisión anual | 4 | Máximo nivel de gobernanza |
| P1.1 | 2 | Aprobada por Dirección General | 3 | Nivel adecuado |
| P1.1 | 3 | Documento no aprobado formalmente | 2 | Existe pero sin respaldo ejecutivo |
| P1.1 | 4 | En elaboración | 1 | Proceso iniciado |
| P1.1 | 5 | No existe estrategia | 0 | Ausencia crítica |
| P3.1 | 1 | Sí, dashboard en tiempo real | 4 | Monitorización avanzada |
| P3.1 | 2 | Sí, informe mensual | 3 | Monitorización adecuada |
| P3.1 | 3 | Estimación aproximada | 1 | Sin medición sistemática |
| P3.1 | 4 | No se mide pero hay conciencia | 1 | Conciencia sin acción |
| P3.1 | 5 | Desconocemos el indicador | 0 | Brecha de conocimiento |
| P4.3 | 1 | Procedimiento documentado, tres plazos | 4 | Conformidad NIS2 completa |
| P4.3 | 2 | Cumplimos pero proceso tenso | 3 | Conformidad marginal |
| P4.3 | 3 | Solo para incidentes mayores | 1 | Conformidad parcial |
| P4.3 | 4 | Sin procedimientos formales | 0 | Incumplimiento NIS2 Art.23 |
| P4.3 | 5 | Desconocíamos estos plazos | 0 | Riesgo crítico de incumplimiento |

---

### HOJA 3 — «IGM_MSS_Cálculo»
*Motor de cálculo del Índice de Madurez Global*

#### Lógica de agregación por pilares

```excel
// Pilar I — Gobernanza y Estrategia (preguntas: P1.1–P1.7, P2.1–P2.3)
Pilar_I_Bruto = PROMEDIO.SI(Respuestas[Pilar],"P-I",Respuestas[Puntuación])
Pilar_I_Max = 4  // máximo posible
Pilar_I_Pct = (Pilar_I_Bruto / Pilar_I_Max) × 100
Pilar_I_Ponderado = Pilar_I_Pct × 0.20

// Pilar II — Detección y Respuesta (preguntas: P3.1–P3.10, P6.1–P6.4)
Pilar_II_Bruto = PROMEDIO.SI(Respuestas[Pilar],"P-II",Respuestas[Puntuación])
Pilar_II_Pct = (Pilar_II_Bruto / 4) × 100
Pilar_II_Ponderado = Pilar_II_Pct × 0.25

// Pilar III — Cumplimiento y Riesgos (preguntas: P4.1–P4.7, P11.1–P11.2)
Pilar_III_Bruto = PROMEDIO.SI(Respuestas[Pilar],"P-III",Respuestas[Puntuación])
Pilar_III_Pct = (Pilar_III_Bruto / 4) × 100
Pilar_III_Ponderado = Pilar_III_Pct × 0.20

// Pilar IV — Resiliencia y Capital Humano (preguntas: P5.1–P5.5, P7.1–P7.5)
Pilar_IV_Bruto = PROMEDIO.SI(Respuestas[Pilar],"P-IV",Respuestas[Puntuación])
Pilar_IV_Pct = (Pilar_IV_Bruto / 4) × 100
Pilar_IV_Ponderado = Pilar_IV_Pct × 0.15

// Pilar V — Tecnología y Emergentes (preguntas: P8.1–P8.3, P9.1–P9.4, P10.1–P10.5, P6.5–P6.6)
Pilar_V_Bruto = PROMEDIO.SI(Respuestas[Pilar],"P-V",Respuestas[Puntuación])
Pilar_V_Pct = (Pilar_V_Bruto / 4) × 100
Pilar_V_Ponderado = Pilar_V_Pct × 0.20

// IGM-MSS TOTAL
IGM_MSS = Pilar_I_Ponderado + Pilar_II_Ponderado + Pilar_III_Ponderado 
          + Pilar_IV_Ponderado + Pilar_V_Ponderado
```

#### Ajuste por preguntas N/A

```excel
// Si una pregunta devuelve N/A, se excluye y el peso se redistribuye
Preguntas_Respondidas_PilarX = CONTAR.SI(Respuestas[Pilar],"P-X") 
                               - CONTAR.SI(Respuestas[Puntuación],"N/A")
Pilar_X_Ajustado = SUMA.SI(Respuestas[Pilar],"P-X") / (Preguntas_Respondidas_PilarX × 4) × 100
```

#### Tabla de resultados en Hoja 3

| Concepto | Fórmula | Valor calculado |
|----------|---------|-----------------|
| IGM-MSS Total | Suma ponderada de pilares | [0–100] |
| Nivel de madurez | BUSCARV(IGM_MSS, Tabla_Niveles) | [1–5 con descripción] |
| Pilar más fuerte | INDICE(Pilares, COINCIDIR(MAX(Pilares),Pilares,0)) | [Nombre del pilar] |
| Pilar más débil | INDICE(Pilares, COINCIDIR(MIN(Pilares),Pilares,0)) | [Nombre del pilar] |
| Tasa de completitud | Respondidas/Total × 100 | [%] |

---

### HOJA 4 — «ROSI_Cálculo»
*Modelo actuarial de retorno sobre inversión en seguridad*

#### Modelo ROSI Básico (inputs manuales)

**SECCIÓN A — Parámetros de Exposición al Riesgo**

| Variable | Símbolo | Descripción | Unidad | Input |
|----------|---------|-------------|--------|-------|
| Asset Value (AV) | AV | Valor total de activos de información en riesgo | € | [Input manual] |
| Exposure Factor (EF) | EF | % del AV que se perdería en caso de materialización | % (0-100%) | [Input manual] |
| Annualized Rate of Occurrence (ARO) | ARO | Frecuencia esperada de incidentes por año | # veces/año | [Input manual] |

**SECCIÓN B — Cálculo de Exposición**

```excel
// Single Loss Expectancy (SLE): pérdida esperada por un solo incidente
SLE = AV × (EF / 100)

// Annualized Loss Expectancy (ALE): pérdida esperada anualizada SIN controles
ALE_sin_controles = SLE × ARO
```

**SECCIÓN C — Impacto del Control MSS**

| Variable | Símbolo | Descripción | Unidad |
|----------|---------|-------------|--------|
| Exposure Factor modificado | EF_mod | % del AV en riesgo CON los controles MSS | % |
| ARO modificado | ARO_mod | Frecuencia incidentes CON los controles MSS | # veces/año |
| Coste anual del control | CSC | Coste total anual del servicio MSS | € |

```excel
// ALE con controles implementados
ALE_con_controles = (AV × (EF_mod / 100)) × ARO_mod

// Pérdidas anuales evitadas
Perdidas_Evitadas = ALE_sin_controles - ALE_con_controles

// ROSI
ROSI_pct = ((Perdidas_Evitadas - CSC) / CSC) × 100

// Payback period (años)
Payback = CSC / Perdidas_Evitadas
```

**SECCIÓN D — Tabla de Escenarios (Análisis de Sensibilidad)**

La hoja genera automáticamente una tabla de sensibilidad bidimensional:

```
Filas: variación de EF (50%, 60%, 70%, 80%, 90%, 100%)
Columnas: variación de ARO (0.1, 0.25, 0.5, 1, 2, 5 veces/año)
Valores: ROSI resultante para cada combinación
```

Esto permite visualizar el rango de ROSI plausible bajo diferentes supuestos de materialización del riesgo.

#### Modelo ROSI Avanzado (con datos del IGM-MSS)

El modelo avanzado usa la puntuación del Pilar II (Detección y Respuesta) para estimar automáticamente la reducción de EF y ARO:

```excel
// Factor de reducción de riesgo basado en madurez Pilar II
Reduccion_ARO = Pilar_II_Pct × 0.60   // Hasta 60% reducción de frecuencia en nivel 5
Reduccion_EF = Pilar_II_Pct × 0.40    // Hasta 40% reducción de impacto en nivel 5

// ARO y EF ajustados por madurez
ARO_mod_calculado = ARO × (1 - Reduccion_ARO / 100)
EF_mod_calculado = EF × (1 - Reduccion_EF / 100)
```

*Nota: Los factores de reducción (0.60, 0.40) son valores conservadores basados en la literatura actuarial. El CAS Research Paper on Cyber Risk (junio 2025) proporciona rangos alternativos por sector que pueden sustituir estos valores.*

---

### HOJA 5 — «Benchmark_Sectorial»
*Comparativa con datos de referencia del mercado*

**Datos de referencia pre-cargados** (actualizables con nuevas ediciones del informe):

| Sector | N respondentes | IGM-MSS Mediana | IGM-MSS P25 | IGM-MSS P75 | MTTD Mediana | MTTR Mediana |
|--------|---------------|-----------------|------------|------------|-------------|-------------|
| Banca y Seguros | Ref. ENISA/AON 2025 | 68 | 55 | 78 | <1h | <4h |
| Energía | Ref. ENISA 2025 | 62 | 48 | 74 | <4h | <8h |
| Administración Pública | Ref. CCN/INCIBE 2025 | 51 | 38 | 64 | <24h | <48h |
| Sanidad | Ref. ENS Sanitario 2025 | 47 | 35 | 62 | <24h | <48h |
| Manufactura/OT | Ref. ENISA OT 2025 | 42 | 28 | 58 | <8h | <24h |
| Agroindustria y Logística | Ref. AON España 2025 | 34 | 22 | 48 | >24h | >48h |
| Media mercado España | Balance INCIBE 2025 | 48 | 32 | 65 | <24h | <48h |
| Media mercado UE | ENISA MSS 2025 | 52 | 38 | 68 | <8h | <24h |

*Nota: Estos valores son benchmarks estimados construidos a partir de las fuentes documentales del informe MSS 2025-2026. Deben sustituirse por datos empíricos cuando el instrumento acumule N>30 respuestas reales por sector.*

**Fórmulas de comparación:**

```excel
// Diferencia respecto a mediana sectorial
Delta_IGM = IGM_MSS_Organizacion - Benchmark_Mediana_Sector

// Percentil estimado (interpolación lineal entre P25 y P75)
Percentil_estimado = SI(IGM_MSS_Org <= Benchmark_P25, 
                        "<P25",
                        SI(IGM_MSS_Org >= Benchmark_P75, 
                           ">P75",
                           25 + (IGM_MSS_Org - Benchmark_P25) / 
                           (Benchmark_P75 - Benchmark_P25) × 50))
```

---

### HOJA 6 — «Dashboard_Visual»
*Panel de visualización ejecutiva (gráficos automáticos)*

**Gráficos incluidos (se generan automáticamente con los datos calculados):**

1. **Gráfico de radar de 5 pilares (Spider Chart):**
   - Eje 1: Pilar I — Gobernanza (0-100)
   - Eje 2: Pilar II — Detección (0-100)
   - Eje 3: Pilar III — Cumplimiento (0-100)
   - Eje 4: Pilar IV — Resiliencia (0-100)
   - Eje 5: Pilar V — Tecnología (0-100)
   - Serie 1: Puntuación organización (azul)
   - Serie 2: Benchmark sectorial (gris punteado)

2. **Velocímetro del IGM-MSS:**
   - Indicador tipo «gauge» de 0 a 100
   - Zonas de color: 0-20 (rojo), 21-40 (naranja), 41-60 (amarillo), 61-80 (verde claro), 81-100 (verde)

3. **Gráfico de barras comparativo de pilares:**
   - Barras de la organización vs. benchmark sectorial vs. benchmark UE

4. **Gráfico de análisis de sensibilidad ROSI:**
   - Mapa de calor (heatmap) de la tabla de escenarios
   - Colores: verde (ROSI>100%), amarillo (0-100%), rojo (ROSI<0%)

5. **Gráfico de brechas prioritarias:**
   - Barras horizontales ordenadas de mayor a menor brecha respecto al benchmark
   - Top 5 áreas de mejora resaltadas

---

### HOJA 7 — «Plan_Mejora»
*Generador automático de hoja de ruta de mejora*

La hoja utiliza las puntuaciones de Hoja 1 para generar automáticamente las recomendaciones de mejora ordenadas por prioridad:

**Lógica de priorización:**

```excel
// Para cada pregunta con puntuación < 3:
Brecha = 3 - Puntuacion_Pregunta  // Brecha respecto al nivel objetivo "Definido"
Peso_Normativo = BUSCARV(Pregunta_ID, Tabla_Pesos_Normativos)  // 1=bajo, 2=medio, 3=alto
Impacto_ROSI = BUSCARV(Pregunta_ID, Tabla_Impacto_ROSI)  // 1=bajo, 2=medio, 3=alto
Facilidad = BUSCARV(Pregunta_ID, Tabla_Facilidad)  // 1=difícil, 2=medio, 3=fácil

Prioridad_Compuesta = (Brecha × 2) + (Peso_Normativo × 1.5) + (Impacto_ROSI × 1.5) + (Facilidad × 0.5)
```

**Tabla de salida de Plan de Mejora:**

| Rank | Pregunta | Área de mejora | Brecha actual | Objetivo 6m | Objetivo 12m | Requisito normativo | Estimación esfuerzo | Estimación coste |
|------|----------|---------------|--------------|------------|-------------|---------------------|--------------------|--------------------|
| 1 | P6.3 | Implementar MFA universal | 0 → 2 | 2 | 4 | NIS2 Art.21.2.j | 2-4 semanas | Bajo-Medio |
| 2 | P4.3 | Procedimiento notificación incidentes | 0 → 3 | 3 | 4 | NIS2 Art.23 | 4-8 semanas | Bajo |
| 3 | P3.7 | Gestión continua vulnerabilidades | 1 → 3 | 2 | 3 | NIS2 Art.21.2.b | 8-12 semanas | Medio |
| … | … | … | … | … | … | … | … | … |

---

### HOJA 8 — «Histórico_Evolución»
*Registro de evoluciones temporales del IGM-MSS*

Para organizaciones que realizan reaplicaciones periódicas de la encuesta:

| Fecha | IGM-MSS Total | Pilar I | Pilar II | Pilar III | Pilar IV | Pilar V | Notas |
|-------|--------------|---------|---------|----------|---------|---------|-------|
| [Fecha 1] | [Auto] | [Auto] | [Auto] | [Auto] | [Auto] | [Auto] | Diagnóstico inicial |
| [Fecha 2] | [Auto] | [Auto] | [Auto] | [Auto] | [Auto] | [Auto] | Reaplicación 6m |
| [Fecha 3] | [Auto] | [Auto] | [Auto] | [Auto] | [Auto] | [Auto] | Reaplicación 12m |

Gráfico de líneas automático que muestra la evolución del IGM-MSS y de cada pilar a lo largo del tiempo.

---

## INSTRUCCIONES DE IMPLEMENTACIÓN PASO A PASO

### Paso 1 — Preparación del archivo

1. Crear libro Excel con 8 hojas con los nombres definidos
2. Activar las macros (si se usa VBA) o configurar las fórmulas manuales
3. Proteger las hojas de cálculo con contraseña (excepto Hoja 1 y Hoja 4)
4. Configurar la validación de datos en la columna D de Hoja 1 (lista desplegable 1-7)

### Paso 2 — Carga de datos de encuesta

1. En Hoja 1 (Respuestas_Encuesta), ingresar el código numérico de la respuesta elegida en columna D
2. Las columnas E (texto) y F (puntuación) se calculan automáticamente
3. Para respuestas «N/A», usar código «0» (la fórmula de Hoja 3 lo gestiona)

### Paso 3 — Introducción de parámetros ROSI

1. En Hoja 4 (ROSI_Cálculo), introducir en las celdas amarillas:
   - AV (valor total activos en riesgo, en euros)
   - EF (factor de exposición, en %)
   - ARO (frecuencia esperada de incidentes, en número por año)
   - CSC (coste anual del servicio MSS, en euros)
2. Los resultados ROSI, SLE, ALE y payback se calculan automáticamente

### Paso 4 — Lectura de resultados

1. Ir a Hoja 6 (Dashboard_Visual) para vista ejecutiva
2. Consultar Hoja 7 (Plan_Mejora) para hoja de ruta priorizada
3. Exportar Hoja 3 e Hoja 4 para el informe ejecutivo

---

## INSTRUCCIONES PARA ANÁLISIS MULTI-RESPONDENTE

Si varios perfiles de la organización completan la encuesta:

1. Crear una copia del archivo por cada respondente
2. En una hoja «Agregado», usar la siguiente fórmula de reconciliación:

```excel
// Para preguntas numéricas: media ponderada por relevancia del perfil
Puntuacion_Agregada = SUMA(Peso_Perfil × Puntuacion_Perfil) / SUMA(Peso_Perfil)

// Pesos recomendados por perfil:
// CISO: 1.5
// CTO/CIO: 1.2
// Director Riesgos: 1.2
// Gestor contratos MSS: 1.0
// Director General: 0.8
```

---

*Plantilla IGM-MSS y ROSI — Versión 1.0 · Abril 2026*
*Metodología ROSI basada en: NIST SP 800-55, CAS Research Paper on Cyber Risk (junio 2025), AON Cyber 2025 Spain, ENISA MSS Market Analysis 2025*
