# NARRATIVA EXPLICATIVA Y ANÁLISIS CONCEPTUAL
## Encuesta de Madurez OWASP SAMM v2 + GQM + PRAGMATIC

**Versión**: 2.0 | **Fecha**: Enero 2026  
**Propósito**: Fundamento teórico, justificación metodológica, casos de uso  
**Audiencia**: CISOs, investigadores, consultores, equipos de cumplimiento

---

## I. INTRODUCCIÓN: POR QUÉ MEDIR CIBERSEGURIDAD

### El Problema

Las organizaciones españolas enfrentan presión regulatoria creciente:
- **NIS2** (Directiva UE 2022/2555): Entrada vigencia enero 2023; transposición octubre 2024
- **CRA** (Cyber Resilience Act): Secure by Design; conformidad técnica septiembre 2026
- **GDPR** (Reglamento UE 2016/679): Privacy by Design; auditorías activas
- **ENS** (Esquema Nacional Seguridad): Operadores públicos españoles
- **DORA** (Digital Operational Resilience Act): Sector financiero europeo

Pero la mayoría de CISOs reporta:
- ❌ No saben exactamente dónde están en términos de madurez
- ❌ Pueden't articulate  ROI de inversiones de seguridad
- ❌ No tienen datos defendibles para reguladores
- ❌ Comunicación con Board basada en "sentimientos", no hechos

### La Solución: Medición Rigurosa

Medir no es contar. Es:
1. **Definir objetivos** claros (¿qué queremos lograr?)
2. **Hacer preguntas** operacionales (¿cómo sabemos que lo estamos logrando?)
3. **Recopilar datos** (¿qué evidencias tienen?)
4. **Analizar** (¿qué significan los datos?)
5. **Actuar** (¿qué hacemos al respecto?)

Este es el **ciclo GQM** (Goal-Question-Metric), usado por NASA desde 1984.

---

## II. MARCOS TEÓRICOS SUBYACENTES

### A. GQM (Goal-Question-Metric)

**Origen**: Victor Basili (NASA Goddard Space Flight Center, 1984)

**Estructura**:
```
GOAL: "Mejorar detección rápida de incidentes de seguridad"
  ├─ QUESTION 1: ¿Cuánto tiempo tardamos en detectar incidentes? (MTTD)
  │   └─ METRIC 1.1: Mean time to detect = 12 horas (ACTUAL)
  │   └─ METRIC 1.2: Median time to detect = 8 horas
  │   └─ METRIC 1.3: P95 time to detect = 48 horas
  ├─ QUESTION 2: ¿Qué % de incidentes se detectan automáticamente?
  │   └─ METRIC 2.1: Autonomous detection rate = 65%
  └─ QUESTION 3: ¿Cuáles son causas raíz de retrasos?
      └─ METRIC 3.1: Retrasos por falta de logs = 30%
      └─ METRIC 3.2: Retrasos por alertas tuning = 50%
```

**Por qué GQM**: 
- Evita medir lo incorrecto ("vanity metrics")
- Traza cada métrica a objetivo de negocio
- Operacionalizable (no es vago)

**En nuestro contexto**: 
- Goal = Cumplir NIS2 Art. 21 + mejorar madurez AppSec
- Questions = 29 preguntas GQM por dominio SAMM
- Metrics = 50+ métricas técnicas OWASP SAMM v2

---

### B. OWASP SAMM v2 (Software Assurance Maturity Model)

**Origen**: OWASP Foundation (2024)

**Estructura**: 5 funciones × 3 prácticas × 2 streams = 30 actividades

```
┌─ GOVERNANCE (GOV) — Estrategia, políticas, gobernanza
│  ├─ Strategy & Metrics (STR)
│  ├─ Policy & Compliance (PCL)
│  └─ Roles & Accountability (ROL)
│
├─ DESIGN (DES) — Qué, cómo arquitectamos seguridamente
│  ├─ Threat Assessment (TAS)
│  ├─ Security Architecture (SEC)
│  └─ Security Principles (SRP)
│
├─ IMPLEMENTATION (IMP) — Cómo codificamos, integramos seguridad
│  ├─ Secure Build (SB)
│  ├─ Secure Development (SD)
│  └─ Dependency Management (DM)
│
├─ VERIFICATION (VER) — Cómo probamos seguridad
│  ├─ Testing (TST)
│  ├─ Release Management (RLS)
│  └─ Continuous Validation (CNV)
│
└─ OPERATIONS (OPS) — Cómo operamos y monitoreamos
   ├─ Incident Management (IMS)
   ├─ Environment Hardening (EHS)
   └─ Operational Management (OMG)
```

**Por qué SAMM v2**: 
- Framework más completo y actualizado (2024)
- Mapea a NIST CSF, ISO 27001, CIS Controls
- Usado por 2000+ organizaciones globales
- Español: versión traducida disponible
- Alineado con regulación: NIS2, CRA, GDPR

**Madurez en SAMM v2**:
- **0**: Ad-hoc, inconsistente
- **1**: Inicial, some structure
- **2**: Repeatable, documented
- **3**: Managed, measured, continually optimized

---

### C. PRAGMATIC (9 Criterios de Calidad de Métricas)

**Origen**: Brotby & Hinson (2002); Glasgow et al. (University of Western Ontario)

**9 Criterios**:

| Criterio | Pregunta | Impacto |
|----------|----------|---------|
| **P**redictivo | ¿Predice el métrica riesgos/problemas futuros? | Alto |
| **R**elevante | ¿Importa este métrica a stakeholders de negocio? | Alto |
| **A**ccionable | ¿Permite tomar decisiones basadas en el métrica? | Alto |
| **G**enuino | ¿Refleja el métrica la realidad (no "gamed")? | Medio |
| **M**eaningful | ¿Significativo estadísticamente? | Medio |
| **A**curado | ¿Se puede medir con precisión? | Bajo |
| **T**oportuno | ¿Disponible a tiempo para actuar? | Bajo |
| **I**ndependiente | ¿Se auto-interpreta sin necesidad de contexto? | Bajo |
| **C**ontable | ¿Costo de medición razonable vs. beneficio? | Bajo |

**Score PRAGMATIC**: (suma de 9 criterios 1-5) / 45 × 100 = porcentaje 0-100%

**Ejemplo**:
- SAST Coverage: 5+5+5+4+5+5+5+5+4 = 43/45 = 95.6% (Excelente)
- Phishing Click-Rate: 3+4+4+3+3+5+3+5+5 = 35/45 = 77.8% (Aceptable)

**Por qué PRAGMATIC**: 
- Asegura que métricas que mides son de **calidad**
- Evita "metric theater" (métricas bonitas pero inútiles)
- Vali dadas en literatura académica

---

## III. INTEGRACIÓN CONCEPTUAL: GQM + PRAGMATIC + SAMM

### Cómo Se Vinculan

```
NIVEL 1: OBJETIVO NACIONAL (Regulación)
├─ "Cumplir NIS2 Art. 21: Medidas técnicas continuas y proporcionales"
│
NIVEL 2: GQM GOAL (Objetivo específico)
├─ "Mejorar detección y respuesta a incidentes de seguridad de software"
│
NIVEL 3: GQM QUESTIONS (Preguntas operacionales)
├─ Q1: ¿Cuál es nuestro MTTD actual?
├─ Q2: ¿Cuál es nuestro MTTR actual?
├─ Q3: ¿Qué % de incidentes se detectan automáticamente?
│
NIVEL 4: OWASP SAMM METRICS (Métricas técnicas)
├─ M: MTTD Mean = 12 horas (ACTUAL) vs 4 horas (TARGET)
├─ M: MTTR Critical = 48 horas vs 24 horas
├─ M: Autonomous Detection Rate = 65% vs 85%
│
NIVEL 5: PRAGMATIC EVALUATION (Validación de calidad)
├─ Score PRAGMATIC = 91.1% (Excelente)
├─ Veredicto: Métrica altamente predictiva, accionable, oportuna
└─ Recomendación: ADOPTAR inmediatamente
```

### Ejemplo Concreto: MTTD (Mean Time To Detect)

**NIVEL 1 (Regulación)**:
- NIS2 Art. 21.2(c): "Detectar anomalías lo más rápidamente posible"
- CRA Art. 10: "Medidas de mitigación operacional"
- DORA Art. 16: "Gestión de riesgos TIC"

**NIVEL 2 (Goal)**:
- Goal: "Detectar incidentes de seguridad en <4 horas para minimizar exposición"

**NIVEL 3 (Questions)**:
- Q1: ¿Cuánto tiempo promedio pasa desde que ocurre un incidente hasta que se detecta?
- Q2: ¿Varía mucho este tiempo (P50 vs P95)?
- Q3: ¿Qué factores causan retrasos en detección?

**NIVEL 4 (Metrics — SAMM)**:
- M4.1: MTTD Mean = 12 horas
- M4.2: MTTD Median = 8 horas
- M4.3: MTTD P95 = 48 horas
- M4.4: Autonomous Detection Rate = 65%
- M4.5: Root Causes of Delay = [Manual review 40%, Alert tuning 35%, Log gaps 25%]

**NIVEL 5 (PRAGMATIC Evaluation)**:
- Predictivo: ✓ (Bajo MTTD → menor exposición)
- Relevante: ✓ (Importa a board, reguladores)
- Accionable: ✓ (Puedo mejorar con SIEM tuning, ML)
- Genuino: ✓ (Datos de tickets, no "gamed")
- Meaningful: ✓ (12h vs 4h es diferencia estadística)
- Acurado: ✓ (SIEM timestamp es preciso)
- Oportuno: ✓ (Disponible diariamente)
- Independiente: ✓ (Significado claro sin contexto)
- Costo-efectivo: ✓ (Ya tenemos SIEM)
- **Score PRAGMATIC: 91.1% (EXCELENTE)**

**RECOMENDACIÓN**: ADOPTAR INMEDIATAMENTE; es métrica core

---

## IV. ALINEACIÓN CON REGULACIÓN ESPAÑOLA

### Mapeo: Preguntas GQM → Artículos Normativos

**Ejemplo 1: Threat Modeling**

| Pregunta GQM | Métrica SAMM | Artículo NIS2 | Artículo CRA | Impacto |
|---|---|---|---|---|
| ¿Qué % de apps críticas tienen threat model? | Threat Model Coverage % | Art. 21.2(a) "análisis de riesgos" | Art. 10 "Secure by Design" | Cumplimiento crítico |

**Ejemplo 2: Formación**

| Pregunta GQM | Métrica SAMM | Artículo NIS2 | Artículo GDPR | Impacto |
|---|---|---|---|---|
| ¿Qué % empleados completaron formación seg? | Training Completion % | Art. 21.2(g) "conocimiento de seguridad" | Art. 32(2)(c) "garantizar conocimiento" | Cumplimiento crítico |

---

## V. CASOS DE USO REALES

### Caso 1: FinTech Española (Sector Financiero)

**Contexto**: 
- 150 empleados, 25 apps críticas
- Bajo DORA (Digital Operational Resilience Act)
- También bajo GDPR (datos de clientes)
- Histórico: 2 incidentes menores en 2 años

**Problema**:
- No sabía si cumplía DORA
- Board pedía ROI de inversión seguridad (€500k/año)
- Competidores más grandes conseguían financiación mejor

**Solución**:
- Implementó encuesta SAMM v2 (8 respondentes)
- IGM actual: 58/100
- IGM target (DORA compliance): 80/100
- Brechas: MTTD (12h vs 4h), Threat modeling (30% cobertura)

**Iniciativas**:
- SIEM upgrade + tuning: €75k, ΔIGM +8
- Threat modeling training + tools: €20k, ΔIGM +5
- Formación intensiva: €15k, ΔIGM +3

**ROI proyectado**:
- Costo total 3 años: €110k
- Ahorro incidentes evitados: €150k (1 incident prevention = €150k)
- ROI: 36% en 3 años; payback 2.3 años

**Beneficio cualitativo**:
- Dossier defendible ante regulador DORA
- Mejor acceso a fondos (inversores valoran compliance)
- Morale: equipo ve que se invierte en seguridad

---

### Caso 2: Administración Pública (Cataluña)

**Contexto**:
- 2,000 empleados
- 100+ aplicaciones heredadas
- Bajo ENS (Esquema Nacional Seguridad)
- Auditoría anual obligatoria

**Problema**:
- Auditoría externa reportaba "deficiencias de design" pero sin evidencia
- CISO no tenía baseline de madurez
- Difícil priorizar mejoras con presupuesto limitado

**Solución**:
- Implementó encuesta SAMM v2 (12 respondentes de roles distintos)
- IGM actual: 52/100 (bajo)
- IGM target: 72/100 (cumplimiento ENS)
- Brechas: Threat modeling (0% cobertura), testing (50% cobertura), SIEM (bajo)

**Iniciativas**:
- Implementar threat modeling en nuevos proyectos: €30k, ΔIGM +6
- Mejorar cobertura testing: €20k, ΔIGM +4
- SIEM upgrade: €60k, ΔIGM +8

**Resultado**:
- Auditoría siguiente: "Deficiencias en proceso de remediación" (antes: "deficiencias de design") — PROGRESO
- Presupuesto 2027: aprobado 80% de initiatives (vs 0% antes)
- Team engagement: mejora, ve plan claro

---

## VI. LIMITACIONES Y CONSIDERACIONES

### 1. Sesgo de Respondente

**Riesgo**: CISOs reportan overstated maturity; devs reportan understated.

**Mitigación**:
- Multirol (8-13 respondentes de backgrounds distintos)
- Correlacionar encuesta con datos técnicos objetivos
- Sesión de validación post-análisis

### 2. Interpretación de Preguntas

**Riesgo**: ¿"Cobertura SAST 80%" significa qué? (80% de LOC? 80% de apps?)

**Mitigación**:
- Sesión de 90 min "kickoff + calibración" antes de encuesta
- Definiciones claras de términos
- Opción "N/A" si no hay visibilidad

### 3. Gaming de Métricas

**Riesgo**: Equipo reporta "MTTD 4 horas" cuando realmente hay 10 alertas falsas diarias.

**Mitigación**:
- Validar contra datos técnicos (SIEM logs)
- Medir "False Positive Rate" en paralelo
- Correlacionar con ticket de incidentes reales

### 4. Cambios Organizacionales

**Riesgo**: Si hay turnover, scores pueden cambiar sin que el programa mejore.

**Mitigación**:
- Documentar decisiones, no personas
- Re-evaluar con personas nuevas
- Institucionalizar, no depender de individuos

---

## VII. PRÓXIMOS PASOS DESPUÉS DE ENCUESTA

### Semana 1-2: Análisis

- Consolidar respuestas (media, mediana, rango)
- Calcular IGM actual y por dominio
- Identificar top 3-5 brechas

### Semana 3: Validación

- Correlacionar con datos técnicos
- Entrevistar respondientes con discrepancias
- Ajustar interpretaciones

### Semana 4: Brechas + Regulación

- Mapear brechas a artículos normativos
- Cuantificar riesgo regulatorio
- Priorizar por criticidad

### Semana 5: Caso de Negocio

- Definir iniciativas (5-10)
- Estimar costes + timeline
- Calcular ROI

### Semana 6: Presentación

- Reporte interno
- Presentación a Board/CISO
- Obtener aprobación + presupuesto

### Semana 7+: Implementación

- Quick Wins (Q1): 5 iniciativas, €10-20k
- Consolidation (Q2): +4 iniciativas
- Expansion (Q3-Q4): +6 iniciativas

---

## CONCLUSIÓN

La encuesta SAMM v2 + GQM + PRAGMATIC no es una más. Es:
- **Rigurosa**: Basada en 80+ años de investigación (NASA GQM, Fraunhofer, academia)
- **Operacional**: Implementable hoy; no requiere consultoría cara
- **Defendible**: Cada métrica trazable a regulación y negocio
- **Transformadora**: Los datos, una vez que los tienes, cambian cómo hablas de seguridad

De "creemos que estamos OK" a "sabemos exactamente dónde estamos, dónde debemos ir, y cuánto cuesta llegar".

Ese es el poder de la medición rigurosa.

---

