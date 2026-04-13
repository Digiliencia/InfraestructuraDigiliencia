

# Informe sobre CISA KEV y Métricas Nacionales de Ciberseguridad (Enfoque España – Perspectiva Global)

## 1. Resumen ejecutivo

Desde 2024, el catálogo de **Known Exploited Vulnerabilities (KEV)** de CISA se ha consolidado como el “metronomo” mundial de qué vulnerabilidades pasan del mundo de lo **potencial** a lo **realmente explotado**. El ritmo no baja: en 2023 se añadieron 187 vulnerabilidades, en 2024 unas 185–186, y en 2025 el crecimiento vuelve a acelerarse hasta 245 nuevas entradas, superando las 1.4k vulnerabilidades acumuladas en el catálogo.[^1_1][^1_2][^1_3]

En paralelo, estudios de grandes proveedores (Qualys, Rapid7, Mandiant, Bitsight, ENISA, CCN‑CERT, etc.) muestran un patrón consistente:

- Apenas ~**1% de las nuevas CVE** son weaponizadas en el corto plazo, pero su **impacto desproporcionado** explica buena parte de los incidentes graves.[^1_4][^1_5][^1_6][^1_7]
- Las KEV son **mucho más prevalentes** que las vulnerabilidades “normales” y, aun así, se parchean **tarde y mal**: mediana de 174 días frente a 621 días para vulnerabilidades no KEV.[^1_8]
- La explotación se desplaza con decisión hacia **dispositivos perimetrales, VPN, firewalls, file transfer y software de infraestructura (CI/CD, MDM, etc.)**, con una proporción elevada de cero‑days en appliances de red.[^1_9][^1_10][^1_11][^1_12]

En Europa, ENISA incorpora **245 KEV añadidas** durante su último periodo de referencia y destaca que la explotación de vulnerabilidades es el segundo vector de intrusión más eficaz tras el phishing, en un contexto de 42.595 nuevas vulnerabilidades divulgadas (+27% interanual). La nueva **EU Vulnerability Database (EUVD)** se alimenta explícitamente del catálogo KEV de CISA, entre otras fuentes, como pieza de soberanía tecnológica y pilar de NIS2 y la futura Cyber Resilience Act.[^1_7][^1_13]

En España, el **CCN‑CERT** constata que:

- Las vulnerabilidades más explotadas siguen siendo **antiguas** y muy extendidas (Office, WinRAR, etc.).[^1_14]
- Los atacantes muestran una fuerte preferencia por el **compromiso de dispositivos perimetrales vulnerables** y cadenas de phishing + explotación de CVE conocidas.[^1_14]
- España figura entre los países **más atacados por grupos hacktivistas prorrusos**, con DDoS y explotación de sistemas expuestos, lo que amplifica el riesgo asociado a KEV no parcheadas en Administración y operadores críticos.[^1_15][^1_14]

Aunque no hay aún estadísticas públicas detalladas de **“porcentaje de organizaciones españolas con KEV abiertas”**, los datos globales de Bitsight (1,4 M de organizaciones analizadas) ofrecen una línea base razonable para diseñar métricas nacionales:


| Indicador global (Bitsight, 2023) | Valor de referencia |
| :-- | :-- |
| Organizaciones con ≥1 KEV | 35% de organizaciones analizadas[^1_8] |
| Organizaciones con ≥5 KEV | 25% de las que tienen KEV[^1_8] |
| Mediana tiempo de remediación KEV | 174 días (≈6 meses)[^1_8] |
| Mediana KEV críticas | 137 días (≈4,5 meses)[^1_8] |
| Mediana tiempo no‑KEV | 621 días (>1,7 años)[^1_8] |
| Plazos CISA incumplidos | >60% de los casos[^1_8] |

El mensaje subyacente es incómodo pero claro: **el catálogo KEV funciona como priorizador global**, pero los países (España entre ellos) todavía están lejos de cerrar estas brechas con la velocidad que el riesgo exige. Desde una óptica de política pública y de métricas nacionales, KEV ofrece un eje muy fértil para:

- Medir la **exposición real** de un país a vulnerabilidades explotadas.
- Evaluar la **capacidad de respuesta** (tiempos de parcheo, cumplimiento de SLAs).
- Comparar sectores, territorios y países en términos de **resiliencia digital**.

En las secciones siguientes se detalla el panorama KEV desde 2024, la posición europea y española, y se propone un **marco concreto de indicadores y métricas nacionales para España**, con referencias comparativas globales y, al final, un módulo de **preguntas y opciones de respuesta para encuestas**, con el tono ligero, irónico y constructivo que merece cualquier cuestionario que aspire a ser respondido sin bostezos.

***

## 2. Metodología y alcance

**Fuentes utilizadas**

- Documentación oficial de CISA (BOD 22‑01, KEV, Top Routinely Exploited Vulnerabilities).[^1_16][^1_17][^1_18][^1_19]
- Estudios de proveedores de seguridad (Rapid7, Qualys, Mandiant, Bitsight, Edgescan, etc.).[^1_10][^1_5][^1_11][^1_12][^1_20][^1_9][^1_4][^1_8]
- Informes de **ENISA** (Threat Landscape 2024 y briefing 2024‑2025).[^1_21][^1_22][^1_23][^1_7]
- Informes nacionales de **CCN‑CERT** e información operativa de **INCIBE‑CERT**.[^1_24][^1_25][^1_26][^1_15][^1_14]
- Análisis académicos y técnicos sobre KEV, EPSS y priorización de vulnerabilidades (arXiv, TechRxiv, Cyentia).[^1_27][^1_28][^1_29]
- Artículos técnicos y resúmenes de CISA sobre vulnerabilidades más explotadas en 2023–2024.[^1_30][^1_18][^1_19]

**Ventana temporal**

- Tendencias clave desde **2023**, con foco especial en datos **2024–2025**, que es donde KEV se estabiliza primero y vuelve a acelerarse después.[^1_2][^1_3][^1_1][^1_7]

***

## 3. Panorama global de las KEV desde 2024

### 3.1 Crecimiento y estabilización del catálogo KEV

Diversos análisis de terceros sobre el propio catálogo KEV dibujan una trayectoria clara:


| Año | Nuevas KEV añadidas | Total aprox. al final de año | Comentario |
| :-- | :-- | :-- | :-- |
| 2021 (lanzamiento) | ~300 iniciales en pocos meses[^1_1] | ~300+ | Fase de arranque, “backlog histórico”. |
| 2022 | ~500 en primeros 6 meses[^1_1] | ~800 | Expansión agresiva inicial. |
| 2023 | 187 nuevas KEV[^1_1][^1_2][^1_3] | ~1.050 | Crecimiento anual ≈21%. |
| 2024 | 185–186 nuevas KEV; total ≈1.238–1.251[^1_31][^1_1][^1_3] | ~1.250 | Ritmo estable, ligera normalización. |
| 2025 | 245 nuevas KEV; total 1.484[^1_2] | 1.484 | Reaceleración (+20% catálogo en un año). |

Aunque distintas fuentes dan cifras totales ligeramente diferentes (1.238 vs 1.251 vulnerabilidades), coinciden en el orden de magnitud y en la forma de la curva: **fuerte crecimiento inicial, meseta en 2023–2024 y nuevo salto en 2025**.[^1_31][^1_3][^1_1][^1_2]

### 3.2 KEV frente al océano de CVEs

Varios informes permiten situar KEV en el contexto del “mar de CVEs”:

- Qualys estima que, entre enero y mediados de julio de 2024, se publicaron **22.254 CVEs**, un 30% más que el mismo periodo del año anterior.[^1_5][^1_6][^1_4]
- De esas nuevas CVE, **204 fueron weaponizadas** en ese periodo: un **0,91%** de las nuevas vulnerabilidades.[^1_6][^1_4][^1_5]
- ENISA reporta **42.595 vulnerabilidades divulgadas** en su último periodo (jul 2024–jun 2025, +27% anual), de las que **245** se convirtieron en KEV durante ese tiempo.[^1_7]

Esto sugiere, con todas las cautelas, que:

- Solo una **fracción muy pequeña (~1%) de las nuevas CVE** acaba siendo explotada de forma suficientemente relevante como para entrar en KEV.
- Aun así, esa fracción explica una **porción desproporcionada de incidentes graves, ransomware y campañas estatales**.[^1_18][^1_19][^1_9][^1_10][^1_30]


### 3.3 Naturaleza de las vulnerabilidades KEV (2023–2025)

Las tendencias técnicas desde 2023 son claras:

1. **Dispositivos perimetrales y appliances de red**
    - Rapid7 constata que el **24% de las vulnerabilidades explotadas** en su conjunto de datos son “network pivot vulnerabilities” (puertas de pivotaje en el perímetro), mientras que en KEV **≈19%** de las entradas afectan a dispositivos de borde o pasarelas de seguridad.[^1_11][^1_9]
    - Mandiant muestra que en 2024 la **mayor parte de los incidentes con exploit como vector inicial** se debieron a vulnerabilidades en dispositivos perimetrales:
        - Palo Alto PAN‑OS (CVE‑2024‑3400).
        - Ivanti Connect Secure / Policy Secure (CVE‑2023‑46805, CVE‑2024‑21887, CVE‑2024‑21893).
        - Fortinet FortiClient EMS (CVE‑2023‑48788).[^1_10]
2. **File transfer, colaboración y CI/CD**
    - MOVEit Transfer (CVE‑2023‑34362), Barracuda ESG (CVE‑2023‑2868), TeamCity (CVE‑2023‑42793), GitLab (CVE‑2023‑7028), Atlassian Confluence (CVE‑2023‑22515/22518/22527) aparecen de forma reiterada en KEV y en los listados de vulnerabilidades más explotadas por ransomware y APT.[^1_27][^1_18][^1_14]
3. **Vulnerabilidades antiguas y log4j eterno**
    - La CISA y resúmenes derivados señalan que las **vulnerabilidades más explotadas en 2023–2024 incluyen varias CVE de 2021 o anteriores**, siendo log4j (CVE‑2021‑44228) el caso paradigmático, vinculado a más de **31 grupos de amenazas**.[^1_19][^1_30][^1_18]
    - CCN‑CERT observa que entre las vulnerabilidades más explotadas en muestras de malware destacan **CVE‑2017‑11882, CVE‑2018‑0802 y CVE‑2017‑0199** en Microsoft Office, es decir, software muy antiguo y ubicuo.[^1_14]
4. **CWE dominantes**
    - ENISA y Kaspersky resaltan el peso de CWE como inyección SQL (CWE‑89), inyección de comandos OS (CWE‑78), path traversal (CWE‑22) y upload de ficheros peligrosos (CWE‑434) entre las vulnerabilidades explotadas en 2024.[^1_32][^1_7]
    - Análisis de KEV para 2024 muestran CWE‑79 (XSS), CWE‑20 (input validation), CWE‑416 (use‑after‑free) y CWE‑287 (improper authentication) como debilidades repetidamente asociadas a KEV.[^1_3][^1_31][^1_1]

***

## 4. KEV, explotación real y otros sistemas de priorización (CVSS, EPSS, NIST LEV)

### 4.1 CVSS vs KEV: severidad vs realidad

- CVSS mide **impacto potencial**, no uso real. Grandes porciones del espacio de CVEs con puntuaciones 9.x jamás se explotan de forma masiva.
- KEV, en cambio, captura únicamente vulnerabilidades con **explotación confirmada** y añade **fecha de inclusión, acción requerida y fecha límite de remediación** según BOD 22‑01.[^1_33][^1_17][^1_34][^1_16]

En la práctica:

- KEV actúa como “capa superior” de priorización: **si está en KEV, se trata como crítico aunque CVSS no sea 10/10**.
- Proveedores como Qualys, Rapid7, Dynatrace, FOSSA, etc., recomiendan explícitamente priorizar KEV sobre otros criterios.[^1_35][^1_36][^1_37][^1_34][^1_38][^1_9][^1_4][^1_5]


### 4.2 EPSS y KEV: qué predice y qué no

Un estudio independiente en arXiv analiza la **capacidad de EPSS v3 para anticipar explotación** en CVE de alta severidad (CVSS ≥9.0) que posteriormente entraron en KEV.[^1_27]

Resultados clave:

- Muestra: 90 CVE con CVSS ≥9.0 añadidas a KEV entre 15/03/2023 y 01/07/2024.[^1_27]
- Para CVE de **2022 o anteriores**, EPSS se comporta razonablemente bien: casi todas tenían puntuaciones altas **antes** de su inclusión en KEV.[^1_27]
- Para CVE **2023+**:
    - **42 de 57** CVE (≈74%) tenían **scores bajos (dígito simple)** antes de entrar en KEV.[^1_27]
    - Si se amplía a todas las 250 CVE añadidas a KEV en el periodo (sin filtrar por CVSS), **más de dos tercios** tenían EPSS <36% (umbral recomendado) justo antes de su inclusión.[^1_28][^1_27]

Conclusión del autor: EPSS actúa más como **indicador rezagado** que como predictor en muchos casos, sobre todo para vulnerabilidades recientes. Una estrategia nacional o corporativa que **se limite a EPSS** dejaría abiertas muchas KEV críticas durante el periodo en que ya están siendo explotadas.[^1_29][^1_28][^1_27]

En cambio, combinar:

- **CVSS** (impacto potencial),
- **KEV** (explotación confirmada),
- **EPSS/NIST LEV** (probabilidad relativa de explotación),

ofrece un marco de **priorización multinivel** mucho más sólido.[^1_39][^1_20][^1_28][^1_27]

### 4.3 Efecto real de KEV sobre el parcheo

Bitsight ofrece la primera visión amplia (1,4 M de organizaciones) del impacto de KEV en comportamientos de parcheo:[^1_40][^1_41][^1_8]

- **Remediación KEV 3,5 veces más rápida**:
    - Mediana KEV: **174 días**.
    - Mediana no‑KEV: **621 días**.
- Aun así, **>60% de las KEV** se remedia **después** del plazo recomendado por CISA.[^1_8]
- Organismos federales estadounidenses, obligados por BOD 22‑01, son **56% más propensos** a cumplir los plazos que el resto.[^1_8]
- KEV usadas en **ransomware** (≈20% del catálogo) son **64% más prevalentes** que el resto, pero se remiendan 2,5 veces más rápido (el miedo es un excelente motor de SLAs).[^1_8]

Como línea base comparativa, estos datos permiten a España plantearse objetivos del tipo: “reducir media nacional de remediación KEV críticas por debajo de 120 días” o “llevar el % de KEV fuera de plazo nacional por debajo del 40%”.

***

## 5. Dimensión europea y española

### 5.1 Europa: ENISA, EUVD y NIS2

El contexto europeo converge explícitamente hacia KEV:

- **ENISA Threat Landscape 2024** y el briefing 2024–2025 destacan:
    - **Phishing** sigue siendo el vector inicial dominante (≈60% de incidentes).
    - La **explotación de vulnerabilidades** representa ≈21% de incidentes y ≈70% de los casos en que se usa conduce directamente a intrusión, y en ≈68% se observa despliegue de malware.[^1_7]
    - 42.595 vulnerabilidades divulgadas (+27%) y **245 KEV añadidas** durante el periodo de análisis.[^1_7]
- La **EU Vulnerability Database (EUVD)**, presentada por ENISA en 2025, se alimenta de:
    - CSIRTs nacionales,
    - proveedores,
    - bases existentes como MITRE CVE,
    - y explícitamente del **catálogo KEV de CISA**.[^1_13]

Su objetivo es convertirse en **fuente centralizada de vulnerabilidades para la UE**, alineada con NIS2 y la futura Cyber Resilience Act.[^1_13]

En términos de métricas nacionales, esto significa que:

- España podrá, en el medio plazo, **correlacionar datos propios de exposición y remediación con EUVD**, incluyendo el “flag KEV” como atributo de cada vulnerabilidad.
- Las obligaciones de NIS2 en materia de **gestión de vulnerabilidades y notificación** tenderán a alinear los tiempos de parcheo y el seguimiento de KEV en los Estados miembros.


### 5.2 España: CCN‑CERT, INCIBE‑CERT y patrón de explotación

**CCN‑CERT – Ciberamenazas y Tendencias 2024 (datos 2023)**

En la sección de vulnerabilidades, CCN‑CERT sintetiza tendencias muy coherentes con las observadas por CISA y ENISA:[^1_14]

- “La explotación de vulnerabilidades recientes ha sido empleada como método de acceso inicial por todo tipo de ciberamenazas, observando una **predilección por el compromiso de dispositivos perimetrales vulnerables**.”[^1_14]
- Sin embargo, “las vulnerabilidades más explotadas siguen siendo **vulnerabilidades antiguas de productos ampliamente utilizados**”, destacando las CVE de Office mencionadas antes (2017–2018) con cientos o miles de observaciones.[^1_14]
- Google es el proveedor que más vulnerabilidades publicó en 2023; las de Microsoft crecieron un **42% respecto a 2022**.[^1_14]
- En el plano geopolítico, **España se sitúa entre los países más atacados por grupos hacktivistas prorrusos**, principalmente mediante DDoS y campañas oportunistas asociadas al apoyo a Ucrania.[^1_15][^1_14]

Aunque el informe no referencia explícitamente el catálogo KEV, muchas de las vulnerabilidades destacadas coinciden con KEV y/o con las listas de “Top Routinely Exploited Vulnerabilities” de CISA: Citrix, Fortinet, Atlassian, MOVEit, JetBrains, etc.[^1_18][^1_19][^1_14]

**INCIBE‑CERT**

- La sección de **alertas de vulnerabilidades** incluye crecientemente referencias explícitas a KEV cuando CISA añade una CVE relevante (por ejemplo, CVE‑2025‑3928 en Commvault Web Server, añadida al catálogo KEV el 28/04/2025).[^1_26]
- INCIBE también ha difundido comunicados sobre la lista de vulnerabilidades más explotadas en 2022 reseñando avisos conjuntos de CISA y otros organismos (AA23‑215A), en los que se insta a priorizar el parcheo de vulnerabilidades “rutinariamente explotadas”.[^1_24][^1_19]

En resumen, **España ya está operativamente alineada con KEV** a través de:

- Alertas CCN‑CERT/INCIBE‑CERT que siguen los advisories de CISA.
- La adopción en curso de NIS2 y el despliegue de EUVD, que integra KEV como fuente upstream.[^1_15][^1_13][^1_14]

Lo que falta, y aquí está la oportunidad, es **traducir esa alineación operativa en métricas agregadas de país**.

***

## 6. Propuesta de marco de indicadores KEV a nivel nacional (España)

A efectos de política pública, supervisión sectorial y benchmarking internacional, puede articularse un sistema de indicadores KEV en tres niveles:

1. **Exposición**: ¿cuántas y qué tipo de KEV afectan a activos en España?
2. **Capacidad de respuesta**: ¿con qué rapidez y consistencia se remedia?
3. **Resultados e impacto**: ¿hasta qué punto KEV se traduce en incidentes reales?

### 6.1 Indicadores de exposición

**E1. Porcentaje de organizaciones españolas con ≥1 KEV expuesta**

- Definición:
\- Nº de organizaciones en España con al menos una vulnerabilidad incluida en KEV **detectada en activos expuestos a Internet** / Nº total de organizaciones analizadas.
- Línea base global: 35% (muestra Bitsight, 1.4 M entidades).[^1_8]
- Posible desagregación: por comunidad autónoma, por tamaño (PYME, gran empresa), por sector (ENS, operadores esenciales NIS2, etc.).
- Fuentes:
    - Telemetría de proveedores de rating/scan (Bitsight, SecurityScorecard, Shodan‑like).
    - Datos agregados anonimizados de SOC gubernamentales y operadores críticos.

**E2. Densidad media de KEV por organización expuesta**

- Definición:
\- Nº total de KEV detectadas en organizaciones españolas / Nº de organizaciones con al menos una KEV.
- Bitsight reporta que, entre quienes tienen KEV, el 66% tiene >1, el 25% ≥5, y el 10% ≥10.[^1_8]
- Permite fijar metas del tipo: “Reducir el porcentaje de organizaciones con ≥5 KEV abiertas por debajo del 15%”.

**E3. Distribución tipo de KEV por tecnología en España**

- Categorías sugeridas:
    - Dispositivos perimetrales (VPN, firewalls, WAF, load balancers).
    - File transfer / almacenamiento.
    - Plataformas de colaboración (Exchange, Confluence, etc.).
    - Infraestructura CI/CD y DevOps (TeamCity, GitLab…).[^1_9][^1_11][^1_10][^1_27][^1_14]
- Objetivo: identificar **“puntos calientes nacionales”** (por ejemplo, sobreexposición a un fabricante perimetral concreto en determinados sectores).


### 6.2 Indicadores de capacidad de respuesta

**R1. Tiempo medio/mediano de remediación de KEV en España**

- Definición:
\- Mediana de días desde la **fecha de inclusión en KEV** hasta la **fecha de cierre efectivo** (parche o mitigación) para cada vulnerabilidad observada en organizaciones españolas.
- Línea base global:
    - Mediana KEV global: 174 días.
    - Mediana KEV críticas: 137 días.[^1_8]
- Posible objetivo español:
    - “Reducir mediana KEV críticas a <120 días y KEV de cualquier severidad a <150 días en 3 años.”

**R2. Porcentaje de KEV remediadas dentro del plazo recomendado por CISA**

- CISA fija plazos por defecto:
    - CVE con ID anterior a 2021: ≤6 meses.
    - Resto: ≤2 semanas (aunque posteriormente ha habido ajustes).[^1_17][^1_42][^1_8]
- Bitsight: >60% de KEV se remedia **fuera de plazo** a nivel global, pero las agencias federales cumplen plazos en un % significativamente superior.[^1_8]
- Indicador español:
    - Nº de KEV observadas en organizaciones españolas remediadas antes de la fecha límite KEV / Total de KEV observadas.
    - Desglosable por sector crítico, administración pública, etc.

**R3. Porcentaje de activos perimetrales críticos con KEV abiertas**

- Dado que la mayoría de campañas recientes explotan dispositivos de borde, conviene disponer de un indicador específico:[^1_11][^1_9][^1_10][^1_14]
    - Nº de dispositivos perimetrales expuestos con alguna KEV abierta / Nº total de dispositivos perimetrales expuestos inventariados.
    - Posible objetivo: “Ningún organismo sujeto al ENS con dispositivos perimetrales en producción con KEV abiertas más allá del plazo KEV”.


### 6.3 Indicadores de impacto

**I1. Porcentaje de incidentes significativos vinculados a KEV**

- Definición:
\- Nº de incidentes de gravedad alta o muy alta (según taxonomía nacional) en los que el vector inicial o de escalada explotó una CVE incluida en KEV / Nº total de incidentes de esa gravedad en el periodo.
- Fuentes:
    - CCN‑CERT, INCIBE‑CERT, CSIRTs sectoriales.
- Alineación con CISA/ENISA:
    - CISA y los advisories “Top Routinely Exploited Vulnerabilities” ya etiquetan incidentes por CVE y CWE.[^1_19][^1_18]
    - ENISA también clasifica incidentes por vector (phishing, exploit, etc.).[^1_7]

**I2. Incidentes KEV por millón de habitantes / por 1.000 organizaciones**

- Permite comparaciones internacionales (a partir de datos compartidos o informes de ENISA) y entre regiones españolas.
- Útil para priorizar inversión pública en concienciación, apoyo a PYMEs, etc.

**I3. Incidentes KEV en infraestructuras críticas**

- Subconjunto de I1/I2 focalizado en sectores contemplados por NIS2, Ley PIC, etc.:
    - Energía, transporte, sanidad, agua, financiero, digital, etc.
- La combinación “KEV + sector crítico” debería desencadenar **umbral de atención regulatoria** y requisitos de reporte reforzados.

***

## 7. Recomendaciones estratégicas para España (nivel país)

1. **Integrar explícitamente KEV en el Esquema Nacional de Seguridad (ENS) y la transposición de NIS2**
    - Incluir referencias a KEV en las medidas de **gestión de vulnerabilidades**, con obligación explícita de:
        - Monitorizar el catálogo KEV.
        - Definir SLAs diferenciados para KEV vs otras vulnerabilidades.
        - Reportar métricas agregadas de remediación KEV a CCN‑CERT/autoridades competentes.
2. **Construir un “panel KEV nacional”**
    - Integrar fuentes:
        - Telemetría de proveedores comerciales (Bitsight, SecurityScorecard, etc.).
        - Información agregada de CCN‑CERT/INCIBE‑CERT.
        - Datos de EUVD y del programa CVE de ENISA.[^1_13][^1_15][^1_7][^1_14][^1_8]
    - Objetivo: tener **indicadores E/R/I** (exposición, respuesta, impacto) por sector y territorio.
3. **Aprovechar KEV como “mínimo común denominador” regulatorio**
    - Para operadores de servicios esenciales y entidades importantes NIS2, establecer como obligación de resultado (no solo de medios) que:
        - No existan KEV críticas abiertas más allá de X días.
        - Se mantenga un % máximo de KEV abiertas por activo perimetral.
4. **Convergencia con marcos internacionales**
    - Alinear las métricas KEV nacionales con:
        - NIST CSF 2.0 (funciones Identify, Protect, Detect, Respond, Recover).[^1_39]
        - Prácticas de priorización combinando CVSS, KEV, EPSS/NIST LEV, ya adoptadas por grandes proveedores.[^1_20][^1_4][^1_28][^1_9][^1_39][^1_27]
5. **Promover transparencia sectorial**
    - Publicar de forma anonimizada, por sectores, indicadores anuales de:
        - Media de KEV por organización.
        - Mediana de tiempo de remediación de KEV críticas.
        - Porcentaje de incidentes significativos vinculados a KEV.

Así, España podría situarse como **referente europeo en “KEV‑driven cyber metrics”**, algo muy alineado con el papel creciente de ENISA como CNA (CVE Numbering Authority) y con la EUVD.[^1_23][^1_13][^1_7]

***

## 8. Módulo de encuesta: preguntas y opciones de respuesta (tono ameno, irónico y útil)

A continuación se proponen bloques de preguntas tipo para encuestas dirigidas a organizaciones españolas (CISOs, responsables de TI, etc.), orientadas a captar **madurez en el uso de KEV**. Cada una incluye un conjunto de **respuestas tipo**, formuladas en un tono profesional pero con un punto irónico que ayuda a que la gente responda con menos dolor de corazón.

### 8.1 Gobernanza y política de vulnerabilidades

**P1. En su organización, ¿cómo se integra el catálogo KEV de CISA en la política de gestión de vulnerabilidades?**

Opciones sugeridas:

- a) “KEV está explícitamente mencionado en nuestra política y define SLAs diferenciados de parcheo.”
- b) “Usamos KEV como una de varias fuentes (junto con CVSS, EPSS, etc.), pero sin SLAs formales específicos.”
- c) “Lo revisamos cuando hay una gran noticia o un advisory grave, pero no de forma sistemática.”
- d) “Conocemos KEV de oídas; por ahora vivimos felices en el universo CVSS y ‘ya si eso’.”

**P2. ¿Quién es el responsable último de que las KEV críticas se remedien en plazo?**

Opciones:

- a) “Responsable de ciberseguridad con mandato explícito y apoyo de dirección.”
- b) “Compartido entre TI, ciberseguridad y los dueños de negocio (modelo colegiado).”
- c) “En teoría TI; en la práctica, cada proyecto se apaña como puede.”
- d) “Nadie en concreto: confiamos en la energía cósmica del parche mensual.”


### 8.2 Procesos y métricas internas

**P3. ¿Con qué frecuencia se revisan las nuevas entradas de KEV frente a su inventario de activos?**

- a) “Diariamente (integrado en herramientas y/o procesos SOC).”
- b) “Semanalmente.”
- c) “Mensualmente, salvo emergencias mediáticas.”
- d) “Solo cuando nos llega un boletín alarmante… o nos llama el proveedor.”

**P4. ¿Qué indicadores relacionados con KEV monitoriza regularmente su organización? (selección múltiple posible)**

Opciones de respuesta (tipo lista de chequeo):

- “Número de KEV abiertas por activo / por entorno (producción, preproducción…).”
- “Tiempo medio de remediación de KEV críticas y altas.”
- “Porcentaje de KEV remediadas dentro del plazo CISA o interno equivalente.”
- “Porcentaje de incidentes significativos en los que intervino alguna KEV.”
- “Ninguno todavía; medimos sobre todo el número de parches instalados y la longitud de la hoja Excel.”


### 8.3 Tecnología y herramientas

**P5. ¿Cómo consumen técnicamente la información de KEV?**

- a) “Integración automática (API/feeds) en soluciones de gestión de vulnerabilidades o GRC.”
- b) “A través de herramientas comerciales que ya incorporan la etiqueta KEV (scanners, ASM, etc.).”
- c) “Descarga manual/periódica del catálogo KEV para cruces puntuales.”
- d) “Principalmente vía artículos de prensa, blogs técnicos o boletines de terceros.”

**P6. De las vulnerabilidades detectadas en sus activos, ¿cómo prioriza actualmente?**

- a) “Primero KEV, luego EPSS/LEV, luego CVSS y contexto de negocio.”
- b) “Primero CVSS (críticas), y dentro de ellas damos prioridad a KEV cuando las hay.”
- c) “Priorizamos por impacto en negocio percibido y la ventana de mantenimiento disponible; KEV es un factor más.”
- d) “Lo prioriza el calendario: lo que cae en el parche mensual entra; lo demás espera tiempos mejores.”


### 8.4 Cultura y percepción de riesgo

**P7. ¿Cómo describiría la actitud de su organización hacia las KEV?**

- a) “Son tratadas como emergencias gestionadas: pocas, muy serias y con foco de dirección.”
- b) “Se consideran importantes, pero compiten en igualdad con otras tareas técnicas.”
- c) “Generan cierta fatiga: ‘otra lista más’ que añadir a las mil ya existentes.”
- d) “KEV es esa cosa de la que habla el proveedor antes de enseñarnos el PowerPoint de ventas.”

**P8. En términos de comunicación interna, cuando se notifica una KEV crítica, ¿qué ocurre?**

- a) “Se activa un procedimiento claro: evaluación de impacto, ventana de parcheo, seguimiento hasta cierre.”
- b) “Se abre un ticket prioritario y se intenta encajar en el próximo ciclo de cambios.”
- c) “Se reenvía un correo masivo con asunto en mayúsculas y se confía en la buena voluntad del destinatario.”
- d) “Se guarda en la carpeta de ‘asuntos serios’ para la próxima reunión en la que haya tiempo (spoiler: nunca).”

***

## 9. Cierre

El catálogo KEV de CISA ha pasado, en pocos años, de ser una iniciativa “doméstica” para agencias federales estadounidenses a un **estándar de facto mundial de priorización de vulnerabilidades explotadas**. ENISA lo integra en la base de datos europea EUVD; grandes proveedores de seguridad lo incorporan como señal de riesgo de primera clase; los estudios empíricos muestran que **las KEV se corrigen más rápido que el resto**, aunque todavía demasiado despacio para el gusto de cualquier ransomware mínimamente ambicioso.[^1_38][^1_1][^1_2][^1_3][^1_7][^1_8]

Para España, el camino lógico –y estratégico– pasa por:

- **Adoptar KEV como eje vertebrador de métricas nacionales de ciberseguridad**, especialmente en sectores críticos y Administración.
- **Medirse sistemáticamente** frente a líneas base globales (porcentaje de organizaciones con KEV, tiempos de remediación, peso de KEV en incidentes graves).
- Aprovechar la sinergia con **NIS2, ENS y EUVD** para construir un panel de indicadores que permita a reguladores, CSIRTs y organizaciones hablar el mismo idioma cuando discuten de riesgo: no de CVEs en abstracto, sino de **las vulnerabilidades que ya se están usando contra nosotros**.[^1_15][^1_13][^1_7][^1_14][^1_8]

Y, por supuesto, hacerlo sin perder el sentido del humor: porque si algo enseñan los datos de KEV es que **parchear tarde es una tradición muy humana**, pero también que, cuando se dan señales claras y medibles, los comportamientos cambian. El reto ahora es que esas señales y métricas se definan **a nivel país**, y ahí es donde España puede jugar muy bien sus cartas.
<span style="display:none">[^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_80][^1_81][^1_82][^1_83][^1_84]</span>

<div align="center">⁂</div>

[^1_1]: https://cyble.com/blog/cisa-known-exploited-vulnerabilities-catalog-update/

[^1_2]: https://thecyberexpress.com/cisa-known-exploited-vulnerabilities-kev-2025/

[^1_3]: https://socradar.io/cisa-kev-2024-review-trends-from-the-past-year/

[^1_4]: https://www.enterprisetimes.co.uk/2024/08/06/qualys-sees-a-surge-in-cves/

[^1_5]: https://www.la-cyber.com/Current-Threat-Data.php?id=3128

[^1_6]: https://kbi.media/press-release/2024-qualys-midyear-threat-landscape-review/

[^1_7]: https://breached.company/enisa-threat-landscape-briefing-2024-2025-analysis/

[^1_8]: https://www.bitsight.com/press-releases/bitsight-reveals-more-60-percent-known-exploited-vulnerabilities-remain-unmitigated

[^1_9]: https://www.scribd.com/document/740086417/2024-Attack-Intelligence-Report

[^1_10]: https://cyberscoop.com/mandiant-m-trends-2025/

[^1_11]: https://www.rapid7.com/globalassets/_pdfs/research/rapid7_2024_attack_intelligence_report.pdf

[^1_12]: https://corelight.com/blog/insights-from-mandiant-m-trends-2024

[^1_13]: https://www.redseguridad.com/actualidad/ciberseguridad/enisa-lanza-una-base-de-datos-europea-de-vulnerabilidades-para-reforzar-la-ciberseguridad-en-la-ue_20250519.html

[^1_14]: https://www.ccn-cert.cni.es/es/informes/informes-ccn-cert-publicos/7274-ccn-cert-ia-04-24-ciberamenazas-y-tendencias-edicion-2024/file.html

[^1_15]: https://ciberseguridadegalicia.gal/es/actualidad/noticias/el-ccn-cert-publica-la-edicion-de-2024-del-informe-de-ciberamenazas-y

[^1_16]: https://www.infocean.com/cisa-issues-bod-22-01-reducing-the-significant-risk-of-known-exploited-vulnerabilities/

[^1_17]: https://csrc.nist.gov/csrc/media/Presentations/2022/dhs-binding-operational-directive-bod-22-01/7-Bokan Day2 1130am DHS Binding Operational Directive 22-01.pdf

[^1_18]: https://media.defense.gov/2024/Nov/12/2003581596/-1/-1/0/CSA-2023-TOP-ROUTINELY-EXPLOITED-VULNERABILITIES.PDF

[^1_19]: https://media.defense.gov/2023/Aug/03/2003273618/-1/-1/0/JOINT-CSA-2022-TOP-ROUTINELY-EXPLOITED-VULNERABILITIES.PDF

[^1_20]: https://www.edgescan.com/wp-content/uploads/2024/03/2023-Vulnerability-Statistics-Report.pdf

[^1_21]: https://traficom.fi/sites/default/files/media/file/ENISA’s threat landscape 2024, ENISA.pdf

[^1_22]: https://www.traficom.fi/sites/default/files/media/file/ENISA’s threat landscape 2024, ENISA.pdf

[^1_23]: https://securitydelta.nl/media/com_hsd/report/690/document/ENISA-Threat-Landscape-2024.pdf

[^1_24]: https://www.incibe.es/incibe-cert/publicaciones/bitacora-de-seguridad/publicado-el-listado-de-vulnerabilidades-mas-explotadas-en-2022

[^1_25]: https://www.incibe.es/incibe-cert/alerta-temprana/vulnerabilidades

[^1_26]: https://www.incibe.es/incibe-cert/alerta-temprana/vulnerabilidades/cve-2025-3928

[^1_27]: https://arxiv.org/html/2411.02618v1

[^1_28]: https://www.cyentia.com/wp-content/uploads/2024/07/EPSS-Exploration-Of-Exploits.pdf

[^1_29]: https://www.techrxiv.org/users/1014795/articles/1378267-prediction-meets-patch-queues-empirical-limits-of-epss-only-prioritization-using-cisa-kev-additions-in-2025

[^1_30]: https://www.opensecurity.es/las-principales-vulnerabilidades-explotadas-en-2024-segun-cisa-un-aumento-del-20-en-ataques/

[^1_31]: https://thecyberexpress.com/cisas-2024-kev-catalog-update/

[^1_32]: https://securelist.lat/vulnerability-exploit-report-q2-2024/98958/

[^1_33]: https://kqlquery.com/posts/prioritize-vulnerabilities-cisa/

[^1_34]: https://fossa.com/blog/using-cisa-kev-catalog/

[^1_35]: https://www.rapid7.com/blog/post/2024/02/12/etr-critical-fortinet-fortios-cve-2024-21762-exploited/

[^1_36]: https://blog.qualys.com/vulnerabilities-threat-research/2024/08/06/2024-midyear-threat-landscape-review

[^1_37]: https://www.dynatrace.com/news/blog/prioritize-vulnerabilities-based-on-the-cisa-known-exploited-vulnerabilities-catalog/

[^1_38]: https://www.revenera.com/blog/software-composition-analysis/cisas-kev-catalog-focusing-on-what-matters/

[^1_39]: https://www.aptori.com/blog/comparing-nist-lev-epss-and-kev-for-vulnerability-prioritization

[^1_40]: https://authlab.com/community/organization-patching-cisa-kev-vulnerabilities-3-5-times-faster-than-other-vulnerabilities/

[^1_41]: https://netlas.io/blog/when_patches_fail/

[^1_42]: https://integrisit.com/new-cisa-directive-what-you-need-to-know-about-bod-22-01/

[^1_43]: https://www.dotforce.it/wp-content/uploads/2024/08/rapid7_2024_attack_intelligence_report_key_takeaways.pdf

[^1_44]: https://deepstrike.io/blog/zero-day-exploit-statistics-2025

[^1_45]: https://auxiom.com/blog/vlog/mandiant-mtrends-2024-report/

[^1_46]: https://www.linkedin.com/posts/saeedabbasi_2024-midyear-threat-landscape-review-qualys-activity-7231339525044662272-c-b2

[^1_47]: https://app.opencve.io/cve/?vendor=rapid7

[^1_48]: https://www.reddit.com/r/cybersecurity/comments/1ntbe4l/mandiant_says_most_exploited_vulnerabilities_in/

[^1_49]: https://www.reddit.com/r/cybersecurity/comments/t5wwnr/cisa_adds_95_known_exploited_vulnerabilities_to/

[^1_50]: https://support.holmsecurity.com/knowledge/what-is-cisas-known-exploited-vulnerabilities-catalog

[^1_51]: https://www.linkedin.com/posts/cybrmonk_a-look-at-cisa-known-exploited-vulnerabilities-activity-7279444012950863873-Jeti

[^1_52]: https://phoenix.security/vulnerability-management-the-impact-of-the-new-cisa-directive-22-01/

[^1_53]: https://anchore.com/blog/how-to-check-for-cisa-catalog-of-exploited-vulnerabilities/

[^1_54]: https://www.balbix.com/blog/analyzing-cisa-known-exploited-vulnerabilities-with-business-context/

[^1_55]: https://www.cibersecurity.io/cisa-catalog-of-known-exploited-vulnerabilities/

[^1_56]: https://xygeni.io/es/blog/known-exploited-vulnerabilities-what-to-fix-first/

[^1_57]: https://www.incibe.es/node/257842

[^1_58]: https://www.incibe.es/incibe-cert/alerta-temprana/vulnerabilidades/avisos-cna

[^1_59]: https://www.lksnext.com/es/noticias_boletin/el-ccn-cert-publica-su-informe-de-ciberamenazas-y-tendencias-de-2024/

[^1_60]: https://industrialcyber.co/reports/enisa-threat-landscape-2024-identifies-availability-ransomware-data-attacks-as-key-cybersecurity-threats/

[^1_61]: https://www.secopsolution.com/blog/cisa-kev-and-epss-correlation

[^1_62]: https://securityscorecard.com/blog/patch-cadence-and-management-best-practices/

[^1_63]: https://windowsforum.com/threads/understanding-cisas-known-exploited-vulnerabilities-catalog-and-its-critical-role-in-cybersecurity.362810/

[^1_64]: https://xygeni.io/es/sscs-glossary/what-is-kevs-known-exploited-vulnerabilities/

[^1_65]: https://sevenice.net/cisa-agrega-cinco-vulnerabilidades-explotadas-conocidas-al-catalogo-3/2

[^1_66]: https://www.q2bstudio.com/nuestro-blog/1425/cisa-agrega-vulnerabilidad-catalogo-kev

[^1_67]: https://www.ecucert.gob.ec/wp-content/uploads/2025/03/AL-2025-009-vulnerabilidad-Adobe-y-Oracle.pdf

[^1_68]: https://es.linkedin.com/pulse/reporte-principales-vulnerabilidades-explotadas-7aa0e

[^1_69]: https://noticias.unad.edu.co/index.php/2025/7905-agencia-cisa-anade-dos-nuevas-vulnerabilidades-activamente-explotadas-al-catalogo-estan-sus-sistemas-en-riesgo

[^1_70]: https://enhacke.com/blog/microsoft-corrige-67-vulnerabilidades-incluido-un-zero-day-en-webdav-ya-explotado-684997ea9fd6b

[^1_71]: https://sevenice.net/cisa-agrega-dos-vulnerabilidades-explotadas-conocidas-al-catalogo/3

[^1_72]: https://translate.google.com/translate?u=https%3A%2F%2Fwww.cisa.gov%2Fknown-exploited-vulnerabilities-catalog\&hl=es\&sl=en\&tl=es\&client=srp

[^1_73]: https://gammaingenieros.com/wp-content/uploads/2023/11/BOLETIN-DE-CIBERSEGURIDAD-SEMANAL_EDICION-1823.pdf

[^1_74]: https://translate.google.com/translate?u=https%3A%2F%2Fwww.armosec.io%2Fglossary%2Fknown-exploited-vulnerabilities-catalog-kev%2F\&hl=es\&sl=en\&tl=es\&client=srp

[^1_75]: https://bequo.io/cisa-agrega-una-vulnerabilidad-explotada-conocida-al-catalogo-16

[^1_76]: https://www.keysight.com/blogs/en/tech/nwvs/2023/08/25/cisa-alert-2022-top-routinely-exploited-vulnerabilities

[^1_77]: https://fossa.com/blog/using-cisa-kev-catalog

[^1_78]: https://www.defendedge.com/aa23-215a/

[^1_79]: https://newsletter.radensa.ru/wp-content/uploads/2023/08/aa23-215a_joint_csa_2022_top_routinely_exploited_vulnerabilities.pdf

[^1_80]: https://www.vulncheck.com/blog/kev-prioritization

[^1_81]: https://www.picussecurity.com/resource/blog/cisa-aa23-215a-lessons-learned-from-top-routinely-exploited-vulnerabilities-of-2022

[^1_82]: https://nucleussec.com/resources/guides/guide-to-cisa-kev-enrichment/

[^1_83]: https://www.tenable.com/blog/aa23-215a-2022s-top-routinely-exploited-vulnerabilities

[^1_84]: https://www.wiz.io/blog/detect-and-prioritize-cisa-known-exploited-vulnerabilities-kev-with-wiz


---