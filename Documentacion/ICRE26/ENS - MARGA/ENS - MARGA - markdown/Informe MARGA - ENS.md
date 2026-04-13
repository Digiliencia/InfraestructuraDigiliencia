
# Informe MARGA - ENS.

El punto de partida honesto es éste: a día de hoy, el término «MARGA‑ENS» no aparece como marco público, estable y documentado al estilo de las Guías STIC 800, de las IMC de INCIBE o del propio Real Decreto 311/2022 que regula el Esquema Nacional de Seguridad. Todo indica que estamos ante un marco en construcción o de circulación restringida, probablemente articulado sobre piezas ya visibles: ENS, guías STIC 81x/82x, las IMC de INCIBE y algunas iniciativas recientes de estandarización de indicadores para CISOs.[^1][^2][^3][^4][^5][^6][^7]

Dicho esto, es perfectamente posible —y útil— reconstruir el “esqueleto” de un Informe MARGA‑ENS a partir de esos ladrillos oficiales y de la evolución internacional de la métrica de ciberseguridad desde 2025. Lo que sigue es, por tanto, un ejercicio de arqueología conceptual: leer entre líneas lo que el Estado y el ecosistema europeo ya han colocado sobre la mesa, y ensamblarlo en clave de indicadores nacionales comparables globalmente.

***

### 1. ENS como columna vertebral: de la norma a los indicadores

El ENS actualizado por el Real Decreto 311/2022 refuerza la idea de que la seguridad de la Administración Digital debe gobernarse mediante un ciclo completo de adecuación, implantación, auditoría, certificación e información periódica sobre el estado de seguridad. En la fase de «Informar sobre el Estado de Seguridad» el propio CCN remite explícitamente a métricas e indicadores como herramientas para la toma de decisiones estratégicas.[^8][^9][^2][^5][^1]

La lógica es inequívoca: sin indicadores cuantificables, el ENS sería un catecismo normativo imposible de dirigir a escala país. Desde 2022 se ha ido consolidando una transición desde el “cumplo y miento” documental hacia una lectura más madura basada en datos operativos: tiempos de detección, de respuesta, porcentaje de sistemas auditados, niveles de madurez por dominio, etc. A partir de 2025 esta tendencia se acelera por tres fuerzas externas:[^2][^10]

1. La Estrategia de Ciberseguridad de la UE, que insiste en resiliencia medible, capacidad operativa y cooperación, con inversiones crecientes condicionadas a resultados.[^11]
2. La presión geopolítica y el cambio de tono en los informes como el Global Cybersecurity Outlook 2026 del WEF, donde el riesgo cibernético se declara “realidad cotidiana” y no hipótesis remota.[^12]
3. La inflación regulatoria (NIS2, DORA, AI Act, 5G, etc.), que obliga a demostrar con indicadores el alineamiento entre controles y riesgo.[^13][^14]

En ese contexto, un marco tipo MARGA‑ENS sólo puede ser, por diseño, una capa de orquestación de indicadores sobre el ENS, no un sustituto de éste.

***

### 2. Las fuentes “canónicas” de indicadores en España

Si uno rastrea la “biblioteca” de métricas serias en España, la huella es clara:

1. **ENS + Guías STIC Serie 800.** El portal del ENS remite a la normativa y a las guías STIC 800 como referencia de detalle. Ahí se sistematiza la adecuación, auditoría, certificación y, sobre todo, el reporte de estado, donde aparecen categorías de indicadores (cumplimiento, incidentes, eficacia de controles, etc.).[^7][^2]
2. **Diccionario de Indicadores para Mejora de la Ciberresiliencia (IMC_02) de INCIBE.** Se trata de un catálogo exhaustivo de indicadores alineados con metas funcionales (“Anticipar”, “Resistir”, “Recuperar”, etc.), con fichas que incluyen código, objetivo, fórmula de cálculo, fuente de datos y periodicidad. Es, en la práctica, el primer intento serio de dar un metamodelo nacional de indicadores reutilizable por distintos sectores.[^4][^6]
3. **Sector público vertical (ej. Estrategia de Ciberseguridad del SNS).** Para ámbitos críticos como sanidad se ha elaborado una estrategia de ciberseguridad específica que, aunque no se detalla aquí, sigue la misma lógica ENS + indicadores de madurez, incidentes, tiempo de recuperación y continuidad asistencial.[^15]
4. **Iniciativas privadas de estandarización para CISOs.** El ISMS Forum, por ejemplo, trabaja desde 2025 en un “marco estandarizado de indicadores” para CISOs basado en KPIs y KRIs estratégicamente relevantes, medibles y comparables, con foco en cómo comunicar a la Alta Dirección el impacto de la ciberseguridad.[^3]

Si MARGA‑ENS existe como artefacto real —aunque no publicado—, es difícil imaginar que no beba de estas cuatro fuentes.

***

### 3. Qué mide de verdad un marco tipo MARGA‑ENS

Aunque el nombre concreto del marco no aparezca en las fuentes públicas, sí podemos aislar las familias de indicadores que un esquema de esta naturaleza tendría que recoger para ser coherente con ENS, con las IMC y con la agenda europea. A grandes rasgos, caben seis dominios:

1. Gobernanza y cumplimiento ENS.
2. Postura de ciberresiliencia (anticipar, resistir, recuperar).
3. Eficacia operativa (detección, respuesta, continuidad).
4. Gestión del riesgo y del impacto (incluido el actuarial).
5. Integración de Zero Trust y nuevas arquitecturas.
6. Comparabilidad internacional.

Veámoslos uno por uno.

***

#### 3.1. Gobernanza ENS y adecuación nacional

El ENS fija principios de gestión del riesgo, proporcionalidad, responsabilidad y transparencia, además de niveles de seguridad (básico, medio, alto) vinculados a controles crecientes y evidencia de auditoría. Traducido a indicadores, la gobernanza nacional se resumiría en tres grandes grupos:[^10][^5]

- Cobertura ENS: porcentaje de organismos y sistemas críticos con adecuación completada, auditoría realizada y, cuando proceda, certificación.[^1][^2]
- Condición ENS: grado de cumplimiento por dominio de control (organizativo, operacional, de protección, etc.), calculado desde los resultados de auditoría y de pruebas técnicas.[^2][^10]
- Trazabilidad y mejora continua: número y porcentaje de no conformidades resueltas, frecuencia de auditorías y ejercicios de prueba, evolución año a año.[^10][^2]

El CCN ya señala en sus materiales que informar sobre el estado de seguridad mediante métricas e indicadores es un requisito explícito del proceso de adecuación. Un MARGA‑ENS sensato no inventaría nada exótico aquí: simplemente estandarizaría cómo se calculan, agregan y reportan esos porcentajes a escala nacional (Ministerios, CCAA, entidades locales, proveedores críticos).[^9][^2]

***

#### 3.2. Ciberresiliencia: el ascenso de las IMC

Las guías IMC de INCIBE, y en particular el “Diccionario de indicadores para mejora de la ciberresiliencia”, ofrecen una taxonomía que encaja casi a la perfección con una lectura actuarial‑estratégica de la seguridad. Cada indicador se sitúa en una meta funcional (Anticipar, Proteger, Detectar, Responder, Recuperar, etc.), con un código y una ficha que incluyen:[^6][^4]

- Objetivo del indicador (qué pretende demostrar).
- Fórmula de cálculo (porcentaje, tasa, número absoluto, índice compuesto).
- Dominio funcional (política, gestión de activos, monitorización, formación, etc.).
- Fuente de datos (herramientas, registros, encuestas).
- Periodicidad y umbrales objetivos.[^4]

Por ejemplo, la ficha A‑PC‑OG1‑01, en el dominio “Política de ciberseguridad”, se define para “establecer, actualizar y mantener una política de ciberseguridad”, y se acompaña de métricas medibles. El punto clave no es el contenido concreto de cada ficha, sino el patrón: codificación, trazabilidad y replicabilidad para cualquier organización que quiera medir su resiliencia.[^4]

Desde 2025, esta visión ha ido convergiendo con la narrativa global en torno a la “resiliencia digital”, entendida no ya como un conjunto de controles, sino como una capacidad entrenable de mantener funciones esenciales ante perturbaciones, según recogen tanto los informes europeos como el Global Cybersecurity Outlook 2026. En un marco MARGA‑ENS de nivel país, los indicadores de ciberresiliencia funcionarían como “módulos” reutilizables de las IMC, agregados por sector y territorio.[^14][^12]

***

#### 3.3. Eficacia operativa: del KPI de CISO al indicador nacional

En el ecosistema internacional, los KPIs esenciales de ciberseguridad son ya un canon bastante estable: número de vulnerabilidades críticas, porcentaje de parches aplicados, tiempos medios de detección (MTTD) y de respuesta (MTTR), falsos positivos, incidentes mitigados dentro de SLA, impacto económico estimado, etc. Todo ello casa con lo que marcos como el NIST CSF, ISO/IEC 27004 o la propia literatura de Zero Trust recomiendan.[^16][^17][^18]

España no es una isla: los informes de estado de la ciberseguridad en España elaborados por consultoras y asociaciones reflejan precisamente esos indicadores, y el ENS anima a emplear métricas e indicadores para la mejora continua. La diferencia entre un tablero de CISO y un MARGA‑ENS nacional es de escala y de agregación: lo que en una organización es un KPI operativo, a nivel país se convierte en:[^19][^10]

- Distribuciones de tiempos de detección y respuesta por sector (sanidad, educación, administración general del Estado, entidades locales).
- Frecuencias de incidentes por tipo (ransomware, denegación de servicio, fraude, fuga de información).
- Porcentaje de entidades con capacidad de monitorización continua efectiva, según criterios como los de las IMC.[^4]

La UE, en su estrategia de ciberseguridad, subraya la necesidad de aumentar la resiliencia frente a ciberamenazas y de sostener esa ambición con “un nivel de inversión sin precedentes”. A nadie se le ocurriría justificar tales inversiones sin un cuadro coherente de indicadores. MARGA‑ENS, de existir, sería la plantilla que homologa qué se mide y cómo, para poder justificar presupuestos y priorizar intervenciones.[^11]

***

#### 3.4. Riesgo, impacto y la tentación actuarial

El discurso del riesgo cibernético como riesgo empresarial y sistémico ha madurado notablemente desde 2025. Informes como el Global Cybersecurity Outlook 2026 del WEF indican que el riesgo cibernético es una “realidad cotidiana” y que más del 60% de las organizaciones integran ya los ciberataques con motivación geopolítica en su estrategia. La Comisión Europea, por su parte, insiste en la ciberresiliencia como componente esencial de la seguridad económica y social de la Unión.[^12][^14]

Trasladado a indicadores, esto implica negociar entre dos tentaciones:

- El exceso actuarial: reducir la ciberseguridad a primas, siniestros y curvas de pérdida esperada, como si se tratase de seguros de automóvil, obviando el carácter adaptativo y estratégico del adversario.
- El voluntarismo técnico: acumular datos operativos sin traducirlos en lenguaje de riesgo comprensible por Consejos de Administración y supervisores.

Las iniciativas españolas que buscan un marco estandarizado de indicadores para CISOs tratan precisamente de equilibrar ambos extremos con KPIs y KRIs que sean estratégicamente relevantes, medibles y comparables. En esa lógica, un MARGA‑ENS de país debería incorporar:[^3]

- Indicadores de exposición (superficie de ataque, criticidad de servicios, dependencias de terceros).
- Indicadores de control (grado de implementación de medidas ENS, Zero Trust, detección avanzada).
- Indicadores de pérdida (costes directos e indirectos de incidentes, interrupciones de servicio, impacto reputacional estimado).[^18]

No para alimentar un fetiche numérico, sino para permitir priorizar inversiones y políticas públicas en función del riesgo agregado.

***

#### 3.5. Zero Trust y nuevas arquitecturas como variables observables

Desde 2020 el NIST viene definiendo Zero Trust como un conjunto de paradigmas que desplazan la seguridad desde perímetros estáticos hacia una protección centrada en usuarios, activos y recursos, bajo el principio «nunca confíes, siempre verifica». España ha empezado a incorporar esta narrativa: INCIBE, por ejemplo, describe Zero Trust como una metodología integral que reduce la superficie de ataque limitando el acceso de usuarios y aplicaciones sólo a los recursos necesarios.[^17][^20][^16]

El salto que un marco como MARGA‑ENS debería dar es convertir esa arquitectura en indicadores verificables. Algunos ejemplos, inspirados en la literatura internacional y compatibles con ENS, serían:

- Porcentaje de recursos críticos accesibles exclusivamente mediante autenticación fuerte y autorización contextual.
- Grado de segmentación y microsegmentación de redes (medido en número de enclaves, controladores de acceso, políticas de tráfico).
- Porcentaje de tráfico inspeccionado y registrado entre segmentos, no sólo en el perímetro.
- Presencia de controles de acceso basados en identidad y dispositivo en todos los canales de acceso remoto.[^20][^16][^17]

En otras palabras, desplazar el “tenemos un firewall muy majo” hacia métricas de verificación continua, alineadas con la orientación Zero Trust y compatibles con los requisitos del ENS en materia de control de acceso, autenticación, monitorización y trazabilidad.[^5][^10]

***

### 4. España en el espejo internacional

La comparación mundial es, por definición, ingrata: cada país juega con normas propias, pero todos ven el mismo vendaval. La UE ha articulado su Estrategia de Ciberseguridad alrededor de resiliencia, capacidad operativa y cooperación, apoyada en una inversión multiplicada por cuatro respecto a periodos anteriores. La Comisión Europea insiste en fortalecer la ciberresiliencia y la respuesta coordinada como instrumento de seguridad económica y social, particularmente frente al despliegue de 5G y a la protección de infraestructuras críticas.[^13][^14][^11]

En este coro, el Esquema Nacional de Seguridad sigue siendo una referencia singular: pocos países disponen de una norma de rango reglamentario tan precisa, con guías técnicas complementarias, un órgano especializado (CCN) y una red de capacidades de respuesta. El “agujero” histórico ha sido, precisamente, la dificultad de traducir esa elegancia normativa en cuadros de mando homogéneos, comparables y orientados a riesgo. Desde 2023–2026 se observa una convergencia entre:[^9][^7][^1]

- ENS y guías STIC (norma y controles).[^7][^10]
- IMC de resciliencia (métrica detallada reusable).[^6][^4]
- Marcos internacionales (NIST CSF, Zero Trust, indicadores tipo WEF).[^16][^17][^12]
- Iniciativas sectoriales y de CISOs para estandarizar KPIs/KRIs.[^19][^3]

Dicho de otro modo: la “materia prima” para un MARGA‑ENS ya existe y es comparable con la de los países de referencia. Falta —y presumiblemente el marco que mencionas pretende aportar— la partitura común que permita orquestar los indicadores de todos los organismos públicos y proveedores relevantes de forma consistente, trazable y explotable tanto a escala nacional como europea.

***

### 5. Hacia un Informe MARGA‑ENS: propuesta de arquitectura

Si tu objetivo es elaborar un Informe MARGA‑ENS con aplicación territorial en España y vocación comparativa mundial, una estructura coherente podría ser:

1. **Marco conceptual y normativo.** Posicionar ENS, Real Decreto 311/2022, guías STIC 800, IMC de INCIBE y estrategias europeas como fundaciones del marco.[^14][^5][^11][^1][^7][^4]
2. **Metamodelo de indicadores.** Adoptar la taxonomía de las IMC (metas como Anticipar, Resistir, Recuperar) y las categorías ENS (organización, protección, detección, respuesta, recuperación), cruzándolas con KPIs/KRIs de aceptación internacional (MTTD, MTTR, pérdida esperada, etc.).[^18][^3][^6][^4]
3. **Catálogo nacional MARGA‑ENS.** Seleccionar un subconjunto de indicadores “de país” que todos los organismos ENS deban reportar, capitalizando las fichas existentes (como A‑PC‑OG1‑01) y los indicadores de eficacia operativa.[^18][^4]
4. **Modelo de agregación y comparación.** Definir cómo se agregan y normalizan datos por sector y territorio, y cómo se alinean con los marcos europeos (por ejemplo, reportes NIS2, ejercicios de ciberresiliencia de la UE).[^11][^14]
5. **Gobernanza y ciclo de mejora.** Establecer quién consolida, valida y analiza los indicadores (CCN, INCIBE, departamentos sectoriales) y cómo se vinculan a decisiones de política pública, inversión y priorización de capacidades.[^19][^9][^2]

Todo ello, naturalmente, con una buena dosis del tono irónico‑constructivo que merece el asunto: no se trata de diseñar el enésimo “powerpoint de madurez”, sino de aceptar que los indicadores no son un fin en sí mismos sino un mecanismo para que el ENS deje de ser, en algunos ámbitos, una liturgia y pase a ser una práctica empírica.

***

### 6. Limitaciones y líneas de investigación

Conviene cerrar con una advertencia metodológica clara: el nombre “MARGA‑ENS” como tal no aparece, en abierto, en la documentación oficial del CCN, del Ministerio o de INCIBE, ni en artículos académicos de acceso público bajo esa sigla exacta. Eso implica dos cosas:[^9][^1][^7][^4]

1. Cualquier intento de describirlo en detalle es necesariamente reconstructor: se apoya en marcos, guías e iniciativas públicas existentes, pero no puede citar un texto normativo concreto llamado “MARGA‑ENS”.
2. La investigación rigurosa sobre indicadores de ENS desde 2025 debe apoyarse en piezas adyacentes: IMC de INCIBE, guías STIC 800/81x, estrategias sectoriales de ciberseguridad y las corrientes internacionales en Zero Trust, resiliencia y métricas de riesgo.[^17][^16][^12][^14][^6][^4]


<span style="display:none">[^21][^22][^23][^24][^25][^26][^27][^28][^29][^30]</span>

<div align="center">⁂</div>

[^1]: https://portal.mineco.gob.es/es-es/ministerio/estrategias/Paginas/Esquema_Nacional_de_Seguridad.aspx

[^2]: https://ens.ccn.cni.es/es/conformidad/proceso-de-adecuacion

[^3]: https://www.ismsforum.es/noticias/2436/impulsando-la-ciberseguridad-estrat-gica-hacia-un-marco-estandarizado-de-indicadores-para-cisos/

[^4]: https://www.incibe.es/sites/default/files/contenidos/guias/IMC/imc_02_diccionario-indicadores_2023.pdf

[^5]: https://www.boe.es/buscar/doc.php?id=BOE-A-2022-7191

[^6]: https://www.incibe.es/sites/default/files/contenidos/guias/IMC/imc_02_diccionario-indicadores.pdf

[^7]: https://ens.ccn.cni.es/es/normativa

[^8]: https://ens.ccn.cni.es/es/inicio

[^9]: https://ens.ccn.cni.es/es/

[^10]: https://www.pmg-ssi.com/2025/11/siglas-ens-esquema-nacional-seguridad/

[^11]: https://digital-strategy.ec.europa.eu/es/policies/cybersecurity-strategy

[^12]: https://noushuman.com/ciberseguridad-en-2026-por-que-la-resiliencia-digital-es-ya-una-prioridad-estrategica/

[^13]: https://www.acta.es/medios/informes/2022001.pdf

[^14]: https://www.bittnet.ro/es/noutati/strategia-comisiei-europene-pentru-consolidarea-rezilientei-cibernetice-in-ue/

[^15]: https://www.sanidad.gob.es/areas/saludDigital/doc/20250701_Estrategia_de_Ciberseguridad_del_SNS_vF2.pdf

[^16]: https://revistas.ugm.cl/index.php/rnodos/article/view/724

[^17]: https://www.ibm.com/es-es/think/insights/the-evolution-of-zero-trust-and-the-frameworks-that-guide-it

[^18]: https://www.qualoom.es/indicadores-clave-kpis-para-medir-la-eficacia-de-tu-estrategia-de-ciberseguridad/

[^19]: https://www.deloitte.com/es/es/services/consulting/research/estado-ciberseguridad.html

[^20]: https://www.incibe.es/incibe-cert/blog/metodologia-zero-trust-fundamentos-y-beneficios

[^21]: https://www.dsn.gob.es/sites/default/files/documents/ACCESIBLE MAQUETA IASN2023.pdf

[^22]: https://espanadigital.gob.es/ca/actualidad?f[0]=%3ACiberseguridad\&search_api_fulltext=\&sort_bef_combine=title_ASC\&sort_by=title\&sort_order=DESC\&page=179

[^23]: https://www.incibe.es/sites/default/files/paginas/red-excelencia/estudios-caracterizacion/201701_catalogo.pdf

[^24]: https://www.escudodigital.com/ciberseguridad/las-empresas-en-espana-carecen-de-ciberseguros-los-datos-personales-del-gobierno-de-nuevo-filtrados-y-las-claves-de-por-que-israel-es-una-potencia-en-ciberespionaje.html

[^25]: https://www.ismsforum.es/noticias/2486/2025-las-organizaciones-refuerzan-sus-estrategias-de-ciberseguridad-en-el-marco-de-adaptaci-n-a-la-nis2/

[^26]: https://www.ciset.es/publicaciones/blog/892-proteger-tu-empresa-de-ciberataques-riesgo-humano

[^27]: https://www.studocu.com/co/document/unir-colombia/gobierno-de-la-ciberseguridad-y-analisis-de-riesgos/ens-815-guia-de-metricas-e-indicadores-del-esquema-nacional-de-seguridad/145577500

[^28]: https://ens.ccn.cni.es/en/home

[^29]: https://angeles.ccn-cert.cni.es/es/

[^30]: https://datos.gob.es/es/catalogo/ea0044367-indicadores-de-iniciativa-marco-de-red-es-seleccionada-campus-en-red-programa-finalizado

