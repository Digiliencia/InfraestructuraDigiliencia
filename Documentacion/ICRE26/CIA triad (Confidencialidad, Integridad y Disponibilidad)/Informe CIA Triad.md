# CIA Triad: Indicadores y Métricas de Ciberseguridad 2025
## España ante el Mundo — Análisis Exhaustivo para Líderes de Seguridad

***

> *"Lo que no se mide no se puede proteger; lo que no se protege, inevitablemente, se pierde."*
> — Adaptación libre del principio de gestión de Drucker al lenguaje de los CISO del siglo XXI.

***

## 1. Encuadre Epistemológico: El Tridente Imperecedero

La tríada CIA —Confidencialidad (*Confidentiality*), Integridad (*Integrity*) y Disponibilidad (*Availability*)— no es, para quien la practique con rigor, un mero acrónimo corporativo. Es la arquitectura conceptual que subyace a cualquier política de seguridad de la información digna de ese nombre, desde los primeros formalismos de los años ochenta hasta los marcos normativos más recientes. A diferencia de las modas tecnológicas —que llegan y se van con la velocidad de las actualizaciones del firmware—, la tríada CIA ha demostrado una resiliencia singular: sobrevivió el paso del mainframe al cloud, del perímetro al Zero Trust, y ahora afronta el desafío cuántico y la inteligencia artificial con una ecuanimidad que envidiarían muchos marcos más jóvenes.[^1][^2][^3]

Su fortaleza reside precisamente en su abstracción: no prescribe tecnologías ni herramientas concretas, sino que articula resultados —confidencialidad de la información, exactitud de los datos, acceso garantizado— que toda organización, independientemente de su sector, tamaño o latitud geográfica, puede adoptar como brújula. Las organizaciones emplean la tríada para estructurar políticas, fundamentar evaluaciones de riesgo y justificar inversiones ante los consejos de administración.[^4][^5][^1]

Lo que sí ha evolucionado, y de forma vertiginosa a partir de 2024, son los **indicadores y métricas** asociados a cada uno de sus tres vértices. Este informe aborda precisamente esa evolución, con datos frescos de 2025, poniendo a España en el centro del análisis sin perder de vista el contexto global.

***

## 2. El Ecosistema de Amenazas en 2025: El Sustrato que Alimenta las Métricas

Antes de analizar los indicadores propios de cada pilar, conviene trazar el mapa del territorio. Sin comprender la naturaleza y la escala de las amenazas, los indicadores carecen de contexto y los umbrales de alerta pierden significado.

### 2.1. España: Récord de Incidentes y Madurez Institucional en Tensión

El año 2025 ha sido, con diferencia, el más exigente de la historia reciente de la ciberseguridad española. El INCIBE-CERT gestionó **122.223 incidentes de ciberseguridad**, un incremento del **26% respecto a los 97.348 de 2024**, constituyendo la cifra más alta jamás registrada por el organismo. Desglosando este número, emerge un paisaje con diferentes matices:[^6][^7]

| Categoría de Incidente | Cifra 2025 | Variación |
|---|---|---|
| **Malware** (total) | 55.411 casos | Tipo más frecuente |
| — de los cuales, ransomware | 392 ataques | Alto impacto unitario |
| **Fraude online** | 45.445 casos | +19% vs. 2024 |
| — de los cuales, phishing | 25.133 casos | Método más frecuente |
| **Robo de información / accesos no autorizados** | 3.849 casos | — |
| **Sistemas vulnerables notificados** | 237.028 sistemas | — |
| **Operadores esenciales (NIS2)** | 401 incidentes | Banca 34%, Transporte 14% |

*Fuente: INCIBE, Balance de Ciberseguridad 2025 *[^7][^8][^6]

El dato de los **237.028 sistemas vulnerables** detectados y notificados proactivamente por INCIBE-CERT merece un comentario especial: representa casi un cuarto de millón de vectores de ataque potenciales en infraestructuras conectadas a internet en territorio español. El 85% de las botnets detectadas estaban relacionadas con dispositivos IoT —televisores, decodificadores, reproductores multimedia—, lo que evidencia que la superficie de ataque ya no se circunscribe a los activos TI tradicionales.[^8]

El ámbito de la administración pública también ha sufrido episodios de alta visibilidad. INCIBE registró ataques de ransomware contra los municipios de Melilla y Villajoyosa (Alicante) que provocaron la **inoperatividad de los sistemas informáticos municipales durante cerca de dos semanas**, con impacto directo en servicios administrativos esenciales. Estos casos ilustran, con dolorosa concreción, las consecuencias de un indicador de **disponibilidad** en colapso.[^9]

Paradójicamente, la posición estratégica de España en el panorama internacional de la ciberseguridad es sólida. Según el **Índice Global de Ciberseguridad (GCI) 2024 de la UIT**, España se sitúa en el **Tier 1** (nivel de máximo compromiso), con una puntuación de 99,74 sobre 100 —la máxima en todas las categorías salvo desarrollo de capacidades, donde alcanza los 19,74 puntos—, posicionándola entre los veinte países europeos con la calificación "role-modelling". El Gobierno español es, según la propia UIT, el **segundo país del mundo** con más centros de ciberseguridad, solo superado por Estados Unidos.[^10][^11][^12]

Esta aparente contradicción —cifras de incidentes récord y posición institucional de primera fila— no es, en realidad, paradójica. Responde a una realidad estructural: mayor madurez institucional implica mayor capacidad de detección y notificación, no necesariamente mayor incidencia real. El Consejo de Ministros aprobó en mayo de 2025 un paquete de actuaciones complementarias al Plan Nacional de Ciberseguridad con una inversión de **1.157 millones de euros**, orientado a reforzar desde la prevención hasta la recuperación.[^13][^14][^10]

### 2.2. Europa: El Panorama ENISA 2025

El **ENISA Threat Landscape 2025**, que cubre el período julio de 2024 a junio de 2025 basándose en aproximadamente **4.875 incidentes seleccionados**, revela que la Unión Europea sigue siendo objetivo prioritario de actores de amenaza heterogéneos y con motivaciones convergentes:[^15][^16]

- **DDoS**: 77% de los incidentes reportados, liderados por hacktivistas, con apenas el 2% causando disrupción real de servicios.
- **Ransomware**: La amenaza de mayor impacto operativo. En España, el grupo Qilin encabeza el ranking, seguido por Akira y FOG, con la industria manufacturera como sector más afectado.[^15]
- **Administración pública**: 38,2% de los objetivos, blanco predilecto de hackactivistas y actores estatales.
- **Vectores de intrusión dominantes**: Phishing (60%) y explotación de vulnerabilidades (21,3%).[^16][^17]

El informe de **Inversiones NIS 2025 de ENISA**, con datos de 1.080 profesionales en 27 Estados miembros, fotografía el contexto de recursos:[^18][^19]

- Presupuesto mediano de ciberseguridad: **1,5 millones de euros** (9% del presupuesto TI).
- Déficit estructural de talento: **299.000 profesionales** en la UE.
- El 28% de las organizaciones tarda **más de tres meses** en parchear vulnerabilidades críticas.
- El 30% no realizó ninguna evaluación de seguridad en el último año.[^20]

### 2.3. El Mundo: Datos Globales de Referencia

El ecosistema global de amenazas proporciona el marco de comparación necesario para contextualizar los indicadores españoles y europeos:

**Verizon DBIR 2025** — El mayor dataset de la historia del informe: 22.052 incidentes y 12.195 brechas confirmadas en 139 países:[^21][^22]
- Ransomware presente en el **44% de las brechas** (pago mediano: $115K; el 64% de víctimas rechazó pagar).
- Terceros implicados en el **30% de las brechas** (el doble respecto al año anterior).
- Credenciales robadas: 22%; explotación de vulnerabilidades: 20%.
- Factor humano: presente en el **60% de las brechas**.
- Espionaje: aumento del **163%**, representando el 17% de las brechas.

**IBM Cost of a Data Breach 2025** — El coste medio global de una brecha cayó a **$4,44 millones** (-9%), pero el ciclo de vida promedio de una brecha se redujo a **241 días** (mínimo en nueve años: 158 días de detección + 83 de contención). Las organizaciones con herramientas de IA detectan brechas **80 días antes** y ahorran **$1,9 millones** de media.[^23][^24][^25]

***

## 3. Indicadores de CONFIDENCIALIDAD: Blindar lo que No Debe Verse

La confidencialidad garantiza que la información sea accesible únicamente a quienes están autorizados para conocerla. En la práctica operativa de 2025, sus indicadores han evolucionado hacia la medición continua y automatizada, alejándose de los controles puntuales de auditoría.[^5][^4]

### 3.1. Métricas Técnicas Nucleares

**1. Cobertura de Autenticación Multifactor (MFA Coverage)**

*Fórmula*: \(\text{MFA Coverage} = \frac{\text{Usuarios y sistemas críticos con MFA activo}}{\text{Total de usuarios y sistemas críticos}} \times 100\)

El 94% de las organizaciones incrementaron su adopción de MFA como medida de confidencialidad. Sin embargo, la simple implantación ya no basta: los indicadores avanzados distinguen entre MFA resistente al phishing (basado en FIDO2/passkeys) y MFA vulnerable (OTP por SMS). Una cobertura MFA del 100% sobre métodos vulnerables puede generar una falsa sensación de seguridad.[^2]

- **Umbral mínimo ENS**: Obligatorio en sistemas de nivel Alto (RD 311/2022).[^26]
- **Umbral aspiracional**: 100% en sistemas críticos con MFA resistente al phishing.

**2. Tasa de Cifrado de Datos en Reposo y Tránsito**

*Fórmula*: \(\text{Encryption Coverage} = \frac{\text{Activos cifrados}}{\text{Total de activos con datos sensibles}} \times 100\)

El cifrado aparece como el **principal mitigador de costes de brecha** en el informe IBM 2025, con un ahorro medio de $208.087 por incidente. El ENS obliga al cifrado de información de nivel Confidencial y Alto. La tendencia 2025 incorpora la distinción entre cifrado clásico y cifrado post-cuántico híbrido (ver sección 6).[^24][^26]

**3. Data Loss Prevention (DLP) — Tasa de Detección de Exfiltración**

Este indicador mide el porcentaje de eventos de exfiltración potencial detectados por controles DLP antes de que los datos abandonen el perímetro de control organizacional. En 2025, el 30% de las brechas globales involucran datos en múltiples entornos (cloud + on-premise), con un coste medio de $5,05 millones —el más alto de cualquier tipología—.[^27]

**4. Tiempo Medio de Detección de Brechas de Confidencialidad (MTTD-C)**

Las brechas relacionadas con credenciales robadas tardaron en 2025 una media de **292 días en detectarse y contenerse** (IBM). Este indicador, desglosado por tipo de brecha (phishing, credentials, insider), permite priorizar inversiones en detección.[^27]

**5. Cobertura de Control de Acceso Privilegiado (PAM Coverage)**

La gestión de cuentas privilegiadas es crítica: los insiders maliciosos generaron brechas con coste medio de **$4,92 millones** en 2025, la tipología más costosa de todas. El indicador mide:[^28][^23]
- Número de cuentas privilegiadas activas / total de cuentas privilegiadas inventariadas.
- Porcentaje con acceso revisado en los últimos 90 días.
- Porcentaje vinculado a identidades verificadas con registro de auditoría trazable.

### 3.2. Indicadores Avanzados: IA, Shadow AI y Zero Trust

**6. Índice de Exposición por Shadow AI**

Indicador emergente en 2025: el 63% de las organizaciones carecen de políticas de gobernanza para gestionar el "shadow AI" (uso de IA no sancionado), y el 97% de las brechas relacionadas con IA ocurrieron donde faltaban controles de acceso adecuados. La ausencia de este indicador en los cuadros de mando CISO representa una laguna crítica.[^28]

*Fórmula orientativa*: \(\text{Shadow AI Risk Score} = \frac{\text{Instancias de IA no inventariadas}}{\text{Total de instancias de IA detectadas}} \times \text{Factor de impacto de datos}\)

**7. Cobertura Zero Trust de Identidad**

Basado en el NIST SP 1800-35 (publicado en junio de 2025), mide el porcentaje de accesos que siguen el principio "never trust, always verify". Investigaciones en entornos de defensa muestran que la implementación rigurosa de Zero Trust reduce los incidentes de acceso no autorizado en un **63,7%**.[^29][^30]

**8. Tasa de Clicks en Simulacros de Phishing**

El phishing fue el vector más frecuente de brechas en 2025 (16% de incidentes IBM, 60% de intrusiones ENISA). Este indicador mide la resiliencia humana, no la técnica, y complementa las métricas tecnológicas con la dimensión conductual. Las organizaciones con formación activa observan una reducción de la tasa de clics de hasta 4x.[^16][^23][^21]

### 3.3. Cuadro de Mando de Confidencialidad para España

| Indicador | Umbral Crítico | Umbral Objetivo | Referencia |
|---|---|---|---|
| Cobertura MFA (sistemas críticos) | < 70% | ≥ 99% | NIST CSF 2.0 / ENS |
| Cifrado datos en reposo | < 80% | 100% | ISO 27001:2022 / ENS |
| MTTD-C (brechas credenciales) | > 180 días | < 60 días | IBM 2025 |
| PAM Coverage | < 60% | ≥ 95% | NIST SP 800-53 R5 |
| Tasa phishing (simulacros) | > 20% clicks | < 5% clicks | ENISA / INCIBE |
| Shadow AI inventariado | < 50% | ≥ 95% | IBM 2025 |

***

## 4. Indicadores de INTEGRIDAD: La Exactitud como Forma de Dignidad

La integridad garantiza que la información permanezca exacta, consistente y no haya sido alterada de forma no autorizada a lo largo de su ciclo de vida. Es, de los tres pilares, el que más ambigüedad operativa genera: a diferencia de la confidencialidad (binaria: accedido o no) o la disponibilidad (medible en tiempo de actividad), la integridad requiere mecanismos de verificación activa y continua.[^31][^4][^5]

El debate epistemológico de 2025 sobre la integridad en la tríada CIA es revelador: la vaguedad del concepto en entornos operativos modernos —donde la IA puede alterar datos de formas difícilmente detectables sin contexto semántico— exige una operacionalización más sofisticada que la simple comprobación de hashes.[^31]

### 4.1. Métricas Técnicas Nucleares

**9. Cobertura de Monitorización de Integridad de Ficheros (FIM Coverage)**

*Fórmula*: \(\text{FIM Coverage} = \frac{\text{Activos críticos con FIM activo (SHA-256)}}{\text{Total de activos críticos}} \times 100\)

El hash SHA-256 sigue siendo el estándar de facto para la verificación de integridad de archivos. Los indicadores avanzados incluyen la frecuencia de verificación (tiempo real vs. diferido) y el porcentaje de alertas FIM procesadas en menos de 15 minutos.[^32]

**10. Tiempo Mediano de Parcheo de Vulnerabilidades Críticas (TMPVC)**

Este indicador conecta directamente integridad y disponibilidad: las vulnerabilidades sin parchear son vectores de manipulación de datos. Datos globales alarmantes de ENISA 2025: el **28% de las organizaciones europeas** tardó más de tres meses en parchear vulnerabilidades críticas. En el caso concreto de dispositivos de borde (edge) y VPN, el **Verizon DBIR 2025** constata que solo el **54% están parcheados**, con un tiempo mediano de remediación de **32 días**.[^21][^20]

- **Referencia ENS**: Las guías CCN-STIC establecen plazos máximos diferenciados por criticidad.
- **Referencia DORA**: Obligación de reporting de vulnerabilidades con plazos específicos para entidades financieras.[^33]

**11. Tasa de Detección de Alteraciones no Autorizadas**

*Fórmula*: \(\text{Tampering Detection Rate} = \frac{\text{Alteraciones no autorizadas detectadas}}{\text{Total de alteraciones reales (estimadas)}} \times 100\)

Indicador de segunda generación que requiere capacidades de threat hunting para estimación del denominador. Se correlaciona con la cobertura SIEM/XDR y la calidad de los logs de auditoría.

**12. Ratio de Errores Humanos Causantes de Incidentes de Integridad**

El factor humano estuvo presente en el **60% de las brechas globales en 2025**. Para la integridad, los errores relevantes incluyen modificaciones accidentales de configuraciones, errores en scripts de automatización y permisos excesivos. Este indicador se alimenta del registro de incidentes y se alinea con la metodología de clasificación VERIS utilizada por Verizon DBIR.[^21]

**13. Cobertura de Firma Digital y No Repudio**

Indicador vinculado al modelo extendido CIANA (Confidentiality, Integrity, Availability, Non-repudiation, Authenticity). Mide el porcentaje de transacciones críticas, documentos oficiales y comunicaciones de alto riesgo respaldados por firma digital verificable. El ENS español ya incorpora explícitamente los requisitos de **autenticidad y trazabilidad** como dimensiones adicionales a la tríada clásica. La directiva DORA exige garantías de autenticidad e integridad en las comunicaciones de las entidades financieras.[^34][^35][^26]

**14. Índice de Cobertura MITRE ATT&CK para Tácticas de Manipulación de Datos**

Las evaluaciones MITRE ATT&CK Enterprise 2025 —en las que participaron once proveedores— midieron cobertura de detección frente a técnicas de manipulación de datos, con algunos vendedores alcanzando el **100% de detección y cobertura**. Este índice permite comparar la capacidad de detección de alteraciones frente al catálogo de técnicas adversariales conocidas.[^36][^37]

### 4.2. Indicadores Emergentes: Integridad de Datos en IA

La integridad de los modelos de IA emerge como un nuevo frente en 2025. Los ataques de envenenamiento de datos (*data poisoning*), el robo de modelos (*model theft*) y los ataques adversariales comprometen la integridad no ya de los datos, sino de los sistemas de decisión que los procesan. El indicador correspondiente —**Tasa de Detección de Anomalías en Datos de Entrenamiento**— es de implementación incipiente pero creciente en organizaciones que despliegan IA en procesos críticos.[^38][^39]

Según IBM 2025, el 16% de todas las brechas involucraron atacantes usando IA, con el 37% empleando phishing generado por IA y el 35% utilizando deepfakes. Esta dimensión añade un matiz cualitativo a los indicadores de integridad tradicionales: no es solo verificar que el dato no fue modificado, sino que el dato mismo no fue generado sintéticamente de forma maliciosa.[^40]

**15. Índice de Espionaje como Amenaza para la Integridad**

El **163% de aumento en brechas motivadas por espionaje** en el Verizon DBIR 2025, que representan ya el 17% del total, introduce un vector de integridad frecuentemente subestimado: la modificación subrepticia de información de inteligencia o documentación oficial. Este tipo de amenaza exige indicadores orientados a la persistencia de acceso y la detección de alteraciones de baja magnitud pero alto impacto estratégico.[^21]

### 4.3. Cuadro de Mando de Integridad

| Indicador | Umbral Crítico | Umbral Objetivo | Referencia |
|---|---|---|---|
| FIM Coverage (activos críticos) | < 70% | 100% | NIST SP 800-53 / ENS |
| Tiempo mediano de parcheo (críticas) | > 90 días | < 15 días | ENISA NIS 2025 / DORA |
| Cobertura firma digital | < 60% | ≥ 95% | ENS / DORA / eIDAS |
| Cobertura ATT&CK detección de tampering | < 50% | ≥ 85% | MITRE ATT&CK 2025 |
| Tasa errores humanos en incidentes | > 30% | < 10% | Verizon DBIR 2025 |
| Anomalías datos IA detectadas (alertas/mes) | 0 (sin monitorización) | Monitorización continua | NIST AI RMF |

***

## 5. Indicadores de DISPONIBILIDAD: El Derecho al Acceso Ininterrumpido

La disponibilidad garantiza que los sistemas e información sean accesibles para los usuarios autorizados cuando los necesitan. Es el pilar más fácil de operacionalizar —el uptime es un número, el tiempo de inactividad es un coste cuantificable—, pero también el que más directamente traduce los fallos de ciberseguridad en impacto operativo y reputacional.[^4][^5]

### 5.1. Métricas Técnicas Nucleares

**16. Disponibilidad del Sistema / SLA de Uptime**

La fórmula canónica:

\[\text{Disponibilidad} = \frac{MTBF}{MTBF + MTTR} \times 100\]

Donde MTBF (*Mean Time Between Failures*) y MTTR (*Mean Time To Recover*) son los componentes fundamentales. Los umbrales de referencia por SLA:[^41]

| Nivel de SLA | Disponibilidad | Tiempo máximo de inactividad/año |
|---|---|---|
| Tres nueves (99,9%) | Alta | 8h 45min |
| Cuatro nueves (99,99%) | Muy alta | 52 min |
| Cinco nueves (99,999%) | Excelente | 5 min |

*Fuente: SOC 2 Availability Trust Service Criteria *[^41]

**17. RTO (Recovery Time Objective) y RPO (Recovery Point Objective)**

Son las métricas de disponibilidad más directamente relacionadas con la continuidad del negocio:[^42][^43]

- **RTO**: Tiempo máximo tolerable de inactividad tras un incidente. Define cuánto puede estar "caído" un sistema.
- **RPO**: Pérdida máxima tolerable de datos medida en tiempo. Define la frecuencia mínima de backup.
- **MTD (Maximum Tolerable Downtime)**: El umbral absoluto más allá del cual el daño es irreversible.

La directiva DORA exige la definición y prueba de estos parámetros para todas las entidades financieras de la UE. El ENS español articula requisitos equivalentes para la administración pública.[^44][^26][^33][^34]

**18. MTTD, MTTR y MTTC — El Trío Operativo**

Tres indicadores interdependientes que miden la eficiencia del ciclo de respuesta:[^45][^46][^47]

- **MTTD** (*Mean Time to Detect*): Tiempo medio desde la ocurrencia hasta la detección. El benchmark global en 2025 es de 158 días (IBM). Con IA, las organizaciones detectan **80 días antes**.[^24]
- **MTTR** (*Mean Time to Respond*): Tiempo desde la detección hasta la resolución.
- **MTTC** (*Mean Time to Contain*): Tiempo desde la detección hasta el aislamiento del incidente.

Fórmula del MTTD:
\[\text{MTTD} = \frac{\sum (\text{Tiempo detección} - \text{Tiempo ocurrencia})}{n \text{ incidentes}}\]

El coste diferencial es contundente: las brechas detectadas y contenidas en **menos de 200 días** cuestan de media **$3,61 millones**, frente a los **$5,49 millones** de las que superan ese umbral —una diferencia de $1,88 millones.[^24]

**19. Tasa de Incidentes DDoS con Disrupción Efectiva**

El informe ENISA 2025 revela un dato estratégicamente importante: aunque los DDoS representaron el **77% de los incidentes reportados** en la UE, apenas el **2% causó disrupción real de servicios**. Este indicador —tasa de DDoS con impacto en disponibilidad / total DDoS— permite evaluar la eficacia de los controles anti-DDoS y evitar el ruido estadístico que distorsiona la percepción del riesgo real.[^15][^16]

**20. Tasa de Recuperación de Ransomware (RRR — Ransomware Recovery Rate)**

Dado el protagonismo del ransomware en la afectación a la disponibilidad —392 ataques en España en 2025; presente en el 44% de las brechas globales—, este indicador mide el porcentaje de sistemas restaurados desde backup sin pago de rescate, en el tiempo objetivo definido por el RTO. El 64% de las víctimas globales rechazaron pagar en 2025. Involucrar a fuerzas del orden redujo los costes de brecha en aproximadamente $1 millón.[^8][^27][^21]

**21. Índice de Cobertura de Parches en Dispositivos de Borde**

Las vulnerabilidades en dispositivos de borde (edge) y VPN aumentaron **ocho veces** su presencia en los vectores de acceso inicial según Verizon DBIR 2025. Solo el **54% de estos dispositivos estaban parcheados** cuando fueron explotados. Este indicador específico de disponibilidad mide la superficie de riesgo más directamente explotable.[^21]

### 5.2. Indicadores de Disponibilidad en Infraestructuras Críticas

El Cisco Cybersecurity Readiness Index 2025 presenta un diagnóstico específico para España: la **resiliencia de red está retrocediendo**, con una caída del nivel "Progressive" al nivel "Formative" — la dirección contraria a la deseada. Este retroceso sugiere que la expansión acelerada de infraestructuras digitales supera la capacidad de los controles de seguridad correspondientes.[^48]

España clasifica los siguientes sectores como infraestructuras críticas: administración pública, espacio, químico/nuclear, agua, energía, TIC, salud, transporte, alimentación, finanzas y seguridad/defensa. El marco normativo para la protección de estas infraestructuras —el Plan Nacional de Protección de Infraestructuras Críticas (PNPIC)— obliga a la definición de indicadores de disponibilidad diferenciados por sector.[^49]

El informe del **Financial Stability Board (FSB) sobre España** (noviembre 2025) recomendó, entre otras medidas, el establecimiento de **un canal único nacional para la notificación de incidentes** que centralice y agilice la gestión de crisis con impacto en disponibilidad.[^50]

**22. Densidad de Sistemas Vulnerables IoT por Sector**

El 85% de las botnets detectadas por INCIBE en 2025 tienen origen en dispositivos IoT. Este indicador sectorizado —número de sistemas vulnerables IoT notificados / total de sistemas IoT inventariados, por sector— permite priorizar esfuerzos de remediación con criterios de criticidad.[^8]

### 5.3. Cuadro de Mando de Disponibilidad

| Indicador | Umbral Crítico | Umbral Objetivo | Referencia |
|---|---|---|---|
| Uptime SLA (sistemas esenciales) | < 99,9% | ≥ 99,99% | SOC 2 / ENS / DORA |
| RTO (sistemas críticos) | > 4 horas | < 15 minutos | DORA / ISO 22301 |
| RPO (datos críticos) | > 24 horas | < 1 hora | DORA / ISO 22301 |
| MTTD (promedio incidentes) | > 200 días | < 60 días | IBM 2025 |
| MTTC | > 30 días | < 24 horas | NIST CSF 2.0 |
| Cobertura anti-DDoS | < 60% | 100% activos críticos | ENISA 2025 |
| RRR (recuperación sin pago) | < 50% | ≥ 90% | Verizon DBIR 2025 |
| Parches edge/VPN aplicados | < 54% | ≥ 95% | Verizon DBIR 2025 |

***

## 6. La Expansión del Modelo: Del CIA al CIANA y Más Allá

El ENS español, en su versión actualizada por el Real Decreto 311/2022, supera desde hace años la tríada clásica: define como dimensiones de seguridad de la información la **confidencialidad, integridad, disponibilidad, autenticidad, trazabilidad y conservación**. Esta expansión es doctrinalmente significativa: reconoce que la tríada CIA, siendo necesaria, no es suficiente en el contexto regulatorio y operativo moderno.[^26]

A nivel internacional, se consolida la propuesta del **pentágono CIANA** —*Confidentiality, Integrity, Availability, Non-repudiation, Authenticity*—, que añade el **No Repudio** (la imposibilidad de que un actor niegue haber realizado una acción documentada) y la **Autenticidad** (la garantía de que la comunicación o documento procede de quien dice proceder):[^35][^51]

- **No Repudio**: Abordado en el NIST SP 800-53 R5 bajo la familia de controles AU-10 (*Audit and Accountability*). Indicadores relevantes: cobertura de logs con firma criptográfica; tasa de cadenas de custodia digitales completas en incidentes litigados.[^35]
- **Autenticidad**: Conectada con PKI, certificados digitales, eIDAS 2 y la gestión de identidades federadas. Indicadores: porcentaje de transacciones con verificación criptográfica de origen; cobertura de certificados de confianza cualificada.[^51]

El mapeo CIANA con STRIDE (*Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege*) proporciona una herramienta de análisis de amenazas particularmente útil: cada vector de STRIDE ataca, al menos, uno de los cinco vértices del pentágono.[^52]

***

## 7. El Desafío Cuántico: Cuando los Cimientos Criptográficos Tiemblan

El impacto de la computación cuántica sobre la tríada CIA constituye el reto sistémico más significativo para la próxima década. No es un riesgo inmediato —el MITRE estima que un ordenador cuántico capaz de romper RSA-2048 no llegará antes de 2055-2060, aunque algunos expertos lo adelantan a 2035— pero la **latencia del riesgo** exige actuar hoy.[^53]

### 7.1. Impacto por Pilar CIA

**Confidencialidad — El Ataque "Harvest Now, Decrypt Later" (HNDL)**

El algoritmo de Shor puede romper RSA y ECC una vez exista un ordenador cuántico suficientemente potente. La estrategia HNDL —capturar datos cifrados hoy para descifrarlos mañana— afecta ya al 67% de las organizaciones encuestadas en una revisión sistemática de 847 implementaciones criptográficas. El indicador crítico es la **proporción de datos sensibles cifrados con algoritmos vulnerables a ataques cuánticos** frente al total de activos de información clasificados.[^54]

**Integridad — La Forjabilidad de Firmas Digitales**

Los ataques cuánticos pueden comprometer las funciones hash y los algoritmos de firma digital (RSA, ECDSA) utilizados para verificar la integridad de software, certificados y comunicaciones. La tasa de **cobertura de migración a algoritmos PQC para firma** es el indicador de integridad más urgente en este contexto.[^55]

**Disponibilidad — Disrupción de Infraestructuras de Cifrado en Tránsito**

Una disrupción de los sistemas criptográficos que protegen las comunicaciones en tránsito podría paralizar infraestructuras críticas. El indicador de resiliencia cuántica para disponibilidad es el porcentaje de canales de comunicación crítica migrados a protocolos resistentes a ataques cuánticos.[^56]

### 7.2. Los Estándares PQC del NIST: La Respuesta Institucional

En agosto de 2024, el NIST publicó los **tres primeros estándares de criptografía post-cuántica (PQC)**:[^57][^58]

| Estándar FIPS | Algoritmo | Tipo | Aplicación |
|---|---|---|---|
| FIPS 203 | ML-KEM (Kyber) | Encapsulación de clave | Intercambio de claves / TLS |
| FIPS 204 | ML-DSA (Dilithium) | Firma digital | Autenticación / PKI |
| FIPS 205 | SLH-DSA (SPHINCS+) | Firma digital (respaldo) | Autenticación / PKI |

El NIST deprecará los algoritmos clásicos vulnerables para **2035**, con transición acelerada para sistemas de alta criticidad. La Agencia de Seguridad Nacional de EE.UU. (NSA) inició la migración bajo el marco CNSA 2.0 en 2025. El Falcon (firma digital) y HQC (KEM) se encuentran en proceso de estandarización adicional.[^59][^57]

El indicador de madurez para la transición PQC es el **Índice de Cripto-Agilidad**: la capacidad de una organización para reemplazar algoritmos criptográficos sin rediseñar los sistemas que los utilizan. Este índice, de medición compleja pero creciente relevancia, se convierte en el indicador transversal de confidencialidad e integridad para los próximos diez años.[^60]

Un marco híbrido de IA + PQC puede reducir la exposición a vulnerabilidades en un **94%** manteniendo un uptime del **99,4%**, con una eficiencia de coste un **37% inferior** al promedio industrial para PQC independiente.[^54]

***

## 8. El Marco Normativo Español: ENS, NIS2, DORA y los Indicadores de Cumplimiento

### 8.1. El Esquema Nacional de Seguridad (ENS)

El ENS —actualizado por el Real Decreto 311/2022— es el instrumento normativo español que traduce operativamente la tríada CIA (y sus extensiones) para el sector público y los proveedores privados que prestan servicios a la Administración. Define tres **niveles de seguridad** (Básico, Medio, Alto) y cinco **dimensiones** (confidencialidad, integridad, disponibilidad, autenticidad y trazabilidad), aplicando el principio de proporcionalidad.[^61][^44][^26]

Los indicadores del ENS se articulan, entre otras referencias, en las guías **CCN-STIC** del Centro Criptológico Nacional, siendo la **CCN-STIC-817** el documento de referencia para métricas de gestión de ciberincidentes. La metodología de adecuación sigue el ciclo PDCA (Plan-Do-Check-Act) inspirado en ISO 27001.[^62][^44]

**Indicadores de cumplimiento ENS relevantes**:
- Porcentaje de sistemas de información categorizados y certificados.
- Resultado de auditorías ENS (número de no conformidades por dimensión CIA).
- Tiempo medio de resolución de no conformidades identificadas.
- Porcentaje de incidentes gestionados conforme al procedimiento CCN-STIC-817.

### 8.2. NIS2 y la Nueva Gobernanza de Ciberseguridad en España

La Directiva NIS2 entró en vigor en España el 17 de octubre de 2024. En enero de 2025, el Consejo de Ministros aprobó el **Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad**, que establece el nuevo **Centro Nacional de Ciberseguridad (CNCS)** bajo la tutela del Ministerio del Interior, integrando la supervisión sobre el CCN-CERT (sector público) e INCIBE-CERT (sector privado). Las sanciones por incumplimiento alcanzan los **10 millones de euros o el 2% del volumen de negocio global**.[^63][^64]

Los indicadores obligatorios bajo NIS2 incluyen:
- **Notificación temprana** de incidentes significativos: dentro de las **24 horas** (alerta inicial) y **72 horas** (notificación formal).[^33]
- **Evaluaciones periódicas de riesgo** con frecuencia mínima anual.
- Métricas de gestión de la **cadena de suministro**: evaluación del riesgo de terceros proveedores.
- Los sectores más afectados en España en 2025 (operadores esenciales): banca (34%), transporte (14%), energía (8%).[^7]

### 8.3. DORA: La Resiliencia Operacional Digital en el Sector Financiero

El **Digital Operational Resilience Act (DORA)**, vigente desde el 17 de enero de 2025, introduce para las entidades financieras europeas un marco específico de indicadores CIA orientados a la resiliencia operativa. Sus requisitos incluyen:[^34][^33]

- **Gestión del riesgo TIC**: controles de disponibilidad, autenticidad, integridad y confidencialidad documentados y medidos.
- **Pruebas de resiliencia digital**: TLPT (*Threat-Led Penetration Testing*) para entidades significativas.
- **Gestión de incidentes**: obligación de reporte con umbrales de impacto definidos (clasificación por criticidad).
- **Gestión de terceros críticos**: inventario y evaluación continua de proveedores TIC sistémicamente importantes.

El FSB, en su revisión de pares de España (noviembre 2025), reconoció las "buenas prácticas" del sector financiero español en resiliencia cibernética, aunque recomendó el desarrollo de un **mapa comprehensivo del panorama de amenazas** y la creación de un canal único de notificación de incidentes.[^50]

***

## 9. La Cuantificación del Riesgo: FAIR y las Métricas Financieras de la CIA Triad

La tendencia más significativa en la gestión de riesgos de ciberseguridad de 2025 es la **transición de métricas cualitativas a métricas financieras cuantitativas**. El modelo FAIR (*Factor Analysis of Information Risk*) lidera esta transformación: casi el **45% de las organizaciones** globales lo usan o planean usarlo, con una tasa de éxito del **90% entre los adoptantes**.[^65][^66]

La lógica FAIR aplicada a la tríada CIA permite expresar el riesgo como pérdida esperada anualizada (ALE), desglosada por pilar:

\[\text{ALE} = \text{ARO} \times \text{SLE}\]

Donde ARO (*Annual Rate of Occurrence*) es la frecuencia anual estimada del evento de pérdida, y SLE (*Single Loss Expectancy*) es el impacto esperado por ocurrencia. Esta formulación transforma los indicadores CIA en lenguaje de negocio comprensible para consejos de administración y reguladores.

Los **CISO, CIO y CTO** son los principales consumidores de esta información en el 2025. El mercado de seguros cibernéticos en España refleja esta maduración: los clientes de Aon registraron una **mejora interanual del 5% en la implementación de controles críticos**, y las primas de seguros cibernéticos cayeron un **7% en el primer trimestre de 2025** —décimo trimestre consecutivo de descensos—, en respuesta a la mejora de la postura de seguridad.[^67][^68][^69][^65]

***

## 10. Cuadro de Mando Integrado CIA para España: Dashboard Estratégico

La siguiente tabla sintetiza los indicadores más relevantes para la gobernanza de la ciberseguridad a nivel nacional, organizados por pilar y con referencias normativas específicas para el contexto español.

| Pilar | Indicador | Cómo se mide | Referencia Normativa |
|---|---|---|---|
| **C** | Cobertura MFA resistente al phishing | % usuarios con MFA FIDO2/passkeys | ENS / NIS2 / NIST CSF 2.0 |
| **C** | Tasa de cifrado activos sensibles | % activos CIA con cifrado activo | ISO 27001 / ENS / DORA |
| **C** | MTTD-C (brechas credenciales) | Días detección brechas de identidad | IBM 2025 / ENS CCN-STIC |
| **C** | Cobertura inventario Shadow AI | % instancias IA inventariadas | ISO 42001 / AI Act |
| **C** | Tasa phishing en simulacros | % clicks sobre correos simulados | NIST SP 800-50 / INCIBE |
| **I** | FIM Coverage activos críticos | % activos con hash verificación activa | ENS Nivel Medio/Alto / NIST |
| **I** | Tiempo mediano de parcheo crítico | Días desde publicación CVE a parche | ENISA NIS 2025 / DORA |
| **I** | Cobertura PQC en sistemas críticos | % migración a ML-KEM/ML-DSA/SLH-DSA | NIST PQC 2024 / CCN |
| **I** | Tasa de detección de tampering | % alteraciones detectadas vs. reales | MITRE ATT&CK / NIST 800-53 |
| **I** | Cobertura de firma digital (no repudio) | % transacciones críticas firmadas | eIDAS 2 / DORA / ENS |
| **A** | MTTD (promedio todos los incidentes) | Días desde ocurrencia a detección | NIST CSF 2.0 / ENS |
| **A** | RTO sistemas críticos | Tiempo máximo de inactividad tolerable | DORA / ISO 22301 / ENS |
| **A** | RPO datos críticos | Pérdida máxima de datos tolerable | DORA / ISO 22301 / ENS |
| **A** | Tasa recuperación ransomware sin pago | % restauraciones desde backup | INCIBE / CCN-STIC / ENISA |
| **A** | Cobertura parches edge/VPN | % dispositivos perimetrales parcheados | Verizon DBIR 2025 / ENS |

***

## 11. Perspectiva Comparada: España en el Mundo

| Indicador Comparativo | España 2025 | UE (mediana 2025) | EE.UU. 2025 | Global 2025 |
|---|---|---|---|---|
| Incidentes gestionados (CERT nacional) | 122.223 (+26%) | — | — | — |
| Posición ITU GCI | Tier 1 (99,74/100) | Tier 1 (20 países) | Tier 1 | — |
| Coste promedio brecha | — | ~$4,44M (global) | $10,22M | $4,44M |
| Tiempo detección brecha | — | — | 241 días | 241 días |
| Ransomware como % brechas | — | 44% (Verizon) | 44% | 44% |
| Madurez ciberseguridad empresarial | 61% Formative / 16% Mature [^48] | — | — | 4% Mature global |
| Presupuesto ciberseg. (% IT) | — | 9% (1,5M€ mediana) | — | — |
| Déficit profesionales | — | 299.000 (UE) | — | — |

La lectura de esta tabla revela tensiones productivas. España presenta indicadores institucionales excepcionales (Tier 1 ITU, infraestructura de CERTs robusta, marco regulatorio avanzado) mientras los datos operativos muestran un nivel de madurez empresarial en el que el 61% de las organizaciones se encuentran en estado "Formative" según Cisco CRI 2025. Esta brecha entre capacidad institucional y madurez operativa empresarial es, probablemente, el reto estratégico más relevante para la ciberseguridad española en el período 2025-2030.[^48]

***

## 12. Conclusiones y Líneas de Acción Estratégica

La tríada CIA sigue siendo el andamiaje conceptual indispensable para cualquier arquitectura de seguridad, pero su operacionalización exige, en 2025, una sofisticación que trasciende los controles clásicos. Las conclusiones estratégicas para España, en el marco comparado global, pueden articularse en cinco ejes:

**I. De la conformidad a la cuantificación**. La adopción del modelo FAIR y la expresión del riesgo CIA en términos financieros es el cambio cultural más urgente. El 45% de adopción global del modelo en organizaciones avanzadas contrasta con su penetración todavía incipiente en España, excepto en el sector financiero.[^65]

**II. La ventana de oportunidad post-cuántica**. Los estándares NIST PQC publicados en 2024 (FIPS 203, 204, 205) exigen acción inmediata, no en 2030. Los sistemas clasificados y las infraestructuras críticas deberían iniciar la migración ahora. El CCN tiene aquí un rol de liderazgo técnico insustituible.[^58][^57]

**III. La integridad bajo IA adversarial**. La proliferación de ataques de IA —phishing generado por IA en el 37% de brechas con componente IA; deepfakes en el 35%— requiere indicadores de integridad que incluyan la verificación de la procedencia y autenticidad del dato, no solo su integridad técnica.[^40]

**IV. El talento como palanca de disponibilidad**. El déficit de 299.000 profesionales en la UE es, en última instancia, un riesgo de disponibilidad sistémico. Sin las personas adecuadas para operar los sistemas de detección y respuesta, los indicadores técnicos son irrelevantes. Las inversiones en formación y retención de talento deben expresarse como indicadores de resiliencia operativa.[^18]

**V. La cadena de suministro como vector transversal**. Con el 30% de brechas globales vinculadas a terceros en 2025, los indicadores CIA deben extenderse a proveedores y socios. NIS2 y DORA ya lo exigen normativamente; la implementación operativa es la asignatura pendiente, con el 37% de las organizaciones europeas reportando dificultades en la gestión del riesgo de cadena de suministro.[^70][^20][^21]

La tríada CIA, como los grandes textos clásicos, no envejece. Se reinterpreta. Y cada época le exige que responda preguntas que sus autores nunca imaginaron. La pregunta de 2025 no es si proteger la confidencialidad, integridad y disponibilidad; es cómo medirlas con la precisión suficiente para tomar decisiones que marquen la diferencia entre la resiliencia y la capitulación digital.

***

*Fuentes primarias consultadas: INCIBE (Balance Ciberseguridad 2025), ENISA (Threat Landscape 2025, NIS Investments 2025), IBM (Cost of a Data Breach Report 2025), Verizon (DBIR 2025), Cisco (Cybersecurity Readiness Index 2025), NIST (CSF 2.0, SP 800-53 R5, SP 1800-35, PQC Standards FIPS 203-205), ITU (Global Cybersecurity Index 2024), FAIR Institute (State of Cyber Risk Management 2025), Aon (Global Cyber Risk Report 2025, Estudio Ciberseguridad España 2025), FSB (Peer Review Spain 2025), CCN-CNI (ENS, CCN-STIC-817), BOE (Orden PJC/448/2025), MITRE ATT&CK (Enterprise Evaluations 2025).*

---

## References

1. [The Confidentiality-integrity-availability (cia) Triad - Shadecoder](https://www.shadecoder.com/topics/the-confidentiality-integrity-availability-cia-triad-a-comprehensive-guide-for-2) - As organizations adopt new technologies in 2025, teams often use the triad to quickly articulate whe...

2. [Inside CIA Triad: How It's Revolutionizing Security in 2025 - Avatier](https://www.avatier.com/blog/cia-triad-revolutionizing-security/) - The CIA Triad—comprising Confidentiality, Integrity, and Availability—remains a foundational model g...

3. [The CIA Triad of confidentiality, integrity, availability - i-SCOOP](https://www.i-scoop.eu/cybersecurity/cia-confidentiality-integrity-availability-security/) - Confidentiality, integrity, and availability are known as the three essential goals, attributes, or ...

4. [CIA triad: Confidentiality, integrity, and availability - SailPoint](https://www.sailpoint.com/identity-library/cia-triad) - The CIA triad is an information security model that is based on three pillars—confidentiality, integ...

5. [What is the CIA triad (confidentiality, integrity and availability)?](https://www.techtarget.com/whatis/definition/Confidentiality-integrity-and-availability-CIA) - The CIA triad refers to confidentiality, integrity and availability, describing a model designed to ...

6. [Balance INCIBE 2025: 122.223 ciberincidentes en España (+26%)](https://digitalperito.es/blog/incibe-balance-2025-122000-ciberincidentes-espana/) - INCIBE gestionó 122.223 ciberincidentes en 2025, un 26% más. 55.411 malware, 25.133 phishing, 392 ra...

7. [INCIBE detectó más de 122.000 incidentes de ciberseguridad en 2025](https://www.incibe.es/incibe/sala-de-prensa/incibe-detecto-mas-de-122000-incidentes-de-ciberseguridad-en-2025) - Entre los incidentes más recurrentes en 2025 destacaron: Malware, con 55.411 casos, incluyendo virus...

8. [INCIBE gestionó 122.223 incidentes de ciberseguridad en 2025, un ...](http://espanadigital.gob.es/en/actualidad/incibe-gestiono-122223-incidentes-de-ciberseguridad-en-2025-un-26-mas-que-el-ano) - En 2025 los incidentes más recurrentes fueron: Malware: 55.411 casos, incluidos 392 ataques de ranso...

9. [Top 7 ciberincidentes durante el año 2025 | INCIBE-CERT](https://www.incibe.es/incibe-cert/publicaciones/bitacora-de-seguridad/top-7-ciberincidentes-durante-el-ano-2025) - En el año 2025, se han llevado a cabo algunos de los ataques cibernéticos más importantes y conocido...

10. [The Government approves a strengthening of Spain's cybersecurity ...](https://digital.gob.es/en/comunicacion/notas-prensa/mtdfp/2025/05/2025-05-06_02) - In 2024, more than 100,000 cyberattacks were detected in Spain and every three days there was one co...

11. [ITU Global Cybersecurity Index 2024](https://administracionelectronica.gob.es/pae_Home/en/pae_OBSAE/Posicionamiento-Internacional/Summary-Spain-international-rankings/ITU-Global-Cybersecurity-Index-2024.html)

12. [España obtiene una valoración casi perfecta en el Global ...](https://www.ituser.es/actualidad/2024/09/espana-obtiene-una-valoracion-casi-perfecta-en-el-global-cybersecurity-index-2024-de-itu) - Según el quinto informe elaborado por la International Telecommunication Union, Europa encabeza el c...

13. [El Gobierno aprueba un refuerzo de las capacidades de España en ...](https://digital.gob.es/comunicacion/notas-prensa/mtdfp/2025/05/2025-05-06_02) - El conjunto de actuaciones permitirá mejorar las capacidades de ciberseguridad y ciberdefensa de amp...

14. [BOE-A-2025-9088 Orden PJC/448/2025, de 6 de mayo, por la que ...](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-9088) - El Plan Nacional de Ciberseguridad concretó un conjunto de actuaciones para avanzar del modo más efi...

15. [ENISA 2025 Threat Landscape report highlights EU faces escalating ...](https://industrialcyber.co/reports/enisa-2025-threat-landscape-report-highlights-eu-faces-escalating-hacktivist-attacks-and-state-aligned-cyber-threats/) - Spain saw Qilin in first place, followed by Akira and FOG, with manufacturing being targeted the mos...

16. [European Union Agency for Cybersecurity (ENISA) - Threat ... - k3y](https://k3ylabs.com/blog/european-union-agency-for-cybersecurity-enisa-threat-landscape-2025/) - The report examines 4,875 incidents between 1 July 2024 and 30 June 2025, offering a clear view of t...

17. [Complete Guide to the ENISA 2025 Threat Landscape - PrivacyRise](https://privacyrise.com/blog/threat-landscape-enisa-2025/) - It is an 87-page report offering a clear picture of the cybersecurity threat ecosystem in Europe, co...

18. [ENISA 2025 NIS Investments Report: Technology Prioritized as ...](https://complexdiscovery.com/enisa-2025-nis-investments-report-technology-prioritized-as-cyber-talent-pools-contract/) - ENISA's 2025 NIS Investments report shows EU organizations shifting cybersecurity strategies from pe...

19. [NIS Investments 2025 - ENISA - European Union](https://www.enisa.europa.eu/publications/nis-investments-2025) - ENISA: Every day we experience the Information Society. Interconnected networks touch our everyday l...

20. [Enisa NIS Investments 2025 Report | Davide Maniscalco - LinkedIn](https://www.linkedin.com/posts/davide-maniscalco_enisa-nis-investments-2025-report-activity-7404043917194792960-BIXU) - European Union Agency for Cybersecurity (ENISA) #NIS Investments 2025 — Key Takeaways on How Cyber P...

21. [2025 Verizon Data Breach Investigations Report - Keepnet Labs](https://keepnetlabs.com/blog/2025-verizon-data-breach-investigations-report) - Review the most useful findings from Verizon’s 2025 DBIR, including ransomware, exploited vulnerabil...

22. [2025 Verizon DBIR: Why Devaluing Data Stops Breaches](https://www.bluefin.com/bluefin-news/devalue-data-defeat-breach-2025-verizon-dbir/) - 2025 DBIR: Third-party risks surge. Discover how encryption and tokenization can render stolen data ...

23. [IBM's 2025 Cost of a Data Breach Report: Key Findings and ...](https://www.bluefin.com/bluefin-news/ibms-2025-data-breach-report-key-findings-and-the-years-biggest-attacks/) - IBM’s 2025 Cost of a Data Breach report highlights AI threats, shadow AI risks, and recent data brea...

24. [Average Data Breach Cost $4.44M | IBM Report Analysis - DataFence](https://www.datafence.ai/data-breach-report-2025) - Data breaches cost $4.44M globally, $10.22M in the US. Discover how shadow AI and supply chain attac...

25. [Key Insights from IBM's 2025 Cost of a Data Breach Report](https://www.allcovered.com/blog/key-insights-from-ibms-2025-cost-of-a-data-breach-report) - IBM's 2025 Cost of a Data Breach Report states global average cost has dropped, but AI adoption with...

26. [Qué es el Esquema Nacional de Seguridad (ENS) - CNI](https://ens.ccn.cni.es/es/que-es-el-ens) - El Esquema Nacional de Seguridad, de aplicación a todo el Sector Público, así como a los proveedores...

27. [Data Breach Statistics 2025–2026: Global Trends & Costs](https://deepstrike.io/blog/data-breach-statistics-2025) - Data breach statistics in 2025–2026 reveal rising attack frequency, high breach costs, and evolving ...

28. [Cost of a Data Breach 2025: IBM Global Report - Northdoor plc](https://www.northdoor.co.uk/insight/news/cost-of-a-data-breach-report-2025/) - Discover the cost of data breaches in 2025. IBM’s report reveals the $4.44M average breach cost and ...

29. [[PDF] Zero-trust architecture for secure real-time information sharing in ...](https://wjaets.com/sites/default/files/fulltext_pdf/WJAETS-2025-0640.pdf) - Abstract. Zero-trust architecture represents a transformative approach to securing defense and aeros...

30. [Implementing a Zero Trust Architecture: SP 1800-35 | CSRC](https://csrc.nist.gov/news/2025/implementing-a-zero-trust-architecture-sp-1800-35) - This publication outlines results and best practices from the NCCoE effort featuring work with 24 ve...

31. [Reimagining Integrity: Why the CIA Triad Falls Short](https://securityboulevard.com/2025/06/reimagining-integrity-why-the-cia-triad-falls-short/) - For decades, the CIA Triad of Confidentiality, Integrity, and Availability has been the bedrock fram...

32. [[PDF] Part-145 – ISMS Process Review Document – PART IS | SasSofia](https://sassofia.com/wp-content/uploads/2025/06/Part-145-ISMS-Process-Review-Document-PART-IS-1.pdf) - Continuously Improve Security Measures through incident learning, audits, and performance reviews. 1...

33. [IA, NIS2 y DORA en 2025: hoja de ruta clave | 4DLegal](https://4dlegal.es/cumplimiento-ai-act-nis2-dora/) - Cómo prepararse en 2025 para cumplir con AI Act, NIS2 y DORA: riesgos, obligaciones y roadmap integr...

34. [[PDF] DORA Requirements - ASEPEC](https://www.asepec.es/wp-content/uploads/2025/08/White-paper-DORA-5.8.2025.pdf) - (c) provisions on availability, authenticity, integrity and confidentiality in relation to the prote...

35. [A humble proposal: The InfoSec CIA triad should be expanded](https://www.helpnetsecurity.com/2025/01/16/infosec-cia-triad/) - As such, I propose that use term “the CIANA pentad”, covering: “Confidentiality”, “Integrity”, “Avai...

36. [MITRE Posts Results of 2025 ATT&CK Enterprise Evaluations](https://radar.offseq.com/threat/mitre-posts-results-of-2025-attck-enterprise-evalu-0eb3a600) - Several vendors reported achieving 100% detection and coverage rates, indicating significant improve...

37. [2025 MITRE ATT&CK®: CrowdStrike Delivers 100% Results](https://www.crowdstrike.com/en-us/resources/reports/2025-mitre-results/) - Insider Risk Services Identify, contain, and prevent insider threats with advanced intelligence and ...

38. [[PDF] Cybersecurity and Artificial Intelligence: Triad-Based Analysis ...](https://cit.iict.bas.bg/CIT-2025/v-25-3/10341-Volume25_Issue_3-10_paper.pdf)

39. [The Double-Edged Sword of AI in Cybersecurity - Scirp.org.](https://www.scirp.org/journal/paperinformation?paperid=147064) - AI-driven tools are seen to strengthened cybersecurity defenses through various ways such as anomaly...

40. [Data Breach Statistics & Trends [updated 2025] - Varonis](https://www.varonis.com/blog/data-breach-statistics) - In 2025, the United States is the country with the highest average breach cost at $10.22 million, fo...

41. [Understanding SOC 2 Availability, Uptime & DR | ISMS.online](https://www.isms.online/soc-2/availability/) - Explore how SOC 2 defines availability through uptime, DR, and SLAs—ensuring continuous operations a...

42. [SQL disaster recovery best practices: Ultimate Guide 2025](https://www.ainfosys.com/tutorials/sql-disaster-recovery-best-practices/) - Three critical metrics form the basis of any DR plan: RPO, RTO, and SLA. They determine how much dat...

43. [RTO vs RPO: Essential Business Continuity Metrics for 2025](https://www.trustcloud.ai/risk-management/mastering-rto-and-rpo-for-bulletproof-business-continuity/) - When these concepts are put side by side, RTO and RPO serve as crucial indicators that help organiza...

44. [El Esquema Nacional de Seguridad (ENS): Un marco esencial para ...](https://s2grupo.es/el-esquema-nacional-de-seguridad-ens/) - El ENS establece tres niveles de seguridad según el tipo de información manejada y el impacto de un ...

45. [20 Cybersecurity Metrics & KPIs to Track in 2025 - SecurityScorecard](https://securityscorecard.com/resources/learning-center/9-cybersecurity-metrics-kpis-to-track/) - Explore the top cybersecurity metrics for 2025. Learn how to measure risk, performance, and vendor e...

46. [Key metrics for measuring cybersecurity in your company - Logalty](https://www.logalty.com/en/blog/2025/11/27/key-metrics-measuring-company-cybersecurity/) - The MTTD (Mean Time To Detect) measures how long it takes the company to detect a threat. The MTTR (...

47. [30 Cybersecurity Metrics & KPIs Every Company Must Track in 2025](https://securityboulevard.com/2025/05/30-cybersecurity-metrics-kpis-every-company-must-track-in-2025/) - This blog outlines 30 cybersecurity metrics that provide strategic insights into risk exposure, oper...

48. [[PDF] Spain - 2025 Cisco Cybersecurity Readiness Index](https://newsroom.cisco.com/c/dam/r/newsroom/en/us/interactive/cybersecurity-readiness-index/2025/documents/2025_Cisco_Cybersecurity_Readiness_Index_ES.pdf) - The 2025 edition of this study shows that readiness remained flat from 2024. Based on five pillars o...

49. [Cybersecurity in critical infrastructure and national resilience - Sener](https://www.group.sener/en/insights/cybersecurity-in-critical-infrastructure-and-national-resilience/) - Spain recognises the following as critical sectors: Public administration and government; Space infr...

50. [FSB recommends Spain further enhance cyber resilience of its ...](https://www.fsb.org/2025/11/fsb-recommends-spain-further-enhance-cyber-resilience-of-its-financial-sector-to-address-rising-challenges/) - FSB recommends Spain further enhance cyber resilience of its financial sector to address rising chal...

51. [Understanding of the CIA Triad, Non-Repudiation, and Authenticity](https://www.stratosally.com/defensive-security/cia-triad-7581) - In the subject of information security, the CIA Triad provides a key paradigm for developing and ass...

52. [CIA Triad, CIANA, and STRIDE: Foundations of Cybersecurity and ...](https://codebaseit.com/cia-triad-ciana-and-stride-foundations-of-cybersecurity-and-threat-modeling/) - This article delves into the CIA Triad, explores its extended form as CIANA, and connects these prin...

53. [Quantum Computing is a Long-Term Cybersecurity Risk, But ...](https://thequantuminsider.com/2025/02/01/quantum-computing-is-a-long-term-cybersecurity-risk-but-deserves-immediate-attention-analysts-report/) - MITRE report warns that the U.S. must act now to secure sensitive data against future quantum decryp...

54. [Quantum Computing Threats to Cryptography - Sciety](https://sciety.org/articles/activity/10.21203/rs.3.rs-6795420/v1) - Background The emergence of quantum computing poses unprecedented threats to current cryptographic s...

55. [PART 5 Impact of Quantum Computing on the CIA Triad: Quantum computing… | Tomikia B. Sylvester](https://www.linkedin.com/posts/tomikia-b-sylvester_part-5-impact-of-quantum-computing-on-the-activity-7247902229838331904-k1wq) - PART 5 Impact of Quantum Computing on the CIA Triad: Quantum computing will have a profound impact o...

56. [🔐 Quantum Computing vs. the CIA Triad: Are Our Security Foundations at… | Kris Boehm, CISSP](https://www.linkedin.com/posts/krisboehm_quantum-computing-vs-the-cia-triad-are-activity-7313553364112273410-FK4O) - 🔐 Quantum Computing vs. the CIA Triad: Are Our Security Foundations at Risk? As quantum computing be...

57. [Post-Quantum Cryptography | CSRC](https://csrc.nist.gov/projects/post-quantum-cryptography) - Short URL: https://www.nist.gov/pqcrypto For a plain-language introduction to post-quantum cryptogra...

58. [NIST Releases First 3 Finalized Post-Quantum Encryption Standards](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards) - NIST is encouraging computer system administrators to begin transitioning to the new standards as so...

59. [A Complete Guide to Post-Quantum Cryptography Standards](https://www.paloaltonetworks.com/cyberpedia/pqc-standards) - PQC standards define approved post-quantum algorithms, how to implement them, and the requirements f...

60. [Cyber Insights 2025: Quantum and the Threat to Encryption](https://www.securityweek.com/cyber-insights-2025-quantum-and-the-threat-to-encryption/) - 2025 is an important year – it is probably our last chance to start our migration to post quantum cr...

61. [Esquema Nacional de Seguridad (ENS) - Garante Privacy](https://garanteprivacy.es/esquema-nacional-de-seguridad/) - El ENS establece una serie de principios, políticas, normas y medidas de seguridad que las organizac...

62. [Guía CCN-STIC-817: Ciberincidentes | PDF | La seguridad informática](https://es.scribd.com/document/453682178/CCN-STIC-817-Gestion-de-Ciberincidentes-ENS) - Este documento proporciona orientación sobre la gestión de ciberincidentes de acuerdo con el Esquema...

63. [NIS2 Spain Transposition: Status, Requirements, and Roadmap](https://copla.com/blog/compliance-regulations/nis2-directive-regulations-and-implementation-in-spain/) - Deadline for Member States to transpose NIS2 into national law. Spanish Draft Approval, 14 January 2...

64. [The NIS2 Directive will transform cybersecurity in Spain - PKF Attest](https://www.pkf-attest.es/en/noticias/la-directiva-que-cambiara-la-ciberseguridad-empresarial-en-espana/) - The NIS2 Directive is the new European regulation that seeks to strengthen cybersecurity in all Memb...

65. [2025 State of Cyber Risk Management Report - The FAIR Institute](https://www.fairinstitute.org/state-of-crm-2025) - The 2025 State of Cyber Risk Management Report examines how leading organizations are adapting their...

66. [[PDF] 2025 State of Cyber Risk Management - The FAIR Institute](https://www.fairinstitute.org/hubfs/State%20of%20Cyber%20Risk%20Management/FAIRInstitute_2025StateOfCyberRiskManagement%20Report_June2025.pdf) - The 2025 State of Cyber Risk Management Report examines how leading organizations are adapting their...

67. [Informe Global de Riesgos Cibernéticos 2025 - Aon](https://www.aon.com/cyber-risk-report/es-la) - Las organizaciones clientes de Aon registraron una mejora interanual del 5% en la implementación de ...

68. [Global 2025 Cyber Risk Report - Aon](https://www.aon.com/cyber-risk-report/es-es) - Las organizaciones clientes de Aon demostraron una mejora interanual del 5 % en los controles crític...

69. [Aprovechando la ola: EMEA se acerca a la madurez cibernética. - Aon](https://www.aon.com/cyber-risk-report/es-es/riding-the-wave-emea-approaches-cyber-maturity) - Los controles técnicos se refuerzan, pero aumenta el riesgo de terceros · Los seguros ciber y las re...

70. [[PDF] Verizon's 2025 Data Breach Investigations Report](https://completecompli.com/wp-content/uploads/2025/06/6-9-25-CCI-IT-Update-Verizon-Report.pdf)

