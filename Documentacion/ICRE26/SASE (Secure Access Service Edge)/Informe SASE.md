# Indicadores y métricas SASE (Secure Access Service Edge) para España con comparación internacional (tendencias desde 2025)

## 1. Introducción y contexto

El marco SASE (Secure Access Service Edge) ha pasado en pocos años de ser una “visión” de Gartner a convertirse en el patrón de facto para converger red y seguridad en arquitecturas cloud–first y Zero Trust, en particular a partir del impulso de trabajo híbrido, SaaS masivo y la presión regulatoria (GDPR, NIS2, ENS, etc.).  Desde 2025, el debate ya no es “si” adoptar SASE, sino “cómo medir” su eficacia, tanto a nivel organizativo como a escala país.[^1][^2]

En España, la actualización del Esquema Nacional de Seguridad (ENS) mediante el Real Decreto 311/2022 y su despliegue en el marco del Plan Nacional de Ciberseguridad y España Digital 2026 obligan a disponer de métricas robustas de ciberseguridad, continuidad de negocio y uso seguro del cloud, donde SASE encaja como pieza técnica, pero siempre subordinada al marco ENS y NIS2.  Este informe sintetiza tendencias desde 2025 en indicadores SASE, proponiendo un cuadro de mando aplicable a nivel nacional (sector público y operadores esenciales) y comparándolo con prácticas internacionales.[^3][^4]

## 2. Fundamentos de SASE y su relación con Zero Trust y NIS2/ENS

SASE se define como una arquitectura cloud–nativa que unifica funciones de red (fundamentalmente SD‑WAN) con capacidades de seguridad como SWG, CASB, FWaaS y ZTNA, entregadas como servicio desde una red global de puntos de presencia.  La esencia del modelo es acercar la política de seguridad y la inspección al borde, donde están usuarios, dispositivos y aplicaciones, sustituyendo el perímetro clásico de centro de datos.[^5][^6][^1]

Las guías europeas de Zero Trust (NIST, CISA, ENISA) insisten en métricas de verificación continua, comportamiento y gestión del riesgo (identidad, postura, contexto, señales compartidas, indicadores de compromiso, respuesta orquestada), que son directamente trasladables a un despliegue SASE bien instrumentado.  NIS2, por su parte, exige medidas de gestión de riesgos, controles de acceso fuertes, monitorización continua, métricas de eficacia de seguridad y planes de continuidad, lo que favorece arquitecturas SASE/SSE como mecanismo para aplicar políticas homogéneas, registrar accesos y consolidar evidencias de cumplimiento.[^7][^8][^9][^3]

En España, el ENS actualizado establece principios básicos, requisitos mínimos y medidas de protección comunes a todas las AAPP y proveedores tecnológicos, incorporando explícitamente medidas para servicios cloud, cadena de suministro, interconexiones y vigilancia continua.  La arquitectura SASE, adecuadamente gobernada, permite instrumentar muchas de estas medidas (control de acceso, cifrado, monitorización, DLP, segmentación, etc.) y, sobre todo, dotar de telemetría homogénea para alimentar los informes de estado de la seguridad que la Comisión Sectorial de Administración Electrónica debe consolidar a partir de las “principales variables de ciberseguridad”.[^4][^10]

## 3. Panorama de adopción SASE y SSE (2025–2026)

Los informes de mercado coinciden en que el segmento SASE crece por encima del 20% anual, impulsado por cloud, trabajo híbrido, Zero Trust y exigencias regulatorias.  Estimaciones recientes sitúan el mercado global SASE en torno a 15–16 mil millones de dólares en 2025, con previsiones de 39–45 mil millones hacia 2030–2031, con especial peso de Norteamérica pero con crecimiento acelerado en Europa por presión de NIS2 y GDPR.[^11][^12][^2][^13]

Informes específicos sobre acceso seguro indican que solo alrededor de un 8% de las organizaciones declara tener SASE completamente desplegado, aunque más del 80% está evaluando o planificando su adopción, con SD‑WAN, ZTNA, SWG y CASB como componentes prioritarios.  Los estudios de adopción SSE para 2025 muestran cifras similares: cerca del 79% de las organizaciones planea implantar SSE en 24 meses y un 62% considera SASE muy importante para su estrategia, con fuerte preferencia (61%) por soluciones single‑vendor que unifican SSE y SD‑WAN.[^14][^15][^16][^17]

En el contexto español y europeo, informes sectoriales señalan la convergencia entre redes y seguridad (SD‑WAN seguro, SASE) como uno de los principales motores de inversión en seguridad de red, especialmente en organizaciones con infraestructuras distribuidas y usuarios remotos.  La propia comunidad de ciberseguridad española (INCIBE, eventos ASLAN, iniciativas de operadoras y fabricantes) presenta SASE como solución clave para gestionar la seguridad en infraestructuras híbridas y multicloud, con crecimiento significativo de despliegues unificados de un solo fabricante hasta 2025.[^18][^19][^20]

## 4. De los KPIs clásicos de ciberseguridad a los indicadores específicos SASE

Los marcos de métricas clásicas en ciberseguridad (MTTD, MTTR, tasa de falsos positivos, ritmo de parcheo, activos con monitorización, usuarios con MFA, etc.) siguen siendo imprescindibles, pero resultan insuficientes para capturar la naturaleza distribuida, identity–centric y cloud–native de SASE.  Lo que cambia no es el amor por las métricas, sino el objeto medido: ya no se trata solo del “castillo y el foso”, sino de medir un enjambre de perímetros efímeros.[^21][^22][^23]

En la literatura técnica y en guías de fabricantes y laboratorios de pruebas aparecen cuatro grandes familias de indicadores SASE a partir de 2024–2025:

- **Métricas de rendimiento de red y experiencia digital (QoS/QoE).** Latencias extremo a extremo, jitter, pérdida de paquetes, tiempos de establecimiento de sesión, disponibilidad de PoPs, calidad de experiencia por tipo de tráfico (voz, vídeo, transaccional).[^24][^25][^26][^27]
- **Métricas de seguridad y Zero Trust.** Tasa de autenticación satisfactoria, latencia de decisión de política, efectividad de ZTNA (intentos de acceso bloqueados conforme a política), volumen y severidad de eventos, impacto de las funciones de seguridad en el rendimiento (TLS inspection, DLP, sandboxing, etc.).[^28][^29]
- **Métricas de gobierno, cumplimiento y risk management.** Coherencia de políticas, incidentes de violación de política y uso de servicios no conformes (“shadow IT”), evidencias de cumplimiento ENS/NIS2 (registros de acceso, cifrado, segmentación), estado de la cadena de suministro y terceros.[^8][^30][^31]
- **Métricas de adopción, satisfacción de usuario y valor de negocio.** Niveles de experiencia de usuario, adopción de acceso directo a SaaS sin VPN, reducción de tiempo de provisión de sedes y usuarios, consolidación de herramientas, reducción del coste operativo y de incidencias, impacto en continuidad de negocio.[^32][^14][^24]

La convergencia SASE/SRE ha introducido también el lenguaje de SLIs/SLOs en este ámbito: tasas de autenticación, latencias de decisión de política y de establecimiento de sesión, latencia a PoPs, con objetivos explícitos (por ejemplo, 99,9% de decisiones de política por debajo de 300 ms).[^28]

## 5. Categorías de indicadores SASE: definición y ejemplos

### 5.1. Métricas de rendimiento de red y QoE

Los estudios de pruebas de rendimiento y whitepapers especializados recomiendan medir SASE no solo con KPIs de red clásicos, sino con indicadores de **Quality of Experience (QoE)** alineados con la percepción humana del servicio.  Esto implica ir más allá de latencia genérica y contemplar:[^26][^29][^24]

- **Latencia de aplicaciones cloud y aplicaciones internas.** Valores de referencia típicos sitúan una experiencia aceptable en menos de 150 ms hacia aplicaciones cloud y menos de 100 ms para aplicaciones internas; por encima de 200–300 ms el impacto en la experiencia de usuario se vuelve notable.[^25]
- **Pérdida de paquetes y jitter.** Umbrales recomendados: pérdida de paquetes entre 0–1% y jitter menor de 30 ms para experiencias de voz y vídeo de calidad, monitorizados por túnel y por tipo de tráfico.[^27][^25]
- **Tiempo de transacción por tipo de aplicación.** Transacciones básicas en aplicaciones cloud en torno a 1 s y para aplicaciones internas sensibles < 500 ms, medido desde el punto de vista del usuario (DEM/RUM), no solo desde la red.[^33][^25]
- **Disponibilidad de túneles SD‑WAN / PoPs SASE.** Porcentaje de tiempo con túneles activos y PoPs alcanzables, y tiempo medio de conmutación ante fallo, como base de los acuerdos de nivel de servicio.

Plataformas de prueba específicas recomiendan además instrumentar KPIs de capacidad: ancho de banda efectivo, número de usuarios concurrentes, tasas de conexión y throughput bajo inspección TLS, comparando distintos proveedores SASE y atribuyendo degradaciones a red, nube o funciones de seguridad.[^34][^29][^26]

### 5.2. Métricas de seguridad, Zero Trust y detección/respuesta

En el plano de seguridad, SASE proporciona un plano de datos común para medir la eficacia de SWG, CASB, FWaaS, ZTNA, DLP, RBI y otras funciones avanzadas.  Los indicadores clave incluyen:[^19][^1]

- **Autenticación y autorización.** Tasa de autenticación satisfactoria, ratio de MFA aplicado, latencia de autenticación y de decisión de política, errores por sincronización con IdP o repositorios de identidades.[^35][^28]
- **Cobertura de políticas Zero Trust.** Porcentaje de aplicaciones privadas publicadas únicamente a través de ZTNA, porcentaje de usuarios privilegiados obligados a ZTNA, número de accesos a recursos de alta criticidad que usan túneles “one‑to‑one” en lugar de acceso de red completo.[^17][^1]
- **Eficacia de detección de amenazas.** Número y tasa de amenazas bloqueadas por categoría (malware, phishing, C2, exfiltración), incidentes evitados, ratio de falsos positivos y falsos negativos, correlación con frameworks como MITRE ATT&CK para evaluar cobertura de técnicas.[^36][^26]
- **MTTD, MTTR, MTTC específicos de SASE.** Tiempos medios para detectar, contener y responder a incidentes en el plano SASE (por ejemplo, credenciales comprometidas explotadas a través de acceso remoto, bypass de SWG, fuga de datos vía SaaS), integrados con SIEM y SOAR.[^23][^21]
- **Impacto de la seguridad en el rendimiento.** Sobre‑carga de latencia introducida por inspección TLS, DLP o sandboxing, y correlación entre endurecimiento de políticas y degradación medible de QoE (para evitar que los usuarios desactiven controles por frustración).[^37][^29]

Algunos whitepapers proponen además SLIs específicos, como **policy decision latency** (tiempo desde que llega una petición de acceso al plano de control hasta que se emite la decisión) o **session establishment time** (desde clic del usuario hasta que la sesión queda plenamente operativa), con SLOs en el rango de 300–500 ms.[^38][^28]

### 5.3. Métricas de cumplimiento ENS/NIS2 y gobierno

La adopción de NIS2 obliga a las entidades esenciales e importantes a implantar medidas de gestión de riesgos, controles de acceso fuertes, cifrado, monitorización, pruebas de eficacia y planes de continuidad, entre otros.  Por su parte, el ENS establece 75 medidas organizativas, operacionales y técnicas, que deben implantarse y auditarse periódicamente.[^39][^40][^41][^8]

En este contexto, los indicadores SASE a nivel país deberían incluir, al menos:

- **Porcentaje de sistemas críticos con acceso canalizado vía SASE/ZTNA.** Especialmente en servicios esenciales cubiertos por NIS2 y sistemas ENS de categoría media/alta.
- **Cobertura de cifrado extremo a extremo.** Proporción de tráfico hacia servicios cloud y aplicaciones internas protegido mediante TLS robusto, y porcentaje de ese tráfico inspeccionado de forma conforme a ENS (protección de datos personales, uso de criptografía alineada con CCN).[^40][^4]
- **Trazabilidad y registros.** Proporción de accesos gestionados por la plataforma SASE que generan registros adecuados para auditoría ENS/NIS2 (incluyendo identidad, contexto, decisión de política, recursos accedidos y transferencias de datos).[^8][^4]
- **Shadow IT y servicios no conformes.** Número de aplicaciones cloud no autorizadas detectadas por CASB, reducción de su uso en un horizonte temporal, y porcentaje de tráfico hacia servicios no verificados bloqueado o condicionado.[^1][^19]
- **Seguridad de la cadena de suministro.** Porcentaje de proveedores de servicios cloud/SASE con certificaciones relevantes (ISO 27001, ENS categoría alta, SOC 2, etc.) y con controles alineados con los requisitos de NIS2 sobre terceros.[^31][^8]

La propia regulación ENS prevé que la Comisión Sectorial de Administración Electrónica recopile “las principales variables de la ciberseguridad” para elaborar un informe periódico; SASE puede convertirse en el sensor privilegiado para dichas variables en entornos cloud y de trabajo híbrido.[^4]

### 5.4. Métricas de adopción, consolidación y valor de negocio

Los informes de mercado y encuestas de líderes de TI muestran que las motivaciones para adoptar SASE son tanto técnicas como económicas: mejorar la postura de seguridad (citado por más del 50% de organizaciones), simplificar la gestión y reducir complejidad (cerca del 50%) y asegurar acceso remoto con menor latencia.[^15][^16][^42]

A partir de 2025 se generalizan KPIs de negocio asociados a SASE, entre ellos:

- **Consolidación de proveedores y herramientas.** Número de soluciones de red y seguridad sustituidas por la plataforma SASE, porcentaje de reducción de “vendor sprawl” y contratos, y ahorro operativo asociado.[^42][^24][^17]
- **Tiempo de provisión.** Tiempo medio para dar de alta una nueva sede o colectivo de usuarios a través de SASE (desde petición hasta pleno funcionamiento), comparado con el modelo tradicional de MPLS + appliances.[^43][^24]
- **Soporte a trabajo híbrido.** Número de usuarios remotos activos, incidencias de acceso remoto por usuario, impacto en productividad percibida en encuestas internas.[^14][^15]
- **Continuidad de negocio.** Tiempo de recuperación de servicios críticos cuando un PoP o enlace falla, porcentaje de rutas alternativas operativas, y ejercicios de conmutación planificada o simulada.

## 6. Calidad de Experiencia (QoE) como indicador macro SASE

Una tendencia clara en la literatura técnica es desplazar el foco desde la **Quality of Service (QoS)** (métricas puramente técnicas de red) hacia la **Quality of Experience (QoE)**, que intenta capturar cómo perciben los usuarios la interacción con aplicaciones y servicios asegurados por SASE.[^44][^26][^33]

Plataformas de SD‑WAN y SASE avanzadas ya ofrecen paneles de QoE por tipo de tráfico (voz, vídeo, transaccional) con puntuaciones (por ejemplo, verde/amarillo/rojo) derivadas de latencia, jitter y pérdida de paquetes respecto a umbrales de SLA.  Laboratorios de prueba y fabricantes recomiendan usar QoE como “unidad de medida” privilegiada, por su correlación directa con satisfacción de usuario, adopción y, en última instancia, con éxito de programas de transformación digital.[^26][^38][^27]

A nivel nacional, esto sugiere incorporar indicadores agregados de QoE SASE por sector (sanidad, educación, justicia, administración general, etc.), basados en telemetría anonimizada y encuestas de satisfacción, como complemento a los indicadores ENS/NIS2 de cumplimiento formal. El objetivo político deja de ser “tener un firewall” y pasa a ser “que los servicios esenciales funcionen con seguridad percibida como razonable por usuarios y profesionales”.

## 7. Cuadro de mando de indicadores SASE para España (nivel país)

### 7.1. Dimensión técnica: red y seguridad

Para un despliegue nacional alineado con ENS/NIS2 se propone una batería mínima de indicadores SASE de cobertura técnica:

- **Cobertura SASE en servicios esenciales.** Porcentaje de entidades sujetas a NIS2 y ENS de categoría media/alta que canalizan el acceso remoto y cloud a través de una arquitectura SASE/SSE certificada.
- **Latencia media y p95 hacia servicios cloud críticos.** Medida desde usuarios en territorio español (incluyendo sedes periféricas) hasta aplicaciones SaaS clave (administración electrónica, sanidad, educación), diferenciando tráfico sin y con inspección profunda.[^19][^4]
- **Porcentaje de tráfico inspeccionado.** Proporción del tráfico de salida/entrada de administraciones y operadores esenciales que pasa por SWG/CASB/IPS integrados en el plano SASE, manteniendo cifrado adecuado y respeto a privacidad.[^1][^19]
- **Cobertura ZTNA.** Porcentaje de aplicaciones internas de las AAPP expuestas únicamente mediante ZTNA, porcentaje de usuarios con MFA y acceso segmentado por contexto.[^30][^7]
- **Métricas de amenazas.** Volumen de eventos de malware, phishing, C2 y exfiltración bloqueados por millón de sesiones, tasa de incidentes mayores reportados a CCN‑CERT e INCIBE relacionados con fallos de acceso remoto o VPN heredada.[^36][^4]

### 7.2. Dimensión ENS/NIS2: gobernanza, cumplimiento y riesgo

En coherencia con el ENS y NIS2, la dimensión de gobernanza podría incluir:

- **Grado de cumplimiento ENS apoyado en SASE.** Porcentaje de medidas técnicas ENS (especialmente de protección T y operacional P) soportadas directamente por controles SASE (control de acceso, cifrado, registro, monitorización, segmentación).[^40][^4]
- **Madurez Zero Trust.** Evolución de las entidades ENS/NIS2 en un modelo de madurez Zero Trust (tradicional, inicial, avanzado, óptimo) inspirado en CISA ZTMM, considerando identidad, dispositivos, red, aplicaciones y datos, y uso de telemetría SASE como evidencia.[^9][^30]
- **Gestión de terceros y servicios cloud.** Porcentaje de proveedores críticos con niveles de certificación adecuados y con integración de registros SASE/SSE en los SOC nacionales (COCS, otros centros regionales).[^8][^4]
- **Ensayos y auditorías.** Número de pruebas de penetración, ejercicios de respuesta y auditorías de seguridad que utilizan datos generados por SASE como insumo principal y porcentaje de hallazgos críticos cerrados en plazo.

### 7.3. Dimensión experiencia ciudadana y continuidad de servicios

Por último, una dimensión más “humana” del cuadro de mando debería incluir:

- **Índice de QoE de servicios públicos digitales.** Puntuación agregada (por ejemplo, de 0 a 100) de la experiencia de usuarios finales en interacciones con portales clave (sanidad, educación, justicia, trámites), basada en métricas DEM y en encuestas, separando problemas atribuibles a la capa SASE de otros.[^45][^33]
- **Continuidad de servicios críticos.** Tiempo medio de interrupción de servicios esenciales debido a incidentes de red/seguridad, y porcentaje de estos en los que la resiliencia SASE (multi‑PoP, SD‑WAN redundante, políticas de fail‑open/fail‑closed razonables) ha mitigado el impacto.
- **Confianza y percepción de seguridad.** Evolución de indicadores de confianza ciudadana en servicios digitales (por ejemplo, encuestas nacionales de ciberconfianza) correlacionada con el despliegue de SASE y Zero Trust en las AAPP.

## 8. Comparación internacional: tendencias de KPIs SASE desde 2025

### 8.1. Foco en QoE, Zero Trust y consolidación

A partir de 2025 los informes de analistas (Gartner, IDC, Frost & Sullivan) y de proveedores coinciden en varias tendencias relevantes:[^46][^47][^48]

- **QoE como KPI estrella.** Se generaliza la recomendación de medir latencias, tasas de error, jitter y tiempos de transacción por tipo de aplicación, sintetizándolos en índices comprensibles para negocio (calidad buena/aceptable/mala) en lugar de reportar únicamente KPIs de red clásicos.[^25][^27][^26]
- **Zero Trust como modelo por defecto.** Gartner y fabricantes señalan que Zero Trust pasa de ser aspiracional a baseline, con previsión de que la mayoría de nuevos despliegues de acceso remoto se basen en ZTNA más que en VPN.[^49][^50][^51]
- **Consolidación de plataformas.** Las organizaciones priorizan plataformas SASE y SSE de un único proveedor, buscando un plano de políticas y telemetría unificado para reducir complejidad, ceguera y coste operativo.[^52][^13][^17]

Los informes de adopción SSE/SASE muestran también que los indicadores que más interesan a la alta dirección son precisamente aquellos que relacionan seguridad con valor de negocio: reducción de incidentes, mejora de visibilidad y control de datos sensibles, consolidación de herramientas y soporte fluido a trabajo híbrido.[^16][^15][^42]

### 8.2. Europa y España: ENS, NIS2 y cloud soberano

En la Unión Europea, NIS2 actúa como catalizador para métricas de seguridad transversales (riesgo, incidentes, continuidad, proveedores, etc.) y refuerza el alineamiento con modelos Zero Trust y arquitecturas SASE/SSE como forma de aplicar controles homogéneos.  ENISA, junto con NIST y CISA, ha publicado guías de Zero Trust que enfatizan métricas de identidad fuerte, control de acceso basado en riesgo, monitorización de comportamiento y madurez por dominios, aplicables a configuraciones SASE.[^7][^39][^9][^3][^31]

En España, el ENS actualiza los principios de seguridad para la administración digital y establece obligaciones de vigilancia continua, medición del estado de la seguridad y reporte centralizado de variables principales, con CCN‑CERT y INCIBE como nodos clave de respuesta e inteligencia.  Informes y blogs técnicos de organismos como INCIBE describen explícitamente la arquitectura SASE como vía para cumplir requisitos ENS en entornos cloud y trabajo híbrido, destacando la convergencia de funciones (NGFW, SWG, CASB, ZTNA, DLP, WAAP, RBI) y la mejora de QoE.[^53][^4][^19]

La contratación de soluciones SASE por parte de administraciones autonómicas y organismos regionales (por ejemplo, proyectos de Madrid Digital basados en plataformas SASE/Zero Trust) ilustra una tendencia hacia la adopción de SASE como infraestructura troncal para sedes, ayuntamientos y usuarios remotos, con requisitos de ZTNA, DLP avanzado, sandboxing, segmentación y analítica de amenazas.  Estos pliegos ya incluyen de facto KPIs de rendimiento, disponibilidad global, número de PoPs, capacidad de segmentación y capacidades avanzadas de seguridad que pueden convertirse en indicadores normalizados a escala nacional.[^54]

## 9. Propuesta de indicadores SASE para una encuesta nacional en España

Con el objetivo de medir el grado de madurez SASE/Zero Trust en España y compararlo con el entorno internacional, se propone una encuesta nacional orientada a CISOs, CIOs y responsables de continuidad, que recoja tanto indicadores cuantitativos como percepciones cualitativas. A modo de muestra, se sugieren algunos bloques de preguntas y posibles ítems de respuesta, con un tono deliberadamente inquisitivo pero constructivo.

### 9.1. Bloque A: Arquitectura y alcance SASE

- **A1. Cobertura de la arquitectura SASE.**
  - ¿Qué porcentaje aproximado de su tráfico hacia aplicaciones SaaS y servicios cloud pasa hoy por su plataforma SASE/SSE?
    - 0–25% (aún confiamos en el “castillo y el foso” tradicional).
    - 26–50% (estamos a mitad de camino, intentando dejar de cavar fosos y llenar nubes).
    - 51–75% (el perímetro ya no es un lugar, es una política).
    - 76–100% (hemos asumido que el perímetro ahora nos persigue a nosotros).

- **A2. Acceso a aplicaciones internas.**
  - Para el acceso remoto a aplicaciones internas críticas, su organización utiliza principalmente:
    - VPN clásica con acceso de red completo (y un rosario de reglas de firewall heredadas).
    - ZTNA parcial para algunos colectivos o aplicaciones.
    - ZTNA obligatorio para todo acceso remoto a aplicaciones internas.
    - Un modelo híbrido en transición, con fecha de jubilación anunciada para la VPN.

### 9.2. Bloque B: Identidad, Zero Trust y control de acceso

- **B1. Autenticación fuerte y contexto.**
  - ¿Qué porcentaje de usuarios con acceso a datos sensibles está protegido con MFA y políticas contextuales (dispositivo, ubicación, riesgo)?
    - 0–25% (todavía creemos demasiado en la bondad intrínseca del usuario interno).
    - 26–50% (hemos instalado MFA, pero solo donde “ardía”).
    - 51–75% (MFA por defecto, excepciones justificadas y vigiladas).
    - 76–100% (la confianza se gana cada vez que el usuario inicia sesión).

- **B2. Segmentación de acceso.**
  - ¿Cómo describe su modelo de segmentación de acceso a aplicaciones internas?
    - Red plana, con mucha fe y algo de VLAN.
    - Segmentación básica por zonas (oficinas, CPD, proveedores).
    - Segmentación granular basada en identidad y rol (Zero Trust “en serio”).
    - Segmentación dinámica basada en riesgo (dispositivo, comportamiento, clasificación de datos).

### 9.3. Bloque C: Métricas de rendimiento y QoE

- **C1. Latencia percibida hacia servicios cloud clave.**
  - ¿Cómo describiría la experiencia de sus usuarios al acceder a aplicaciones SaaS críticas a través de SASE?
    - A menudo lenta, tanto que algunos usuarios buscan atajos “por fuera”.
    - Aceptable: protestan menos de lo que esperábamos.
    - Buena: el comentario típico es “funciona igual o mejor que antes”.
    - Excelente: si desactiváramos SASE, los usuarios lo notarían (y se quejarían).

- **C2. Umbrales objetivos.**
  - ¿Dispone de SLOs explícitos de QoE (latencia, jitter, tiempos de transacción) para tráfico a través de SASE y los monitoriza de forma continua?
    - No, nos conformamos con que “no se caiga”.
    - Algunos umbrales de red, pero no orientados a experiencia de usuario.
    - SLOs definidos para aplicaciones críticas, con paneles de QoE.
    - SLOs revisados con negocio, con decisiones de inversión basadas en esos datos.

### 9.4. Bloque D: Detección, respuesta y visibilidad

- **D1. Telemetría y correlación.**
  - ¿Está integrada la telemetría de su plataforma SASE (eventos de SWG, CASB, ZTNA, FWaaS) con su SIEM/SOC nacional o interno?
    - No, SASE es aún un “aparte” con su propio portal que casi nadie mira.
    - Integración parcial (logs críticos y alertas de alto nivel).
    - Integración completa, con casos de uso específicos en el SIEM.
    - Uso extensivo en casos de threat hunting y análisis forense.

- **D2. Métricas de detección y respuesta.**
  - ¿Mide de forma diferenciada MTTD, MTTR y MTTC para incidentes originados o detectados en la capa SASE?
    - No (los incidentes son incidentes, vengan de donde vengan).
    - Sí, pero sin objetivos claros aún.
    - Sí, con objetivos y revisiones periódicas.
    - Sí, y dichos indicadores influyen en objetivos de desempeño del equipo de seguridad.

### 9.5. Bloque E: Cumplimiento ENS/NIS2 y cadena de suministro

- **E1. ENS y servicios cloud.**
  - Para servicios cloud consumidos por su organización, ¿en qué medida utiliza SASE para implantar medidas ENS (control de acceso, cifrado, monitorización, registro, DLP)?[^4][^19]
    - Residual: cada proyecto cloud se defiende como puede.
    - Parcial, en algunos servicios o dominios.
    - Amplia, con SASE como plano común de control y visibilidad.
    - Casi total, con perfiles de cumplimiento específicos y controles centralizados.

- **E2. Proveedores y certificaciones.**
  - ¿Qué porcentaje de sus proveedores de servicios SASE/SSE/SD‑WAN dispone de certificaciones relevantes (ENS, ISO 27001, NIS2‑ready) y comparte telemetría de seguridad con su SOC?
    - Menos del 25% (las certificaciones están en la lista de deseos, no de requisitos).
    - Entre el 25% y el 50%.
    - Entre el 51% y el 75%.
    - Más del 75%, por diseño contractual.

## 10. Recomendaciones de diseño de indicadores para España

A la luz de la evidencia disponible y del marco regulatorio español y europeo, destacan varias recomendaciones para el diseño de indicadores SASE a nivel nacional:

1. **No reinventar la rueda: extender ENS y NIS2.** Los indicadores SASE deben alinearse explícitamente con las medidas ENS (O, P, T) y con los requisitos de NIS2 sobre riesgo, incidentes, continuidad y terceros, utilizando SASE como sensor y mecanismo de ejecución, no como fin en sí mismo.[^40][^8][^4]
2. **QoE y Zero Trust como ejes visibles para negocio.** Incorporar indicadores de experiencia de usuario (latencias, tiempos de transacción, satisfacción) y de madurez Zero Trust (cobertura ZTNA, MFA, segmentación, comportamiento) como KPIs de alto nivel reportados en los informes de estado de la seguridad de la administración digital.[^7][^26][^28]
3. **Telemetría común para AAPP y operadores esenciales.** Establecer formatos, taxonomías y mecanismos de agregación de datos SASE/SSE hacia CCN‑CERT, INCIBE y el futuro ecosistema NIS2, garantizando anonimización donde proceda pero maximizando la capacidad de detección temprana y análisis sectorial.[^3][^53][^4]
4. **Indicadores de consolidación y eficiencia.** Medir reducción de complejidad (número de herramientas, contratos, puntos de fallo), ahorro operativo y mejora de tiempos de provisión como parte de los beneficios de SASE, para justificar inversiones en términos comprensibles para la alta dirección y organismos de control presupuestario.[^13][^24][^17]
5. **Adaptación territorial y sectorial.** Introducir perfiles de cumplimiento específicos (como permite el ENS) que definan umbrales y KPIs SASE diferenciados para sanidad, educación, justicia, administración general, corporaciones locales e infraestructuras críticas, respetando las distintas realidades de recursos y riesgos.[^10][^4]
6. **Gobernanza compartida y transparencia.** Fomentar que las decisiones sobre SASE se tomen en órganos de gobernanza de ciberseguridad y continuidad (CISOs, CIOs, responsables de negocio y de riesgos), utilizando los indicadores descritos como lenguaje común para priorizar inversiones y reformas organizativas.[^48][^30]

## 11. Conclusión

Desde 2025, los indicadores del marco SASE han evolucionado desde métricas puramente técnicas de red y seguridad hacia un lenguaje común que mezcla QoE, Zero Trust, cumplimiento regulatorio y valor de negocio.  A nivel internacional, los países y organizaciones más avanzados combinan KPIs de latencia, disponibilidad y detección de amenazas con métricas de madurez Zero Trust, consolidación de plataformas y satisfacción de usuario, utilizando la telemetría SASE como columna vertebral de su observabilidad de ciberseguridad.[^47][^24][^15][^17][^26][^28]

España dispone de un marco normativo robusto (ENS actualizado, Plan Nacional de Ciberseguridad, inminente transposición de NIS2) y de capacidades institucionales (CCN‑CERT, INCIBE, COCS) que pueden aprovechar SASE como palanca técnica y como fuente de indicadores homogéneos para la administración pública y operadores esenciales.  El reto ya no es definir SASE, sino medirlo con la suficiente finura como para que estos indicadores orienten decisiones de política pública, presupuestarias y de gestión del riesgo, sin perder de vista que, al final, la mejor métrica es que los servicios críticos funcionen, los ataques no arruinen el día… y el ciudadano deje de notar que hay un perímetro, precisamente porque está en todas partes.[^53][^3][^19][^4]

---

## References

1. [What Is SASE (Secure Access Service Edge)? | A Starter ...](https://www.paloaltonetworks.com/cyberpedia/what-is-sase) - Secure access service edge (SASE) is a cloud-native architecture that unifies SD-WAN with security f...

2. [Secure Access Service Edge (SASE) Market Size, Growth ...](https://www.mordorintelligence.com/industry-reports/global-secure-access-service-edge-market) - The Secure Access Service Edge Market worth USD 15.54 billion in 2026 is growing at a CAGR of 20.29%...

3. [NIS2 Directive: securing network and information systems](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive) - The NIS2 Directive establishes a unified legal framework to uphold cybersecurity in 18 critical sect...

4. [Real Decreto 311/2022, de 3 de mayo, por el que se ...](https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191) - BOE-A-2022-7191 Real Decreto 311/2022, de 3 de mayo, por el que se regula el Esquema Nacional de Seg...

5. [What is Secure Access Service Edge (SASE)?](https://www.crowdstrike.com/en-us/cybersecurity-101/cloud-security/Secure-Access-Service-Edge-SASE/) - Secure access service edge (SASE) is a cybersecurity and networking framework that enables the integ...

6. [What is SASE (Secure Access Service Edge)? Benefits and ...](https://www.fortinet.com/resources/cyberglossary/sase) - Secure Access Service Edge (SASE) is a cloud-delivered framework that converges essential networking...

7. [[PDF] Zero Trust & The Flaming Sword of Justice - ENISA](https://www.enisa.europa.eu/sites/default/files/all_files/6%20FlamingSword(ENISA-Lisbon-2023)Final.pdf) - What is Zero Trust? • Where/how/when trust is decided has changed. • Must continuously verify. • Ass...

8. [NIS2 requirements: A complete guide to compliance & implementation](https://www.dataguard.com/nis2/requirements/) - Learn who needs to comply with NIS2, key security measures, reporting rules, and deadlines. Stay ahe...

9. [[PDF] Zero Trust Architecture - Palindrome Technologies](https://palindrometech.com/hubfs/Zero%20Trust%20Architecture%20-%20A%20Unified%20Approach%20to%20Modern%20Cybersecurity%20Based%20on%20CISA-ENISA%20and%20NIST%20Guidance.pdf) - This paper provides a comprehensive technical overview of Zero Trust. Architecture, drawing upon the...

10. [Esquema Nacional de Seguridad](https://portal.mineco.gob.es/es-es/ministerio/estrategias/Paginas/Esquema_Nacional_de_Seguridad.aspx)

11. [Secure Access Service Edge Market Size Share, 2025-2032](https://www.coherentmi.com/industry-reports/secure-access-service-edge-market) - The Global Secure Access Service Edge Market is estimated to be valued at USD 2.72 Bn in 2025 and is...

12. [Secure Access Service Edge (SASE) Market Outlook 2025-2030](https://finance.yahoo.com/news/secure-access-edge-sase-market-082200935.html) - The SASE market is estimated to be USD 15.52 billion in 2025 and reach USD 44.68 billion in 2030 at ...

13. [Secure Access Service Edge Market Report 2025-2033.](https://www.imarcgroup.com/secure-access-service-edge-market) - Secure Access Service Edge Market size was valued at USD 4.11 Billion in 2024, exhibiting a CAGR of ...

14. [2025 State of Secure Network Access: Exploring the Future of](https://www.contentree.com/reports/2025-state-of-secure-network-access-exploring-the-future-of-sase-sse-zero-trust-and-hybrid-security-strategies_429610) - Hughes - 2025 State of Secure Network Access: Exploring the Future of SASE, SSE, Zero Trust, and Hyb...

15. [New Report: State of Secure Network Access in 2025](https://www.cybersecurity-insiders.com/state-of-secure-network-access-2025/) - AI is evolving at a rapid pace, and the uptake of Generative AI (GenAI) is revolutionising the way h...

16. [2025 State of Secure Network Access](https://www.hughes.com/sites/hughes.com/files/2025-01/2025-Secure-Network-Access-Report-Hughes.pdf)

17. [SSE Adoption Report 2025 - The state of secure access](https://www.cybersecurity-insiders.com/sse-adoption-report-2025-the-state-of-secure-access/) - SSE Adoption Report 2025 reveals secure access trends, challenges, and implementations shaping enter...

18. [Cloud, SASE y redes distribuidas disparan el mercado global de ...](https://ciberseguridadtic.es/actualidadinfraestructura/cloud-sase-y-redes-distribuidas-disparan-el-mercado-global-de-seguridad-de-red-2025121211214.htm) - La convergencia entre redes y seguridad, materializada en enfoques como SD-WAN seguro y SASE, se con...

19. [La arquitectura SASE en tu estrategia de seguridad](https://www.incibe.es/incibe-cert/blog/la-arquitectura-sase-en-tu-estrategia-de-seguridad) - Los paradigmas tradicionales de la ciberseguridad se han quedado anticuados con la llegada del cloud...

20. [Programa oficial de Conferencias en Congreso ASLAN202](https://aslan.es/congreso/programa/) - Secure Access Service Edge (SASE) se ha consolidado como una solución esencial para gestionar la seg...

21. [Essential Security Operations Metrics for Effective ...](https://www.tufin.com/blog/essential-security-operations-metrics-effective-cybersecurity) - In the security industry, Key Performance Indicators (KPIs) are measurable values that demonstrate h...

22. [Common Cybersecurity Metrics: Key KPIs to Measure](https://www.kiuwan.com/blog/common-cybersecurity-metrics-key-kpis-to-measure/) - Regardless of their background, it's important that stakeholders understand their cybersecurity team...

23. [20 Cybersecurity Metrics & KPIs to Track in 2025](https://securityscorecard.com/resources/learning-center/9-cybersecurity-metrics-kpis-to-track/) - Metrics and KPIs: Establishing key performance indicators (KPIs) for cybersecurity training, such as...

24. [What Are the Steps to a Successful SASE Implementation Strategy?](https://www.zenarmor.com/docs/network-security-tutorials/steps-of-successful-sase-implementation-strategy) - What Are the Steps to a Successful SASE Implementation Strategy? How Do You Select the Right SASE Ve...

25. [SASE KPI Breakdown: What Really Matters?](https://www.commandlink.com/wp-content/uploads/2025/02/SASE-KPI-Breakdown-What-Really-Matters.pdf)

26. [Testing Challenges and Strategies for Successful SASE Deployments](https://blog.viavisolutions.com/2022/11/21/testing-challenges-and-strategies-for-successful-sase-deployments/) - SASE emerged in 2019 as a visionary security framework where security functions are hosted in the cl...

27. [QoE Tab](https://techdocs.broadcom.com/us/en/vmware-sde/velocloud-sase/vmware-velocloud-sd-wan/4-5/sd-wan-administration-guide/monitoring-enterprise-portal/edges/qoe-tab.html) - The VMware Quality of Experience (QoE) tab shows the Quality Score for different applications. The Q...

28. [What is Secure Access Service Edge? Meaning, Architecture ...](http://devsecopsschool.com/blog/secure-access-service-edge/) - ---

29. [Secure Access Service Edge (SASE) - Keysight](https://www.keysight.com/ch/de/assets/7120-1277/flyers/CyPerf-Secure-Access-Service-Edge.pdf) - Test agents send application and attack traffic simultaneously through SASE solutions to validate th...

30. [Global cybersecurity agencies advocate adoption of zero trust, SSE ...](https://industrialcyber.co/cisa/global-cybersecurity-agencies-advocate-adoption-of-zero-trust-sse-sase-to-enhance-network-access-security/) - Global cybersecurity agencies advocate adoption of zero trust, SSE, SASE to enhance network access s...

31. [Understanding NIS2 Compliance: A Practical Implementation Guide](https://opsiocloud.com/no/blogs/nis2-compliance/) - This guide breaks down the complex NIS2 compliance requirements into practical, actionable insights ...

32. [Top Cybersecurity Metrics and KPIs for 2026](https://www.upguard.com/blog/cybersecurity-metrics) - Key performance indicators (KPIs) (The "how"): These are strategic, rate-based measurements tied to ...

33. [What is SSE (Security Service Edge)? | Glossary](https://www.hpe.com/us/en/what-is/security-service-edge.html) - ... Secure Access Service Edge (SASE) architecture that significantly improves end user Quality of E...

34. [Secure Access Service Edge (SASE)](https://www.keysight.com/jp/ja/assets/7120-1277/flyers/CyPerf-Secure-Access-Service-Edge.pdf) - Test agents send application and attack traffic simultaneously through SASE solutions to validate th...

35. [What Is Secure Access Service Edge (SASE)?](https://www.microsoft.com/en-us/security/business/security-101/what-is-sase) - SASE stands for secure access service edge. It's a cloud-delivered architecture that combines networ...

36. [[PDF] Critical Guidance for Evaluating SASE Solutions | Fortinet](https://www.fortinet.com/content/dam/fortinet/assets/white-papers/pov-critical-considerations-when-evaluating-sase-solutions.pdf)

37. [Why SASE Performance Matters for Network Security - Versa Networks](https://versa-networks.com/blog/why-sase-performance-matters-more-than-you-think/) - Discover why SASE performance is more than a technical metric. Learn how latency, TLS inspection, an...

38. [Security and Performance Testing for SASE-ZT](https://assets.ctfassets.net/wcxs9ap8i19s/6B7qpOhTk9KNQtartXuJIP/1c99aaa3ddd08eca539eb59ee7d595a7/WP_Security_Performance_Testing_SASE-ZT_-RevA.pdf) - real-time metrics to assess the impact of failures on QoE service recovery times. ... latency ... un...

39. [The NIS 2 Directive | Updates, Compliance, Training](https://www.nis-2-directive.com) - It is designed to enhance cybersecurity across the European Union by establishing a high common leve...

40. [Esquema Nacional de Seguridad: Guía completa de ... - Audidat](https://www.audidat.com/blog/seguridad/esquema-nacional-seguridad-ens/) - El Esquema Nacional de Seguridad (ENS) es clave. Descubre qué es, su obligatoriedad, categorías y la...

41. [Qué es el Esquema Nacional de Seguridad (ENS)](https://ens.ccn.cni.es/es/que-es-el-ens)

42. [Cato Survey: Remote Access Issues and Need for ...](https://www.catonetworks.com/blog/cato-survey-remote-access-issues-and-need-for-increased-visibility-continue-to-drive-sase-in-2024/) - Vendor consolidation remains crucial for nearly half of respondents to our most recent IT survey. Bu...

43. [The Ultimate Guide To Unified SASE In 2025](https://www.aryaka.com/blog/ultimate-guide-unified-sase-2025/) - Unified SASE enhances performance by leveraging a direct-to-cloud architecture that removes the bott...

44. [Quality of Experience vs Quality of Service: Which are You ...](https://www.netskope.com/blog/quality-of-experience-vs-quality-of-service-which-are-you-getting) - A Leader in Secure Access Service Edge (SASE) · A Forrester Wave™ SSE ... Quality of Experience vs Q...

45. [Quality of Experience (QoE): Definition, Benefits & Best Practices](https://www.itbroker.com/resources/glossary/quality-of-experience-qoe) - ... metrics like latency ... Integration with SD-WAN and SASE QoE monitoring ... Edge Computing Brin...

46. [The State of SASE in 2025: Trends and Key Insights - Versa Networks](https://versa-networks.com/resources/webinars/the-state-of-sase-in-2025-trends-evaluation-criteria-and-strategic-insights/) - the 2025 GigaOm Radar for SASE—highlighting the market trends, evaluation criteria, and architectura...

47. [Frost Radar : Secure Access Service Edge, 2025](https://www.cisco.com/c/dam/en/us/solutions/collateral/secure-access-service-edge-sase/frost-radar-sase2025-report.pdf) - Frost & Sullivan expects global SASE market revenue to reach $7.4 billion by 2029 (an increase from....

48. [IDC-MarketScape-Worldwide-Managed-SASE-2025. ...](https://www.levelblue.com/hubfs/Web/Library/Documents_pdf/IDC-MarketScape-Worldwide-Managed-SASE-2025.pdf) - SASE emerged as an architectural framework that integrates software-defined networking with security...

49. [A Leader In Sase](https://www.paloaltonetworks.sg/resources/research/gartner-predicts-2025-zero-trust-and-resilience-sase) - Read the latest research from Gartner® on how Zero Trust, with a SASE platform, will help organizati...

50. [5 Predictions for Zero Trust and SASE in 2025 - Zscaler, Inc.](https://www.zscaler.com/blogs/product-insights/5-predictions-zero-trust-and-sase-2025-what-s-next) - Learn about five key trends that will shape cybersecurity priorities in 2025, and how zero trust + A...

51. [Netskope Announces ZTNA Next, evolution of its ZTNA solution](https://timestech.in/netskope-announces-ztna-next-evolution-of-its-ztna-solution/) - Netskope, a leader in Secure Access Service Edge (SASE), announced ZTNA Next, the evolution of its a...

52. [Cisco Named a Leader in 2025 Frost Radar for SASE](https://www.cisco.com/site/us/en/solutions/secure-access-service-edge-sase/sase-frost-radar-2025.html) - Download the 2025 Frost Radar for Secure Access Service Edge to see why Frost & Sullivan ranks Cisco...

53. [ENS - ENS](https://ens.ccn.cni.es/es/) - Para llevar a cabo la Gobernanza de la ciberseguridad y facilitar el proceso completo de adecuación ...

54. [[PDF] Resolución 544-2025 - Comunidad de Madrid |](https://www.comunidad.madrid/tacp/sites/default/files/resolucion544-expediente_542-2025.pdf) - ▫ Hardware propio para ZTNA: la arquitectura se basa en SD-WAN, no en ZTNA puro. Page 14. Calle Manu...

