# Plantilla de Excel – IGM y ROI integrados con GQM + PRAGMATIC

Esta plantilla amplía la propuesta de cálculo de IGM y ROI incorporando explícitamente los objetivos GQM (G1–G4) y las calificaciones PRAGMATIC de las métricas.[web:26][web:22]

## 1. Estructura de hojas

1. **DATOS_ENCUESTA** – Respuestas de la encuesta por organización.
2. **CALCULOS_GQM** – Cálculo de métricas M1.x–M4.x por organización y eje.
3. **PRAGMATIC_SCORES** – Ponderaciones PRAGMATIC por métrica.
4. **IGM_Y_ROI** – Cálculo de IGM por eje y global, ROI y scores ajustados PRAGMATIC.
5. **RESUMEN_NACIONAL** – Agregados por sector, tamaño y naturaleza.

## 2. Hoja DATOS_ENCUESTA

Igual que en la versión básica: filas = organizaciones, columnas = respuestas codificadas (P5–P40), más identificadores de sector, tamaño, etc.[web:12]

## 3. Hoja CALCULOS_GQM

### 3.1. Cálculo de métricas de tiempo (G1)

- Columnas ejemplo:
  - `MTTD_critico` (a partir de P15). Asignar valor medio del rango.
  - `MTTC_critico` (P16). Idem.
  - `MTTR_critico` (P17). Idem.
  - `Impacto_SOAR_Tiempos` (P18) convertido a factor de mejora.

A partir de estas, puede derivarse:

- `M1.1` = `MTTD_critico` (en minutos u horas).
- `M1.2` = `MTTC_critico`.
- `M1.3` = `MTTR_critico`.
- `M1.5` = `Impacto_SOAR_Tiempos` (porcentaje).[web:24]

### 3.2. Métricas de cobertura y calidad (G2)

- `Cobertura_Alertas_Autom` (de P10). Convertir rango a %.
- `Casos_Uso_Autom` (de P11–12, P26). Número o %.
- `Tasa_Exito_Playbooks` (si se añade módulo complementario o se infiere de P22–23).

Estas alimentan las columnas:

- `M2.1`, `M2.2`, `M2.3`, `M2.5`.

### 3.3. Métricas de cumplimiento y reporting (G3)

- `Uso_SOAR_Notificacion` (P30). Codificar 0–1.
- `Tiempo_Notificacion` (P31). Asignar valor medio de rango.
- `%_Notificaciones_Plazo` (si se añade módulo de detalle o a través de auditorías; puede estimarse inicialmente cualitativamente).[web:39]

### 3.4. Métricas económicas (G4)

- `Estima_Coste_Incidentes` (P33) → indicador binario.
- `Modelo_ROI_Formal` (P35) → indicador binario.
- `Percepcion_Valor_SOAR` (P36) → escala 1–4.

Si se dispone de datos numéricos de coste e inversión:

- `Coste_Pre` / `Coste_Post` / `Inversion_SOAR` → para compilar M4.2–M4.4.[web:26]

## 4. Hoja PRAGMATIC_SCORES

Crear una tabla con filas = métricas (M1.1, M1.2, ..., M4.5) y columnas = criterios PRAGMATIC.

- Asignar valores numéricos (A=3, M=2, B=1) según la matriz de evaluación.[code_file:52]
- Calcular `Score_PRAGMATIC` por métrica = `PROMEDIO(Predictivo:Rentable)`.

Opcionalmente, normalizar a 0–1 o 0–100.

## 5. Hoja IGM_Y_ROI

### 5.1. Ejes de madurez (IGM) alineados con objetivos G1–G4

Para cada organización:

- `IGM_G1_Tiempos` basado en M1.x (normalizado 0–100, invirtiendo valores donde menos es mejor).
- `IGM_G2_Automatizacion` basado en M2.x (0–100).
- `IGM_G3_Cumplimiento` basado en M3.x (0–100).
- `IGM_G4_Impacto` basado en M4.x (0–100).

El **IGM global** puede ser:

- `IGM_Global = PROMEDIO(IGM_G1:IGM_G4)` o una combinación ponderada.

### 5.2. Ajuste PRAGMATIC

Para reflejar la calidad de las métricas subyacentes:

- Definir pesos por métrica = `Score_PRAGMATIC_normalizado`.
- Calcular, por ejemplo, `IGM_G1_ajustado` como media ponderada de M1.x con sus pesos PRAGMATIC.

Esto permite que métricas muy débiles en términos PRAGMATIC tengan menor influencia en el indicador compuesto.

### 5.3. ROI integrado

Mantener el cálculo de ROI ya propuesto, pero permitir análisis adicionales:

- `ROI_vs_IGM` → correlación entre ROI_SOAR y IGM_G2/IGM_Global.
- `ROI_ajustado` → análisis de sensibilidad considerando solo métricas con alta calidad PRAGMATIC.

## 6. Hoja RESUMEN_NACIONAL

- Distribuciones de IGM por sector, tamaño, naturaleza.
- Tablas de medias y medianas de M1.x–M4.x.
- Indicadores clave: % org. que miden tiempos, que usan SOAR para notificación, que calculan ROI, etc.[web:12][web:39]

Esta estructura integra GQM en la forma de organizar los cálculos (por objetivos y métricas asociadas) y PRAGMATIC en la forma de ponderar y priorizar la importancia de cada métrica en los indicadores compuestos.