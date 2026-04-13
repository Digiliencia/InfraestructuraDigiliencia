# PLANTILLA EXCEL PARA CÁLCULO DE IGM Y ROI
## Kit de Herramientas Cuantitativas para Seguimiento

**Versión:** 1.0  
**Fecha:** Enero 2026  
**Formato:** Instrucciones para reproducir en Google Sheets o Microsoft Excel

---

## PARTE 1: HOJA "SCORING" - Cálculo IGM

### Estructura Recomendada

```
ENCUESTA INTEGRALBERSEGURIDAD - SCORING IGM
Organización: ________________
Fecha Evaluación: ________________
Responsable: ________________
Facilitador: ________________

SECCIÓN 1: GOBERNANZA Y RIESGO (GR)
─────────────────────────────────────────────────────────
Pregunta                              | Puntuación (1-5) | Nivel | Notas
─────────────────────────────────────────────────────────
GR-01: Política Riesgos              | ___             | ___  | ____________
GR-02: Conformidad Regulatoria       | ___             | ___  | ____________
GR-03: CISO Autonomía                | ___             | ___  | ____________
GR-04: Riesgos Terceros              | ___             | ___  | ____________
─────────────────────────────────────────────────────────
SUBTOTAL GR (4 items)                | ___             | ___  | Promedio: ___
─────────────────────────────────────────────────────────

SECCIÓN 2: GESTIÓN VULNERABILIDADES (GV)
─────────────────────────────────────────────────────────
GV-01: Programa Estructura           | ___             | ___  | ____________
GV-02: Cobertura Escaneo            | ___             | ___  | ____________
GV-03: Adopción EPSS                | ___             | ___  | ____________
GV-04: Priorización Integrada       | ___             | ___  | ____________
GV-05: MTTR Críticas                | ___             | ___  | ____________
GV-06: Validación Remediación       | ___             | ___  | ____________
GV-07: Eficiencia Operacional       | ___             | ___  | ____________
─────────────────────────────────────────────────────────
SUBTOTAL GV (7 items)                | ___             | ___  | Promedio: ___
─────────────────────────────────────────────────────────

[Continuar para PT, SI, RI, CC...]

═════════════════════════════════════════════════════════
ÍNDICE DE GOBERNANZA DE MADUREZ (IGM) GLOBAL
═════════════════════════════════════════════════════════

Promedio GR: ___  (4 preguntas)
Promedio GV: ___  (7 preguntas)
Promedio PT: ___  (6 preguntas)
Promedio SI: ___  (6 preguntas)
Promedio RI: ___  (6 preguntas)
Promedio CC: ___  (7 preguntas)

IGM = (GR + GV + PT + SI + RI + CC) / 6 = ___

CLASIFICACIÓN IGM:
┌─ 1.0-1.5: Crítica
├─ 1.5-2.5: Débil
├─ 2.5-3.5: Aceptable
├─ 3.5-4.5: Buena
└─ 4.5-5.0: Excelente
```

### Fórmulas Excel Recomendadas

```
Para calcular Promedio GR (asumiendo respuestas en celdas B2:B5):
=AVERAGE(B2:B5)

Para clasificación automática IGM (en celda B30):
=IF(B30>=4.5,"Excelente",IF(B30>=3.5,"Buena",IF(B30>=2.5,"Aceptable",IF(B30>=1.5,"Débil","Crítica"))))

Para colores condicionales (Formato Condicional):
- Rojo: <1.5
- Naranja: 1.5-2.5
- Amarillo: 2.5-3.5
- Verde claro: 3.5-4.5
- Verde oscuro: 4.5-5.0
```

---

## PARTE 2: HOJA "ANÁLISIS DE GAPS"

### Estructura Recomendada

```
ANÁLISIS DE BRECHAS (GAP ANALYSIS)
════════════════════════════════════════════════════════

Dominio          | Actual | Target | Gap  | % Mejora | Prioridad
─────────────────────────────────────────────────────────────
Gobernanza (GR)  | ___    | 3.8    | ___  | ____%    | [ROJO/AMARILLO/VERDE]
Vulnerabilidades | ___    | 3.8    | ___  | ____%    | [ROJO/AMARILLO/VERDE]
Pen Testing (PT) | ___    | 3.5    | ___  | ____%    | [ROJO/AMARILLO/VERDE]
Monitoreo (SI)   | ___    | 3.8    | ___  | ____%    | [ROJO/AMARILLO/VERDE]
Respuesta (RI)   | ___    | 3.6    | ___  | ____%    | [ROJO/AMARILLO/VERDE]
Capacitación (CC)| ___    | 3.5    | ___  | ____%    | [ROJO/AMARILLO/VERDE]
─────────────────────────────────────────────────────────────
IGM GLOBAL       | ___    | 3.68   | ___  | ____%    | [ROJO/AMARILLO/VERDE]

FÓRMULAS:
Gap = Target - Actual
% Mejora = Gap / Actual × 100
Prioridad automática:
- Gap >0.5 (>20% mejora): ROJO (Crítica)
- Gap 0.3-0.5 (10-20% mejora): AMARILLO (Alta)
- Gap <0.3 (<10% mejora): VERDE (Mediana)
```

---

## PARTE 3: HOJA "ROI & BUSINESS CASE"

### Modelo de Cálculo ROSI (Return On Security Investment)

```
CÁLCULO DE ROI EN CIBERSEGURIDAD
════════════════════════════════════════════════════════

PASO 1: Cuantificar Riesgo Actual (Annual Loss Expectancy - ALE)
─────────────────────────────────────────────────────────

Tipo de Evento de Riesgo        | Probabilidad | Impacto Financiero | ALE
─────────────────────────────────────────────────────────────────────
Data Breach (externos)          | ___%         | €_________         | €________
Ransomware                      | ___%         | €_________         | €________
Incidente de disponibilidad     | ___%         | €_________         | €________
Fraude interno                  | ___%         | €_________         | €________
Cumplimiento regulatorio (multa)| ___%         | €_________         | €________
Reputacional (cliente churn)    | ___%         | €_________         | €________
─────────────────────────────────────────────────────────────────────
ALE TOTAL = Σ (Probabilidad × Impacto) = €________

PASO 2: Estimar Mitigación por Mejora IGM
─────────────────────────────────────────────────────────

Mejora IGM: ___  (Ejemplo: 2.0 → 3.5 = +1.5 puntos)

Reducción de riesgos esperada por dominio:

Dominio                | Mejora    | Reducción Riesgo | Justificación
────────────────────────────────────────────────────────────────────
GR (Gobernanza)        | ___       | ____%            | Decisiones mejor informadas
GV (Vulnerabilidades)  | ___       | ____%            | EPSS reduce falsos positivos 50%
PT (Pen Testing)       | ___       | ____%            | Detección de gaps antes explotación
SI (SIEM)              | ___       | ____%            | MTTD reducido → escalada evitada
RI (Incidentes)        | ___       | ____%            | Respuesta rápida → daño limitado
CC (Capacitación)      | ___       | ____%            | Phishing reduction → menos breaches
────────────────────────────────────────────────────────────────────
Mitigación Media Esperada = __% de ALE

RIESGO RESIDUAL = ALE × (1 - Mitigación%) = €________
REDUCCIÓN CUANTIFICADA = ALE - Riesgo Residual = €________

PASO 3: Costo de Mejora
─────────────────────────────────────────────────────────

Inversión Requerida                           | Costo Anual
─────────────────────────────────────────────────────────
Herramientas (SIEM, SOAR, VM tools)          | €________
Personal especializado (contratación/retención)| €________
Consultoría/Servicios profesionales          | €________
Capacitación y concienciación                | €________
Cambios de procesos y políticas              | €________
─────────────────────────────────────────────────────────
COSTO TOTAL INVERSIÓN (Año 1) = €________

PASO 4: Cálculo de ROSI
─────────────────────────────────────────────────────────

ROSI = (Reducción Cuantificada - Costo Inversión) / Costo Inversión × 100%

ROSI = (€________ - €________) / €________ × 100% = ____%

INTERPRETACIÓN:
- ROSI > 200%: Excelente ROI (cada €1 invierte retorna €3+)
- ROSI 100-200%: Muy bueno (cada €1 invierte retorna €2-3)
- ROSI 50-100%: Bueno (cada €1 invierte retorna €1.50-2)
- ROSI 0-50%: Moderado (cada €1 invierte retorna €1-1.50)
- ROSI < 0%: Negativo (inversión > beneficio percibido)

ROSI CALCULADO = __% → [Excelente / Muy Bueno / Bueno / Moderado / Negativo]

PERIODO PAYBACK = Costo Inversión / (Reducción Cuantificada / 12) meses = ___ meses
```

### Ejemplo Real Completo

```
CASO: Startup SaaS España - Mejora IGM 2.0 → 3.5 (+1.5 puntos)

PASO 1: ALE ACTUAL
─────────────────────────────────────────────────────────
Data Breach (10% prob, €500K impacto) = €50K
Ransomware (5% prob, €200K impacto) = €10K
Indisponibilidad (20% prob, €100K impacto) = €20K
Cumplimiento GDPR multa (2% prob, €400K impacto) = €8K
─────────────────────────────────────────────────────────
ALE TOTAL = €88K

PASO 2: MITIGACIÓN ESPERADA (IGM 2.0 → 3.5)
─────────────────────────────────────────────────────────
GV: Adopción EPSS → 40% reducción Data Breach = -€20K
SI: SIEM implementado → 60% reducción Ransomware = -€6K
RI: Plan formalizado → 50% reducción Indisponibilidad = -€10K
CC: Capacitación → 30% reducción GDPR multa = -€2.4K
───────────────────────────────────────────────────────
Mitigación Total = €38.4K (43.6% de ALE)
Riesgo Residual = €49.6K

PASO 3: COSTO INVERSIÓN
─────────────────────────────────────────────────────────
EPSS integración (1 dev × 2 semanas) = €3K
SIEM piloto (SaaS 6 meses) = €6K
Plan IR formalización = €2K
Capacitación phishing + platform = €4K
───────────────────────────────────────────────────────
Costo Total Año 1 = €15K

PASO 4: ROSI
─────────────────────────────────────────────────────────
ROSI = (€38.4K - €15K) / €15K × 100% = 156%

RESULTADO: Excelente ROI. Cada €1 invertido retorna €2.56
Payback: 4.7 meses

CONCLUSIÓN: Inversión €15K genera €38.4K en valor de mitigación.
Decisión: APROBADO - Maximiza presupuesto limitado con alto impacto.
```

---

## PARTE 4: HOJA "DASHBOARD & TRACKING"

### Seguimiento Trimestral de Progreso

```
DASHBOARD DE SEGUIMIENTO - IGM vs TARGET
═════════════════════════════════════════════════════════════════

Periodo: 2026-Q1 Responsable: _____ Última Actualización: _______

GRÁFICO: Evolución IGM
────────────────────────────────────────────────────────
Baseline (Ene 2026):    2.0 ████░░░░░░░░░░░░░░░░░░░░░░░
Q1 Target (Mar 2026):  2.3 ██████░░░░░░░░░░░░░░░░░░░░░░
Q1 Actual (Mar 2026):  2.2 █████░░░░░░░░░░░░░░░░░░░░░░░
Q2 Target (Jun 2026):  2.7 ███████░░░░░░░░░░░░░░░░░░░░░
Q3 Target (Sep 2026):  3.1 ████████░░░░░░░░░░░░░░░░░░░░
Q4 Target (Dic 2026):  3.5 ██████████░░░░░░░░░░░░░░░░░░

EVOLUCIÓN POR DOMINIO (Gráfico Radar)
────────────────────────────────────────────────────────
                Baseline | Q1 Actual | Q2 Target
        GR         2.0   |   2.1    |   2.5
        GV         1.8   |   2.2    |   2.8
        PT         1.5   |   1.8    |   2.3
        SI         2.2   |   2.3    |   2.8
        RI         2.1   |   2.2    |   2.6
        CC         2.3   |   2.2    |   2.7

KPIs OPERACIONALES CLAVE
────────────────────────────────────────────────────────
KPI                      | Baseline | Q1 Actual | Q1 Target | Estado
──────────────────────────────────────────────────────────────────
Cobertura Escaneo (%)    |   30%    |   45%     |   50%     | ✓ EN TRACK
EPSS Adoption (%)        |   15%    |   40%     |   60%     | ⚠ ATRÁS
MTTR Críticas (días)     |   35     |   28      |   20      | ⚠ ATRÁS
SIEM MTTD (horas)        |   24     |   18      |   12      | ✓ EN TRACK
IR Ejercicios (qty/año)  |    0     |   2       |   4       | ✓ EN TRACK
Phishing Click Rate (%)  |   40%    |   22%     |   15%     | ✓ EN TRACK
Tasa Cumpl. Capacitación |   60%    |   72%     |   80%     | ✓ EN TRACK

INVERSIÓN ACUMULADA vs PRESUPUESTO
────────────────────────────────────────────────────────
Categoría                | Presupuesto | Gastado   | % Utilización
──────────────────────────────────────────────────────────────────
Herramientas/SaaS        |   €45K      |   €18K    |   40%
Personal especializado   |   €60K      |   €22K    |   37%
Consultoría              |   €30K      |   €8K     |   27%
Capacitación            |   €15K      |   €4K     |   27%
────────────────────────────────────────────────────────────────
TOTAL 2026              |   €150K     |   €52K    |   35%

RIESGOS Y MITIGACIONES
────────────────────────────────────────────────────────
Riesgo Identificado              | Probabilidad | Impacto | Mitigación
────────────────────────────────────────────────────────────────────────
Rotación personal CISO           | Media        | Alta    | Retención +20%
Retraso en herramientas VM       | Media        | Medio   | Vendor soporte
SIEM tuning lento (FP)           | Alta         | Bajo    | Consultoría ML
────────────────────────────────────────────────────────────────────────

PROXIMAS ACCIONES (Q2 2026)
────────────────────────────────────────────────────────
[ ] Completar integración EPSS en herramienta VM
[ ] Iniciar piloto SOAR para automatización
[ ] Realizar ejercicio IR tabletop (Abril)
[ ] Lanzar campaña phishing mensual (Marzo)
[ ] Formalizar SLA de remediación (Marzo)

FIRMADO: _________________ Fecha: _________________
REVISADO: ________________ Fecha: _________________
```

---

## CONCLUSIÓN: MODELO DE DATOS

Estructura de datos recomendada para Excel/Sheets:

| Hoja | Propósito | Actualización |
|---|---|---|
| **Scoring** | Captura de puntuaciones por pregunta | Anual (o cuando cambios significativos) |
| **Gap Analysis** | Cálculo automático de brechas | Inmediata (linked a Scoring) |
| **ROI & Business Case** | Cuantificación financiera | Anual + ajustes trimestrales |
| **Dashboard & Tracking** | Seguimiento operativo | Trimestral (o mensual si deseable) |

**Referencia:**
- Mantener todas hojas en archivo consolidado (una pestaña por hoja)
- Usar linkage automático entre hojas (fórmulas con referencias SHEET())
- Publicar Dashboard a liderazgo mensualmente (o trimestral)
- Guardar copias históricas para benchmarking longitudinal

---

*Plantilla desarrollada por Consorcio de Científicos de Datos y Estrategas de Ciberseguridad*  
*Enero 2026*
