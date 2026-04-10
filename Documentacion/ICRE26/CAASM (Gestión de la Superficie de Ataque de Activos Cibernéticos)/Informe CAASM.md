
# Informe CAASM.

La CAASM se está consolidando desde 2025 como el “sistema nervioso central” de la gestión de activos y de la superficie de ataque, y sus indicadores evolucionan claramente hacia: visibilidad unificada, riesgo material, alineamiento regulatorio (NIS2, ENS, GDPR) y capacidad de remediación continua. A nivel España, la presión regulatoria UE‑centrada y el peso de sectores esenciales hacen que los indicadores territoriales de CAASM graviten sobre exposición sectorial, criticidad de servicios públicos y madurez de supervisión continua, en sintonía con el enfoque europeo de ENISA y NIS2.[^1][^2][^3][^4][^5][^6]

***

## 1. Qué es CAASM hoy (y qué le exigimos)

- La gestión de la superficie de ataque de activos cibernéticos (CAASM) se basa en descubrir, inventariar y correlacionar todos los activos (TI, OT, IoT, nube, identidades, contenedores, APIs) y sus riesgos en un único “panel de realidad” para el equipo de seguridad.[^7][^2][^3][^1]
- Los fabricantes y analistas coinciden en que CAASM ya no es “un inventario más”, sino un agregador de datos que cruza CMDB, EDR, IAM, nubes, vulnerabilidades y telemetría para construir un inventario vivo y accionable de riesgos de superficie de ataque.[^2][^8][^3][^1][^7]
- Desde 2024–2026, los informes de mercado ven a CAASM como pieza clave del giro desde CMDB tradicional hacia gestión de superficie y exposición, con previsión de fuerte despegue del mercado antes de 2027.[^9][^8][^5][^10][^11]

Ejemplo ilustrativo: si el ministerio X declara en la CMDB 5.000 servidores, el CAASM le dirá que en realidad expone 5.700 superficies lógicas relevantes (incluyendo VMs olvidadas, microservicios huérfanos y APIs fantasma) y qué parte de esa fauna es verdaderamente peligrosa hoy.[^3][^1][^7][^2]

***

## 2. Bloques de indicadores CAASM (visión global)

A partir de las definiciones técnicas de proveedores, guías de ASM y análisis sectoriales, las métricas de CAASM en 2025–2026 se agrupan en cinco familias: visibilidad, higiene y control, exposición y riesgo, ciclo de vida de remediación, y alineamiento normativo.[^12][^13][^11][^1][^7][^2][^3]

### 2.1. Visibilidad y cobertura de activos

Indicadores típicos derivados de las capacidades de descubrimiento y agregación descritas por Tenable, CrowdStrike, Zscaler, Vectra y otros:[^14][^13][^11][^1][^7][^2][^3]

- Porcentaje de activos descubiertos vs activos estimados (ratio de “oscuridad” de la superficie de ataque).
- Proporción de TI invisible / “shadow IT” detectada (activos no inventariados que aparecen en escaneos CAASM).
- Cobertura de activos por dominio: TI tradicional, OT, IoT, nube (IaaS/PaaS/SaaS), identidades, contenedores/Kubernetes, APIs e interfaces externas.[^13][^1][^7][^2][^12][^3]
- Grado de integración de fuentes (número y tipo de conectores activos: CMDB, EDR, IAM, nube, escáner de vulnerabilidades, SIEM, etc.).[^1][^7][^2][^12][^3]
- Actualidad de los datos: latencia media de actualización de inventario, porcentaje de activos con datos “stale”.[^7][^2][^3][^1]


### 2.2. Higiene de seguridad y controles

Alineado con la capa de validación de controles que describen Tenable y otros fabricantes:[^11][^2][^12][^13][^3]

- Porcentaje de activos protegidos por EDR/XDR, cifrado, gestión de parches, MFA y microsegmentación declarados y realmente aplicados (validado por CAASM).
- Densidad de activos con configuraciones inseguras (puertos expuestos, servicios inseguros, cifrados débiles, identidades sin MFA, etc.).[^2][^13][^3][^7]
- Cobertura de políticas Zero Trust a nivel de activos: porcentaje de activos integrados en políticas de acceso basado en identidad y contexto.[^14][^12][^3]
- Número de brechas de control por activo crítico (activos marcados como críticos sin todos los controles exigidos por el marco interno o normas como NIS2/ENS).


### 2.3. Exposición y riesgo material

Las guías recientes enfatizan que CAASM debe ir más allá del CVSS bruto y acercarse a riesgo material, apoyándose en inteligencia de amenazas y modelos como EPSS.[^4][^12][^13][^3][^7][^2]

- Activos con vulnerabilidades explotables (según EPSS, inteligencia de amenazas o explotación observada).[^3][^4][^7][^2]
- “Toxic combinations”: activos donde convergen alta criticidad de negocio, exposición externa y vulnerabilidades o fallos de control de alto impacto.[^12][^13][^2][^3]
- Superficie de ataque externa vs interna (número y criticidad de activos expuestos a Internet, terceros o redes interconectadas).[^6][^13][^3]
- Riesgo agregado por dominio (TI, OT, nube, identidades, APIs) ponderado por impacto de negocio, en línea con la priorización recomendada por ASM/CAASM.[^13][^1][^2][^12][^3]


### 2.4. Remediación y capacidad de respuesta

Las mejores prácticas de ASM subrayan que la métrica relevante ya no es “cuántas vulnerabilidades tengo”, sino “con qué cadencia y eficacia cierro las que importan”.[^11][^12][^13][^3]

- MTTR de exposición (tiempo medio para mitigar exposición relevante, no solo aplicar parches).
- Porcentaje de exposiciones críticas cerradas dentro de los SLA internos (por ejemplo, 7 días para exposiciones de alto riesgo).
- Tasa de recurrencia: exposiciones críticas que reaparecen tras una remediación teórica (indica falta de control estructural).[^12][^13][^3]
- Grado de automatización de remediación: porcentaje de exposiciones cerradas mediante flujos orquestados frente a tareas manuales.[^13][^3][^11][^12]


### 2.5. Cumplimiento y reporting

Los proveedores apuntan a que CAASM se está integrando de forma nativa con marcos como NIST, ISO 27001, GDPR y las directivas europeas.[^4][^1][^2][^3][^12]

- Trazabilidad de controles frente a marcos NIST SP 800‑53, ISO 27001, NIS2, ENS, GDPR (porcentaje de controles con evidencias automáticas).
- Porcentaje de activos sin clasificación adecuada frente al marco de criticidad regulatoria (por ejemplo, esenciales e importantes NIS2).[^2][^3][^4]
- Número de no conformidades detectadas a través de CAASM frente a auditorías puntuales (indicador de madurez de supervisión continua).[^3][^2][^12]

***

## 3. Tendencias 2025+ en indicadores CAASM

Basándonos en informes y análisis recientes sobre ASM/CAASM y tendencias de amenazas en la UE, pueden identificarse varias “derivas” claras en las métricas.[^5][^10][^6][^4][^11][^12][^13][^3]

### 3.1. De inventario a riesgo de exposición continua

- La literatura de ASM reciente sitúa la gestión de superficie de ataque como ciclo continuo de descubrimiento, clasificación, priorización, remediación y monitorización, lo que empuja a medir ciclos más que fotos fijas.[^10][^11][^3]
- Los indicadores dejan de centrarse en “\# vulnerabilidades” y pasan a “exposiciones materialmente explotables cerradas por unidad de tiempo”, en paralelo con el enfoque por riesgo de ENISA y el paisaje de amenazas de la UE (DDoS, ransomware, hacktivismo).[^4][^3]
- Los informes de mercado señalan la maduración de CAASM como mercado propio, con previsiones de crecimiento significativo y consolidación en suites de gestión de exposición, lo que refuerza el énfasis en métricas de reducción de riesgo cuantificable y retorno de inversión.[^9][^5][^10][^11][^12]


### 3.2. Extensión de dominio: nube, IoT/OT, APIs, IA

- Los fabricantes resaltan la capacidad de CAASM para abarcar IoT, OT y dispositivos de borde, ampliando el espacio de métricas hacia indicadores sectoriales (por ejemplo, proporción de activos OT con segmentación adecuada, número de interfaces IT/OT expuestas).[^1][^2][^12][^13][^3]
- El énfasis en APIs y superficies cloud hace que los indicadores incluyan “número de endpoints de API expuestos por error”, “recursos cloud sin etiquetado de criticidad” o “identidades cloud con privilegios excesivos”, integrados en el inventario CAASM.[^11][^1][^12][^13][^3]
- Los análisis de ASM empiezan a incorporar ataque a capas de IA y modelos, proponiendo métricas de exposición asociadas a servicios de IA, aunque aún de forma emergente.[^3]


### 3.3. IA para priorización y predicción

- Los informes técnicos subrayan el uso creciente de IA y ML en CAASM para priorizar riesgos, correlacionando valor del activo, vulnerabilidades, exposición real y contexto de amenazas.[^7][^2][^12][^13][^3]
- La utilización de modelos como EPSS y motores de predicción de explotación se refleja en métricas como “porcentaje de vulnerabilidades con alta probabilidad de explotación aún no mitigadas”.[^7][^2][^3]
- Surgen indicadores de eficacia de la priorización, como “porcentaje de incidentes graves originados en exposiciones previamente clasificadas como bajas”, que sirven para recalibrar los modelos.[^12][^13][^3]


### 3.4. Afinidad regulatoria europea (NIS2, ENS, CRA, DORA)

- El enfoque europeo en amenazas (ENISA) y NIS2 pone el acento en sectores esenciales y servicios críticos, lo que impulsa métricas por sector, exposición y criticidad de servicio.[^4]
- España, inmersa en la aplicación de NIS2, ENS y otros marcos como GDPR y DORA, se ve empujada hacia indicadores de superficie de ataque que permitan demostrar supervisión continua en entidades esenciales e importantes.[^15][^6][^4]
- CAASM se posiciona como fuente de evidencia para auditorías y autoridades, fomentando métricas de “grado de cobertura de controles ENS/NIS2 por activo” y “tiempo de detección de desviaciones de configuración exigidas por normativa”.[^2][^12][^3][^4]

***

## 4. Propuesta de cuadro de mando CAASM nacional para España

A partir de la literatura de CAASM, las tendencias ASM y los informes de amenazas a nivel UE y España, puede bosquejarse un cuadro de indicadores a nivel país, con vocación comparativa internacional.[^15][^6][^1][^13][^7][^2][^12][^3][^4]

### 4.1. Ejes principales de medición

1) **Visibilidad y exactitud del inventario nacional**
2) **Exposición de superficie de ataque en sectores esenciales y estratégicos**
3) **Capacidad de remediación y resiliencia**
4) **Convergencia con marcos regulatorios europeos**
5) **Madurez de gobernanza y cooperación público‑privada**

### 4.2. Indicadores sugeridos (vista de alto nivel)

Tabla de categorías y ejemplos de indicadores para un Observatorio Nacional de CAASM:


| Dimensión | Indicador sugerido (nivel país) |
| :-- | :-- |
| Visibilidad | Porcentaje estimado de activos críticos (TI/OT/IoT/nube) con representación en plataformas CAASM u homólogas en entidades esenciales.[^1][^7][^2][^3][^4] |
| Visibilidad | Ratio medio de activos “descubiertos pero no inventariados” en entidades reguladas (shadow IT) por sector.[^1][^7][^2][^3][^4] |
| Exposición | Número y proporción de servicios expuestos a Internet en sectores esenciales sin controles mínimos (MFA, cifrado robusto, endurecimiento básico).[^7][^2][^3][^4][^6] |
| Exposición | Densidad de activos OT e IoT sin segmentación adecuada en infraestructuras críticas.[^1][^2][^12][^3][^4] |
| Riesgo | Porcentaje de exposiciones con alta probabilidad de explotación (EPSS u otros) pendientes de mitigación en entidades esenciales.[^7][^2][^3][^4] |
| Riesgo | Tasa de incidentes significativos asociados a exposiciones previamente identificadas en ASM/CAASM (indicador de brecha entre conocimiento y acción).[^3][^4][^6] |
| Remediación | MTTR medio de exposición crítica en sectores esenciales (días) y desviación estándar entre sectores.[^12][^13][^3][^4][^6] |
| Remediación | Porcentaje de exposiciones críticas cerradas dentro de plazos recomendados por NIS2 / ENS (por ejemplo, ≤7/30 días según criticidad).[^2][^3][^4] |
| Cumplimiento | Cobertura media de controles ENS/NIS2 (seguridad de redes, gestión de activos, gestión de vulnerabilidades) evidenciada automáticamente mediante CAASM.[^2][^3][^4][^15] |
| Cumplimiento | Número de no conformidades recurrentes detectadas en auditorías vs exposiciones ya señaladas por CAASM (indicador de inacción).[^2][^12][^3][^4] |
| Gobernanza | Porcentaje de entidades esenciales que comparten telemetría de superficie de ataque con el CSIRT nacional de forma periódica.[^4][^15][^6] |
| Gobernanza | Existencia y uso de un repositorio nacional de “patrones de exposición” (misconfiguraciones recurrentes, top errores cloud, etc.).[^3][^4][^15][^6] |

La gracia literaria, por si la quieres enunciada, sería pasar de la métrica “número de servidores” a la métrica “número de oportunidades objetivas que tiene un adversario mínimamente capaz de arruinarnos el café del lunes”.

***

## 5. España en contexto internacional: puntos finos

A partir del paisaje europeo de amenazas y del peso regulatorio, la construcción de indicadores CAASM a nivel nacional en España debería dialogar con las siguientes realidades.[^16][^10][^6][^15][^4]

### 5.1. Presión de amenaza y sectores prioritarios

- ENISA destaca que en la UE los DDoS de hacktivismo y el ransomware siguen siendo amenazas dominantes, con especial impacto en administraciones públicas y sectores esenciales recogidos en NIS2.[^4]
- Informes sobre España subrayan el papel de servicios de información, seguridad nacional y otros sectores clave, indicando una concentración de ataques en ámbitos ya señalados por la regulación.[^6]
- Este patrón empuja a que las métricas CAASM nacionales prioricen exposición de superficie de ataque en administración pública, operadores críticos, servicios digitales esenciales y cadena de suministro.[^15][^6][^4]


### 5.2. Regulación y mercado nacional

- El ecosistema español vive un incremento de presión normativa por GDPR, NIS2, DORA, ENS y el futuro Reglamento de Ciberresiliencia, con exigencias crecientes de evidencias continuas, no solo auditorías anuales.[^15][^4]
- El mercado de ciberseguridad en España muestra crecimiento de doble dígito, impulsado por migración a la nube, arquitecturas API‑first y adopción de Zero Trust, lo que amplía la superficie y refuerza la necesidad de CAASM como soporte a estos modelos.[^15]
- A nivel internacional, otros países (p.ej., Canadá) publican evaluaciones de amenazas nacionales que podrían beneficiarse de indicadores CAASM similares, lo que permite diseñar métricas comparables y “exportables”.[^10][^16][^4]


### 5.3. Oportunidad de liderazgo metodológico

- La UE ya dispone de marcos de referencia de amenazas y sectores esenciales, por lo que España podría elaborar un “apéndice CAASM” nacional que defina indicadores mínimos homogéneos por sector y tamaño de entidad.[^6][^4]
- Esta estandarización facilitaría comparaciones internacionales con otros miembros UE y con países con informes nacionales de amenazas, siempre que adopten indicadores similares de exposición, tiempo de remediación y cobertura de controles.[^16][^10][^4]

***

## 6. Batería de preguntas de encuesta (tono inquisitivo‑constructivo)

A continuación, una lista de preguntas y posibles respuestas tipo Likert / opción múltiple para un cuestionario dirigido a CISOs, responsables de riesgo o arquitectos de seguridad en España, con enfoque CAASM nacional y comparativo.

### 6.1. Visibilidad de activos

1. “En su organización, ¿qué grado de confianza tiene en que el inventario de activos refleja la realidad viva de su superficie de ataque (TI, OT, IoT, nube, identidades, APIs)?”
    - Casi total: confiamos en datos consolidados por una plataforma de CAASM.
    - Alta: disponemos de varias fuentes integradas, aunque aún hay islas.
    - Limitada: sabemos que hay “zonas oscuras”, especialmente en nube y OT.
    - Francamente baja: sospechamos que el mapa es más un deseo que una topografía.
2. “¿Con qué frecuencia se detectan activos ‘sorpresa’ (no inventariados) en auditorías, pentests o escaneos externos?”
    - Rara vez (menos de una vez al año).
    - Ocasionalmente (1–2 veces al año).
    - Con frecuencia (trimestralmente).
    - Siempre que alguien mira con un poco de mala intención.

### 6.2. Cobertura de controles y Zero Trust

3. “¿Qué porcentaje aproximado de sus activos críticos cuenta con todos los controles de seguridad definidos (EDR/XDR, cifrado, parches al día, MFA, segmentación adecuada)?”
    - ≥ 90% (lo que falta está en un plan de retirada digna).
    - Entre 70% y 89% (las brechas están identificadas y priorizadas).
    - Entre 40% y 69% (sabemos qué falta, pero falta oxígeno y presupuesto).
    - < 40% (nuestra estrategia es la fe y algún que otro firewall heroico).
4. “Respecto a la adopción de un modelo Zero Trust apoyado en CAASM (inventario de identidades, dispositivos, servicios y datos), su organización se encuentra…”
    - En fase avanzada: políticas dinámicas basadas en contexto y riesgo de activo.
    - En despliegue: pilotos activos en varios dominios (nube, VPN, entornos sensibles).
    - En planificación: hay estrategia y hojas de ruta, aún sin despliegue significativo.
    - En fase de contemplación filosófica: hablamos mucho de Zero Trust en presentaciones.

### 6.3. Exposición y riesgo material

5. “En los últimos 12 meses, ¿se han materializado incidentes significativos vinculados a activos o servicios que CAASM / ASM ya había señalado como ‘en riesgo’?”
    - No, las exposiciones identificadas se han tratado a tiempo.
    - Sí, pero fueron contenidos sin impacto material relevante.
    - Sí, con impacto operativo o reputacional apreciable.
    - Sí, y seguimos revisando el diccionario de la palabra ‘prioridad’.
6. “En términos de priorización del riesgo técnico, ¿qué peso real tiene hoy la probabilidad de explotación (EPSS, inteligencia de amenazas) frente a la mera severidad de vulnerabilidades (CVSS)?”
    - Predomina la probabilidad de explotación y el contexto de negocio.
    - Intentamos ponderar ambos, aunque CVSS sigue dominando las discusiones.
    - La severidad técnica es el criterio de facto (CVSS como evangelio).
    - El criterio dominante es ‘lo que podemos apagar sin protestas de negocio’.

### 6.4. Remediación y ciclo de vida

7. “¿Cuál es su tiempo medio de mitigación de exposiciones críticas (no solo parcheo, sino cierre efectivo de la ventana de ataque)?”
    - Menos de 7 días.
    - Entre 7 y 30 días.
    - Entre 1 y 3 meses.
    - Más de 3 meses, o indeterminado (las exposiciones adquieren ciudadanía permanente).
8. “¿Qué grado de automatización existe en la remediación de exposiciones identificadas por CAASM?”
    - Alto: uso extensivo de flujos automatizados (SOAR / playbooks).
    - Moderado: automatización para casos conocidos, manual para el resto.
    - Bajo: la mayoría de las remediaciones requieren coordinación manual.
    - Nulo: CAASM nos informa y nosotros suspiramos.

### 6.5. Cumplimiento y entorno regulatorio

9. “¿Hasta qué punto utiliza su organización CAASM o herramientas equivalentes para obtener evidencias continuas de cumplimiento (ENS, NIS2, GDPR, DORA)?”
    - Es la fuente principal de evidencias y reporting continuo.
    - Se usa como complemento a auditorías tradicionales y revisiones manuales.
    - Se utiliza de forma parcial, en algunos dominios (p. ej., nube o endpoints).
    - No lo usamos para cumplimiento, solo para apagar incendios técnicos.
10. “De cara a NIS2 y ENS, ¿qué nivel de preparación percibe a la luz de las métricas de superficie de ataque (exposición de servicios, activos críticos inventariados, tiempos de remediación)?”
    - Alto: métricas consolidadas, brechas identificadas y proyectos en marcha.
    - Medio: buena visibilidad, pero brechas relevantes aún sin financiación asegurada.
    - Bajo: sabemos que el delta entre regulación y realidad es considerable.
    - Experimental: aún estamos intentando decidir qué debe medirse exactamente.

***

¿Te interesa que bajemos del Olimpo conceptual al barro sectorial (por ejemplo, indicadores CAASM específicos para sanidad, energía o administración pública en España)?
<span style="display:none">[^17][^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30]</span>

<div align="center">⁂</div>

[^1]: https://www.tenable.com/cybersecurity-guide/learn/what-is-caasm

[^2]: https://es-la.tenable.com/cybersecurity-guide/learn/what-is-caasm

[^3]: https://www.vectra.ai/topics/attack-surface-management

[^4]: https://industrialcyber.co/reports/enisa-2025-threat-landscape-report-highlights-eu-faces-escalating-hacktivist-attacks-and-state-aligned-cyber-threats/

[^5]: https://www.marketreportanalytics.com/reports/cyber-asset-attack-surface-management-52485

[^6]: https://socradar.io/wp-content/uploads/2025/12/Spain-Threat-Landscape-Report-2025.pdf

[^7]: https://www.crowdstrike.com/es-es/cybersecurity-101/exposure-management/cyber-asset-attack-surface-management-caasm/

[^8]: https://omdia.tech.informa.com/blogs/2026/jan/asset-discovery-market-transformation-in-2026-why-easm-and-caasm-matter

[^9]: https://sitsi.pacanalyst.com/analysis-report/prediction-for-2025-cyber-asset-attack-surface-management-caasm-will-make-a-breakthrough-by-2027/

[^10]: https://www.kuppingercole.com/watch/attack-surface-management

[^11]: https://www.centraleyes.com/cyber-asset-attack-surface-management-caasm-tools/

[^12]: https://www.jupiterone.com/blog/the-ultimate-caasm-guide-for-2025

[^13]: https://www.openappsec.io/post/best-cyber-asset-attack-surface-management-tools-for-2025

[^14]: https://www.zscaler.com/es/products-and-solutions/caasm

[^15]: https://deepstrike.io/blog/top-cybersecurity-companies-spain

[^16]: https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026

[^17]: https://www.crowdstrike.com/es-es/platform/exposure-management/caasm/

[^18]: https://www.zscaler.com/zpedia/what-is-cyber-asset-attack-surface-management-caasm

[^19]: https://www.sentinelone.com/es/cybersecurity-101/cybersecurity/attack-surface-management/

[^20]: https://www.ismsforum.es/ficheros/descargas/revistaixforociberseguridad20201600934515.pdf

[^21]: https://www.comunidad.madrid/sites/default/files/doc/sanidad/epid/informe_epidemiologico_semanal.pdf

[^22]: https://www.isc.cl/que-es-la-gestion-de-superficie-de-ataque-de-activos-ciberneticos-caasm/

[^23]: https://digibug.ugr.es/bitstream/handle/10481/105804/TFM_Cristobal.pdf?sequence=1\&isAllowed=y

[^24]: https://aslan.es/centro-de-conocimiento-cybersecurity/

[^25]: https://tecbound.com/es/caasm-gestion-de-la-superficie-de-ataque-de-activos-ciberneticos/

[^26]: https://www.zscaler.com/es/zpedia/what-is-cyber-asset-attack-surface-management-caasm

[^27]: https://repositorio.unican.es/xmlui/bitstream/handle/10902/36854/456313.pdf?sequence=1

[^28]: https://riskxchange.co/blog/best-attack-surface-management-tools-2026-guide

[^29]: https://marketintelo.com/report/cyber-asset-attack-surface-management-market

[^30]: https://www.kriativ-tech.com/?p=66544

