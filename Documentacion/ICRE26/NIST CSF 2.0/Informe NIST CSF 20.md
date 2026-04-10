
# Informe NIST CSF 20.

La versión 2.0 del NIST CSF ha convertido la medición en un “deber ser” explícito: ya no basta con “hacer cosas de seguridad”, hay que demostrar, con números, que se gobierna el riesgo y se mejora en el tiempo. A nivel país, España puede articular indicadores CSF 2.0 apoyándose en su Estrategia Nacional de Ciberseguridad, el Plan Nacional de Ciberseguridad y las métricas que ya publica la Administración General del Estado sobre incidentes, inversión y capacidades.[^1][^2][^3][^4]

## 1. Qué mide realmente NIST CSF 2.0

CSF 2.0 no incluye “KPIs pre‑hechos”, pero sí define dónde deben existir métricas: en casi todas las subcategorías hay ejemplos de objetivos medibles, riesgos cuantificados, y revisiones con KPIs/KRIs. En particular:[^2][^1]

- GOVERN (GV): exige objetivos de gestión del riesgo medibles, declaraciones de apetito y tolerancia al riesgo, KPIs/KRIs revisados y comunicados a la alta dirección.[^1][^2]
- IDENTIFY (ID): inventarios completos y priorización de activos, vulnerabilidades y dependencias, con uso de análisis de impacto y registros de riesgo para priorizar respuestas.[^2][^1]
- PROTECT (PR): control de acceso, formación, seguridad de datos y plataformas, todos con ejemplos de cobertura, frecuencia, calidad y cumplimiento que son fácilmente traducibles a métricas.[^1][^2]
- DETECT (DE), RESPOND (RS), RECOVER (RC): insisten en detección oportuna, respuesta contenida y recuperación alineada con objetivos de resiliencia (RTO/RPO), con lecciones aprendidas y planes actualizados.[^2][^1]

Además, NIST ha publicado “Implementation Examples” que, aunque no llaman a nada “indicador” de forma explícita, describen acciones que solo tienen sentido si se miden (revisión de KPIs/KRIs, seguimiento de planes de acción, evaluación de desempeño).[^1]

## 2. Dimensiones clave de indicadores CSF 2.0 (visión mundial)

A partir del propio CSF 2.0 y de sus ejemplos de implementación, se pueden agrupar las métricas modernas (post‑2024) en seis bloques temáticos.[^2][^1]

### 2.1. Gobernanza, apetito de riesgo y desempeño (GV)

Indicadores típicos alineados con GOVERN:

- Porcentaje de objetivos de gestión de riesgo ciber definidos con métricas claras (p.ej., “% sistemas críticos por debajo de X vulnerabilidades críticas”).[^1]
- Porcentaje de unidades u organismos que han formalizado y comunicado sus declaraciones de apetito y tolerancia al riesgo.[^1]
- Número de riesgos ciber agregados en el registro de riesgos corporativo/nacional (integrados con ERM), y proporción respecto al total de riesgos estratégicos.[^2][^1]
- Frecuencia con la que se revisa la estrategia de ciberseguridad a la luz de auditorías, incidentes y cambios en requisitos (normativos, tecnológicos, de misión).[^1]
- Existencia y uso de un método estandarizado de cálculo y priorización de riesgos (porcentaje de análisis de riesgo realizados bajo ese método).[^1]

Ejemplo de KPI “filosófico pero cuantificable”: porcentaje de decisiones estratégicas de negocio (fusiones, grandes contratos, externalizaciones) que incluyen análisis explícito de ciberriesgo documentado.[^1]

### 2.2. Gestión de activos, datos y dependencias (ID.AM, ID.IM)

- Cobertura de inventario de hardware y software (p.ej., “% de dispositivos OT/IoT detectados automáticamente frente a estimación total”).[^1]
- Porcentaje de servicios en la nube, APIs y SaaS catalogados con propietario, criticidad y datos tratados.[^1]
- Porcentaje de activos priorizados por criticidad y impacto en la misión, actualizado en los últimos 12 meses.[^1]
- Cobertura de clasificación de datos para tipos designados (PII, IP, datos OT, etc.) y porcentaje con metadatos completos (origen, propietario, geolocalización).[^1]
- Porcentaje de sistemas que incorporan criterios de ciberseguridad a lo largo de todo su ciclo de vida (desde diseño hasta retirada), incluido desmantelamiento seguro.[^1]


### 2.3. Evaluación de riesgos, vulnerabilidades y amenazas (ID.RA)

CSF 2.0 dedica varias subcategorías a que el riesgo sea cuantificado, registrado y seguido.[^1]

- Densidad de vulnerabilidades críticas (número por activo o por mil activos), y tiempo medio de remediación por criticidad.[^1]
- Porcentaje de vulnerabilidades identificadas que cuentan con plan de respuesta documentado y seguimiento.[^1]
- Cobertura de fuentes de threat intelligence integradas efectivamente en herramientas de detección/respuesta.[^1]
- Porcentaje de escenarios de riesgo con estimaciones explícitas de probabilidad e impacto documentadas en el registro de riesgos.[^1]
- Porcentaje de cambios y excepciones con análisis de riesgo formal y rastreable, revisados periódicamente.[^1]


### 2.4. Operaciones de protección, detección y respuesta (PR, DE, RS)

Aunque el CSF es agnóstico a tecnologías concretas, los ejemplos apuntan a indicadores operacionales clásicos modernizados.[^2][^1]

- Porcentaje de identidades (usuarios, servicios, dispositivos) cubiertas por MFA conforme a política.[^1]
- Porcentaje de cuentas con privilegios revisados en plazo tras cambio de rol o salida (cero trust disciplinado).[^1]
- Porcentaje de plantilla cubierta por programas de concienciación, y tasa de éxito/fracaso en simulaciones de phishing.
- Cobertura de logs y telemetría (p.ej., “% de activos críticos integrados en SIEM/Plataforma de detección”, “% tráfico Este‑Oeste monitorizado”).
- Tiempos medios: MTTD (detección), MTTR (respuesta), TME para contener, aislar y erradicar incidentes críticos.
- Porcentaje de incidentes gestionados conforme a los planes formales de respuesta, con lecciones aprendidas documentadas.


### 2.5. Recuperación y resiliencia (RC)

CSF 2.0 enfatiza resiliencia y objetivos de recuperación como parte de la estrategia.[^1]

- Porcentaje de servicios críticos con objetivos de RTO/RPO definidos, aprobados y comunicados.[^1]
- Porcentaje de servicios que cumplen su RTO/RPO en pruebas de recuperación y en incidentes reales.
- Frecuencia y alcance de pruebas de continuidad/recuperación (incluida participación de proveedores críticos).[^1]
- Porcentaje de planes de continuidad y DR actualizados en los últimos 12 meses.


### 2.6. Cadena de suministro y terceros (GV.SC)

La función GOVERN incorpora explícitamente la Cybersecurity Supply Chain Risk Management, con ejemplos de inventario, criterios de criticidad y requisitos contractuales.[^1]

- Porcentaje de proveedores clasificados por criticidad según criterios normalizados (datos tratados, acceso a sistemas, impacto en la misión).[^1]
- Porcentaje de proveedores críticos con requisitos de seguridad explícitos en contrato (SLAs de seguridad, SBOM, divulgación de vulnerabilidades, etc.).[^1]
- Porcentaje de proveedores críticos sometidos a evaluación periódica de seguridad, y porcentaje que demuestra conformidad (certificaciones, auditorías, evidencias técnicas).[^1]
- Número de incidentes significativos originados o amplificados por la cadena de suministro, y tiempo de detección/comunicación conjunto.[^1]


## 3. Tendencias recientes (2025–2026) en métricas CSF 2.0

A partir de CSF 2.0, de sus Implementation Examples y de la evolución de guías asociadas (perfiles sectoriales, guías rápidas), pueden verse varias tendencias claras.[^5][^1]

- De “cumplir controles” a medir resultados: se priorizan métricas que relacionan capacidades con reducción de impacto (p.ej., cumplimiento de RTO, caída de incidentes graves, menor exposición de vulnerabilidades críticas) frente a mera existencia de políticas.[^1]
- Integración con ERM: las guías de NIST sobre integración con Enterprise Risk Management fomentan el uso de KPIs/KRIs comunes para ciber, privacidad, cadena de suministro y otros riesgos.[^2][^1]
- Indicadores de gobernanza y desempeño del CISO: NIST sugiere explícitamente revisar KPIs y KRIs para ajustar estrategia, evaluar el rendimiento de roles clave y asegurar que la política se cumple.[^2][^1]
- Métricas para IA y dominios emergentes: los perfiles CSF específicos para IA usan los mismos tipos de resultados y, por tanto, incentivan indicadores análogos (inventarios, riesgos, controles, respuesta).[^6]
- Automatización y monitorización continua: marcos de implementación recientes insisten en inventarios dinámicos, métricas actualizadas casi en tiempo real y seguimiento de acciones mediante registros de riesgo y planes de acción.[^7][^8]


## 4. Aplicación a nivel nacional en España

España ya dispone de una arquitectura institucional que se presta bien a mapear indicadores CSF 2.0 a escala país: Estrategia Digital 2025, Estrategia Nacional de Ciberseguridad, Plan Nacional de Ciberseguridad, CCN‑CERT, INCIBE, CNPIC, etc. Los planes recientes insisten en reforzar capacidades, adaptarse a nuevas tecnologías (IA, computación cuántica) y afrontar un volumen creciente de ataques (más de 100 000 en 2024, con un crecimiento del 300% desde 2015 y un incidente muy grave cada tres días).[^3][^4]

### 4.1. Ejes de indicadores nacionales alineados con CSF 2.0

A nivel país, los indicadores pueden estructurarse de forma paralela a las funciones CSF:

- Gobernanza nacional (GV):
    - Número de estrategias y planes vigentes que incorporan ciberriesgo en la planificación nacional (seguridad, digitalización, defensa).[^4][^3]
    - Porcentaje del presupuesto nacional de ciber y ciberdefensa ejecutado vs. planificado, por organismo (Defensa, DSN, CNI‑CCN, etc.).[^4]
    - Frecuencia de revisión de la Estrategia Nacional de Ciberseguridad para incorporar cambios de amenazas y tecnologías (IA, cuántica).[^4]
- Capacidad instalada y preparación (ID, PR):
    - Número de especialistas nuevos en ciberseguridad, IA y datos formados respecto al objetivo (p.ej., 20 000 nuevos especialistas en 2025).[^3]
    - Porcentaje de servicios públicos digitalizados con medidas de ciberseguridad alineadas a un perfil CSF (actual o futuro).[^3]
    - Número y cobertura de Centros de Operaciones de Seguridad (públicos y sectoriales) conectados con CERT nacionales (INCIBE‑CERT, CCN‑CERT).
- Exposición y eficacia operativa (DE, RS, RC):
    - Número total de incidentes gestionados por los CERT nacionales por año, tasa de crecimiento y distribución por sector.[^4]
    - Número de ciberataques “muy graves” por periodo (p.ej., un caso cada tres días en 2024) y su tendencia.[^4]
    - Tiempos medios de detección, notificación a CSIRT nacionales y recuperación de servicios esenciales.
- Cadena de suministro y ecosistema (GV.SC):
    - Porcentaje de contratos públicos estratégicos que incluyen cláusulas de ciberseguridad alineadas a requisitos CSF (seguridad en la nube, SBOM, notificación de incidentes, etc.).[^1]
    - Número de proveedores y operadores esenciales que reportan incidentes y métricas a los organismos nacionales (CERT, supervisores sectoriales).


### 4.2. Tabla de ejes de indicadores nacionales CSF 2.0

| Función CSF 2.0 | Eje de medición nacional (España) | Ejemplos de indicadores |
| :-- | :-- | :-- |
| GOVERN | Estrategia y recursos nacionales | % presupuesto ejecutado; nº revisiones de estrategia; nº órganos de coordinación activos.[^3][^4] |
| IDENTIFY | Inventario de sectores y servicios críticos | % OES/servicios esenciales con perfil CSF; nº análisis de impacto negocio por sector. |
| PROTECT | Capacidades de protección y formación | % servicios públicos con requisitos mínimos; nº especialistas formados vs. objetivo.[^3] |
| DETECT | Monitorización e inteligencia | Nº incidentes detectados por CERT; % sectores conectados a plataformas de intercambio de inteligencia.[^4] |
| RESPOND | Gestión nacional de incidentes | Tiempo medio de notificación; nº ejercicios nacionales multiactor al año. |
| RECOVER | Resiliencia y continuidad | % servicios esenciales con RTO/RPO definidos y probados; nº simulacros de recuperación exitosos. |
| GV.SC | Cadena de suministro | % contratos críticos con cláusulas de seguridad; nº proveedores críticos evaluados periódicamente.[^1] |

## 5. Comparativa internacional: cómo lo están haciendo otros

Aunque cada país viste el traje CSF 2.0 a su manera, se aprecian patrones convergentes:

- Estados Unidos: NIST posiciona el CSF como base para sectores críticos y para la integración con ERM federal, con énfasis en Tiers, perfiles organizativos y métricas ligadas a KPIs/KRIs empresariales.[^2][^1]
- Unión Europea: la regulación (NIS2, DORA, CRA) impulsa indicadores de resiliencia y madurez (tiempos de notificación, niveles de cobertura de medidas de seguridad, resultados de pruebas de penetración y TLPT), que se mapean bien a funciones CSF.
- Países con estrategia avanzada (Nordics, Países Bajos, Alemania): suelen publicar paneles de ciberresiliencia nacional que incluyen: volumen de incidentes, cobertura de CERT sectoriales, niveles de cumplimiento, formación, participación en ejercicios y datos de cadena de suministro.

España comparte con estos países una combinación de: ambición de digitalización, presión regulatoria europea y necesidad de adaptar continuamente su Plan Nacional de Ciberseguridad al contexto geopolítico y tecnológico (IA, cuántica, etc.). El espacio natural de convergencia es un cuadro de mando nacional articulado en torno a los seis verbos CSF y poblado con métricas que ya existen dispersas (CERT, ministerios, supervisores sectoriales) pero hoy no siempre se presentan bajo ese prisma.[^3][^4]

## 6. Propuesta de indicadores “para encuesta” con tono CSF 2.0

Como orquestador de la liga de CISOs, criptógrafos y demás fauna ilustrada, uno puede desplegar en una encuesta nacional algo como esto (formulado para que el encuestado sienta el pellizco, pero también la guía):

### 6.1. Gobernanza (GV)

- “¿Hasta qué punto dispone su organización de objetivos de gestión de riesgo ciber traducidos a métricas? (p.ej., ‘% sistemas críticos sin vulnerabilidades críticas abiertas más de 30 días’).
    - 0% – Vivimos en la alegre nebulosa del ‘hágase la seguridad’.
    - 1–25% – Algún KPI suelto, cual verso libre.
    - 26–75% – Tenemos un poema razonablemente completo.
    - >75% – El consejo lee un cuadro de mando que casi da miedo de lo claro que es.”
- “¿Con qué frecuencia se revisa su estrategia de ciberseguridad a raíz de auditorías, incidentes o cambios regulatorios?
    - Nunca o ad hoc (solo después del desastre).
    - Anualmente, con cierta disciplina estoica.
    - Al menos dos veces al año, con datos y sangre fría.
    - Iterativamente, incorporando KPIs y KRIs casi en tiempo real.”


### 6.2. Gestión de activos y datos (ID)

- “¿Qué porcentaje estima que tiene de inventario de activos (IT, OT, IoT, nube) detectado automáticamente?
    - <50% – Somos más colección de sorpresas que de activos.
    - 50–80% – Vemos bastante, sospechamos el resto.
    - 81–95% – Solo se nos escapan los ninjas.
    - >95% – Cualquier dispositivo que respira en la red, lo sabemos.”
- “¿Los tipos de datos clave (PII, IP, datos OT, etc.) están etiquetados y con propietario definido?
    - No, los datos vagan libres como el ganado en la Mesta.
    - Parcialmente, en sistemas críticos.
    - Mayoritariamente, con clasificación y dueño.
    - Sí, y se usan estas etiquetas para políticas y monitoreo.”


### 6.3. Riesgo, vulnerabilidades y cambios (ID.RA)

- “¿Qué porcentaje de vulnerabilidades críticas se corrigen dentro del plazo definido por su política?
    - <25% – La política es más literatura que realidad.
    - 25–75% – Avanzamos, pero el backlog nos mira con sorna.
    - >75% – El SLA de parcheo compite con la Fórmula 1.”
- “En los últimos 12 meses, ¿qué porcentaje de cambios relevantes en sistemas críticos se acompañó de un análisis de riesgo formal?
    - Casi ninguno – ‘Qué podría salir mal’, dijeron.
    - Algunos cambios importantes.
    - La mayoría de cambios que tocan sistemas críticos.
    - Prácticamente todos, documentados y revisados.”


### 6.4. Protección, detección y respuesta (PR, DE, RS)

- “¿Qué cobertura tiene la autenticación multifactor en sus cuentas de alto riesgo (administradores, acceso remoto, aplicaciones críticas)?
    - <25% – La fe en la contraseña sigue siendo fuerte.
    - 25–75% – En transición, con resistencia cultural incluida.
    - >75% – Solo olvidamos a algún servicio ‘de toda la vida’.
    - ~100% – El paraíso zero trust (o casi).”
- “Ante un incidente grave, el tiempo medio hasta la contención (aislar sistemas, cortar propagación) suele ser:
    - Desconocido – vivimos en la épica, no en el cronómetro.
    - >24 h – Luchamos con fuego y correo electrónico.
    - 4–24 h – Coordinación razonable.
    - <4 h – Orquesta bien ensayada, aunque a veces improvisemos jazz.”


### 6.5. Recuperación y continuidad (RC)

- “¿Su organización tiene objetivos de RTO/RPO definidos y probados para sus procesos críticos?
    - No, confiamos en la providencia (y en backups misteriosos).
    - Definidos, pero apenas probados.
    - Definidos y probados al menos anualmente.
    - Definidos, probados y revisados tras cada incidente o ejercicio.”
- “En el último ejercicio de recuperación, ¿qué porcentaje de servicios alcanzó el RTO definido?
    - No hacemos ejercicios.
    - Menos de la mitad.
    - Entre la mitad y tres cuartas partes.
    - La mayoría o todos (y lo podemos demostrar con datos).”


### 6.6. Cadena de suministro (GV.SC)

- “¿Qué porcentaje de sus proveedores críticos tiene requisitos de ciberseguridad definidos en contrato (incluyendo notificación de incidentes, SBOM, auditorías, etc.)?
    - ~0% – La confianza es nuestro único control.
    - 1–25% – Empezamos por los contratos más grandes.
    - 26–75% – Los críticos están bastante bien cubiertos.
    - >75% – Si no hay cláusulas de ciber, no hay contrato.”
- “¿Con qué frecuencia revisa la seguridad de sus proveedores críticos (evidencias, auditorías, evaluaciones técnicas)?
    - Nunca – suponemos que todo va estupendamente.
    - Solo al inicio de la relación.
    - Cada 2–3 años o tras incidentes.
    - Al menos anual, con métricas y seguimiento.”

***



<div align="center">⁂</div>

[^1]: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf

[^2]: https://www.blumira.com/blog/nist-cybersecurity-framework-2.0-2025-guide-for-mid-market-companies

[^3]: https://portal.mineco.gob.es/RecursosArticulo/mineco/ministerio/ficheros/210204_Digital_Spain_2025.pdf

[^4]: https://digital.gob.es/en/comunicacion/notas-prensa/mtdfp/2025/05/2025-05-06_02

[^5]: https://www.nist.gov/news-events/news/2026/03/nist-releases-two-new-csf-20-quick-start-guides

[^6]: https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8596.iprd.pdf

[^7]: https://www.saltycloud.com/blog/how-to-implement-nist-csf/

[^8]: https://cognisys.co.uk/security-compliance/nist-csf-2-0/

[^9]: https://securityscorecard.com/resources/learning-center/9-cybersecurity-metrics-kpis-to-track/

[^10]: https://www.nist.gov/cyberframework

[^11]: https://safe.security/resources/insights/nist-cybersecurity-framework/

[^12]: https://www.sgs.com/en-th/news/2025/04/nist-cybersecurity-framework

[^13]: https://industrialcyber.co/nist/nist-releases-updated-csf-2-0-quick-start-guide-to-strengthen-cyber-erm-and-workforce-integration/

[^14]: https://www.nist.gov/document/csf-20-implementations-pdf

[^15]: https://blog.isecauditors.com/en/how-to-adapt-an-existing-security-program-to-the-nist-cybersecurity-framework-2-0

