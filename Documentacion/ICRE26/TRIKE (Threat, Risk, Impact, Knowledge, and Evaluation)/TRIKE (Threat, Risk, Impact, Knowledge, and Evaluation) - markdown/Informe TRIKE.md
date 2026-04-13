
# Informe TRIKE.

TRIKE nació como un método de modelado de amenazas tan artesanal como testarudo: un intento de obligar a que “amenaza, riesgo e impacto” cuadren numéricamente, no solo narrativamente. Desde 2025 no se ha reinventado, pero sí se ha “releído” en clave de métricas, automatización y escalado a nivel país, empujado por NIS2, la Ley 43/2022 y el festival continuo de incidentes en España y fuera de ella.[^1][^2][^3][^4][^5]

## 1. Qué mide realmente TRIKE en 2026

TRIKE sigue siendo, en esencia, un marco de requisitos y un modelo de implementación unidos por una capa de análisis de riesgo cuantitativo apoyado en diagramas de flujo de datos (DFD). La novedad no está en el “recetario original”, sino en cómo se están reinterpretando sus cinco letras —Threat, Risk, Impact, Knowledge, Evaluation— como familias de indicadores robustos y alineables con estándares nacionales e internacionales.[^2][^6][^7][^8][^1]

En la práctica, TRIKE usa escalas discretas (clásicamente de cinco puntos) para valorar probabilidad, severidad e “insatisfacción” del stakeholder, lo que permite derivar métricas compuestas para cada amenaza y para cada flujo de datos. En 2025–2026, estas escalas se están mapeando cada vez más a métricas continuas de CVSS, FAIR, seguros cibernéticos y KPIs regulatorios, de forma que los indicadores TRIKE puedan alimentar dashboards nacionales sin perder trazabilidad técnica.[^9][^6][^4][^5][^2]

## 2. Indicadores “T”: Threat a escala nacional

Si uno toma en serio la “T” de TRIKE a nivel país, el juego deja de ser listar “posibles amenazas” y pasa a medir sistemáticamente qué tan expuesto está el territorio a familias de adversarios, vectores y superficies de ataque. Desde 2025, los informes globales (CrowdStrike, Darktrace, IBM X‑Force) convergen en varios ejes que encajan bien como indicadores de Threat, aunque ellos no los llamen TRIKE.[^10][^11][^12]

Para España, estos indicadores de amenaza se pueden articular así, con vocación de comparabilidad internacional:

- Tasa anual de incidentes por 100.000 habitantes y por sector crítico, derivada de datos de CCN‑CERT e INCIBE, comparable con cifras de otros CSIRTs nacionales.[^13][^3][^10]
- Proporción de incidentes ligados a actores avanzados (APT, eCrime organizado) frente a “ruido” oportunista, siguiendo taxonomías de informes globales.[^12][^10]
- Peso relativo de ataques malware‑free, automatizados o asistidos por IA, dado que en 2025 más del 80% de las detecciones eran ya sin malware clásico y los ataques habilitados por IA crecieron cerca del 90% anual.[^11][^10][^12]
- Densidad de vulnerabilidades explotadas en cadena de suministro software y servicios cloud, alineando categorías de NIS2 con familias de amenazas observadas por X‑Force y otros.[^8][^12]

España tiene materia prima estadística: más de 107.000 incidentes en el sector público en 2023 gestionados por CCN‑CERT, y decenas de miles adicionales gestionados por INCIBE para ciudadanos y empresas, lo que da base para series temporales de Threat robustas. Un país que supera los 97.000 incidentes anuales solo en el ámbito cubierto por INCIBE y ve un incremento de dos dígitos año a año tiene ya suficiente “ruido” como para construir indicadores de amenaza de alta resolución territorial, si se decide hacerlo.[^3][^13]

## 3. Indicadores “R”: Risk como puente entre TRIKE, NIS2 y seguros

La “R” de TRIKE es donde la teoría se topa con la contabilidad nacional. TRIKE plantea riesgo como función de probabilidad y consecuencias sobre los stakeholders, pero en 2025–2026 se está empujando a que esa función sea compatible con: CVSS para vulnerabilidades, FAIR para riesgo financiero, y la lógica actuarial que ya emplean las pólizas de ciberseguro.[^14][^6][^4][^1][^2]

A nivel estatal, los indicadores de Risk que emergen al cruzar TRIKE con el contexto europeo (NIS2, Ley 43/2022) y con la realidad económica española podrían tomar esta forma:

- Riesgo agregado por sector crítico, expresado como pérdida económica esperada anual (en euros) por cada mil millones de valor añadido, tomando como insumos tasas de incidente sectoriales, severidad típica y datos de mercado de ciberseguros.[^4][^5]
- Índice de cumplimiento de requisitos NIS2/Ley 43‑2022 ponderado por criticidad y tamaño de la entidad, lo que se traduce en un “riesgo residual normativo” que TRIKE puede incorporar como factor en sus matrices.[^5][^4][^8]
- Prima media de ciberseguro por millón de facturación y ratio siniestralidad/prime, que el mercado español está viendo crecer a medida que aumentan los incidentes, como ilustran informes que relacionan el auge del seguro con el aumento de más de 97.000 incidentes anuales.[^13][^4]
- Distribución del riesgo entre pymes, grandes empresas y sector público, apoyándose en datos que sitúan una parte sustancial de los incidentes en ciudadanos y pymes, pero concentran el impacto sistémico en infraestructuras críticas.[^3][^4][^13]

En comparación con otros países europeos, España se encuentra en la zona “media‑alta” de exposición y crecimiento del mercado de ciberseguridad, con previsiones de superar los 3.000 millones de euros de volumen en 2026 y crecimientos anuales de dos dígitos, impulsados por NIS2 y la digitalización intensiva de pymes. Ese crecimiento, si uno se lo mira con gafas TRIKE, es casi un indicador indirecto de riesgo percibido: cuanto más sube el gasto estructural, más claro es que el riesgo ya está internalizado en presupuestos, aunque no siempre con métricas coherentes.[^4][^5]

### Tabla ilustrativa: Ejemplos de indicadores T y R a nivel país

| Dimensión | España (ejemplo) | Enfoque TRIKE | Comparación internacional |
| :-- | :-- | :-- | :-- |
| Threat: incidentes/100k hab. | Basado en >97.000 incidentes anuales de INCIBE y >100.000 del CCN‑CERT | Normalizar por población y sector, asociar a flujos de datos nacionales | Usar métricas equivalentes de CSIRTs de otros países para comparar intensidad de amenaza |
| Risk: pérdida esperada | Derivable de mercado español previsto en 3.000 M€ y tasas de incidente | Calcular riesgo anualizado por sector y tamaño de organización | Mapear a métricas FAIR y primas de ciberseguro en otros países |

[^6][^14][^5][^13][^3][^4]

## 4. Indicadores “I”: Impact más allá del susto mediático

TRIKE distingue con cierta disciplina el impacto en activos del impacto en stakeholders. Trasladado a escala nacional, esto obliga a dejar de contar solo “incidentes” y empezar a medir, con algo más de mala leche, cuánto duele cada uno a nivel económico, social y estratégico.[^1][^2][^10][^12][^4]

En la práctica, desde 2025 se ve una convergencia hacia varias métricas de Impacto que encajan bien con la filosofía TRIKE:

- Duración media de interrupciones en servicios esenciales por incidente significativo (minutos, horas, días), ligada a indicadores de continuidad de negocio y resiliencia.[^12][^8]
- Coste económico medio y máximo por incidente por sector, que en algunos países se estima combinando estudios industriales con datos de seguros y de incumplimientos regulatorios.[^14][^4]
- Impacto reputacional y social aproximado, medido por indicadores indirectos como usuarios afectados, alcance mediático, sanciones regulatorias, o variaciones en indicadores de confianza digital.[^4][^12]
- Impacto sistémico potencial (riesgo de “cascada” en la cadena de suministro), línea en la que tanto la industria como think tanks globales alertan de vulnerabilidades estructurales en software y proveedores críticos.[^6][^12]

En España, la combinación de incidentes masivos en la administración pública, la expansión acelerada de 5G y el empuje a la adopción de Zero Trust identificados en el mercado nacional hacen especialmente pertinente medir impacto no solo a nivel de entidad, sino de ecosistema. Un fallo prolongado en un proveedor cloud utilizado por varias comunidades autónomas, por ejemplo, no es solo “un incidente más” en la estadística, sino un nodo entero del gráfico TRIKE nacional cambiando de color.[^8][^5][^4]

## 5. Indicadores “K”: Knowledge en manos de un país que aprende (o no)

El “K” de TRIKE es el pariente siempre olvidado en los frameworks: el conocimiento sobre amenazas, vulnerabilidades y controles que una organización (o un Estado) es capaz de generar, compartir y usar. En 2025–2026, los marcos de threat modeling revisados por organismos como ISACA insisten en la necesidad de integrar inteligencia de amenazas, lecciones aprendidas y métricas de madurez en el propio ciclo de modelado.[^2][^1][^6][^8]

A nivel nacional, los indicadores de Knowledge que mejor casan con TRIKE incluyen:

- Cobertura de inteligencia de amenazas: número y diversidad de fuentes de threat intel utilizadas por el CERT nacional, frecuencia de actualización y capacidad de correlación automática.[^10][^12]
- Tasa de cierre de “gaps de conocimiento”: tiempo desde que se detecta una nueva técnica de ataque global hasta que se incorpora a catálogos nacionales de amenazas y guías de mitigación.[^10][^8]
- Madurez profesional y capacidad de formación: volumen del mercado de ciberseguridad, número de profesionales certificados, programas universitarios específicos y brecha de talento señalada por informes de mercado para España.[^5][^4]
- Reutilización de modelos TRIKE y otros: proporción de proyectos (públicos o grandes privados) que reutilizan plantillas de amenaza, catálogos de patrones y librerías de controles en lugar de reinventar el modelo de amenazas en cada sistema.[^6][^8]

España arrastra, como muchos otros países, un déficit de talento en ciberseguridad a pesar de un mercado que se dispara hacia los miles de millones de euros y crece cerca de un 10–14% anual. En términos TRIKE, eso significa que la variable Knowledge es el cuello de botella: no es que falten amenazas que modelar, sino manos expertas y estructuras institucionales capaces de convertir incidentes en conocimiento codificado y métricas reutilizables.[^8][^5][^4]

## 6. Indicadores “E”: Evaluation en tiempos de NIS2 y auditorías perpetuas

La “E” de TRIKE obliga a que todo lo anterior no se quede en un PDF bonito: hay que evaluar sistemáticamente la eficacia de los controles y la calidad del propio modelo de amenazas. Los trabajos recientes sobre threat modeling destacan precisamente esta fase de revisión y mejora continua, alineándola con marcos como el ciclo PDCA y las auditorías que exigen NIS2 y las normativas nacionales.[^1][^2][^6][^8]

En clave país, Evaluation puede traducirse en indicadores como:

- Porcentaje de entidades esenciales y importantes que han realizado modelos de amenaza formales (TRIKE, STRIDE, OCTAVE u otros) en sistemas regulados durante el último ciclo de auditoría.[^4][^8]
- Tasa de mitigación de riesgos de alto nivel: proporción de riesgos “rojos” identificados en los modelos que se reducen a niveles aceptables en un plazo definido.[^14][^8]
- Calidad del modelo: métricas de cobertura de amenazas (p.ej. cuánto se solapa el catálogo de amenazas modeladas con las observadas en informes globales de 2025–2026) y de ausencia de falsos negativos graves.[^11][^12][^10]
- Integración con indicadores globales: grado en que las métricas de amenaza y riesgo nacionales se trazan contra indicadores de informes industriales, lo que permite comparar exposición y desempeño frente a otras jurisdicciones.[^12][^10][^4]

Para España, donde el cumplimiento de NIS2 se ha convertido en motor explícito de gasto en ciberseguridad y en factor cuantificable de mercado, estos indicadores de Evaluation son también indicadores de competitividad regulatoria: un país que modela bien, mide mejor y corrige más rápido, resulta más atractivo para inversiones digitales.[^5][^8][^4]

## 7. España en el espejo internacional

Si elevamos la vista y comparamos, España muestra un perfil peculiar: tasa alta de incidentes reportados, mercado en expansión rápida, fuerte presión regulatoria y una base empresarial dominada por pymes muy dependientes de terceros para servicios digitales. En muchos sentidos, es un “laboratorio” perfecto para aplicar TRIKE a nivel territorial, porque las cadenas de dependencia, los flujos de datos y los stakeholders están ya intensamente entrelazados.[^13][^3][^8][^5][^4]

En el contexto global de 2025–2026, donde los informes de amenazas resaltan el auge de ataques asistidos por IA, el incremento brutal de ataques sin malware y la creciente explotación de la cadena de suministro, España se enfrenta a riesgos cualitativamente similares a los de otras economías avanzadas, pero con diferencias en escala, madurez y estructura productiva. Si TRIKE sirve para algo más que para decorar presentaciones, debería ayudar a España a traducir esa comparabilidad abstracta en indicadores concretos que permitan saber, por ejemplo, si la probabilidad y el impacto de un ataque a su administración electrónica es mayor, menor o simplemente diferente al de sus vecinos europeos.[^2][^11][^1][^10][^12][^8]

Una propuesta razonable de siguiente paso sería seleccionar un sector crítico (p.ej. sanidad o administración electrónica), construir un modelo TRIKE completo a nivel nacional y derivar de él un panel reducido de métricas T‑R‑I‑K‑E que puedan alimentarse con datos de CCN‑CERT, INCIBE, supervisores sectoriales, mercado de ciberseguros y encuestas de madurez. A partir de ahí, la comparación internacional dejaría de ser pura literatura y pasaría a ser una tabla incómoda, pero accionable.[^3][^13][^8][^4]

<span style="display:none">[^15]</span>

<div align="center">⁂</div>

[^1]: https://trike.sourceforge.net

[^2]: https://www.eccouncil.org/cybersecurity-exchange/threat-intelligence/trike-threat-modeling-methodology/

[^3]: https://fitls.com/en/the-rise-of-cyberattacks-in-spain-record-number-of-incidents-and-the-main-threats/

[^4]: https://www.mordorintelligence.com/industry-reports/spain-cybersecurity-market

[^5]: https://www.security.land/spain-cybersecurity-market-3-billion-2026/

[^6]: https://www.sei.cmu.edu/blog/threat-modeling-12-available-methods/

[^7]: https://www.linkedin.com/learning/security-architecture-a-strategic-approach-by-infosec/trike-threat-modeling-methodology

[^8]: https://www.isaca.org/resources/white-papers/2025/threat-modeling-revisited

[^9]: https://www.esecurityplanet.com/networks/selecting-a-threat-risk-model-for-your-organization-part-two/

[^10]: https://www.crowdstrike.com/en-us/global-threat-report/

[^11]: https://www.darktrace.com/blog/what-the-darktrace-annual-threat-report-2026-means-for-security-leaders

[^12]: https://www.ibm.com/think/insights/more-2026-cyberthreat-trends

[^13]: https://www.apolocybersecurity.com/en/blog-posts/espana-supera-los-97-000-incidentes-de-ciberseguridad-en-2024-ha-llegado-la-hora-del-ciberseguro

[^14]: https://breachfin.com/2025/01/31/threat-modeling-frameworks-strengthening-cybersecurity-by-predicting-threats/

[^15]: https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro

