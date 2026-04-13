
# Informe INES - ENS.

El INES no es un simple formulario: es el espejo nacional donde el ENS se mira cada año para saber si progresa adecuadamente… o si sigue repitiendo curso en ciberseguridad. A partir de 2022–2025, ese espejo se ha pulido, alineado con NIS2 y endurecido frente a proveedores privados, elevando la discusión sobre indicadores desde el “checklist” a la gobernanza real del riesgo a escala país.[^1][^2][^3][^4][^5][^6][^7]

## 1. Qué mide realmente INES dentro del ENS

El punto de partida está escrito negro sobre blanco: el ENS obliga a medir la seguridad de forma periódica y con un sistema de indicadores que cubra, como mínimo, tres dimensiones: grado de implantación de medidas, eficacia y eficiencia de esas medidas e impacto de los incidentes. Esa exigencia, plasmada originalmente en el artículo 35 del ENS y actualizado en el Real Decreto 311/2022, es la génesis del proyecto INES, concebido por el CCN como plataforma telemática para recoger, consolidar y analizar indicadores de seguridad de todas las Administraciones y, desde 2022, también de un buen trozo del tejido privado que les da servicio.[^2][^3][^4][^8][^1]

La Guía CCN‑STIC 815 “Métricas e Indicadores en el ENS” y la 824 “Informe del Estado de Seguridad” funcionan como el “manual de estilo” de estos indicadores: la primera define el marco de métricas, tipos de indicadores y cuadros de mando típicos; la segunda aterriza qué se pide, para qué se pide y cómo se agregan los datos que nutren el Informe Nacional del Estado de Seguridad. Ambas insisten en que no se trata de inventariar controles, sino de medir desempeño: uso explícito de modelos de madurez (CMM), indicadores de cumplimiento y de eficacia, tasas de incidentes y tiempos de gestión, todo ello alineado con las cinco dimensiones del ENS (confidencialidad, integridad, disponibilidad, autenticidad y trazabilidad).[^9][^10][^11][^8][^12][^13][^14]

El CCN ha rodeado este núcleo métrico con un ecosistema de gobernanza: INES, AMPARO y PILAR aparecen como herramientas oficiales de soporte a la adecuación, análisis de riesgos y seguimiento, integradas en el portal del ENS como instrumental estándar para quienes quieran algo más que un “PowerPoint de buenas intenciones”. El resultado es que el Informe INES deja de ser una curiosidad documental y se convierte en mecanismo regular de supervisión, insumo para auditorías, certificaciones ENS (CoCENS) e, indirectamente, para la planificación de inversión y continuidad de negocio de las entidades públicas.[^15][^16][^11][^17][^18][^2]

### Tabla: Ámbitos básicos que cubren los indicadores ENS–INES

| Dimensión ENS | Tipo de indicador en INES | Ejemplo sintético |
| :-- | :-- | :-- |
| Implantación de medidas | Madurez y cumplimiento | Porcentaje de medidas ENS implantadas por categoría de sistema[^3][^11] |
| Eficacia y eficiencia | Desempeño operativo | Reducción de incidentes graves por 1000 activos en 12 meses[^3][^8] |
| Impacto de incidentes | Riesgo materializado | Servicios críticos afectados y tiempo medio de recuperación[^3][^8] |
| Interconexiones | Protección de flujos y dependencias | Número de enlaces críticos con controles ENS ‘alto’ efectivos[^19][^8] |
| Gobernanza y madurez | Modelo tipo CMM, agregados de madurez por dominio | Nivel 1–5 en gestión de identidades, continuidad, proveedores[^8][^13] |

## 2. Anatomía de los indicadores INES (versión 2025, sin maquillaje)

Si uno desmenuza las guías 815 y 824, lo que aparece es una arquitectura de indicadores en varios niveles, pensada para que un ministerio pequeño y una consejería autonómica mastodóntica puedan hablar el mismo idioma sin colapsar de Excel. En la base están las métricas elementales (número de sistemas en categoría alta, número de usuarios privilegiados, cantidad de incidentes por tipología), que se combinan en indicadores compuestos y, finalmente, en indicadores agregados de madurez y conformidad usados por auditores y órganos de control externo.[^11][^8][^12][^13][^17]

Los indicadores básicos giran en torno a cuatro bloques, con una obstinada vocación de torpedear la auto‑complacencia:

- Medidas de seguridad: porcentaje de medidas ENS implantadas, documentadas, verificadas y auditadas por familia (organización, protección, detección, recuperación, etc.).[^3][^8][^11]
- Incidentes y ciberresiliencia: número y gravedad de incidentes, tiempo medio de detección y resolución, recurrencia de causas raíz, impacto en servicios críticos y capacidad de recuperación frente a objetivos de continuidad.[^20][^8][^3]
- Interconexiones y proveedores: nivel de protección en conexiones con otras entidades y terceros, existencia de acuerdos de nivel de servicio y cláusulas de seguridad, dependencia de servicios externalizados clave.[^19][^8][^21]
- Madurez de gestión: adopción de políticas, existencia de roles formales de seguridad, frecuencia de auditorías, uso de herramientas del CCN y grado de automatización de la monitorización y respuesta.[^8][^22][^15]

A partir de ahí, la Guía 824 define indicadores agregados de madurez y cumplimiento que permiten emitir juicios sintéticos sobre el “estado de la casa”: una serie de índices resumen, utilizados ya por órganos de control como sindicaturas de cuentas autonómicas, que cruzan cumplimiento ENS, eficacia de controles e incidentes relevantes para pintar un semáforo estratégico. Lo interesante es que el modelo no se queda en la foto fija: se explicita su uso para análisis de tendencia (comparación anual obligatoria) y para la priorización de medidas en los planes de acción de seguridad.[^12][^17][^2][^3][^11][^8]

En el plano operativo, la herramienta INES automatiza parte de este proceso: soporta la captura de datos, determina métricas, extrae conclusiones y, atención, realiza prospectivas sobre el futuro de la seguridad, incluyendo la generación automatizada de una declaración de conformidad para categoría básica del ENS y el soporte a la documentación necesaria para adecuación y auditoría. Esa automatización, lejos de ser un lujo, es el único modo de que un país entero rellene el boletín de notas de su ciberseguridad sin colapsar en la burocracia.[^10][^2][^3]

## 3. Tendencias recientes (2025–2026): de “cumplir” a “evidenciar”

Desde la actualización del ENS por el Real Decreto 311/2022 y la ampliación de obligaciones de reporte a entidades privadas que prestan servicios al sector público, el Informe INES ha ido mutando discretamente de examen interno a instrumento de gobernanza sectorial y de alineamiento con las exigencias europeas (NIS2, Directiva 2022/2555). Organizaciones especializadas en ENS subrayan que, desde esta reforma, empresas privadas que gestionan sistemas clasificados o servicios clave para la Administración están obligadas a cumplimentar el Informe INES, transformando el mapa de contribuyentes a la métrica nacional.[^4][^6][^7][^1][^2]

En paralelo, la propia administración sanitaria estatal habla ya de “alinear INES con otros índices” como el Índice SEIS y de emplear estas métricas para establecer líneas base de madurez de ciberseguridad del Sistema Nacional de Salud, lo que muestra el desembarco de INES en sectores críticos concretos con dinámicas propias. Esa misma lógica sectorial se observa en nuevos marcos autonómicos de gobernanza de ciberseguridad pública instrumental, que citan de forma expresa el Informe INES como pieza obligatoria junto a auditorías ENS y otras pruebas de cumplimiento, integrándolo en un ciclo de gestión del riesgo que va mucho más allá del ministerio clásico.[^23][^17][^20][^11]

En términos de contenido, el énfasis reciente se desplaza hacia indicadores que captan:

- Resiliencia operacional: continuidad de servicios críticos, tiempos de recuperación en ataques complejos (ransomware, ataques a la cadena de suministro), dependencia de servicios externos y nube.[^21][^2][^20]
- Gestión de terceros y cadena de suministro, en coherencia con la presión de NIS2 sobre proveedores y la expansión de sectores críticos cubiertos por la normativa europea (de 7 a 15 sectores).[^6][^7][^21]
- Gobernanza y rendición de cuentas: roles de ciberseguridad formalizados, frecuencia de reporting al máximo órgano de gobierno y grado de alineamiento con estrategias sectoriales y nacionales.[^24][^16][^20]

En resumen, el “desde 2025” no inventa indicadores exóticos, pero sí reordena prioridades: de la lista de controles al relato de madurez, resiliencia y responsabilización, con el Informe INES como narrador de fondo.

## 4. España (INES–ENS) frente al mundo: el encanto discreto del indicador público

Si ponemos España en el escaparate internacional, el dueto ENS–INES resulta menos “excéntrico” de lo que a veces se cree y más parecido a varias tendencias globales, con un matiz ibérico inconfundible: un énfasis notable en la normalización pública, la centralización metódica de métricas y la articulación de guías detalladas por un CERT nacional especializado (el CCN). La lógica de fondo se asemeja mucho al espíritu de NIS2: establecer un nivel común elevado de ciberseguridad, ampliar el perímetro de entidades obligadas, enfocarse en riesgo, resiliencia y reporte estructurado de incidentes, y reforzar las capacidades sancionadoras y de supervisión de autoridades nacionales.[^25][^16][^7][^22][^15][^6][^21]

En otros países de la UE, la métrica se expresa en marcos inspirados en ISO 27001, NIST CSF y controles CIS, con indicadores de riesgo y madurez que resuenan con lo que la Guía 815 ya definía hace años: indicadores de implantación de controles, eficacia operacional, impacto de incidentes y cuadros de mando ejecutivos que permiten comparaciones temporales y sectoriales. La diferencia española es la institucionalización: mientras muchos países recomiendan marcos, España impone un esquema (ENS) y articula una herramienta concreta (INES), con guías STIC específicas que descienden al detalle de qué preguntar, qué sumar y cómo presentar resultados a nivel país.[^14][^15][^3][^8][^6][^21]

Más allá de Europa, el enfoque INES se aproxima a iniciativas nacionales de medición de ciberresiliencia que cruzan datos incidentales, indicadores de madurez y métricas de cumplimiento en sectores críticos, aunque en otros contextos suelen aparecer como marcos consultivos o programas voluntarios más que como obligación reglamentaria generalizada. Desde la perspectiva de un CISO global, el ENS–INES se percibe como un caso interesante de “regulación prescriptiva de métricas”, donde el Estado entra hasta la cocina de la medición, no solo de los requisitos, lo que tiene ventajas de homogeneidad y comparabilidad, y el inevitable coste de una cierta rigidez burocrática.[^7][^6][^21]

### Tabla: ENS–INES frente a marcos internacionales de indicadores

| Elemento clave | ENS–INES (España) | Tendencia internacional (ej. NIS2, NIST, ISO) |
| :-- | :-- | :-- |
| Naturaleza del marco | Regulatorio, obligatorio para sector público y ciertos privados[^1][^4] | Híbrido: leyes marco + estándares de referencia voluntarios[^6][^21][^7] |
| Herramienta de indicadores | Plataforma estatal específica (INES) con guías STIC detalladas[^3][^8][^14] | Herramientas variadas, muchas de mercado, sin una plataforma nacional única[^6][^21] |
| Foco métrico central | Implantación ENS, eficacia, incidentes y madurez de gestión[^3][^11][^8] | Riesgo ciber, resiliencia, incidentes significativos y cumplimiento básico[^6][^21] |
| Alcance de entidades | AP + proveedores del sector público y sistemas clasificados[^1][^2][^4] | Operadores esenciales/importantes, sectores críticos y operadores de servicios digitales[^6][^21][^7] |
| Grado de prescripción | Alto: indicadores sugeridos y cuadros de mando tipo en guías CCN[^8][^12][^17] | Medio: orientaciones genéricas, alto margen de diseño local de métricas[^6][^21] |

## 5. Propuestas propositivas (con un toque de ironía) para evolucionar indicadores ENS–INES

Si asumimos que el objetivo no es sólo “aprobar el ENS”, sino demostrar resiliencia digital y continuidad de país ante amenazas cada vez más creativas, los indicadores ENS–INES tienen margen para una cierta revolución silenciosa. Una primera línea de avance es reforzar los indicadores que capturan dinámicas, no fotos: métricas de tiempo (mean time to detect, respond, recover), frecuencia de pruebas de continuidad en escenarios adversos plausibles (cortafuegos caído, proveedor cloud indisponible, cadena de suministro comprometida) y velocidad de despliegue de parches críticos en activos clave.[^2][^20][^21]

Otra línea es integrar explícitamente indicadores de riesgo actuarial y económico, algo que NIS2 insinúa cuando exige gestión de riesgos más madura, cadena de suministro vigilada y responsabilidad directa de la alta dirección, pero que rara vez se aterriza en cuadros de mando nacionales. Sería perfectamente coherente con la filosofía de la Guía 815 incorporar métricas que cuantifiquen pérdidas evitadas, exposición residual tras controles e impacto económico de interrupciones significativas, a partir de los datos de incidentes que ya recoge INES.[^3][^8][^6][^21][^7]

También resultaría natural, en plena fiebre de IA y computación cuántica, extender los indicadores a dominios emergentes: nivel de preparación ante criptografía post‑cuántica, dependencia de algoritmos vulnerables, grado de adopción segura de IA (modelos, datos, cadena MLOps) y capacidad para monitorizar riesgos algorítmicos como parte del estado de seguridad global. El ENS ya contempla la autenticidad y la trazabilidad como dimensiones formales; no costaría mucho traducir eso en indicadores sobre integridad de modelos, trazabilidad de decisiones automatizadas y resiliencia de las infraestructuras que los alojan.[^9][^4][^6][^21][^7]

Desde la óptica comparativa internacional, España puede permitirse el lujo de ir un paso más allá y abrir parcialmente las métricas ENS–INES (al menos en forma agregada y anonimizada) para fomentar benchmarking público entre sectores y territorios, algo que elevaría la conversación desde el “cumplo/no cumplo” al “dónde estoy respecto a mis iguales” y alinearía la cultura ENS con iniciativas de transparencia en ciberresiliencia observadas en otros países. Después de todo, la única cosa más incómoda que un cuestionario anual del CCN es ver en un ranking que tu organización lleva tres años sin mejorar un miserable semáforo.[^24][^25][^6][^21]


<span style="display:none">[^26][^27][^28][^29]</span>

<div align="center">⁂</div>

[^1]: https://www.govertis.com/entidades-privadas-deben-comunicar-informe-ines

[^2]: https://ingertec.com/informe-ines-obligatorio-en-empresas-privadas/

[^3]: http://ens.unizar.es/informe-ines

[^4]: https://www.boe.es/buscar/doc.php?id=BOE-A-2022-7191

[^5]: http://femp.femp.es/files/566-1808-archivo/INES.docx

[^6]: https://leaf-it.com/navigating-nis2-2025/

[^7]: https://www.nis-2-directive.com

[^8]: https://es.scribd.com/document/128625444/815-Metricas-e-Indicadores-ENS

[^9]: https://www.youtube.com/watch?v=B7-93DyIEQM

[^10]: https://www.ismsforum.es/ficheros/descargas/ccn-stic-808.pdf

[^11]: https://www.ccontasgalicia.es/sites/consello_de_contas/files/contents/documents/2026/RESUMEN_EJECUTIVO_CBCS_AYUNTAMIENTO_DE_LUGO_C_0.pdf

[^12]: https://www.sindicom.gva.es/public/Attachment/2020/3/inf-cbcs-2019-ay-torrent-09-final-definitivo_signed.pdf

[^13]: https://es.scribd.com/document/348825703/Ccn-Stic-824-Ens-Informe-Ines

[^14]: https://ru.scribd.com/document/862996814/El-Esquema-Nacional-de-Seguridad-2docx

[^15]: https://ens.ccn.cni.es/es/

[^16]: https://www.preparatic.org/blog/wp-content/uploads/2024/11/20241110-Preparatic-MIGUEL-A-AMUTIO-99-rev.pdf

[^17]: https://www.sindicatura.cat/documents/36414/85841/2024_16_es.pdf

[^18]: https://ens.ccn.cni.es/gl/

[^19]: https://www.nunsys.com/ines-la-importancia-de-la-seguridad-en-la-administracion-publica/

[^20]: https://www.sanidad.gob.es/areas/saludDigital/doc/20250701_Estrategia_de_Ciberseguridad_del_SNS_vF2.pdf

[^21]: https://www.cocus.com/en/nis-2-which-companies-need-to-act-by-2025/

[^22]: https://www.preparatic.org/material/20151031/preparaticXXIII_20151031_s4_ENS.pdf

[^23]: https://www.sindicom.es/public/Attachment/2025/11/gobernanza_ciberseguridad_sector_publico_instrumental_gv_organismos_autonomos_2024_cas_firmado.pdf

[^24]: https://portal.mineco.gob.es/es-es/ministerio/estrategias/Paginas/Esquema_Nacional_de_Seguridad.aspx

[^25]: https://grupoadaptalia.es/blog/esquema-nacional-de-seguridad-que-es

[^26]: https://www.ivap.euskadi.eus/evento/cumplimiento-y-adaptacion-al-ens-8211-esquema-nacional-seguridad-2025-1-5-1/webivap00-a3prtoki/es/

[^27]: https://seleccionisdefe.es/convocatoria-1515

[^28]: https://www.govertis.com/cumplir-con-el-informe-de-estado-de-la-seguridad

[^29]: https://www.applicalia.com/esquema-nacional-de-seguridad-ens-preguntas-y-respuestas-para-entender-donde-estas-y-que-te-queda-por-hacer/

