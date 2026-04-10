# Marco integrativo GQM + PRAGMATIC para indicadores Zero Trust

## 1. Introducción

Este documento define un marco integrativo que combina la metodología Goal-Question-Metric (GQM) con los criterios PRAGMATIC para evaluar y gobernar los indicadores de madurez Zero Trust a nivel organizativo y nacional (por ejemplo, en España bajo ENS, NIS2, DORA y la estrategia de Década Digital). [web:51][web:47]

- GQM asegura la trazabilidad desde los objetivos estratégicos (Goal), pasando por preguntas evaluativas (Question), hasta métricas concretas (Metric). [web:53]
- PRAGMATIC (Predictivo, Relevante, Accionable, Genuino, Significativo, Preciso, Oportuno, Independiente y Rentable) proporciona un marco para evaluar la calidad de cada métrica. [web:53]

El resultado es un sistema de indicadores Zero Trust que no solo mide, sino que anticipa, guía decisiones y resiste auditorías serias.

## 2. Estructura general del marco GQM

### 2.1. Niveles de objetivos

Se definen tres niveles de objetivos:

- **Nivel 1 – Objetivos nacionales y regulatorios**: alineados con estrategias de país (Agenda España Digital 2025, Década Digital UE, Estrategia Nacional de Ciberseguridad, ENS, NIS2, DORA, RGPD). [web:47][web:52][web:53]
- **Nivel 2 – Objetivos organizativos**: propios de ministerios, agencias, operadores de servicios esenciales, grandes empresas, etc.
- **Nivel 3 – Objetivos técnicos / operativos**: derivados de los pilares Zero Trust (identidad, dispositivos, red, aplicaciones, datos, monitorización y resiliencia). [web:51][web:49]

### 2.2. Plantilla GQM genérica

Para cada objetivo (G), se formulan una o varias preguntas (Q) que explicitan cómo sabremos si el objetivo se cumple, y se asocian métricas (M) que permiten responder cuantitativamente a esas preguntas.

- **Goal (G)**: Formalmente, enunciar el objetivo con estructura: *Analizar/controlar [objeto] con el propósito de [motivo] desde el punto de vista de [stakeholder] en el contexto de [entorno]*.
- **Question (Q)**: Preguntas que operacionalizan el objetivo.
- **Metric (M)**: Datos cuantitativos o cualitativos estructurados que responden a las preguntas.

## 3. Ejemplos GQM por pilar Zero Trust

A continuación se presentan ejemplos de GQM para los indicadores clave mencionados en el informe de indicadores Zero Trust.

### 3.1. Pilar Identidad y Acceso

**Objetivo G1 (nacional/organizativo)**  
Analizar el nivel de protección de identidades con el propósito de reducir el riesgo de compromiso de cuentas y accesos no autorizados, desde el punto de vista de la autoridad nacional de ciberseguridad y de los CISOs, en el contexto de organizaciones sujetas a NIS2 y ENS.

**Preguntas (Q)**  
Q1.1. ¿En qué medida los usuarios que acceden a sistemas críticos están protegidos mediante MFA fuerte?  
Q1.2. ¿En qué medida se aplica el principio de mínimo privilegio de forma sistemática y auditable?  
Q1.3. ¿En qué medida las cuentas privilegiadas se gestionan con controles reforzados (PAM, JIT, auditoría)?  
Q1.4. ¿Hasta qué punto se monitorizan y detectan comportamientos anómalos de acceso (UEBA, analítica de riesgo)?

**Métricas (M)**  
M1.1. Porcentaje de usuarios con MFA habilitado en sistemas críticos.  
M1.2. Porcentaje de cuentas con permisos revisados al menos una vez al año.  
M1.3. Porcentaje de cuentas privilegiadas gestionadas a través de un sistema PAM.  
M1.4. Número de incidentes de acceso anómalo detectados y gestionados por UEBA / sistemas equivalentes, por trimestre.

### 3.2. Pilar Dispositivos y Endpoints

**Objetivo G2**  
Controlar la postura de seguridad de dispositivos con el propósito de reducir la superficie de ataque y el riesgo de explotación de vulnerabilidades, desde el punto de vista de responsables de seguridad y reguladores, en el contexto de entornos híbridos TI/OT.

**Preguntas**  
Q2.1. ¿Qué porcentaje de dispositivos está gestionado e inventariado?  
Q2.2. ¿Cuál es el tiempo medio para aplicar parches críticos?  
Q2.3. ¿Qué grado de cobertura tienen las soluciones EDR/XDR?  
Q2.4. ¿Cómo se controla el riesgo de dispositivos no gestionados (BYOD, terceros)?

**Métricas**  
M2.1. % de dispositivos inventariados con agente de gestión activo.  
M2.2. Tiempo medio (días) desde la publicación de un parche crítico hasta su despliegue en ≥ 90 % de dispositivos afectados.  
M2.3. % de endpoints con EDR/XDR activo y actualizado.  
M2.4. Ratio de dispositivos no gestionados detectados por cada 1.000 usuarios.

### 3.3. Pilar Red, ZTNA y Microsegmentación

**Objetivo G3**  
Controlar la exposición y el movimiento lateral en redes con el propósito de limitar el impacto de intrusiones, desde el punto de vista de operadores de servicios esenciales y CERT nacionales, en el contexto de redes híbridas y acceso remoto.

**Preguntas**  
Q3.1. ¿Qué proporción del tráfico interno se inspecciona a nivel de aplicación (L7)?  
Q3.2. ¿En qué medida se ha adoptado ZTNA frente a VPN tradicionales?  
Q3.3. ¿En qué grado existe segmentación y microsegmentación coherente con Zero Trust?  
Q3.4. ¿Qué capacidad existe para detectar y bloquear movimientos laterales?

**Métricas**  
M3.1. % de tráfico interno que pasa por proxies / firewalls de inspección L7.  
M3.2. % de accesos remotos a aplicaciones críticas realizados a través de ZTNA vs. VPN.  
M3.3. Número medio de segmentos/microsegmentos por aplicación crítica.  
M3.4. Número de intentos de movimiento lateral detectados y bloqueados por periodo.

### 3.4. Pilar Aplicaciones, Nube y Cargas de Trabajo

**Objetivo G4**  
Analizar la seguridad de aplicaciones y cargas de trabajo para reducir vulnerabilidades explotables y accesos indebidos, desde el punto de vista de equipos DevSecOps y reguladores, en el contexto de entornos multicloud/híbridos.

**Preguntas**  
Q4.1. ¿Qué porcentaje de nuevas aplicaciones se desarrolla siguiendo principios Zero Trust by design?  
Q4.2. ¿Cómo se gestionan las identidades de servicios y APIs?  
Q4.3. ¿Qué tan rápida es la respuesta ante incidentes en la nube?  
Q4.4. ¿Hasta qué punto están protegidas las APIs expuestas?

**Métricas**  
M4.1. % de nuevas aplicaciones con autenticación fuerte, autorización granular y logging exhaustivo documentado.  
M4.2. % de secretos de aplicaciones/servicios gestionados en vault con rotación automática.  
M4.3. MTTR (horas) en incidentes de seguridad cloud.  
M4.4. % de APIs críticas protegidas por gateway con controles (auth, rate limiting, WAF, analítica).

### 3.5. Pilar Datos y Protección de la Información

**Objetivo G5**  
Proteger la confidencialidad e integridad de datos sensibles con el propósito de reducir fugas y uso indebido, desde el punto de vista de reguladores (RGPD, NIS2) y responsables de negocio, en el contexto de ecosistemas altamente digitalizados.

**Preguntas**  
Q5.1. ¿Existe y se aplica un esquema de clasificación de la información?  
Q5.2. ¿Qué porcentaje de datos sensibles tiene controles de acceso contexto-sensibles?  
Q5.3. ¿Hasta qué punto se controlan y previenen exfiltraciones de datos?  
Q5.4. ¿Se monitoriza el acceso a datos sensibles con suficiente granularidad?

**Métricas**  
M5.1. % de activos de información clasificados según un esquema formal.  
M5.2. % de repositorios de datos sensibles protegidos con controles de acceso basados en contexto.  
M5.3. Número de incidentes de exfiltración detectados vs. intentos bloqueados (ratio).  
M5.4. % de accesos a datos sensibles registrados y correlacionados en el SIEM.

### 3.6. Monitorización, Resiliencia y Continuidad

**Objetivo G6**  
Asegurar capacidades de detección, respuesta y continuidad alineadas con Zero Trust, con el propósito de minimizar el tiempo e impacto de los incidentes, desde el punto de vista de CISOs, CERTs y órganos de supervisión.

**Preguntas**  
Q6.1. ¿Qué grado de monitorización centralizada existe (SIEM/UEBA/SOAR)?  
Q6.2. ¿Cuál es el MTTD real para incidentes significativos?  
Q6.3. ¿Cuál es el MTTR de contención y recuperación?  
Q6.4. ¿En qué medida los planes de continuidad incorporan segmentación y controles Zero Trust?  
Q6.5. ¿Con qué frecuencia se realizan simulacros de ciberincidentes?

**Métricas**  
M6.1. % de sistemas críticos integrados en SIEM/monitorización centralizada.  
M6.2. MTTD (días) para incidentes significativos.  
M6.3. MTTR (horas) de contención y restauración de servicios críticos.  
M6.4. % de procesos críticos con procedimientos de aislamiento/microsegmentación documentados.  
M6.5. Nº de simulacros de ciberincidentes realizados al año.

## 4. Aplicación de los criterios PRAGMATIC

Cada métrica se evalúa según los nueve criterios PRAGMATIC, normalmente con una escala 0–3:  
0 = No cumple, 1 = Cumplimiento bajo, 2 = Cumplimiento moderado, 3 = Cumplimiento alto.

- **P – Predictivo**: ¿La métrica ayuda a anticipar resultados futuros (incidentes, brechas, impacto)?  
- **R – Relevante**: ¿Es importante para los objetivos y las decisiones reales de los stakeholders?  
- **A – Accionable**: ¿Sugerirá acciones concretas cuando cambie el valor?  
- **G – Genuino**: ¿Refleja la realidad o se puede “maquillar” fácilmente?  
- **M – Significativo (Meaningful)**: ¿Es comprensible y significativo para quienes deben usarla?  
- **P – Preciso**: ¿Se puede medir con exactitud y consistencia?  
- **T – Oportuno (Timely)**: ¿Se puede obtener con la frecuencia necesaria?  
- **I – Independiente**: ¿No está excesivamente correlacionada con otras métricas (no duplica)?  
- **C – Rentable (Cost-effective)**: ¿Su coste de medición es razonable frente a su utilidad?

En la matriz PRAGMATIC (documento separado) se asigna una puntuación por criterio a las métricas clave de cada pilar.

## 5. Ejemplo de ficha GQM + PRAGMATIC por métrica

Ejemplo: **M1.1 – % de usuarios con MFA en sistemas críticos**

- **Goal**: Reducir la probabilidad de compromiso de cuentas críticas.  
- **Question**: ¿Qué proporción de usuarios de sistemas críticos está protegida mediante MFA robusto?  
- **Metric**: Número de usuarios con MFA habilitado / número total de usuarios de sistemas críticos × 100.

Evaluación PRAGMATIC (ejemplo orientativo):

| Criterio     | Pregunta orientadora                                     | Puntuación (0–3) | Comentario breve |
|--------------|-----------------------------------------------------------|------------------|------------------|
| Predictivo   | ¿Anticipa riesgo futuro de compromiso de cuentas?        | 3                | Fuerte predictor de phishing exitoso. |
| Relevante    | ¿Es clave para ENS, NIS2, buenas prácticas?              | 3                | Altamente alineado con marcos. |
| Accionable   | ¿Sugiere acciones claras (desplegar MFA)?                | 3                | Elevar cobertura MFA. |
| Genuino      | ¿Refleja realidad sin incentivos para maquillarla?       | 2                | Puede inflarse si se habilita MFA pero no se aplica bien. |
| Significativo| ¿Lo entienden dirección y técnicos?                      | 3                | Métrica simple e intuitiva. |
| Preciso      | ¿Se puede medir con exactitud?                           | 3                | Datos de IAM centralizado. |
| Oportuno     | ¿Se puede obtener con frecuencia adecuada?               | 3                | Consultas periódicas a IAM. |
| Independiente| ¿Aporta info distinta de otras métricas?                 | 2                | Correlaciona con madurez IAM, pero aporta valor propio. |
| Rentable     | ¿Su obtención es barata?                                 | 3                | Bajo coste una vez montado el reporte. |

La suma (o media) de estas puntuaciones ayuda a priorizar métricas en cuadros de mando nacionales y organizativos.

## 6. Uso del marco a nivel nacional

- Traducir los objetivos nacionales (estrategias de ciberseguridad, planes de digitalización) a objetivos GQM por pilar. [web:47][web:53]  
- Mapear las preguntas de la encuesta de madurez Zero Trust a estos objetivos y métricas.  
- Evaluar las métricas candidatas con PRAGMATIC para seleccionar un subconjunto “estrella” para reporting nacional (por ejemplo, 10–20 KPIs clave). [web:6][web:41]  
- Establecer umbrales objetivo (targets) por sector y tipo de entidad.

## 7. Próximos pasos

- Afinar la lista de métricas por sector (sanidad, energía, finanzas, administración pública, industria).  
- Validar el modelo GQM + PRAGMATIC con un panel de expertos (CISOs, reguladores, aseguradoras).  
- Integrar los resultados en cuadros de mando nacionales y sectoriales, con revisiones anuales.