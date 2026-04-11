
# Informe CRA (Cyber Resilience Act).

El CRA no trae una “tabla periódica” de KPIs ya cocinada, pero sí obliga a los Estados y a los fabricantes a medir sistemáticamente el ciclo de vida de la ciberseguridad de los productos con elementos digitales y a conectarlo con sus estrategias nacionales (en España, la Estrategia Nacional de Ciberseguridad, NIS2 y el nuevo marco de gobernanza).[^1][^2][^3][^4]

## 1. Qué pide realmente el CRA (y qué no)

El Cyber Resilience Act es un Reglamento directamente aplicable que establece requisitos esenciales de ciberseguridad para “productos con elementos digitales”, desde routers hasta software embebido, pasando por IoT industrial y plataformas.  No enumera KPIs detallados, pero sí define obligaciones mensurables para fabricantes, importadores y distribuidores: gestión de vulnerabilidades, actualizaciones de seguridad, reporte de incidentes, documentación técnica y evaluación de conformidad.[^2][^3][^1]

A partir de 11‑09‑2026, los fabricantes deberán notificar vulnerabilidades explotadas activamente y los incidentes graves en un plazo muy corto (24 horas en los borradores de ejecución), a través de una plataforma única de reporte que gestionará ENISA.  El propio diseño de esta plataforma implica indicadores de volumen, rapidez y calidad del reporte, así como de coordinación entre autoridades de vigilancia del mercado.[^5][^6][^7]

El CRA se apoya en esquemas de certificación existentes, en particular el esquema EUCC (Common Criteria europeo) como vía de “presunción de conformidad”, que a su vez arrastra métricas clásicas de evaluación (niveles de seguridad, familias de requisitos, defectos residuales, etc.).  En paralelo, el documento estratégico 2025‑2027 de ENISA introduce indicadores para medir su apoyo a la implementación del CRA, lo que en la práctica acaba siendo un esqueleto de KPIs a nivel de Unión.[^8][^9][^7][^10][^11][^3]

## 2. Capas de indicadores CRA: desde Bruselas al territorio

Para poder hablar de “indicadores CRA” con sentido, conviene distinguir tres planos que se cruzan:

1. Plano regulatorio‑europeo:
Aquí viven las métricas de implementación institucional: existencia y operación de la plataforma de notificación, número de esquemas de certificación EU aplicados al CRA, volumen de autoridades nacionales activas, grado de satisfacción de los Estados miembros con el apoyo de ENISA.  No miden la ciberseguridad de una pyme en León, pero sí el andamiaje que debería hacer posible esa mejora.[^9][^7][^11]
2. Plano nacional‑estratégico:
Los Estados miembros articulan el CRA con NIS2, el Reglamento de certificación y sus estrategias nacionales.  En España, el “Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad” es la pieza que integra NIS2 y la Directiva de Resiliencia de Entidades Críticas, y que crea el Centro Nacional de Ciberseguridad (CNCS) como autoridad pivotal.  El Gobierno, además, ha aprobado un paquete de 1.157 millones de euros para reforzar capacidades de ciberseguridad y ciberdefensa, con objetivos expresos sobre servicios críticos, plataformas de auditoría automatizada y un SOC 5G nacional.[^12][^13][^14][^11][^15][^4][^1][^2]
3. Plano operativo‑producto/sector:
Aquí están los indicadores que de verdad duelen o tranquilizan: porcentaje de productos “CRA‑conformes”, tiempos de parcheo, tasa de vulnerabilidades explotadas, frecuencia de incidentes, cobertura de seguros, capacidad de recuperación, etc.  No son invento de marketing; aparecen, con distintos sabores, en guías técnicas de ENISA, en informes industriales serios y en revisiones internacionales del grado de resiliencia de sectores como el financiero.[^16][^17][^10][^11][^18][^9]

La tarea para España (y para cualquier Estado miembro) es bajar el CRA de la estratosfera regulatoria a esos indicadores operativos, sin perder de vista la comparabilidad internacional ni la coherencia con NIS2 y la Estrategia Nacional de Ciberseguridad.[^14][^11][^4][^1][^12]

## 3. Núcleo duro de métricas CRA a nivel país

A partir de lo que el CRA exige, de lo que ENISA propone medir y de lo que los informes internacionales recomiendan como métricas para gobiernos, emerge un conjunto de indicadores que, si uno fuera un Ministerio diligente, pondría en el cuadro de mando nacional.

### 3.1. Superficie de cumplimiento y certificación

La primera familia es casi de higiene: cuánto del ecosistema de productos digitales del país está, al menos en teoría, alineado con CRA o cubierto por esquemas equivalentes.

- Proporción de productos con elementos digitales en el mercado nacional que declaran cumplimiento CRA (por número de modelos y por cuota de mercado).[^3][^18][^1][^2]
- Número de fabricantes con sede o presencia en el país registrados como sujetos a CRA, y porcentaje de ellos con procesos de gestión de vulnerabilidades certificados o auditados.[^18][^1][^2][^3]
- Número de certificaciones EUCC emitidas para productos relevantes en el territorio y su distribución por nivel de garantía.[^10][^11][^8][^3]
- Porcentaje de entidades críticas (NIS2) que utilizan exclusivamente productos CRA‑conformes o certificados en sus segmentos más sensibles (redes OT, IoT industrial, infraestructuras de comunicaciones).[^11][^1][^12][^14]

Estas métricas, en España, deberían cruzarse con los sectores bajo la futura Ley de Coordinación y Gobernanza de la Ciberseguridad y con la propia Estrategia Nacional de Ciberseguridad, que ya prioriza la protección de infraestructuras críticas y servicios esenciales.[^15][^4][^12][^14]

### 3.2. Gestión de vulnerabilidades y ciclo de parcheo

Si el CRA tiene un corazón, está hecho de CVEs, parches y plazos.

- Tiempo medio de publicación de un parche desde que se identifica una vulnerabilidad explotada activamente en un producto sujeto a CRA (time to patch, TTP), desglosado por fabricante y categoría de producto.[^1][^2][^3][^18]
- Proporción de vulnerabilidades explotadas activamente en productos con elementos digitales usados en el país que tienen más de un año (las “aging vulnerabilities” de los economistas del desastre).[^16]
- Porcentaje de instalaciones en el territorio que han aplicado el parche dentro de un plazo objetivo (por ejemplo, 30 días para vulnerabilidades críticas), tanto en sector público como privado.[^13][^11][^16]
- Número de vulnerabilidades notificadas a través de la plataforma CRA y su distribución por criticidad, tiempo de mitigación y reincidencia.[^6][^7][^11][^3]

Zurich Insurance, en su propuesta de métricas de ciberresiliencia para gobiernos, destaca precisamente el peso de vulnerabilidades antiguas como proxy de incapacidad sistémica de remediación; el CRA, al obligar a la gestión continua y al reporte, convierte esa señal en un dato duro disponible para las autoridades.[^11][^16]

### 3.3. Incidentes, notificación y capacidad de respuesta

Una regulación que impone notificación temprana genera, por necesidad, un sistema de indicadores sobre incidentes.

- Número de incidentes significativos asociados a productos cubiertos por CRA, por año y por sector, con desagregación de impacto (servicio interrumpido, datos comprometidos, daños físicos, etc.).[^2][^5][^6][^1][^11]
- Porcentaje de incidentes notificados dentro de las 24 horas desde su detección, y porcentaje de informes completos entregados en los plazos subsiguientes.[^7][^5][^6][^11]
- Tiempo medio de detección (MTTD) y de contención (MTTC) de incidentes vinculados a productos CRA, tanto en operadores esenciales como en administraciones públicas.[^19][^17][^13]
- Tasa de “near misses” o cuasi‑incidentes detectados gracias a capacidades de monitorización, simulaciones o pruebas de intrusión, como indicador indirecto de madurez defensiva.[^17][^19][^9][^16]

El énfasis en la rapidez de notificación casa bien con la evolución regulatoria europea y con tendencias fuera de la UE (por ejemplo, el refuerzo de plazos estrictos en otras jurisdicciones), que usan el retraso en el reporte como síntoma de debilidad organizativa.[^20][^9][^2][^11]

### 3.4. Resiliencia económica y de mercado

Los analistas que miran el riesgo con gafas actuariales introducen métricas menos técnicas pero políticamente muy elocuentes.

- Porcentaje de organizaciones con pólizas de ciberseguro o con certificaciones de seguridad reconocidas, segmentado por tamaño y sector.[^17][^16][^11]
- Estimación de pérdidas económicas directas e indirectas por incidentes relacionados con productos CRA (interrupción de negocio, rescates pagados, sanciones regulatorias), como proporción del PIB o del valor añadido sectorial.[^2][^16][^17]
- Gasto público y privado en ciberseguridad como porcentaje del presupuesto TIC, con detalle de inversiones orientadas a cumplimiento CRA (por ejemplo, refactorización de productos, pipelines de desarrollo seguro, herramientas de SBOM).[^13][^18][^11]
- Nivel de concentración de proveedores de productos digitales críticos y grado de dependencia de productos no conformes o de origen extracomunitario sin certificación reconocida.[^10][^3][^16][^2]

La propia revisión por pares del Consejo de Estabilidad Financiera sobre la resiliencia cibernética del sector financiero español subraya que las autoridades han desarrollado buenas prácticas, pero recomienda fortalecer aún más la medición y la vigilancia de riesgos tecnológicos y de terceros, lo cual encaja con el énfasis del CRA en la cadena de valor del producto digital.[^17][^11]

### 3.5. Capacidades institucionales y capital humano

Finalmente, lo que no se mide en hardware se mide en neuronas.

- Capacidad de las autoridades de vigilancia de mercado: número de inspecciones y evaluaciones técnicas realizadas, tiempo medio de tramitación, sanciones impuestas, recursos técnicos disponibles.[^6][^9][^7][^11]
- Grado de implantación de la Estrategia Nacional de Ciberseguridad y del plan estratégico de INCIBE (porcentaje de acciones completadas, alcance de campañas de concienciación, servicios prestados a ciudadanos y pymes).[^4][^15]
- Tamaño y cualificación de la fuerza laboral en ciberseguridad, incluyendo perfiles especializados en desarrollo seguro, ingeniería de producto y análisis de vulnerabilidades.[^9][^4][^11]
- Nivel de satisfacción de los Estados miembros y de las autoridades nacionales con el apoyo de ENISA y la eficacia del marco CRA, que la propia ENISA recoge como indicador de su estrategia.[^7][^9][^11]

España, en su agenda España Digital 2025, sitúa la ciberseguridad como uno de los ejes estratégicos del país y alinea la actividad de INCIBE con estos objetivos, lo que ofrece un marco natural para absorber los indicadores CRA en la planificación nacional.[^15][^4]

## 4. España en el espejo internacional

Desde la óptica comparativa, el CRA funciona como una especie de “GDPR de las cosas”: un estándar de facto que no se limita a la UE, porque fabricantes globales no van a diseñar un producto para Europa y otro, menos seguro, para el resto del planeta sin una buena razón económica.  El nivel de adopción y de exigencia efectiva que muestre España tendrá, por tanto, efectos sobre su posición relativa en ciberresiliencia frente a otros países europeos y frente a grandes actores extracomunitarios.[^21][^3][^2]

En el contexto europeo, la rapidez con la que España está transponiendo NIS2 y creando estructuras como el CNCS indica una voluntad de estar en el pelotón de cabeza, no en la cola.  El refuerzo presupuestario de más de mil millones para ciberseguridad y ciberdefensa refuerza esta impresión y abre la puerta a financiar la infraestructura de medición que los indicadores CRA requieren: sensores, plataformas de agregación, capacidades analíticas.[^12][^14][^13][^11][^15]

Fuera de la UE, el paralelo más cercano son propuestas legislativas que, como el Cyber Security and Resilience Bill del Reino Unido, refuerzan la regulación de infraestructura digital crítica, amplían el perímetro de entidades reguladas y endurecen los requisitos de notificación y control técnico (MFA, segmentación, cifrado, etc.).  Sin embargo, estos marcos no disponen todavía de un equivalente estricto al CRA centrado en productos, lo que convierte a la UE en laboratorio normativo y a indicadores como los descritos en referencia obligada para comparaciones internacionales.[^21][^20][^3][^2]

Si se quisieran construir índices compuestos de “madurez CRA” comparables entre países, sería razonable combinar métricas de cumplimiento y certificación, datos de vulnerabilidades e incidentes y medidas de impacto económico y capacidades institucionales, semejantes a los propuestos por iniciativas europeas de índices de ciberseguridad.  El resultado, bien diseñado, podría informar tanto políticas públicas como decisiones de inversión privada y de aseguradoras.[^22][^11]

## 5. Propuesta de enfoque para un informe CRA nacional‑territorial

Con este contexto, un informe CRA para España con vocación de excelencia podría articularse en tres actos.

Primero, anclar jurídicamente el marco: explicar el CRA, su cronograma, su conexión con NIS2, la Ley de Coordinación y Gobernanza de la Ciberseguridad, la Estrategia Nacional de Ciberseguridad y la agenda España Digital 2025, dejando claro qué obligaciones se traducen en datos observables.[^14][^3][^4][^1][^12][^15][^2]

Segundo, definir el cuadro de mando de indicadores en las cinco familias anteriores, especificando para cada métrica la fuente (plataforma CRA, CNCS, INCIBE, sector financiero, aseguradoras, encuestas empresariales), la periodicidad y las metas deseables a medio plazo.  La gracia, si se quiere mantener un tono mínimamente literario, está en mostrar que cada número cuenta una historia sobre cómo se fabrican, despliegan y rompen los productos digitales en el país.[^18][^16][^6][^13][^9][^10][^11][^17]

Tercero, incorporar una dimensión comparativa internacional, usando tanto datos de ENISA y de otros organismos europeos como revisiones sectoriales (por ejemplo, del FSB para finanzas o de iniciativas de índices de ciberseguridad en la UE), y situar a España en ese mapa, con claridad sobre fortalezas, debilidades y riesgos emergentes.[^22][^9][^11][^17]

<span style="display:none">[^23][^24][^25][^26][^27][^28]</span>

<div align="center">⁂</div>

[^1]: https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act

[^2]: https://www.spglobal.com/market-intelligence/en/news-insights/research/2025/10/europes-cyber-resilience-act-the-gdpr-for-things

[^3]: https://www.scribd.com/document/889312992/ENISA-Cyber-Resilience-Act-CRA-2025

[^4]: https://dig.watch/resource/spains-national-cybersecurity-strategy

[^5]: https://www.taylorwessing.com/en/insights-and-events/insights/2025/11/cyber-resilience-act-overview

[^6]: https://www.cencenelec.eu/media/CEN-CENELEC/Events/Events/2025/2025-04-08_cyber-resilience-act-and-the-horizontal-standards-workshop.pdf

[^7]: https://www.enisa.europa.eu/sites/default/files/2025-02/A Trusted and Cyber Secure Europe - ENISA Strategy - Indicators.pdf

[^8]: https://www.sgs.com/en-es/news/2025/09/safeguards-13125-update-on-developments-relating-to-the-eu-cyber-resilience-act

[^9]: https://www.enisa.europa.eu/sites/default/files/2025-07/A Trusted and Cyber Secure Europe - ENISA Strategy Indicators.pdf

[^10]: https://www.sgs.com/en-ch/news/2025/09/safeguards-13125-update-on-developments-relating-to-the-eu-cyber-resilience-act

[^11]: https://www.scribd.com/document/862976647/ENISA-Single-Programming-Document-2025-2027-Condensed-version

[^12]: https://copla.com/blog/compliance-regulations/nis2-directive-regulations-and-implementation-in-spain/

[^13]: https://digital.gob.es/en/comunicacion/notas-prensa/mtdfp/2025/05/2025-05-06_02

[^14]: https://www.dominios.es/en/informacion-de-interes/noticias/european-nis2-directive-strengthens-cybersecurity-spain-leading

[^15]: https://www.incibe.es/en/incibe/corporate-information/what-we-do

[^16]: https://www.helpnetsecurity.com/2025/10/09/zurich-governments-cyber-resilience-metrics/

[^17]: https://www.fsb.org/2025/11/fsb-recommends-spain-further-enhance-cyber-resilience-of-its-financial-sector-to-address-rising-challenges/

[^18]: https://control-plane.io/posts/beyond-compliance-strategic-cyber-resilience-in-financial-services-under-the-eus-cra/

[^19]: https://securityscorecard.com/resources/learning-center/9-cybersecurity-metrics-kpis-to-track/

[^20]: https://yousign.com/blog/uk-cyber-resilience-act-implementation-checklist-smes

[^21]: https://www.kusari.dev/learning-center/eu-cyber-resilience-act

[^22]: https://d-russia.ru/wp-content/uploads/2024/03/eu_csi_methodological_note_v1-0.pdf

[^23]: https://www.digitaltrustcenter.nl/sites/default/files/2025-10/CRA Gids v2.0 september 2025 UK.pdf

[^24]: https://help.drata.com/en/articles/12150854-nis2-update-what-enisa-s-new-guidance-means-for-you

[^25]: https://www.enisa.europa.eu/sites/default/files/2024-11/enisa_programming_document_2023_2025.pdf

[^26]: https://docbox.etsi.org/Workshop/2025/10_SECURITY_CONFERENCE/6OCTOBER/KEYNOTES/EUROPEANCOMMISSION_JONES-MOURAO.pdf

[^27]: https://www.linkedin.com/pulse/important-kpi-monitor-your-cyber-security-maturity-anil-appayanna

[^28]: https://www.ismsforum.es/ficheros/descargas/the-ciso-and-senior-management1765382437.pdf

