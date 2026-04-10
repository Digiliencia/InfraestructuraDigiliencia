# Encuesta Integral sobre TLPT, Ciberresiliencia y DORA/TIBER-ES

> Objetivo: recoger, con elegancia inquisitiva, el estado real de adopción y eficacia de las pruebas TLPT en las organizaciones sujetas (o aspirantes) a DORA y TIBER-ES.[web:16][web:38]

## 0. Datos generales de la organización

1. Tipo de entidad (marcar todas las que apliquen)
   - [ ] Entidad de crédito
   - [ ] Empresa de servicios de inversión
   - [ ] Entidad de pago / dinero electrónico
   - [ ] Infraestructura de mercado financiero (sistema de pagos, CCP, CSD, etc.)
   - [ ] Aseguradora / reaseguradora
   - [ ] Proveedor TIC crítico o importante (cloud, core bancario, procesador de pagos, etc.)[web:39]
   - [ ] Otro (por favor, especifique): __________

2. Ámbito geográfico principal de operación
   - [ ] España
   - [ ] UE (multipaís)
   - [ ] Global (UE + terceros países)

3. Volumen aproximado de activos / negocio gestionado (seleccione el rango que mejor le represente)
   - [ ] Micro / pequeña entidad
   - [ ] Mediana
   - [ ] Grande
   - [ ] Sistémica / de importancia significativa (G-SII/O-SII, infraestructuras críticas, etc.)[web:31]

---

## 1. Gobierno de TLPT y alineamiento normativo

### 1.1 Marco de referencia

4. ¿Existe en la organización una política formal que regule las pruebas TLPT (o equivalentes TIBER-ES/CBEST)?
   - [ ] No existe, pero hablamos mucho de “hacer un Red Team algún día”.
   - [ ] Existe un documento genérico de pruebas de seguridad; TLPT se menciona de pasada.
   - [ ] Existe política específica TLPT/TIBER-ES aprobada por el órgano de administración.[web:16][web:38]
   - [ ] Existe política TLPT, procedimiento operativo y criterios de selección de entidades/alcance claramente definidos.

5. ¿En qué medida la alta dirección participa en la aprobación del alcance y resultados del TLPT?
   - [ ] Apenas es informada, cuando se acuerdan a última hora las diapositivas.
   - [ ] Recibe un resumen ejecutivo después de la prueba.
   - [ ] Aprueba el alcance antes de la prueba y valida el plan de remediación.[web:16]
   - [ ] Participa activamente en la priorización de escenarios, recursos y acciones de remediación.

### 1.2 Roles, equipos y segregación de funciones

6. ¿Están formalmente definidos los roles de Control Team / White Team / Red Team / Blue Team, conforme a DORA y TIBER-ES?[web:16][web:38]
   - [ ] No, usamos variaciones creativas según el proyecto.
   - [ ] Están descritos de forma genérica, sin vinculación específica a TLPT/TIBER-ES.
   - [ ] Están definidos por escrito, asignados nominalmente y aprobados por la función de riesgos.
   - [ ] Están definidos, asignados y se revisan después de cada ejercicio para mejorarlos.

7. ¿Existe una política específica sobre el uso de testers internos para TLPT (cuando procede)?
   - [ ] No se contempla el uso de testers internos.
   - [ ] Se usa Red Team interno sin política ni salvaguardas formales.
   - [ ] Hay política de uso de testers internos alineada con DORA, pero no se revisa periódicamente.[web:16]
   - [ ] Política formalizada, revisada, con salvaguardas de independencia y obligación de test externo al menos cada 3 ciclos.

---

## 2. Alcance, criticidad y dependencia de terceros

### 2.1 Funciones críticas y servicios externalizados

8. ¿Dispone de un inventario formal y actualizado de funciones críticas de negocio, conforme a DORA y al BIA corporativo?[web:26]
   - [ ] No, dependemos de la memoria colectiva y de “lo que todo el mundo sabe”.
   - [ ] Existe un inventario en algún repositorio, pero no está alineado con DORA ni BIA.
   - [ ] Inventario formal, aprobado, revisado al menos una vez al año.
   - [ ] Inventario formal, revisado, con trazabilidad directa a arquitectura TIC y a TLPT en vigor.

9. En el último TLPT realizado, ¿qué porcentaje aproximado de funciones críticas se incluyó en el alcance?
   - [ ] 0–25% (un TLPT “degustación”).
   - [ ] 26–50%.
   - [ ] 51–75%.
   - [ ] >75% (ejercicio “plato fuerte”).

10. ¿En qué medida se incluyeron en el TLPT los servicios de terceros TIC que soportan esas funciones críticas?[web:39]
    - [ ] No se incluyeron proveedores TIC.
    - [ ] Se incluyó solo al proveedor principal.
    - [ ] Se incluyeron los principales proveedores TIC críticos/ importantes definidos por el marco DORA.
    - [ ] Se articuló un ejercicio conjunto o “pooled” con varios proveedores y entidades.

### 2.2 Ámbito técnico

11. El TLPT ejecutado se realizó sobre:
    - [ ] Entornos de preproducción o laboratorio, por motivos de “prudencia”.
    - [ ] Mezcla de preproducción y producción.
    - [ ] Sistemas en producción, con medidas de contención de riesgo, según exigen DORA y TIBER-EU/TIBER-ES.[web:36][web:38]

12. Tipo de activos en alcance (marcar todas las opciones relevantes)
    - [ ] Canales digitales de clientes (web, móvil).
    - [ ] Sistemas de pagos y compensación.
    - [ ] Sistemas de mercado de valores (negociación, liquidación).
    - [ ] Sistemas core bancarios / core aseguradores.
    - [ ] Sistemas de gestión interna (ERP, HR, etc.).
    - [ ] Infraestructura de red, IAM, directorio, etc.
    - [ ] Otros: __________

---

## 3. Metodología TLPT, TTI y Red Team

### 3.1 Inteligencia de amenazas (Threat Intelligence / TTI)

13. ¿Se elaboró una fase de inteligencia de amenazas específica (TTI), conforme al marco TIBER-ES / TIBER-EU?[web:38][web:31]
    - [ ] No, se usó una lista genérica de vulnerabilidades.
    - [ ] Sí, pero limitada a fuentes internas y sin mapeo a amenazas del sector.
    - [ ] Sí, con análisis de amenazas específico del sector y de la entidad.
    - [ ] Sí, con TTI específica, validada por el equipo TIBER-ES / TLPT Authority, incluyendo escenarios sectoriales y cadena de suministro.

14. Número de escenarios de ataque definidos en la fase TTI:
    - [ ] 1–3 (un “menú degustación”).
    - [ ] 4–6.
    - [ ] 7–10.
    - [ ] >10 (para gourmets de la complejidad).

15. ¿Qué porcentaje aproximado de los escenarios TTI definidos llegó a ser ejercitado realmente durante el TLPT?
    - [ ] <25%.
    - [ ] 25–50%.
    - [ ] 51–75%.
    - [ ] >75%.

### 3.2 Ejecución del Red Team

16. Duración de la fase activa de Red Team (en semanas)[web:16][web:34]
    - [ ] <8 semanas.
    - [ ] 8–11 semanas.
    - [ ] ≥12 semanas (alineado con la duración de referencia del RTS TLPT).
    - [ ] >16 semanas (ejercicio largo y épico).

17. ¿Cómo describiría el nivel de realismo de las tácticas, técnicas y procedimientos (TTP) utilizados por el Red Team?
    - [ ] Básico (tácticas genéricas, tipo “curso de ética hacker nivel 1”).
    - [ ] Intermedio (mezcla de técnicas estándar con algunos escenarios ad hoc).
    - [ ] Alto (TTP mapeadas a amenazas reales observadas en el sector y a MITRE ATT&CK).
    - [ ] Muy alto (uso de TTP avanzadas, living‑off‑the‑land, simulación de adversarios específicos).

18. Grado de intervención del White Team durante la prueba (ayudas, bypasses, accesos directos)
    - [ ] Mínimo; casi todo el mérito o el desastre es atribuible al Red Team y al Blue Team.
    - [ ] Moderado; se concedieron algunas ayudas para evitar impactos excesivos.
    - [ ] Alto; el ejercicio habría fracasado sin intervención frecuente del White Team.

---

## 4. Detección, respuesta y continuidad (indicadores operativos)

### 4.1 Detección (MTTD y cobertura)

19. Frente a las actividades ofensivas del TLPT, ¿en cuánto tiempo medio se produjo la detección inicial (MTTD)?
    - [ ] No se detectó nada hasta que el White Team lo explicó en el informe.
    - [ ] Más de 7 días.
    - [ ] Entre 24 horas y 7 días.
    - [ ] Menos de 24 horas.
    - [ ] Menos de 4 horas (reflejos de ninja digital).

20. ¿Qué porcentaje aproximado de las acciones del Red Team fueron detectadas por los sistemas de monitorización y el personal operativo?
    - [ ] 0–25% (mucho por hacer).
    - [ ] 26–50%.
    - [ ] 51–75%.
    - [ ] >75% (no está mal para un día en producción).

21. Principales fuentes de detección (marcar todas las que apliquen)
    - [ ] SIEM / SOC propio.
    - [ ] SOC externo / MSSP.
    - [ ] Alertas en herramientas EDR/XDR.
    - [ ] Monitorización de fraude transaccional.
    - [ ] Usuarios internos “sospechosamente atentos”.
    - [ ] Otros: __________

### 4.2 Respuesta y recuperación (MTTC, MTTR)

22. Una vez detectado el ataque, ¿cuánto tiempo medio se tardó en iniciar acciones de contención (MTTC)?
    - [ ] No se llegó a contener durante el ejercicio.
    - [ ] Más de 24 horas.
    - [ ] Entre 4 y 24 horas.
    - [ ] Menos de 4 horas.

23. Tiempo estimado para restablecer la operación normal de los sistemas afectados (MTTR, durante el ejercicio)[web:39]
    - [ ] No se simuló recuperación (foco exclusivamente ofensivo).
    - [ ] Más de 72 horas.
    - [ ] Entre 24 y 72 horas.
    - [ ] Menos de 24 horas.

24. Coordinación entre TLPT y los planes de continuidad de negocio (BCP/DRP)
    - [ ] No se involucró al equipo de continuidad de negocio.
    - [ ] Se informó a BCP/DRP, pero sin escenarios específicos.
    - [ ] Se probaron procedimientos de continuidad vinculados a los escenarios TLPT.
    - [ ] Se obtuvo feedback formal de continuidad para mejorar los planes y ejercicios conjuntos.

---

## 5. Hallazgos, remediación y seguimiento

### 5.1 Severidad y volumen de hallazgos

25. Número aproximado de hallazgos identificados en el último TLPT (agrupado por severidad)
    - [ ] 0–5 hallazgos críticos/altos.
    - [ ] 6–15 hallazgos críticos/altos.
    - [ ] >15 hallazgos críticos/altos.
    - [ ] Preferimos no responder (por pudor estadístico).

26. ¿Cuál fue el porcentaje de hallazgos críticos/altos con plan de remediación aprobado en un plazo ≤ 8 semanas desde la recepción del informe? [web:16]
    - [ ] 0–25%.
    - [ ] 26–50%.
    - [ ] 51–75%.
    - [ ] >75%.

27. ¿Qué porcentaje de hallazgos identificados en el TLPT fueron recurrentes (ya habían sido detectados en ejercicios o auditorías previas)?
    - [ ] 0–10% (aprendemos rápido).
    - [ ] 11–30%.
    - [ ] 31–50%.
    - [ ] >50% (la resiliencia se nos está repitiendo).

### 5.2 Plan de acción, re‑test y attestation

28. ¿Existe un plan de remediación formal, priorizado y aprobado por el órgano competente para los hallazgos TLPT?
    - [ ] No; cada equipo gestiona “su parte” como puede.
    - [ ] Sí, pero sin priorización explícita por criticidad.
    - [ ] Sí, priorizado por riesgo y con plazos definidos.
    - [ ] Sí, priorizado, con responsables asignados y seguimiento periódico en comité de riesgos.

29. Nivel de avance en la ejecución del plan de remediación del último TLPT
    - [ ] <25% de acciones completadas.
    - [ ] 26–50%.
    - [ ] 51–75%.
    - [ ] >75%.
    - [ ] Completado y verificado mediante re‑test.

30. ¿Se ha realizado un re‑test formal (o ejercicio complementario) para verificar la remediación de los hallazgos TLPT más críticos?
    - [ ] No, confiamos en la documentación.
    - [ ] Sí, de forma parcial, sobre algunos hallazgos.
    - [ ] Sí, re‑test completo sobre hallazgos críticos/altos.
    - [ ] Sí, con evidencia consolidada para supervisores y auditores.

31. ¿La entidad ha recibido la attestation TLPT de la autoridad competente (TIBER-ES / TLPT Authority) para el último ejercicio realizado?[web:16][web:38]
    - [ ] No aplica (aún no hemos realizado TLPT).
    - [ ] No, está en curso de revisión.
    - [ ] Sí, con observaciones menores.
    - [ ] Sí, sin observaciones significativas.

---

## 6. Frecuencia, planificación y cobertura multianual

32. La organización realiza TLPT:
    - [ ] Nunca, por el momento.
    - [ ] De forma ad hoc (tras incidentes o exigencias puntuales).
    - [ ] Según un ciclo formal (al menos una vez cada 3 años, conforme a DORA).[web:36][web:39]
    - [ ] Con mayor frecuencia que la mínima regulatoria, integrando TLPT en un programa continuo de pruebas adversariales.

33. ¿Existe un plan plurianual de ejercicios avanzados (TLPT, TIBER-ES, Red Team internos, tabletop) alineado con el marco DORA de pruebas de resiliencia digital?[web:24][web:26]
    - [ ] No.
    - [ ] Sí, pero sin vínculo explícito con DORA.
    - [ ] Sí, alineado con DORA, aprobado y financiado.
    - [ ] Sí, y se revisa anualmente en función de incidentes, cambios en la organización y nuevas amenazas.

---

## 7. Gobernanza, cultura y madurez

34. ¿Cómo describiría el nivel de cultura interna respecto a TLPT y ciberresiliencia?
    - [ ] Se percibe como una molestia normativa inevitable.
    - [ ] Se considera útil, pero difícil de integrar con el negocio.
    - [ ] Se ve como herramienta clave para priorizar inversiones y proyectos.
    - [ ] Es parte del ADN de la organización; hablamos de resiliencia tanto como de rentabilidad.

35. Impacto percibido de los resultados TLPT en el presupuesto de ciberseguridad y continuidad
    - [ ] Nulo; el presupuesto ya estaba congelado.
    - [ ] Moderado; se aprobaron algunas acciones urgentes.
    - [ ] Significativo; el TLPT redefinió prioridades e inversiones.
    - [ ] Transformador; encaminó un programa de cambio estructural.

36. ¿Existe un cuadro de mando o conjunto de KPI/KRI que recoja sistemáticamente indicadores derivados de TLPT (MTTD, MTTR, número de hallazgos, recurrencia, etc.)?
    - [ ] No.
    - [ ] Sí, pero se usa solo a nivel técnico.
    - [ ] Sí, con reporting periódico a la alta dirección.
    - [ ] Sí, integrado en la gestión global de riesgos operacionales.

37. ¿En qué medida comparte la organización las lecciones aprendidas del TLPT con otras entidades, foros sectoriales o iniciativas coordinadas por supervisores?
    - [ ] No se comparte información (más allá de lo estrictamente obligatorio).
    - [ ] Se participa ocasionalmente en foros.
    - [ ] Se comparten de forma sistemática lecciones agregadas y buenas prácticas.
    - [ ] Se lideran iniciativas sectoriales para mejorar la ciberresiliencia colectiva.

---

## 8. Comentarios abiertos

38. ¿Qué obstáculos principales ha encontrado su organización para implantar TLPT de forma efectiva?  
   Respuesta abierta:  
   _______________________________________________________________________

39. ¿Qué buenas prácticas o innovaciones destacaría en su enfoque de TLPT y ciberresiliencia?  
   Respuesta abierta:  
   _______________________________________________________________________

40. ¿Qué espera de los supervisores y del marco normativo (DORA, TIBER-ES, RTS TLPT) para facilitar un uso más inteligente y eficiente de TLPT?  
   Respuesta abierta:  
   _______________________________________________________________________