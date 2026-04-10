# 🗺️ MAPEO NORMATIVO DE PREGUNTAS
## Encuesta MSS — Correspondencia con Requisitos Regulatorios
### Cada Pregunta, Su Marco Legal y Su Consecuencia
#### Versión 1.0 — Abril 2026

---

> *"Las normas sin indicadores son deseos con sello oficial. Los indicadores sin normas son métricas en busca de consecuencias. Esta tabla es el matrimonio de ambos."*

---

## NOTA INTRODUCTORIA

La siguiente tabla mapea cada pregunta de la Encuesta MSS a los requisitos normativos y marcos de buenas prácticas que la justifican. Las columnas indican:

- **Pregunta:** Identificador del bloque y pregunta
- **Texto resumido:** Resumen de lo que evalúa
- **NIS2 / Ley Gobernanza:** Artículos relevantes de la Directiva NIS2 y el Anteproyecto español
- **ENS:** Medidas y categorías del Esquema Nacional de Seguridad (RD 311/2022)
- **DORA:** Artículos relevantes del Reglamento (UE) 2022/2554
- **ISO 27001:2022:** Cláusulas y controles de Annex A relevantes
- **NIST CSF 2.0:** Funciones y subcategorías relevantes
- **ENISA MSS / ECSMAF:** Referencias al análisis de mercado MSS y el framework de análisis
- **Consecuencia regulatoria:** Impacto de incumplimiento o brecha

---

## TABLA DE MAPEO NORMATIVO COMPLETA

| Pregunta | Texto resumido | NIS2 / Ley Gobernanza | ENS (RD 311/2022) | DORA | ISO 27001:2022 | NIST CSF 2.0 | ENISA MSS 2025 / ECSMAF | Consecuencia regulatoria |
|----------|---------------|----------------------|-------------------|------|---------------|-------------|--------------------------|--------------------------|
| **P0.5** | Clasificación como Operador Esencial o Entidad Importante | Art. 3 NIS2; Art. 5-8 Anteproyecto Ley Gobernanza | No aplica directamente | Art. 2 DORA (sector financiero) | — | GV.OC-01 | ECSMAF V3.0 Sección 3.1 | Multas hasta 10M€ o 2% facturación global (Operador Esencial) |
| **P1.1** | Existencia de Estrategia de Ciberseguridad formal | Art. 21.1 NIS2; Art. 15 Anteproyecto | Política de seguridad (org.1, org.2) | Art. 6.1 DORA | Cl. 5.2, 6.1, 6.2 | GV.PO-01, GV.PO-02 | ECSMAF Dimensión Gobernanza | Incumplimiento NIS2 Art. 21 → sanción administrativa |
| **P1.2** | Frecuencia de revisión de la Estrategia | Art. 21.1 c) NIS2: gestión continua del riesgo | Revisión periódica implícita categoría ALTA | Art. 6.5 DORA: revisiones anuales | Cl. 9.3 (revisión por dirección) | GV.PO-02, ID.RA-09 | ENISA MSS Market Analysis: revisión de servicios | Estrategia obsoleta = incumplimiento del deber de diligencia NIS2 |
| **P1.3** | Existencia de función CISO o equivalente | Art. 20 NIS2: responsabilidad directiva en ciberseguridad | Responsable de seguridad obligatorio (org.4) | Art. 5 DORA: órganos de gestión | Cl. 5.3 (roles y responsabilidades) | GV.RR-01, GV.RR-02 | — | Ausencia de función CISO = riesgo de accountability difuso bajo NIS2 |
| **P1.4** | Reporte periódico a Alta Dirección | Art. 20.1 NIS2: gestión activa Alta Dirección | Implícito en revisión por dirección | Art. 5.2 e) DORA: reporte al órgano de dirección | Cl. 9.3 | GV.OV-01, GV.OV-02 | — | Responsabilidad personal de miembros del Consejo bajo NIS2 Art. 20.2 |
| **P1.5** | Formación Alta Dirección en ciberseguridad | **Art. 20.2 NIS2: obligación EXPLÍCITA de formación directiva** | No explícito ENS | Art. 5.4 DORA: conocimientos adecuados del órgano rector | Cl. 7.2 (competencia) | GV.RR-04 | — | Multa directa a miembros individuales de la Alta Dirección (NIS2) |
| **P1.6** | Comité de Seguridad activo | Art. 21 NIS2: gobernanza de riesgos | org.4 (comités y responsabilidades) | Art. 5 DORA | Cl. 6.1.1, Cl. 5.3 | GV.OV-01 | — | Ausencia = déficit de gobernanza en auditorías NIS2 |
| **P1.7** | Presupuesto ciberseguridad (% TI) | Art. 21 NIS2: medidas «proporcionales al riesgo» | Proporcionalidad según categoría ENS | Art. 17.1 DORA: recursos adecuados | Cl. 6.1.3 (tratamiento de riesgo con recursos) | GV.OV-05 | ENISA: presupuesto MSS < 10% como brecha de mercado | Insuficiencia presupuestaria = incumplimiento del principio de proporcionalidad |
| **P2.1** | Modelo de provisión de seguridad | Art. 21.1 d) NIS2: seguridad en cadena de suministro | Externalización con responsabilidad retenida | Art. 28-30 DORA: gestión de riesgos de terceros TIC | Cl. A.5.19 (seguridad en relaciones con proveedores) | GV.SC-01, GV.SC-05 | ENISA MSS Market Analysis: taxonomía de servicios | Responsabilidad no delegable al proveedor MSS bajo NIS2 |
| **P2.2** | Número de proveedores MSS | Art. 21.1 d) NIS2 | — | Art. 28.2 DORA: identificación de dependencias | Cl. A.5.19, A.5.20 | GV.SC-06 | ENISA: concentración de mercado, riesgo de dependencia | Fragmentación excesiva = riesgo de coordinación en IR |
| **P2.3** | Domicilio y control del proveedor MSS | Art. 21.1 NIS2; soberanía digital | — | Art. 28 DORA: evaluación de riesgos de proveedor | Cl. A.5.19 | GV.SC-07 | **ENISA 2025: 51% MSSPs bajo control no-UE** | Riesgo geopolítico; potencial conflicto con GDPR (transferencias internacionales) |
| **P2.4** | Servicios MSS contratados | Art. 21.2 NIS2: catálogo de medidas mínimas | Medidas técnicas ENS según categoría | Art. 9 DORA: funciones críticas externalizadas | Cl. A.5.20, A.5.21 | PR.AA, DE.CM | ENISA MSS: taxonomía de servicios (técnicos, consultoría, formación) | Ausencia de servicios mínimos = incumplimiento NIS2 Art. 21.2 |
| **P2.5** | Existencia de SLA formal | Art. 21 NIS2; Art. 28.9 d) DORA (SLAs documentados) | Contratos con proveedores críticos | **Art. 30 DORA: cláusulas contractuales obligatorias** | Cl. A.5.20 | GV.SC-10 | ENISA: brecha demanda/oferta en personalización de SLA | Ausencia de SLA = incumplimiento DORA Art. 30 para sector financiero |
| **P2.6** | Métricas en SLA | Art. 21 NIS2; Art. 30.2 g) DORA (indicadores de rendimiento) | — | **Art. 30.2 g) DORA: métricas de rendimiento obligatorias** | Cl. A.5.20 | GV.SC-10 | ENISA: 24% demanda logra personalización vs. 0% oferta | DORA requiere explícitamente indicadores de rendimiento en contratos TIC críticos |
| **P2.7** | Valoración de personalización de métricas MSS | — | — | Art. 30 DORA | Cl. A.5.20 | — | ENISA MSS: brecha estructural de personalización | Indicador de calidad del contrato MSS |
| **P3.1** | Monitorización del MTTD | Art. 23 NIS2: notificación en plazos (requiere detección) | op.mon.1 (monitorización del sistema) | Art. 11.6 DORA: métricas de resiliencia | Cl. A.8.16 (monitorización de actividades) | DE.CM-01, DE.AE-01 | ENISA MSS: MTTD como métrica esencial | Sin MTTD medido = imposible cumplir plazos notificación NIS2 de 24h |
| **P3.2** | Valor real del MTTD | Art. 23.1 NIS2: alerta temprana 24h | op.mon.1, op.exp.1 | Art. 11 DORA | Cl. A.8.16 | DE.CM-09 | ENISA: MTTD como KPI primario MSS | MTTD > 24h pone en riesgo el cumplimiento de la ventana de notificación NIS2 |
| **P3.3** | Monitorización del MTTR | Art. 21.2 c) NIS2: recuperación post-incidente | op.exp.3 (gestión de incidentes) | Art. 11.6 DORA | Cl. A.5.26 (respuesta a incidentes) | RS.MA-01, RC.RP-01 | ENISA MSS: MTTR como KPI de respuesta | — |
| **P3.4** | Valor real del MTTR | Art. 21 NIS2: medidas proporcionales | op.exp.3 | Art. 11 DORA: resiliencia operativa | Cl. A.5.26 | RS.MA-04, RC.RP-02 | ENISA MSS: indicadores temporales core | MTTR > 72h implica incapacidad de recuperación en el plazo de notificación NIS2 |
| **P3.5** | Tasa de falsos positivos | — | op.mon.1: eficacia de monitorización | — | Cl. A.8.16 | DE.AE-04 | ENISA MSS: calidad de detección | Alta FPR = fatiga de analistas = incidentes reales no detectados |
| **P3.6** | Asset Coverage Ratio (ACR) | Art. 21.2 a) NIS2: políticas de seguridad sobre activos | op.inv.1 (inventario de activos) | Art. 8 DORA: gestión de activos TIC | Cl. A.5.9 (inventario de activos) | ID.AM-01, ID.AM-02 | ECSMAF: cobertura como dimensión de madurez | ACR < 80% = superficie sin monitorizar; riesgo de incidentes no detectados |
| **P3.7** | Gestión continua de vulnerabilidades | Art. 21.2 b) NIS2: gestión de vulnerabilidades | op.exp.2 (gestión de vulnerabilidades) | Art. 9.4 DORA: pruebas de vulnerabilidades | Cl. A.8.8 (gestión de vulnerabilidades técnicas) | ID.RA-01, PR.PS-02 | — | NIS2 Art. 21.2 b) exige explícitamente gestión de vulnerabilidades |
| **P3.8** | Tiempo de remediación de CVEs críticas | Art. 21.2 b) NIS2 | op.exp.2 | Art. 9.4 DORA | Cl. A.8.8 | ID.RA-05, PR.PS-02 | — | CVE crítica sin parchear > 30 días = riesgo de explotación activa (CISA KEV) |
| **P3.9** | Threat Hunting proactivo | Art. 21.2 a) NIS2: detección de amenazas | op.mon.3 (detección de intrusiones) | Art. 11 DORA | Cl. A.5.25 (evaluación de eventos) | DE.AE-07 | ENISA MSS: Threat Hunting como servicio premium | — |
| **P3.10** | Capacidad de respuesta 24×7 | Art. 21.2 c) NIS2; Art. 23 (notificación sin demora) | op.exp.3 | Art. 11.1 DORA: continuidad del proceso | Cl. A.5.26 (respuesta a incidentes de seguridad) | RS.MA-01 | ENISA MSS: disponibilidad como KPI de SLA | Sin 24×7 = imposible cumplir ventana de alerta NIS2 de 24h en incidentes nocturnos |
| **P4.1** | Estado conformidad ENS | — | **ENS RD 311/2022: certificación obligatoria para AAPP** | — | — | — | — | Incumplimiento ENS = suspensión de contratos con AAPP |
| **P4.2** | Preparación NIS2 | **Art. 21 NIS2; Ley Gobernanza Ciberseguridad** | — | — | — | GV.PO-02 | ECSMAF: análisis brechas NIS2 | Multas hasta 10M€ o 2% / 7M€ o 1.4% según clasificación |
| **P4.3** | Plazos de notificación NIS2 | **Art. 23 NIS2: 24h/72h/1 mes** | op.exp.7 (notificación de incidentes) | Art. 19 DORA: notificación 4h/24h/1 mes | Cl. A.5.24 (planificación de respuesta a incidentes) | RS.CO-02, RS.CO-03 | — | Incumplimiento plazos = multa directa + notificación regulatoria obligatoria |
| **P4.4** | Certificación ISO/IEC 27001 | Art. 24 NIS2: uso de certificaciones europeas | ENS reconoce ISO 27001 como equivalente parcial | Art. 26.1 DORA: marcos de referencia reconocidos | **ISO/IEC 27001:2022: todas las cláusulas** | Todos los dominios | ENISA MSS: ISO 27004 adoptado por 92% proveedores | Certificación facilita demostración de cumplimiento NIS2 Art. 21 |
| **P4.5** | Conformidad DORA | — | — | **DORA Reglamento (UE) 2022/2554: en vigor enero 2025** | — | — | — | Multas supervisoras del sector financiero (BCE, BdE) |
| **P4.6** | Evaluaciones formales de riesgo | Art. 21.1 a) NIS2: política de análisis y gestión de riesgo | mp.inf.1, op.pl.1 (análisis de riesgos) | Art. 6.1 DORA: marco de gestión de riesgos TIC | Cl. 6.1.2 (evaluación de riesgos) | ID.RA-01 al ID.RA-09 | — | Ausencia de evaluación formal = incumplimiento base NIS2 Art. 21.1 |
| **P4.7** | Gestión riesgo de proveedores (TPRM) | Art. 21.1 d) NIS2; Art. 21.3 NIS2 (cadena de suministro) | Acuerdos con terceros: op.ext.1 | **Art. 28-30 DORA: marco completo TPRM** | Cl. A.5.19 al A.5.22 | GV.SC-01 al GV.SC-10 | ENISA MSS: riesgo de cadena de suministro MSS | NIS2 exige evaluaciones de seguridad de proveedores críticos; DORA los codifica en detalle |
| **P5.1** | Plan de Continuidad de Negocio (BCP) | Art. 21.2 c) NIS2: continuidad del negocio | op.cont.1, op.cont.2 (continuidad) | Art. 11 DORA: continuidad operativa y planes de recuperación | Cl. A.5.29, A.5.30 | RC.RP-01, RC.RP-03 | — | Ausencia de BCP con escenarios ciber = incumplimiento NIS2 Art. 21.2 c) |
| **P5.2** | Frecuencia de simulacros ciber | Art. 21.2 c) NIS2: pruebas y ejercicios | op.cont.3 (pruebas y ensayos) | Art. 26 DORA: pruebas de resiliencia operativa digital | Cl. A.5.29 (preparación para interrupciones) | RC.IM-01, ID.IM-01 | ENISA MSS: simulacros como servicio de formación MSS | DORA Art. 26: pruebas TLPT obligatorias para entidades financieras significativas |
| **P5.3** | RTO/RPO definidos | Art. 21.2 c) NIS2 | op.cont.1 (objetivos de recuperación) | Art. 11.3 DORA: objetivos de recuperación | Cl. A.5.29, A.5.30 | RC.RP-03 | — | RTO/RPO no probados = incumplimiento del principio de efectividad |
| **P5.4** | Copias de seguridad verificadas | Art. 21.2 c) NIS2 | mp.com.9 (copias de seguridad) | Art. 9.4 DORA: copias de seguridad y restauración | Cl. A.8.13 (copia de seguridad de la información) | PR.DS-11 | — | Backup en misma red que producción = vector de ransomware documentado |
| **P5.5** | Experiencia con ransomware | Contexto de incidente real | — | — | — | — | ENISA TL 2025: ransomware impacto más alto | Dato contextual para calibración de madurez real |
| **P6.1** | SIEM operativo | Art. 21.2 a) NIS2 | op.mon.1 | Art. 11 DORA: detección precoz | Cl. A.8.16 | DE.CM-01, DE.CM-09 | ENISA MSS: SIEM/MDR como servicio central MSS | Sin SIEM = imposible cumplir requisitos de monitorización NIS2 |
| **P6.2** | Arquitectura Zero Trust | Art. 21 NIS2: medidas proporcionales avanzadas | op.acc.1 y siguientes (control de acceso) | Art. 9 DORA: seguridad de red y protocolos | Cl. A.8.2, A.8.3 (gestión de accesos) | PR.AA-01 al PR.AA-05 | ENISA MSS: Zero Trust como tendencia emergente | Zero Trust reduce superficie de ataque de movimiento lateral |
| **P6.3** | Autenticación multifactor (MFA) | Art. 21.2 j) NIS2: autenticación multifactor **explícita** | op.acc.5 (autenticación) | Art. 9.4 b) DORA: autenticación fuerte | Cl. A.8.5 (autenticación segura) | PR.AA-03 | — | **NIS2 Art. 21.2 j) menciona explícitamente MFA como medida obligatoria** |
| **P6.4** | XDR/EDR avanzado | Art. 21 NIS2 | op.exp.5 (herramientas de seguridad) | Art. 9.4 DORA | Cl. A.8.16, A.8.22 | DE.CM-01, PR.PS-01 | ENISA MSS: MDR/XDR como servicio MSS esencial | — |
| **P6.5** | Inventario de activos | Art. 21.2 a) NIS2 | **op.pl.1 (inventario de activos): OBLIGATORIO** | Art. 8.1 DORA: registro de activos TIC | Cl. A.5.9 (inventario de activos) | **ID.AM-01, ID.AM-02** | ECSMAF: inventario como prerequisito de análisis de madurez | Inventario incompleto = shadow IT = superficie de ataque no gestionada |
| **P6.6** | Entornos OT/ICS | Art. 21 NIS2: sectores OT incluidos | mp.if.7 (perímetro de seguridad física) | Art. 9 DORA (si aplica sector) | Cl. A.8.1 al A.8.25 | PR.IR-01 (segmentación de red) | ENISA MSS: OT como brecha de mercado identificada | Convergencia IT/OT sin segmentación = riesgo crítico para infraestructuras esenciales |
| **P7.1** | Programa de formación y concienciación | Art. 20.2 NIS2; Art. 21.2 i) NIS2: higiene cibernética | mp.per.3 (concienciación) | Art. 13.6 DORA: programas de formación | Cl. A.6.3 (concienciación, educación y formación) | PR.AT-01, PR.AT-02 | ENISA MSS: formación como familia de servicios MSS | NIS2 Art. 21.2 i) exige higiene cibernética y formación |
| **P7.2** | Simulacros de phishing | Art. 21.2 i) NIS2 | mp.per.4 (formación) | Art. 13.6 DORA | Cl. A.6.3 | PR.AT-01 | ENISA MSS: simulaciones como servicio formativo MSS | — |
| **P7.3** | Tasa de clics en phishing | Indicador de eficacia de formación NIS2 | — | — | Cl. A.6.3 | PR.AT-01 | — | > 20% tasa clics = brecha de concienciación significativa |
| **P7.4** | Brecha de talento en ciberseguridad | Art. 21 NIS2: recursos adecuados | — | Art. 5.4 DORA: conocimientos adecuados | Cl. 7.2 | GV.RR-01 | ENISA: crisis de talento como driver MSS | Brecha de talento justifica y exige adopción de MSS externos |
| **P7.5** | Programa de amenaza interna | Art. 21 NIS2: seguridad de RRHH | mp.per.1 (gestión del personal) | Art. 5.9 DORA | Cl. A.6.1, A.6.2 (condiciones de empleo) | DE.AE-06 | — | Insider Threat no gestionado = vector frecuente en incidentes de alto impacto |
| **P8.1** | Consumo de Threat Intelligence | Art. 21.2 f) NIS2: evaluación de eficacia de medidas | op.mon.5 (detección de intrusiones avanzada) | Art. 11.5 DORA | Cl. A.5.7 (inteligencia sobre amenazas) | DE.AE-02, ID.RA-02 | ENISA MSS: CTI como servicio MSS | Cl. A.5.7 ISO 27001:2022 introduce explícitamente inteligencia de amenazas |
| **P8.2** | Participación en plataformas de intercambio | Art. 29 NIS2: acuerdos de intercambio de información | — | Art. 45 DORA: intercambio de información | Cl. A.5.7 | ID.RA-06 | ENISA: plataformas compartición como buena práctica | NIS2 Art. 29 crea base legal para compartición voluntaria de información sobre amenazas |
| **P8.3** | Vigilancia Dark Web | Art. 21 NIS2: detección proactiva | op.mon.4 | — | Cl. A.5.7, A.8.16 | DE.AE-02 | ENISA MSS: vigilancia digital como servicio CTI | — |
| **P9.1** | Cuantificación impacto económico (CRQ) | Art. 21.1 a) NIS2: gestión del riesgo con base económica | — | Art. 6.5 DORA: escenarios de riesgo | Cl. 6.1.2 (valoración de riesgos) | ID.RA-08 | CAS Research Paper 2025: CRQ metodología actuarial | ROSI no medido = argumento presupuestario débil ante la Alta Dirección |
| **P9.2** | Seguro de ciberriesgos | Art. 21 NIS2 (transferencia del riesgo) | — | — | Cl. 6.1.3 (tratamiento del riesgo: transferencia) | ID.RA-09 | Aon España 2025: mercado ciberseguro +12% | Ciberseguro inadecuado = exposición financiera residual sin cobertura |
| **P9.3** | Variación de prima de ciberseguro | Indicador de madurez del mercado | — | — | — | — | Aon España 2025: -7% primas Q1 2025 para mejores controles | Aumento de prima = señal del mercado de deterioro del perfil de riesgo |
| **P9.4** | Medición del ROSI | Art. 21 NIS2: proporcionalidad | — | Art. 17 DORA: coste-beneficio de medidas | Cl. 6.1 | GV.OV-05 | — | ROSI negativo o no medido = incapacidad de justificar inversión en seguridad |
| **P10.1** | Evaluación de riesgo cuántico | Art. 21 NIS2: gestión de riesgos emergentes | — | Art. 9 DORA: tecnologías emergentes | Cl. 6.1.2 | ID.RA-01, ID.RA-09 | ENISA: PQC como driver de crecimiento MSS | «Harvest Now, Decrypt Later»: daño futuro por datos robados hoy |
| **P10.2** | Plan de transición PQC | Art. 21 NIS2 | — | Art. 9 DORA | Cl. 6.1.3 (tratamiento de riesgo) | PR.PS-01 | ENISA MSS: criptografía postcuántica como driver | NIST PQC standards publicados agosto 2024: ventana de migración abierta |
| **P10.3** | Gestión «Harvest Now, Decrypt Later» | Art. 21 NIS2: protección de confidencialidad a largo plazo | mp.com.2 (cifrado) | Art. 9 DORA | Cl. A.8.24 (uso de la criptografía) | PR.DS-01, PR.DS-10 | ENISA: riesgo cuántico como tendencia emergente | Sectores con datos larga vida (banca, defensa, salud): riesgo de retroacción |
| **P10.4** | IA en detección y respuesta | Art. 21 NIS2: eficacia de medidas | op.mon.1: herramientas avanzadas | Art. 11 DORA: herramientas de detección | Cl. A.8.16 | DE.CM-09 | ENISA MSS: IA como diferenciador de eficacia MSS | Microsoft: -40% MTTR con IA; +60% reducción falsos positivos |
| **P10.5** | Riesgos de IA generativa por empleados | Art. 21 NIS2: gestión de riesgos emergentes | mp.per.3 (concienciación de riesgos) | Art. 13 DORA | Cl. A.6.3, A.8.16 | ID.RA-01, PR.AT-01 | ENISA TL 2025: IA como vector de amenaza | Fraude IA +1.210% en 2025; deepfakes +880% (CyberSecStats 2026) |
| **P11.1** | Localización y jurisdicción de datos en la nube | Art. 21 NIS2; RGPD Art. 46-49 (transferencias internacionales) | mp.com.1 (protección de la información) | Art. 28.8 DORA: localización del proveedor TIC crítico | Cl. A.5.33 (protección de registros) | PR.DS-01, PR.DS-10 | ENISA: soberanía digital como dimensión de riesgo MSS | RGPD: transferencias a países sin decisión de adecuación requieren garantías adicionales |
| **P11.2** | Estrategia de salida de proveedores MSS/cloud | Art. 21.1 d) NIS2: gestión de dependencias | — | **Art. 28.2 f) y Art. 30.2 h) DORA: estrategias de salida OBLIGATORIAS** | Cl. A.5.20 | GV.SC-09 | ENISA MSS: lock-in de proveedor como riesgo sistémico | DORA exige contractualmente estrategias de salida para proveedores TIC críticos |
| **P12.1** | Nivel de madurez global autoevaluado | Marco de referencia general | ENS: niveles de madurez implícitos | DORA: niveles de madurez | — | Todos los dominios CSF | CMM-SOC (niveles 1-5) | Indicador de autoconciencia organizacional |
| **P12.2** | Principales obstáculos de mejora | — | — | — | — | — | ECSMAF V3.0: análisis de barreras del mercado | Identificación de barreras sistémicas para políticas públicas |
| **P12.3** | Iniciativa prioritaria próximos 12 meses | — | — | — | — | — | ECSMAF V3.0: prioridades de inversión | Orientación de la hoja de ruta de mejora |
| **P12.4** | Observaciones abiertas | — | — | — | — | — | — | Enriquecimiento cualitativo del diagnóstico |

---

## RESUMEN DE ARTÍCULOS NIS2 DE MAYOR IMPACTO EN LA ENCUESTA

| Artículo NIS2 | Contenido | Preguntas que evalúan su cumplimiento |
|---------------|-----------|---------------------------------------|
| Art. 20 | Gobernanza: responsabilidad directiva y formación | P1.3, P1.4, P1.5 |
| Art. 21.1 | Marco de gestión de riesgos | P1.1, P1.2, P4.6 |
| Art. 21.2 a) | Políticas de análisis de riesgo, seguridad de activos | P3.6, P6.5 |
| Art. 21.2 b) | Gestión de incidentes | P3.1–P3.4, P3.7, P3.8 |
| Art. 21.2 c) | Continuidad del negocio y recuperación | P5.1–P5.4 |
| Art. 21.2 d) | Seguridad de la cadena de suministro | P2.3, P4.7 |
| Art. 21.2 f) | Eficacia de medidas de gestión de riesgos | P8.1 |
| Art. 21.2 i) | Higiene cibernética y formación | P7.1, P7.2 |
| Art. 21.2 j) | **MFA y comunicaciones seguras** | P6.3 |
| Art. 23 | **Notificación de incidentes: 24h/72h/1 mes** | P3.10, P4.3 |
| Art. 24 | Certificaciones y estándares | P4.4 |
| Art. 29 | Intercambio de información sobre amenazas | P8.2 |

---

*Mapeo Normativo — Versión 1.0 · Abril 2026*
*Fuentes normativas: Directiva (UE) 2022/2555 (NIS2), Reglamento (UE) 2022/2554 (DORA), Reglamento (UE) 2025/37, RD 311/2022 (ENS), ISO/IEC 27001:2022, NIST CSF 2.0, ENISA MSS Market Analysis junio 2025, ENISA ECSMAF V3.0 marzo 2026*
