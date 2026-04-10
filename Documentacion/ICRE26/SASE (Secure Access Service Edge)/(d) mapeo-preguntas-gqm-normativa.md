# Mapeo de Preguntas/Métricas GQM a Requisitos Normativos (ENS, NIS2, otros)

> Tabla de referencia que vincula preguntas y métricas del marco GQM SASE con requisitos de ENS, NIS2 y marcos de continuidad/resiliencia relacionados. No pretende sustituir al análisis jurídico, sino facilitar la trazabilidad técnica–normativa.

---

## Tabla principal de mapeo

| Grupo | Pregunta/Métrica (Q/M) | Tema | ENS (RD 311/2022) – Ejemplos | NIS2 – Ejemplos | Otros marcos | Comentario de encaje |
|-------|------------------------|------|-------------------------------|-----------------|--------------|----------------------|
| G1 – Rendimiento & QoE | Q1.1 / M1.1 (latencia p95) | Rendimiento extremo a extremo | Principios de disponibilidad y calidad del servicio; medidas de protección de comunicaciones | Art. sobre continuidad de servicios y mitigación de impacto | Prácticas de QoS/QoE | Demuestra que las medidas de seguridad no degradan inaceptablemente servicios esenciales. |
| G1 – Rendimiento & QoE | Q1.2 / M1.2 (jitter voz/vídeo) | Estabilidad de comunicaciones | Medidas de comunicaciones seguras y disponibilidad | Requisitos para servicios esenciales (telemedicina, etc.) | Recomendaciones QoE sectoriales | Relevante en sanidad, emergencias y educación síncrona. |
| G1 – Rendimiento & QoE | Q1.3 / M1.4 (tiempo transacción) | Experiencia de usuario | ENS: objetivos de servicio al ciudadano, eficiencia | NIS2: impacto en prestación de servicios | UX / eGovernment | Métrica puente entre red y servicio público/negocio. |
| G1 – Rendimiento & QoE | Q1.4 / M1.5 (disponibilidad PoPs/túneles) | Disponibilidad infra SASE | ENS: disponibilidad, continuidad, redundancia | NIS2: continuidad y resiliencia | BIA/BCP | Clave para justificar diseño y pruebas de HA. |
| G1 – Rendimiento & QoE | Q1.5 / M1.6 (índice QoE) | QoE agregada | ENS: satisfacción en servicios digitales (implícita) | NIS2: confianza en servicios esenciales | Modelos de experiencia digital | Facilita reporting ejecutivo sobre “estado del servicio seguro”. |
| G2 – Zero Trust | Q2.1 / M2.1 (% MFA) | Autenticación fuerte | ENS: control de acceso, autenticación | NIS2: MFA donde proceda, políticas de acceso | Guías Zero Trust (NIST, ENISA) | Evidencia cumplimiento de requisitos de autenticación reforzada. |
| G2 – Zero Trust | Q2.2 / M2.2 (% apps vía ZTNA) | Exposición de apps internas | ENS: protección de sistemas de información; segmentación | NIS2: seguridad de redes y sistemas | NIST Zero Trust | Mide sustitución de modelos VPN amplios por acceso granular. |
| G2 – Zero Trust | Q2.3 / M2.3 (% accesos privilegiados via ZTNA+contexto) | Gestión de privilegios | ENS: cuentas privilegiadas, segregación | NIS2: gestión de identidades y privilegios | ISO 27001 A.9 | Indicador fino de control de acceso de alto riesgo. |
| G2 – Zero Trust | Q2.4 / M2.4 (madurez ZT) | Madurez arquitectónica | ENS: organización de la seguridad; mejora continua | NIS2: gestión de riesgos | Modelos ZTMM | Resume el nivel de implantación Zero Trust. |
| G3 – SOC | Q3.1–3 / M3.1–3 (MTTD/MTTC/MTTR SASE) | Detección y respuesta | ENS: gestión de incidentes, tiempos de respuesta | NIS2: identificación, mitigación, notificación | ISO 27035 | Demuestran capacidad operativa del SOC y efectividad de SASE como sensor/actuador. |
| G3 – SOC | Q3.4 / M3.4–3.5 (incidentes, amenazas bloqueadas) | Cobertura de detección | ENS: medidas de protección, registros | NIS2: monitorización y detección | MITRE ATT&CK (cobertura) | Apoya análisis de cobertura y eficacia de controles. |
| G4 – Cumplimiento | Q4.1 / M4.1 (% proyectos cloud integrados en SASE) | Gobernanza cloud | ENS: servicios en la nube, cadena de suministro | NIS2: seguridad de proveedores y servicios de terceros | Guías ENS cloud | Mide disciplina en exigir SASE/ZTNA como requisito de diseño. |
| G4 – Cumplimiento | Q4.2 / M4.2 (% sistemas ENS M/A vía SASE/ZTNA) | Cobertura de controles en sistemas críticos | ENS: medidas reforzadas en sistemas medio/alto | NIS2: servicios esenciales y críticos | Perfil ENS sectorial | Indicador directo para AAPP y proveedores ENS. |
| G4 – Cumplimiento | Q4.3 / M4.3 (% logs desde SASE) | Trazabilidad | ENS: registro y trazabilidad | NIS2: monitorización y logging | ISO 27001 A.12 | Demuestra centralización de evidencias de acceso. |
| G4 – Cumplimiento | Q4.4 / M4.4 (índice alineamiento SASE–ENS/NIS2) | Mapeo formal de controles | ENS & NIS2 en conjunto | ENS–NIS2 guía de trasposición | GRC corporativo | Ofrece visión sintética del encaje regulatorio. |
| G5 – Continuidad | Q5.1 / M5.1 (SASE en planes BCP) | Inclusión en continuidad | ENS: continuidad de la actividad | NIS2: continuidad y recuperación | ISO 22301 | Mide integración entre ciber y continuidad. |
| G5 – Continuidad | Q5.2–5.3 / M5.2–5.3 (redundancia y conmutación) | Resiliencia infra | ENS: redundancia, tolerancia a fallos | NIS2: resiliencia de redes/sistemas | Arquitecturas HA | Apoya diseño de topologías resilientes y pruebas periódicas. |
| G5 – Continuidad | Q5.3 / M5.4 (indisponibilidad anual atribuible a SASE) | Impacto de SASE | ENS: objetivos de disponibilidad | NIS2: impacto en servicios esenciales | KPIs de disponibilidad | Permite identificar riesgos residuales en la capa SASE. |
| G6 – Negocio/ROI | Q6.1 / M6.1 (consolidación plataformas) | Simplificación | ENS: gestión de activos; eficacia de medidas | NIS2: eficiencia en gestión de riesgos | Estrategias de consolidación | Relaciona SASE con reducción de complejidad operacional. |
| G6 – Negocio/ROI | Q6.2 / M6.2–6.3 (ahorros, horas OPEX) | Eficiencia económica | ENS: eficiencia en gestión de seguridad | NIS2: proporcionalidad | Modelos de TCO | Alimenta discurso de sostenibilidad financiera. |
| G6 – Negocio/ROI | Q6.3–6.4 / M6.4–6.5 (reducción incidentes, ROI) | Coste evitado y retorno | ENS & NIS2: reducción de riesgo e impacto | NIS2: enfoque basado en riesgo | Buenas prácticas ROI ciber | Permite “hablar el idioma” de dirección y finanzas. |