# PLANTILLA DE CÁLCULO: EXCEL IGM, ROI Y CUADRO DE MANDO
## Especificaciones para Implementación en Hoja de Cálculo

---

## VISIÓN GENERAL

Esta plantilla implementa en Excel el cálculo integral de:
- **IGM** (Índice Global de Madurez) de 0-5
- **PD** (Puntuación por Dominio) de 0-1
- **NIM** (Índice NIST CSF) de 1-6
- **ICN** (Índice Conformidad Normativa) %
- **ROICS** (Retorno sobre Inversión en Ciberseguridad) %
- **Dashboard visual** de brechas y recomendaciones

---

## HOJA 1: ENTRADA DE DATOS (RAW_SURVEY_DATA)

### Estructura de Columnas

```
Columna A: Identificador Pregunta (P2.1, P2.2, ... P11.2)
Columna B: Sección (Gobernanza, Vulnerabilidades, etc.)
Columna C: Descripción breve pregunta
Columna D: Respuesta Numérica (1-5)
Columna E: Confianza de Respuesta (%) [Opcional: 0-100]
Columna F: Notas del Respondente
Columna G: Dominio (GR, VUL, PEN, SIEM, CAP, NORM, CONT, SUPL, CTRL, INT)
Columna H: Peso del Dominio (%)
```

### Ejemplo de Tabla

```
| Pregunta | Sección | Descripción | Respuesta | Confianza | Notas | Dominio | Peso |
|----------|---------|-------------|-----------|-----------|-------|---------|------|
| P2.1 | Gestión Riesgos | Metodología formal análisis riesgos | 3 | 85% | Tenemos ISO 27005 documentado | GR | 20% |
| P2.2 | Gestión Riesgos | Cuantificación AVRQ/FAIR | 2 | 70% | Parcial, métrica manual | GR | 20% |
| P2.3 | Gestión Riesgos | Planes de tratamiento | 3 | 90% | Todos los críticos | GR | 20% |
| P3.1 | Vulnerabilidades | Escaneo de vulnerabilidades | 4 | 95% | Semanal automatizado | VUL | 15% |
| P3.2 | Vulnerabilidades | Priorización CVSS | 4 | 80% | Pero no EPSS | VUL | 15% |
| ... | ... | ... | ... | ... | ... | ... | ... |
```

---

## HOJA 2: CÁLCULOS_IGM

### Sección 2.1: Promedios por Dominio

**Rango: A1:L15**

```
Dominio | Preguntas Incluidas | Nº Preguntas | Suma Respuestas | Promedio (0-1) | Comentario
--------|-------------------|--------------|-----------------|----------------|----------
GR | P2.1, P2.2, P2.3 | 3 | 8 | 0.533 | Parcial
VUL | P3.1, P3.2, P3.3 | 3 | 11 | 0.733 | Bueno
PEN | P4.1, P4.2 | 2 | 7 | 0.700 | Bueno
SIEM | P5.1, P5.2, P5.3 | 3 | 10 | 0.667 | Aceptable
... | ... | ... | ... | ... | ...
```

**Fórmula para Promedio Dominio:**
```Excel
=PROMEDIO([Respuestas en Dominio])/5
```

Ejemplo para GR (asumiendo respuestas en D2:D4):
```Excel
=PROMEDIO(D2:D4)/5
```

### Sección 2.2: Cálculo de IGM

**Celda B2 (IGM Final)**

```Excel
=SUMAPRODUCTO(Promedios_Dominios, Pesos_Dominios) / 5
```

Desglosado:
```Excel
=(A5*0.20 + B5*0.15 + C5*0.10 + D5*0.15 + E5*0.10 + F5*0.10 + G5*0.05 + H5*0.05 + I5*0.10 + J5*0.05) / 5
```

Donde:
- A5 = Promedio GR (Gobernanza)
- B5 = Promedio VUL (Vulnerabilidades)
- C5 = Promedio PEN (Penetración)
- D5 = Promedio SIEM
- E5 = Promedio CAP (Capacitación)
- F5 = Promedio NORM (Normativa)
- G5 = Promedio CONT (Continuidad)
- H5 = Promedio SUPL (Suministro)
- I5 = Promedio CTRL (Controles)
- J5 = Promedio INT (Inteligencia)
- 0.20, 0.15, ... = Pesos respectivos
- /5 = Normalización a escala 0-5

### Sección 2.3: Cálculo de NIM (NIST CSF)

**Celda B3**

```Excel
=IGM * 6
```

Donde:
- Resultado 1.0-1.2 → Nivel 1 (Incomplete)
- Resultado 1.2-2.4 → Nivel 2 (Managed)
- Resultado 2.4-3.6 → Nivel 3 (Defined)
- Resultado 3.6-4.8 → Nivel 4 (Quantitatively Managed)
- Resultado 4.8+ → Nivel 5/6 (Optimized)

**Fórmula de Conversión Automática (Celda B4):**

```Excel
=SI(B3<=1.2,"Nivel 1: Incomplete",SI(B3<=2.4,"Nivel 2: Managed",SI(B3<=3.6,"Nivel 3: Defined",SI(B3<=4.8,"Nivel 4: Quantitatively Managed","Nivel 5/6: Optimized"))))
```

### Sección 2.4: Cálculo de ICN (Índice Conformidad Normativa)

**Celda B5**

```Excel
=Promedio_NORM * 100
```

Donde Promedio_NORM es la puntuación ponderada del dominio "Cumplimiento Normativo".

**Interpretación:**
```
Si ICN >= 80% → "CONFORME"
Si ICN 60-79% → "PARCIALMENTE CONFORME"
Si ICN < 60% → "NO CONFORME"
```

**Fórmula de Clasificación (Celda B6):**

```Excel
=SI(B5>=80,"CONFORME",SI(B5>=60,"PARCIALMENTE CONFORME","NO CONFORME"))
```

---

## HOJA 3: CÁLCULOS_ROI

### Sección 3.1: Análisis de Inversiones de Ciberseguridad

**Tabla: Análisis Inversión Actual**

```
| Categoría | Inversión Año 1 | Inversión Año 2 | Inversión Año 3 | Total 3 Años |
|-----------|-----------------|-----------------|-----------------|--------------|
| Infraestructura (SIEM, firewalls, EDR) | €150,000 | €180,000 | €200,000 | €530,000 |
| Herramientas (escaneo, SOAR, etc.) | €50,000 | €60,000 | €70,000 | €180,000 |
| Personal (CISO, analistas, ingenieros) | €300,000 | €330,000 | €360,000 | €990,000 |
| Capacitación y servicios profesionales | €30,000 | €40,000 | €50,000 | €120,000 |
| Operación y mantenimiento | €80,000 | €100,000 | €120,000 | €300,000 |
| **TOTAL INVERSIÓN** | **€610,000** | **€710,000** | **€800,000** | **€2,120,000** |
```

**Fórmula Excel (Celda E3):**
```Excel
=SUMA(B3:D3)
```

### Sección 3.2: Cuantificación de Riesgos Mitigados (Metodología Mercury AVRQ)

**Tabla: Activos Críticos y Valoración**

```
| Activo | Valor (€) | Probabilidad Incidente (%) | Impacto Potencial (€) | AVRQ Score (0-1) | Riesgo Residual (€) |
|--------|-----------|---------------------------|----------------------|-------------------|---------------------|
| Sistemas de Pago | €10,000,000 | 5% | €2,000,000 | 0.3 | €600,000 |
| Base de Datos Clientes | €5,000,000 | 8% | €1,500,000 | 0.4 | €600,000 |
| Servidor de Email | €2,000,000 | 10% | €500,000 | 0.5 | €250,000 |
| **TOTAL VALOR PROTEGIDO** | **€17,000,000** | | | | **€1,450,000** |
```

**Fórmulas:**
```Excel
Riesgo Residual = Valor × Probabilidad × (1 - AVRQ Score)

Ejemplo (Celda F3):
=B3*C3*(1-E3)
```

### Sección 3.3: Beneficios Cuantificados (3 años)

**Tabla: Beneficios por Categoría**

```
| Beneficio | Año 1 (€) | Año 2 (€) | Año 3 (€) | Total 3 Años (€) | Justificación |
|-----------|-----------|-----------|-----------|-------------------|---------------|
| **Evitar Brechas Críticas** | €400,000 | €500,000 | €600,000 | €1,500,000 | Reducción de riesgo residual |
| **Mejora MTTR (Reducir downtime)** | €100,000 | €120,000 | €150,000 | €370,000 | Reducción de 8h a 2h: ~€50/hora |
| **Evitar Multas NIS2** | €500,000 | €1,000,000 | €0 | €1,500,000 | 0.5% × €2B potencial (años 1-2) |
| **Mejora de Confianza (Clientes)** | €50,000 | €80,000 | €120,000 | €250,000 | Retención de clientes risk-averse |
| **Reducción de Incidentes (Costo promedio €80K)** | €160,000 | €240,000 | €320,000 | €720,000 | Reducción de 2→1 incidentes/año |
| **Automatización (reducir personal manual)** | €30,000 | €50,000 | €80,000 | €160,000 | SOAR + automatización procesos |
| **TOTAL BENEFICIOS** | **€1,240,000** | **€1,990,000** | **€1,270,000** | **€4,500,000** | |
```

**Fórmula Excel (Celda E8 - Total Beneficios Año 1):**
```Excel
=SUMA(B3:B7)
```

### Sección 3.4: Cálculo de ROICS (Return on Investment in Cybersecurity)

**Celda B10:**

```Excel
=((E8 - E2) / E2) * 100
```

Donde:
- E8 = Total Beneficios 3 años (€4,500,000)
- E2 = Total Inversión 3 años (€2,120,000)

**Resultado Esperado:**
```
ROICS = (4,500,000 - 2,120,000) / 2,120,000 × 100 = 112%
```

**Interpretación:**
```
ROICS > 100% → Excelente (beneficio >costo)
ROICS 50-100% → Muy bueno
ROICS 25-50% → Bueno (justificable)
ROICS 0-25% → Aceptable (beneficio regulatorio)
ROICS < 0% → Requiere revisión (pérdida financiera)
```

### Sección 3.5: Payback Period (Período de Recuperación)

**Celda B11:**

```Excel
=REDONDEAR(E2 / (E8 / 3), 1)
```

Donde:
- E2 = Inversión total 3 años
- E8/3 = Beneficio promedio anual

**Resultado:** ~1.4 años hasta recuperar inversión

---

## HOJA 4: BRECHAS Y RECOMENDACIONES

### Sección 4.1: Matriz de Brechas

**Tabla: Brecha por Dominio**

```
| Dominio | Puntuación Actual | Objetivo (Taget) | Brecha | Peso | Criticidad | Prioridad |
|---------|-------------------|------------------|--------|------|-----------|-----------|
| GR | 2.5 | 4.5 | 2.0 | 20% | Alta (NIS2) | **CRÍTICA** |
| VUL | 3.4 | 4.5 | 1.1 | 15% | Alta (raíz) | **ALTA** |
| SIEM | 3.0 | 4.5 | 1.5 | 15% | Crítica (EE) | **CRÍTICA** |
| CAP | 2.8 | 4.0 | 1.2 | 10% | Media | MEDIA |
| NORM | 2.2 | 4.5 | 2.3 | 10% | Crítica (NIS2) | **CRÍTICA** |
| CONT | 3.5 | 4.5 | 1.0 | 5% | Media | MEDIA |
| SUPL | 2.9 | 4.0 | 1.1 | 5% | Media | MEDIA |
| CTRL | 3.2 | 4.5 | 1.3 | 10% | Alta | **ALTA** |
| INT | 2.5 | 4.0 | 1.5 | 5% | Media | MEDIA |
```

**Fórmula Brecha (Celda D2):**
```Excel
=C2-B2
```

**Fórmula Prioridad (Celda G2):**
```Excel
=D2*E2
```

Ordenar por Prioridad descendente para identificar dominios requieren acción inmediata.

### Sección 4.2: Recomendaciones Automáticas

**Regla: Si Brecha > 1.0 y Criticidad Alta → Recomendación Nivel 1**

```
Dominio GR (Brecha 2.0):
✓ Implementar cuantificación AVRQ (Mercury)
✓ Automatizar cálculo de ROI para inversiones de seguridad
✓ Establecer gobierno formal con comité de riesgos

Dominio SIEM (Brecha 1.5):
✓ Desplegar o mejorar SIEM existente
✓ Tuning de reglas para reducir falsos positivos
✓ Establecer SLA de MTTR <4h para incidentes críticos

Dominio NORM (Brecha 2.3):
✓ Iniciar transposición NIS2 (ley entra en vigor Q1 2026)
✓ Documentar todas las medidas técnicas y organizacionales
✓ Designar responsable de notificación ante CNCS
```

---

## HOJA 5: CUADRO DE MANDO (DASHBOARD)

### Sección 5.1: KPIs Principales

**Tabla Visual (usar gráficos condicionales)**

```
┌─────────────────────────────────────────────┐
│         ÍNDICE GLOBAL DE MADUREZ (IGM)      │
│                 3.2 / 5.0                   │
│              [████████░░░░░░░░░] 64%         │
│           Clasificación: TIER 3 - ESTABLECIDO│
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│     NIVEL NIST CSF (NIM): 3.2 / 6.0        │
│   Nivel 3 (Defined) - Procesos Establecidos │
│  Objetivo: Nivel 4 (Quantitatively Managed) │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  CONFORMIDAD NORMATIVA (ICN): 68% CUMPLIMIENTO│
│         Clasificación: PARCIALMENTE CONFORME │
│   Requiere acción antes de Q1 2026 (NIS2)   │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│   ROICS (3 años): 112% - EXCELENTE         │
│  Beneficios: €4.5M | Inversión: €2.1M     │
│      Payback Period: 1.4 años               │
└─────────────────────────────────────────────┘
```

### Sección 5.2: Gráfico de Dominios (Radar/Araña)

**Estructura:**

```
         GR     NORM   CONT
          |      |      |
    5.0  ★------★------★
         │      │      │
    4.0 │  ╱────┼────╲  │
        │ ╱     │     ╲ │
    3.0│▓▓ 2.5 │3.0  ▓▓│ SIEM 3.0
       │▓▓     │     ▓▓ │
    2.0│▓▓▓────┼────▓▓▓│ VUL 3.4
       │▓▓▓   │    ▓▓▓  │
    1.0│▓▓▓▓──┼───▓▓▓▓ │
       │▓▓▓▓ │  ▓▓▓▓  │
    0.0 ─────┼─────────
         CAP INT CTRL

Línea interior = Actual
Línea exterior = Objetivo
```

**Implementación en Excel:**
- Usar gráfico Radar con datos de Dominio
- Línea 1: Puntuaciones actuales (B2:K2)
- Línea 2: Objetivos (B3:K3)

### Sección 5.3: Semáforo de Conformidad Regulatoria

```
┌─ NIS2 Art. 20 (Análisis Riesgos) ───────┐
│ Status: 🟠 PARCIALMENTE CONFORME      │
│ Cumple: 70% | Gaps: Cuantificación AVRQ │
└──────────────────────────────────────────┘

┌─ NIS2 Art. 21 (Medidas Técnicas) ───────┐
│ Status: 🟢 CONFORME                    │
│ Cumple: 90% | Gaps: Testing penetración │
└──────────────────────────────────────────┘

┌─ NIS2 Art. 22 (Capacitación) ──────────┐
│ Status: 🟠 PARCIALMENTE CONFORME      │
│ Cumple: 65% | Gaps: Alto dirigentes    │
└──────────────────────────────────────────┘

┌─ ISO 27001 General ─────────────────────┐
│ Status: 🟠 PARCIALMENTE CONFORME      │
│ Cumple: 68% | Objetivo: Certificación   │
└──────────────────────────────────────────┘
```

**Codificación Colores en Excel:**

```Excel
Celda Status:
=SI(Conformidad>=80%,"🟢 CONFORME",SI(Conformidad>=60%,"🟠 PARCIALMENTE","🔴 NO CONFORME"))
```

### Sección 5.4: Roadmap de 12 Meses

```
Q1 2026 (Trimestre 1)
├─ Acción 1: Implementar AVRQ Mercury [GR]
├─ Acción 2: Tuning SIEM, reducir FPR [SIEM]
└─ Recurso: €200K | Crítica NIS2

Q2 2026 (Trimestre 2)
├─ Acción 1: ISO 27001 formal assessment
├─ Acción 2: Certificación primera etapa
└─ Recurso: €150K | Alta impacto

Q3 2026 (Trimestre 3)
├─ Acción 1: Expandir A.D.A.M. mapeo
├─ Acción 2: Testing penetración anual
└─ Recurso: €100K | Operacional

Q4 2026 (Trimestre 4)
├─ Acción 1: Evaluación de mejora (re-encuesta)
├─ Acción 2: Planificación 2027
└─ Recurso: €50K | Evaluación
```

---

## VALIDACIONES Y CONTROLES DE CALIDAD

### Validación 1: Rango de Respuestas

```Excel
En Hoja RAW_SURVEY_DATA, Columna D:
=SI(Y(D2>=1,D2<=5,MOD(D2,1)=0),"✓ Válida","✗ Inválida")
```

Asegura que todas las respuestas estén entre 1-5 y sean enteros.

### Validación 2: Completitud de Datos

```Excel
=CONTAR(BLANCO(RAW_SURVEY_DATA!D:D))
```

Si resultado > 0 → Hay preguntas sin respuesta

### Validación 3: Consistencia de Pesos

```Excel
=SUMA(Pesos_Dominios)
```

Debe ser = 100% (1.0 en decimal)

---

## INSTRUCCIONES DE USO

1. **Completar RAW_SURVEY_DATA:** Copiar respuestas de encuesta en columna D
2. **Ejecutar CÁLCULOS_IGM:** Fórmulas se recalculan automáticamente
3. **Revisar CÁLCULOS_ROI:** Ajustar inversiones reales si es necesario
4. **Consultar BRECHAS:** Identificar top 3 dominios con mayor prioridad
5. **Usar DASHBOARD:** Mostrar a Junta Directiva para decisiones

---

## EXPORTACIÓN Y REPORTERÍA

### Exportar a PowerPoint
- Copiar Dashboard → Pegado especial como imagen
- Incorporar en Informe Ejecutivo (Hoja 6)

### Exportar a PDF
- Archivo > Exportar > PDF
- Seleccionar hojas: DASHBOARD + BRECHAS

---

*Plantilla diseñada para ser flexible y escalable. Ajustar pesos de dominios según prioridades organizacionales.*

**Versión 2.0 | Enero 2026**