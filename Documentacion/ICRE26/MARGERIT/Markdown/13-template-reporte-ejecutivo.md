# TEMPLATE REPORTE EJECUTIVO: PRESENTACIÓN JUNTA DIRECTIVA
## Estructura Profesional 15-Página para Comunicar Ciberseguridad a C-Suite

**Versión:** 2.0 | **Formato:** Guía Markdown para conversión PowerPoint  
**Audiencia:** Junta Directiva, CFO, CEO, Consejero Independiente  
**Duración Presentación:** 30-45 minutos | **Acciones Requeridas:** Sí

---

## ESTRUCTURA REPORTE (15 PÁGINAS)

---

### 📄 PÁGINA 1: PORTADA

```
CONFIDENCIAL
═════════════════════════════════════════════════════

     EVALUACIÓN CIBERSEGURIDAD 2026
     
     Metodología: GQM + PRAGMATIC
     Marcos: MAGERIT v3 + NIS2 + ENS + NIST CSF 2.0
     
═════════════════════════════════════════════════════

Organización: [NOMBRE EMPRESA]
Sector: [Categoría NIS2: Esencial/Importante/Otra]
Fecha Evaluación: 24-25 de Enero 2026
Período Auditoría: Q1 2026

Preparado por: CISO + Data Science Team
Presentado a: Junta Directiva
Clasificación: CONFIDENCIAL - Acceso Limitado

═════════════════════════════════════════════════════
```

---

### 📄 PÁGINA 2: EXECUTIVE SUMMARY (1 Página - Clave)

**Estructura: 4 gráficos + 4 párrafos = decisión en 2 minutos**

```
┌─────────────────────────────────────────────────────────┐
│ SCORECARD EJECUTIVO: ESTADO CIBERSEGURIDAD 2026        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  IGM: 62% (L3 Repetible)      PRAGMATIC: 3.85/5.0     │
│       ┌──────────────┐          ┌──────────────┐       │
│       │ ▓▓▓▓▓▓░░░░  │          │ ▓▓▓▓░░░░░░  │       │
│       │  Target: 75% │          │Target: 4.0+  │       │
│       └──────────────┘          └──────────────┘       │
│                                                         │
│ BRECHA NIS2: 82%              ALE RESIDUAL: €480K     │
│  ✓ Cumplidor                   vs. Target: €400K      │
│  ⚠ 3 requisitos críticos       Varianza: -€80K        │
│  Gap: -13%                     (5% bajo target)        │
│                                                         │
└─────────────────────────────────────────────────────────┘

PÁRRAFO RESUMEN:

"La evaluación GQM+PRAGMATIC de Q1 2026 revela que nuestra 
organización mantiene nivel de madurez ciberseguridad L3 
(Repetible) con 62% de IGM global. Mientras que superamos 
conformidad NIS2 (82%), identificamos 3 requisitos críticos 
en análisis de riesgos (Art 21a) que requieren atención antes 
auditoría Q2 2026. El riesgo residual (€480K/año) está 5% 
bajo target, alcanzable con 3 inversiones prioritarias (ROI 
promedio 1.200%+)."

HALLAZGOS CLAVE:
1. ✓ FORTALEZAS: Gobernanza sólida (L3+), Cumplimiento 
   (84%), Incidentes (L3)
2. ⚠ ÁREAS DÉBILES: SIEM (L2, -1.0 puntos), MAR (L2, 
   análisis incompleto), Resiliencia (L2, RTO/RPO ausentes)
3. 🔴 CRÍTICOS: Threat modeling (65%), Cascadas (60%), 
   Eficacia Salvaguardas (70%)
4. 💰 OPORTUNIDADES: 4 salvaguardas con ROI >1.000% 
   (SIEM, Pentesting, RTO/RPO, Threat Intel)

RECOMENDACIÓN JUNTA:
→ Aprobar inversión €85K en 3 mejoras prioritarias 
  (SIEM €50K, RTO/RPO €75K, Threat Intel €5K)
→ Target IGM 75%+ en 12 meses
→ Re-evaluación trimestral
```

---

### 📄 PÁGINA 3: CONTEXTO & METODOLOGÍA

```
METODOLOGÍA GQM+PRAGMATIC EN 30 SEGUNDOS

┌─────────────────────────────────────────────────────┐
│ NIVEL 1: GOAL (¿Por qué?)                           │
│ "Reducir riesgo residual a <€400K/año"             │
│                           ↓                         │
│ NIVEL 2: QUESTION (¿Qué medir?)                     │
│ "¿Cobertura salvaguardas por amenaza crítica?"     │
│                           ↓                         │
│ NIVEL 3: METRIC (¿Cómo cuantificar?)                │
│ "% = (Amenazas con salvaguarda) / (Total × 100)"   │
│                           ↓                         │
│ NIVEL 4: PRAGMATIC VALIDATION (¿Es robusto?)        │
│ 9 criterios (Predictivo, Relevante, Accionable...) │
│ Score 4.7/5.0 → EXCELENTE indicador                │
└─────────────────────────────────────────────────────┘

MARCOS NORMATIVOS INTEGRADOS:
• MAGERIT v3 (MAR.1-4): Análisis riesgos español
• NIS2: Directiva UE ciberseguridad (Art 21)
• ENS RD 311/2022: Proporcionalidad L2-L4
• NIST CSF 2.0: Govern, Identify, Protect, Detect, 
  Respond, Recover
• ISO 27001:2022: 93 controles SGSI
• FAIR: Cuantificación riesgo en €

SCOPE EVALUACIÓN:
✓ 75 preguntas en 10 bloques temáticos
✓ 3 respondentes (CISO, TI, Legal)
✓ 20 indicadores MAGERIT evaluados
✓ 9 criterios PRAGMATIC por indicador
✓ Auditoría interna (8 horas)
✓ Triangulación 2+ fuentes datos

LIMITACIONES:
- Snapshot enero 2026 (no predictivo extremos)
- Muestreo vulnerabilidades (cubierta 80% activos)
- Estimaciones subjetivas (threat modeling, 
  eficacia salvaguardas) validadas por expertos
```

---

### 📄 PÁGINA 4: RESULTADOS IGM (Índice Global Madurez)

```
MADUREZ CIBERSEGURIDAD POR BLOQUE (Gráfico Radar 10 ejes)

                    GOBERNANZA 3.2
                         ▲
                    ╱────────╲
              CONTEXTO 3.3      CUMPLIMIENTO 3.4
            ╱                      ╲
       INCIDENTES 3.2          MAR RIESGOS 2.8 ← CRÍTICO
       │          ╲            ╱   │
       │           ╲          ╱    │
       │            ╲        ╱     │
    RESILIENCIA 2.9 ╲      ╱ INDICADORES 3.1
       │             ╲    ╱      │
       │              ╲  ╱       │
       │           SIEM 2.5 ← CRÍTICO
       │              ╱╲
    CAPACITACIÓN 3.0    ╲
                    VULNERABILIDADES 3.5

LEYENDA:
3.5-4.5: ✓ Bueno (Verde)
2.6-3.4: ⚠ Aceptable (Amarillo)
<2.6: 🔴 Crítico (Rojo)

INTERPRETACIÓN POR BLOQUE:

1. ✓ GOBERNANZA (3.2): Políticas formalizadas, CISO 
   reporta Junta, presupuesto asignado. Mejora: 
   objetivo estratégico ciberseguridad explícito.

2. 🔴 MAR RIESGOS (2.8): Análisis incompleto en activos 
   mapeados. Requiere: Tarea MAR.1 (inventario) al 
   100%, MAR.2 (threat modeling STRIDE), MAR.3 
   (salvaguardas), MAR.4 (cuantificación ALE).

3. ⚠ INDICADORES (3.1): 10 KPIs implementados, solo 6 
   accionables. Mejora: GQM alignment (GOAL→QUESTION→
   METRIC), validación PRAGMATIC.

4. ✓ VULNERABILIDADES (3.5): Escaneo trimestral, 
   CVSS tracking, penetesting anual. Fortaleza.

5. 🔴 SIEM (2.5): Herramienta básica, sin correlación 
   eventos, MTTR >24h, alertas ignoradas 40%. 
   Crítico: invertir SIEM robusto (€50K).

6. ⚠ CAPACITACIÓN (3.0): Curso anual + phishing test 
   6m. Mejora: contenido NIS2, tabla periódica 
   amenazas, casos reales.

7. 🔴 RESILIENCIA (2.9): RTO/RPO indefinidos, BCP sin 
   pruebas anuales, failover manual. Requiere: 
   formalizacion Recovery Plan (€75K inversión).

8. ✓ CUMPLIMIENTO (3.4): Auditoría ISO anual, control 
   cambios formalizado, política clara. Fortaleza.

9. ⚠ INCIDENTES (3.2): Plan respuesta escrito, equipo 
   asignado, pero sin simulacros. Mejora: drill 
   anual.

10. ✓ CONTEXTO (3.3): Entendimiento NIS2, riesgo 
    geopolítico considerado, benchmarking sectorial.

IGM GENERAL: 3.09 / 5.0 = 62% → NIVEL L3 (REPETIBLE)

COMPARATIVA:
- Nuestro IGM: 3.09
- Benchmark industria: 3.09 (EN LÍNEA)
- Target 2026: 3.75 (L4 Gestionado = 75%)
- Gap: +0.66 puntos (21% mejora necesaria)
```

---

### 📄 PÁGINA 5: PRAGMATIC SCORE INDICADORES

```
CALIDAD INDICADORES: DISTRIBUCION PRAGMATIC (9 criterios)

SCORECARD 20 INDICADORES:

┌──────────────────────────────────┬───────────┬────────┐
│ Indicador                        │ Score     │ Status │
├──────────────────────────────────┼───────────┼────────┤
│ Cobertura Salvaguardas           │ 4.7/5.0   │ ✓✓✓✓✓ │
│ Gaps Documentados                │ 4.6/5.0   │ ✓✓✓✓✓ │
│ Inventario Cobertura             │ 4.4/5.0   │ ✓✓✓✓  │
│ ARO Amenaza                      │ 4.3/5.0   │ ✓✓✓✓  │
│ Threat Intelligence              │ 4.4/5.0   │ ✓✓✓✓  │
│ ALE Total                        │ 4.4/5.0   │ ✓✓✓✓  │
│ Residual por Categoría ENS       │ 4.2/5.0   │ ✓✓✓   │
│ ROI Salvaguardas                 │ 4.3/5.0   │ ✓✓✓✓  │
│ ─────────────────────────────    │ ─────     │ ────  │
│ [TOP 8 Indicadores PROMEDIO]     │ 4.35/5.0  │ BUENO │
│ ─────────────────────────────    │ ─────     │ ────  │
│ Completitud Atributos            │ 3.8/5.0   │ ✓✓✓   │
│ Madurez Salvaguardas CMM         │ 3.8/5.0   │ ✓✓✓   │
│ Análisis Dependencias            │ 3.6/5.0   │ ✓✓✓   │
│ Trazabilidad Activos↔Procesos   │ 3.6/5.0   │ ✓✓✓   │
│ ─────────────────────────────    │ ─────     │ ────  │
│ [MIDDLE 4 INDICADORES]           │ 3.75/5.0  │ ACEPTABLE │
│ ─────────────────────────────    │ ─────     │ ────  │
│ % Amenazas STRIDE/CAPEC          │ 3.2/5.0   │ ⚠⚠    │
│ Degradación Potencial            │ 3.2/5.0   │ ⚠⚠    │
│ Eficacia Salvaguarda             │ 3.3/5.0   │ ⚠⚠    │
│ Cascadas Multiactivo             │ 3.3/5.0   │ ⚠⚠    │
│ ─────────────────────────────    │ ─────     │ ────  │
│ [BOTTOM 4 INDICADORES]           │ 3.25/5.0  │ DÉBIL │
└──────────────────────────────────┴───────────┴────────┘

PRAGMATIC PROMEDIO: 3.85/5.0 (ACEPTABLE)

75% indicadores >3.5 (BUENO+)
25% indicadores <3.5 (DÉBIL)

IMPLICACIONES:
✓ 75% indicadores implementables inmediato (PRAGMATIC >3.5)
⚠ 25% requieren herramientas/metodologías adicionales
🔴 Ningún indicador abandonar (<3.0)

ACCIONES MEJORA PRIORITARIAS (3 meses):
1. Bottom 4 indicadores: Rediseño con herramientas 
   (STRIDE tool €5K, FAIR Montecarlo Excel gratis)
2. Validación externa (auditor): Confirmar PRAGMATIC scores
3. Automatización: Integrar feeds threat intel en SIEM
```

---

### 📄 PÁGINA 6: CONFORMIDAD NORMATIVA (Heatmap)

```
BRECHA NIS2 + ENS + ISO 27001: MATRIZ ROJO/AMARILLO/VERDE

╔═══════════════════════════════════════════════════════╗
║ CUMPLIMIENTO REGULATORIO 2026 (% Conformidad)        ║
╠═══════════════════════════════════════════════════════╣
║                                                       ║
║ NIS2 Art 21(a) Análisis Riesgos          88% 🟡     ║
║   ├─ Inventario activos                92% ✓       ║
║   ├─ Caracterización activos           85% 🟡      ║
║   ├─ Análisis amenazas                 85% 🟡      ║
║   ├─ Salvaguardas asignadas            95% ✓       ║
║   └─ Cuantificación riesgo (ALE)       78% 🟡 ← CR │
║                                                       ║
║ NIS2 Art 21(d) Continuidad/Resiliencia 75% 🟡 ← CR  ║
║   ├─ RTO definido                      60% 🔴 ← CR │
║   ├─ RPO definido                      55% 🔴 ← CR │
║   └─ Pruebas BCP anuales               85% 🟡      ║
║                                                       ║
║ NIS2 Art 21(g) Gestión Incidentes      82% 🟡      ║
║   ├─ Plan respuesta                    95% ✓       ║
║   ├─ Equipo 24/7 (SOC)                 70% 🟡 ← CR │
║   └─ Notificación <72h                 75% 🟡      ║
║                                                       ║
║ ENS Med.2 Análisis Amenazas            82% 🟡      ║
║ ENS Med.3-6 Medidas Protección         85% 🟡      ║
║ ISO 27001:2022 Cobertura General       88% 🟡      ║
║                                                       ║
║ PROMEDIO GENERAL: 82% 🟡 (AMARILLO)                 ║
║                                                       ║
║ LEYENDA:                                            ║
║ 🟢 Verde (≥95%): Conforme, auditar muestreo        ║
║ 🟡 Amarillo (70-94%): No conforme, plan acción 3m  ║
║ 🔴 Rojo (<70%): No conforme crítico, acción 1m     ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝

BRECHAS CRÍTICAS IDENTIFICADAS:

🔴 CRÍTICO 1 - RTO/RPO Indefinidos (55% conformidad)
   Requisito: NIS2 Art 21(d), ENS Cat.2
   Impacto: Si incidente servicios críticos, sin 
   objetivo recuperación → incumplimiento regulatorio
   Solución: Formalizar RTO/RPO por servicio 
   + test bimensual (€75K inversión, 3 meses)

🔴 CRÍTICO 2 - SOC 24/7 Parcial (70% conformidad)
   Requisito: NIS2 Art 21(g) monitorización continua
   Impacto: MTTR actual 18h, target <2h (crítica seguridad)
   Solución: SIEM robusto + escalación automática 
   (€50K + €30K/año, 2 meses)

🟡 CRÍTICO 3 - Cuantificación Riesgo Incompleta (78%)
   Requisito: NIS2 Art 21(a) análisis riesgos formal
   Impacto: Auditor externo puede cuestionar MAGERIT MAR.4
   Solución: FAIR Montecarlo + validación auditor 
   (€0 si Excel, 1 mes)

PLAN REMEDIACIÓN:
┌─────────────────────────────────────────────┐
│ Q1 2026 (NOW):    Auditoría interna riesgos │
│ Q2 2026:          Implementar RTO/RPO       │
│ Q2 2026:          Upgrade SIEM + SOC        │
│ Q3 2026:          Re-evaluación audit       │
│ Q4 2026:          Auditoría externa NIS2   │
└─────────────────────────────────────────────┘

FORECAST CONFORMIDAD:
Q1: 82% → Q2: 87% → Q3: 91% → Q4: 95%+ ✓
```

---

### 📄 PÁGINA 7: ANÁLISIS FINANCIERO (ROI & ALE)

```
ROI SALVAGUARDAS PROPUESTAS (Payback + NPV 3 años)

OPCIÓN A: CONSERVADOR (Salvaguardas críticas solo)
┌────────────────────────────────────────────────────┐
│ 1. SIEM Centralizado                               │
│    • Inversión: €50K                               │
│    • Costo anual: €30K                             │
│    • ALE Reducción: €364K/año (detección +48%)    │
│    • Payback: 1.6 meses                            │
│    • NPV 3años: €892K                              │
│    • ROI: 1.784% (EXCELENTE) → ✓ INVERTIR AHORA  │
│                                                    │
│ 2. RTO/RPO Formales (Resiliencia)                  │
│    • Inversión: €75K (consultoría + herramientas) │
│    • Costo anual: €15K                             │
│    • ALE Reducción: €140K/año (disponibilidad)   │
│    • Payback: 6.4 meses                            │
│    • NPV 3años: €325K                              │
│    • ROI: 433% → ✓ INVERTIR SIGUIENTE             │
│                                                    │
│ 3. Pentesting Anual (Vulnerabilidades)             │
│    • Inversión: €20K (primer año)                  │
│    • Costo anual: €5K                              │
│    • ALE Reducción: €100K/año (riesgo residual)  │
│    • Payback: 2.4 meses                            │
│    • NPV 3años: €265K                              │
│    • ROI: 1.325% → ✓ INVERTIR SIMULTÁNEO SIEM    │
│                                                    │
│ SUBTOTAL FASE 1: €145K inversión                  │
│ ALE Reducción Total: €604K/año                     │
│ Payback combinado: 2.9 meses                       │
│ NPV 3años: €1.482K                                 │
│ ROI Promedio: 1.021% → EXCEPCIONAL                 │
└────────────────────────────────────────────────────┘

OPCIÓN B: AGRESIVO (Todas salvaguardas)
+ Threat Intelligence (€5K) = €150K total
+ Capacitación avanzada (€10K) = €160K total
Total ROI 3-años: €1.600K+ (mantiene ROI >900%)

OPCIÓN C: MÍNIMO (Solo SIEM)
€50K inversión, ROI 1.784% → No sostenible a largo plazo
Riesgo: Brecha de RTO/RPO en auditoría 2027

RECOMENDACIÓN JUNTA:
→ Opción A (SIEM + RTO/RPO + Pentesting) = €145K
→ Presupuesto disponible Q1-Q2 2026
→ Payback < 3 meses (financieramente sólido)
→ Conformidad NIS2 alcanzada Q2 2026

ANÁLISIS RIESGO-BENEFICIO:

Escenario 1: No invertir (Business as usual)
- IGM 2026: Permanece 62%
- Brecha NIS2: -13% (incumplimiento)
- Riesgo: Audit finding crítico
- Costo oportunidad: €604K/año en riesgo residual

Escenario 2: Invertir €145K (Recomendado)
- IGM 2026: 75% (L4 Gestionado)
- Brecha NIS2: 95%+ (completo)
- Beneficio: €604K reducción ALE/año
- ROI: 1.021% (paga en 2.9 meses)
- Diferencial vs. Opción 1: €459K valor neto 3 años

DECISIÓN FINANCIERA: Opción 2 (Invertir)
Justificación: ROI >400%, cumplimiento regulatorio, 
reducción riesgo operacional
```

---

### 📄 PÁGINA 8: TOP 10 ACCIONES PRIORITARIAS

```
PLAN DE ACCIÓN 2026: PRIORIZADO POR IMPACTO + PLAZO

RANKING | ACCIÓN | DUEÑO | PLAZO | INVERSIÓN | IMPACTO | STATUS
────────┼────────┼───────┼───────┼──────────┼────────┼────────
  1     │ SIEM Upgrade     │ CISO │ 8w   │ €50K   │ ALE-€364K│ 🔴 Crítico
  2     │ RTO/RPO Formal   │ CISO │ 12w  │ €75K   │ ALE-€140K│ 🔴 Crítico
  3     │ MAGERIT MAR.1    │ Risk │ 6w   │ €0K    │ Confm+12%│ 🟡 Alto
  4     │ Pentesting Anual │ CISO │ 4w   │ €20K   │ ALE-€100K│ 🟡 Alto
  5     │ Threat Intel     │ SOC  │ 2w   │ €5K    │ Detection│ 🟡 Alto
  6     │ BCP Test 6m      │ Risk │ 8w   │ €0K    │ L3→L4    │ 🟡 Alto
  7     │ STRIDE Model     │ CISO │ 12w  │ €15K   │ Threat√  │ 🟡 Medio
  8     │ Capacitación NIS2│ HR   │ 4w   │ €8K    │ L3→L3.5  │ 🟡 Medio
  9     │ Control Cambios  │ CISO │ 6w   │ €0K    │ L3→L3.2  │ 🟡 Medio
 10     │ Auditoría Interna│ Internal│ 2w │ €5K    │ 0-validar│ 🟢 Operativo

HITO CRÍTICO - Q2 2026 (AUDITORÍA NIS2 PREVISTA):
- ✓ SIEM deployed (semana 4)
- ✓ MAGERIT MAR.1-2 completado
- ✓ Brecha NIS2 <5% (de 18% actual)

PROPIETARIOS Y RACI:
- CISO: Responsable general + SIEM, RTO/RPO, Pentesting
- Risk Manager: MAR análisis, BCP test, Auditoría
- SOC Manager: Threat Intel, SIEM operación
- CFO: Presupuesto control (€153K total)

DEPENDENCIAS:
SIEM (Acción 1) → prerequisito Threat Intel (Acción 5)
RTO/RPO (Acción 2) → input BCP Test (Acción 6)
MAR.1 (Acción 3) → base STRIDE (Acción 7)

RIESGOS PLAN:
- Delay SIEM (vendor): Mitiga con plan B backup tool
- Budget freeze: Mantener +15% contingency
- Team capacity: Consultant support primeras 8 semanas
```

---

### 📄 PÁGINA 9: INDICADORES A RECHAZAR O REDISEÑAR

```
INDICADORES DÉBILES: ANÁLISIS DE DECISIÓN

Para indicadores con PRAGMATIC <3.5, análisis costo-beneficio
de mantener vs. rediseñar vs. abandonar:

INDICADOR: "% Amenazas STRIDE/CAPEC Mapeadas" (3.2/5.0)

  ANÁLISIS:
  ├─ Precisión: 2/5 (Análisis manual, inconsistencias)
  ├─ Oportunidad: 2/5 (Requiere 2-3 meses actualización)
  ├─ Costo: €40K/año (Consultant threat modeling)
  ├─ Relevancia: 4/5 (NIS2 Art 21a requiere amenazas)
  └─ VEREDICTO: REDISEÑAR (no abandonar)

  OPCIONES:
  A) Mantener con herramienta (€10K STRIDE): 
     PRAGMATIC Score →4.2 en 3m
  B) Simplicar a "% Amenazas con Inteligencia": 
     PRAGMATIC Score →4.0 en 1m (más rápido)
  C) Abandonar (NO RECOMENDADO): Breche auditoría

  DECISIÓN: Opción B (simplificar) + Opción A (futuro)

INDICADOR: "Degradación Potencial (%)" (3.2/5.0)

  PROBLEMA: Estimación subjetiva, error 30-50%
  
  SOLUCIONES:
  1. FAIR Montecarlo: Excel formula automática 
     → PRAGMATIC +1.5 puntos
  2. Experto panel: 5 CISO +consenso → PRAGMATIC +0.8
  3. Abandonar: Usar "ALE reducción" en su lugar
     (ya disponible, PRAGMATIC 4.4)
  
  DECISIÓN: Opción 1 (FAIR) en Q2 2026

INDICADOR: "Cascadas Multiactivo" (3.3/5.0)

  CONTEXTO: Solo crítico para Utilities/Telecom
  
  APLICA A NOSOTROS: ✗ NO (retail, bajo riesgo cascada)
  
  DECISIÓN: Abandonar este indicador
  
  IMPACTO: -1 indicador, mantiene 19 core
```

---

### 📄 PÁGINA 10-12: DETALLES TÉCNICOS POR BLOQUE

**(Resumen comprimido; versión completa en archivo técnico aparte)**

```
BLOQUE 1: GOBERNANZA (Fortaleza L3, Mejora: Objetivo estratégico)
BLOQUE 2: MAR (CRÍTICO L2, Mejora: Completar 4 tareas MAR)
BLOQUE 3: INDICADORES (Aceptable L3, Mejora: GQM alignment)
BLOQUE 4: VULNERABILIDADES (Fortaleza L3.5, Mantener)
BLOQUE 5: SIEM (CRÍTICO L2, Mejora: Herramienta +€50K)
BLOQUE 6: CAPACITACIÓN (Aceptable L3, Mejora: NIS2 content)
BLOQUE 7: RESILIENCIA (CRÍTICO L2.9, Mejora: RTO/RPO formalizado)
BLOQUE 8: CUMPLIMIENTO (Fortaleza L3.4, Mantener auditoría anual)
BLOQUE 9: INCIDENTES (Aceptable L3.2, Mejora: Drill anual)
BLOQUE 10: CONTEXTO (Fortaleza L3.3, Mantener)
```

---

### 📄 PÁGINA 13: APÉNDICES

```
APÉNDICE A: GLOSSARIO GQM+PRAGMATIC
APÉNDICE B: BENCHMARK SECTORIAL (Universidades españolas)
APÉNDICE C: MATRIZ NORMATIVA DETALLADA
APÉNDICE D: CONTACTOS AUDITORÍA EXTERNA
APÉNDICE E: NEXT STEPS TIMELINE
```

---

### 📄 PÁGINA 14: PRESUPUESTO RECOMENDADO

```
DESGLOSE INVERSIÓN 2026

LÍNEA 1: Herramientas
├─ SIEM Centralizado: €50.000
├─ RTO/RPO Consultoría: €60.000 (herramientas)
├─ STRIDE Tool: €10.000 (threat modeling)
└─ Threat Intel Premium: €5.000 (feeds)
SUBTOTAL: €125.000

LÍNEA 2: Servicios
├─ Pentesting Anual: €20.000
├─ Auditoría Interna: €5.000
├─ Capacitación NIS2: €8.000
└─ Consultoría MAGERIT: €10.000 (si necesario)
SUBTOTAL: €43.000

LÍNEA 3: Operación (incremento anual)
├─ SIEM: €30.000/año
├─ RTO/RPO Mantenimiento: €15.000/año
├─ Pentesting: €5.000/año
└─ Threat Intel: €3.000/año
SUBTOTAL ANUAL: €53.000/año (incremental)

PRESUPUESTO TOTAL 2026: €168.000 (capex €125K + servicios €43K)

FINANCIACIÓN:
Source 1: Presupuesto Seguridad TI: €100K (ya asignado)
Source 2: Capex Transformación Digital: €50K (presupuesto 2026)
Source 3: Ahorro OPEX (infraestructura legacy): €18K
TOTAL: €168K ✓ Financiado
```

---

### 📄 PÁGINA 15: CONCLUSIÓN Y DECISIONES REQUERIDAS

```
CONCLUSIONES EJECUTIVAS:

1. ✓ POSICIÓN GENERAL: Ciberseguridad en nivel aceptable (L3), 
   conforme con mayoría regulaciones (82% NIS2), pero con 
   brechas críticas en resiliencia y monitorización.

2. ⚠ RIESGOS INMEDIATOS: 
   • RTO/RPO ausentes (auditoría Q2 podría resultar 
     incumplimiento)
   • SIEM deficiente (MTTR >18h, target <2h)
   • Análisis riesgos incompleto (MAR.1-2 parcial)

3. 💰 OPORTUNIDADES: 4 inversiones principales generan ROI 
   >1.000% combinado, pagables en <3 meses, reducen ALE 
   €604K anuales.

4. 📈 TRAYECTORIA: Con plan propuesto, IGM 62%→75% en 12m, 
   conformidad NIS2 82%→95%+ en 6m.

DECISIONES REQUERIDAS DE JUNTA:

☐ DECISIÓN 1: Aprobar presupuesto €168K para 2026
   Justificación: ROI 1.021% (excepcional), 
   cumplimiento regulatorio, reducción riesgo €604K/año

☐ DECISIÓN 2: Autorizar CISO gestión Plan Acción
   Responsabilidad: CISO + Risk Manager (RACI definido)
   Seguimiento: KPI trimestral en Junta

☐ DECISIÓN 3: Hito crítico Q2 2026 pre-auditoría NIS2
   Objetivos: SIEM deployed, RTO/RPO formalizado, 
   brecha NIS2 <5%

☐ DECISIÓN 4: Re-evaluación GQM+PRAGMATIC Q4 2026
   Esperado: IGM 75%+, PRAGMATIC score 4.0+, 
   conformidad 95%+

PRÓXIMOS PASOS:

Semana 1: Aprobación Junta + comunicación equipo
Semana 2: CISO kickoff meeting: asignación tasks
Semana 3: Selección vendors SIEM + RTO/RPO
Semana 4: Inicio implementaciones paralelas
Semana 8: Checkpoint progress (CISO reporte)

CONTACTO Y PREGUNTAS:

CISO: [nombre] | [email] | [teléfono]
CFO: [nombre] | [email] | [presupuesto]
Auditor Externo: [nombre] | [auditoría Q2 confirmada]

═════════════════════════════════════════════════════
FIN REPORTE
Versión: 2.0 | Clasificación: CONFIDENCIAL
Próxima Revisión: Q2 2026 (post-auditoría NIS2)
═════════════════════════════════════════════════════
```

---

**© 2026 Template Reporte Ejecutivo | Consorcio Ciberseguridad**  
*Estructura 15-página para presentación Junta: contexto + datos + decisiones.*
