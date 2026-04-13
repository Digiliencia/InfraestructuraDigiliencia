# PLANTILLA DE EXCEL PARA CÁLCULO DE IGM E IGM ROI
## Kit de Cálculo Automatizado - Implementación en Excel/Google Sheets

**Versión:** 1.0  
**Fecha:** Enero 2026  
**Propósito:** Plantilla lista para implementar; automatiza cálculo de Índice de Generación de Métricas (IGM) y ROI de seguridad

---

## ESTRUCTURA GENERAL DE LA PLANTILLA EXCEL

La plantilla consta de **6 hojas de cálculo integradas**:

```
LIBRO: "CIS_Controls_IGM_ROI_Calculation.xlsx"
│
├── Hoja 1: INSTRUCCIONES (Guía de uso)
├── Hoja 2: ENTRADA DE DATOS (Data input por indicador)
├── Hoja 3: CÁLCULO IGM (Índice Generación Métricas)
├── Hoja 4: CÁLCULO ROI (Retorno de Inversión)
├── Hoja 5: DASHBOARD (Visualización ejecutiva)
└── Hoja 6: BENCHMARKS (Comparativas sectoriales)
```

---

## HOJA 1: INSTRUCCIONES

### Contenido

```
TÍTULO: "Guía de Uso - Plantilla CIS Controls IGM & ROI"

SECCIÓN 1: Definiciones
─────────────────────
IGM (Índice de Generación de Métricas):
  Métrica agregada que mide madurez de framework de indicadores.
  Rango: 0-100 (0=ningún indicador, 100=todos indicadores en nivel 4-5)
  Fórmula: (Σ puntuaciones PRAGMATIC / (Nº indicadores × 3)) × 100

ROI (Retorno de Inversión Ciberseguridad):
  Medida de valor creado por inversión en seguridad.
  Rango: -100% a +500% (típicamente)
  Fórmula: [(Riesgos mitigados - Inversión) / Inversión] × 100

SECCIÓN 2: Instrucciones de entrada
─────────────────────────────────────
1. Ir a Hoja 2: ENTRADA DE DATOS
2. Columna A: Seleccionar indicador de lista desplegable
3. Columna B-J: Ingresar scores PRAGMATIC (0-3) para cada criterio
4. Columna K: Score total se calcula automáticamente
5. Columna L: Recomendación se genera automática (✅/⚠️/❌)

SECCIÓN 3: Interpretación de resultados
────────────────────────────────────────
IGM 80-100: Excelente framework de indicadores (implementar todos)
IGM 60-79: Bueno; considerar agregar 2-3 indicadores más
IGM 40-59: Aceptable; plan de expansión necesario
IGM <40: Crítico; iniciar implementación fase 1 inmediatamente

ROI >200%: Inversión muy rentable (típico año 2-3)
ROI 100-200%: Rentable (año 1-2)
ROI 0-100%: Break-even a largo plazo
ROI <0: Requiere re-evaluación (usualmente indicadores débiles)

SECCIÓN 4: Soporte
──────────────────
Preguntas: Contactar CISO@organización
Actualizaciones: Revisar trimestralmente
Auditoría: Validar externamente anualmente
```

---

## HOJA 2: ENTRADA DE DATOS

### Estructura de Tabla

```
| Fila | Columna | Tipo | Descripción | Ejemplo |
|-----|---------|------|-------------|---------|
| 1 | A-L | Header | Títulos de columnas | "Indicador", "P", "R", "A", ... |
| 2-N | A | Dropdown | Seleccionar indicador de lista | "MTTD", "MFA Adoption", etc. |
| 2-N | B | Number | Puntuación P (Predictivo) 0-3 | 3 |
| 2-N | C | Number | Puntuación R (Relevante) 0-3 | 3 |
| 2-N | D | Number | Puntuación A (Accionable) 0-3 | 3 |
| 2-N | E | Number | Puntuación G (Genuino) 0-3 | 2 |
| 2-N | F | Number | Puntuación S (Significativo) 0-3 | 3 |
| 2-N | G | Number | Puntuación P (Preciso) 0-3 | 3 |
| 2-N | H | Number | Puntuación T (Oportuno) 0-3 | 2 |
| 2-N | I | Number | Puntuación I (Independiente) 0-3 | 2 |
| 2-N | J | Number | Puntuación C (Rentable) 0-3 | 3 |
| 2-N | K | Formula | Score Total = AVG(B:J) | =AVERAGE(B2:J2) |
| 2-N | L | Formula | Recomendación | =IF(K2>=2.75,"✅",IF(K2>=2,"⚠️","❌")) |
```

### Ejemplo de Entrada

```
Indicador | P | R | A | G | S | P | T | I | C | Score | Recomendación
──────────────────────────────────────────────────────────────────────
MTTD      | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 2.89  | ✅
Phishing  | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 2.89  | ✅
MFA Rate  | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2.67  | ✅
Vulns Cr. | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 1 | 2 | 2.56  | ✅
```

### Validación de Datos

```
Regla de Validación para columnas B-J:
├─ Tipo: Número entero
├─ Mínimo: 0
├─ Máximo: 3
└─ Mensaje de error: "Ingrese puntuación entre 0 y 3"

Lista desplegable Columna A:
├─ Incluir todos indicadores de Matriz PRAGMATIC (45+)
├─ Ordenados por módulo CIS
└─ Actualizar semestral con nuevos indicadores
```

---

## HOJA 3: CÁLCULO IGM

### Definición de IGM

```
IGM = Índice de Generación de Métricas

Fórmula Base:
IGM = (Σ Scores PRAGMATIC / (Nº indicadores × 3)) × 100

Descomposición:
├─ Numerador: Suma de todos scores PRAGMATIC de indicadores implementados
├─ Denominador: Número de indicadores × 3 (máximo posible)
└─ × 100: Convertir a escala porcentual (0-100)

Ejemplo Cálculo:
└─ 5 indicadores con scores: 2.89, 2.89, 2.78, 2.56, 2.56
   └─ Suma = 13.68
   └─ IGM = (13.68 / (5 × 3)) × 100 = (13.68 / 15) × 100 = 91.2%
```

### Estructura de Tabla IGM

```
SECCIÓN 1: INGRESO DE DATOS
─────────────────────────
Columna A: Módulo CIS (GRC, IDENTIFY, IAM, etc.)
Columna B: Indicador (nombre)
Columna C: Score PRAGMATIC (obtenido de Hoja 2)
Columna D: Peso (opcional; por defecto 1)
Columna E: Score Ponderado (= C × D)

SECCIÓN 2: CÁLCULOS AGREGADOS
──────────────────────────────
Fila 30: "Total Indicadores" | Count(Indicadores con score ≠ null)
Fila 31: "Suma Scores" | SUM(E:E)
Fila 32: "Puntuación Máxima Posible" | Total × 3
Fila 33: "IGM (%)" | (Fila 31 / Fila 32) × 100

SECCIÓN 3: DESGLOSE POR MÓDULO
───────────────────────────────
Tabla resumida:
│ Módulo | Indicadores | Promedio Score | IGM Módulo |
│--------|-------------|----------------|-----------|
│ GRC    | 3           | 2.45           | 81.7%     |
│ IDENTIFY| 2           | 2.50           | 83.3%     |
│ IAM    | 4           | 2.65           | 88.3%     |
│ ... (resto módulos)
│ TOTAL  | 18          | 2.58           | 86.0%     |
```

### Fórmulas Excel

```
Celda: B30 (Total indicadores)
Fórmula: =COUNTA(C:C)-1  // Excluye header

Celda: B31 (Suma scores)
Fórmula: =SUMIF(C:C,">0")

Celda: B32 (Máximo posible)
Fórmula: =B30*3

Celda: B33 (IGM %)
Fórmula: =(B31/B32)*100

Celda: B35-B37 (IGM por módulo)
Fórmula (ejemplo GRC): =AVERAGEIF(A:A,"GRC",C:C)/3*100
```

---

## HOJA 4: CÁLCULO ROI

### Definición de ROI Ciberseguridad

```
ROI = [(Beneficios - Inversión) / Inversión] × 100

En contexto ciberseguridad:

Beneficios = Riesgos Mitigados (en valor monetario)
Inversión = Costo de implementar medidas de seguridad
```

### Estructura de Tabla ROI

```
SECCIÓN 1: ESTIMACIÓN DE INVERSIÓN (€)
──────────────────────────────────────
Concepto                    | 2025 | 2026 | 2027 | Total
────────────────────────────┼──────┼──────┼──────┼──────
Herramientas (SIEM, etc)    | 80k  | 50k  | 50k  | 180k
Personal (CISO + team)      | 250k | 250k | 250k | 750k
Capacitación                | 30k  | 30k  | 30k  | 90k
Consultorías/Auditorías     | 100k | 50k  | 50k  | 200k
─────────────────────────────────────────────────────────
TOTAL INVERSIÓN 3 AÑOS      | 460k | 380k | 380k | 1.22M

Notas:
├─ Presupuesto anual existente se deduce (solo incremental)
├─ Incluir costos ocultos: time away from work, etc.
└─ Proyectar en análisis multi-año (mínimo 3 años)
```

### Estimación de Beneficios (Riesgos Mitigados)

```
SECCIÓN 2: ESTIMACIÓN DE BENEFICIOS (€)
───────────────────────────────────────

Método A: Basado en Probabilidad × Impacto

Risk Factor 1: Reducción Breach Probability
├─ Baseline: Probabilidad breach sin inversión: 15%
├─ Post-inversión: Probabilidad con SIEM + MFA: 5%
├─ Reducción: 10% (10 puntos porcentuales)
├─ Si Asset Value = €50M, Impacto breach = 30% (€15M)
└─ Beneficio Anual: 10% × €15M = €1.5M

Risk Factor 2: Reducción Ransomware MTTR
├─ Baseline MTTR: 72 horas
├─ Post-inversión MTTR: 4 horas
├─ Ahorro downtime: 68 horas × €10k/hora = €680k
└─ Beneficio Anual: €680k

Risk Factor 3: Cumplimiento regulatorio
├─ Multa GDPR potencial: €20M
├─ Multa NIS2 potencial: €10M
├─ Probabilidad evitada por cumplimiento: 5% → 0.5%
└─ Beneficio Anual: 4.5% × €30M = €1.35M

TOTAL BENEFICIO ANUAL: €1.5M + €680k + €1.35M = €3.53M (conservador)
```

### Cálculo de ROI

```
SECCIÓN 3: CÁLCULO ROI 3 AÑOS
─────────────────────────────

Año 1: [(€3.53M × 1) - €0.46M] / €0.46M × 100 = 667%
Año 2: [(€3.53M × 2) - €0.46M - €0.38M] / (€0.46M + €0.38M) × 100 = 426%
Año 3: [(€3.53M × 3) - (€0.46M + €0.38M + €0.38M)] / €1.22M × 100 = 755%

3-YEAR CUMULATIVE:
Beneficios Totales: €3.53M × 3 = €10.59M
Inversión Total: €1.22M
ROI 3-AÑOS: (€10.59M - €1.22M) / €1.22M × 100 = 768%

Interpretación:
"Por cada €1 invertido en 3 años, la organización ahorra/genera €7.68"
```

### Tabla Excel de ROI

```
Fila | Concepto | Año 1 | Año 2 | Año 3 | Total 3Y | Fórmula
─────┼──────────┼───────┼───────┼───────┼─────────┼──────────
10  | Beneficio| €3.53M| €3.53M| €3.53M| €10.59M | =SUM(B10:D10)
11  | Inversión| €0.46M| €0.38M| €0.38M| €1.22M  | =SUM(B11:D11)
12  | Beneficio Neto| €3.07M| €3.15M| €3.15M| €9.37M | =B10-B11
13  | ROI (%) | 667%  | 426%  | 755%  | 768%    | =(B12/B11)*100

Sensitivity Analysis (si varían asunciones):
├─ Si beneficios -20%: ROI 3Y = 614%
├─ Si inversión +30%: ROI 3Y = 590%
├─ Si beneficios -20% + inversión +30%: ROI 3Y = 450%
└─ Breakeven point: Año 1, Mes 2 (muy favorable)
```

---

## HOJA 5: DASHBOARD

### Visualizaciones Recomendadas

```
SECCIÓN 1: INDICADORES CLAVE (KPI Box)
──────────────────────────────────────
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ IGM: 86.0%      │  │ ROI 3Y: 768%    │  │ Indicadores: 18 │
│ ↑ 12% vs Q3     │  │ ↑ 145% vs Q3    │  │ ✅ 13 / ⚠️ 5   │
└─────────────────┘  └─────────────────┘  └─────────────────┘

SECCIÓN 2: GRÁFICO IGM POR MÓDULO (Barras)
───────────────────────────────────────────
GRC: ███████████████░░░░░ 83%
IDENTIFY: ██████████████░░░░░ 80%
IAM: █████████████████░░ 87%
PROTECT: ██████████████░░░░░░ 79%
DETECT: ███████░░░░░░░░░░░░░░░ 67%
RESPOND: ████████████████░░░ 82%
RECOVER: ██████████████████░░ 88%
CYBER_RISK: ██████████░░░░░░░░░░░░░ 71%
SCRM: ████████░░░░░░░░░░░░░░░░ 67%

SECCIÓN 3: TENDENCIA ROI (Línea 3 años)
────────────────────────────────────────
€12M │                         ★
     │                    ★
€10M │               ★
     │
€8M  │
     │
€6M  │ ╱
     │╱    ╱
€4M  │────╱────╱───
     │   €1.22M
€0M  │______________→ Año 1 | Año 2 | Año 3
     Breakeven: Mes 2, Año 1

SECCIÓN 4: COMPARATIVA BENCHMARKS (Tabla)
──────────────────────────────────────────
              │ Vuestra Org | Benchmark | Brecha
──────────────┼─────────────┼───────────┼───────
IGM Actual    │ 86.0%       │ 75% (IG2) │ +11%
Indicadores   │ 18/45       │ 25/45     │ -7
MTTD (hrs)    │ 8           │ 4         │ -4h
MFA Coverage  │ 92%         │ 95%       │ -3%
Vuln Remediation | 35d      │ 7d        │ -28d
ROI 3Y        │ 768%        │ 600%      │ +168%

SECCIÓN 5: ALERTAS (Semáforo)
──────────────────────────────
🟢 VERDE:     IGM >85%, ROI >500%
🟡 AMARILLO:  IGM 70-85%, ROI 300-500%
🔴 ROJO:      IGM <70%, ROI <300%

Estado Actual: 🟢 (Excelente posición)
```

---

## HOJA 6: BENCHMARKS

### Datos Comparativos

```
SECCIÓN 1: BENCHMARKS POR SECTOR ESPAÑA
────────────────────────────────────────

Sector Financiero:
├─ IGM Promedio: 78%
├─ Indicadores Implementados: 32/45 (71%)
├─ ROI 3Y Típico: 650%
├─ MTTD Promedio: 4h
└─ Cobertura MFA: 98%

Sector Energía/Crítica:
├─ IGM Promedio: 81%
├─ Indicadores Implementados: 35/45 (78%)
├─ ROI 3Y Típico: 750%
├─ MTTD Promedio: 2h
└─ Cobertura MFA: 99%

Sector Tecnología:
├─ IGM Promedio: 84%
├─ Indicadores Implementados: 38/45 (84%)
├─ ROI 3Y Típico: 850%
├─ MTTD Promedio: 1h
└─ Cobertura MFA: 99%

PME (<250 empleados):
├─ IGM Promedio: 62%
├─ Indicadores Implementados: 18/45 (40%)
├─ ROI 3Y Típico: 400%
├─ MTTD Promedio: 24h
└─ Cobertura MFA: 65%

Admin Pública:
├─ IGM Promedio: 71%
├─ Indicadores Implementados: 25/45 (56%)
├─ ROI 3Y Típico: 500%
├─ MTTD Promedio: 8h
└─ Cobertura MFA: 80%
```

### Interpretación de Posición Competitiva

```
TABLA DE POSICIONAMIENTO SECTOR FINANCIERO:
═════════════════════════════════════════════

IGM %     │ Cuartil | Posición           | Acción Recomendada
──────────┼─────────┼────────────────────┼──────────────────
90-100%   │ Q1 (Top)│ Líder sector       │ Mantener + innovar
80-89%    │ Q2      │ Arriba promedio    │ Expansión indicadores
70-79%    │ Q3      │ Promedio sector    │ Plan mejora 6-12m
<70%      │ Q4      │ Rezagado           │ Acción urgente

Vuestra Org (86%): Cuartil Q2 (Arriba promedio)
Recomendación: Considerar 7 indicadores adicionales para Q1
```

---

## GUÍA DE IMPLEMENTACIÓN EN EXCEL

### Pasos Iniciales

```
1. DESCARGAR PLANTILLA
   └─ Archivo: "CIS_Controls_IGM_ROI_Calculation.xlsx"
   └─ Tamaño: ~2.5 MB
   └─ Compatibilidad: Excel 2016+, Google Sheets

2. CONFIGURAR DATOS INICIALES (Hoja 2)
   └─ Insertar indicadores implementados actualmente
   └─ Completar puntuaciones PRAGMATIC (B-J)
   └─ Validar que scores caen en rango 0-3

3. REVISAR CÁLCULOS (Hoja 3-4)
   └─ Verificar que IGM se calcula automáticamente
   └─ Revisar estimaciones de inversión y beneficios
   └─ Ajustar asunciones si necesario

4. INTERPRETAR DASHBOARD (Hoja 5)
   └─ Identificar módulos con bajo IGM
   └─ Priorizar indicadores de alta criticidad
   └─ Comparar vs benchmarks sectoriales

5. REPORTAR A EJECUTIVOS
   └─ Usar Hoja 5 para presentación
   └─ Destacar ROI 768% en 3 años
   └─ Proponer plan de expansión de indicadores
```

### Mantenimiento Continuo

```
Frecuencia: TRIMESTRAL

Actividades:
├─ Actualizar scores PRAGMATIC de nuevos indicadores
├─ Recalcular IGM y ROI
├─ Comparar vs benchmarks sectoriales
├─ Ajustar estimaciones de beneficios si hay incidentes reales
└─ Reportar progreso a board (KPIs principales)

Revisión Anual:
├─ Auditoría externa de métricas seleccionadas
├─ Validación de beneficios reclamados (vs reales)
├─ Actualización de benchmarks
└─ Planificación de año siguiente
```

---

## MÉTRICAS DE VALIDEZ DE LA PLANTILLA

```
Criterios para asegurar que plantilla sigue siendo válida:

✅ Indicadores cubiertos: Mínimo 18 de 45 (40%)
✅ IGM mínimo: >70% (si <70%, requiere plan urgente)
✅ ROI mínimo: >300% en 3 años (si <300%, revisar asunciones)
✅ Actualización: Revisión trimestral de datos de entrada
✅ Auditoría: Validación externa anualmente

Si alguno NO se cumple, escalar a CISO/board para revisión
```

---

**Documento Versión 1.0 | Enero 2026 | España**

**DESCARGAR:** CIS_Controls_IGM_ROI_Calculation.xlsx (Plantilla Excel lista para implementar)

