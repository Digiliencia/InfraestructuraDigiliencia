
# Informe TLPT.

La TLPT, hija díscola de DORA y hermana del TIBER‑EU, se está convirtiendo en un lenguaje común de “ciber‑estrés test” a escala europea, y España ya juega en primera división con TIBER‑ES y con los RTS conjuntos de las ESAs de 2024 como partitura oficial.[^1][^2]

***

## 1. Marco normativo TLPT 2025+ (España y mundo)

- DORA convierte la TLPT en prueba avanzada obligatoria para entidades financieras sistémicas y otras que superen umbrales cuantitativos, con aplicación desde enero de 2025 y frecuencia habitual trienal.[^3][^4][^1]
- El RTS conjunto de las ESAs de julio 2024 concreta criterios de selección, metodología, fases, requisitos de testers internos/externos, uso de inteligencia de amenazas y cooperación supervisora, constituyendo el estándar mínimo de TLPT bajo DORA.[^2][^1][^3]
- España adopta TIBER‑EU mediante TIBER‑ES (Guía de implementación 2022, Banco de España), manteniendo la lógica de tres fases (preparación, test, cierre), trabajo sobre entornos de producción y proveedores externos de TI y Red Team, ahora armonizable con DORA.[^2]
- Varios países de la UE (NL, IE, DE, FR, IT, PT, SE, etc.) ya tenían marcos TIBER nacionales y los están alineando con los RTS TLPT, mientras que fuera de la UE predominan marcos equivalentes tipo CBEST (Reino Unido) o esquemas sectoriales basados en NIST/OSSTMM pero sin un RTS tan detallado.[^5][^1][^2]

**Idea de mensaje para encuesta (tono irónico‑constructivo):**

- “Hemos pasado de jugar pachangas de pentest a la Champions League de la ciberresiliencia: ahora el reglamento viene numerado, firmado por las ESAs y con acta del TIBER‑ES.”

***

## 2. Fases TLPT y familias de indicadores

### 2.1 Fase de preparación

Según TIBER‑ES y los RTS DORA, la preparación incluye: constitución de White/Control Team, selección de proveedores, definición de alcance basado en funciones críticas, gestión de riesgos, planificación.[^6][^2]

Familias de métricas:

- Alcance y criticidad
    - Porcentaje de funciones críticas de negocio cubiertas por el TLPT sobre el total de funciones críticas identificadas en el BIA.[^6][^2]
    - Número de servicios críticos soportados por terceros TIC incluidos en el test frente al total de servicios críticos externalizados.[^2][^6]
- Gobierno y madurez
    - Tiempo desde la notificación de obligación de TLPT por la autoridad hasta la designación formal del Control/White Team.[^1][^2]
    - Existencia de política formal de uso de testers internos (cuando se aplique DORA, con los requisitos específicos de política, recursos y mitigación de impacto sobre operaciones).[^1]
- Proveedores y riesgo
    - Porcentaje de proveedores de TI/Red Team que cumplen los requisitos de experiencia, independencia, aseguramiento y cobertura de riesgos establecidos en el RTS y en las guías TIBER‑EU de contratación.[^1][^2]
    - Número de riesgos identificados en el análisis de riesgo del TLPT y porcentaje con medidas de mitigación aceptadas antes del inicio del test.[^6][^2]


### 2.2 Fase de test (Threat Intelligence + Red Team)

La metodología TLPT exige una fase de inteligencia dirigida (GTL/TTI) seguida de una campaña de Red Team activa de al menos 12 semanas sobre sistemas en producción.[^2][^6][^1]

Familias de métricas:

- Inteligencia y escenarios
    - Número de escenarios de ataque definidos en el TTI alineados con el panorama de amenazas real del sector financiero español/europeo.[^6][^2]
    - Porcentaje de escenarios TTI finalmente ejercitados por el Red Team en el plan de test.[^2][^6]
- Ejecución Red Team
    - Duración real de la ventana de Red Team activo frente al mínimo regulatorio de 12 semanas.[^1][^6]
    - Número de “banderas” u objetivos críticos comprometidos (confidencialidad, integridad, disponibilidad, fraude, etc.) frente a los planificados en el alcance.[^6][^2]
    - Número y tipo de ayudas concedidas por el White Team (bypasses de controles, accesos directos) y su impacto en la interpretación de resultados.[^6]
- Detección y respuesta (Blue Team “a ciegas”)
    - Tiempo de detección del primer indicador de compromiso (MTTD TLPT) desde el inicio de actividades hostiles realistas por parte del Red Team.[^2][^6]
    - Tiempo de contención (MTTC) y de recuperación (MTTR) de los sistemas o funciones afectados durante el ejercicio.[^6]
    - Porcentaje de actividades del Red Team detectadas por los mecanismos de monitorización y el personal de operaciones (cobertura de detección).[^6]


### 2.3 Fase de cierre, purple teaming y remediación

Los RTS hacen obligatoria la fase de purple teaming y replay en el cierre; TIBER‑ES ya contemplaba informes detallados de Red Team y Blue Team, informe resumen y plan de acción.[^1][^2][^6]

Familias de métricas:

- Calidad de informes
    - Plazo de entrega del Red Team Test Report y del Blue Team Test Report frente a los plazos de referencia del RTS (se ampliaron tras la consulta pública por preocupación de la industria).[^1][^2]
    - Grado de detalle técnico y de negocio en el Test Summary Report, medido por cobertura de todas las funciones críticas, TTP utilizadas y mapeo a controles.[^2][^1]
- Plan de remediación
    - Número total de hallazgos categorizados por criticidad (muy alto, alto, medio, bajo) y tipo (técnico, proceso, humano, tercero).[^1][^2]
    - Porcentaje de vulnerabilidades críticas y altas con plan de remediación aprobado en un máximo de 8 semanas tras el cierre (plazo de referencia indicado en prácticas DORA/TLPT).[^2][^1]
    - Porcentaje de acciones de remediación ejecutadas dentro del plazo comprometido, y número de hallazgos reabiertos en re‑test posterior.[^6]
- Cooperación supervisora
    - Tiempo desde la entrega del plan de remediación a la recepción de la “attestation” por parte de la autoridad TLPT, que certifica que el ejercicio se ha ejecutado conforme al RTS y que identifica funciones en alcance.[^1]

**Ejemplo de pregunta de encuesta (ad hoc, con un punto de mala leche):**

- “Cuando le dijeron a su Blue Team que el ‘incidente’ había sido un TLPT, ¿la reacción mayoritaria fue: a) alivio, b) vergüenza profesional, c) petición de más presupuesto, d) todo lo anterior?”

***

## 3. Indicadores TLPT para uso nacional (España)

### 3.1 Indicadores a nivel de entidad

Pensados para ser agregables por supervisores (Banco de España, CNMV, DGSFP) bajo DORA y TIBER‑ES.[^2][^1][^6]

- Cobertura estructural
    - TLPT‑01: Entidades obligadas que han realizado al menos un TLPT en el ciclo trienal vs. total de entidades identificadas según criterios RTS (G‑SII, O‑SII, infraestructuras de mercado, etc.).[^1]
    - TLPT‑02: Porcentaje de funciones críticas de negocio cubiertas por el TLPT más reciente.
- Calidad y rigor de prueba
    - TLPT‑03: Porcentaje de TLPT con duración de Red Team ≥ 12 semanas y con uso efectivo de TTI alineado con GTL sectorial.[^2][^6][^1]
    - TLPT‑04: Porcentaje de TLPT con ejercicios de purple teaming completados y documentados.
- Eficacia de detección y respuesta
    - TLPT‑05: MTTD mediano (en horas/días) frente a ataques TLPT exitosos, por tipo de técnica (credenciales, phishing, explotación de vulnerabilidad, cadena de suministro).[^6]
    - TLPT‑06: Porcentaje de ataques TLPT que alcanzan objetivos críticos sin detección previa.
- Gestión de vulnerabilidades
    - TLPT‑07: Ratio hallazgos críticos/altos por TLPT y porcentaje cerrados en plazo ≤ 6/12 meses.
    - TLPT‑08: Porcentaje de hallazgos TLPT recurrentes (ya aparecían en el TLPT anterior o en un TIBER‑ES previo).[^2][^6]


### 3.2 Indicadores agregados país/territorio

Orientados a cuadros de mando nacionales, alineados con DORA y con el rol del TIBER Cyber Team español.[^1][^2]

- Penetración TLPT
    - % de activos financieros nacionales (por volumen de balance, transacciones, activos bajo gestión) cubiertos por al menos un TLPT en los últimos 3 años.
- Madurez operativa
    - Mediana de MTTD/MTTR TLPT a nivel de país, comparada con benchmarks europeos (cuando se publiquen análisis agregados).
- Dependencias críticas
    - Número de TLPT conjuntos o “pooled” que involucran proveedores TIC clave (cloud, core bancario, procesadores de pagos), indicando qué porcentaje del sector queda cubierto mediante estos ejercicios.[^1]

***

## 4. Comparativa internacional de indicadores TLPT

### 4.1 Europa (DORA + TIBER‑EU)

- Estándar común
    - Los RTS de 2024 fijan requisitos homogéneos para criterios de selección, metodología, fases y cooperación supervisora, lo que permite comparar indicadores como frecuencia, cobertura, severidad de hallazgos y tiempos de remediación entre Estados miembros.[^3][^1]
- Caso España
    - España parte con ventaja al tener TIBER‑ES operativo desde 2022; muchas métricas ya existen de facto (banderas, tiempos, cobertura) y solo requieren alineación terminológica con DORA.[^6][^2]


### 4.2 Reino Unido (CBEST) y otros

- Reino Unido
    - CBEST, precursor de TIBER‑EU, ya utilizaba indicadores similares (éxito de escenarios, tiempo de detección, calidad de respuesta) en ejercicios orientados a infraestructuras críticas financieras; la convergencia con TLPT es alta, aunque el lenguaje normativo es distinto.
- Estados Unidos y otros
    - No cuentan con un RTS TLPT equivalente, pero se aproximan a través de marcos de “assumed breach”, red‑teaming continuado y pruebas adversariales avanzadas ligadas a NIST CSF, con métricas de eficacia de controles, tiempos de contención y cobertura de monitoreo, que pueden mapearse a indicadores TLPT.


### 4.3 Tabla de ejes de comparación

| Eje | España (TIBER‑ES + DORA) [^2][^1] | Resto UE (TIBER‑EU + DORA) [^1][^3] | UK (CBEST) | EEUU / otros |
| :-- | :-- | :-- | :-- | :-- |
| Naturaleza TLPT | Obligatoria para entidades designadas | Obligatoria para entidades designadas | Sectorial | Voluntaria/sectorial |
| Marco técnico | TIBER‑ES alineado con TIBER‑EU | TIBER‑EU nacional | CBEST | NIST/propios |
| Duración Red Team | ≥ 12 semanas | ≥ 12 semanas | Variable | Variable |
| Foco métricas | Función crítica, MTTD/MTTR, remediación | Idem, con variaciones locales | Escenarios, respuesta | Controles, tiempos |
| Supervisión y attestation | Attestation TLPT nacional | Attestation TLPT nacional/EMI | Regulador sectorial | Diverso |


***

## 5. Líneas de evolución 2025‑2027 en indicadores TLPT

- De “pasar el examen” a medir resiliencia real
    - El RTS deja claro que TLPT es un mínimo y que las autoridades pueden exigir ir más allá, lo que empujará métricas de madurez (ej. integración con Zero Trust, automatización de respuesta, calidad de telemetría) más allá del simple “conté los hallazgos”.[^2][^1]
- Más enfoque en terceros y pruebas conjuntas
    - Crecen las figuras de “pooled test” y “joint test” que obligan a definir indicadores sobre proveedores TIC compartidos (qué parte del riesgo sistémico se ha ejercitado realmente, cuántas funciones críticas de varios bancos dependen del mismo incidente simulado).[^1]
- Internalización controlada del Red Team
    - DORA permite testers internos con salvaguardas y exige externalizar al menos cada tercer test, lo que abre la puerta a indicadores de capacidad interna (número de pruebas adversariales internas al año, calidad de los informes, independencia) que complementen el TLPT regulatorio.[^1]


<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30][^7][^8][^9]</span>

<div align="center">⁂</div>

[^1]: https://www.tarlogic.com/es/blog/pruebas-tlpt/

[^2]: https://www.alter-solutions.es/pruebas-penetracion-amenazas-tlpt

[^3]: https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/operational-resilience/joint-regulatory-technical-standards-specifying-elements-related-threat-led-penetration-tests

[^4]: https://www.digital-operational-resilience-act.com/DORA_Article_23_(Proposal).html

[^5]: https://fortbridge.co.uk/pentesting/the-ultimate-guide-to-threat-led-penetration-testing-tlpt/

[^6]: https://itresit.es/dora-pruebas-tlpt/

[^7]: https://telefonicatech.com/blog/tiber-eu-y-tlpt-pruebas-avanzadas-de-ciberresiliencia-para-el-sector-financiero-en-el-marco-dora

[^8]: https://www.hackplayers.com/2025/01/dora-tlpt-ciberseguridad-financiera.html

[^9]: https://doctorcarlosmorales.com/unidad-del-dolor-malaga/terapia-laser-percutanea-tlp-la-medicina-regenerativa-que-elimina-su-dolor-cronico-en-malaga/

[^10]: https://www.flu-project.com/2024/11/zerolynx-referencia-tltp-redteam-dora.html

[^11]: https://news.altonaspain.es/ciberseguridad/estrategia-zero-trust-clave-para-la-evolucion-y-la-resiliencia/

[^12]: https://www.deloitte.com/es/es/services/consulting/research/estado-ciberseguridad.html

[^13]: https://intelequia.com/es/blog/post/reglamento-de-resiliencia-operativa-digital-dora-qué-es-y-cumplimiento-normativo

[^14]: https://www.ciberseguridadpyme.es/actualidad/pruebas-tlpt-que-son-y-que-empresas-deben-realizarlas/

[^15]: https://ceim.es/documento/publication-document-1736782515.pdf

[^16]: https://www.digital-chiefs.de/es/tlpt-bajo-dora-como-los-cio-superan-la-prueba-de-ciberresiliencia/

[^17]: https://a3sec.com/blog/threat-intelligence-mitigacion-ciberamenazas

[^18]: https://www.bde.es/f/webbde/INF/MenuHorizontal/Servicios/TIBER-ES/Guia_implantacion_Tiber.pdf

[^19]: https://www.esma.europa.eu/sites/default/files/2024-07/JC_2024-29_-_Final_report_DORA_RTS_on_TLPT.pdf

[^20]: https://www.scribd.com/document/772085907/JC-2024-29-Final-report-DORA-RTS-on-TLPT

[^21]: https://www.infront.co/content/dam/infront-co/language-masters/en/downloads/dora/JC 2024-29 - Final report_DORA%20RTS%20on%20TLPT.pdf

[^22]: https://www.eba.europa.eu/sites/default/files/2024-07/427a52cf-5772-4b69-8eb5-d121c90c470a/JC 2024-29 - Final report_DORA%20RTS%20on%20TLPT.pdf

[^23]: https://www.deloitte.com/ie/en/services/consulting-risk/research/dora-regulatory-technical-standards.html

[^24]: https://www.deloitte.com/mt/en/services/risk-advisory/perspectives/dora-european-supervisory-authorities-publish-second-set-of-technical-standards-and-guidelines.html

[^25]: https://www.eba.europa.eu/publications-and-media/events/consultation-joint-draft-rts-specifying-elements-related-threat-led-penetration-tests

[^26]: https://panorays.com/blog/tlpt-for-dora-compliance/

[^27]: https://www.regulation-dora.eu/pdf/dora-rts-its-complete-overview.html

[^28]: https://www.linkedin.com/posts/pg-legal_european-supervisory-authorities-adopt-new-activity-7234458763108220928-nfZF

[^29]: https://assets.kpmg.com/content/dam/kpmgsites/be/pdf/KPMG-BE-Webcast_DORA-Unleashed-Navigating-the-2nd-Batch-of-RTS-and-ITS_20240313.pdf.coredownload.inline.pdf

[^30]: https://www.eiopa.europa.eu/esas-provide-guidelines-facilitate-consistency-regulatory-classification-crypto-assets-industry-and-2024-12-10_en

