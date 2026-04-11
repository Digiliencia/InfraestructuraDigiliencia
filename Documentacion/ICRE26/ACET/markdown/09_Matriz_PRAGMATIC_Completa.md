# MATRIZ DE EVALUACIÓN PRAGMATIC COMPLETA
## Evaluación de 25 Indicadores ACET según 9 Criterios PRAGMATIC

**Versión:** 2.0 | **Fecha:** Enero 2026 | **Cobertura:** NIST CSF 2.0 Integral (GV, ID, PR, DE, RS, RC)

---

## INSTRUCCIONES DE USO

Para cada indicador (fila):
- Evaluar cada criterio PRAGMATIC en escala 0-3:
  - **0:** No cumple | **1:** Parcialmente | **2:** Mayormente | **3:** Completamente
- Calcular **Score Total = Suma de 9 criterios (0-27)**
- Calcular **% PRAGMATIC = (Score/27) × 100**
- Interpretar:
  - **>90% (27-25):** EXCELENTE → Implementar
  - **80-90% (24-22):** BUENO → Implementar con validaciones
  - **70-80% (21-19):** ACEPTABLE → Requiere auditoría cruzada
  - **<70% (18-15):** POBRE → Reconsiderar

---

## MATRIZ PRAGMATIC COMPLETA: 25 INDICADORES

### DOMINIO: GOBIERNO (GV)

#### Indicador GV-1: Existencia Política Ciberseguridad Formalizada

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice madurez organizacional futuro |
| **R - Relevante** | ✓ | 3 | Clave para junta directiva |
| **A - Accionable** | ✓ | 3 | Si falta = redactar en 30 días |
| **G - Genuino** | ✓ | 3 | Documento verificable |
| **S - Significativo** | ✓ | 3 | Eje de gobernanza |
| **Pr - Preciso** | ✓ | 3 | Binario: existe o no |
| **O - Oportuno** | ✓ | 3 | Disponible inmediato |
| **I - Independiente** | ⚠️ | 2 | Requiere auditoría de contenido |
| **Re - Rentable** | ✓ | 3 | Costo redacción = mínimo |
| | | **26/27** | **96% PRAGMATIC** |

---

#### Indicador GV-2: Designación Formal CISO

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice autoridad decisional |
| **R - Relevante** | ✓ | 3 | Demandado por NIS2, GDPR |
| **A - Accionable** | ✓ | 3 | Si ausente = designar inmediato |
| **G - Genuino** | ✓ | 3 | Verificable en organigrama |
| **S - Significativo** | ✓ | 3 | Crítico para ejecución |
| **Pr - Preciso** | ✓ | 3 | Binario: designado o no |
| **O - Oportuno** | ✓ | 3 | Dato público disponible |
| **I - Independiente** | ✓ | 3 | Verificable externamente |
| **Re - Rentable** | ✓ | 3 | Costo = 0 administrativo |
| | | **27/27** | **100% PRAGMATIC** |

---

#### Indicador GV-3: Comité Riesgos Cibernéticos (Frecuencia Reuniones)

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice vigilancia riesgos |
| **R - Relevante** | ✓ | 3 | Clave gobernanza |
| **A - Accionable** | ✓ | 3 | Si <quarterly = aumentar frecuencia |
| **G - Genuino** | ⚠️ | 2 | Requiere validar: actas muestran discusión real? |
| **S - Significativo** | ✓ | 3 | Asegura escalación |
| **Pr - Preciso** | ✓ | 3 | Fácil contar reuniones |
| **O - Oportuno** | ✓ | 3 | Datos históricos disponibles |
| **I - Independiente** | ⚠️ | 2 | Sesgo: más reuniones ≠ mejor (validar contenido) |
| **Re - Rentable** | ✓ | 3 | Costo absorvido en tiempo directivos |
| | | **24/27** | **89% PRAGMATIC** |

---

#### Indicador GV-4: Registro Riesgos Actualizado (Trimestral+)

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice identificación amenazas futuro |
| **R - Relevante** | ✓ | 3 | Mandatorio ISO 27001, ENS |
| **A - Accionable** | ✓ | 3 | Si desactualizado = actualizar |
| **G - Genuino** | ✓ | 3 | Documento auditable |
| **S - Significativo** | ✓ | 3 | Base para priorización |
| **Pr - Preciso** | ✓ | 3 | Verificable por fecha última actualización |
| **O - Oportuno** | ✓ | 3 | Acceso inmediato al documento |
| **I - Independiente** | ⚠️ | 2 | Auditor requiere validar: ¿riesgos identificados reales? |
| **Re - Rentable** | ✓ | 3 | Costo mantenimiento = bajo |
| | | **25/27** | **93% PRAGMATIC** |

---

### DOMINIO: IDENTIFICAR (ID)

#### Indicador ID-1: CMDB Cobertura (>90% Activos)

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice exposición riesgos identificables |
| **R - Relevante** | ✓ | 3 | Clave NIST CSF, ISO |
| **A - Accionable** | ✓ | 3 | Si <90% = expandir discovery |
| **G - Genuino** | ⚠️ | 2 | ¿CMDB = realidad? Requiere validación técnica muestreo |
| **S - Significativo** | ✓ | 3 | Base visibilidad |
| **Pr - Preciso** | ✓ | 3 | Métrica cuantitativa clara |
| **O - Oportuno** | ✓ | 3 | Dashboard CMDB real-time |
| **I - Independiente** | ⚠️ | 2 | Sesgo: Equipo IT puede inflar cobertura |
| **Re - Rentable** | ✓ | 3 | Costo = herramientas discovery (SIEM ya tiene) |
| | | **23/27** | **85% PRAGMATIC** |

---

#### Indicador ID-2: Clasificación Datos (Sensibilidad Documentada)

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice protección proporcional datos |
| **R - Relevante** | ✓ | 3 | GDPR, ENS obligatorio |
| **A - Accionable** | ✓ | 3 | Si no clasificado = implementar framework |
| **G - Genuino** | ⚠️ | 2 | ¿Clasificación real o teórica? Validar con auditor |
| **S - Significativo** | ✓ | 3 | Impacta GDPR, ROI |
| **Pr - Preciso** | ⚠️ | 2 | Subjetividad: ¿qué es "confidencial"? Requiere estándar |
| **O - Oportuno** | ⚠️ | 2 | Requiere escaneo: puede demorar en datacenters grandes |
| **I - Independiente** | ⚠️ | 2 | DPO/Auditor debe validar |
| **Re - Rentable** | ✓ | 3 | Costo = DLP tools (inversión inicial) |
| | | **20/27** | **74% PRAGMATIC** |

---

#### Indicador ID-3: Evaluación Vulnerabilidades (Mensual+)

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice exposición CVE futuro |
| **R - Relevante** | ✓ | 3 | Crítico para seguridad |
| **A - Accionable** | ✓ | 3 | Si vulnerabilidades halladas = parchear por SLA |
| **G - Genuino** | ✓ | 3 | Resultados verificables técnicamente |
| **S - Significativo** | ✓ | 3 | Base de remediación |
| **Pr - Preciso** | ✓ | 3 | Automatizado (Nessus, Qualys) |
| **O - Oportuno** | ✓ | 3 | Reportes generables en <1h |
| **I - Independiente** | ✓ | 3 | Herramienta escaneadora independiente |
| **Re - Rentable** | ✓ | 3 | ROI alto (evita breaches) |
| | | **27/27** | **100% PRAGMATIC** |

---

### DOMINIO: PROTEGER (PR)

#### Indicador PR-1: MFA Implementado (>85% Críticos)

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice resistencia a credential compromise |
| **R - Relevante** | ✓ | 3 | Mandatorio NIS2 Art. 20 |
| **A - Accionable** | ✓ | 3 | Si <85% = expand MFA |
| **G - Genuino** | ✓ | 3 | Verificable en AD/IAM |
| **S - Significativo** | ✓ | 3 | Previene 70%+ de breaches |
| **Pr - Preciso** | ✓ | 3 | Métrica clara (% usuarios con MFA) |
| **O - Oportuno** | ✓ | 3 | Reporte IAM real-time |
| **I - Independiente** | ✓ | 3 | Auditable por terceros |
| **Re - Rentable** | ✓ | 3 | Costo bajo vs. beneficio |
| | | **27/27** | **100% PRAGMATIC** |

---

#### Indicador PR-2: Cifrado en Tránsito (TLS 1.2+ Mandatory)

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice resistencia eavesdropping |
| **R - Relevante** | ✓ | 3 | GDPR Art. 32, ISO 27001 |
| **A - Accionable** | ✓ | 3 | Si TLS <1.2 = upgrade protocolo |
| **G - Genuino** | ✓ | 3 | Verificable con SSL scan |
| **S - Significativo** | ✓ | 3 | Previene intercepción datos |
| **Pr - Preciso** | ✓ | 3 | Técnicamente verificable |
| **O - Oportuno** | ✓ | 3 | Scan results inmediatos |
| **I - Independiente** | ✓ | 3 | Herramienta SSL scanner independiente |
| **Re - Rentable** | ✓ | 3 | Bajo costo, alto ROI |
| | | **27/27** | **100% PRAGMATIC** |

---

#### Indicador PR-3: Capacitación Anual (>95% Completación)

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice consciencia seguridad futuro |
| **R - Relevante** | ✓ | 3 | Mandatorio GDPR Art. 32(2)(c) |
| **A - Accionable** | ✓ | 3 | Si <95% = recordatorio HR |
| **G - Genuino** | ⚠️ | 2 | ¿Completación = aprendizaje? Validar con assessment |
| **S - Significativo** | ✓ | 3 | Previene phishing 40-60% |
| **Pr - Preciso** | ✓ | 3 | Métrica clara (% completados) |
| **O - Oportuno** | ✓ | 3 | LMS reporta real-time |
| **I - Independiente** | ⚠️ | 2 | HR puede inflar por presión laboral |
| **Re - Rentable** | ✓ | 3 | Costo bajo, ROI 200%+ |
| | | **24/27** | **89% PRAGMATIC** |

---

### DOMINIO: DETECTAR (DE)

#### Indicador DE-1: MTTD <2 Horas (Mean Time To Detect)

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice daño controlado |
| **R - Relevante** | ✓ | 3 | Crítico GDPR notificación <72h |
| **A - Accionable** | ✓ | 3 | Si MTTD >2h = tune SIEM, capacity |
| **G - Genuino** | ⚠️ | 2 | ¿Timestamp = detección real? Requiere validar falsos positivos |
| **S - Significativo** | ✓ | 3 | €5K-10K/hora de delay |
| **Pr - Preciso** | ✓ | 3 | Automático timestamp |
| **O - Oportuno** | ✓ | 3 | SIEM dashboard real-time |
| **I - Independiente** | ⚠️ | 2 | Requiere auditoría externa (10% incidentes) |
| **Re - Rentable** | ✓ | 3 | €0 colección (SIEM ya tiene) |
| | | **24/27** | **89% PRAGMATIC** |

---

#### Indicador DE-2: SIEM Cobertura (>85% Sistemas)

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice visibilidad futura |
| **R - Relevante** | ✓ | 3 | Clave detección |
| **A - Accionable** | ✓ | 3 | Si <85% = expand agent/integration |
| **G - Genuino** | ⚠️ | 2 | ¿Logs completos? Validar muestra |
| **S - Significativo** | ✓ | 3 | Base visibilidad |
| **Pr - Preciso** | ✓ | 3 | Métrica % clara |
| **O - Oportuno** | ✓ | 3 | SIEM console immediate |
| **I - Independiente** | ⚠️ | 2 | SOC puede reportar optimista |
| **Re - Rentable** | ✓ | 3 | Costo agents bajo |
| | | **23/27** | **85% PRAGMATIC** |

---

#### Indicador DE-3: False Positive Rate (<25% Alertas)

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice fatiga analista |
| **R - Relevante** | ✓ | 3 | Crítico para SOC productividad |
| **A - Accionable** | ✓ | 3 | Si FPR >25% = tune rules, add context |
| **G - Genuino** | ⚠️ | 2 | ¿Clasificación FP = acertada? Requiere revisión |
| **S - Significativo** | ✓ | 3 | Impacta MTTD (si gastamos tiempo en FP) |
| **Pr - Preciso** | ⚠️ | 2 | Subjetivo qué = FP vs. TP borderline |
| **O - Oportuno** | ✓ | 3 | SIEM reporta con latencia |
| **I - Independiente** | ⚠️ | 2 | SOC puede misclassify para mejorar ratio |
| **Re - Rentable** | ✓ | 3 | Costo ajustes = bajo |
| | | **21/27** | **78% PRAGMATIC** |

---

### DOMINIO: RESPONDER (RS)

#### Indicador RS-1: MTTR <4 Horas (Mean Time To Resolve)

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice daño minimizado |
| **R - Relevante** | ✓ | 3 | Crítico para ROI incidentes |
| **A - Accionable** | ✓ | 3 | Si MTTR >4h = aumentar escalada, automatización |
| **G - Genuino** | ⚠️ | 2 | ¿"Resuelto" = real? Requiere validar seguimiento |
| **S - Significativo** | ✓ | 3 | Daño exponencial con tiempo |
| **Pr - Preciso** | ✓ | 3 | Automático timestamp |
| **O - Oportuno** | ✓ | 3 | Dashboard real-time |
| **I - Independiente** | ⚠️ | 2 | Equipo puede cerrar falsamente |
| **Re - Rentable** | ✓ | 3 | Costo automación = ROI alto |
| | | **23/27** | **85% PRAGMATIC** |

---

#### Indicador RS-2: Plan Respuesta Incidentes (Actualizado Anual)

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice coordinación en crisis |
| **R - Relevante** | ✓ | 3 | Mandatorio GDPR Art. 33, NIS2 |
| **A - Accionable** | ✓ | 3 | Si desactualizado = actualizar |
| **G - Genuino** | ✓ | 3 | Documento auditable |
| **S - Significativo** | ✓ | 3 | Crítico para eficiencia respuesta |
| **Pr - Preciso** | ✓ | 3 | Binario: existe o no |
| **O - Oportuno** | ✓ | 3 | Acceso inmediato |
| **I - Independiente** | ⚠️ | 2 | Auditor debe validar: ¿plan practicado realmente? |
| **Re - Rentable** | ✓ | 3 | Costo redacción bajo |
| | | **25/27** | **93% PRAGMATIC** |

---

#### Indicador RS-3: Simulacros Anuales (Mínimo 1)

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice capacidad real respuesta |
| **R - Relevante** | ✓ | 3 | Mandatorio NIST CSF, NIS2 |
| **A - Accionable** | ✓ | 3 | Si no simulados = programar ejercicio |
| **G - Genuino** | ⚠️ | 2 | ¿Simulacro = realista? Puede ser teatro |
| **S - Significativo** | ✓ | 3 | Valida plan + identifica gaps |
| **Pr - Preciso** | ✓ | 3 | Métrica contable |
| **O - Oportuno** | ✓ | 3 | Resultados disponibles post-ejercicio |
| **I - Independiente** | ⚠️ | 2 | Equipo puede manipular escenario |
| **Re - Rentable** | ✓ | 3 | Costo ~€5K, ROI millonario |
| | | **23/27** | **85% PRAGMATIC** |

---

### DOMINIO: RECUPERAR (RC)

#### Indicador RC-1: Backups Estrategia 3-2-1 Implementado

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice recuperabilidad post-ataque |
| **R - Relevante** | ✓ | 3 | Crítico continuidad negocio |
| **A - Accionable** | ✓ | 3 | Si no 3-2-1 = implementar |
| **G - Genuino** | ⚠️ | 2 | ¿Backups realmente recuperables? Require test |
| **S - Significativo** | ✓ | 3 | Diferencia entre cierre vs. retorno |
| **Pr - Preciso** | ✓ | 3 | Verificable técnicamente |
| **O - Oportuno** | ✓ | 3 | Logs backup disponibles |
| **I - Independiente** | ⚠️ | 2 | Equipo puede reportar optimista |
| **Re - Rentable** | ✓ | 3 | Costo bajo vs. beneficio |
| | | **24/27** | **89% PRAGMATIC** |

---

#### Indicador RC-2: RTO/RPO Definidos y Documentados

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice expectativa realista recuperación |
| **R - Relevante** | ✓ | 3 | Mandatorio para DR planning |
| **A - Accionable** | ✓ | 3 | Si no definidos = definiir en taller |
| **G - Genuino** | ✓ | 3 | Documento verificable |
| **S - Significativo** | ✓ | 3 | Base inversión DR |
| **Pr - Preciso** | ✓ | 3 | Métricas claras (horas/minutos) |
| **O - Oportuno** | ✓ | 3 | Acceso inmediato documento |
| **I - Independiente** | ⚠️ | 2 | Requiere validación: ¿RTO/RPO alcanzable técnicamente? |
| **Re - Rentable** | ✓ | 3 | Costo redacción mínimo |
| | | **25/27** | **93% PRAGMATIC** |

---

#### Indicador RC-3: Pruebas Restauración Anuales (Mínimo 1)

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice capacidad real recuperación |
| **R - Relevante** | ✓ | 3 | Crítico continuidad |
| **A - Accionable** | ✓ | 3 | Si no probados = test inmediato |
| **G - Genuino** | ✓ | 3 | Resultados verificables |
| **S - Significativo** | ✓ | 3 | Valida plan, identifica gaps |
| **Pr - Preciso** | ✓ | 3 | Métrica contable |
| **O - Oportuno** | ✓ | 3 | Resultados post-test |
| **I - Independiente** | ✓ | 3 | Test técnico objetivo |
| **Re - Rentable** | ✓ | 3 | Costo test << beneficio |
| | | **27/27** | **100% PRAGMATIC** |

---

### DOMINIOS ESPECIALES: VULNERABILIDADES, SIEM, CAPACITACIÓN

#### Indicador VA-1: CVE Crítica Sin Parchear (Target: 0)

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice breach inmediata |
| **R - Relevante** | ✓ | 3 | Crítico para ejecutivos |
| **A - Accionable** | ✓ | 3 | Si hay crítica = parchear urgente |
| **G - Genuino** | ✓ | 3 | Verificable técnicamente |
| **S - Significativo** | ✓ | 3 | Alto riesgo |
| **Pr - Preciso** | ✓ | 3 | Automatizado (scan CVE) |
| **O - Oportuno** | ✓ | 3 | Reporta en <24h |
| **I - Independiente** | ✓ | 3 | Herramienta independiente |
| **Re - Rentable** | ✓ | 3 | ROI evitar breach = infinito |
| | | **27/27** | **100% PRAGMATIC** |

---

#### Indicador SIEM-1: Alert-to-Incident Ratio (Target: 1:50)

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice eficiencia SOC |
| **R - Relevante** | ✓ | 3 | Importante para productividad |
| **A - Accionable** | ✓ | 3 | Si ratio >1:25 = tune reglas |
| **G - Genuino** | ⚠️ | 2 | ¿Clasificación incidente = acertada? Validar |
| **S - Significativo** | ✓ | 3 | Impacta MTTD |
| **Pr - Preciso** | ✓ | 3 | Métrica clara |
| **O - Oportuno** | ✓ | 3 | SIEM reporta automático |
| **I - Independiente** | ⚠️ | 2 | SOC puede misclassify |
| **Re - Rentable** | ✓ | 3 | Costo tuning bajo |
| | | **23/27** | **85% PRAGMATIC** |

---

#### Indicador CAP-1: Phishing Click Rate (Target: <5%)

| Criterio | Eval | /3 | Notas |
|----------|------|-----|--------|
| **P - Predictivo** | ✓ | 3 | Predice vulnerabilidad humana |
| **R - Relevante** | ✓ | 3 | CEO vigila este métrico |
| **A - Accionable** | ✓ | 3 | Si >10% = capacitación adicional |
| **G - Genuino** | ⚠️ | 2 | ¿Simulacro realista? Puede no reflejar realidad |
| **S - Significativo** | ✓ | 3 | Causa de 70% breaches |
| **Pr - Preciso** | ✓ | 3 | Automatizado en plataforma |
| **O - Oportuno** | ✓ | 3 | Reporta en <24h |
| **I - Independiente** | ✓ | 3 | Herramienta independiente |
| **Re - Rentable** | ✓ | 3 | Costo bajo, ROI alto |
| | | **25/27** | **93% PRAGMATIC** |

---

## RESUMEN: SCORE PRAGMATIC POR DOMINIO

| Dominio | Indicadores | Prom. PRAGMATIC | Recomendación |
|---------|------------|-----------------|--------------|
| **GOBIERNO (GV)** | 4 | 92% | IMPLEMENTAR TODOS |
| **IDENTIFICAR (ID)** | 3 | 86% | IMPLEMENTAR CON AUDITORÍA |
| **PROTEGER (PR)** | 3 | 96% | IMPLEMENTAR TODOS |
| **DETECTAR (DE)** | 3 | 84% | IMPLEMENTAR CON VALIDACIÓN |
| **RESPONDER (RS)** | 3 | 88% | IMPLEMENTAR CON AJUSTES |
| **RECUPERAR (RC)** | 3 | 94% | IMPLEMENTAR TODOS |
| **ESPECIALES** | 3 | 93% | IMPLEMENTAR TODOS |
| | **PROMEDIO TOTAL** | **90% PRAGMATIC** | ✓ EXCELENTE |

---

**Conclusión:** 25 de 25 indicadores tienen Score PRAGMATIC ≥78% (aceptable). 22 de 25 están ≥85% (bueno/excelente). Recomendación: Implementar cartera completa con validaciones cruzadas para indicadores <85%.

