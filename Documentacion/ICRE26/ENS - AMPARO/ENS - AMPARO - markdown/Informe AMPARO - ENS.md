
# Informe AMPARO - ENS.

AMPARO‑ENS es, en esencia, el intento del Estado de poner orden en el caos métrico de la ciberseguridad pública española: que todos midan lo mismo, de la misma forma, al mismo tiempo, y que esos números sirvan tanto para certificar, como para gobernar y para anticipar riesgos.[^1][^2][^3]

Desde 2025, el giro no ha sido tanto añadir “otra herramienta más”, sino convertir el tándem INES‑AMPARO en un verdadero sistema nacional de indicadores, alineado con el Real Decreto 311/2022 y las guías de métricas del CCN‑STIC, aprovechable por administraciones y por el sector privado crítico que les presta servicios.[^4][^2][^3][^5][^1]

A partir de ahí, vayamos por partes.

### 1. Qué es AMPARO dentro del ecosistema ENS

El CCN sitúa AMPARO como una de las herramientas de Gobernanza de la Ciberseguridad Nacional, junto con INES y PILAR, orientada a facilitar todo el ciclo de adecuación, implantación, auditoría y certificación del ENS.[^6][^7][^1]

INES se usa para la recogida anual de información y el análisis de indicadores sobre el estado de la seguridad; AMPARO es el entorno de gestión donde esa información se convierte en plan de adecuación, declaración de aplicabilidad, evidencias y documentación de cumplimiento.[^7][^2][^3]

La actualización de junio de 2025 del CCN no fue cosmética: se renovó la plataforma INES‑AMPARO para optimizar su usabilidad y facilitar tanto la conformidad con el ENS como la generación de la información necesaria para el Informe Nacional del Estado de Seguridad.  Esa información se apoya explícitamente en el sistema de métricas e indicadores definido en la guía CCN‑STIC‑815 y vinculado al Informe Nacional del Estado de la Seguridad (CCN‑STIC‑824).[^8][^2][^5][^9]

En resumen: AMPARO es el “orquestador” operativo de la métrica ENS. INES mide, AMPARO gobierna, y las guías CCN‑STIC dan la partitura.

### 2. El marco ENS y el lugar de los indicadores

El ENS, actualizado por el Real Decreto 311/2022, persigue alinear la seguridad del sector público con el nuevo contexto estratégico y normativo, reforzando capacidades frente a ciberamenazas y promoviendo la vigilancia continua.  En esa vigilancia continua, el sistema de métricas deja de ser un apéndice burocrático para convertirse en requisito de auditoría y certificación, con referencia expresa a la guía CCN‑STIC‑815 “Sistema de Métricas e Indicadores” y a la CCN‑STIC‑824 sobre el Informe Nacional del Estado de la Seguridad.[^10][^5][^9][^4]

El ENS exige además la realización de un informe de estado de seguridad (art. 12), obligatorio también para entidades privadas que presten servicios al sector público o gestionen sistemas clasificados.  Ese informe se construye, precisamente, con la información consolidada en INES y gobernada en AMPARO.[^2][^3]

De esta forma, la métrica ENS pasa a cumplir, simultáneamente, cuatro funciones:

1. Soportar la certificación y verificación de cumplimiento.
2. Alimentar la supervisión centralizada del CCN y del Informe Nacional.
3. Servir de cuadro de mando comparativo (benchmark) para cada organización frente a su colectivo.
4. Actuar como input cuantitativo para la planificación de medidas, presupuestos y priorización de riesgos.

AMPARO es el instrumento que permite que ese ciclo cierre y no se quede en una colección dispersa de excels bienintencionados.[^6][^1][^2]

### 3. Tipología de indicadores AMPARO‑ENS (visión funcional)

Aunque los detalles exhaustivos están en la guía CCN‑STIC‑815, la arquitectura de métricas que subyace a INES‑AMPARO y al ENS se organiza, de facto, en varias familias de indicadores que se reflejan en los cuadros de mando de INES y en la documentación gestionada por AMPARO.[^5][^9][^2]

Podemos agruparlos, a efectos de gobernanza nacional, en cuatro bloques grandes:

1. Indicadores de madurez y cumplimiento ENS.
2. Indicadores de riesgo y protección (incluido Zero Trust y criptografía).
3. Indicadores de operación, incidentes y ciberresiliencia.
4. Indicadores de gestión, recursos y cultura.

#### 3.1. Indicadores de madurez y cumplimiento ENS

La guía CCN‑STIC‑815 establece un sistema de métricas e indicadores ligado a las medidas del Anexo II del ENS y a los perfiles de cumplimiento, que sirve de referencia tanto para las auditorías (CCN‑STIC‑808, 824) como para la preparación de la Declaración de Aplicabilidad.[^9][^5][^6]

En la práctica, AMPARO estructura y explota indicadores como:

– Porcentaje de medidas ENS implementadas por categoría (Organización, Operación, Protección, Prevención, Detección, Respuesta, Recuperación, etc.), ponderadas por criticidad del sistema.[^5][^6]
– Nivel de adecuación al Perfil de Cumplimiento Específico (PCE) asociado al sistema, apalancando la metodología μCeENS para sistematizar requisitos y evidencias.[^7][^6]
– Grado de cobertura de documentación obligatoria ENS (políticas, procedimientos, planes de continuidad, planes de respuesta, análisis de riesgos), apoyándose en plantillas predefinidas incluidas en INES‑AMPARO.[^2][^6]
– Estado de certificación ENS por sistema o por entidad, medido como porcentaje de sistemas certificados, en proceso, o pendientes, lo que se integra en el análisis del Informe Nacional del Estado de Seguridad.[^11][^2][^5]

La novedad desde 2025 no está tanto en el tipo de indicador como en su explotación: INES presenta cuadros de mando donde cada organización puede comparar sus indicadores clave con la mediana de otras entidades de su colectivo y año, apoyando una gobernanza basada en benchmarking interno de país.[^3][^2]

#### 3.2. Indicadores de riesgo, Zero Trust y criptografía

Aunque el ENS sigue anclado en un análisis clásico de riesgos (activo – amenaza – probabilidad – impacto), las propias FAQ del esquema subrayan que la metodología se apoya en herramientas de gobernanza como INES‑AMPARO y en herramientas de análisis como PILAR para determinar valor del riesgo, categorización de sistemas y rigurosidad de medidas como el doble factor de autenticación.[^1][^6]

En este contexto, los indicadores AMPARO‑ENS empiezan a incorporar, de manera más explícita desde 2025, dimensiones alineadas con prácticas de Zero Trust y protección criptográfica avanzada:

– Porcentaje de accesos protegidos por autenticación multifactor, en línea con la insistencia del ENS en el uso de MFA y con los marcos de confianza cero de fabricantes como Microsoft y proveedores de referencia, que enfatizan controles de identidad y acceso granulares.[^12][^13][^6]
– Grado de segmentación de red y uso de microsegmentación o controles de acceso basados en contexto, en sintonía con la arquitectura Zero Trust que “elimina el concepto de confianza implícita en la red”.[^13][^14][^12]
– Estado de transición hacia criptografía robusta frente a amenazas emergentes (incluida la post‑cuántica), recogiendo líneas recomendadas en servicios especializados de análisis de riesgo cuántico que ponen el foco en la adopción gradual de criptografía post‑cuántica y el cumplimiento con normativas europeas y españolas.[^15][^4]
– Métricas de exposición residual, donde el análisis de riesgos ENS, automatizado en parte por PILAR y gobernado por AMPARO, permite cuantificar el riesgo agregado por categorías de servicio y tipo de información (incluyendo datos personales y servicios esenciales).[^4][^6][^1]

Estas métricas, aún no empaquetadas en un único acrónimo glamuroso, convergen claramente hacia un modelo de confianza cero estadísticamente observable: el ENS, empujado por el CCN y por la presión regulatoria europea, se mueve de la “lista de controles” al “perfil de riesgo medido y monitorizado”.

#### 3.3. Indicadores de operación, incidentes y ciberresiliencia

La ciberresiliencia, entendida como la capacidad de una organización para anticipar, resistir y recuperarse de incidentes, se ha posicionado como concepto central en la literatura y en el debate público español, tanto en think tanks como en foros “CISO meets CEO”.[^16][^17][^18]

El ENS, a través de sus guías CCN‑STIC (por ejemplo, la 817 de gestión de ciberincidentes, que remite de nuevo a la 815 de métricas e indicadores), exige el establecimiento de sistemas de detección, reacción y registro de incidentes, sobre los que las organizaciones deben remitir anualmente al CCN‑CERT un resumen con datos esenciales.[^19][^9]

De ahí se derivan indicadores típicos que AMPARO ayuda a consolidar y que encajan bien en una visión nacional:

– Volumen de incidentes por categoría (confidencialidad, integridad, disponibilidad, fraude, etc.) y por nivel de impacto.[^19][^9]
– Tiempo medio de detección (MTTD), tiempo medio de respuesta (MTTR) y tiempo de recuperación de servicios críticos.[^16][^9]
– Porcentaje de incidentes que atraviesan varias capas de defensa (indicador indirecto de madurez de defensa en profundidad y de la eficacia de modelos Zero Trust).[^12][^13][^16]
– Cobertura de monitorización y correlación (capacidad SIEM/SOC), coherente con el énfasis de los marcos de confianza cero en el uso de SIEM para análisis en tiempo real y respuesta temprana.[^13][^4]
– Grado de integración de la ciberseguridad en los mecanismos generales de gestión de crisis y continuidad de negocio, aspecto que los análisis sobre ciberresiliencia señalan como imprescindible para pasar de un enfoque puramente técnico a otro estratégico.[^4][^16]

Estos indicadores alimentan no solo el Informe Nacional del Estado de la Seguridad, sino también la conversación entre CISO y alta dirección, como reflejan informes industriales sobre el estado de la ciberseguridad en España que subrayan la necesidad de integrar seguridad y estrategia empresarial, gestionar la resiliencia y afrontar retos de talento y presupuesto.[^20][^21]

#### 3.4. Indicadores de gestión, recursos y cultura

Los cuadros de mando de INES, y el propio discurso ENS, han contribuido a que la métrica deje de ser exclusivamente técnica: entran en juego indicadores sobre gestión, recursos y cultura que son críticos para comparar la postura de seguridad a escala nacional.[^3][^2][^4]

Entre ellos destacan:

– Presupuesto dedicado a ciberseguridad en relación con el tamaño de la organización, la criticidad de los servicios y la categoría ENS de los sistemas.[^21][^20]
– Dotación y cualificación de recursos humanos, especialmente en perfiles de CISO, SOC, arquitectos de seguridad y especialistas en cumplimiento ENS/NIS2.[^20][^21]
– Grado de integración de la ciberseguridad en la gobernanza corporativa: participación del CISO en comités de riesgo, alineamiento con gestión de riesgos no cibernéticos, presencia en ejercicios y simulacros.[^17][^16][^20]
– Nivel de concienciación y formación de usuarios finales, medido a través de campañas, indicadores de phishing simulado, o métricas análogas recogidas en los informes anuales.[^21][^20]
– Madurez de procesos de gestión de riesgos, incluyendo el uso sistemático de metodologías como PILAR y la formalización de apetito de riesgo y criterios de priorización.[^6][^16][^1]

AMPARO configura y documenta estos aspectos, de manera que la foto ENS de una entidad no es sólo un mapa de firewalls y cifrados, sino también un retrato –a veces poco favorecedor– de su cultura de riesgo.

### 4. Aplicación territorial: del indicador al mapa nacional

Una de las consecuencias más interesantes del modelo INES‑AMPARO es que las organizaciones pueden ver sus indicadores comparados con la mediana de otras del mismo colectivo y año, tanto para administraciones como para entidades privadas obligadas.[^2][^3]

Esto abre la puerta a una cartografía territorial de la ciberseguridad española:

– Es posible derivar, desde el Informe Nacional del Estado de Seguridad (CCN‑STIC‑824) y las remisiones anuales de datos esenciales, mapas de cumplimiento por comunidad autónoma, tipo de administración (local, autonómica, estatal), sector (sanidad, educación, justicia, hacienda, etc.) y tamaño de entidad.[^9][^11][^5]
– El ENS actualizado y las estadísticas de certificación reflejan un claro incremento en el número de organizaciones certificadas, con cifras como las 1.119 nuevas certificaciones en 2025, que evidencian una adopción masiva del esquema como columna vertebral de la confianza digital.[^11][^4]
– Las herramientas μCeENS e INES‑AMPARO permiten, además, gestionar de forma centralizada la documentación, la autoevaluación y las evidencias de cumplimiento, reduciendo esfuerzos manuales y tiempos de respuesta, lo que favorece la extensión territorial del modelo incluso a entidades de menor tamaño.[^22][^7][^2]

Desde la perspectiva actuarial del riesgo, esto significa que España está construyendo –con todas sus imperfecciones– una base de datos estructurada que vincula medidas de seguridad, incidentes, contexto organizativo y territorio.  Es, para un teórico del riesgo, el equivalente cibernético de un padrón estadístico bien alimentado.[^5][^9][^2]

### 5. Comparativa internacional: ENS‑AMPARO frente a otros marcos de indicadores

Para situar AMPARO‑ENS en el mundo conviene compararlo, al menos conceptualmente, con tres grandes referencias: NIST CSF en Estados Unidos, los marcos ISO/IEC 2700x y las obligaciones europeas ligadas a NIS2 y a la regulación del ciberseguro.

– NIST CSF propone funciones, categorías y subcategorías, dejando a cada organización libertad para definir sus propios indicadores, aunque existan catálogos de métricas ampliamente difundidos. ENS, en cambio, combina marco normativo con sistema de indicadores normalizado y herramienta estatal de recogida y análisis (INES‑AMPARO).[^4][^2][^5]
– ISO/IEC 27001/27004 describen qué medir y cómo evaluar la eficacia de los controles, pero no proporcionan una plataforma nacional común ni un informe país coordinado. ENS añade esa capa de centralización, apoyada en el CCN, el CCN‑CERT y las guías STIC.[^9][^5][^4]
– NIS2 exige a los Estados miembros fortalecer la supervisión, la notificación de incidentes y la resiliencia de servicios esenciales y proveedores clave. ENS, con INES‑AMPARO, ofrece a España un mecanismo operativo concreto para cumplir y demostrar esa supervisión, incluyendo a entidades privadas que prestan servicios al sector público.[^3][^11][^4]

La otra diferencia importante está en la visión de ciberresiliencia: los análisis estratégicos en España subrayan que la ciberresiliencia debe integrarse en la gestión global de riesgos, con CISO participando en comités y simulacros junto a otros responsables de riesgo, y que las métricas deben reflejar esa integración.  En muchos países, esa conexión aún se mantiene en un plano más discursivo que instrumental.[^17][^16]

Paradójicamente, lo que para algunos parece burocracia (informes, tablas, plantillas) es, visto fríamente, una ventaja competitiva: España ha institucionalizado un “idioma común” de indicadores de ciberseguridad para el sector público y su ecosistema proveedor, mientras otros entornos se limitan a recomendaciones voluntarias y catálogos de buenas prácticas.[^1][^2][^4]

### 6. Tendencias desde 2025: hacia una gobernanza métrica madura

Desde 2025 se observan varias tendencias claras en el universo AMPARO‑ENS y su sistema de indicadores:

1. **Extensión al sector privado crítico.** La obligación de rellenar INES para entidades privadas que prestan servicios al sector público amplía la base de datos de indicadores y difumina la frontera entre “lo público” y “lo estrictamente privado” en materia de seguridad.[^2][^3]
2. **Consolidación de la métrica como requisito de certificación.** Las referencias explícitas a las guías de métricas (CCN‑STIC‑815) y al Informe Nacional (824) en la documentación de auditoría ENS refuerzan la idea de que no hay certificación sin indicadores sólidos y comparables.[^5][^9]
3. **Mayor énfasis en resiliencia y continuidad.** La producción de análisis y eventos en torno a la ciberresiliencia, la figura del CISO y su rol en el tablero global de riesgos enfatiza métricas de continuidad de negocio, tiempos de recuperación y grado de integración en la gestión de crisis.[^18][^16][^17]
4. **Alineamiento con arquitecturas Zero Trust.** Las descripciones de Zero Trust por parte de fabricantes y proveedores líderes subrayan métricas de autenticación fuerte, segmentación, análisis continuo y uso intensivo de SIEM; estos elementos se alinean progresivamente con las exigencias ENS y se traducen en indicadores operativos en los cuadros de mando.[^14][^12][^13][^6]
5. **Profesionalización de la analítica de riesgo cuántico.** Servicios especializados en análisis de riesgos cuánticos para empresas, referenciados en el contexto español, muestran una incipiente transición hacia métricas de adopción de criptografía post‑cuántica y exposición a amenazas futuras, que previsiblemente acabarán permeando los ejercicios ENS.[^15][^4]
6. **Crecimiento cuantitativo y cualitativo de certificaciones ENS.** El ritmo de nuevas certificaciones, con cifras destacadas como las de 2025, indica que el ENS no sólo se despliega, sino que se vuelve la norma de facto para la confianza digital en la relación ciudadano‑Estado y en la cadena de suministro tecnológica.[^11][^4]

### 7. Propuesta de lectura y uso de los indicadores AMPARO‑ENS

Si se mira AMPARO‑ENS con la mirada un poco cansada del CISO veterano o del teórico del riesgo, lo que se ve no es un formulario más, sino una oportunidad incómoda: por primera vez, un país dispone de un marco normativo, un sistema de métricas formalizado y una plataforma centralizada que permiten:

– Medir y comparar madurez ENS de manera homogénea.[^3][^2][^5]
– Vincular medidas técnicas (MFA, segmentación, cifrado, SIEM) con resultados operativos (incidentes, tiempos de respuesta, continuidad) y con variables organizativas (presupuesto, recursos, cultura).[^16][^20][^13][^6]
– Analizar la ciberresiliencia no como una metáfora, sino como una variable que se expresa en indicadores observables y comparables entre territorios y sectores.[^16][^9][^11]
– Integrar, gradualmente, nuevas dimensiones de riesgo (por ejemplo, la amenaza cuántica) en un sistema métrico ya aceptado por administraciones y proveedores críticos.[^15][^4]

El reto real para los próximos años no será tanto diseñar nuevos indicadores como resistir la tentación de pervertir los existentes: evitar que la métrica se convierta en un juego de maquillaje, que el benchmarking derive en un concurso de vanidades y que la gobernanza se reduzca a perseguir colores verdes en un dashboard, mientras la superficie de ataque crece silenciosa.

AMPARO‑ENS ofrece, en definitiva, un armazón sólido para una gobernanza basada en datos, comparables y auditables, con aplicación territorial completa en España y alineamiento creciente con las grandes corrientes internacionales de Zero Trust, ciberresiliencia y regulación del riesgo digital.  Que lo usemos para construir resiliencia o para escribir informes complacientes dependerá, como casi siempre, menos de la criptografía y más de la voluntad política y la ética profesional.[^12][^13][^1][^4][^16][^2][^5]

<span style="display:none">[^23][^24][^25][^26][^27][^28]</span>

<div align="center">⁂</div>

[^1]: https://ens.ccn.cni.es/es/

[^2]: https://ingertec.com/informe-ines-obligatorio-en-empresas-privadas/

[^3]: https://www.govertis.com/entidades-privadas-deben-comunicar-informe-ines

[^4]: https://portal.mineco.gob.es/es-es/ministerio/estrategias/Paginas/Esquema_Nacional_de_Seguridad.aspx

[^5]: https://www.adokcertificacion.com/wp-content/uploads/2023/04/AUDITORIA-Y-CERTIFICACION-ENS.pdf

[^6]: https://ens.ccn.cni.es/es/que-es-el-ens/faq

[^7]: https://ens.ccn.cni.es/es/conformidad/microceens

[^8]: https://www.redseguridad.com/actualidad/organismos-ciberseguridad/actualizadas-las-soluciones-del-ccn-ines-y-amparo-para-optimizar-la-experiencia-de-los-usuarios_20250617.html

[^9]: https://www.aec.es/wp-media/uploads/DPD-00266.SEG-GUI-004-CCN-STIC-817_Gestion_de_Ciberincidentes_ENS.pdf

[^10]: https://www.odilo.es/ens-actualizado-ciberseguridad-y-preservacion-digital/

[^11]: https://www.neotica.net/concienciacion-en-ciberseguridad/el-ens-como-columna-vertebral-de-la-confianza-digital-guia-completa-y-actualidad/

[^12]: https://www.paloaltonetworks.es/cyberpedia/what-is-a-zero-trust-architecture

[^13]: https://www.microsoft.com/es-es/security/business/security-101/what-is-zero-trust-architecture

[^14]: https://www.trendmicro.com/es_es/what-is/what-is-zero-trust/zero-trust-architecture.html

[^15]: https://inza.blog/category/esquema-nacional-de-seguridad-ens/

[^16]: https://www.realinstitutoelcano.org/analisis/la-ciberresiliencia-entre-la-ciberseguridad-y-la-resiliencia/

[^17]: https://cyberlideria.es/event/ciso-meets-ceo/

[^18]: https://www.youtube.com/watch?v=WZa9s1yJESU

[^19]: https://actumforensepress.es/archivos/guias-esenciales-del-ccn-cert-de-utilidad-en-investigacion-criminologica-y-forense/

[^20]: https://www.deloitte.com/es/es/services/consulting/research/estado-ciberseguridad.html

[^21]: https://ptedisruptive.es/wp-content/uploads/2024/12/INFORME-DE-SITUACION_CIBERSEGURIDAD_2024.pdf

[^22]: https://www.camerfirma.com/esquema-nacional-de-seguridad/

[^23]: https://cecocib.es/informes

[^24]: https://www.mintur.gob.es/Publicaciones/Publicacionesperiodicas/EconomiaIndustrial/RevistaEconomiaIndustrial/410/MIGUEL A. AMUTIO GÓMEZ.pdf

[^25]: https://es.linkedin.com/posts/ccncert_ccn-in%C3%A9s-amparo-activity-7340341338686586880-HnMS

[^26]: https://www.brainscape.com/flashcards/herramientas-ccn-cert-12777492/packs/21237743

[^27]: https://ens.ccn.cni.es/gl/inicio

[^28]: https://fiscalizacion.es/wp-content/uploads/2024/07/ccn-stic-881-adecuacion-al-ens-para-universidades_.pdf

