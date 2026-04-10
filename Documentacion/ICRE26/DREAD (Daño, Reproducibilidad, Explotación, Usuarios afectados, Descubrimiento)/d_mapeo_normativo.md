# MAPEO NORMATIVO DETALLADO
## Correspondencia entre Preguntas de la Encuesta DREAD y Requisitos Normativos
### Kit de Encuesta DREAD · Edición 2025–2026

---

> *"La regulación sin métricas es teatro. Las métricas sin regulación son experimentos. Esta tabla es el punto donde ambas se dan la mano."*

---

## LEYENDA DE MARCOS NORMATIVOS

| Código | Marco normativo / Estándar |
|--------|---------------------------|
| **NIS2** | Directiva (UE) 2022/2555 + Anteproyecto LCGC España (enero 2025) |
| **ENS** | Real Decreto 311/2022 — Esquema Nacional de Seguridad |
| **DORA** | Reglamento (UE) 2022/2554 — Digital Operational Resilience Act |
| **GDPR** | Reglamento (UE) 2016/679 + LOPDGDD (LO 3/2018) |
| **NIS2-ES** | Anteproyecto Ley de Coordinación y Gobernanza de la Ciberseguridad (España, enero 2025) |
| **MAGERIT** | Metodología de Análisis y Gestión de Riesgos de los SSII (CCN-CERT) |
| **INCIBE-IMC** | Indicadores de Madurez en Ciberseguridad — Metodología GQM (INCIBE) |
| **ENISA-ETL** | ENISA Threat Landscape Methodology (agosto 2025) |
| **ISO27001** | ISO/IEC 27001:2022 — Sistemas de Gestión de Seguridad de la Información |
| **NIST-CSF** | NIST Cybersecurity Framework v2.0 (2024) |
| **IEC62443** | IEC 62443 — Ciberseguridad industrial (OT/ICS) |
| **CRA** | Cyber Resilience Act (UE, 2024) |

---

## TABLA MAESTRA DE MAPEO NORMATIVO

| Pregunta | Dimensión DREAD | ENS | NIS2 / NIS2-ES | DORA | GDPR | ISO27001 | NIST-CSF | MAGERIT | INCIBE-IMC | IEC62443 | CRA | Observaciones |
|----------|----------------|-----|----------------|------|------|----------|----------|---------|------------|---------|-----|---------------|
| **P0.5** — Identificación como operador esencial/importante | — | ✓ Art.28 | ✓ Art.3 + NIS2-ES Arts.4-7 | — | — | — | — | — | ✓ | — | — | NIS2 Art.3 define entidades esenciales e importantes; NIS2-ES amplía con sectores adicionales para España |
| **P1.2** — Frameworks de evaluación utilizados | Todos | ✓ Annex I | ✓ Art.21.2 | ✓ Arts.5-8 | — | ✓ A.6.1.2 | ✓ GV.RM | ✓ Fase III | ✓ GQM | — | — | NIS2 Art.21.2 exige gestión de riesgos con metodología formal |
| **P2.1** — Evaluación del Daño potencial | D — Daño | ✓ Cat. ALTA/MEDIA/BÁSICA | ✓ Art.21.2.a | ✓ Art.6.1 | ✓ Art.33 | ✓ A.8.8 | ✓ ID.RA | ✓ Criterio C/I/D | ✓ KRI-01 | — | — | ENS clasifica sistemas en categorías de seguridad por impacto en C/I/D |
| **P2.2** — Sub-indicadores de Daño considerados | D — Daño | ✓ Cat. ALTA | ✓ Art.21.2.b | ✓ Art.6.2-3 | ✓ Arts.33-34 | ✓ A.5.30, A.8.8 | ✓ ID.RA-01 | ✓ Valoración activos | ✓ KRI-01, KRI-02 | — | — | Impacto en vidas humanas → IEC62443 para entornos OT |
| **P2.3** — Daño en últimos incidentes | D — Daño | ✓ | ✓ Art.23 | ✓ Art.19 | ✓ Art.33.3 | ✓ A.5.24 | ✓ RS.AN | ✓ | ✓ KPI-03 | — | — | NIS2 Art.23: notificación de incidentes significativos en < 24h / 72h |
| **P2.4** — Vinculación Daño con notificación regulatoria | D — Daño | ✓ Art.40 | ✓ Arts.23-24 | ✓ Arts.19-20 | ✓ Arts.33-34 | ✓ A.5.26 | ✓ RS.CO | — | ✓ KPI-04 | — | — | DORA Arts.19-20: clasificación de incidentes y notificación al regulador financiero |
| **P2.5** — Cuantificación financiera del daño | D — Daño | — | ✓ Art.21.2 | ✓ Arts.6-8 | — | ✓ A.6.1.2 | ✓ GV.RM-06 | ✓ | ✓ KRI-03 | — | — | DORA exige cuantificación del impacto financiero para entidades financieras |
| **P3.1** — Evaluación de Reproducibilidad | R — Reproducibilidad | ✓ | ✓ Art.21.2.e | — | — | ✓ A.8.8 | ✓ ID.RA-01 | ✓ Amenaza P.A | ✓ KRI-05 | — | — | ENS exige análisis de amenazas con probabilidad de ocurrencia |
| **P3.2** — Seguimiento de exploits públicos | R — Reproducibilidad | ✓ | ✓ Art.21.2.e | — | — | ✓ A.8.8 | ✓ ID.RA-01 | ✓ | ✓ KPI-07 | — | ✓ Art.13 | CRA Art.13: obligación de monitorizar vulnerabilidades en productos con elementos digitales |
| **P3.3** — Uso del EPSS | R + E | — | ✓ Art.21 | — | — | — | ✓ ID.RA | — | ✓ | — | — | EPSS proporciona probabilidad objetiva que alimenta R y E de DREAD |
| **P3.4** — MTTR de vulnerabilidades críticas | R — Reproducibilidad | ✓ Medida 5 | ✓ Art.21.2.e | ✓ Art.5.2 | — | ✓ A.12.6.1 | ✓ RC.RP | ✓ | ✓ KPI-08 | ✓ | ✓ Art.13 | DORA Art.5.2 exige gestión del riesgo TIC con plazos de remediación definidos |
| **P3.5** — Reproducibilidad en OT/ICS/IoT | R — Reproducibilidad | — | ✓ Anexo I sectores | — | — | — | ✓ | — | — | ✓ Full | ✓ | IEC 62443-3-3: evaluación de amenazas en sistemas de control industrial |
| **P4.1** — Evaluación de la Explotabilidad | E — Explotabilidad | ✓ | ✓ Art.21.2 | ✓ Art.6 | — | ✓ A.8.8 | ✓ ID.RA | ✓ P.A (probabilidad) | ✓ KRI-06 | — | — | ENS: análisis de amenazas incluye probabilidad de explotación |
| **P4.2** — Impacto de IA generativa en Explotabilidad | E — Explotabilidad | — | ✓ Art.21.2 | — | — | ✓ A.8.28 | ✓ ID.RA-05 | — | ✓ | — | — | ENISA ETL 2025 reporta +75% en ataques automatizados con IA; NIS2 exige actualizar análisis de amenazas |
| **P4.3** — Explotabilidad en ataques sobre IA/LLMs | E — Explotabilidad | — | ✓ Art.21 | — | ✓ Art.25 (privacy by design) | ✓ A.8.28 | ✓ ID.RA-05 | — | — | — | — | GDPR Art.25: privacy by design aplica a sistemas de IA que procesan datos personales |
| **P4.4** — Perfiles de atacante | E — Explotabilidad | ✓ | ✓ Art.21.2 | — | — | ✓ A.6.1.2 | ✓ ID.RA-03 | ✓ Agentes de amenaza | ✓ | — | — | MAGERIT: identificación de agentes de amenaza como parte del análisis |
| **P4.5** — Controles para reducir Explotabilidad | E — Explotabilidad | ✓ Measures ENS | ✓ Art.21.2 | ✓ Art.9 | — | ✓ Annex A | ✓ PR.AA, PR.AC | ✓ Salvaguardas | ✓ KPI-10 | ✓ | ✓ | ENS Anexo II: medidas de seguridad clasificadas por dimensión |
| **P5.1** — Cuantificación de usuarios afectados | A — Usuarios Afectados | ✓ Categorización | ✓ Art.23.3 (incidentes significativos) | ✓ Art.19.3 | ✓ Art.33 (personas afectadas) | ✓ A.5.30 | ✓ ID.RA | ✓ Activos: Usuarios | ✓ KRI-07 | — | — | NIS2 Art.23.3: "gran magnitud" → afecta a muchos usuarios o sectores esenciales |
| **P5.2** — Umbrales de usuarios para protocolos | A — Usuarios Afectados | ✓ | ✓ Arts.23-24 | ✓ Arts.19-20 | ✓ Arts.33-34 | ✓ A.5.24 | ✓ RS.CO | — | ✓ KPI-05 | — | — | GDPR: notificación a AEPD si > 0 personas físicas afectadas con alto riesgo; NIS2: umbrales propios |
| **P5.3** — Grupos con protección diferenciada | A — Usuarios Afectados | — | — | — | ✓ Arts.9-10 (datos especiales) | ✓ A.5.34 | — | — | — | — | — | GDPR Arts.9-10: categorías especiales de datos y personas vulnerables requieren protección reforzada |
| **P5.4** — Escala territorial / sectorial | A — Usuarios Afectados | — | ✓ Art.23 (impacto transfronterizo) | ✓ Art.19 | — | — | ✓ GV.SC | — | ✓ | — | — | NIS2 Art.23: notificación ENISA si impacto transfronterizo; NIS2-ES: CNCS coordina respuesta nacional |
| **P5.5** — Inventario de activos y mapa de afectación | A — Usuarios Afectados | ✓ Medida 2 (inventario) | ✓ Art.21.2.f | ✓ Art.8 | — | ✓ A.8.1 | ✓ ID.AM | ✓ Inventario activos | ✓ KPI-01 | ✓ | ✓ | ENS Medida 2: gestión de activos; NIS2 Art.21.2.f: gestión de activos TIC |
| **P6.1** — Enfoque sobre Descubribilidad | D — Descubribilidad | ✓ | ✓ Art.21.2.e | — | — | ✓ A.8.8 | ✓ ID.RA | ✓ Vulnerabilidades | ✓ KRI-08 | — | — | ENS prohíbe implícitamente la seguridad por oscuridad como medida única de protección |
| **P6.2** — Vigilancia digital activa | D — Descubribilidad | ✓ | ✓ Art.21.2.h | — | — | ✓ A.8.16 | ✓ DE.CM | — | ✓ KPI-09 | — | — | NIS2 Art.21.2.h: monitorización y análisis de amenazas; NIST-CSF: Detect.Continuous Monitoring |
| **P6.3** — Red team y pentest | D — Descubribilidad | ✓ | ✓ Art.21.2 | ✓ Art.26 (TLPT) | — | ✓ A.8.8 | ✓ ID.RA-05 | ✓ | ✓ | — | — | DORA Art.26: Threat-Led Penetration Testing (TLPT) obligatorio para entidades financieras significativas |
| **P6.4** — Attack Surface Management | D — Descubribilidad | ✓ | ✓ Art.21.2.e | ✓ Art.8 | — | ✓ A.8.8 | ✓ ID.AM, DE.CM | ✓ | ✓ KPI-11 | — | ✓ | CRA: obligación de gestionar la superficie de ataque en productos con elementos digitales |
| **P7.1** — Nivel de automatización del scoring | Todos | ✓ | ✓ Art.21 | ✓ Art.5 | — | ✓ A.8.16 | ✓ DE.CM, RS.AN | — | ✓ KPI-12 | — | — | NIS2 Art.21: medidas de gestión de riesgos deben ser proporcionadas al estado del arte |
| **P7.2** — Herramientas de scoring | Todos | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ PILAR | ✓ | — | — | ENS recomienda herramienta PILAR/EAR; NIS2 exige herramientas adecuadas al estado del arte |
| **P7.3** — DREAD con Machine Learning | Todos | — | ✓ Art.21 (estado del arte) | — | ✓ Art.25 (IA que trata datos) | — | ✓ | — | — | — | — | NIS2 Art.21: "estado del arte" incluye soluciones ML para scoring de amenazas |
| **P7.4** — Frecuencia de revisión | Todos | ✓ | ✓ Art.21.2.e | ✓ Art.5.5 | — | ✓ A.6.1, A.8.8 | ✓ ID.RA | ✓ | ✓ KPI-13 | — | — | DORA Art.5.5: revisión periódica del marco de gestión de riesgos TIC |
| **P7.5** — Consistencia inter-analista | Todos | — | ✓ Art.21 | — | — | ✓ A.6.1.2 | ✓ GV.RM | ✓ | ✓ | — | — | ISO27001: el SGSI debe garantizar consistencia en la evaluación de riesgos |
| **P8.2** — Alineación con ENS | Todos | ✓ Full | — | — | — | ✓ | — | ✓ Full | ✓ | — | — | ENS es de aplicación obligatoria a todas las AAPP y sus proveedores de servicios TIC |
| **P8.3** — Alineación con NIS2 / LCGC | Todos | — | ✓ Full | — | — | ✓ | — | — | ✓ | — | — | LCGC España (enero 2025): crea CNCS, define entidades, plazos y obligaciones |
| **P8.4** — Alineación con DORA | Todos | — | — | ✓ Full | — | ✓ | ✓ | — | ✓ | — | — | DORA de aplicación desde enero 2025 para entidades financieras en la UE |
| **P8.5** — KPIs/KRIs al Consejo | Todos | ✓ | ✓ Art.20 (gobernanza) | ✓ Art.5 | — | ✓ A.5.35 | ✓ GV.RR | — | ✓ Full | — | — | NIS2 Art.20: el órgano de dirección aprueba y supervisa las medidas de gestión de riesgos |
| **P9.1** — Escala nacional en evaluación de riesgos | A — Usuarios Afectados | — | ✓ Art.21 + NIS2-ES | — | — | — | ✓ GV.SC | — | ✓ | — | — | NIS2-ES: el CNCS coordinará el análisis de riesgos a nivel nacional |
| **P9.2** — Coordinación con organismos nacionales | Todos | ✓ | ✓ Arts.26-27 | — | — | — | ✓ RS.CO | — | ✓ | — | — | NIS2 Arts.26-27: cooperación con CSIRTs y Autoridades Competentes |
| **P9.3** — BCP/DRP ante ciberincidentes | D + A | ✓ | ✓ Art.21.2.c | ✓ Art.11 | — | ✓ A.5.30 | ✓ RC.RP | ✓ | ✓ KPI-15 | — | — | DORA Art.11: planes de continuidad del negocio específicos para incidentes TIC |
| **P10.1** — Cultura de ciberseguridad | Todos | ✓ | ✓ Art.21.2.g (formación) | ✓ Art.13 | — | ✓ A.6.3 | ✓ PR.AT | — | ✓ | — | — | NIS2 Art.21.2.g: programas de formación y concienciación como medida obligatoria |
| **P10.2** — Formación en metodologías | Todos | ✓ | ✓ Art.21.2.g | ✓ Art.13 | — | ✓ A.6.3 | ✓ PR.AT | — | ✓ | ✓ | — | DORA Art.13: formación específica en resiliencia operacional digital |
| **P10.3** — Presupuesto de ciberseguridad | Todos | — | ✓ Art.21 (proporcionalidad) | ✓ Arts.5-6 | — | ✓ A.5.35 | ✓ GV.RM | — | ✓ | — | — | NIS2 Art.21: las medidas deben ser proporcionales al riesgo y a los recursos de la entidad |

---

## TABLA DE ARTÍCULOS NORMATIVOS CLAVE

### NIS2 — Artículos con mayor incidencia en la encuesta

| Artículo NIS2 | Contenido | Preguntas relacionadas |
|--------------|-----------|----------------------|
| Art. 3 | Identificación de entidades esenciales e importantes | P0.5 |
| Art. 20 | Gobernanza: responsabilidad del órgano de dirección | P8.5, P10.1 |
| Art. 21 | Medidas de gestión de riesgos de ciberseguridad | P1.2, P2.1, P4.1, P7.1, P7.4 |
| Art. 21.2.a | Políticas de seguridad y análisis de riesgos | P2.1, P3.1, P4.1 |
| Art. 21.2.b | Gestión de incidentes | P2.3, P2.4 |
| Art. 21.2.c | Continuidad del negocio | P9.3 |
| Art. 21.2.e | Seguridad en la cadena de suministro | P3.2, P6.4 |
| Art. 21.2.f | Gestión de activos y seguridad en la adquisición | P5.5 |
| Art. 21.2.g | Formación y concienciación | P10.1, P10.2 |
| Art. 21.2.h | Monitorización continua y análisis de ciberseguridad | P6.2, P7.1 |
| Art. 23 | Notificación de incidentes (alerta 24h, notificación 72h, informe final 1 mes) | P2.4, P5.2 |
| Art. 26-27 | Cooperación con CSIRTs y Autoridades Competentes | P9.2 |

### ENS — Medidas con mayor incidencia en la encuesta

| Medida ENS | Categoría | Preguntas relacionadas |
|-----------|-----------|----------------------|
| Marco Organizativo — Política de Seguridad | Todas | P1.2, P8.2 |
| Marco Operacional — Planificación (análisis de riesgos) | Gestión | P2.1, P3.1, P4.1, P5.1 |
| Medida 2 — Gestión de activos | Operacional | P5.5, P6.4 |
| Medida 5 — Gestión de vulnerabilidades | Operacional | P3.2, P3.4 |
| Medida técnica — Monitorización | Técnica | P6.2, P7.1 |
| Categoría ALTA/MEDIA/BÁSICA | Clasificación | P2.1, P0.4 |

### DORA — Artículos clave

| Artículo DORA | Contenido | Preguntas relacionadas |
|--------------|-----------|----------------------|
| Art. 5 | Marco de gestión del riesgo TIC | P7.4, P8.4 |
| Art. 6 | Política de gestión del riesgo TIC | P2.1, P4.1 |
| Art. 8 | Gestión de activos TIC | P5.5, P6.4 |
| Art. 9 | Protección y prevención | P4.5 |
| Art. 11 | Continuidad del negocio y recuperación | P9.3 |
| Art. 13 | Aprendizaje y evolución / Formación | P10.2 |
| Art. 19 | Clasificación de incidentes | P2.3, P5.2 |
| Art. 20 | Notificación de incidentes graves | P2.4 |
| Art. 26 | TLPT (Threat-Led Penetration Testing) | P6.3 |

---

## NOTAS METODOLÓGICAS SOBRE EL MAPEO

1. **Principio de proporcionalidad normativa:** NIS2 y ENS aplican el principio de proporcionalidad: las obligaciones son más exigentes para entidades esenciales (categoría ALTA en ENS) que para entidades importantes o básicas. El mapeo refleja los requisitos en su nivel más exigente; cada organización debe calibrar según su categorización real.

2. **Solapamiento normativo:** Muchas preguntas mapeadas a NIS2 también mapean a ISO 27001 y NIST-CSF, ya que NIS2 no prescribe controles específicos sino objetivos de seguridad, y la forma de alcanzarlos puede ser mediante ISO 27001 u otros marcos equivalentes reconocidos por ENISA.

3. **DORA como lex specialis:** Para entidades del sector financiero, DORA prevalece sobre NIS2 como marco sectorial específico en materia de resiliencia digital. El mapeo doble (NIS2 + DORA) en preguntas de gestión de incidentes y continuidad refleja esta relación.

4. **CRA (Cyber Resilience Act):** Plenamente aplicable desde diciembre 2027, pero con obligaciones de diseño seguro y gestión de vulnerabilidades que ya afectan a fabricantes de productos digitales desde 2025 (período transitorio). El mapeo anticipatorio permite a los fabricantes posicionarse con antelación.

5. **IEC 62443:** Solo aplica a organizaciones con entornos OT/ICS. El mapeo se ha realizado para la versión 62443-3-3 (requisitos de seguridad del sistema) que es la más relevante para la evaluación de reproducibilidad y explotabilidad en sistemas industriales.

---

*Kit de Encuesta DREAD · Mapeo Normativo v1.0 · Abril 2026*
*Basado en: NIS2 (2022/2555), ENS RD 311/2022, DORA (2022/2554), GDPR (2016/679), ISO/IEC 27001:2022, NIST CSF v2.0, IEC 62443, CRA (UE 2024), INCIBE-IMC, MAGERIT v3*
