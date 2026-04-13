# PLANTILLA EXCEL: CÁLCULO IGM Y ROI (ADAM 2.0)
## Guía de Implementación con Fórmulas Detalladas

**Versión:** 2.0  
**Fecha:** Enero 2026  
**Plataformas:** Excel, Google Sheets, LibreOffice Calc  
**Automatización:** 80% fórmulas, 20% entrada manual

---

## ESTRUCTURA DE HOJAS RECOMENDADA

### Hoja 1: "ENTRADA INDICADORES"

**Propósito:** Recopilar valores brutos de 25 indicadores ADAM

**Estructura:**

| Columna | Descripción | Tipo | Ejemplo |
|---------|-------------|------|---------|
| A | ID Indicador (1-25) | ID | 1, 2, 3... |
| B | Nombre Indicador | Texto | "CISO Reporta CEO" |
| C | Dominio NIST (GV/ID/PR/DE/RS/RC) | Dropdown | GV |
| D | Valor Medido | Numérico/Texto | 1 (si=CEO), 0 (no) |
| E | Unidad | Texto | Sí/No, %, días, €... |
| F | Fecha Medición | Fecha | 2026-01-15 |
| G | Fuente Dato | Texto | CMDB, SIEM, Auditor... |
| H | Confianza Medición (1-5) | Numérico | 5 (alta) |

**Fórmula Validación (Columna I):**
```
=IF(OR(D2="",E2=""),"INCOMPLETO","VÁLIDO")
```

---

### Hoja 2: "CONVERSIÓN A ESCALA 0-5"

**Propósito:** Convertir valores brutos a escala de madurez 0-5

**Mapeo Automático:**

| Indicador | Input | Conversión Fórmula | Output 0-5 |
|-----------|-------|-------------------|-----------|
| CISO Reporta CEO | Sí/No | =IF(D2="Sí",5,1) | 1 o 5 |
| % Cobertura Inventario | 0-100% | =(D2)/100)*5 | 0-5 |
| MTTD (minutos) | 0-1440 | =MAX(0, 5-(D2/60)) | 0-5 (inverso) |
| Vulnerabilidades Críticas | 0-50 | =MAX(0, 5-(D2/10)) | 0-5 (inverso) |
| Click Rate Phishing | 0-50% | =MAX(0, 5-(D2*5)) | 0-5 (inverso) |

**Lógica:**
- Indicadores "más es mejor" (ej: % cobertura): Escala lineal 0-100% → 0-5
- Indicadores "menos es mejor" (ej: MTTD): Inversa, con techo máximo

**Ejemplo Fórmula Compleja (MTTD):**
```
=IF(D2="","",IF(D2<=15, 5, IF(D2<=60, 4, IF(D2<=240, 3, IF(D2<=480, 2, IF(D2<=1440, 1, 0))))))
```

---

### Hoja 3: "CÁLCULO IGM POR DOMINIO"

**Propósito:** Calcular puntuación IGM para cada dominio NIST (6 dominios)

**Estructura:**

| Dominio | Indicadores | Fórmula Promedio | Score 0-5 | Ponderación | Score Ponderado |
|---------|------------|-----------------|-----------|-------------|---|
| **GV (Gobernar)** | 1-5 | =PROMEDIO(H2:H6) | 3.2 | 25% | 0.8 |
| **ID (Identificar)** | 6-10 | =PROMEDIO(H7:H11) | 3.4 | 20% | 0.68 |
| **PR (Proteger)** | 11-18 | =PROMEDIO(H12:H19) | 3.1 | 25% | 0.775 |
| **DE (Detectar)** | 19-22 | =PROMEDIO(H20:H23) | 2.8 | 15% | 0.42 |
| **RS (Responder)** | 23-25 | =PROMEDIO(H24:H26) | 3.3 | 10% | 0.33 |
| **RC (Recuperar)** | 26-28 | =PROMEDIO(H27:H29) | 3.5 | 5% | 0.175 |

**Ponderaciones Predefinidas (por criticidad operacional):**
- GV: 25% (gobierno impacta todos)
- ID: 20% (identificación base)
- PR: 25% (protección crítica)
- DE: 15% (detección desacoplada)
- RS: 10% (respuesta importante pero reactiva)
- RC: 5% (recuperación última línea)

**Fórmula IGM Total:**
```
=SUMPRODUCT(Score_Dominio, Ponderación) / SUMA(Ponderación)
```

Resultado: IGM Score (0-5)

---

### Hoja 4: "MATURITY LEVEL"

**Propósito:** Convertir IGM a Nivel Madurez (0-4) + Riesgo Residual

**Tabla Conversión:**

| IGM Score | Maturity Level | Descripción | Riesgo Residual |
|-----------|---|---|---|
| 0.0 - 1.5 | 0 | Inicial (Ad-hoc) | 80% CRÍTICO |
| 1.6 - 2.5 | 1 | Inicial (Documentado) | 70% ALTO |
| 2.6 - 3.5 | 2 | Gestionada (Procesos) | 50% MEDIO-ALTO |
| 3.6 - 4.5 | 3 | Definida (Optimizada) | 30% MEDIO |
| 4.6 - 5.0 | 4 | Optimizada (IA/ML) | 10% BAJO |

**Fórmulas:**

```
Maturity Level:
=IF(IGM_Score<=1.5, 0, IF(IGM_Score<=2.5, 1, IF(IGM_Score<=3.5, 2, IF(IGM_Score<=4.5, 3, 4))))

Riesgo Residual (%):
=IF(Maturity=0, 80, IF(Maturity=1, 70, IF(Maturity=2, 50, IF(Maturity=3, 30, 10))))

Riesgo en €:
=ALE_Total * Riesgo_Residual_Porcentaje
```

---

### Hoja 5: "ANÁLISIS FAIR SIMPLIFICADO"

**Propósito:** Cuantificar riesgo en términos económicos (ALE)

**Estructura:**

| Factor de Riesgo | Valor | Fórmula | Resultado |
|---|---|---|---|
| **TEF** (Threat Event Frequency) | Asumido por sector | - | 5 eventos/año |
| **TCap** (Threat Capability) | 0-100% | - | 60% |
| **Vulnerabilidad** | 1-Cobertura ID | =1-Cobertura_Escaneo | 0.15 (85% cobertura) |
| **LM** (Loss Magnitude) | €/evento | Según activos | €500k promedio |
| | | | |
| **ALE (Annual Loss Expectancy)** | = TEF × TCap × Vuln × LM | =5*0.6*0.15*500000 | **€225,000** |

**Fórmula ALE por Dominio:**

```
ALE_Total = TEF * TCap * (1 - Vulnerabilidad_Mitigada) * Loss_Magnitude_Promedio
```

Donde:
- Vulnerabilidad_Mitigada = f(ID score, PR score, DE score)
- Loss_Magnitude_Promedio = histórico incidentes org

---

### Hoja 6: "ESCENARIOS ROI"

**Propósito:** Calcular ROSI para iniciativas de inversión

**Escenario 1: Implementación SIEM**

| Item | Fórmula | Valor |
|---|---|---|
| **ALE Actual** | Ver Hoja 5 | €225,000 |
| **Beneficio MTTD** | ALE × (MTTD actual - MTTD post) / MTTD actual | €100,000/año |
| **Costo Año 1** | Licencias + Impl | €200,000 |
| **Costo Año 2-3** | Operación | €80,000/año |
| **Beneficio Acumulado 3a** | Beneficio × 3 - Amort Impl | €300,000 - €200k = €100k neto |
| **ROSI 3 años** | (Beneficio Neto / Costo Total) × 100 | 50% (conservador) |

**Escenario 2: MFA Universal**

| Item | Fórmula | Valor |
|---|---|---|
| **Reducción Riesgo** | % Incidentes previo MFA × ALE | 35% × €225k = €78.75k |
| **Costo Año 1** | Licencia MFA × Users | €60,000 |
| **ROSI Año 1** | €78.75k / €60k | **131% (bueno)** |

**Plantilla General ROSI:**

```
ROSI = [(Beneficio Anual - Costo Anual) / Costo Año 1] × 100

Payback Period (meses) = (Costo Año 1 / Beneficio Mensual)
```

---

### Hoja 7: "BENCHMARKING SECTOR"

**Propósito:** Comparar IGM con organizaciones similares

**Estructura:**

| Organización | IGM | Maturity | Percentil | Sector | Tamaño | Gap vs. Org |
|---|---|---|---|---|---|---|
| **Nuestra Org** | 2.92 | 2 | P40 | Industrial | 500 emp | - |
| **Benchmark Sector** | 3.07 | 2 | P50 | Industrial | 500+ emp | -0.15 |
| **Líder Sector** | 4.20 | 4 | P95 | Industrial | 5000+ emp | -1.28 |
| **PYME Promedio** | 2.15 | 1 | P25 | Todos | <200 emp | +0.77 |

**Fórmulas:**

```
Percentil = PERCENTRANK.INC(Rango_Benchmark, IGM_Nuestra_Org) × 100

Gap = IGM_Nuestra_Org - IGM_Benchmark

Posición Relativa: IF(IGM > Benchmark, "MEJOR", "PEOR")
```

---

### Hoja 8: "ROADMAP 18 MESES"

**Propósito:** Planificar iniciativas por trimestre con IGM proyectado

**Estructura:**

| Q | Iniciativa | Inversión | IGM Actual | IGM Post | Beneficio Estimado | ROI % |
|---|---|---|---|---|---|---|
| **Q1** | MFA + Políticas | €150k | 2.92 | 3.15 | €80k | 53% |
| **Q2-Q3** | SIEM + Pentest | €400k | 3.15 | 3.85 | €500k | 125% |
| **Q4-Q6** | Red Team + ZT | €300k | 3.85 | 4.10 | €350k | 117% |
| **Total 18m** | 12 inicitativas | €850k | 2.92 | 4.10 | €930k | 109% |

**Validación:**
- IGM crece ~0.6 puntos por trimestre (realista)
- ROI promedio >100% (justificable)
- Payback <1 año en algunos casos

---

## DASHBOARDS RECOMENDADOS

### Dashboard 1: "Estado General" (1 hoja)

**Elementos visuales:**
1. **Gauge Chart:** IGM Score (0-5) con zonas rojo/amarillo/verde
2. **KPI Cards:**
   - IGM: 2.92
   - Maturity: 2
   - Riesgo Residual: 50%
3. **Trend:** IGM último año (gráfico línea)

### Dashboard 2: "Dominios NIST" (1 hoja)

**Elementos visuales:**
1. **Radar Chart:** 6 ejes (GV/ID/PR/DE/RS/RC), zona exterior = benchmark
2. **Bar Chart:** Gaps vs benchmark (negativo = below target)
3. **Traffic Light:** Rojo/Amarillo/Verde por dominio

### Dashboard 3: "Financiero" (1 hoja)

**Elementos visuales:**
1. **Waterfall Chart:** ALE actual → ALE post-iniciativas
2. **Bar Stacked:** ROSI por iniciativa (Costo vs Beneficio)
3. **Timeline:** Roadmap 18m con hitos IGM

---

## GUÍA DE ENTRADA DE DATOS

### Entrada Manual (20% esfuerzo)

Estos 5 indicadores requieren input directo (no automáticos):

1. **CISO Reporta CEO** → Datos organigrama (Sí/No)
2. **Presupuesto Seguridad** → Finanzas (€ total)
3. **Análisis FAIR** → Consultor externo (score 1-5)
4. **RTO/RPO** → IT (documentado, horas)
5. **Histórico Incidentes** → ITSM (últimos 10 años)

### Entrada Automatizada (80% esfuerzo)

Estos 20 indicadores extraen datos de herramientas:

```
CMDB → Cobertura Inventario
Vulnerability Scanner → Vulnerabilidades críticas, CVSS
SIEM → MTTD, Falsos positivos
ITSM → Ciclo vida vulnerabilidades, MTTC, MTTR
Backup Tool → Pruebas backup exitosas
LMS → Capacitación %
MFA System → Cobertura MFA
Patch Manager → % Sistemas parchados
Phishing Platform → Click rate
```

---

## FRECUENCIA ACTUALIZACIÓN

| Métrica | Frecuencia | Esfuerzo |
|---|---|---|
| IGM completo | Trimestral | 20h |
| Indicadores operacionales (MTTD, Falsos+) | Mensual | 2h |
| Benchmarking | Semestral | 4h |
| Roadmap + ROI | Anual | 40h |

---

## VALIDACIÓN Y AUDITORÍA

### Validación Interna

- Revisar entrada de datos vs. fuentes
- Verificar fórmulas (test con valores conocidos)
- Chequear outliers (valores anormales)

### Auditoría Externa

- Muestra 10% de entrada de datos
- Recalcular IGM independientemente
- Verificar benchmarks vs. bases de datos auditor

---

## TEMPLATE DESCARGABLE

**Archivo:** `ADAM_IGM_ROI_Calculator_v2.0_[Español].xlsx`

**Contenido:**
- 8 hojas (Entrada → Dashboard)
- 150+ fórmulas pre-cargadas
- Validación de datos integrada
- Dashboard interactivo (3 vistas)

**Requisitos:** Excel 2016+ o Google Sheets (compatible 100%)

---

**Fin de Plantilla Excel ADAM 2.0**

*Descarga disponible en: [Repositorio]*
