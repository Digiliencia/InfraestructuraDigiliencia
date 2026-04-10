# Encuesta Integral sobre Riesgos y Ataques impulsados por Agentic IA

> Versión 1.0 — Inspirada en el perfil de gestión de riesgos de Agentic IA del CLTC Berkeley, la guía de la AEPD y el marco multicapa de ENISA para IA.

## 0. Datos generales de la organización

1. Sector principal de actividad  
   - [ ] Administración pública  
   - [ ] Sanitario / Farma  
   - [ ] Financiero / Seguros  
   - [ ] Energía / Infraestructuras críticas  
   - [ ] Industria / Manufacturing  
   - [ ] TIC / Servicios digitales  
   - [ ] Educación / Investigación  
   - [ ] Otro (especificar): ____________

2. Tamaño aproximado de la organización (plantilla total)  
   - [ ] < 50 personas  
   - [ ] 50–249  
   - [ ] 250–999  
   - [ ] 1.000–4.999  
   - [ ] ≥ 5.000  

3. Ámbito geográfico de operación  
   - [ ] Local / Regional (España)  
   - [ ] Nacional (España)  
   - [ ] Unión Europea  
   - [ ] Global  

4. Rol de la persona que responde  
   - [ ] CISO / Responsable de Seguridad  
   - [ ] DPO / Delegado de Protección de Datos  
   - [ ] Director de TI / CTO / CIO  
   - [ ] Responsable de Riesgos / Cumplimiento  
   - [ ] Arquitecto de Seguridad / Zero Trust  
   - [ ] Otro (especificar): ____________  

---

## 1. Uso actual de sistemas de Agentic IA

5. ¿En qué grado utiliza su organización sistemas de Agentic IA (agentes capaces de planificar y ejecutar tareas con autonomía)?  
   - [ ] No los utilizamos y no está previsto hacerlo  
   - [ ] No los utilizamos, pero estamos explorando posibles casos de uso  
   - [ ] Pilotos limitados en áreas concretas  
   - [ ] Uso moderado en procesos críticos seleccionados  
   - [ ] Uso extensivo y transversal en múltiples procesos de negocio  

6. Principales casos de uso de agentes de IA en la organización (seleccione todos los que apliquen)  
   - [ ] Automatización de operaciones TI / SecOps  
   - [ ] Atención al cliente / chatbots avanzados  
   - [ ] Asistentes internos (productividad, ofimática, desarrollo)  
   - [ ] Análisis de datos / Business Intelligence  
   - [ ] Detección y respuesta a incidentes de seguridad  
   - [ ] Otros (especificar): ____________  

7. ¿Qué nivel de autonomía se concede habitualmente a estos agentes?  
   - [ ] Solo sugerencias (sin acciones automatizadas)  
   - [ ] Acciones automatizadas de bajo impacto (no productivas)  
   - [ ] Acciones automatizadas en entornos de prueba / sandbox  
   - [ ] Acciones automatizadas en sistemas de producción con límites claros  
   - [ ] Alta autonomía en sistemas de producción (mínima supervisión humana)  

8. ¿Se ha documentado formalmente el catálogo de agentes de IA desplegados (con objetivos, alcance, herramientas y datos usados)?  
   - [ ] Sí, catálogo completo y actualizado  
   - [ ] Sí, pero parcial o desactualizado  
   - [ ] No, pero está en preparación  
   - [ ] No se ha considerado necesario (todavía)  

---

## 2. Gobernanza y responsabilidades de Agentic IA

9. ¿Existe un marco de gobernanza específico para sistemas de Agentic IA, alineado con marcos como NIST AI RMF o el perfil de Agentic IA de Berkeley?  
   - [ ] Sí, formalizado y aprobado por la alta dirección  
   - [ ] Sí, en fase piloto  
   - [ ] No, pero está planificado  
   - [ ] No, cada proyecto se gestiona de forma aislada  
   - [ ] No, no se considera relevante por el momento  

10. ¿Qué órganos participan de forma sistemática en las decisiones sobre despliegue de Agentic IA?  
    - [ ] Alta dirección / Comité de riesgos  
    - [ ] CISO / Seguridad de la información  
    - [ ] DPO / Privacidad  
    - [ ] Arquitectura empresarial / Zero Trust  
    - [ ] Unidades de negocio  
    - [ ] Jurídico / Cumplimiento  
    - [ ] Otros (especificar): ____________  

11. ¿Se aplica la “Regla de 2” (no combinar a la vez: entrada no controlada, datos sensibles y acciones autónomas)?  
    - [ ] Sí, se aplica de forma sistemática  
    - [ ] Sí, en la mayoría de los casos  
    - [ ] Solo en casos de alto riesgo  
    - [ ] No, pero se está evaluando adoptarla  
    - [ ] No, no se aplica ni se prevé hacerlo  

12. ¿Se realizan evaluaciones de impacto (DPIA / EIPD) específicas para los agentes de IA?  
    - [ ] Sí, para todos los sistemas de Agentic IA  
    - [ ] Sí, solo para los de mayor riesgo  
    - [ ] En preparación  
    - [ ] No se realizan  

13. ¿Con qué frecuencia se revisa y actualiza la evaluación de riesgos de los agentes de IA?  
    - [ ] Trimestral  
    - [ ] Semestral  
    - [ ] Anual  
    - [ ] Solo tras un incidente  
    - [ ] No hay ciclo de revisión definido  

---

## 3. Datos, memoria y superficie de ataque

14. ¿Cómo clasificaría el tipo de datos a los que acceden sus agentes de IA?  
    - [ ] Datos públicos o de baja sensibilidad  
    - [ ] Datos internos no sensibles  
    - [ ] Datos personales no sensibles  
    - [ ] Datos personales sensibles (salud, financieros, etc.)  
    - [ ] Datos altamente confidenciales / secretos empresariales  
    - [ ] No se ha realizado esta clasificación  

15. ¿Se han establecido políticas de minimización de datos específicas para los agentes (acceso “just enough”, “just in time”)?  
    - [ ] Sí, formalizadas y aplicadas  
    - [ ] Parcialmente, en función del proyecto  
    - [ ] En desarrollo  
    - [ ] No  

16. En relación con la memoria de los agentes (almacenamiento de contexto, historial, logs enriquecidos, etc.):  
    - [ ] Existe compartmentalización clara de memorias por caso de uso  
    - [ ] Se definen tiempos de retención y se aplican borrados periódicos  
    - [ ] Se aplican técnicas de seudonimización / anonimización  
    - [ ] La memoria del agente es amplia y poco restringida  
    - [ ] No existe una política específica sobre la memoria del agente  

17. ¿Se han analizado riesgos de envenenamiento de memoria o de índices (por ejemplo, en sistemas RAG)?  
    - [ ] Sí, y se han desplegado controles específicos  
    - [ ] Sí, pero sin controles específicos por el momento  
    - [ ] En fase de evaluación  
    - [ ] No se ha analizado  

18. ¿Cómo se gestiona el acceso de los agentes a servicios externos (APIs, plugins, herramientas de terceros)?  
    - [ ] Lista de permitidos (allowlist) estricta, con revisión periódica  
    - [ ] Aprobación caso por caso  
    - [ ] Confianza por defecto en servicios del proveedor de IA  
    - [ ] No existen controles específicos sobre estas conexiones  

---

## 4. Métricas de comportamiento del agente (UAR, PAR, PED, etc.)

19. ¿Evalúan actualmente el Unsafe Action Rate (UAR) de sus agentes (porcentaje de escenarios que llevan a acciones inseguras o contrarias a la política)?  
    - [ ] Sí, con métricas cuantitativas definidas  
    - [ ] Sí, de forma cualitativa / ad hoc  
    - [ ] En fase de diseño  
    - [ ] No, pero nos interesa hacerlo  
    - [ ] No, y no se considera prioritario  

20. Si mide el UAR, ¿con qué frecuencia se realizan estos ejercicios de prueba o “red teaming” contra el agente?  
    - [ ] Mensual  
    - [ ] Trimestral  
    - [ ] Semestral  
    - [ ] Anual  
    - [ ] Solo tras cambios significativos en el agente  
    - [ ] No se mide UAR  

21. ¿Evalúan el Policy Adherence Rate (PAR) (porcentaje de acciones del agente que cumplen la política definida)?  
    - [ ] Sí, con indicadores periódicos  
    - [ ] Sí, de forma esporádica  
    - [ ] En diseño  
    - [ ] No  

22. ¿Se han definido políticas específicas de “dentro de rol / fuera de rol” para los agentes (Out-of-Role Action Rate, OORAR)?  
    - [ ] Sí, y se monitoriza el OORAR  
    - [ ] Sí, pero no se cuantifica el OORAR  
    - [ ] En desarrollo  
    - [ ] No  

23. ¿Analizan el riesgo de escalado de privilegios de los agentes, basado en algo equivalente a un Privilege-Escalation Distance (PED)?  
    - [ ] Sí, y se dispone de métricas de PED  
    - [ ] Sí, pero sin métricas formales  
    - [ ] En estudio  
    - [ ] No  

24. ¿Evalúan el Retrieval Risk Score (RRS) asociado a las fuentes de datos que utilizan los agentes para recuperar información (por ejemplo, bases RAG internas)?  
    - [ ] Sí, con metodología definida  
    - [ ] Sí, pero informalmente  
    - [ ] En fase de diseño  
    - [ ] No  

25. ¿Se utiliza alguna métrica de coste-riesgo (equivalente a Cost-Exploit Susceptibility, CES) para estimar el impacto económico de un exploit impulsado por Agentic IA?  
    - [ ] Sí, integrada en el modelo de riesgo financiero  
    - [ ] Sí, pero como aproximación cualitativa  
    - [ ] En diseño  
    - [ ] No  

---

## 5. Métricas operativas de SOC y gestión de incidentes

26. En el SOC (interno o externo), ¿qué nivel de automatización basada en IA se emplea para la triage de alertas?  
    - [ ] Ninguna automatización basada en IA  
    - [ ] IA solo para agrupar o enriquecer alertas  
    - [ ] IA para priorización de alertas, decisiones siguen siendo humanas  
    - [ ] IA para triage casi completo, con revisión humana muestral  
    - [ ] IA con capacidad de respuesta autónoma (acciones de contención)  

27. ¿Se mide el Alert Triage Automation Rate (porcentaje de alertas triadas por IA)?  
    - [ ] Sí, con objetivo explícito de mejora  
    - [ ] Sí, pero solo como dato observacional  
    - [ ] En planificación  
    - [ ] No  

28. ¿Se monitoriza el Mean Time to Triage (MTTT) antes y después de introducir la Agentic IA en el SOC?  
    - [ ] Sí, con comparativas históricas  
    - [ ] Sí, pero sin comparativa formal  
    - [ ] En diseño  
    - [ ] No  

29. ¿Se monitoriza la tasa de falsos positivos y su reducción atribuible a IA?  
    - [ ] Sí, y se utiliza como indicador clave (KPI)  
    - [ ] Sí, pero no se vincula explícitamente a IA  
    - [ ] En planificación  
    - [ ] No  

30. ¿Se mide el Time-to-Contain (TTC) específicamente para incidentes donde se sospecha o confirma un ataque impulsado por Agentic IA?  
    - [ ] Sí, claramente diferenciado de otros incidentes  
    - [ ] Sí, pero sin distinción por tipo de ataque  
    - [ ] En diseño  
    - [ ] No  

---

## 6. Cumplimiento normativo y marcos de referencia

31. ¿Con qué marcos y normas se alinea su gestión de Agentic IA? (seleccione todos los que apliquen)  
    - [ ] GDPR / RGPD  
    - [ ] Guía AEPD sobre Agentic IA  
    - [ ] NIST AI Risk Management Framework  
    - [ ] Perfil de Agentic IA (CLTC Berkeley)  
    - [ ] ENISA Multilayer Framework for Good Cybersecurity Practices for AI  
    - [ ] ISO/IEC 27001  
    - [ ] Otras normas ISO/IEC (por ejemplo, 15408, 18045)  
    - [ ] AI Act (UE)  
    - [ ] Otros (especificar): ____________  

32. ¿Existe un registro de actividades de tratamiento específico para sistemas de Agentic IA, según exige el RGPD?  
    - [ ] Sí, detallado por agente y proceso  
    - [ ] Sí, pero integrado en registros generales  
    - [ ] En elaboración  
    - [ ] No  

33. ¿Se han establecido cláusulas contractuales específicas con proveedores de IA sobre seguridad, uso de datos, retención y auditoría?  
    - [ ] Sí, para todos los contratos relevantes  
    - [ ] Sí, pero solo para los proveedores críticos  
    - [ ] En revisión  
    - [ ] No  

34. ¿Se exige a los proveedores de soluciones Agentic IA alguna certificación de ciberseguridad o cumplimiento (por ejemplo, ISO/IEC 27001, esquemas derivados de ISO/IEC 15408, etc.)?  
    - [ ] Sí, siempre  
    - [ ] Sí, en función del riesgo  
    - [ ] No, pero se está considerando  
    - [ ] No  

---

## 7. Capacitación, cultura y transparencia

35. ¿Se imparten formaciones específicas sobre riesgos de Agentic IA al personal técnico (DevOps, SecOps, arquitectos, etc.)?  
    - [ ] Sí, con programa estructurado anual  
    - [ ] Sí, de forma puntual  
    - [ ] En preparación  
    - [ ] No  

36. ¿Se forman a decisores de negocio y alta dirección sobre las implicaciones de los agentes autónomos (riesgos, métricas clave, responsabilidades legales)?  
    - [ ] Sí, con sesiones periódicas  
    - [ ] Sí, de manera ad hoc  
    - [ ] En preparación  
    - [ ] No  

37. ¿Se informa a los usuarios finales (empleados, clientes) cuando interactúan con un agente de IA, y sobre el tipo de datos que se emplean?  
    - [ ] Sí, de forma clara y previa a la interacción  
    - [ ] Sí, pero de forma poco destacada  
    - [ ] Solo en algunos casos  
    - [ ] No  

38. ¿Se dispone de procedimientos para que los interesados ejerzan sus derechos (acceso, rectificación, oposición, etc.) frente a tratamientos realizados por agentes de IA?  
    - [ ] Sí, integrados en los procesos existentes  
    - [ ] En diseño  
    - [ ] No  

---

## 8. Experiencia con incidentes de Agentic IA

39. ¿Ha identificado su organización incidentes o casi-incidentes en los que un agente de IA haya realizado acciones no deseadas o inseguras?  
    - [ ] Sí, incidentes con impacto significativo  
    - [ ] Sí, incidentes menores / casi-incidentes  
    - [ ] No, pero se sospechan “comportamientos inquietantes”  
    - [ ] No se han detectado incidentes  

40. En caso afirmativo, ¿qué tipo de incidentes se han observado?  
    - [ ] Fugas de datos o exfiltración inadvertida  
    - [ ] Acceso indebido a sistemas o privilegios  
    - [ ] Respuestas manipuladas por inyección de prompts  
    - [ ] Errores de razonamiento con impacto operativo  
    - [ ] Otros (especificar): ____________  

41. Tras estos incidentes, ¿se han ajustado las métricas (UAR, PAR, PED, etc.) o controles aplicados a los agentes?  
    - [ ] Sí, se han redefinido umbrales y controles  
    - [ ] Sí, pero solo a nivel puntual  
    - [ ] En proceso  
    - [ ] No  

---

## 9. Perspectiva estratégica y ROI de la Agentic IA

42. ¿Cómo valoraría, en términos generales, el equilibrio entre beneficios y riesgos de la Agentic IA en su organización?  
    - [ ] Beneficio neto muy elevado, riesgos bajo control  
    - [ ] Beneficio neto moderado, riesgos gestionables  
    - [ ] Equilibrio incierto (los beneficios no compensan claramente los riesgos)  
    - [ ] Riesgos percibidos superiores a los beneficios actuales  

43. ¿Dispone de algún modelo de ROI que incorpore métricas de seguridad y resiliencia (por ejemplo, reducción de MTTT, TTC, incidentes evitados)?  
    - [ ] Sí, formalizado  
    - [ ] En diseño  
    - [ ] No, pero se considera necesario  
    - [ ] No, y no se tiene previsto  

44. Finalmente, ¿cómo describiría, con total sinceridad, la actitud de la organización ante la Agentic IA?  
    - [ ] Entusiasta pero disciplinada (románticos con control de cambios)  
    - [ ] Cautelosa pero abierta (escépticos de laboratorio)  
    - [ ] Pragmática oportunista (si aporta valor, se implementa… luego ya veremos)  
    - [ ] Defensiva (solo por obligación o presión externa)  
    - [ ] Otra (especificar): ____________  

---

### Comentarios adicionales

45. Por favor, incluya cualquier comentario, anécdota o reflexión sobre su experiencia con los agentes de IA y su impacto en la ciberseguridad de la organización:

> ______________________________________________________________________  
> ______________________________________________________________________  
> ______________________________________________________________________  
