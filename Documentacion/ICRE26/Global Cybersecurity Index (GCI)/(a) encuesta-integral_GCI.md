# Modelo de Encuesta Integral de Madurez en Ciberseguridad (Alineada con GCI)

> **Propósito**  
> Esta encuesta pretende evaluar la madurez de tu organización en ciberseguridad siguiendo la lógica de los cinco pilares del Global Cybersecurity Index (GCI) de la UIT: medidas **jurídicas**, **técnicas**, **organizativas**, de **desarrollo de capacidades** y de **cooperación**.[web:28][web:33]  
> Tu sinceridad es oro; el maquillaje es para los informes públicos, no para las mejoras internas.

---

## 0. Datos generales de la organización

### 0.1. Perfil básico

1. Tamaño de la organización (personas empleadas)
   - [ ] Micro (1–9)
   - [ ] Pequeña (10–49)
   - [ ] Mediana (50–249)
   - [ ] Grande (250–999)
   - [ ] Muy grande (≥ 1.000)

2. Sector principal de actividad (selecciona el más relevante)
   - [ ] Administración pública
   - [ ] Salud
   - [ ] Energía
   - [ ] Agua y medio ambiente
   - [ ] Transporte y logística
   - [ ] Finanzas y seguros
   - [ ] Industria / manufactura
   - [ ] TIC / servicios digitales
   - [ ] Educación / investigación
   - [ ] Otros (especificar): __________

3. Localización principal
   - [ ] España – ámbito nacional
   - [ ] España – principalmente autonómico / local
   - [ ] Multinacional con presencia significativa en España

4. ¿La organización está sujeta a alguna de estas normativas/figuras?
   - [ ] NIS2 (operador esencial / importante)
   - [ ] ENS (Esquema Nacional de Seguridad)
   - [ ] RGPD / LOPD‑GDD
   - [ ] Sector financiero (EBA, DORA, etc.)
   - [ ] Otros marcos (ISO 27001, NIST CSF, etc.)

5. Rol de la persona que responde
   - [ ] CISO / Responsable de Seguridad de la Información
   - [ ] CIO / CTO / Director de Tecnología
   - [ ] Responsable de Cumplimiento / Legal
   - [ ] Responsable de Operaciones / Riesgos
   - [ ] Otro (especificar): __________

---

## 1. Pilar Jurídico (Legal)

> Aquí miramos si tu organización vive en el siglo XXI jurídico o sigue en la edad de piedra digital.

### 1.1. Cumplimiento normativo general

1. ¿Existe un inventario actualizado de normativas aplicables en materia de ciberseguridad y protección de datos?
   - [ ] No existe
   - [ ] Existe de forma informal (documentos dispersos, no sistemático)
   - [ ] Existe formalmente, pero se revisa de manera esporádica
   - [ ] Existe, se revisa al menos anualmente
   - [ ] Existe, se revisa periódicamente y se vincula a un mapa de riesgos

2. ¿Se ha realizado en los últimos 24 meses un análisis de brechas de cumplimiento (gap analysis) frente a las normativas aplicables?
   - [ ] No
   - [ ] Sí, de manera parcial o puntual
   - [ ] Sí, completo pero sin plan formal de remediación
   - [ ] Sí, completo y con plan de remediación en marcha
   - [ ] Sí, y se monitoriza el avance con indicadores y reporte periódico

3. ¿Cuál es el nivel de integración entre cumplimiento de protección de datos y ciberseguridad?
   - [ ] Independientes, casi sin interacción
   - [ ] Coordinación esporádica (reuniones ad hoc)
   - [ ] Coordinación frecuente (reuniones periódicas y proyectos conjuntos)
   - [ ] Integración alta (modelo de gobierno común, KPIs compartidos)

### 1.2. Ciberdelito, evidencia digital y contratos

4. ¿Se han definido procedimientos internos para la preservación de evidencias digitales ante incidentes?
   - [ ] No, se improvisa según el caso
   - [ ] Sí, pero no están documentados
   - [ ] Sí, documentados pero poco conocidos
   - [ ] Sí, documentados, conocidos y probados en simulacros

5. ¿Los contratos con proveedores TIC y de nube incluyen cláusulas específicas de ciberseguridad (SLAs de seguridad, notificación de incidentes, auditorías)?
   - [ ] No lo sabemos / no se revisa
   - [ ] Se incluye de forma genérica, sin requisitos medibles
   - [ ] Se incluyen requisitos básicos (cifrado, backups, notificación de incidentes)
   - [ ] Se incluyen requisitos avanzados (pruebas, auditorías, métricas)
   - [ ] Existe un marco estándar de cláusulas de ciberseguridad aplicado de forma sistemática

6. ¿Se ha formado al equipo jurídico / compras en aspectos de ciberseguridad contractual?
   - [ ] No
   - [ ] Formación puntual o informal
   - [ ] Programa formativo estructurado y recurrente

---

## 2. Pilar Técnico (Technical)

> Ahora hablamos de máquinas, cables, logs y esa sensación de que el SIEM canta más que un canario en primavera.

### 2.1. Inventario de activos y arquitectura

1. ¿Existe un inventario actualizado de activos de información (hardware, software, datos, servicios en nube)?
   - [ ] No existe
   - [ ] Existe, pero desactualizado (> 12 meses)
   - [ ] Existe y se actualiza al menos anualmente
   - [ ] Existe y se actualiza de forma continua/automatizada

2. ¿Cómo describirías la segmentación de red y el enfoque Zero Trust?
   - [ ] Red plana, confianza casi ilimitada en la red interna
   - [ ] Segmentación básica (por zonas o VLAN) sin políticas granulares
   - [ ] Segmentación media con controles por tipo de servicio / usuario
   - [ ] Principios de Zero Trust parcialmente implantados (MFA, micro‑segmentación en áreas críticas)
   - [ ] Modelo Zero Trust definido y desplegado de forma sistemática

3. ¿Se dispone de un inventario de servicios en nube (SaaS, PaaS, IaaS) aprobado y gobernado?
   - [ ] No, uso de nube mayoritariamente “sombra”
   - [ ] Parcialmente, con inventarios manuales
   - [ ] Sí, inventario formal, con evaluación de riesgos y clasificación de servicios

### 2.2. Protección, detección y respuesta

4. ¿Qué capacidades de monitorización y detección tiene la organización?
   - [ ] Protección básica (antivirus, firewall perimetral) sin monitorización centralizada
   - [ ] Monitorización limitada (logs en algunos sistemas críticos)
   - [ ] SIEM/SOC parcial (solo sistemas clave)
   - [ ] SOC interno / externo que cubre la mayoría de activos críticos
   - [ ] SOC maduro 24x7 con casos de uso avanzados (detección de comportamiento, UEBA, etc.)

5. ¿Se usan tecnologías de automatización (SOAR, scripts, playbooks) para la respuesta a incidentes?
   - [ ] No
   - [ ] Sí, de forma experimental o para algunos casos concretos
   - [ ] Sí, integrado en procesos estándar de respuesta

6. ¿Qué cobertura de copias de seguridad existe para datos críticos?
   - [ ] Copias manuales o esporádicas
   - [ ] Copias regulares, pero sin pruebas de restauración
   - [ ] Copias regulares con pruebas de restauración puntuales
   - [ ] Estrategia 3‑2‑1 (o equivalente), con pruebas de restauración periódicas documentadas

### 2.3. OT/ICS y tecnologías emergentes

7. ¿La organización opera sistemas OT/ICS (plantas industriales, energía, transporte, etc.)?
   - [ ] No aplica
   - [ ] Sí, pero sin medidas específicas de ciberseguridad OT
   - [ ] Sí, con medidas básicas y revisión periódica
   - [ ] Sí, con arquitectura OT segmentada, políticas específicas y auditorías periódicas

8. Respecto al uso de Inteligencia Artificial y analítica avanzada:
   - [ ] No se utiliza IA de forma relevante
   - [ ] Se utilizan casos aislados sin evaluación de riesgos específica
   - [ ] Existe un inventario y evaluación de riesgos de casos de uso de IA
   - [ ] Existe un marco de gobernanza de IA (políticas, controles, revisión periódica)

---

## 3. Pilar Organizativo (Organizational)

> Aquí miramos si la ciberseguridad tiene silla en la mesa… o si se conforma con una taburete al fondo.

### 3.1. Estrategia y gobierno

1. ¿Existe una estrategia o plan director de ciberseguridad alineado con la estrategia de negocio?
   - [ ] No
   - [ ] Sí, pero informal / no aprobado
   - [ ] Sí, formalmente aprobado, pero poco conocido
   - [ ] Sí, aprobado, comunicado y revisado al menos cada 2–3 años

2. ¿Quién es el máximo responsable de ciberseguridad?
   - [ ] No hay una figura definida
   - [ ] Responsable de TI con rol parcial en seguridad
   - [ ] CISO / Responsable de Seguridad reportando a TI
   - [ ] CISO / Responsable de Seguridad reportando a dirección general / consejo

3. Frecuencia de reporte de ciberseguridad al máximo órgano de gobierno (dirección, consejo, patronato)
   - [ ] Nunca o solo ante incidentes graves
   - [ ] Al menos una vez al año
   - [ ] Varias veces al año (trimestral o superior)
   - [ ] Existe un cuadro de mando periódico con indicadores de riesgos, incidentes, inversiones y ROI

### 3.2. Gestión de riesgos y continuidad

4. ¿Se integra la ciberseguridad en el marco de gestión de riesgos corporativos?
   - [ ] No, se trata como asunto técnico aislado
   - [ ] Identificación básica de riesgos TIC
   - [ ] Mapa de riesgos de ciberseguridad con priorización básica
   - [ ] Mapa de riesgos integrado con riesgos operativos y financieros

5. ¿Existen planes de continuidad de negocio (BCP) y recuperación ante desastres (DRP) que incluyan escenarios de ciberincidente?
   - [ ] No
   - [ ] Sí, pero sin pruebas específicas de ciberincidentes
   - [ ] Sí, con pruebas parciales (ejercicios de escritorio, pruebas técnicas limitadas)
   - [ ] Sí, con ejercicios regulares, incluyendo simulacros integrales con negocio

6. ¿Cuál es el nivel de formalización del proceso de gestión de incidentes?
   - [ ] No existe proceso definido
   - [ ] Proceso informal, sin documentación
   - [ ] Proceso documentado, conocido por el equipo de TI
   - [ ] Proceso documentado, conocido por las áreas de negocio relevantes, probado en simulacros

---

## 4. Pilar Desarrollo de Capacidades (Capacity Development)

> Sin personas formadas, la mejor tecnología es solo decoración cara.

### 4.1. Formación y concienciación

1. ¿Existe un programa formal de formación en ciberseguridad para empleados?
   - [ ] No
   - [ ] Sesiones puntuales o “charlas” ocasionales
   - [ ] Programa anual básico (e‑learning, comunicaciones, etc.)
   - [ ] Programa estructurado por perfiles (dirección, TI, negocio, usuarios privilegiados)

2. ¿Se realizan campañas de concienciación y simulacros de phishing u otros ataques de ingeniería social?
   - [ ] No
   - [ ] Sí, de forma esporádica
   - [ ] Sí, de forma regular, con métricas y planes de mejora

3. ¿Existe formación específica para el equipo directivo y el consejo de administración en materia de ciberseguridad y riesgo tecnológico?
   - [ ] No
   - [ ] Sí, ocasional
   - [ ] Sí, se realiza al menos una vez al año

### 4.2. Talento y recursos

4. ¿Cómo describirías el dimensionamiento del equipo de ciberseguridad?
   - [ ] No existe equipo dedicado
   - [ ] 1–2 personas con rol parcial
   - [ ] Equipo pequeño dedicado (3–5 personas)
   - [ ] Equipo dedicado y multidisciplinar (> 5 personas)

5. ¿Cuál es el nivel de subcontratación de servicios de ciberseguridad?
   - [ ] Nulo o residual
   - [ ] Moderado (servicios específicos: auditoría, pentest, etc.)
   - [ ] Elevado (SOC, respuesta a incidentes, consultoría recurrente)
   - [ ] Modelo híbrido bien definido y gobernado

6. ¿La organización dispone de un plan de desarrollo profesional y certificaciones para perfiles de ciberseguridad?
   - [ ] No
   - [ ] Apoyo ad hoc, según presupuesto y demanda
   - [ ] Plan estructurado con objetivos y presupuesto anual

---

## 5. Pilar Cooperación (Cooperation)

> La ciberseguridad es un deporte de equipo; jugar en solitario solo impresiona a los atacantes.

### 5.1. Cooperación externa

1. ¿La organización participa en redes o foros sectoriales de ciberseguridad?
   - [ ] No
   - [ ] Sí, con participación ocasional
   - [ ] Sí, con participación activa (grupos de trabajo, proyectos)

2. ¿Se comparte información sobre incidentes y amenazas con terceros de confianza (CSIRT, asociaciones, organismos públicos)?
   - [ ] No, solo se gestiona internamente
   - [ ] Sí, pero de forma limitada
   - [ ] Sí, de forma sistemática, con acuerdos y canales establecidos

3. ¿Se han realizado ejercicios conjuntos (ej. con proveedores críticos, clientes clave, autoridades) de gestión de ciberincidentes?
   - [ ] No
   - [ ] Sí, ejercicios puntuales
   - [ ] Sí, ejercicios regulares con lecciones aprendidas documentadas

### 5.2. Cooperación interna

4. ¿Cómo valorarías la colaboración entre las áreas de TI, ciberseguridad, negocio y legal?
   - [ ] Fragmentada, cada uno con su agenda
   - [ ] Colaboración básica en proyectos puntuales
   - [ ] Colaboración estructurada (comités, canales formales, proyectos transversales)
   - [ ] Cultura de colaboración madura, con objetivos compartidos y co‑responsabilidad

---

## 6. Inversión, ROI y percepción de riesgo

> Aquí entramos en la parte delicada: el dinero, esa métrica universal del cariño empresarial.

1. ¿Qué porcentaje aproximado del presupuesto de TI se destina a ciberseguridad?
   - [ ] < 5 %
   - [ ] 5–10 %
   - [ ] 10–20 %
   - [ ] > 20 %
   - [ ] No se dispone del dato

2. ¿Cómo ha evolucionado el presupuesto de ciberseguridad en los últimos 3 años?
   - [ ] Ha disminuido
   - [ ] Se ha mantenido estable
   - [ ] Ha aumentado moderadamente (< 20 % acumulado)
   - [ ] Ha aumentado de forma significativa (≥ 20 % acumulado)

3. ¿Se evalúa el retorno de la inversión (ROI) o valor generado por la ciberseguridad?
   - [ ] No, se considera coste necesario
   - [ ] Sí, de forma cualitativa (reducción de riesgos, cumplimiento)
   - [ ] Sí, con métricas cuantitativas (pérdidas evitadas, reducción de incidentes, mejora de disponibilidad)

4. En una escala del 1 al 5, ¿cuál es la percepción de la dirección sobre la criticidad de la ciberseguridad para el negocio?
   - [ ] 1 – Tema técnico secundario
   - [ ] 2 – Importante, pero no prioritario
   - [ ] 3 – Uno más de los riesgos relevantes
   - [ ] 4 – Factor crítico para la continuidad
   - [ ] 5 – Factor estratégico y diferenciador

---

## 7. Comentarios cualitativos

> Espacio para que la realidad matice los checkboxes.

1. Principales retos de ciberseguridad que ve su organización en los próximos 2–3 años:  
   _Respuesta abierta_

2. Tres cambios que más ayudarían a mejorar la ciberseguridad en su organización:  
   _Respuesta abierta_