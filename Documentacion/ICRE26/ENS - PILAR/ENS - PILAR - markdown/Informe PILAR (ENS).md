
# Informe PILAR (ENS).

El marco PILAR-ENS ha cristalizado, desde 2025, en un sistema de indicadores que ya no se limita a “hacer un análisis de riesgos”, sino a **medir** de forma continua madurez, riesgo y cumplimiento frente al ENS como si fueran KPIs de negocio con traje criptográfico y corbata de auditoría.[^1][^2][^3][^4][^5]

## De qué indicadores estamos hablando realmente

PILAR no inventa el riesgo, pero sí lo domestica en forma de números: niveles de 0 a 10 para requisitos de seguridad de los activos, niveles L0–L5 para madurez de salvaguardas y controles, probabilidades e impactos parametrizados, y un semáforo que traduce todo eso a un rojo/ámbar/verde muy comprensible para el comité de dirección.[^2][^1]

Para los activos esenciales, la herramienta obliga a valorar la “demanda” de seguridad entre 0 (despreciable) y 10 (máxima) en cada dimensión: confidencialidad, integridad, disponibilidad, autenticidad, trazabilidad y, cuando corresponde, privacidad de datos personales.  Esa cuadrícula de números por activo y por dominio de seguridad se ha convertido, en la práctica, en uno de los indicadores estructurales del ENS: expresa qué está realmente en juego antes de hablar de amenazas o controles.[^4][^1][^2]

Sobre este lienzo, PILAR aplica perfiles estándar de amenazas y calcula riesgos potenciales y residuales, directos sobre activos de soporte e indirectos o repercutidos sobre activos de negocio; es decir, el mapa de “cuánto valor se nos puede evaporar” por cada combinación de activo, amenaza y dimensión de seguridad.  El resultado son indicadores de riesgo que se pueden explotar tanto en clave técnica como de negocio, algo muy alineado con la filosofía del ENS actualizado y su énfasis en gestión de riesgos documentada y proporcional.[^5][^1][^2][^4]

## Madurez como métrica troncal (L0–L5, CMM en versión ENS)

Desde 2025, los manuales de PILAR empujan claramente hacia una lectura basada en madurez de salvaguardas y controles, reutilizando un modelo tipo CMM (L0–L5) que ya no es sólo narrativa de auditor, sino fuente de indicadores cuantitativos.[^1][^2]

Los niveles son:

- L0 inexistente: ni rastro de la medida.
- L1 ad hoc: hay algo, pero depende de buena suerte y héroes puntuales.
- L2 reproducible intuitivo: la organización repite éxitos, pero sin proceso robusto.
- L3 proceso definido: políticas, procedimientos y mantenimiento sistemático.
- L4 gestionado y medible: la dirección controla empíricamente eficacia y efectividad.
- L5 optimizado: mejora continua con objetivos cuantitativos y ajustes periódicos.[^2][^1]

La gracia moderna está en cómo se explotan estos niveles:

- Se miden por fase de proyecto (situación actual, objetivo, recomendación de PILAR), permitiendo ver la evolución temporal de la seguridad.[^1][^2]
- Se pueden reinterpretar como porcentaje de efectividad o comparar “madurez real” frente a la recomendación de la herramienta, lo que convierte el nivel en un KPI directamente consumible por dirección.[^2][^1]
- Se mantiene la distinción entre madurez técnica de salvaguardas y madurez formal de controles, lo que deja espacio para que la vida real (controles parcialmente implantados, normas algo anacrónicas) se exprese en forma de dos números, no en discusiones metafísicas.[^2]

En el contexto ENS, donde el real decreto exige gestión periódica del riesgo con medidas justificadas y proporcionales, esta madurez numérica funciona como indicador de “cuán sólidamente” están implantadas las medidas del anexo II más allá de la mera existencia documental.[^4][^5]

## Semáforos, recomendaciones y el arte de priorizar

PILAR sabe que la alta dirección no va a leer cien páginas de detalles técnicos, de modo que introduce una batería de indicadores pensados para priorizar sin necesidad de lupa:

- Recomendación (0–10): la herramienta estima la importancia relativa de cada medida de seguridad, teniendo en cuenta activos, niveles de seguridad requeridos y riesgos que trata.  Una celda gris indica que la medida no tiene, para ese sistema, ningún riesgo evidente al que agarrarse; es un “esto aquí no pinta nada” cuantificado.[^1][^2]
- Overkill (o) y underkill (u): etiquetas que señalan cuando una medida parece desproporcionada (más allá de lo necesario) o claramente insuficiente frente a los riesgos identificados.  Como indicadores, convierten discusiones bizantinas sobre controles “excesivos” o “muy caros” en cuestiones relativamente objetivables.[^1][^2]
- Aplicabilidad: la columna en la que se indica si cada control o salvaguarda es aplicable o no, con la particularidad de que PILAR conserva un color distintivo cuando se marca “no aplicable” un control que la norma considera obligatorio, exponiendo la excepcionalidad para futuras auditorías.[^2][^1]

El semáforo combina estos elementos con las fases de madurez:

- Se designa una fase objetivo (cabecera verde) y una fase evaluada (cabecera roja).
- Para cada medida, el color azul indica que la madurez actual está por encima del objetivo, verde que está a la altura, amarillo que va por debajo y rojo que está sensiblemente por debajo; gris, de nuevo, es no aplicable.[^1][^2]

Lo relevante en clave ENS es que este semáforo ya no es un mero adorno gráfico: se ha convertido en indicador sintético de cumplimiento y de riesgo residual, porque refleja en una sola vista cuántas medidas críticas (por peso) están en rojo o amarillo en los dominios donde la exposición de activos es mayor.[^3][^4][^2][^1]

## Dominios, dependencias y riesgos repercutidos: indicadores de arquitectura y exposición

Una de las tendencias técnicas más notables, que casa muy bien con Zero Trust sin necesidad de nombrarlo, es el uso intensivo de dominios de seguridad, zonas y dependencias como base de indicadores sobre arquitectura y superficie de ataque.[^3][^2][^1]

Los dominios de seguridad agrupan activos con un perfil de ataque y de protección homogéneo, y permiten heredar niveles de madurez de salvaguardas entre dominios padre e hijo.  Esto no sólo reduce trabajo operativo: crea indicadores de cobertura “por dominio” que se parecen sospechosamente a las métricas de segmentación de redes en arquitecturas modernas, donde no basta con tener un firewall, sino con demostrar que los niveles de protección están alineados con los requisitos de los activos anidados.[^2][^1]

Las dependencias entre activos permiten refinar la transferencia de valor y de requisitos de seguridad, evitando el supuesto ingenuo de que todos los servidores son igual de críticos para todas las informaciones.  Esto da lugar a indicadores más finos:[^2]

- Riesgo acumulado sobre activos de soporte concretos: qué suma de valor “pasa” por cada hardware, software, red, instalación, usuario.
- Riesgo repercutido hacia activos esenciales: cuánta repercusión hacia negocio tiene cada amenaza que impacta un activo aparentemente “de infraestructura”.[^2]

Con la introducción de nodos OR, PILAR puede diferenciar caminos alternativos de provisión de servicio, evitando trasladar mecánicamente requisitos de disponibilidad a todos los elementos cuando existe redundancia.  Esto se traduce en indicadores más inteligentes sobre puntos únicos de fallo, que son oro puro para la resiliencia digital y la continuidad de negocio.[^2]

La noción de zonas (lógicas, físicas, TEMPEST) permite además un análisis de defensa en profundidad que desemboca en indicadores sobre:

- Cantidad y criticidad de activos en cada zona.
- Robustez de las fronteras, modeladas como activos que concentran perfiles de ataque y salvaguardas específicas.[^1][^2]

En un ENS donde la protección perimetral clásica convive con entornos híbridos, estas métricas de zonas y fronteras se integran de facto como indicadores de “arquitectura segura”, incluso cuando el texto legal no entra tan fino.[^5][^4]

## Perfiles de seguridad, ENS y cumplimiento medible

PILAR incorpora perfiles de seguridad alineados con normas internacionales (ISO 27002, NIST SP 800‑53) y con perfiles específicos (EVL, CCN-STIC) que permiten medir simultáneamente tratamiento del riesgo y cumplimiento normativo.[^6][^3][^1][^2]

En el ámbito ENS, el fichero de configuración STIC y los perfiles asociados son el puente explícito: permiten cargar conjuntos de controles equivalentes a las medidas del anexo II y valorar su madurez, aplicabilidad y recomendación con la misma semántica de L0–L5 y semáforos.  El resultado es un conjunto de indicadores de cumplimiento tales como:[^3][^4][^2]

- Porcentaje de medidas ENS marcadas como aplicables que se encuentran en nivel de madurez igual o superior al recomendado.
- Número de controles obligatorios marcados como no aplicables, con sus correspondientes comentarios, algo extremadamente visible para inspecciones y procesos de certificación.[^2]

La separación entre madurez formal de los controles y madurez real de las salvaguardas asociadas es otra tendencia significativa: permite que los indicadores distingan entre el “expediente” (lo que se declara en documentos de cumplimiento) y la efectividad práctica (lo que realmente reduce el riesgo en el sistema).  Poder mostrar, por ejemplo, un control valorado formalmente en L3 mientras las salvaguardas asociadas están en un rango L1–L5 introduce un saludable grado de honestidad cuantitativa que los comités de riesgo valoran cada vez más.[^2]

Finalmente, el tratamiento del riesgo en PILAR admite usar distintos catálogos de salvaguardas (propias, NIST, perfiles EVL) como base de las decisiones de mitigación; el hecho de poder decidir cuáles se usan para tratar el riesgo y cuáles se limitan a cumplimiento añade capas de indicadores diferenciando lo que se hace “para bajar el riesgo” de lo que se hace “para pasar la auditoría”.[^2]

## Tendencias desde 2025: más cuantificación, más automatización, más alineamiento ENS

Si uno mira el manual 2025 de PILAR y las actualizaciones recientes del soporte ENS, se perciben varias tendencias convergentes.[^7][^4][^5][^3][^1][^2]

Primero, la consolidación de indicadores cuantitativos: no sólo riesgo como producto de probabilidad e impacto, sino madurez, recomendación, pesos de salvaguardas (crítica, muy importante, importante, interesante) y métricas derivadas como porcentaje de efectividad.  Esta proliferación no es caprichosa: responde a la necesidad de métricas e indicadores de ciberseguridad para la toma de decisiones estratégicas, que el propio portal ENS subraya como requisito para conocer el estado de seguridad de los sistemas que soportan la Administración digital.[^7][^5][^1][^2]

Segundo, una automatización más agresiva: la transferencia de valor de activos esenciales a activos de soporte, la aplicación de perfiles estándar de amenaza (TSV o similares), la sugerencia de salvaguardas en función de clase de activo, niveles de seguridad y capacidades de protección, e incluso el cálculo de recomendaciones y colores de semáforo se realizan de forma automática, dejando al analista en el rol de corrector, no de “calculadora humana”.  Esta tendencia encaja con el enfoque ENS de gestionar riesgos con metodologías reconocidas y herramientas que permitan repetir análisis y auditar decisiones sin depender de la memoria del consultor.[^4][^5][^3][^1][^2]

Tercero, una integración más clara con el ciclo de vida: las fases de proyecto conectadas, en las que cada fase refina la anterior y la madurez se hereda hasta que se reevalúa, convierten el análisis de riesgos en un proceso continuo.  El ENS, que exige revisión periódica del análisis y de las medidas adoptadas, encuentra aquí una forma natural de expresar ese ciclo en indicadores: cuánto hemos avanzado de la fase “actual” a la fase “objetivo”, qué medidas siguen en rojo tras dos iteraciones, qué dominios han mejorado o empeorado su madurez media.[^5][^4][^2]

Por último, la apertura a catálogos externos (NIST, EVL, CVE) y el uso de bases de datos SQL para almacenar proyectos y resultados amplían el rango posible de indicadores: se pueden construir cuadros de mando agregados, identificar tendencias de vulnerabilidades explotadas, correlacionar riesgos con activos compartidos entre organizaciones y, en resumen, elevar el juego desde el caso individual al análisis sectorial, algo muy del gusto de organismos reguladores y centros de respuesta nacionales.[^8][^6][^3][^2]

<span style="display:none">[^10][^11][^12][^13][^14][^15][^9]</span>

<div align="center">⁂</div>

[^1]: https://www.pilar-tools.com/doc/manual_basic_es_2025.pdf

[^2]: https://ens.ccn.cni.es/es/

[^3]: https://administracionelectronica.gob.es/ctt/pilar

[^4]: https://ens.ccn.cni.es/gl/soporte-ens/real-decreto-311-2022/capitulo/3/articulo/14

[^5]: https://portal.mineco.gob.es/es-es/ministerio/estrategias/Paginas/Esquema_Nacional_de_Seguridad.aspx

[^6]: https://angeles.ccn-cert.cni.es/es/cursos-stic/xviii-curso-analisis-y-gestion-de-riesgos-de-los-sistemas-de-informacion-pilar

[^7]: https://ens.ccn.cni.es/gl/inicio

[^8]: https://www.gtt.es/boletinjuridico/publicadas-las-guias-ccn-stic-sobre-el-analisis-de-riesgos-para-eell-y-sobre-la-declaracion-y-certificacion-de-conformidad-con-el-ens/

[^9]: https://www.pilar-tools.com/doc/manual_rm_es_2025.pdf

[^10]: https://www.cnmv.es/webservices/verdocumento/ver?t={d3fee249-d4e6-42d7-9421-a819a415369b}

[^11]: https://vintegris.com/es/blog/esquema-nacional-de-seguridad-ens-2/

[^12]: https://rightsinternationalspain.org/wp-content/uploads/2022/03/Análisis-de-riesgos-agosto-2020.pdf

[^13]: https://www.pilar-tools.com/doc/manual_bcm_en_20241.pdf

[^14]: https://dialnet.unirioja.es/metricas/investigadores/846286

[^15]: https://dialnet.unirioja.es/descarga/articulo/8276834.pdf

