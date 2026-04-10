# MAPEO NORMATIVO DETALLADO
## Cada Métrica GQM-DREAD mapeada a Requisitos Normativos Aplicables
### España 2025–2026 · NIS2 · ENS · DORA · GDPR · ISO 27001 · NIST CSF · CRA · IEC 62443 · MAGERIT

---

> *"La regulación sin métricas es declaración de buenas intenciones. Las métricas sin regulación son datos huérfanos. El mapeo normativo es el acto de casamentero que los une... con todas sus consecuencias."*

---

## GUÍA DE LECTURA

La tabla siguiente mapea cada una de las **23 métricas del Kit GQM-DREAD** a los requisitos específicos de los marcos normativos más relevantes para España en 2025-2026:

- **NIS2**: Directiva (UE) 2022/2555 (transpuesta mediante LCGC-2025)
- **ENS**: Esquema Nacional de Seguridad (RD 311/2022)
- **DORA**: Reglamento (UE) 2022/2554 (en vigor desde enero 2025)
- **GDPR**: Reglamento (UE) 2016/679 + LOPDGDD
- **ISO 27001:2022**: Norma internacional de SGSI
- **NIST CSF 2.0**: Marco del NIST para la mejora de la ciberseguridad
- **CRA**: Reglamento de Ciberresiliencia (UE) 2024/2847
- **IEC 62443**: Estándar de seguridad para sistemas de control industrial
- **MAGERIT v3**: Metodología de Análisis y Gestión de Riesgos de las AAPP españolas
- **INCIBE-IMC**: Marco de Indicadores de Ciberresiliencia (INCIBE)

**Columnas de la tabla:**
- **Obligatorio**: La métrica es necesaria para demostrar cumplimiento del requisito normativo
- **Recomendado**: La métrica es la mejor práctica para el cumplimiento, aunque no explícitamente requerida
- **Evidencia**: Qué aporta la métrica como evidencia de auditoría

---

## TABLA MAESTRA DE MAPEO NORMATIVO

### DIMENSIÓN D — DAÑO

| ID Métrica | Nombre | NIS2 | ENS | DORA | GDPR | ISO 27001:2022 | NIST CSF 2.0 | CRA | MAGERIT v3 | INCIBE-IMC | Tipo Req. | Evidencia de auditoría |
|-----------|--------|------|-----|------|------|----------------|-------------|-----|-----------|-----------|----------|----------------------|
| **D.M1** | ALE por amenaza crítica | Art.21.2.a (gestión de riesgos) | Anexo II Med.2 (análisis de riesgos) | Art.6.a (gestión del riesgo TIC) | — | A.6.1.2 (tratamiento del riesgo) | GV.RM (Govern.Risk Mgmt) | Art.13.2 | Fase 3 (evaluación) | IMC-R1 | **Obligatorio** (NIS2/DORA) | Registro de análisis de riesgos con valoración económica, aprobado por el órgano de dirección |
| **D.M2** | IEAC | Art.21.2.f (seguridad de activos) | Org.1 (inventario activos) | Art.8.b (mapeo activos críticos) | — | A.8.1.1 (inventario activos) | ID.AM (Identify.Asset Mgmt) | Art.13.3 | Fase 2 (inventario) | IMC-R2 | **Obligatorio** (NIS2/ENS) | Inventario de activos clasificados por criticidad con porcentaje de exposición documentado |
| **D.M3** | RTO gap | Art.21.2.c (continuidad del negocio) | Op.cont.1 (continuidad) | Art.11.a (continuidad TIC) | — | A.17.1 (planificación continuidad) | RC.RP (Recover.Recovery Plan) | — | Plan de Continuidad | IMC-BC1 | **Obligatorio** (DORA/NIS2) | Resultados de ejercicios BCP/DRP con comparativa RTO objetivo vs. RTO alcanzado; firma del CISO y CO |
| **D.M4** | TBNO | Art.23.1 (notificación de incidentes) | Op.exp.6 (detección incidentes) | Art.19 (notificación) | Art.33-34 GDPR | A.16.1.2 (notificación) | RS.CO (Respond.Comunic.) | — | — | IMC-N1 | **Obligatorio** (GDPR/NIS2) | Registro DPO con timestamps de detección, clasificación y notificación; confirmación de recepción AEPD |
| **D.M5** | TMCD | Art.23.1 (alerta temprana ≤ 24h) | Op.exp.4 (monitorización) | Art.19.4 (alerta temprana) | — | A.16.1.5 (respuesta a incidentes) | RS.AN (Respond.Analysis) | — | — | IMC-D1 | **Obligatorio** (NIS2 Art.23.1) | Log del sistema ITSM con timestamps de clasificación; evidencia de alertas tempranas al CNCS en < 24h |

---

### DIMENSIÓN R — REPRODUCIBILIDAD

| ID Métrica | Nombre | NIS2 | ENS | DORA | GDPR | ISO 27001:2022 | NIST CSF 2.0 | CRA | IEC 62443 | INCIBE-IMC | Tipo Req. | Evidencia de auditoría |
|-----------|--------|------|-----|------|------|----------------|-------------|-----|----------|-----------|----------|----------------------|
| **R.M1** | MTTR por DREAD-R | Art.21.2.e (gestión de vulnerabilidades) | Mp.sw.2 (gestión de parches) | Art.9.2 (gestión de parches TIC) | — | A.12.6.1 (gestión de vulnerabilidades técnicas) | ID.RA (Identify.Risk Assessment) | Art.13.2.c (parcheo oportuno) | SR 2.2 (gestión de actualizaciones) | IMC-V1 | **Obligatorio** (NIS2/CRA) | Registro de vulnerabilidades con fechas de publicación CVE, fechas de remediación y SLAs; informe de excepciones con justificación |
| **R.M2** | TVER (EPSS) | Art.21.2.e (priorización de vulnerabilidades) | Mp.sw.2 (priorización riesgos) | Art.9.2 (priorización) | — | A.12.6.1 (priorización vulnerabilidades) | ID.RA-1 (identificación amenazas) | Art.13.2.c | SR 2.2 | IMC-V2 | **Recomendado** | Dashboard VM con integración EPSS; evidencia de priorización de vulnerabilidades EPSS > 0.5; ratios de remediación por cuartil EPSS |
| **R.M3** | ICEP | Art.21.2.e (monitorización amenazas) | Op.exp.2 (monitorización amenazas externas) | Art.9.2 | — | A.6.1.4 (inteligencia de amenazas) | ID.RA-2 (feeds de inteligencia) | Art.13.2.c | SR 2.2 | IMC-TI1 | **Recomendado** | Registro de amenazas con verificación de exploit público en bases externas (ExploitDB, NVD); correlación con plan de remediación |
| **R.M4** | VEE | Art.21.2.e (ventana de exposición) | Mp.sw.2 | Art.9.2 | — | A.12.6.1 | ID.RA-1 | Art.13.2.c | SR 2.2 | IMC-V3 | **Recomendado** | Análisis de ventana de exposición por activo crítico; evidencia de ASM con timestamps de primera detección externa |

---

### DIMENSIÓN E — EXPLOTABILIDAD

| ID Métrica | Nombre | NIS2 | ENS | DORA | GDPR | ISO 27001:2022 | NIST CSF 2.0 | CRA | IEC 62443 | INCIBE-IMC | Tipo Req. | Evidencia de auditoría |
|-----------|--------|------|-----|------|------|----------------|-------------|-----|----------|-----------|----------|----------------------|
| **E.M1** | SMEC CVSS v4.0 | Art.21.2.e (evaluación riesgos técnicos) | Mp.sw.2 (severidad parches) | Art.9.2 (evaluación riesgo TIC) | — | A.12.6.1 (scoring vulnerabilidades) | ID.RA-1 | Art.13.2.b | SR 2.2 | IMC-V1 | **Recomendado** | Informes VM con CVSS scores de vulnerabilidades activas; distribución por niveles de severidad; tendencia trimestral |
| **E.M2** | TCKEV (CISA KEV) | Art.21.2.e **+ Art.21.3** (medidas apropiadas, KEV como evidencia) | Mp.sw.2 (parches críticos) | Art.9.2 | — | A.12.6.1 | PR.IP-12 (gestión vulnerabilidades) | Art.13.2.c | SR 2.2 | IMC-V2 | **Obligatorio** de facto (NIS2 Art.21.3: "estado del arte") | Cruce diario del inventario de vulnerabilidades activas contra CISA KEV; evidencia de remediación inmediata de coincidencias; registro auditado |
| **E.M3** | DREAD-E LLM | Art.21.2.e (nuevos vectores de amenaza) | — | Art.9.3 (evaluación avanzada de amenazas) | Art.25 (privacy by design en sistemas IA) | A.6.1.4 (inteligencia de amenazas emergentes) | ID.RA-3 (nuevos vectores) | Art.13 (seguridad por diseño en productos digitales) | — | IMC-TI2 | **Recomendado** | Informe de red team LLM/IA con scores DREAD-E para cada vector de ataque identificado; plan de mitigación |
| **E.M4** | TMCE | Art.21.2.b (detección y respuesta a incidentes) | Op.exp.5 (gestión de incidentes) | Art.19.4 (alerta temprana) | — | A.16.1.5 (respuesta a incidentes) | RS.AN-3 (análisis incidentes) | — | SR 6.2 (respuesta a incidentes) | IMC-D2 | **Obligatorio** (NIS2/DORA) | Log SIEM/SOAR con timestamps de detección, alerta y contención; comparativa con SLAs definidos; informe mensual al CISO |
| **E.M5** | ICCAE | Art.21.2.g (autenticación, acceso privilegiado) | Mp.if.7 (segmentación), Mp.si.3 (MFA) | Art.9.3 (controles de acceso TIC) | Art.32.1.a (medidas técnicas) | A.9.1.2 (control de acceso), A.13.1 (segmentación) | PR.AC (Protect.Identity Mgmt) | Art.13.2.d (controles de seguridad) | SR 2.1 (denegación de acceso no autorizado) | IMC-C1 | **Obligatorio** (NIS2/ENS/DORA) | Inventario de activos con estado de implementación de controles (MFA, PAM, micro-segmentación); resultados de auditoría de configuración; cobertura por tier |

---

### DIMENSIÓN A — USUARIOS AFECTADOS

| ID Métrica | Nombre | NIS2 | ENS | DORA | GDPR | ISO 27001:2022 | NIST CSF 2.0 | CRA | MAGERIT v3 | INCIBE-IMC | Tipo Req. | Evidencia de auditoría |
|-----------|--------|------|-----|------|------|----------------|-------------|-----|-----------|-----------|----------|----------------------|
| **A.M1** | UMPA | **Art.23.3** (criterios de "gran magnitud": >50.000 usuarios) | — | Art.19.3 (umbral notificación) | Art.33.1 (umbral notificación significativa) | A.17.1.1 (alcance del BCP) | ID.AM-2 (alcance de impacto) | Art.13.2 (impacto en usuarios) | Fase 3 (valoración de impacto) | IMC-I1 | **Obligatorio** (NIS2 Art.23.3) | Base de datos de usuarios del servicio crítico con cifras actualizadas; mapeado de dependencias de servicio; validación por responsable del servicio |
| **A.M2** | IUVA | — | — | — | **Art.9** (categorías especiales), **Art.32.1** (medidas adicionales) | A.8.2.1 (clasificación datos) | ID.AM-5 (datos sensibles) | — | Fase 2 (clasificación activos) | IMC-I2 | **Obligatorio** (GDPR Art.9) | Mapa de clasificación de datos GDPR Art.9; identificación de sistemas con datos de categoría especial; porcentaje de usuarios en cada categoría |
| **A.M3** | TMNU | **Art.23.2** (notificación a usuarios afectados) | — | Art.19.5 (comunicación a afectados) | **Art.33** (< 72h AEPD), **Art.34** (comunicación a interesados) | A.16.1.6 (aprendizaje de incidentes) | RS.CO-3 (comunicación incidentes) | — | — | IMC-N2 | **Obligatorio** (GDPR Art.33-34) | Registros DPO con timestamps; acuses de recibo de la AEPD; evidencia de comunicación a usuarios afectados; plantillas de notificación aprobadas |
| **A.M4** | CUA | Art.21.2.a (análisis de impacto financiero) | — | **Art.6.a** (impacto financiero cuantificado) | Art.35 (EIPD para procesamiento de alto riesgo) | A.6.1.2 (valoración del impacto) | GV.RM-6 (cuantificación del riesgo) | — | Fase 3 (impacto económico) | IMC-R3 | **Recomendado** | Informe post-incidente con contabilización de costes directos e indirectos; cálculo del coste por usuario afectado; comparativa con benchmarks INCIBE/Ponemon |
| **A.M5** | CCUC | **Art.21.2.c** (continuidad de los servicios esenciales) | Op.cont.1 (BCP) | **Art.11** (continuidad de los servicios TIC) | — | A.17.1.2 (implementación de continuidad) | RC.RP-1 (plan de recuperación) | — | Plan de Continuidad | IMC-BC2 | **Obligatorio** (NIS2/DORA para esenciales) | Inventario de usuarios por servicio con estado de cobertura BCP/DRP; resultados de ejercicios de continuidad; certificación de RTO/RPO por servicio |

---

### DIMENSIÓN Disc — DESCUBRIBILIDAD

| ID Métrica | Nombre | NIS2 | ENS | DORA | GDPR | ISO 27001:2022 | NIST CSF 2.0 | CRA | IEC 62443 | INCIBE-IMC | Tipo Req. | Evidencia de auditoría |
|-----------|--------|------|-----|------|------|----------------|-------------|-----|----------|-----------|----------|----------------------|
| **Disc.M1** | RSAE | Art.21.2.e (gestión de la superficie de ataque) | Mp.com.1 (perímetro de red) | Art.9.4 (monitorización del entorno) | — | A.13.1.1 (controles de red) | ID.AM-3 (inventario red) | Art.13.2.d (superficie de ataque) | SR 5.2 (control de zonas) | IMC-EA1 | **Recomendado** | Informes ASM periódicos con inventario de activos externamente visibles; comparativa con baseline; registro de cambios de exposición |
| **Disc.M2** | RDPR | Art.21.2.h (pruebas de eficacia de controles) | Op.exp.3 (monitorización proactiva) | Art.26 (pruebas de penetración) | — | A.16.1.4 (valoración de incidentes) | DE.CM (Detect.Monitoring) | Art.13.2.c | SR 6.1 (auditoría de seguridad) | IMC-D3 | **Recomendado** | Registro de orígenes de descubrimiento de vulnerabilidades (interno/externo); resultados de red team; evidencia de programa de threat hunting |
| **Disc.M3** | NSIE | Art.21.2.d (hardening de sistemas) | Mp.com.2 (protección de la red), Op.exp.1 (registro de actividad) | Art.9.3 (gestión de la configuración TIC) | — | A.12.6.2 (restricción de software), A.13.1 (seguridad de red) | PR.IP-1 (baseline de configuración) | Art.13.2.d (principio mínimo privilegio) | SR 7.6 (control de puertos y servicios) | IMC-EA2 | **Obligatorio** (ENS/CRA) | Resultados de escaneo de puertos firmados con fecha; registro de justificaciones para puertos abiertos; comparativa vs. baseline de hardening aprobado |
| **Disc.M4** | TMDE | Art.21.2.e (detección temprana de exposición) | Op.exp.4 (monitorización continua) | Art.9.4 (detección temprana) | — | A.12.6.1 (detección de vulnerabilidades nuevas) | DE.CM-8 (escaneo de vulnerabilidades) | Art.13.2.c (monitorización activa) | SR 6.1 | IMC-D4 | **Recomendado** | Registros ASM con timestamps de primera detección externa vs. fecha de publicación CVE; análisis de tendencia de TMDE; plan de mejora |

---

## TABLA RESUMEN: MÉTRICAS POR OBLIGATORIEDAD NORMATIVA

### Métricas de cumplimiento obligatorio (imprescindibles para audit trail regulatorio)

| Métrica | Marco normativo principal | Artículo/Requisito específico |
|---------|--------------------------|------------------------------|
| D.M1 — ALE | NIS2 + DORA | NIS2 Art.21.2.a; DORA Art.6.a |
| D.M2 — IEAC | NIS2 + ENS | NIS2 Art.21.2.f; ENS Org.1 |
| D.M3 — RTO gap | DORA + NIS2 | DORA Art.11; NIS2 Art.21.2.c |
| D.M4 — TBNO | GDPR + NIS2 | GDPR Art.33-34; NIS2 Art.23.1 |
| D.M5 — TMCD | NIS2 | NIS2 Art.23.1 (alerta 24h) |
| R.M1 — MTTR | NIS2 + CRA | NIS2 Art.21.2.e; CRA Art.13.2.c |
| E.M2 — TCKEV | NIS2 Art.21.3 ("estado del arte") | Evidencia de gestión proactiva de KEV |
| E.M4 — TMCE | NIS2 + DORA | NIS2 Art.21.2.b; DORA Art.19.4 |
| E.M5 — ICCAE | NIS2 + ENS + DORA | NIS2 Art.21.2.g; ENS Mp.si.3; DORA Art.9.3 |
| A.M1 — UMPA | NIS2 | NIS2 Art.23.3 (umbral "gran magnitud") |
| A.M2 — IUVA | GDPR | GDPR Art.9 (datos categoría especial) |
| A.M3 — TMNU | GDPR + NIS2 | GDPR Art.33 (72h AEPD); NIS2 Art.23.2 |
| A.M5 — CCUC | NIS2 + DORA | NIS2 Art.21.2.c; DORA Art.11 |
| Disc.M3 — NSIE | ENS + CRA | ENS Mp.com.2; CRA Art.13.2.d |

### Métricas de mejor práctica recomendada

| Métrica | Marco normativo de referencia | Fundamento |
|---------|------------------------------|-----------|
| R.M2 — TVER (EPSS) | NIS2 Art.21.2.e + "estado del arte" | EPSS como metodología avanzada de priorización |
| R.M3 — ICEP | NIS2 Art.21.2.e + NIST CSF | Inteligencia de amenazas con exploits públicos |
| R.M4 — VEE | NIS2 Art.21.2.e + CRA Art.13 | Gestión proactiva de la ventana de exposición |
| E.M1 — SMEC | NIS2 Art.21.2.e + NIST CSF | Scoring de severidad con CVSS v4.0 (actualización "estado del arte") |
| E.M3 — DREAD-E LLM | NIS2 Art.21.2.e + CRA Art.13 (nuevos vectores) | Evaluación de explotabilidad en sistemas IA |
| A.M4 — CUA | DORA Art.6.a + MAGERIT | Cuantificación financiera por usuario afectado |
| Disc.M1 — RSAE | NIS2 Art.21.2.e + CRA Art.13.2.d | ASM como práctica de gestión proactiva de superficie de ataque |
| Disc.M2 — RDPR | NIS2 Art.21.2.h + DORA Art.26 | Ratio de eficacia del programa de detección |
| Disc.M4 — TMDE | NIS2 Art.21.2.e + NIST CSF DE.CM | Monitorización continua de exposición externa |

---

## NOTA SOBRE LA TRANSPOSICIÓN NIS2 EN ESPAÑA (LCGC-2025)

La Ley de Coordinación y Gobernanza de la Ciberseguridad (LCGC), que transpone NIS2 en España, mantiene los requisitos de notificación de incidentes (Art.23 NIS2) y los requisitos de medidas de gestión de riesgos (Art.21 NIS2) con los mismos plazos y umbrales. Las organizaciones esenciales e importantes identificadas por el CNCS deben implementar los 10 grupos de medidas del Art.21.2 NIS2, para los cuales las métricas de este kit proporcionan la evidencia cuantitativa necesaria para demostrar su implementación efectiva.

Para el **sector financiero** (bancos, aseguradoras, gestoras, infraestructuras de mercado), DORA se aplica de forma directa desde enero de 2025 como lex specialis sobre NIS2 en lo relativo a la resiliencia operativa digital. Las métricas D.M3, E.M4, A.M5 y E.M5 son especialmente críticas para la demostración de cumplimiento DORA ante el Banco de España y la CNMV.

---

*Mapeo Normativo · Documento D del Kit GQM+PRAGMATIC DREAD · Abril 2026*
*Fuentes normativas: NIS2 (2022/2555/UE), ENS (RD 311/2022), DORA (2022/2554/UE), GDPR (2016/679)*
*CRA (2024/2847/UE), ISO/IEC 27001:2022, NIST CSF 2.0, IEC 62443-2-1, MAGERIT v3, INCIBE-IMC*
