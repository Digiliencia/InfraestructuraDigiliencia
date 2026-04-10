# Plantilla de Excel para IGM y Evaluación PRAGMATIC

## 1. Hoja "Métricas_Nacionales"

Columnas sugeridas:
- Anio
- Sector
- M1_IncidentesSignificativos
- M2_TasaIncidentes
- M3_%Ransomware
- M3_%DDoS
- M3_%BEC
- M4_MTTD
- M5_MTTR
- M6_TiempoRecuperacion
- M7_IndiceControles
- M8_IGM_Sector
- M9_%RTO_RPO_Cumplidos
- M10_EjerciciosCrisis
- M10_%LeccionesImplementadas
- M11_%Cumplimiento_ENS_NIS2
- M12_Sanciones
- M13_%Presupuesto_Ciber
- M15_PerdidasEvitadas

## 2. Hoja "PRAGMATIC"

Filas = Métricas (M1 a M15)  
Columnas = Criterios PRAGMATIC (P, R, A, G, M, P2, O, I, R2) con valores 0-3.

Se puede añadir una columna "Score_PRAGMATIC" calculada como:

Score_PRAGMATIC = PROMEDIO(P:R2)

## 3. Hoja "IGM_Sectores"

Si se dispone de datos de encuesta por organización:
- Calcular IGM por organización (mediante plantilla anterior).
- Calcular IGM medio por sector.

## 4. Hoja "ROI_Nacional" (opcional)

Agregar:
- Inversion_Ciber_Sector (por año)
- M1, M2, M4, M5, M6 por sector y año
- Estimaciones de PerdidasEvitadas (M15)

Definir indicadores derivados, como:
- RiesgoMitigado_por_Euro = PerdidasEvitadas / Inversion_Ciber_Sector

## 5. Hoja "Dashboards"

Tablas y gráficos dinámicos para:
- Evolución temporal de M1–M6.
- Comparación entre sectores de M7–M11.
- Relación entre inversión (M13) y resultados (M1, M4, M5, M11).
- Distribución de scores PRAGMATIC por métrica.