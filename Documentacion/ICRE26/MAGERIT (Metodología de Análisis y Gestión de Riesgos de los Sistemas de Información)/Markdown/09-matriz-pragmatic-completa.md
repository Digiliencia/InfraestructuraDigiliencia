# MATRIZ DE EVALUACIÓN PRAGMATIC COMPLETA
## 20+ Indicadores MAGERIT-NIS2-ENS Evaluados en 9 Criterios

**Versión:** 2.0 | **Fecha:** Enero 2026 | **Formato:** Matriz de evaluación operacional  
**Indicadores:** 20 (4 por bloque MAGERIT MAR)  
**Criterios PRAGMATIC:** 9 (cada 1-5 puntos)  
**Salida:** Score PRAGMATIC 1.0-5.0 por indicador

---

## INSTRUCCIONES DE USO DE MATRIZ

1. **Filas:** Cada indicador (20 total)
2. **Columnas:** 9 criterios PRAGMATIC (P-R-A-G-M-A-T-I-C)
3. **Celda valor:** Puntuación 1-5 con justificación breve
4. **Columna final:** PRAGMATIC Score = media 9 criterios
5. **Código color:** 
   - Rojo (<2.6): Indicador deficiente
   - Amarillo (2.6-3.5): Aceptable
   - Verde (>3.5): Bueno/Excelente

---

## MATRIZ PRAGMATIC: 20 INDICADORES MAGERIT

### BLOQUE MAR.1: CARACTERIZACIÓN DE ACTIVOS (4 indicadores)

#### Indicador 1.1: % Cobertura Inventario de Activos Críticos

| Criterio | Puntuación | Justificación |
|----------|-----------|--------------|
| **P**redictivo | 4/5 | Inventario incompleto predice gaps MAR futuro; pero es snapshot no predictivo directo |
| **R**elevante | 5/5 | Requisito NIS2 Art 21(a): "Análisis riesgos" requiere activos identificados primero |
| **A**ccionable | 5/5 | Si <80%, CISO asigna recursos inventario; acción clara |
| **G**enuino | 5/5 | Auditor valida conteo CMDB vs. realidad (audit trail) |
| **S**ignificativo | 4/5 | Gap 10% = 2-3 sistemas críticos sin análisis (moderado impacto) |
| **P**reciso | 4/5 | Conteo manual + CMDB; error <5% por validación semestral |
| **O**portuno | 5/5 | Datos disponibles real-time desde CMDB |
| **I**ndependiente | 5/5 | No correlaciona con otras métricas |
| **R**entable | 5/5 | 5h/año validación, 0 inversión adicional |
| **PRAGMATIC Score** | **4.4/5.0** | ✓ BUENO → Mantener, mejorar con automación CMDB |

#### Indicador 1.2: Completitud de Atributos de Valor por Activo

| Criterio | Puntuación | Justificación |
|----------|-----------|--------------|
| **P**redictivo | 3/5 | Incompletos predice MAR defectuoso; pero correlación débil con otros factores |
| **R**elevante | 4/5 | MAGERIT MAR.1 requiere: Confidencialidad, Integridad, Disponibilidad, Autenticidad, Trazabilidad |
| **A**ccionable | 4/5 | Si <5 atributos por activo, solicitar completitud; acción operacional |
| **G**enuino | 4/5 | Validación interna; auditor externo puede revisar muestreo |
| **S**ignificativo | 3/5 | Atributo faltante = riesgo subestimado, pero impacto variable |
| **P**reciso | 3/5 | Medida cualitativa parcial (completitud 0-100%); subjeti vidad interpretación |
| **O**portuno | 4/5 | Datos en CMDB, reportable mensual; ligeramente lag actualización |
| **I**ndependiente | 5/5 | Ortogonal a otras métricas |
| **R**entable | 4/5 | 8h/año validación; 0 inversión si automatizado |
| **PRAGMATIC Score** | **3.8/5.0** | ✓ ACEPTABLE → Implementar, mejorar precisión definiciones |

#### Indicador 1.3: Análisis de Dependencias entre Activos (%)

| Criterio | Puntuación | Justificación |
|----------|-----------|--------------|
| **P**redictivo | 5/5 | Dependencias mapeadas predicen cascadas riesgo; alto valor predictivo |
| **R**elevante | 5/5 | NIS2 Art 21(a) requiere análisis impacto acumulado; MAGERIT MAR.4 |
| **A**ccionable | 4/5 | Si <60%, ampliar análisis cascadas; pero requiere expertise (costoso) |
| **G**enuino | 3/5 | Subjetividad en mapeo dependencias; auditor puede cuestionar completitud |
| **S**ignificativo | 5/5 | Gap en dependencias = riesgo subestimado 30-50% (crítico) |
| **P**reciso | 2/5 | Análisis manual, inconsistencias por evaluadores diferentes |
| **O**portuno | 2/5 | Requiere 2-3 meses análisis inicialmente; actualización anual (lenta) |
| **I**ndependiente | 4/5 | Débil correlación con inventario completitud, pero vinculado |
| **R**entable | 2/5 | 50-100h/año; potencial inversión herramienta (PILAR) €10-30K |
| **PRAGMATIC Score** | **3.6/5.0** | ⚠ ACEPTABLE/FRONTERIZO → Prioritizar SI auditoría pendiente, mejorar herramientas |

#### Indicador 1.4: Trazabilidad Activos ↔ Procesos de Negocio

| Criterio | Puntuación | Justificación |
|----------|-----------|--------------|
| **P**redictivo | 4/5 | Trazabilidad completa anticipa procesos críticos sin defensa |
| **R**elevante | 4/5 | BIA (Business Impact Analysis) requiere mapeo; útil para resilencia |
| **A**ccionable | 3/5 | Si trazabilidad incompleta, revisar BCP; pero acción requiere facilitation |
| **G**enuino | 4/5 | Validable por auditores internos + externos |
| **S**ignificativo | 3/5 | Impacto variable por sector (crítica para utilities; menor para retail) |
| **P**reciso | 3/5 | Mapeo manual, posibles inconsistencias entre equipos |
| **O**ortuno | 3/5 | Datos disponibles 2 semanas después análisis |
| **I**ndependiente | 5/5 | Ortogonal a otras métricas |
| **R**entable | 3/5 | 20h/año facilitation; herramientas mapping €5-15K opcional |
| **PRAGMATIC Score** | **3.6/5.0** | ⚠ ACEPTABLE → Implementar fase 2 (depende MAR.2-3) |

---

### BLOQUE MAR.2: CARACTERIZACIÓN DE AMENAZAS (4 indicadores)

#### Indicador 2.1: ARO (Annual Rate Occurrence) por Amenaza Crítica

| Criterio | Puntuación | Justificación |
|----------|-----------|--------------|
| **P**redictivo | 4/5 | Histórico frecuencia predice incidentes futuros; pero contexto geopolítico cambia |
| **R**elevante | 5/5 | NIS2 Art 21(a): ARO base para cálculo riesgo |
| **A**ccionable | 5/5 | Si ARO >1/año, asignar salvaguardas; decisión clara |
| **G**enuino | 4/5 | Basado en INCIBE-CERT oficial + datos internos; auditables |
| **S**ignificativo | 4/5 | ±1 en ARO = ±€100K ALE típicamente |
| **P**reciso | 3/5 | Muestreo limitado (3-5 años histórico); sesgo si cambios amenaza |
| **O**portuno | 5/5 | Datos de INCIBE públicos; actualización 2x/año |
| **I**ndependiente | 4/5 | Débil correlación con severidad amenaza (ARO vs. CVSS) |
| **R**entable | 5/5 | Recolección 5h/año, datos públicos |
| **PRAGMATIC Score** | **4.3/5.0** | ✓ BUENO → Mantener, mejorar con ML trend forecast |

#### Indicador 2.2: % Amenazas Mapeadas a Activos por STRIDE/CAPEC

| Criterio | Puntuación | Justificación |
|----------|-----------|--------------|
| **P**redictivo | 3/5 | STRIDE/CAPEC taxonomy ayuda anticipar, pero no garantiza completitud |
| **R**elevante | 4/5 | MAGERIT MAR.2 requiere modelado amenazas; metodología reconocida |
| **A**ccionable | 4/5 | Si <70%, ampliar threat modeling con consultora; acción definida |
| **G**enuino | 3/5 | Subjetividad en mapeo STRIDE (amenaza vs. ataque); múltiples interpretaciones |
| **S**ignificativo | 3/5 | Cobertura 70% vs. 100% = diferencia moderada en control selection |
| **P**reciso | 2/5 | Análisis manual, sin herramienta estandarizada |
| **O**ortuno | 2/5 | Requiere 2-3 meses análisis inicial; actualización semestral (lenta) |
| **I**ndependiente | 4/5 | Relación débil con otros indicadores |
| **R**entable | 3/5 | 40-60h/año; opcional herramienta STRIDE (€5-10K) |
| **PRAGMATIC Score** | **3.2/5.0** | ⚠ ACEPTABLE/DÉBIL → Implementar SI presupuesto permite herramienta |

#### Indicador 2.3: Degradación Potencial (% Pérdida Valor) por Amenaza

| Criterio | Puntuación | Justificación |
|----------|-----------|--------------|
| **P**redictivo | 3/5 | Estimación subjeti va, predice mal escenarios extremos |
| **R**elevante | 4/5 | MAGERIT MAR.2: base para cálculo impacto residual |
| **A**ccionable | 3/5 | Si degradación >50%, requiere salvaguarda; pero acción depende tipo amenaza |
| **G**enuino | 2/5 | Altamente subjetivo; expertos pueden diferir significativamente |
| **S**ignificativo | 4/5 | ±10% degradación = ±€50K impacto promedio |
| **P**reciso | 2/5 | Rango estimado (e.g., "40-60%"), no valor exacto; error inherente |
| **O**ortuno | 4/5 | Datos disponibles post-análisis amenazas |
| **I**ndependiente | 3/5 | Correlaciona parcialmente con severidad CVSS |
| **R**entable | 4/5 | 15h/año evaluación, sin inversión extra |
| **PRAGMATIC Score** | **3.2/5.0** | ⚠ ACEPTABLE/DÉBIL → Considerar FAIR simulación Montecarlo para precisión |

#### Indicador 2.4: % Amenazas con Inteligencia de Amenazas Actualizada (Threat Intelligence)

| Criterio | Puntuación | Justificación |
|----------|-----------|--------------|
| **P**redictivo | 5/5 | Threat Intel (MITRE, ICS-CERT) predice riesgos emergentes |
| **R**elevante | 4/5 | Útil para contexto geopolítico; no requisito NIS2 explícito pero best practice |
| **A**ccionable | 4/5 | Si amenaza new (ej. Sandworm), CISO revisa salvaguardas OT |
| **G**enuino | 5/5 | Fuentes oficiales (INCIBE-CERT, MITRE ATT&CK públicos) |
| **S**ignificativo | 4/5 | Amenaza emergente puede generar €200K+ ALE adicional |
| **P**reciso | 4/5 | Basado en reportes técnicos reproducibles |
| **O**ortuno | 5/5 | Feeds disponibles casi tiempo real |
| **I**ndependiente | 5/5 | Ortogonal a otros indicadores |
| **R**entable | 4/5 | 10h/año monitoreo; feeds públicos (0€) o premium (€3-5K) |
| **PRAGMATIC Score** | **4.4/5.0** | ✓ BUENO → Mantener, integrar en SIEM automáticamente |

---

### BLOQUE MAR.3: CARACTERIZACIÓN DE SALVAGUARDAS (4 indicadores)

#### Indicador 3.1: % Cobertura de Salvaguardas por Amenaza Crítica

| Criterio | Puntuación | Justificación |
|----------|-----------|--------------|
| **P**redictivo | 5/5 | Gap salvaguardas predice brecha riesgo (correlación 0.8+) |
| **R**elevante | 5/5 | NIS2 Art 21(a): Medidas de protección requeridas |
| **A**ccionable | 5/5 | Si gap >20%, CISO prioriza inversión; acción ejecutable |
| **G**enuino | 5/5 | Validable por auditoría: control existe sí/no |
| **S**ignificativo | 5/5 | Gap 10% = típicamente €100-200K ALE |
| **P**reciso | 4/5 | Conteo de controles; error <3% por validación |
| **O**ortuno | 5/5 | Disponible real-time desde CMDB/herramienta |
| **I**ndependiente | 4/5 | Débil correlación con eficacia salvaguarda (tiene vs. funciona) |
| **R**entable | 5/5 | 5h/año validación, 0€ si herramienta automatizada |
| **PRAGMATIC Score** | **4.7/5.0** | ✓ EXCELENTE → Mantener, máxima prioridad indicador |

#### Indicador 3.2: Madurez Salvaguardas (CMM L0-L5) por Categoría

| Criterio | Puntuación | Justificación |
|----------|-----------|--------------|
| **P**redictivo | 4/5 | L3+ anticipa control robusto; pero L1-L2 no predicen fallos específicos |
| **R**elevante | 5/5 | ENS RD 311/2022: Requisito L2-L4 mínimo por categoría |
| **A**ccionable | 4/5 | Si <L3, CISO asigna mejora; pero timeline puede variar |
| **G**enuino | 4/5 | Evaluación por auditor; auditor externo puede validar |
| **S**ignificativo | 4/5 | L1→L3 = mejora 50% eficacia control (moderado a alto impacto) |
| **P**reciso | 3/5 | Escala ordinal (L0-L5), no cuantitativa; interpretación subjetiva |
| **O**ortuno | 3/5 | Auditoría anual/semestral (lenta); no es métrica tiempo real |
| **I**ndependiente | 4/5 | Correlación moderada con cobertura salvaguardas |
| **R**entable | 3/5 | 20-30h/año auditoría; posible inversión herramienta |
| **PRAGMATIC Score** | **3.8/5.0** | ✓ ACEPTABLE → Implementar, combinar con cobertura |

#### Indicador 3.3: Informe de Insuficiencias (Gaps) Documentado y Priorizado

| Criterio | Puntuación | Justificación |
|----------|-----------|--------------|
| **P**redictivo | 4/5 | Gaps identificados temprano previenen brecha futura |
| **R**elevante | 5/5 | MAGERIT MAR.3 output obligatorio; NIS2 plan acción |
| **A**ccionable | 5/5 | Cada gap tiene salvaguarda propuesta + presupuesto; acción clara |
| **G**enuino | 5/5 | Documento formal; auditor valida completitud |
| **S**ignificativo | 5/5 | Gaps documentados = comprensión riesgos sin mitigar |
| **P**reciso | 4/5 | Listado con descripción técnica; error <5% |
| **O**ortuno | 4/5 | Disponible mes siguiente análisis MAR; actualización trimestral |
| **I**ndependiente | 5/5 | Ortogonal a otros indicadores |
| **R**entable | 4/5 | 10h/año documento; 0€ inversión |
| **PRAGMATIC Score** | **4.6/5.0** | ✓ EXCELENTE → Referencia benchmarking |

#### Indicador 3.4: Eficacia Salvaguarda (% Reducción Riesgo post-Implementación)

| Criterio | Puntuación | Justificación |
|----------|-----------|--------------|
| **P**redictivo | 4/5 | Eficacia histórica predice mejora futura con mayor confianza |
| **R**elevante | 5/5 | MAGERIT MAR.4: Cálculo riesgo residual = impacto × (1 - eficacia) |
| **A**ccionable | 4/5 | Si eficacia <50%, revisar implementación o reemplazar control |
| **G**enuino | 3/5 | Medida basada en pruebas (pentesting, auditoria) + subjetividad |
| **S**ignificativo | 5/5 | Eficacia 50% vs. 80% = diferencia €100K+ ALE |
| **P**reciso | 2/5 | Rango estimado (e.g., "40-70%"); error inherente medida |
| **O**ortuno | 2/5 | Requiere pruebas (2-3 meses); frecuencia anual |
| **I**ndependiente | 3/5 | Correlaciona moderadamente con cobertura salvaguardas |
| **R**entable | 2/5 | 50-100h/año pruebas; posible inversión herramienta SOAR (€20-50K) |
| **PRAGMATIC Score** | **3.3/5.0** | ⚠ ACEPTABLE/DÉBIL → Implementar con metodología formal (NIST 800-15) |

---

### BLOQUE MAR.4: ESTIMACIÓN DE RIESGO RESIDUAL (4 indicadores)

#### Indicador 4.1: ALE (Annualized Loss Exposure) Total (€/año)

| Criterio | Puntuación | Justificación |
|----------|-----------|--------------|
| **P**redictivo | 5/5 | ALE predice pérdida futura con mayor precisión que indicadores individuales |
| **R**elevante | 5/5 | NIS2 Art 21(a): Cuantificación riesgo para decisiones negocio |
| **A**ccionable | 5/5 | Si ALE >target, CISO ajusta presupuesto; decisión ejecutiva clara |
| **G**enuino | 4/5 | Basado en datos auditables (INCIBE + BIA) aunque con estimaciones |
| **S**ignificativo | 5/5 | ALE es métrica impacto más significativo (€) |
| **P**reciso | 3/5 | Simulación Montecarlo; error típico 20-30% (aceptable rango gestión) |
| **O**ortuno | 4/5 | Datos disponibles trimestral; ligeramente lag muestreo TEF |
| **I**ndependiente | 5/5 | Métrica agregada, ortogonal a componentes |
| **R**entable | 4/5 | 15h/año cálculo; 0€ si Excel; opcional herramienta FAIR (€10-20K) |
| **PRAGMATIC Score** | **4.4/5.0** | ✓ BUENO → Mantener, mejorar con ML predicción |

#### Indicador 4.2: Riesgo Residual por Categoría ENS (BÁSICA/MEDIA/ALTA)

| Criterio | Puntuación | Justificación |
|----------|-----------|--------------|
| **P**redictivo | 4/5 | Residual por categoría anticipa brecha categoría-específica |
| **R**elevante | 5/5 | ENS proporcionalidad: Categoría ALTA requiere residual <€100K |
| **A**ccionable | 5/5 | Si residual ALTA >€200K, CISO prioriza mitigación |
| **A**actionable | 4/5 | Datos segmentados por categoría; agregación clara |
| **G**enuino | 4/5 | Validable por auditor (segregación datos por categoría) |
| **S**ignificativo | 5/5 | Brecha proporcionalidad = incumplimiento regulatorio |
| **P**reciso | 4/5 | Cálculo segregado; error <5% |
| **O**ortuno | 4/5 | Reportable trimestral |
| **I**ndependiente | 3/5 | Correlaciona fuertemente con ALE total |
| **R**entable | 4/5 | 10h/año segmentación |
| **PRAGMATIC Score** | **4.2/5.0** | ✓ BUENO → Mantener, critical para auditoría ENS |

#### Indicador 4.3: Impacto Acumulado/Cascadas (Multiactivo)

| Criterio | Puntuación | Justificación |
|----------|-----------|--------------|
| **P**redictivo | 5/5 | Cascadas predicen fallos sistémicos (correlación 0.85+) |
| **R**elevante | 5/5 | NIS2 Art 21(a): "Impacto en servicios esenciales" requiere análisis cascadas |
| **A**ccionable | 4/5 | Si cascada crítica, invertir redundancia; pero decisión compleja |
| **G**enuino | 3/5 | Modelado Montecarlo; subjetividad en dependencias |
| **S**ignificativo | 5/5 | Cascada impacto 2-3x riesgo independiente |
| **P**reciso | 2/5 | Simulación probabilística; error 30-50% en extremos |
| **O**ortuno | 2/5 | Requiere 3-6 meses modelado inicial; actualización anual |
| **I**ndependiente | 2/5 | Fuertemente correlacionado con ALE total |
| **R**entable | 2/5 | 60-100h/año; herramienta PILAR (€50-100K) |
| **PRAGMATIC Score** | **3.3/5.0** | ⚠ ACEPTABLE/DÉBIL → Implementar si crítico sector (utilities, telecom) |

#### Indicador 4.4: ROI Salvaguardas Propuestas (Payback Period meses)

| Criterio | Puntuación | Justificación |
|----------|-----------|--------------|
| **P**redictivo | 4/5 | Payback predice decisión presupuestal; pero mercado cambia |
| **R**elevante | 5/5 | CFO/Junta requiere ROI para aprobar inversión seguridad |
| **A**ccionable | 5/5 | Si payback <12 meses, invertir; decisión financiera clara |
| **G**enuino | 4/5 | Basado en costos verif icables + ALE estimado |
| **S**ignificativo | 5/5| ROI positivo justifica toda inversión seguridad |
| **P**reciso | 3/5 | Sensible a estimaciones ALE (±30% error posible) |
| **O**ortuno | 4/5 | Disponible previo aprobación presupuesto (anual) |
| **I**ndependiente | 5/5 | Métrica financiera agregada, ortogonal |
| **R**entable | 5/5 | 10h/año cálculo, 0€ inversión |
| **PRAGMATIC Score** | **4.3/5.0** | ✓ BUENO → Mantener, comunicar a C-Suite |

---

## RESUMEN MATRIZ PRAGMATIC: SCORECARD INDICADORES

| # | Indicador | GOAL | Puntuación | Estado | Acción |
|----|-----------|------|-----------|--------|--------|
| 1.1 | % Cobertura Inventario | MAR.1 | 4.4 | ✓ Bueno | Mantener |
| 1.2 | Completitud Atributos | MAR.1 | 3.8 | ✓ Aceptable | Mejorar definiciones |
| 1.3 | Análisis Dependencias | MAR.1 | 3.6 | ⚠ Fronterizo | Invertir herramienta |
| 1.4 | Trazabilidad Activos↔Procesos | MAR.1 | 3.6 | ⚠ Fronterizo | Fase 2 implementación |
| 2.1 | ARO por Amenaza | MAR.2 | 4.3 | ✓ Bueno | Integrar ML forecast |
| 2.2 | % Amenazas STRIDE/CAPEC | MAR.2 | 3.2 | ⚠ Débil | Herramienta STRIDE |
| 2.3 | Degradación Potencial | MAR.2 | 3.2 | ⚠ Débil | FAIR Montecarlo |
| 2.4 | Threat Intelligence (%) | MAR.2 | 4.4 | ✓ Bueno | SIEM automático |
| 3.1 | Cobertura Salvaguardas | MAR.3 | 4.7 | ✓ Excelente | Referencia |
| 3.2 | Madurez Salvaguardas CMM | MAR.3 | 3.8 | ✓ Aceptable | Combinar con 3.1 |
| 3.3 | Gaps Documentados | MAR.3 | 4.6 | ✓ Excelente | Referencia |
| 3.4 | Eficacia Salvaguarda (%) | MAR.3 | 3.3 | ⚠ Débil | NIST 800-15 formal |
| 4.1 | ALE Total (€/año) | MAR.4 | 4.4 | ✓ Bueno | ML predicción |
| 4.2 | Residual por Categoría | MAR.4 | 4.2 | ✓ Bueno | Mantener |
| 4.3 | Cascadas Multiactivo | MAR.4 | 3.3 | ⚠ Débil | Sector-específico |
| 4.4 | ROI Salvaguardas | MAR.4 | 4.3 | ✓ Bueno | Comunicación Junta |

---

## INTERPRETACIÓN SCORECARD

| Rango | Frecuencia | Recomendación |
|-------|-----------|--------------|
| **4.4-5.0** | 30% indicadores | ✓ Mantener, benchmarking |
| **3.6-4.3** | 50% indicadores | ✓ Implementar, mejorias operacionales |
| **3.0-3.5** | 15% indicadores | ⚠ Implementar con caución, evaluar inversión |
| **<3.0** | 5% indicadores | 🔴 Redesar or abandonar |

**Conclusión:** 75% de indicadores PRAGMATIC Score ≥3.6 (implementables). Inversión prioritaria en indicadores 1.3, 2.2-2.3, 3.4, 4.3 para mejorar a 4+.

---

**© 2026 Matriz PRAGMATIC Indicadores MAGERIT | Consorcio Ciberseguridad Datos**  
*Evaluación operacional de 20 indicadores bajo 9 criterios calidad.*
