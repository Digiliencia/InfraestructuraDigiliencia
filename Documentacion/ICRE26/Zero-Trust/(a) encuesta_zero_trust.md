# Encuesta Integral de Madurez Zero Trust

## 1. Datos generales de la organización

1.1. Tipo de organización  
- [ ] Administración pública estatal  
- [ ] Administración autonómica  
- [ ] Administración local  
- [ ] Operador de servicios esenciales / NIS2  
- [ ] Empresa privada – gran empresa (>250 empleados)  
- [ ] Empresa privada – mediana empresa (50–249 empleados)  
- [ ] Empresa privada – pequeña empresa (<50 empleados)  
- [ ] Entidad del tercer sector / ONG  
- [ ] Otro (especificar): ___________  

1.2. Sector principal de actividad  
- [ ] Energía / Utilities / Infraestructuras críticas  
- [ ] Finanzas / Seguros  
- [ ] Sanidad / Servicios sociales  
- [ ] Industria / Manufactura / OT  
- [ ] TIC / Telecomunicaciones  
- [ ] Educación / Investigación  
- [ ] Administración pública general  
- [ ] Transporte / Logística  
- [ ] Comercio / Servicios  
- [ ] Otros (especificar): ___________  

1.3. Tamaño aproximado de la organización (personas)  
- [ ] < 50  
- [ ] 50–249  
- [ ] 250–999  
- [ ] 1.000–4.999  
- [ ] ≥ 5.000  

1.4. Rol de la persona que responde  
- [ ] CISO / Responsable de Seguridad de la Información  
- [ ] CIO / CTO / Responsable de Tecnología  
- [ ] DPO / Delegado de Protección de Datos  
- [ ] Responsable de Continuidad de Negocio / Riesgos  
- [ ] Responsable de Operaciones / OT  
- [ ] Alta Dirección (CEO / DG / Consejo)  
- [ ] Otro (especificar): ___________  

---

## 2. Visión estratégica y marco Zero Trust

2.1. ¿En qué grado está formalmente adoptado el modelo Zero Trust en su organización?  
- [ ] No se ha considerado seriamente; seguimos confiando en el “castillo y el foso”.  
- [ ] Se ha discutido a alto nivel, pero sin plan formal.  
- [ ] Existe una hoja de ruta inicial aprobada.  
- [ ] Zero Trust está integrado en los planes estratégicos de seguridad.  
- [ ] Zero Trust es el principio rector de diseño de seguridad en toda la organización.  

2.2. ¿Dispone su organización de una estrategia o política específica de Zero Trust documentada y aprobada?  
- [ ] No existe.  
- [ ] Borrador en elaboración.  
- [ ] Aprobada parcialmente para algunas áreas (TI / nube / identidades).  
- [ ] Aprobada y comunicada para toda la organización.  
- [ ] Aprobada, comunicada y revisada al menos anualmente.  

2.3. ¿En qué medida Zero Trust se alinea con el marco normativo aplicable (ENS, NIS2, DORA, RGPD, etc.)?  
- [ ] No se ha realizado análisis de alineamiento.  
- [ ] Análisis preliminar sin acciones definidas.  
- [ ] Alineamiento básico con requisitos mínimos de cumplimiento.  
- [ ] Alineamiento sistemático con NIS2/ENS/DORA en proyectos críticos.  
- [ ] Alineamiento integral con seguimiento de indicadores y auditorías periódicas.  

2.4. ¿Qué nivel de patrocinio tiene Zero Trust por parte de la Alta Dirección?  
- [ ] Nulo: es un término que solo suena en presentaciones técnicas.  
- [ ] Limitado: se menciona, pero sin presupuesto asociado.  
- [ ] Moderado: existen proyectos concretos vinculados a Zero Trust.  
- [ ] Elevado: la Dirección lo exige explícitamente en decisiones de inversión.  
- [ ] Total: Zero Trust es un requisito transversal en toda decisión estratégica.  

---

## 3. Identidad y acceso (Pilar 1)

3.1. Porcentaje aproximado de usuarios con MFA (autenticación multifactor) habilitado en sistemas críticos  
- [ ] 0–20 %  
- [ ] 21–50 %  
- [ ] 51–80 %  
- [ ] 81–95 %  
- [ ] 96–100 %  

3.2. ¿Qué modelo de gestión de identidades utilizan principalmente?  
- [ ] Cuentas locales y directorios aislados, todo muy “artesanal”.  
- [ ] Directorio centralizado (ej.: AD/LDAP) sin federación.  
- [ ] IAM corporativo con federación (SSO, SAML, OIDC).  
- [ ] Plataforma avanzada de identidad con MFA, SSO y políticas contextuales.  
- [ ] Modelo de identidad unificado para usuarios, dispositivos, servicios y APIs.  

3.3. ¿Aplica su organización el principio de mínimo privilegio de forma sistemática?  
- [ ] No, los permisos se asignan “por costumbre” o antigüedad.  
- [ ] Parcialmente, en sistemas más críticos.  
- [ ] De forma planificada, con revisiones periódicas de permisos.  
- [ ] De forma automatizada, con roles y flujos de aprobación.  
- [ ] De forma dinámica, ajustando permisos en función del riesgo y contexto.  

3.4. ¿Cómo se gestionan las cuentas privilegiadas (administradores, cuentas de servicio, etc.)?  
- [ ] No existe distinción clara; todas las cuentas son más o menos “VIP”.  
- [ ] Listados manuales y controles básicos.  
- [ ] Uso de un sistema PAM para los sistemas más críticos.  
- [ ] Uso de PAM para todas las cuentas privilegiadas, con sesiones auditadas.  
- [ ] Gestión avanzada con acceso just-in-time y revisión continua de uso.  

3.5. ¿Se monitorizan los accesos de alto riesgo mediante analítica de comportamiento (UEBA u otros sistemas)?  
- [ ] No, confiamos en que “todo va bien hasta que no”.  
- [ ] Sí, pero de forma manual y reactiva.  
- [ ] Sí, con reglas básicas de correlación.  
- [ ] Sí, con modelos de riesgo y alertas automáticas.  
- [ ] Sí, con modelos avanzados y respuesta semiautomatizada.  

---

## 4. Dispositivos y endpoints (Pilar 2)

4.1. Porcentaje de dispositivos corporativos gestionados (inventariados y con políticas aplicadas)  
- [ ] 0–40 %  
- [ ] 41–70 %  
- [ ] 71–90 %  
- [ ] 91–99 %  
- [ ] 100 % (al menos sobre el papel y en los informes).  

4.2. ¿Qué grado de cobertura de EDR/XDR tiene la organización en sus endpoints?  
- [ ] Prácticamente nulo.  
- [ ] Piloto en algunas unidades.  
- [ ] Cobertura moderada (50–80 % de dispositivos).  
- [ ] Cobertura amplia (>80 % de dispositivos).  
- [ ] Cobertura casi total, incluyendo servidores, estaciones y dispositivos remotos.  

4.3. ¿Cómo se gestionan los dispositivos no gestionados (BYOD, contratistas, terceros)?  
- [ ] No se discriminan de los dispositivos corporativos.  
- [ ] Se limita su acceso a unas pocas aplicaciones.  
- [ ] Acceso segmentado mediante soluciones MDM/MAM.  
- [ ] Acceso estrictamente controlado por ZTNA y políticas de postura.  
- [ ] Acceso condicionado por riesgo, posture check y autorización dinámica.  

4.4. Tiempo medio para parchear vulnerabilidades críticas en dispositivos clave  
- [ ] Más de 60 días  
- [ ] 31–60 días  
- [ ] 16–30 días  
- [ ] 8–15 días  
- [ ] ≤ 7 días (o incluso antes de que los atacantes lo sepan).  

4.5. ¿Existe política formal de cifrado de disco y protección de datos en dispositivos?  
- [ ] No.  
- [ ] Sí, pero solo en portátiles.  
- [ ] Sí, en portátiles y dispositivos móviles.  
- [ ] Sí, en todos los dispositivos, incluidos servidores.  
- [ ] Sí, con verificación periódica de cumplimiento.  

---

## 5. Red, ZTNA y microsegmentación (Pilar 3)

5.1. ¿Qué porcentaje aproximado del tráfico de red interno es inspeccionado a nivel de aplicación (capa 7)?  
- [ ] 0–20 %  
- [ ] 21–50 %  
- [ ] 51–80 %  
- [ ] 81–95 %  
- [ ] 96–100 % (nada se escapa, salvo quizá los suspiros de la red).  

5.2. ¿Hasta qué punto la organización ha sustituido VPN tradicionales por Zero Trust Network Access (ZTNA)?  
- [ ] 0 % (VPN forever).  
- [ ] Pilotos de ZTNA en curso.  
- [ ] ZTNA para algunos colectivos (proveedores, teletrabajo).  
- [ ] ZTNA como canal principal, VPN residual.  
- [ ] ZTNA como estándar; VPN considerada especie en extinción.  

5.3. Microsegmentación de red  
- [ ] Red plana, un único gran “patio de recreo”.  
- [ ] Segmentación básica por VLAN.  
- [ ] Segmentación por zonas (TI, OT, DMZ, etc.).  
- [ ] Microsegmentación por aplicaciones y servicios.  
- [ ] Microsegmentación dinámica basada en identidad y contexto.  

5.4. ¿Cómo se controlan los movimientos laterales tras una posible intrusión?  
- [ ] No se contempla de forma específica.  
- [ ] Reglas estáticas en firewall.  
- [ ] Políticas de segmentación basadas en roles.  
- [ ] Políticas dinámicas con controles de acceso por flujo.  
- [ ] Uso de herramientas específicas de detección de movimiento lateral y bloqueo automático.  

5.5. Porcentaje de comunicaciones cifradas extremo a extremo en servicios críticos  
- [ ] 0–40 %  
- [ ] 41–70 %  
- [ ] 71–90 %  
- [ ] 91–99 %  
- [ ] 100 % (el texto en claro solo se permite en la poesía interna).  

---

## 6. Aplicaciones, nube y cargas de trabajo (Pilar 4)

6.1. % de nuevas aplicaciones que se diseñan con principios Zero Trust (autenticación fuerte, autorización por recurso, logging exhaustivo)  
- [ ] 0–20 %  
- [ ] 21–50 %  
- [ ] 51–80 %  
- [ ] 81–95 %  
- [ ] 96–100 %  

6.2. ¿Cómo se gestionan las identidades de aplicaciones y servicios (service accounts, API keys, etc.)?  
- [ ] Cada equipo “hace lo que puede”.  
- [ ] Inventario básico y contraseñas compartidas.  
- [ ] Vault centralizado para secretos críticos.  
- [ ] Vault + rotación automática de secretos.  
- [ ] Gestión integral con identidades federadas para servicios y APIs.  

6.3. ¿Dispone su organización de un modelo de seguridad coherente para entornos multicloud / híbridos?  
- [ ] No, cada nube es un universo paralelo.  
- [ ] Lineamientos generales sin implementación uniforme.  
- [ ] Controles homogéneos para las nubes principales.  
- [ ] Marco unificado de políticas Zero Trust para todas las nubes.  
- [ ] Gobernanza y automatización integral de seguridad cloud.  

6.4. ¿Se aplican controles Zero Trust a las APIs expuestas?  
- [ ] No, las APIs son “confianza implícita”.  
- [ ] API keys básicas.  
- [ ] Autenticación robusta (OAuth2/OIDC) en APIs críticas.  
- [ ] Autenticación, autorización granular y rate limiting.  
- [ ] Protección avanzada (WAF/API gateway con políticas dinámicas y análisis de comportamiento).  

6.5. MTTR (tiempo medio de respuesta) ante incidentes en la nube  
- [ ] No medido.  
- [ ] > 72 horas.  
- [ ] 24–72 horas.  
- [ ] 4–24 horas.  
- [ ] < 4 horas, con automatización parcial o total.  

---

## 7. Datos, clasificación y protección (Pilar 5)

7.1. ¿Existe un esquema formal de clasificación de la información?  
- [ ] No, los datos son una masa homogénea.  
- [ ] Esquema definido pero poco aplicado.  
- [ ] Esquema definido y aplicado en áreas críticas.  
- [ ] Esquema definido y aplicado en toda la organización.  
- [ ] Esquema aplicado, automatizado y revisado regularmente.  

7.2. % de datos sensibles con controles de acceso basados en contexto (usuario, dispositivo, ubicación, riesgo)  
- [ ] 0–20 %  
- [ ] 21–50 %  
- [ ] 51–80 %  
- [ ] 81–95 %  
- [ ] 96–100 %  

7.3. ¿Cómo se controla la exfiltración de datos (DLP)?  
- [ ] No se controla.  
- [ ] Reglas básicas en correo electrónico.  
- [ ] DLP en puestos de trabajo y correo.  
- [ ] DLP integrado en endpoints, red y nube.  
- [ ] DLP contextual con políticas Zero Trust y respuesta automática.  

7.4. ¿Se monitoriza y registra el acceso a datos sensibles?  
- [ ] No.  
- [ ] Solo accesos administrativos.  
- [ ] Accesos de usuarios privilegiados.  
- [ ] Accesos de todos los usuarios a datos sensibles.  
- [ ] Accesos de todos los usuarios, con analítica de comportamiento.  

7.5. ¿Se han producido incidentes de exfiltración o fuga de datos en los últimos 12 meses?  
- [ ] Sí, con impacto significativo.  
- [ ] Sí, pero con impacto limitado.  
- [ ] No.  
- [ ] No lo sabemos con certeza.  
- [ ] Prefiero no contestar, pero la respuesta es elocuente.  

---

## 8. Monitorización, respuesta y resiliencia

8.1. ¿Dispone su organización de un SIEM o plataforma equivalente de monitorización centralizada?  
- [ ] No.  
- [ ] Sí, pero infrautilizado.  
- [ ] Sí, con casos de uso básicos.  
- [ ] Sí, con correlación avanzada y casos de uso Zero Trust.  
- [ ] Sí, integrado con SOAR y automatización de respuesta.  

8.2. MTTD (tiempo medio de detección de incidentes significativos)  
- [ ] No medido.  
- [ ] > 90 días.  
- [ ] 31–90 días.  
- [ ] 8–30 días.  
- [ ] ≤ 7 días.  

8.3. MTTR (tiempo medio de respuesta / contención)  
- [ ] No medido.  
- [ ] > 72 horas.  
- [ ] 24–72 horas.  
- [ ] 4–24 horas.  
- [ ] < 4 horas.  

8.4. ¿Dispone de un plan formal de respuesta a incidentes y de continuidad de negocio que incorpore principios Zero Trust?  
- [ ] No.  
- [ ] Sí, pero no contempla Zero Trust explícitamente.  
- [ ] Sí, con algunas referencias a segmentación y mínimo privilegio.  
- [ ] Sí, con integración explícita de controles Zero Trust.  
- [ ] Sí, probado regularmente con simulaciones y ejercicios.  

8.5. Frecuencia de simulacros de ciberincidentes (incluyendo escenarios Zero Trust)  
- [ ] Nunca.  
- [ ] Cada 2 años.  
- [ ] Anualmente.  
- [ ] Varias veces al año.  
- [ ] De forma continua, porque el mundo no da tregua.  

---

## 9. Cumplimiento normativo, riesgo y ciberseguro

9.1. ¿Cómo valora el grado de alineamiento de su organización con NIS2 (si aplica)?  
- [ ] No aplica / No se ha analizado.  
- [ ] Análisis inicial.  
- [ ] Plan de adecuación en curso.  
- [ ] Cumplimiento razonable con acciones de mejora.  
- [ ] Alineamiento avanzado con revisión continua.  

9.2. ¿Cómo valora el grado de alineamiento con el Esquema Nacional de Seguridad (si aplica)?  
- [ ] No aplica / No se ha analizado.  
- [ ] Cumplimiento mínimo.  
- [ ] Cumplimiento medio con lagunas identificadas.  
- [ ] Cumplimiento alto, con revisiones periódicas.  
- [ ] Cumplimiento certificado, con enfoque Zero Trust.  

9.3. ¿Dispone su organización de póliza(s) de ciberseguro?  
- [ ] No.  
- [ ] En evaluación.  
- [ ] Sí, póliza básica.  
- [ ] Sí, póliza avanzada con requisitos de controles técnicos.  
- [ ] Sí, con bonificaciones ligadas a la madurez Zero Trust.  

9.4. ¿Se utilizan métricas Zero Trust (MTTD, MTTR, MFA, ZTNA, etc.) en el análisis de riesgo y en el diálogo con aseguradoras?  
- [ ] No.  
- [ ] Ocasionalmente, de forma informal.  
- [ ] Sí, para algunos indicadores.  
- [ ] Sí, como parte de un cuadro de mando formal.  
- [ ] Sí, integrado en el modelo actuarial de riesgo.  

9.5. ¿Qué impacto estimado tiene Zero Trust en la reducción del coste de los incidentes de seguridad?  
- [ ] No se ha estimado.  
- [ ] < 10 %.  
- [ ] 10–30 %.  
- [ ] 31–50 %.  
- [ ] > 50 % (o eso le contamos al CFO para dormir tranquilos).  

---

## 10. Cultura, formación y “estado de ánimo Zero Trust”

10.1. ¿Cómo describiría la cultura interna respecto a Zero Trust?  
- [ ] Es un tecnicismo que suena en presentaciones.  
- [ ] Un concepto interesante que algunos equipos empiezan a usar.  
- [ ] Un principio que se discute en proyectos relevantes.  
- [ ] Una referencia habitual en el diseño de procesos y sistemas.  
- [ ] Parte natural del lenguaje cotidiano de la organización.  

10.2. Formación y sensibilización en Zero Trust  
- [ ] No se imparte formación específica.  
- [ ] Formación ocasional a equipos técnicos.  
- [ ] Formación periódica para equipos de TI y seguridad.  
- [ ] Formación extendida a líderes de negocio y mandos.  
- [ ] Formación y simulaciones para toda la organización.  

10.3. ¿Con qué frecuencia se revisan y actualizan las políticas de seguridad para alinearlas con Zero Trust?  
- [ ] Nunca o casi nunca.  
- [ ] Ad hoc, cuando ocurre un incidente.  
- [ ] Cada 2–3 años.  
- [ ] Anualmente.  
- [ ] Varias veces al año, dentro de un ciclo ágil de mejora continua.  

10.4. ¿Cómo percibe la organización el equilibrio entre seguridad Zero Trust y usabilidad?  
- [ ] Zero Trust se percibe como obstáculo.  
- [ ] Aceptación limitada, con quejas recurrentes.  
- [ ] Equilibrio razonable en la mayoría de los casos.  
- [ ] Bien aceptado gracias a soluciones usables.  
- [ ] Se percibe como habilitador de trabajo seguro y flexible.  

10.5. En una frase, ¿qué le diría a alguien que sostiene que Zero Trust es “solo marketing”? (respuesta abierta)  
- __________________________________________________________________  

---

## 11. Indicadores cuantitativos adicionales (opcional)

11.1. Número de incidentes de seguridad significativos en el último año: ______  

11.2. Número de incidentes en los que Zero Trust permitió limitar el impacto: ______  

11.3. Coste económico estimado de los incidentes de seguridad en el último año (EUR): ______  

11.4. Inversión aproximada en iniciativas relacionadas con Zero Trust en el último año (EUR): ______  

11.5. Comentarios adicionales, anécdotas, victorias o dolores memorables relacionados con Zero Trust:  

__________________________________________________________________  