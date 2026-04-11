
# Informe Zero-Trust.

En España —y en el mundo—, el modelo Zero Trust ha dejado de ser un “bonito cuento de arquitectura” para convertirse en el nuevo estándar de referencia para indicadores de ciberseguridad, resiliencia digital y continuidad de negocio. A partir de 2025, el foco no está solo en *tener* cinturones Zero Trust, sino en *medir*, con crudeza numérica, cuánto reducen las brechas, cuánto acortan los tiempos de respuesta y cuánto blindan la economía digital a escala nacional.

A continuación despliega el “Informe‑Orquestador” de un consorcio de CISOs de élite, criptógrafos cuánticos y arquitectos Zero Trust, con métricas de alto impacto, aplicables a nivel territorial español y comparables con marcos globales (NIST, CISA, UE‑NIS2, DoD, etc.).

***

### 1. De qué hablamos cuando hablamos de Zero Trust

El modelo Zero Trust, según NIST SP 800‑207, no es una tecnología, sino un paradigma de diseño:

- **Ninguna entidad (usuario, dispositivo, aplicación, flujo de datos) es de confianza por defecto.**
- **Cada acceso es una decisión individual, continua y dinámica**, basada en identidad, contexto y riesgo.[^1]
- **El perímetro ya no es la frontera; el recurso y la identidad lo son.**[^1]

En España, esto se encaja con el Esquema Nacional de Seguridad (ENS), la NIS2, la Directiva DORA y la Agenda España Digital 2025, que exigen un control de riesgo fino sobre activos críticos y servicios públicos.[^2][^3][^4]

***

### 2. Indicadores globales de madurez Zero Trust (2025–2026)

Desde 2025, los organismos y centros de investigación hablan de *KPIs de arquitectura* más que de “parches de seguridad”. Algunos indicadores clave:

#### 2.1. Adopción y madurez

- **Porcentaje de organizaciones con Zero Trust parcial o total:**
    - Encuestas globales (StrongDM 2025, Tailscale, Okta) señalan que alrededor del 80–85% de las empresas ya tienen Zero Trust en fase de despliegue o consolidado.[^5][^6]
- **Madurez por modelo CISA (ZTMM v2):**
    - CISA propone cuatro niveles: *Traditional → Initial → Advanced → Optimal*, medidos sobre cinco pilares: Identidad, Dispositivos, Red, Aplicaciones y Datos, más visibilidad y automatización.[^7][^8]

Métrica de alto nivel:

- **% de entidades públicas/empresas críticas en España en ZTMM ≥ “Advanced” (NIS2 / DORA)**
    - Comparado con UE: Francia, Países Bajos o Alemania ya miden progresos en ZTMM como indicador de cumplimiento.[^9]


#### 2.2. Eficiencia operativa y resiliencia

- **MTTD (tiempo medio de detección) y MTTR (tiempo medio de respuesta):**
    - Organizaciones con granularidad Zero Trust y SIEM‑SOAR‑UEBA reducen MTTD de 200+ días a unas pocas decenas, y MTTR a horas o menos.[^10][^11]
- **Reducción de brechas e impacto:**
    - En ambientes maduros se observan caídas de:
        - alrededor del 40–70% en incidentes por phishing y credenciales comprometidas;
        - 50–60% en ransomware y exfiltración de datos.[^12][^10]

Ejemplo de métrica territorial:

- **Ratio de incidentes críticos por millón de habitantes (ES vs. UE‑27), corregido por nivel de ZTMM en sector público.**

***

### 3. Métricas específicas del marco Zero Trust (pilares)

Bajo NIST, CISA y marcos de madurez europeos, se articulan cinco pilares con sus indicadores. Aquí van ellos, ya traducidos a lógica de “indicador nacional” para España.

#### 3.1. Pilar: Identidad y acceso

**Indicadores de identidad Zero Trust (NIST + CISA):**

- **% de usuarios con acceso JIT (Just‑In‑Time) y MFA obligatorio en sistemas críticos.**
- **Ratio de cuentas con privilegios mínimos frente a cuentas con privilegios elevados:** conviene que el 80–90% de las cuentas privilegiadas estén en régimen de “principio del mínimo privilegio”.[^13][^14]
- **Número de accesos bloqueados por políticas dinámicas de riesgo (behaviour‑based risk policies).**

**Comparativa España vs. mundo:**

- En España, el uso de MFA y IAM avanzado crece, pero aún está por debajo de media UE en el tejido PYME, según estudios de tendencias 2025.[^3][^12]
- A nivel nacional, un buen indicador sería:
    - **% de entidades críticas (NIS2) que miden el riesgo de acceso por sesión (no solo por login).**


#### 3.2. Pilar: Dispositivos y endpoints

**Métricas de seguridad orientadas a dispositivos:**

- **% de dispositivos gestionados (corporativos + BYOD) con políticas de postura de seguridad aplicadas (OS parcheado, EDR, cifrado, etc.).**
- **Media de dispositivos no gestionados por cada 1.000 usuarios en el sector público.**
- **Tiempo medio entre la detección de una vulnerabilidad crítica y su parcheo en dispositivos críticos.**

Zero‑Trust en el ecosistema OT (infraestructuras críticas) implica:

- **Número de zonas de seguridad microsegmentadas por planta / centro de datos.**
- **% de accesos a OT que pasan por gateways de validación continua (no solo firewall).**[^15][^16]


#### 3.3. Pilar: Red y microsegmentación

En un país donde la digitalización de empresas aún rezaga frente a infraestructura, la red es un campo fértil de métricas:

- **% de tráfico de red inspeccionado en profundidad (capa 7) y cifrado de extremo a extremo.**
- **Número medio de segmentos de red por unidad de negocio (microsegmentación).**
- **Movimiento lateral medio tras una brecha:** si es bajo, indica que la microsegmentación funciona.[^11][^14]

Desde 2025, la **Zero Trust Network Access (ZTNA)** se mide también por:

- **% de accesos remotos a aplicaciones críticas que pasan por ZTNA, no por VPN clásica.**
- ZTNA es uno de los segmentos de mercado que más crece (decenas de miles de millones de dólares), lo que evidencia su adopción como métrica de red segura.[^17][^18]


#### 3.4. Pilar: Aplicaciones y cargas de trabajo

Aquí se cruza cloud, DevSecOps y resiliencia digital:

- **% de aplicaciones nuevas diseñadas “Zero‑Trust‑by‑design” (controles de acceso por API, políticas de autorización por recurso, etc.).**
- **MTTR de contención de un incidente en la nube tras una alerta de Zero Trust.**
- **Número de accesos no autorizados bloqueados en API y servicios en la nube.**

Para España, donde la migración a la nube avanza, un indicador de nivel nacional puede ser:

- **Índice de adopción de Zero Trust en aplicaciones de administración electrónica (e‑Gobierno, ayuntamientos, servicios públicos online).**[^4][^2]


#### 3.5. Pilar: Datos y protección de la información

- **% de datos sensibles (PII, datos críticos de infraestructura) que se clasifican y se aplican políticas de acceso basadas en contexto.**
- **Número de intentos de acceso a datos sensibles bloqueados por políticas de mínimo privilegio.**
- **% de exfiltraciones de datos críticos que se evitan gracias a controles de movimiento de datos (DLP) y políticas de acceso.**[^19][^10]

A nivel nacional, este indicador puede calibrarse con estudios de confianza digital y ciberseguridad en España, que ya miden percepción de riesgo pero aún no unifican métricas totalmente cuantitativas.[^19]

***

### 4. Indicadores de ciber‑resiliencia y continuidad de negocio

Zero Trust no solo reduce incidentes; cambia la capacidad de recuperación. Métricas clave:

- **Tiempo medio de restauración de servicios críticos tras incidente (RTO real vs. RTO planeado).**
- **% de procesos críticos con microsegmentación y políticas de acceso que permiten aislamiento rápido.**
- **Reducción de impacto económico medio por incidente (coste de incidente por millón de euros de PIB, corregido por sector).**[^20][^10]

En España, el marco de **Resiliencia Digital** y la **evolución del Ciberseguro** incorporan, desde 2025, indicadores de Zero Trust como variable de riesgo actuarial:

- Que una empresa tenga pilar de identidad en ZTMM ≥ Advanced puede reducir su prima de ciberseguro en un 15–30%, según modelos de riesgo de seguros europeos.[^20]

***

### 5. Comparativa España‑UE‑EE.UU.: algunos ejes de indicadores

Para construir un marco nacional territorial, España puede adoptar o adaptar indicadores paralelos a los de otros países:


| Eje de indicador | España (ejemplo de objetivo) | UE promedio (línea de referencia) | EE.UU. / CISA (referencia global) |
| :-- | :-- | :-- | :-- |
| % de entidades críticas con ZTMM ≥ Advanced | ≥ 60% en 2027 [^7] | ≈ 50–70% según país [^9] | ≥ 70% en agencias federales [^8] |
| % de accesos remotos a apps críticas vía ZTNA | ≥ 50% en 2025 [^18] | ≈ 40–60% en 2025 | > 60% en empresas grandes [^17] |
| MTTD en ambientes Zero Trust | < 60 días | < 50–70 días | < 40 días en entornos avanzados [^10] |
| % de PYMEs críticas con IAM + MFA | ≥ 40% en 2025 [^3] | ≈ 30–50% según estado miembro | ≈ 60% en sector crítico [^21] |

Estos valores pueden ajustarse con datos de INCIBE, ENISA y el Informe de la UE sobre estrategias de ciberseguridad nacional, que ya proponen marcos de evaluación basados en KPIs.[^22][^23]

***

### 6. Propuestas de indicadores “ad hoc” para encuestas / marcos nacionales

Si preparas un cuestionario nacional (por ejemplo, dirigido a CISOs de grandes organizaciones, operadores críticos o ayuntamientos), puedes usar estos ítems como métricas de Zero Trust:

1. **Madurez de identidad (NIST / CISA):**
    - **Ratio de usuarios con MFA en sistemas críticos (0–100%).**
    - **% de accesos sesionales con evaluación de riesgo dinámica (SIEM / UEBA / IAM).**
    - **Número de accesos JIT por rol privilegiado al mes.**
2. **Dispositivos Zero Trust:**
    - **% de dispositivos con políticas de postura de seguridad aplicadas.**
    - **Tiempo medio de parcheo de vulnerabilidades críticas (días).**
    - **Número de dispositivos no gestionados por cada 1.000 usuarios.**
3. **Red y microsegmentación:**
    - **% de tráfico inspeccionado en capa 7 y cifrado extremo‑a‑extremo.**
    - **Número de segmentos de red por unidad crítica (ej.: centro de datos, planta industrial).**
    - **Proporción de accesos remotos vía ZTNA vs. VPN clásica.**
4. **Aplicaciones y datos:**
    - **% de datos sensibles con políticas de acceso contextual.**
    - **Número de accesos no autorizados bloqueados en la última semana.**
    - **% de aplicaciones nuevas “Zero‑Trust‑by‑design” sobre el total de aplicaciones puestas en producción.**
5. **Resiliencia y riesgo actuarial:**
    - **MTTR de servicios críticos tras incidente (horas).**
    - **Reducción de impacto económico por incidente vs. año anterior (%).**
    - **Índice de percepción de ciberseguridad Zero Trust en ciudadanos y empresas (Eurobarómetro / paneles nacionales).**[^4][^19]

***

### 7. Espíritu irónico y constructivo: cómo usar este marco

Imagina que el “parable” de Zero Trust es un árbitro de fútbol que nunca da por buenas las tarjetas amarillas, sino que revisa cada jugada con VAR, algoritmos de riesgo y consultas constantes con el VAR‑central (SIEM / UEBA). En España, el reto no es “poner árbitros”, sino **medir si el VAR está conectado a todos los estadios y si el sistema avisa antes del gol rival**.

Ahora, te propongo:

- Empezar por un **“índice de madurez Zero Trust nacional”** que combine los cinco pilares.
- Publicarlo como KPI territorial comparable con la UE, para que no solo cuenten los ataques, sino la capacidad de no confiar nunca, siempre verificar.


<span style="display:none">[^24][^25][^26][^27][^28][^29][^30][^31][^32][^33][^34][^35][^36][^37][^38][^39][^40][^41][^42][^43][^44][^45][^46][^47][^48][^49][^50][^51][^52][^53]</span>

<div align="center">⁂</div>

[^1]: https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-207.pdf

[^2]: https://portal.mineco.gob.es/RecursosArticulo/mineco/ministerio/ficheros/210204_Digital_Spain_2025.pdf

[^3]: https://itcs.vip/en/tendencias-ciberseguridad-espana-2025/

[^4]: https://digital-strategy.ec.europa.eu/en/factpages/spain-2025-digital-decade-country-report

[^5]: https://tailscale.com/resources/report/zero-trust-report-2025

[^6]: https://openstore.com/the-state-of-zero-trust-in-2025-progress-gaps-and-the-road-ahead/

[^7]: https://www.libertify.com/interactive-library/zero-trust-architecture-guide-2025/

[^8]: https://www.cisco.com/c/en/us/products/collateral/security/zero-trust-cisa-dod-nist-sb.html

[^9]: https://www.kiteworks.com/cybersecurity-risk-management/zero-trust-framework-for-nis2-compliance/

[^10]: https://zerothreat.ai/blog/zero-trust-statistics

[^11]: https://seraphicsecurity.com/learn/zero-trust/zero-trust-architecture-in-2025-7-key-components/

[^12]: https://www.qualoom.es/zero-trust-en-2026-roadmap-y-componentes-fundamentales/

[^13]: https://www.3digits.es/blog/zero-trust.html

[^14]: https://www.qualoom.es/implementacion-efectiva-del-modelo-zero-trust-en-entornos-corporativos-hibridos/

[^15]: https://s2grupo.es/zero-trust-en-entornos-ot-es-posible/

[^16]: https://www.knowmadmood.com/es/blog/zero-trust-ciberseguridad-ot-infraestructuras-criticas

[^17]: https://technologyradius.com/research-analysis/zero-trust-security-adoption-trends-2025

[^18]: https://uk.finance.yahoo.com/news/zero-trust-network-access-ztna-081000867.html

[^19]: https://www.observaciber.es/sites/observaciber/files/media/documents/indicadoresconfianzadigitalyciberseguridadespañayue_octubre2021.pdf

[^20]: https://blog.cyberadvisors.com/zero-trust-framework-trends-for-2025

[^21]: https://electroiq.com/stats/zero-trust-security-statistics/

[^22]: https://www.incibe.es/incibe-cert/blog/metodologia-zero-trust-fundamentos-y-beneficios

[^23]: https://www.enisa.europa.eu/sites/default/files/publications/An evaluation framework for cyber security strategies.pdf

[^24]: https://www.cisco.com/c/es_mx/support/docs/security-vpn/security-vpn/218443-verify-zero-trust-security-whitepaper.pdf

[^25]: https://www.ibm.com/es-es/think/topics/zero-trust

[^26]: https://www.sealpath.com/es/blog/modelo-zero-trust-ciberseguridad/

[^27]: https://revistabyte.es/actualidad-it/modelo-zero-trust-ciberseguridad/

[^28]: https://www.paloaltonetworks.es/zero-trust

[^29]: https://www.checkpoint.com/es/cyber-hub/network-security/what-is-zero-trust/5-core-principles-of-zero-trust-security/

[^30]: https://www.siliconweek.com/security/zero-trust-de-la-gestion-de-riesgos-a-la-resiliencia-en-ciberseguridad-111274

[^31]: https://www.microsoft.com/es-es/security/business/security-101/what-is-zero-trust-architecture

[^32]: https://www.splashtop.com/es/blog/zero-trust-security-a-comprehensive-approach-to-cybersecurity

[^33]: https://learn.microsoft.com/es-es/security/zero-trust/zero-trust-overview

[^34]: https://www.paloaltonetworks.es/cyberpedia/what-is-a-zero-trust-architecture

[^35]: https://www.zscaler.com/es/resources/security-terms-glossary/what-is-zero-trust

[^36]: https://planciber.com/zero-trust-architecture-guia-implementacion-pymes/

[^37]: https://www.keypasco.com/en/what-is-zero-trust-architecture-why-every-business-needs-a-zero-trust-strategy-in-2025/

[^38]: https://www.teamvienna.at/blog/the-rise-of-zero-trust-security-in-2025-trends-and-best-practices

[^39]: https://www.trustbuilder.com/en/top-5-zero-trust-cybersecurity-key-takeaways-for-2024-2025/

[^40]: https://cibersafety.com/zero-trust-2025-implementacion/

[^41]: https://www.linkedin.com/pulse/zero-trust-2025-hype-over-just-getting-smarter-tuhin-banerjee-ehmlc

[^42]: https://www.linkedin.com/pulse/zero-trust-architecture-why-matters-2025-vigilantasia-kw0jc

[^43]: https://www.dsn.gob.es/sites/default/files/2025-12/National Aeroespace Security Strategy 2025 - Accesible_0.pdf

[^44]: https://overtel.com/blog-3/zero-trust-la-clave-para-la-ciberseguridad-en-2025

[^45]: https://www.exteriores.gob.es/es/PoliticaExterior/Documents/EAE_2025-2028/Estrategia%20Acci%C3%B3n%20Exterior%20Ingl%C3%A9s.pdf

[^46]: https://es.linkedin.com/pulse/zero-trust-el-nuevo-estándar-de-seguridad-empresarial-para-2025-i0jof

[^47]: https://www.innovaciondigital360.com/cyber-security/enfoque-de-confianza-cero-para-garantizar-la-ciberseguridad-como-hacerlo/

[^48]: https://aslan.es/especial-tendencias-en-zero-trust-un-reto-en-constante-evolucion-2025/

[^49]: https://avance.digital.gob.es/es-es/Documents/Spain-Strategic-Roadmap.pdf

[^50]: https://itcs.vip/en/blog/tendencias-ciberseguridad-espana-2025

[^51]: https://www.goodaccess.com/blog/nis2-require-zero-trust-essential-security-measure

[^52]: https://www.linkedin.com/top-content/networking/cybersecurity-best-practices/implementing-zero-trust-for-eu-cybersecurity-compliance/

[^53]: http://espanadigital.gob.es/sites/espanadigital/files/2025-12/Informe de país 2025 - España.PDF

