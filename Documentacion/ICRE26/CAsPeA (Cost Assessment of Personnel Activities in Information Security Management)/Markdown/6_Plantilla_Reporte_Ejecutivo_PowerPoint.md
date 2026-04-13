# PLANTILLA DE REPORTE EJECUTIVO EN POWERPOINT
## Estructura de Presentación para Stakeholders

**Versión:** 2.1  
**Duración presentación:** 15-20 minutos  
**Público:** C-Suite, Consejo Directivo, Auditores, Reguladores  

---

## ESTRUCTURA RECOMENDADA (10-12 slides)

### SLIDE 1: PORTADA
```
Título: "EVALUACIÓN DE MADUREZ CIBERSEGURIDAD 2025"
Subtítulo: "[Nombre Organización]"
Logos: [Entidad + Partners]
Fecha: [Enero 2026]
Confidencial: [Restringido a stakeholders aprobados]
```

### SLIDE 2: AGENDA
```
1. Contexto y Objetivos (1 min)
2. Hallazgos Principales (3 min)
3. Madurez General (IMG) (2 min)
4. Análisis ROI (2 min)
5. Brechas Críticas (2 min)
6. Recomendaciones Prioritarias (3 min)
7. Hoja de Ruta (2 min)
```

### SLIDE 3: CONTEXTO Y OBJETIVOS

**Titular:** "¿Por Qué Evaluamos Madurez de Ciberseguridad?"

**Contenido:**
```
✓ Cumplimiento normativo creciente
  - NIS2 obligatorio Q1 2026 (operadores esenciales)
  - DORA (sector financiero) enero 2025
  - ENS (AAPP) nivel [Básico/Medio/Alto]
  
✓ Cuantificación de riesgos operacionales
  - Incidentes espera: [X] / año sin controles
  - Coste promedio incidente: €[Y]K
  
✓ Justificación de inversiones
  - Presupuesto anual: €[Z]K
  - ¿Alineado con sector? (Benchmarking)
  - ¿ROI defensible? (Cuantificado)
```

### SLIDE 4: ÍNDICE DE MADUREZ GENERAL (IMG)

**Gráfico principal: MEDIDOR de 0-100**
```
IMG Actual: [XX]/100 (Tier [2]/5)

Escala:
0-20    | 21-40   | 41-60     | 61-80         | 81-100
Initial | Managed | Defined   | Quantitative  | Optimizing
RED     | ORANGE  | YELLOW    | LIGHT GREEN   | GREEN
```

**Debajo del medidor:**
```
Interpretación: "[Organización está en fase de consolidación de procesos. 
Necesita institucionalización de controles antes de optimización.]"

Comparativa sector: Nuestra IMG [XX] vs mediana sector [YY]
  → Si XX < YY-10: "Significativamente por debajo"
  → Si XX ≈ YY±10: "Alineado con sector"
  → Si XX > YY+10: "Adelante vs peers"
```

### SLIDE 5: MADUREZ POR FUNCIÓN NIST CSF 2.0

**Gráfico: RADAR de 6 ejes**
```
Visualizar fortalezas/debilidades:

        Govern
          /\
    Identify  Recover
       /        \
  Protect      Respond
       \         /
       Detect──

Escala cada eje: Tier 1-4 (o % cobertura)

Patrón esperado: Hexágono más grande = mejor.
Si hay puntas desequilibradas = áreas críticas de mejora.
```

**Debajo:**
```
Función    | Tier | Cobertura | Brecha vs Tier 3
-----------|------|-----------|------------------
Govern     | 2.5  | 62%       | -18 pp
Identify   | 2.3  | 58%       | -22 pp
Protect    | 2.8  | 65%       | -15 pp
Detect     | 1.9  | 48%       | -32 pp ⚠️
Respond    | 1.7  | 42%       | -38 pp ⚠️⚠️
Recover    | 1.5  | 35%       | -45 pp ⚠️⚠️⚠️

Recomendación: Priorizar RESPOND y RECOVER (mayores brechas)
```

### SLIDE 6: ANÁLISIS FINANCIERO - COSTES (CAsPeA)

**Gráfico 1: Distribución de costes por componente**
```
Gráfico de DONA o BARRAS APILADAS:

Presupuesto Total Anual: €[TOTAL]K

├─ Personal Dedicado: [%] = €[X]K
│  ├─ CISO/Director: €[a]K
│  ├─ Especialistas SIEM: €[b]K
│  ├─ Arquitectos: €[c]K
│  └─ Otros roles: €[d]K
│
├─ Servicios Externalizados (MSS/SOC): [%] = €[Y]K
├─ Herramientas/Licencias: [%] = €[Z]K
├─ Consultoría: [%] = €[W]K
└─ Otros: [%] = €[V]K
```

**Debajo:**
```
Coste por Empleado Protegido: €[COSTE/EMP] / año
Comparativa Sector: Mediana €[MED/EMP]
  → Posición: Percentil [P] del sector
```

### SLIDE 7: ANÁLISIS FINANCIERO - ROI

**Gráfico: Comparativa Escenarios**
```
                        SIN CONTROLES    CON CONTROLES    BENEFICIO
Incidentes/año:            [A]              [B]            Evitados
Coste promedio:            €[C]K            €[C]K          (no cambia)
Pérdida anual:            €[A×C]K          €[B×C]K        €[(A-B)×C]K

Inversión seguridad:        €0              €[INV]K        
Coste neto:               €[A×C]K        €[(B×C)+INV]K    

ROI = [(A-B)×C - INV] / INV × 100% = [ROI]%
Payback Period = INV / [(A-B)×C] = [MESES] meses
```

**Colores:**
```
ROI < 0%    → ROJO (inversión no justificada)
ROI 0-30%   → NARANJA (positivo pero bajo)
ROI 30-100% → AMARILLO (saludable)
ROI > 100%  → VERDE (excelente)
```

### SLIDE 8: INCIDENTES Y TENDENCIAS

**Gráfico 1: Historial Incidentes (últimos 3-5 años, si datos)**
```
Gráfico de LÍNEA: Cantidad incidentes/año
Y: Número incidentes
X: Años (2021, 2022, 2023, 2024, 2025-Proyección)

Mostrar:
- Línea histórica
- Tendencia (si ↑ o ↓)
- Proyección 2025 (si se mantiene tendencia o mejora con controles)
```

**Gráfico 2: Costes de Incidentes (distribución por tipo)**
```
Gráfico de BARRAS APILADAS:
Malware: €[a]K
Phishing: €[b]K
Ransomware: €[c]K
Breach: €[d]K
Otros: €[e]K
TOTAL: €[a+b+c+d+e]K
```

### SLIDE 9: BRECHAS CRÍTICAS Y ÁREAS DE RIESGO

**Contenido:**
```
FUNCIÓN CRÍTICA #1: DETECT (MTTD = Mean Time To Detect)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Estado actual:  MTTD = 120 minutos
Benchmark sector: MTTD = 87 minutos (Mediana)
Brecha: +33 minutos (+38%)
Riesgo: Tiempo comprometido para contención
Recomendación: Automatización SIEM, alerting inteligente

FUNCIÓN CRÍTICA #2: RESPOND (MTTR = Mean Time To Respond)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Estado actual:  MTTR = 360 minutos (6 horas)
Objetivo: <240 minutos (4 horas) para críticos
Brecha: +120 minutos
Riesgo: Extensión de dwell time (tiempo del atacante en red)
Recomendación: Playbooks automatizados, SOAR, escalación ágil

VULNERABILIDAD OPERACIONAL: Tasa Remediación
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Estado: Críticas remediadas en 60 días (SLA: 30 días)
Riesgo: Exposición prolongada a exploits conocidos
Recomendación: Procesos de cambio ágiles, patch automation
```

### SLIDE 10: ROADMAP Y RECOMENDACIONES PRIORITARIAS

**Gráfico: Gantt simplificado (horizontal)**
```
TRIMESTRE 1 (Q1 2026 - NIS2 obligatorio)
├─ ✓ CUMPLIMIENTO REGULATORIO
│  └─ Evaluación gaps NIS2 vs estado actual
│  └─ Remediación crítica: €[X]K
│
TRIMESTRE 2 (Q2 2026)
├─ AUTOMATIZACIÓN SIEM
│  └─ Upgrade herramientas: €[Y]K
│  └─ Hiring analista extra: €[Z]K
│  └─ Meta MTTD: 87 min (vs 120 actual)
│
TRIMESTRE 3-4 (Q3-Q4 2026)
├─ RESPUESTA A INCIDENTES
│  └─ Implementación SOAR: €[W]K
│  └─ Playbooks documentadas y testadas
│  └─ Meta MTTR: <240 min
│
2027 (VISIÓN MEDIA PLAZO)
├─ MADUREZ TIER 3 ALCANZADA
│  └─ IMG proyectado: 65+ (vs 47 actual)
│  └─ Beneficio acumulativo ROI: ~180%
```

### SLIDE 11: PRESUPUESTO Y PLAN DE ACCIÓN

**Tabla:**
```
INICIATIVA              | INVERSIÓN | PLAZO    | BENEFICIO ESPERADO
════════════════════════╪═══════════╪══════════╪═════════════════════════════════
Mejora SIEM/Automatización │ €150K  | Q2-Q3 26 | MTTD: 120→70 min (42% mejora)
Respuesta Incidentes (SOAR)│ €120K  | Q3-Q4 26 | MTTR: 360→200 min (44% mejora)
Capacitación seg. especializada│ €45K│ Continuo | Reducción error humano 30%
Cumplimiento NIS2          │ €80K    | Q1 26    | Auditoría externa pasada
Consultoría externa        │ €55K    | Trimestral│ Validación independiente
────────────────────────┼─────────┼──────────┼─────────────────────────────────
TOTAL AÑO 2026         | €450K    |          | ROI Estimado: 120-150%
```

### SLIDE 12: SIGUIENTE PASOS Y PREGUNTAS

**Estructura:**
```
PRÓXIMAS ACCIONES (ESTE MES):

1. Aprobación presupuesto €450K (Junta Directiva)
   → Fecha decisión: [DATE]

2. Asignación de propietario (Executive Sponsor)
   → Responsable: [NAME]

3. Contratación de especialistas + herramientas
   → Timeline: Enero-Febrero 2026

4. Revisión trimestral de progreso
   → Métricas clave: IMG, MTTD, MTTR, ROI real vs proyectado
   → Reportes a: [STAKEHOLDER LIST]

PREGUNTAS / DISCUSIÓN
════════════════════
[Espacio para Q&A en vivo]
```

---

## NOTAS PARA EL PRESENTADOR

### Timing
- Slide 1-2: 1 min (intro + agenda)
- Slide 3-4: 3 min (contexto + IMG)
- Slide 5-7: 4 min (madurez + financiero)
- Slide 8-9: 3 min (incidentes + brechas)
- Slide 10-11: 4 min (roadmap)
- Slide 12: 2 min (Q&A)
- **TOTAL: ~17 minutos**

### Tono Recomendado
- Profesional, no catastrófico (evitar FUD)
- Orientado a soluciones (no solo problemas)
- Data-driven (números respaldan argumentos)
- Realista (no promesas imposibles)

### Antídotos para Objeciones Comunes

**Objeción 1:** "¿Por qué gastamos €450K en seguridad?"
**Respuesta:** "ROI de 120-150% anual. Evitamos breaches que nos costarían €612K+ anuales."

**Objeción 2:** "Nuestro competidor no hace esto."
**Respuesta:** "Probablemente ya sufrió un incidente. Benchmark muestra que pares nuestros gastan €X, nosotros [X/2]. Estamos asumiendo riesgo regulatorio."

**Objeción 3:** "¿No podemos hacerlo internamente?"
**Respuesta:** "Brecha de talento: 30.000 posiciones vacantes España. Outsourcing MSS + especialistas internos es modelo híbrido óptimo."

---

*Plantilla PowerPoint CRA-Cyber v2.1 — Guía Presentación*