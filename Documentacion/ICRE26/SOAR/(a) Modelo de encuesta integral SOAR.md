# Encuesta Nacional SOAR – Modelo Integral para Responsables de Ciberseguridad

> Encuesta dirigida a CISO, responsables de SOC, continuidad de negocio y riesgo operativo.
> Objetivo: comprender el grado de adopción real de orquestación, automatización y respuesta (SOAR) y su impacto en indicadores clave a nivel organizativo y, por extensión, territorial.

---

## 0. Información general de la organización

1. **Tipo de organización**
   - [ ] Administración pública
   - [ ] Empresa privada – gran empresa (> 250 empleados)
   - [ ] Empresa privada – pyme
   - [ ] Operador de servicios esenciales (NIS2)
   - [ ] Proveedor de servicios digitales (NIS2)
   - [ ] Otro (especifique): _________

2. **Sector principal de actividad**
   - [ ] Energía
   - [ ] Transporte
   - [ ] Banca y servicios financieros
   - [ ] Sanidad
   - [ ] Industria / manufactura
   - [ ] Telecomunicaciones / 5G
   - [ ] Administración local / autonómica
   - [ ] Educación / I+D
   - [ ] Otros (especifique): _________

3. **Tamaño aproximado (personas empleadas)**
   - [ ] Menos de 50
   - [ ] 50–249
   - [ ] 250–999
   - [ ] 1.000–4.999
   - [ ] 5.000 o más

4. **¿Está su organización sujeta a NIS2 o ENS?**
   - [ ] NIS2
   - [ ] ENS (Esquema Nacional de Seguridad)
   - [ ] Ambas
   - [ ] Ninguna / en proceso de evaluación

---

## 1. Estrategia y gobierno de SOAR

5. **Situación actual de capacidades SOAR**
   - [ ] No disponemos de plataforma SOAR ni capacidades equivalentes.
   - [ ] Utilizamos scripts / automatizaciones ad hoc, sin plataforma SOAR formal.
   - [ ] Tenemos una plataforma SOAR en producción, limitada a unos pocos casos de uso.
   - [ ] Tenemos una plataforma SOAR en producción, con uso extendido en el SOC.
   - [ ] Disponemos de múltiples soluciones SOAR / automatización integradas.

6. **Propósito estratégico principal de SOAR en su organización**
   - [ ] Reducir tiempos de detección y respuesta (MTTD / MTTR).
   - [ ] Gestionar el volumen de alertas del SOC sin aumentar plantilla.
   - [ ] Mejorar el cumplimiento regulatorio (NIS2, ENS, sectorial).
   - [ ] Estándar corporativo global / mandato del grupo matriz.
   - [ ] Otros (especifique): _________

7. **Nivel de formalización del gobierno de SOAR**
   - [ ] No existe comité ni rol específico de gobierno para SOAR.
   - [ ] Roles y responsabilidades definidos informalmente, sin documento formal.
   - [ ] Existe gobierno formal (comité, responsable SOAR) con mandato definido.
   - [ ] Gobierno formal, con objetivos e indicadores SOAR aprobados por dirección.

8. **Existencia de una hoja de ruta SOAR**
   - [ ] No hay hoja de ruta ni plan formal.
   - [ ] Hoja de ruta interna de TI / seguridad, no aprobada por dirección.
   - [ ] Hoja de ruta formal aprobada por dirección de ciberseguridad.
   - [ ] Hoja de ruta integrada en el plan estratégico corporativo.

---

## 2. Modelo operativo de SOC y cobertura de automatización

9. **Modelo de operación del SOC**
   - [ ] No disponemos de SOC.
   - [ ] SOC interno (24x7).
   - [ ] SOC interno (horario ampliado, sin 24x7).
   - [ ] SOC externalizado (MSSP / proveedor).
   - [ ] Modelo híbrido (interno + proveedor).

10. **Cobertura actual de automatización sobre el volumen total de alertas**
    - [ ] 0–10 %
    - [ ] 11–30 %
    - [ ] 31–60 %
    - [ ] 61–90 %
    - [ ] Más del 90 %
    - [ ] No se mide / se desconoce

11. **Cobertura actual de automatización sobre casos de uso priorizados**
    - [ ] No hay casos de uso priorizados formalmente.
    - [ ] 1–3 casos de uso automatizados (p. ej. phishing, malware simple).
    - [ ] 4–10 casos de uso automatizados.
    - [ ] Más de 10 casos de uso automatizados.
    - [ ] Catálogo formal de casos de uso con revisión anual.

12. **Principales casos de uso donde se aplica SOAR (marque todos los que apliquen)**
    - [ ] Triage de alertas de SIEM / EDR.
    - [ ] Gestión de phishing (análisis, bloqueo, concienciación).
    - [ ] Contención de malware / ransomware (aislamiento, bloqueo).
    - [ ] Gestión de credenciales comprometidas / cuentas comprometidas.
    - [ ] Respuesta a vulnerabilidades críticas / parches.
    - [ ] Respuesta ante incidentes OT / ICS.
    - [ ] Notificación automatizada a CNCS, INCIBE u otras autoridades.
    - [ ] Otros (especifique): _________

13. **Integraciones técnicas clave del SOAR**
    - [ ] SIEM
    - [ ] EDR / XDR
    - [ ] IAM / gestión de identidades
    - [ ] Herramientas de ticketing / ITSM
    - [ ] Firewalls / proxies / WAF
    - [ ] Sistemas de correo / MTA
    - [ ] Herramientas de threat intelligence
    - [ ] Sistemas OT / SCADA
    - [ ] No se dispone de integraciones relevantes

---

## 3. Métricas de tiempo: MTTD, MTTC, MTTR

14. **¿Mide formalmente el MTTD (Mean Time to Detect)?**
    - [ ] Sí, de forma continua y con objetivo definido.
    - [ ] Sí, pero sin objetivo formalizado.
    - [ ] No, pero está previsto hacerlo en los próximos 12 meses.
    - [ ] No se mide ni está previsto.

15. **Rango aproximado de MTTD para incidentes de alta criticidad**
    - [ ] Menos de 15 minutos.
    - [ ] Entre 15 minutos y 1 hora.
    - [ ] Entre 1 y 4 horas.
    - [ ] Entre 4 y 24 horas.
    - [ ] Más de 24 horas.
    - [ ] No se dispone de este dato.

16. **¿Mide formalmente el MTTC/MTTI (tiempo medio de clasificación / contención)?**
    - [ ] Sí, de forma continua y con objetivo definido.
    - [ ] Sí, pero sin objetivo formalizado.
    - [ ] No, pero está previsto hacerlo.
    - [ ] No se mide ni está previsto.

17. **Rango aproximado de MTTR (Mean Time to Respond / Restore) para incidentes críticos**
    - [ ] Menos de 4 horas.
    - [ ] Entre 4 y 24 horas.
    - [ ] Entre 1 y 7 días.
    - [ ] Más de 7 días.
    - [ ] No se dispone de este dato.

18. **Impacto percibido de SOAR en MTTD/MTTR**
    - [ ] Disminución > 50 % respecto a la situación previa sin SOAR.
    - [ ] Disminución entre 30–50 %.
    - [ ] Disminución entre 10–30 %.
    - [ ] Mejora marginal (< 10 %) o no medible.
    - [ ] Empeoramiento / aumento de tiempos.
    - [ ] No se ha evaluado.

---

## 4. Métricas de calidad: falsos positivos, re‑aperturas, rollback

19. **¿Mide la tasa de falsos positivos de sus detecciones automatizadas?**
    - [ ] Sí, con revisión periódica.
    - [ ] Sí, pero sin revisión periódica.
    - [ ] No, pero está previsto medirla.
    - [ ] No se mide ni está previsto.

20. **Rango aproximado de falsos positivos sobre el total de alertas tratadas**
    - [ ] Menos del 10 %.
    - [ ] 10–30 %.
    - [ ] 31–60 %.
    - [ ] Más del 60 %.
    - [ ] No se dispone de este dato.

21. **¿Registra incidentes reabiertos tras cierre automático o semiautomático?**
    - [ ] Sí, de forma sistemática.
    - [ ] Sí, pero solo los casos más graves.
    - [ ] No, se gestiona de forma informal.
    - [ ] No se registran.

22. **Porcentaje estimado de incidentes reabiertos sobre el total de incidentes cerrados automáticamente**
    - [ ] Menos del 1 %.
    - [ ] 1–5 %.
    - [ ] 6–15 %.
    - [ ] Más del 15 %.
    - [ ] No se dispone de este dato.

23. **¿Registra y analiza ejecuciones de playbooks que requieren rollback (deshacer acciones)?**
    - [ ] Sí, con métricas y análisis de causa raíz.
    - [ ] Sí, pero sin análisis sistemático.
    - [ ] No, solo se atienden casos puntuales.
    - [ ] No se han producido rollbacks (que sepamos).

24. **Percepción sobre el equilibrio entre automatización y riesgo operativo**
    - [ ] Preferimos automatizar al máximo, aunque ello implique ciertos riesgos.
    - [ ] Aplicamos automatización gradual con controles manuales significativos.
    - [ ] Somos conservadores: sólo automatizamos tareas de bajo impacto.
    - [ ] Aún no hemos definido una postura clara.

---

## 5. Cobertura de casos de uso y catálogo SOAR

25. **¿Dispone de un catálogo formal de casos de uso del SOC / SOAR?**
    - [ ] Sí, con versión aprobada y revisiones periódicas.
    - [ ] Sí, pero no se revisa de forma regular.
    - [ ] Solo existe de forma informal.
    - [ ] No disponemos de catálogo.

26. **Porcentaje de los 10 tipos de incidentes más frecuentes que cuentan con al menos un playbook definido**
    - [ ] 0–20 %
    - [ ] 21–50 %
    - [ ] 51–80 %
    - [ ] 81–100 %
    - [ ] No se conoce / no aplicable.

27. **Frecuencia de revisión y actualización de playbooks**
    - [ ] Mensual o más frecuente.
    - [ ] Trimestral.
    - [ ] Anual.
    - [ ] Ad hoc / reactivo.
    - [ ] No se revisan.

28. **Participación de áreas de negocio en la definición de casos de uso y playbooks**
    - [ ] Alta: participan en la definición, priorización y validación.
    - [ ] Moderada: participan solo en validación.
    - [ ] Baja: participación ocasional o simbólica.
    - [ ] Nula: la definición es exclusivamente técnica.

---

## 6. Regulación, cumplimiento y notificación de incidentes

29. **Obligaciones regulatorias más relevantes para su organización (marque todas las que apliquen)**
    - [ ] NIS2
    - [ ] ENS
    - [ ] RGPD
    - [ ] Regulación sectorial específica (bancaria, sanitaria, etc.)
    - [ ] Otras (especifique): _________

30. **¿Utiliza su plataforma SOAR para apoyar la notificación de incidentes a autoridades (CNCS, INCIBE, regulador sectorial)?**
    - [ ] Sí, la notificación está parcialmente automatizada.
    - [ ] Sí, pero solo se usa SOAR para recopilar la información.
    - [ ] No, el proceso es completamente manual.
    - [ ] No aplicable.

31. **Tiempo promedio estimado para realizar notificación inicial según NIS2 / normativa aplicable**
    - [ ] Menos de 12 horas desde la detección.
    - [ ] Entre 12 y 24 horas.
    - [ ] Entre 24 y 72 horas.
    - [ ] Más de 72 horas.
    - [ ] No se dispone de dato / no aplicable.

32. **¿Dispone de plantillas normalizadas (semi)automatizadas para informes de incidente regulatorios?**
    - [ ] Sí, integradas en la herramienta SOAR o ITSM.
    - [ ] Sí, pero en documentos independientes (sin integración).
    - [ ] No, se redactan caso a caso.
    - [ ] No aplicable.

---

## 7. Métricas de impacto y coste (ROI de SOAR)

33. **¿Estima el coste económico de los incidentes de ciberseguridad?**
    - [ ] Sí, con modelo actuarial o financiero definido.
    - [ ] Sí, pero de forma aproximada / manual.
    - [ ] No, pero está previsto.
    - [ ] No se estima ni se prevé estimarlo.

34. **Componentes considerados en la estimación de coste de incidentes**
    - [ ] Paradas de servicio / pérdida de productividad.
    - [ ] Costes de recuperación técnica.
    - [ ] Multas / sanciones regulatorias.
    - [ ] Costes legales.
    - [ ] Impacto reputacional (estimado).
    - [ ] Otros (especifique): _________
    - [ ] No se desglosan componentes.

35. **¿Calcula el ROI de los proyectos de automatización / SOAR?**
    - [ ] Sí, utilizando un modelo formal (p. ej. reducción de MTTR vs. coste).
    - [ ] Sí, pero de forma cualitativa.
    - [ ] No, pero se está diseñando un modelo.
    - [ ] No se calcula ni está previsto.

36. **Percepción de la dirección sobre el valor de SOAR**
    - [ ] Lo percibe como inversión estratégica imprescindible.
    - [ ] Lo ve como un coste necesario, pero negociable.
    - [ ] Lo considera un gasto accesorio / “nice to have”.
    - [ ] No consta una opinión definida.

---

## 8. Madurez, barreras y planes de futuro

37. **Nivel de madurez percibido en capacidades SOAR**
    - [ ] Inicial: pruebas, pilotos, automatización limitada.
    - [ ] Básico: algunos casos de uso recurrentes automatizados.
    - [ ] Intermedio: catálogo de casos de uso y métricas básicas.
    - [ ] Avanzado: adopción amplia, métricas, revisión continua.
    - [ ] Líder: automatización extendida, IA, métricas robustas y benchmarking.

38. **Principales barreras para la adopción de SOAR**
    - [ ] Falta de presupuesto.
    - [ ] Falta de personal cualificado.
    - [ ] Resistencia cultural / organizativa.
    - [ ] Limitaciones tecnológicas / legado.
    - [ ] Falta de liderazgo / patrocinio ejecutivo.
    - [ ] Falta de claridad en los beneficios.
    - [ ] Otras (especifique): _________

39. **Ámbitos prioritarios para ampliar la automatización en los próximos 2 años**
    - [ ] Detección y triage de alertas.
    - [ ] Respuesta a phishing y fraude.
    - [ ] Respuesta en entornos OT / ICS.
    - [ ] Notificación regulatoria y reporting.
    - [ ] Gestión de vulnerabilidades.
    - [ ] Coordinación con terceros (proveedores, partners, CSIRT nacionales).
    - [ ] Otros (especifique): _________

40. **Uso previsto de IA avanzada / agentes inteligentes en el SOC**
    - [ ] Ya se utilizan para casos concretos (explicar brevemente).
    - [ ] En piloto, con planes de consolidación.
    - [ ] En estudio, sin piloto activo.
    - [ ] No se contempla a corto plazo.

---

## 9. Comentarios abiertos

41. **En una frase: si pudiera pedir un deseo razonable respecto a SOAR en su organización, ¿cuál sería?**  
   _Respuesta abierta_

42. **Observaciones adicionales, anécdotas, éxitos o fracasos sonados en automatización que crea que merecen entrar en la historia oral de la ciberseguridad nacional**  
   _Respuesta abierta_