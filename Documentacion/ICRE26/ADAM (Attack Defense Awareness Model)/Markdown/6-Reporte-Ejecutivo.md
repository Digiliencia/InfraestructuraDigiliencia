# PLANTILLA REPORTE EJECUTIVO
## Guía para Presentación PowerPoint/Documento Ejecutivo

**Versión:** 1.0 | Enero 2026  
**Audiencia:** C-Level, Junta Directiva, Auditores

---

## ESTRUCTURA REPORTE: 8 DIAPOSITIVAS (MÍNIMO)

---

### **DIAPOSITIVA 1: PORTADA**

**Elementos:**
- Logotipo Organización
- Título: "Evaluación Integral de Ciberseguridad 2025"
- Subtítulo: "Modelo ADAM: Indicadores y Métricas"
- Fecha: [Fecha Evaluación]
- Clasificación: "Uso Estratégico"
- Responsable: [CISO/Responsable GRC]

---

### **DIAPOSITIVA 2: RESUMEN EJECUTIVO**

**Contenido:**

```
ESTADO ACTUAL DE CIBERSEGURIDAD

• Índice Global de Madurez (IGM): 2.92 / 5.0
• Nivel Madurez: 2 (GESTIONADA)
• Riesgo Residual: 50% (MEDIO-ALTO)
• Posición vs. Pares: P40 (percentil 40)

FORTALEZAS PRINCIPALES:
✓ Plan respuesta incidentes formalizado (+3.1/5)
✓ Inventario activos 80% cobertura (+3.2/5)
✓ Backup strategies (2 copias) (+2.9/5)

BRECHAS CRÍTICAS:
✗ SIEM sin SOAR (detección manual) (-2.5/5)
✗ Pentest solo perimetral (sin interno/OT) (-2.5/5)
✗ CISO reporta a TI, no CEO (-2.0/5)

INVERSIÓN RECOMENDADA 2026:
€800k - €1.2M (18 meses)
ROI Esperado: 600-800% | Payback: 34 días

RECOMENDACIÓN JUNTA:
APROBADO - Solicitar presupuesto €200k Q1 2026 (Quick Wins)
```

---

### **DIAPOSITIVA 3: VISIÓN GENERAL - RADAR NIST CSF**

**Componente Visual:**
- Gráfico Radar (6 ejes)
- Eje 1: Gobernar (2.8)
- Eje 2: Identificar (3.2)
- Eje 3: Proteger (3.0)
- Eje 4: Detectar (2.5) ← CRITICO
- Eje 5: Responder (3.1)
- Eje 6: Recuperar (2.9)
- Zona exterior = Benchmark (3.0)
- Zona interior = Actual
- Zona crítica = Detectar (gap vs benchmark)

**Interpretación:**
"Postura equilibrada excepto Detección. Necesita SIEM + SOAR urgente para cierre gap."

---

### **DIAPOSITIVA 4: GOBERNANZA Y RIESGOS**

**Tabla:**

| Indicador | Estado | Target | Gap | Acción |
|-----------|--------|--------|-----|--------|
| Política Ciberseg. | Formalizada 2023 | Anual | -1 año | Actualizar Q1 2026 |
| CISO reporta | Director TI | CEO | -1 nivel | Reorganizar struct. |
| Cumplimiento NIS2 | No aplica* | N/A | - | (*revalorar si CRITIS) |
| Análisis FAIR | Básico | Semestral | -50% | Implementar FAIR riguroso |
| Presupuesto Seg. | €80k/año | 1.5% ingresos | -€40k | Aumentar 2026 |

**Impacto:** Gobernanza débil limita capacidad ejecución. Prioridad: Elevar CISO a nivel ejecutivo.

---

### **DIAPOSITIVA 5: VULNERABILIDADES Y TESTING**

**Gráfico Comparativo:**

```
Vulnerabilidades Pendientes:
                    Actual  |  Target  |  Acción
Críticas:           8       |    0     |  30 días ⚠️
Altas:             23       |    5     |  60 días ⚠️
Medias:            67       |   20     |  90 días →
Bajas:            200       |  <50     |  Anual →

Pentest Cobertura:
                    Implementado
Perimetral:         ✓ Anual (Buen estado)
Interno:            ✗ Nunca (GAP)
OT/SCADA:           ✗ Nunca (GAP si CRITIS)
API/Cloud:          ✗ Parcial (GAP)
Red Team:           ✗ Nunca (Recomendado)

Recomendación:
→ Pentest interno URGENTE (Q2 2026, €50k)
→ Adoptar EPSS junto CVSS (gratuito)
→ Red team semestral (€80k/año)
```

---

### **DIAPOSITIVA 6: DETECCIÓN Y MONITORIZACIÓN (CRÍTICA)**

**Situación Actual vs Target:**

```
SIEM: NO IMPLEMENTADA (IGM 2.5 - CRÍTICO)

Actual Estado:
├─ Arquitectura: No existe
├─ Logs centralizados: 0% (únicamente firewall local)
├─ Detección: Manual/ad-hoc
├─ MTTD (detección): 6-8 horas
├─ Falsos positivos: N/A (sin detección)
└─ Integración respuesta: Nula

Target (Post-SIEM):
├─ Arquitectura: SIEM + SOAR
├─ Logs centralizados: >90%
├─ Detección: Automatizada + IA
├─ MTTD: <15 minutos
├─ Falsos positivos: <5%
└─ Integración: Playbooks automáticos

Inversión + Timeline:
€300k | 4 meses | Q2-Q3 2026

ROI: 400-600% (MTTD reduction solo)
```

---

### **DIAPOSITIVA 7: ROADMAP 18 MESES**

**Timeline Visual:**

```
Q1 2026 - QUICK WINS (€100k, IGM +0.3)
├─ MFA Universal (€30k)
├─ Política actualizada (€10k)
├─ Plan respuesta incidentes formalizado (€15k)
└─ Simulaciones phishing iniciadas (€45k)
    Result: IGM 2.92 → 3.20

Q2-Q3 2026 - STRATEGIC (€400k, IGM +0.7)
├─ SIEM + SOAR implementation (€300k)
├─ Pentest externo + interno (€80k)
├─ Capacitación roles críticos (€20k)
└─ Backup aire-gapped (€40k)
    Result: IGM 3.20 → 3.90

Q4 2026-Q1 2027 - OPTIMIZATION (€300k, IGM +0.2)
├─ Red team exercises (€100k, semestral)
├─ Zero Trust iniciativa (€120k)
├─ Disaster recovery testing (€40k)
└─ Supply chain assessment (€40k)
    Result: IGM 3.90 → 4.10 (OPTIMIZADO)

TOTAL 18 MESES:
├─ Inversión: €800k-1.2M
├─ Beneficio acumulado: €7M+
├─ ROI: 600-800%
└─ Payback period: 34 días
```

**Visualización:** Timeline horizontal con IGM crecimiento de 2.92 → 4.10

---

### **DIAPOSITIVA 8: FINANCIERO - ROI Y BUSINESS CASE**

**Tabla Cuantificación:**

```
ESCENARIOS RIESGO CIBERNÉTICO

Escenario 1: Ransomware
├─ Probabilidad: 20%/año
├─ Impacto potencial: €10M (downtime 3d + rescate)
├─ ALE actual: €2M
└─ Con controles (SIEM+EDR): €400k (-80%)
   → Reducción riesgo: €1.6M/año

Escenario 2: Fuga Datos
├─ Probabilidad: 15%/año
├─ Impacto GDPR: €5M (multa+notification)
├─ ALE actual: €750k
└─ Con controles: €150k (-80%)
   → Reducción riesgo: €600k/año

Escenario 3: Interrupción Servicio
├─ Probabilidad: 10%/año
├─ Impacto: €3M (reputación+pérdida clientes)
├─ ALE actual: €300k
└─ Con RTO/RPO optimizado: €90k (-70%)
   → Reducción riesgo: €210k/año

REDUCCIÓN RIESGO TOTAL: €2.41M/año
INVERSIÓN 18M: €800k
------
NET BENEFIT: €2.41M - €800k = €1.61M
ROI: (€1.61M / €800k) × 100 = 201% (conservador)
PAYBACK: 4 meses

Con Cyber Insurance:
├─ Premium actual: €150k/año
├─ Post-mejora (lower risk): €100k/año
└─ Ahorro adicional: €50k × 3 años = €150k
   → ROI real: ~250%
```

---

### **DIAPOSITIVA 9: RECOMENDACIONES EJECUTIVAS**

**Decisiones Requeridas:**

| Decisión | Opciones | Recomendación | Implicación |
|----------|----------|---|---|
| **Presupuesto Q1** | €50k vs €100k vs €200k | €100k (SIEM piloto) | Quick wins + momentum |
| **CISO Estructura** | Reporta TI vs CEO | CEO (ejecutivo) | Autoridad operacional |
| **Pentest Interno** | Aplazar vs Q2 2026 | Q2 2026 | Cumplir gap crítico |
| **Cyber Insurance** | Renovar igual vs mejorar | Renegociar (risk lower) | Ahorrar €50k-75k/año |
| **NIS2 Readiness** | Si aplica CRITIS | Revisar aplicabilidad | Si sí → acelerar roadmap |

---

### **DIAPOSITIVA 10: RIESGOS Y MITIGACIÓN**

**Matriz de Riesgos Implementación:**

```
RIESGO                          PROBABILIDAD  IMPACTO  MITIGACIÓN
─────────────────────────────────────────────────────────────
Falta soporte ejecutivo         MEDIA         ALTO     Presentar ROI clara
Retrasos presupuestarios        MEDIA         ALTO     Pre-aprobación Q1
Talento insuficiente            ALTA          ALTO     Contratar externo (MSP)
Cambios regulatorios (NIS2)     MEDIA         ALTO     Monitoreo continuo
Incidente durante implementación BAJA          CRÍTICO  Plan contingencia paralelo
─────────────────────────────────────────────────────────────

Contingency Budget: +15% (~€130k para reserva)
```

---

## ANEXOS RECOMENDADOS

**Anexo A:** Comparativa IGM vs. Pares Sectoriales  
**Anexo B:** Matriz Cumplimiento Regulatorio (NIS2, GDPR, ISO 27001)  
**Anexo C:** Catálogo Soluciones (Vendors SIEM, EDR, SOAR)  
**Anexo D:** Plantilla Excel (modelo interactivo cálculos)  
**Anexo E:** Glosario Términos Técnicos  

---

## GUÍA DE PRESENTACIÓN

### **Pre-Presentación (5 min)**
- Distribuir resumen ejecutivo (1 página)
- Aclarar audiencia (Junta vs Comité seguridad)

### **Durante (20-30 min)**
- Diapositiva 1-2: Contexto + Estado actual
- Diapositiva 3: Radar (visual impactante)
- Diapositiva 4-6: Brechas específicas
- Diapositiva 7: Roadmap (futuro positivo)
- Diapositiva 8: ROI (justificación dinero)
- Diapositiva 9-10: Decisiones + Riesgos

### **Post-Presentación (15 min)**
- Q&A
- Siguiente paso: Aprobación presupuesto Q1
- Fecha próxima revisión: Trimestral

---

## NOTAS DE DISEÑO

- **Colores:** Verde (bueno >3.5), Amarillo (medio 2.5-3.5), Rojo (malo <2.5)
- **Gráficos:** Radar (gestalt visual), Timeline (narrativa impacto)
- **Tablas:** Máximo 3 columnas; números destacados en negrita
- **Texto:** Máximo 5 líneas/diapositiva; bullets concisos
- **Logo/Branding:** Consistente con identidad corporativa

---

**Fin de Plantilla Reporte Ejecutivo**

*Descargue template PowerPoint en: [URL repositorio]*
