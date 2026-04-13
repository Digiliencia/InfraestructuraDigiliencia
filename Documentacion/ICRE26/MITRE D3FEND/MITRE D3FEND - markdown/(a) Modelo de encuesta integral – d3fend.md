# (a) Modelo de encuesta integral MITRE D3FEND

## 1. Introducción y contexto

Esta encuesta tiene como finalidad cartografiar, con un mínimo de elegancia y un máximo de honestidad, el grado de adopción de MITRE D3FEND y de las métricas asociadas a la defensa informada por amenazas en su organización.

Se dirige a responsables de ciberseguridad, tecnología, continuidad de negocio, gestión de riesgos y, en general, a cualquier alma valiente a la que se le haya encargado "que esto de los ciberataques no nos estalle en las manos".

## 2. Datos generales de la organización

### 2.1. Identificación básica

1. Nombre de la organización:
2. Sector principal de actividad (según clasificación NIS2 / legislación nacional):
   - Energía
   - Transporte
   - Salud
   - Agua potable y aguas residuales
   - Infraestructuras digitales / TIC
   - Banca y servicios financieros
   - Administración pública
   - Industria manufacturera crítica
   - Otros (especificar)
3. Tamaño aproximado de la organización (empleados):
   - Menos de 50
   - 50–249
   - 250–999
   - 1.000–4.999
   - 5.000 o más
4. Ámbito principal de operación:
   - Local / regional
   - Nacional
   - Multinacional dentro de la UE
   - Multinacional global

### 2.2. Rol de la persona que responde

5. Cargo principal:
   - CISO / Director de Seguridad de la Información
   - CIO / Director de Tecnología
   - Responsable de SOC / CSIRT interno
   - Responsable de Continuidad de Negocio / Resiliencia
   - Responsable de Riesgos / Cumplimiento
   - Otro (especificar)
6. Antigüedad aproximada en el rol actual:
   - Menos de 1 año
   - 1–3 años
   - 3–7 años
   - Más de 7 años

## 3. Conocimiento y adopción de MITRE D3FEND

### 3.1. Nivel de conocimiento

7. ¿Cuál es el nivel de conocimiento general de MITRE D3FEND en su organización?
   - Nunca lo he oído mencionar
   - Me suena vagamente, pero no se utiliza
   - Lo conocen algunas personas clave (p.ej., ingeniería de detecciones, arquitectura de seguridad)
   - Está integrado en algunos procesos o herramientas, aunque sin estandarizar
   - Forma parte explícita de nuestra metodología y documentación de seguridad

8. En relación con MITRE ATT&CK, ¿cómo describiría la situación en su organización?
   - No utilizamos MITRE ATT&CK
   - Se utiliza de forma puntual para análisis o presentaciones
   - Está integrado en procesos de threat intel / ingeniería de detección
   - Se utiliza sistemáticamente en SOC, red team o arquitectura
   - ATT&CK está alineado con nuestros controles y roadmap de seguridad

### 3.2. Uso de D3FEND en la práctica

9. ¿Se utiliza explícitamente MITRE D3FEND para describir controles o contramedidas en su organización?
   - No, no se utiliza
   - Se utiliza de forma experimental o en pilotos
   - Se utiliza sólo en ciertos proyectos o dominios (p.ej., cloud, endpoint)
   - Se utiliza de manera consistente en varios dominios
   - Es el lenguaje de referencia para describir controles y coberturas

10. ¿En qué ámbitos se hace referencia a D3FEND (puede seleccionar varios)?
   - Arquitectura de seguridad
   - Ingeniería de detecciones / reglas de SIEM
   - Diseño de playbooks de respuesta
   - Análisis de brechas frente a ATT&CK
   - OT / ICS / sistemas industriales
   - Relación con proveedores / RFPs
   - No se hace referencia

11. ¿La organización utiliza el conocimiento de D3FEND para discutir inversiones en seguridad (p.ej., priorización de herramientas o proyectos)?
   - Nunca
   - Ocasionalmente, de manera informal
   - En algunos casos, para justificar decisiones concretas
   - De forma habitual, como marco de referencia
   - Está incorporado en el proceso formal de planificación y presupuesto

## 4. Modelado con D3FEND CAD y grafos de contramedidas

### 4.1. Uso de D3FEND CAD

12. ¿Conoce o utiliza su organización la herramienta D3FEND CAD para modelar escenarios y arquitecturas defensivas?
   - Desconocemos la existencia de D3FEND CAD
   - Conocemos la herramienta, pero no la utilizamos
   - Se ha probado en algún caso aislado o laboratorio
   - Se utiliza de manera limitada para algunos sistemas o proyectos
   - Se utiliza sistemáticamente para modelar arquitecturas de seguridad y escenarios de ataque/defensa

13. En caso de uso, ¿para qué finalidades se ha empleado D3FEND CAD?
   - Documentar arquitecturas defensivas de referencia
   - Analizar coberturas frente a ATT&CK
   - Diseñar y ensayar playbooks de respuesta
   - Modelar escenarios de ransomware / ataques dirigidos
   - Modelar sistemas OT / ICS
   - Formación interna y comunicación con otras áreas
   - No aplicable / no se utiliza

### 4.2. Calidad y alcance del modelado

14. ¿En qué medida considera que los modelos (con D3FEND CAD u otras herramientas) reflejan de manera fiel la realidad de sus sistemas?
   - Son meros dibujos bonitos para presentaciones
   - Reflejan parcialmente la realidad, con simplificaciones significativas
   - Recogen adecuadamente los componentes críticos, pero no todo el detalle
   - Son representaciones suficientemente fieles para extraer métricas fiables
   - Se actualizan de forma continua y están integrados con inventarios y CMDB

15. ¿Qué porcentaje aproximado de activos críticos (según su propia definición de criticidad) está representado en modelos formales de contramedidas?
   - 0–20 %
   - 21–40 %
   - 41–60 %
   - 61–80 %
   - 81–100 %
   - Desconozco el dato / preferiría no responder

## 5. Indicadores de cobertura ATT&CK–D3FEND

### 5.1. Definición de catálogos de amenazas

16. ¿Dispone su organización de un catálogo explícito de técnicas ATT&CK consideradas prioritarias?
   - No existe tal catálogo
   - Existe de forma informal (listas dispersas, documentos no consolidados)
   - Existe un catálogo definido para algunos dominios/sistemas
   - Existe un catálogo definido a nivel organizativo
   - El catálogo está alineado con amenazas sectoriales y se revisa periódicamente

17. ¿Con qué frecuencia se revisa ese catálogo de técnicas ATT&CK prioritarias?
   - Nunca / no se revisa
   - Cada más de 2 años
   - Anualmente
   - Semestralmente
   - Trimestralmente o con mayor frecuencia

### 5.2. Medición de coberturas

18. ¿Miden de forma sistemática qué técnicas ATT&CK cuentan con al menos una contramedida D3FEND implementada?
   - No, no realizamos ese tipo de medición
   - Sí, pero sólo para algunos sistemas o proyectos
   - Sí, para los activos críticos
   - Sí, de forma sistemática a nivel organizativo

19. ¿Cómo describiría el nivel actual de cobertura de técnicas ATT&CK críticas con contramedidas adecuadas?
   - Mayoritariamente desconocido
   - Parcial y con lagunas importantes
   - Razonable, aunque con brechas conocidas pendientes de abordar
   - Alto, con un inventario claro de las pocas lagunas restantes
   - Medido y gestionado como objetivo explícito en los planes de seguridad

20. Indique, de forma aproximada, qué porcentaje de las técnicas ATT&CK críticas identificadas considera usted que tiene al menos una contramedida efectiva implementada:
   - 0–25 %
   - 26–50 %
   - 51–75 %
   - 76–90 %
   - Más del 90 %
   - No se dispone de esta estimación

21. ¿Utilizan mapas de calor, dashboards u otras visualizaciones para representar coberturas ATT&CK–D3FEND?
   - No, trabajamos básicamente con documentos y hojas de cálculo
   - Sí, pero desarrollados de forma ad hoc sin estandarización
   - Sí, mediante dashboards consolidados a nivel de SOC u oficina de ciberseguridad
   - Sí, con cuadros de mando ejecutivos que se revisan en comités de dirección

## 6. Métricas operativas (latencia, eficacia, telemetría)

### 6.1. Latencia de detección y respuesta

22. ¿Miden de forma sistemática la latencia de detección (tiempo desde el evento hasta su detección como incidente)?
   - No se mide
   - Se mide de forma puntual para ciertos incidentes
   - Se mide para los incidentes de alta criticidad
   - Se mide de forma sistemática para todos los incidentes gestionados

23. Para incidentes críticos, ¿en qué franja se sitúa habitualmente el tiempo medio de detección (MTTD) reportado?
   - Menos de 5 minutos
   - Entre 5 y 30 minutos
   - Entre 30 minutos y 4 horas
   - Entre 4 y 24 horas
   - Más de 24 horas
   - No se dispone de este dato

24. ¿Miden el tiempo hasta la mitigación o contención efectiva (MTTM/MTTR) de incidentes críticos?
   - No se mide
   - Se mide de forma ad hoc en post-mortems
   - Se mide para incidentes críticos de forma sistemática
   - Se mide y se establecen objetivos explícitos (SLOs) de mejora

### 6.2. Eficacia de mitigaciones

25. ¿Calculan la tasa de éxito de las mitigaciones (es decir, qué proporción de intentos de mitigación logra realmente neutralizar la amenaza)?
   - No, ese indicador no se calcula
   - Se estima cualitativamente en algunos análisis
   - Se calcula cuantitativamente para incidentes críticos
   - Se calcula y se reporta de forma periódica

26. ¿Disponen de métricas sobre la recurrencia de incidentes de tipo similar tras supuestas mitigaciones?
   - No
   - Sí, de manera informal o ad hoc
   - Sí, mediante indicadores sistemáticos de recurrencia

### 6.3. Telemetría y cobertura de sensores

27. ¿Se cuantifica qué porcentaje de activos o flujos relevantes está instrumentado con telemetría adecuada (sensores, logs, sondas, etc.)?
   - No se cuantifica
   - Se cuantifica para algunos sistemas o entornos
   - Se cuantifica para activos críticos
   - Se cuantifica de forma sistemática a nivel de organización

28. ¿Cómo describiría la calidad de la telemetría disponible para soportar las técnicas defensivas modeladas (por ejemplo, según D3FEND)?
   - Fragmentaria y poco fiable
   - Aceptable, pero con lagunas significativas
   - Buena, aunque mejorable
   - Alta, suficiente para análisis avanzados y automatización

29. ¿Se analizan y reportan tasas de falsos positivos y falsos negativos en las detecciones clave?
   - No
   - Sí, pero sólo de forma puntual
   - Sí, como parte de un proceso de mejora continua del SOC

## 7. Entornos OT / ICS y extensión D3FEND para OT

30. ¿Opera su organización infraestructuras OT / ICS o sistemas ciberfísicos críticos?
   - No
   - Sí, pero con peso limitado en la operación
   - Sí, constituyen una parte significativa de la operación

31. En caso afirmativo, ¿se han modelado explícitamente contramedidas para entornos OT utilizando D3FEND u otros marcos equivalentes?
   - No se han modelado
   - Se han modelado parcialmente, de forma piloto
   - Se han modelado para activos OT críticos
   - Se ha realizado un modelado amplio y sistemático

32. ¿Se dispone de métricas específicas para OT, tales como porcentaje de rutas de mando y control cubiertas, cobertura de monitorización de protocolos industriales o tiempo de recuperación de funciones OT críticas?
   - No se dispone de métrricas específicas
   - Se dispone de algunas métricas básicas
   - Se dispone de un conjunto definido y revisado de métrricas OT

## 8. Integración con cumplimiento normativo y regulación

33. ¿Cómo describiría el grado de integración entre las prácticas de seguridad basadas en ATT&CK/D3FEND y las obligaciones normativas (NIS2, legislación nacional, sectorial, etc.)?
   - Son mundos separados que se toleran a distancia
   - Hay conexiones informales entre ambos mundos
   - Se procura alinear controles técnicos con requisitos normativos
   - Existe un mapeo explícito entre controles/técnicas y requisitos normativos

34. ¿Se ha realizado un mapeo formal entre D3FEND y marcos de control como NIST 800-53, ISO 27001 o políticas internas?
   - No
   - Sí, parcialmente (para algunos dominios)
   - Sí, de forma amplia y documentada

35. ¿Utilizan métricas derivadas de D3FEND (cobertura, latencia, eficacia, telemetría) como evidencia en auditorías o procesos de supervisión?
   - No
   - En ocasiones, de manera complementaria
   - De forma habitual, como evidencia principal

## 9. Métricas de negocio, IGM y ROI de seguridad

36. ¿Se traduce el estado de coberturas y métricas de seguridad en indicadores de riesgo para la alta dirección (p.ej., riesgo residual frente a escenarios de referencia)?
   - No, la alta dirección recibe información básicamente cualitativa
   - Sí, con indicadores mayoritariamente cualitativos y algunos cuantitativos
   - Sí, con indicadores cuantitativos alineados con apetito y tolerancia al riesgo

37. ¿Se evalúa de manera estructurada el impacto económico de incidentes (pérdidas directas, costes de recuperación, impacto reputacional aproximado, etc.)?
   - No
   - Sí, de forma puntual en grandes incidentes
   - Sí, mediante un marco de análisis económico y actuarial definido

38. ¿Se calculan indicadores de madurez global (IGM) de la capacidad defensiva, basados en métricas de cobertura y eficacia?
   - No
   - Sí, pero con metodologías ad hoc
   - Sí, con un modelo formalizado y revisado periódicamente

39. ¿Se evalúa el retorno de la inversión (ROI) de proyectos o herramientas de seguridad utilizando métricas derivadas de ATT&CK/D3FEND (por ejemplo, reducción de tiempo de detección, de superficies no cubiertas o de frecuencia de incidentes)?
   - No
   - De forma episódica, cuando hay que defender un presupuesto
   - De manera sistemática, en el ciclo de vida de inversiones en seguridad

## 10. Gobierno, cultura y talento

40. ¿Qué órganos de gobierno revisan regularmente los indicadores de seguridad basados en coberturas y métricas operativas?
   - Ninguno, se revisan de manera informal
   - Comité de seguridad / continuidad
   - Comité de riesgos
   - Comité de dirección
   - Consejo de administración

41. ¿Con qué frecuencia se revisan formalmente estos indicadores en órganos de gobierno?
   - Menos de una vez al año
   - Anualmente
   - Trimestralmente
   - Mensualmente o con mayor frecuencia

42. ¿Dispone de perfiles internos con conocimiento específico de MITRE ATT&CK y D3FEND (ingeniería de detecciones, arquitectos de seguridad, analistas de riesgo técnico)?
   - No
   - Sí, uno o dos perfiles clave
   - Sí, un equipo dedicado o comunidad de práctica

43. ¿Se incluye la formación en ATT&CK/D3FEND en los planes de capacitación interna?
   - No
   - Sí, de forma puntual
   - Sí, de forma estructurada y periódica

## 11. Perspectiva y próximos pasos

44. ¿Qué barreras principales percibe para una adopción más amplia y rigurosa de D3FEND en su organización?
   - Falta de conocimiento interno
   - Falta de tiempo y recursos
   - Falta de herramientas que integren D3FEND de forma nativa
   - Complejidad percibida / curva de aprendizaje
   - Falta de presión regulatoria o de mercado
   - Otras (especificar)

45. En un mundo ideal (o al menos moderadamente razonable), ¿cuál sería el primer paso realista que su organización podría dar en los próximos 12 meses para mejorar en este ámbito?
   - Definir un catálogo de técnicas ATT&CK prioritarias
   - Mapear controles existentes a D3FEND
   - Empezar a utilizar D3FEND CAD en un sistema piloto
   - Definir y acordar 3–5 métricas clave de cobertura y eficacia
   - Integrar estas métricas en un cuadro de mando ejecutivo
   - Incluir formación específica en el plan de capacitación

46. Comentarios adicionales, confesiones tardías o deseos para el futuro próximo (respuesta abierta):

---

Gracias por el tiempo, la honestidad y, sobre todo, por seguir intentándolo en un mundo estadísticamente diseñado para hacerle la vida imposible al CISO.