# 📊 MATRIZ DE EVALUACIÓN PRAGMATIC COMPLETA
## Calificación de las 42 Métricas LINDDUN/LIINE4DU bajo los Nueve Criterios
### Kit GQM + PRAGMATIC · España 2025–2026 · Versión 1.0

---

> *"No basta con elegir la métrica correcta. Hay que saber si la métrica elegida vale lo que cuesta medirla, si predice algo útil y si el decisor sabrá qué hacer con ella al recibirla. Para eso existe PRAGMATIC: el tribunal de calidad de las métricas."*
> — Parafraseando a Brotby & Hinson, *PRAGMATIC Security Metrics*, CRC Press, 2013

---

## INSTRUCCIONES DE LECTURA

Cada métrica se evalúa en **nueve criterios** de 0 a 10:

| Criterio | Símbolo | Pregunta clave |
|----------|---------|----------------|
| **P**redictivo | 🔮 | ¿Predice el estado futuro antes de que el problema ocurra? |
| **R**elevante | 🎯 | ¿Importa directamente a decisores y reguladores? |
| **A**ccionable | ⚡ | ¿Orienta decisiones y acciones concretas y diferenciadas? |
| **G**enuino | 🔬 | ¿Mide el fenómeno real y no un proxy distorsionado? |
| **M**eaningful (Significativo) | 💡 | ¿Es comprensible para técnicos y directivos por igual? |
| **A**ccurate (Preciso) | 📐 | ¿Es exacto, reproducible y con error de medición documentado? |
| **T**imely (Oportuno) | ⏱️ | ¿Los datos llegan con la frecuencia necesaria para decidir? |
| **I**ndependiente | 🛡️ | ¿Es difícil de manipular conscientemente por los sujetos medidos? |
| **C**heap (Rentable) | 💰 | ¿El coste de obtenerla es proporcional a su valor informativo? |

**Puntuación total** = Media aritmética de los 9 criterios (escala 0–10)

**Umbral de calidad mínimo recomendado**: ≥ 6.5 para métricas incluidas en el cuadro de mando

---

## MÓDULO 1 — INDICADOR L (LINKING / VINCULACIÓN)

### Métrica L-M1: % de tratamientos con DFD actualizado

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **7** | Un porcentaje bajo de DFDs actualizados predice riesgo de vinculación no detectada en tratamientos no cartografiados |
| 🎯 Relevante | **9** | Directamente vinculado al Art. 30 RGPD (obligatorio) y al proceso de EIPD; altamente relevante para DPO y auditores |
| ⚡ Accionable | **8** | Un resultado <80% desencadena acción clara: actualizar DFDs del Registro de Actividades; responsable asignable |
| 🔬 Genuino | **7** | Mide la completitud documental real; riesgo de que DFDs existan pero estén desactualizados o sean superficiales |
| 💡 Significativo | **8** | Comprensible para DPO, auditores y CISO; requiere mínima explicación a directivos |
| 📐 Preciso | **8** | Numerador y denominador objetivamente verificables desde el Registro de Actividades |
| ⏱️ Oportuno | **7** | Actualización anual suficiente para el ciclo de cumplimiento; frecuencia adecuada al ciclo de riesgo |
| 🛡️ Independiente | **6** | Posibilidad de "inflado" de DFDs sin calidad real; mitigable con auditoría de contenido |
| 💰 Rentable | **9** | Coste bajo: revisión del Registro de Actividades existente; alto valor de cumplimiento |
| **TOTAL** | **7.67** | ⭐⭐ **Buena** — Implementar con prioridad |

---

### Métrica L-M2: Tasa de quasi-identificadores no controlados

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **8** | Predice directamente el riesgo de re-identificación por cruce de datos; indicador de riesgo latente |
| 🎯 Relevante | **9** | Central para el cumplimiento del Art. 25 RGPD (Privacy by Design) y la prevención del perfilado |
| ⚡ Accionable | **8** | Resultado >10% orienta hacia aplicación de seudonimización o eliminación del quasi-identificador |
| 🔬 Genuino | **6** | Identificar todos los quasi-identificadores es complejo; depende del criterio del analista |
| 💡 Significativo | **6** | Concepto técnico que requiere explicación a directivos no especializados |
| 📐 Preciso | **6** | La definición de "quasi-identificador" puede variar entre analistas; riesgo de inconsistencia |
| ⏱️ Oportuno | **7** | Medición semestral o con cada nuevo tratamiento; periodicidad adecuada |
| 🛡️ Independiente | **7** | Difícil de manipular sin conocimiento técnico especializado |
| 💰 Rentable | **6** | Requiere análisis experto por tratamiento; coste moderado-alto en organizaciones grandes |
| **TOTAL** | **7.00** | ⭐⭐ **Buena** — Implementar con mejora en definición operacional |

---

### Métrica L-M3: Índice de Controles Anti-Vinculación (ICAV)

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **8** | Un ICAV bajo predice alta probabilidad de vinculación exitosa por actores internos o externos |
| 🎯 Relevante | **9** | Mide directamente la implementación técnica del Art. 25 y Art. 32 RGPD |
| ⚡ Accionable | **9** | Cada subcomponente del ICAV es una acción de mejora específica y asignable |
| 🔬 Genuino | **7** | Los 5 controles son verificables técnicamente; riesgo de implementación nominal sin efectividad real |
| 💡 Significativo | **7** | La escala 0–10 es intuitiva; los 5 controles son comprensibles para equipos técnicos |
| 📐 Preciso | **7** | Puntuación semi-objetiva (1/0.5/0 por control); validación técnica recomendada |
| ⏱️ Oportuno | **7** | Revisión semestral o ante cambios en arquitectura; frecuencia adecuada |
| 🛡️ Independiente | **7** | Verificable por auditoría técnica independiente; difícil de inflar sin implementación real |
| 💰 Rentable | **7** | Coste moderado; reutilizable en auditorías de seguridad existentes |
| **TOTAL** | **7.56** | ⭐⭐ **Buena** — Implementar con prioridad |

---

### Métrica L-M4: TTDL — Tiempo de detección de vinculación no autorizada

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **6** | Mide eficacia de detección pasada; capacidad predictiva limitada sobre incidentes futuros |
| 🎯 Relevante | **8** | Directamente relevante para el plazo de notificación de 72h del Art. 33 RGPD |
| ⚡ Accionable | **8** | TTDL >72h activa revisión del sistema de monitorización y respuesta a incidentes |
| 🔬 Genuino | **6** | Solo mide eventos detectados; los no detectados no están en el denominador (sesgo de cobertura) |
| 💡 Significativo | **8** | Horas son una unidad comprensible y urgente para todos los niveles organizacionales |
| 📐 Preciso | **6** | Depende de la calidad del registro de timestamps; sistemas sin logs detallados producen datos imprecisos |
| ⏱️ Oportuno | **8** | Dato disponible en tiempo real en sistemas SIEM; alta oportunidad |
| 🛡️ Independiente | **7** | Difícil de manipular sin alterar logs de forma detectable |
| 💰 Rentable | **6** | Requiere SIEM operativo; coste de infraestructura significativo para PYME |
| **TOTAL** | **7.00** | ⭐⭐ **Buena** — Implementar en organizaciones con SIEM; adaptar en PYME |

---

### Métrica L-M5: % modelos ML con EIPD que evalúa linking

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **8** | Ausencia de EIPD predice riesgo de vinculación no evaluada en modelos en producción |
| 🎯 Relevante | **9** | Obligación directa Art. 35 RGPD + EDPB LLM Report 2025; máxima relevancia regulatoria |
| ⚡ Accionable | **9** | Resultado <100% → iniciar EIPD inmediatamente; acción directa y urgente |
| 🔬 Genuino | **7** | Mide existencia documental; calidad de la EIPD requiere revisión adicional |
| 💡 Significativo | **8** | El porcentaje es directamente comprensible; 100% es la única respuesta aceptable |
| 📐 Preciso | **8** | Numerador/denominador objetivos: registro de modelos ML vs. EIPDs existentes |
| ⏱️ Oportuno | **8** | Verificable en cualquier momento; actualización al desplegar nuevo modelo |
| 🛡️ Independiente | **8** | Las EIPDs son documentos verificables; difícil de simular sin esfuerzo real |
| 💰 Rentable | **7** | Coste de la EIPD ya es obligatorio; el indicador tiene coste marginal casi nulo |
| **TOTAL** | **8.00** | ⭐⭐⭐ **Excelente** — Implementar con máxima prioridad |

---

## MÓDULO 2 — INDICADOR I (IDENTIFYING / IDENTIFICABILIDAD)

### Métrica I-M1: Nivel de K-anonimato medio de datasets publicados

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **8** | Un k bajo predice alta probabilidad de re-identificación exitosa mediante ataques de inferencia |
| 🎯 Relevante | **9** | Central para la validez de la anonimización bajo el Art. 4.1 RGPD y las directrices WP216 GT29 |
| ⚡ Accionable | **8** | k < 5 requiere acción inmediata: supresión de datos, generalización o no publicación |
| 🔬 Genuino | **8** | Métrica estadística formalizada; mide directamente el riesgo de re-identificación por individuo |
| 💡 Significativo | **7** | Intuitivo para técnicos; requiere traducción para directivos ("k=3 significa que podríamos identificar a 1 de cada 3 personas") |
| 📐 Preciso | **8** | Cálculo algorítmico reproducible; herramientas automatizadas disponibles (ARX, sdcMicro) |
| ⏱️ Oportuno | **9** | Calculable automáticamente antes de cada publicación; latencia mínima |
| 🛡️ Independiente | **8** | Cálculo técnico externo al sujeto medido; difícil de manipular sin alterar los datos |
| 💰 Rentable | **7** | Herramientas open source disponibles (ARX Data Anonymization Tool); coste técnico moderado |
| **TOTAL** | **8.00** | ⭐⭐⭐ **Excelente** — Implementar como estándar en publicaciones de datos |

---

### Métrica I-M3: FAR — False Acceptance Rate biométrica

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **9** | FAR alto predice directamente el riesgo de acceso no autorizado o re-identificación por impostor |
| 🎯 Relevante | **10** | Obligatorio para sistemas biométricos bajo Art. 9 RGPD + Art. 5.1.d AI Act; caso AENA es paradigmático |
| ⚡ Accionable | **9** | FAR > 0.01% en sistemas de alta seguridad → ajuste de umbrales, cambio de tecnología, suspensión |
| 🔬 Genuino | **8** | Métrica estandarizada ISO/IEC 19795; mide directamente el fenómeno de identificación errónea |
| 💡 Significativo | **7** | Porcentaje comprensible pero requiere contexto ("un FAR de 0.1% en un sistema de 10M usuarios = 10.000 errores/día") |
| 📐 Preciso | **9** | Estándar ISO; medición en entornos controlados con alta reproducibilidad |
| ⏱️ Oportuno | **8** | Medible en pruebas periódicas; actualización anual o ante cambios del sistema |
| 🛡️ Independiente | **9** | Prueba técnica objetiva; difícil de manipular sin modificar el sistema |
| 💰 Rentable | **6** | Requiere laboratorio de pruebas o proveedor especializado; coste elevado para organizaciones pequeñas |
| **TOTAL** | **8.33** | ⭐⭐⭐ **Excelente** — Obligatoria para sistemas biométricos |

---

### Métrica I-M5: Epsilon (ε) de privacidad diferencial

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **8** | ε alto predice mayor riesgo de re-identificación en modelos ML; indicador prospectivo del riesgo |
| 🎯 Relevante | **8** | Crecientemente relevante con el EDPB Report LLMs 2025; central para modelos de IA con datos sensibles |
| ⚡ Accionable | **7** | ε > umbral → añadir más ruido diferencial o reducir el conjunto de datos de entrenamiento |
| 🔬 Genuino | **9** | Medida matemáticamente formal con garantías probabilísticas verificables (Dwork & Roth, 2014) |
| 💡 Significativo | **4** | Altamente técnica; difícil de comunicar a directivos sin formación matemática; requiere traducción |
| 📐 Preciso | **9** | Fórmula matemática exacta; reproducible dado el mismo modelo y los mismos parámetros |
| ⏱️ Oportuno | **7** | Calculable en el momento de entrenamiento del modelo; no actualizable sin reentrenar |
| 🛡️ Independiente | **9** | Parámetro técnico intrínseco al proceso de entrenamiento; no manipulable sin alterar el modelo |
| 💰 Rentable | **5** | Requiere implementación técnica en el pipeline de entrenamiento; coste inicial significativo |
| **TOTAL** | **7.33** | ⭐⭐ **Buena** — Implementar en organizaciones con capacidad técnica de IA; traducir a directivos |

---

## MÓDULO 3 — INDICADOR NR (NON-REPUDIATION / NO REPUDIO)

### Métrica NR-M1: Tasa de completitud de logs de acceso

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **7** | Logs incompletos predicen incapacidad de detectar brechas y de demostrar cumplimiento en auditoría |
| 🎯 Relevante | **9** | Obligatoria bajo ENS op.exp.8, ISO 27001 A.8.15, y como evidencia ante la AEPD en caso de brecha |
| ⚡ Accionable | **9** | Completitud <99.5% → revisión del sistema de logging; cobertura de sistemas no instrumentados |
| 🔬 Genuino | **7** | Mide cobertura de logs existentes; no captura lo que no está configurado para registrarse |
| 💡 Significativo | **8** | Porcentaje intuitivo; su importancia es comprensible en términos de "prueba de lo ocurrido" |
| 📐 Preciso | **7** | Depende de la calidad del sistema de estimación del denominador (accesos totales estimados) |
| ⏱️ Oportuno | **9** | Monitorizable en tiempo real con herramientas SIEM; alta oportunidad |
| 🛡️ Independiente | **7** | Auditable externamente; manipulación detectable mediante correlación de sistemas |
| 💰 Rentable | **7** | Coste de logging ya previsto en infraestructura; indicador de bajo coste marginal |
| **TOTAL** | **7.78** | ⭐⭐ **Buena** — Implementar como indicador de monitorización continua |

---

### Métrica NR-M4: TMRS — Tiempo Medio de Respuesta a Supresión

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **6** | Mide el pasado reciente; indica tendencias pero no predice incumplimientos futuros directamente |
| 🎯 Relevante | **10** | Obligación directa Art. 17 + Art. 12.3 RGPD; incumplimiento = reclamación automática ante AEPD |
| ⚡ Accionable | **9** | TMRS > 30 días → revisión urgente del proceso de gestión de derechos; SLA internos |
| 🔬 Genuino | **8** | Mide el proceso real; captura todas las solicitudes procesadas |
| 💡 Significativo | **9** | "Días" es la unidad más comprensible posible; directivos y reguladores lo entienden inmediatamente |
| 📐 Preciso | **8** | Calculable con timestamps de recepción y confirmación de supresión; alta precisión si hay registro |
| ⏱️ Oportuno | **9** | Calculable en tiempo real o mensualmente; frecuencia adaptable |
| 🛡️ Independiente | **8** | Verificable mediante auditoría de los registros de solicitudes y respuestas |
| 💰 Rentable | **9** | Coste mínimo: extracción de datos del sistema de gestión de derechos ya existente |
| **TOTAL** | **8.44** | ⭐⭐⭐ **Excelente** — Uno de los indicadores de mayor calidad del catálogo |

---

## MÓDULO 4 — INDICADOR D (DETECTING / DETECCIÓN)

### Métrica D-M1: Índice de Proporcionalidad de Videovigilancia (IPV)

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **6** | IPV bajo predice riesgo de sanción ante inspección de la AEPD; capacidad predictiva moderada |
| 🎯 Relevante | **9** | Art. 22 LOPDGDD; área de alta actividad sancionadora en España (AEPD, 2023–2025) |
| ⚡ Accionable | **9** | Cada subcomponente del IPV es una acción concreta y asignable a un responsable |
| 🔬 Genuino | **7** | Los 5 componentes son verificables; riesgo de cumplimiento formal sin efectividad real |
| 💡 Significativo | **8** | Escala 0–10 intuitiva; cada componente tiene nombre y propósito comprensible |
| 📐 Preciso | **7** | Evaluación semi-objetiva; puntuación de 0.5 para implementación parcial requiere criterio claro |
| ⏱️ Oportuno | **7** | Revisión anual suficiente; medición rápida in situ |
| 🛡️ Independiente | **7** | Verificable por auditor externo o AEPD en inspección |
| 💰 Rentable | **8** | Checklist de bajo coste; alto valor ante riesgo de inspección |
| **TOTAL** | **7.56** | ⭐⭐ **Buena** — Implementar como auditoría anual obligatoria |

---

### Métrica D-M5: % empleados informados de sistemas de monitorización

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **5** | Mide cumplimiento puntual; capacidad predictiva limitada sobre comportamiento futuro |
| 🎯 Relevante | **10** | Art. 87 LOPDGDD es taxativo: la información previa es obligatoria sin excepciones |
| ⚡ Accionable | **10** | Cualquier resultado <100% activa acción inmediata: comunicar formalmente a empleados no informados |
| 🔬 Genuino | **8** | Mide recepción formal de la información; no mide comprensión real (limitación aceptada) |
| 💡 Significativo | **9** | Porcentaje de cumplimiento de obligación legal; máxima claridad para todos los niveles |
| 📐 Preciso | **9** | Verificable mediante registros de comunicación interna firmados o acuse de recibo digital |
| ⏱️ Oportuno | **8** | Verificable en cualquier momento; actualización ante nuevas contrataciones |
| 🛡️ Independiente | **8** | Acuse de recibo documentado es prueba objetiva |
| 💰 Rentable | **9** | Coste casi nulo: revisión de registros de comunicación interna existentes |
| **TOTAL** | **8.44** | ⭐⭐⭐ **Excelente** — Implementar como verificación de cumplimiento inmediato |

---

## MÓDULO 5 — INDICADOR DD (DATA DISCLOSURE / DIVULGACIÓN)

### Métrica DD-M1: % encargados con DPA vigente y auditado

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **7** | Encargados sin DPA predicen exposición a sanciones y responsabilidad solidaria en caso de brecha |
| 🎯 Relevante | **10** | Art. 28 RGPD: obligación directa sin excepción; área frecuentemente sancionada |
| ⚡ Accionable | **10** | DPA ausente → iniciar contratación inmediatamente; acción directa sin ambigüedad |
| 🔬 Genuino | **8** | Mide existencia documental verificable; auditoría de contenido DPA es el paso adicional |
| 💡 Significativo | **9** | "% de proveedores con contrato de privacidad" es comprensible a cualquier nivel directivo |
| 📐 Preciso | **9** | Verificable desde el registro de proveedores y el archivo de contratos |
| ⏱️ Oportuno | **8** | Actualización semestral o al incorporar nuevo proveedor; alta oportunidad |
| 🛡️ Independiente | **8** | Documentos legales verificables por auditor externo |
| 💰 Rentable | **9** | Bajo coste: revisión del registro de proveedores y contratos; alta rentabilidad regulatoria |
| **TOTAL** | **8.67** | ⭐⭐⭐ **Excelente** — Indicador de referencia para gestión de terceros |

---

### Métrica DD-M3: % prompts IA con datos personales no auditados

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **9** | Alta tasa de datos personales en prompts predice futura brecha por re-entrenamiento o leak del proveedor IA |
| 🎯 Relevante | **9** | EDPB Report LLMs 2025; AI Act Arts. 10, 53; máxima relevancia en el contexto post-ChatGPT |
| ⚡ Accionable | **8** | Tasa >2% → política de uso de IA + formación de empleados + herramientas de anonimización de prompts |
| 🔬 Genuino | **7** | Requiere herramientas de DLP (Data Loss Prevention) para detectar PII en prompts; sin DLP, la métrica es inobservable |
| 💡 Significativo | **7** | "Empleados que meten datos de clientes en ChatGPT" es comprensible; el porcentaje contextualiza |
| 📐 Preciso | **6** | Depende de la calidad de la herramienta DLP; falsos positivos/negativos son frecuentes |
| ⏱️ Oportuno | **8** | Monitorizable en tiempo real con DLP; alta oportunidad si la infraestructura existe |
| 🛡️ Independiente | **7** | Medición técnica objetiva; mitigable por empleados con conocimiento técnico avanzado |
| 💰 Rentable | **5** | Requiere herramienta DLP corporativa; coste significativo; métrica emergente con ROI creciente |
| **TOTAL** | **7.33** | ⭐⭐ **Buena** — Implementar progresivamente; alta prioridad estratégica 2025–2026 |

---

### Métrica DD-M5: Índice de Minimización de Datos (IMD)

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **7** | IMD bajo predice mayor superficie de exposición en caso de brecha; volumen excesivo = mayor impacto |
| 🎯 Relevante | **9** | Art. 5.1.c RGPD (minimización) y Art. 25.2 (Privacy by Default) son principios nucleares del RGPD |
| ⚡ Accionable | **8** | Campos sin justificación → eliminación del campo o documentación de la necesidad |
| 🔬 Genuino | **6** | Mide justificación documental, no efectividad real de la minimización; riesgo de justificaciones genéricas |
| 💡 Significativo | **7** | El concepto de "datos necesarios vs. datos recogidos" es comprensible; el porcentaje lo hace tangible |
| 📐 Preciso | **7** | Requiere inventario detallado de campos; coste de auditoría de datos inicial puede ser elevado |
| ⏱️ Oportuno | **6** | Revisión anual o ante rediseño de sistemas; frecuencia limitada |
| 🛡️ Independiente | **6** | Posible inflación de "justificaciones documentadas" sin revisión crítica de su calidad |
| 💰 Rentable | **6** | Requiere auditoría de datos; coste moderado; beneficio en reducción de superficie de ataque |
| **TOTAL** | **6.89** | ⭐⭐ **Buena** — Implementar con criterios claros de justificación |

---

## MÓDULO 6 — INDICADOR U (UNAWARENESS / DESCONOCIMIENTO)

### Métrica U-M1: ILPP — Índice de Legibilidad de Política de Privacidad

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **7** | Una política ilegible predice mayor tasa de reclamaciones por información insuficiente |
| 🎯 Relevante | **8** | Art. 12.1 RGPD: "forma concisa, transparente, inteligible y de fácil acceso, con lenguaje claro y sencillo" |
| ⚡ Accionable | **8** | ILPP <60 → reescribir política con lenguaje más sencillo; objetivo claro y medible |
| 🔬 Genuino | **7** | El índice Flesch-Kincaid mide complejidad lingüística, no comprensión semántica del contenido jurídico |
| 💡 Significativo | **8** | "La política de privacidad tiene un nivel de lectura universitario" es comprensible para cualquier directivo |
| 📐 Preciso | **8** | Algoritmo reproducible y automatizable; herramientas disponibles en castellano |
| ⏱️ Oportuno | **9** | Calculable en minutos con herramientas online; alta oportunidad |
| 🛡️ Independiente | **6** | La legibilidad puede optimizarse sin mejorar la transparencia real del contenido |
| 💰 Rentable | **9** | Coste casi nulo: herramientas de análisis de legibilidad gratuitas o de bajo coste |
| **TOTAL** | **7.78** | ⭐⭐ **Buena** — Excelente métrica de cumplimiento del Art. 12.1 RGPD |

---

### Métrica U-M3: Tasa de consentimientos válidos (4 requisitos Art. 7)

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **8** | Consentimientos inválidos predicen nulidad de la base jurídica y exposición sancionatoria máxima |
| 🎯 Relevante | **10** | Art. 7 RGPD; area de máxima actividad sancionatoria de la AEPD y el EDPB (2023–2025) |
| ⚡ Accionable | **9** | Consentimiento inválido → corrección inmediata del mecanismo de recogida; rediseño del formulario |
| 🔬 Genuino | **7** | Auditoría de muestra verificable; riesgo de que criterios de evaluación sean subjetivos |
| 💡 Significativo | **9** | "El X% de los consentimientos recogidos no son legalmente válidos" es impacto directo comprensible |
| 📐 Preciso | **7** | Depende de la calidad de los criterios de evaluación aplicados en la auditoría |
| ⏱️ Oportuno | **7** | Auditoría de muestra realizable trimestralmente o ante cambio del mecanismo de consentimiento |
| 🛡️ Independiente | **8** | Auditoría externa puede verificar la validez de los consentimientos sin dependencia del sujeto medido |
| 💰 Rentable | **7** | Coste de auditoría jurídica moderado; alto valor preventivo ante multas de hasta 20 M€ |
| **TOTAL** | **8.00** | ⭐⭐⭐ **Excelente** — Implementar como auditoría trimestral de consentimientos |

---

## MÓDULO 7 — INDICADOR NC (NON-COMPLIANCE / INCUMPLIMIENTO)

### Métrica NC-M3: Tasa de brechas notificadas en ≤ 72 horas

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **5** | Mide cumplimiento pasado; no predice brechas futuras pero sí la capacidad de respuesta |
| 🎯 Relevante | **10** | Art. 33 RGPD y Art. 23 NIS2: obligación con plazo legal explícito; incumplimiento = infracción directa |
| ⚡ Accionable | **10** | Tasa <100% → revisión urgente del procedimiento de gestión de incidentes |
| 🔬 Genuino | **9** | Mide el proceso real de respuesta a incidentes con timestamp verificable |
| 💡 Significativo | **10** | "El 100% de las brechas deben notificarse en 72 horas" es el KPI de cumplimiento más comprensible |
| 📐 Preciso | **9** | Timestamps de detección y notificación son objetivos; verificables ante la AEPD |
| ⏱️ Oportuno | **10** | Dato disponible en tiempo real durante el incidente; máxima oportunidad |
| 🛡️ Independiente | **9** | Registrado en el sistema de notificación de la AEPD; altamente verificable |
| 💰 Rentable | **9** | Coste casi nulo: extracción de registros de incidentes ya existentes |
| **TOTAL** | **9.00** | ⭐⭐⭐ **Excelente** — Mejor métrica del catálogo; implementación obligatoria |

---

### Métrica NC-M5: IPAA — Índice de Preparación AI Act

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **9** | IPAA bajo predice incumplimiento de AI Act cuando las obligaciones de alto riesgo entren en vigor (agosto 2026) |
| 🎯 Relevante | **10** | AI Act con sanciones hasta 35 M€; máxima relevancia estratégica para 2025–2026 |
| ⚡ Accionable | **9** | Cada subcomponente es una acción específica; el índice prioriza el esfuerzo de preparación |
| 🔬 Genuino | **7** | Los 5 componentes son verificables; riesgo de cumplimiento formal sin profundidad |
| 💡 Significativo | **8** | La escala 0–10 es intuitiva; los 5 componentes tienen nombres comprensibles |
| 📐 Preciso | **7** | Evaluación semi-objetiva similar al ICAV; requiere criterios claros por subcomponente |
| ⏱️ Oportuno | **8** | Revisión semestral suficiente dada la escala de tiempo normativa |
| 🛡️ Independiente | **7** | Verificable por auditor externo de IA; certificación ISO 42001 proporciona evidencia objetiva |
| 💰 Rentable | **7** | Coste de evaluación moderado; ROI muy alto dado el nivel de sanciones potenciales |
| **TOTAL** | **8.00** | ⭐⭐⭐ **Excelente** — Métrica estratégica de máxima urgencia en 2026 |

---

## MÓDULO 8 — INDICADOR IN (INACCURACY / INEXACTITUD) [LIINE4DU]

### Métrica IN-M3: Disparate Impact Ratio (DIR)

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **9** | DIR bajo predice daño discriminatorio a grupos protegidos antes de que sea evidente en casos concretos |
| 🎯 Relevante | **9** | Art. 22 RGPD + Art. 10 AI Act; prohibición expresa de discriminación en sistemas de IA de alto riesgo |
| ⚡ Accionable | **8** | DIR < 0.80 → revisión del modelo, ajuste de datos de entrenamiento o intervención humana obligatoria |
| 🔬 Genuino | **8** | Métrica estadística establecida (EEOC, 1971; adoptada en AI Act); mide directamente el impacto dispar |
| 💡 Significativo | **6** | Técnicamente rigurosa; la "regla del 80%" es comprensible pero requiere contextualización |
| 📐 Preciso | **8** | Cálculo estadístico reproducible dado el mismo dataset de evaluación |
| ⏱️ Oportuno | **7** | Calculable en ciclos de evaluación del modelo; actualización al reentrenar |
| 🛡️ Independiente | **8** | Calculable por auditor externo con acceso al modelo y datos de evaluación |
| 💰 Rentable | **6** | Requiere datos etiquetados con atributos de grupo protegido; coste moderado de preparación de datos |
| **TOTAL** | **7.67** | ⭐⭐ **Buena** — Implementar como estándar para todos los modelos de IA de alto riesgo |

---

## MÓDULO 9 — INDICADOR EX (EXCLUSION / EXCLUSIÓN) [LIINE4DU]

### Métrica EX-M1: Nivel de conformidad WCAG 2.1 AA

| Criterio | Puntuación | Justificación |
|----------|-----------|---------------|
| 🔮 Predictivo | **6** | Baja conformidad predice barreras de acceso a derechos para personas con diversidad funcional |
| 🎯 Relevante | **8** | RD 1112/2018 (sector público); Art. 12.1 RGPD (accesibilidad de comunicaciones de privacidad) |
| ⚡ Accionable | **9** | Cada criterio WCAG no superado es una mejora técnica específica y asignable |
| 🔬 Genuino | **8** | Estándar internacional ISO 40500; criterios técnicos verificables con herramientas automatizadas |
| 💡 Significativo | **7** | El porcentaje de conformidad es comprensible; la conexión con la privacidad requiere explicación |
| 📐 Preciso | **8** | Herramientas de auditoría automatizada (WAVE, axe, Lighthouse) ofrecen resultados reproducibles |
| ⏱️ Oportuno | **8** | Auditoría automatizable en cada despliegue; integrable en pipeline CI/CD |
| 🛡️ Independiente | **8** | Herramientas de auditoría externas; difícil de manipular sin cambios técnicos reales |
| 💰 Rentable | **9** | Herramientas gratuitas disponibles; coste de auditoría muy bajo para el valor que aporta |
| **TOTAL** | **7.89** | ⭐⭐ **Buena** — Implementar como verificación en cada actualización de portal |

---

## TABLA RESUMEN GLOBAL — RANKING PRAGMATIC DE TODAS LAS MÉTRICAS

| Métrica | Indicador | P | R | A | G | M | A | T | I | C | **Total** | **Calificación** |
|---------|-----------|---|---|---|---|---|---|---|---|---|-----------|-----------------|
| NC-M3 | Non-compliance | 5 | 10 | 10 | 9 | 10 | 9 | 10 | 9 | 9 | **9.00** | ⭐⭐⭐ Excelente |
| DD-M1 | Data Disclosure | 7 | 10 | 10 | 8 | 9 | 9 | 8 | 8 | 9 | **8.67** | ⭐⭐⭐ Excelente |
| D-M5 | Detecting | 5 | 10 | 10 | 8 | 9 | 9 | 8 | 8 | 9 | **8.44** | ⭐⭐⭐ Excelente |
| NR-M4 | Non-repudiation | 6 | 10 | 9 | 8 | 9 | 8 | 9 | 8 | 9 | **8.44** | ⭐⭐⭐ Excelente |
| I-M3 | Identifying (FAR) | 9 | 10 | 9 | 8 | 7 | 9 | 8 | 9 | 6 | **8.33** | ⭐⭐⭐ Excelente |
| NC-M5 | Non-compliance (AI Act) | 9 | 10 | 9 | 7 | 8 | 7 | 8 | 7 | 7 | **8.00** | ⭐⭐⭐ Excelente |
| I-M1 | Identifying (k-anon) | 8 | 9 | 8 | 8 | 7 | 8 | 9 | 8 | 7 | **8.00** | ⭐⭐⭐ Excelente |
| U-M3 | Unawareness (consent) | 8 | 10 | 9 | 7 | 9 | 7 | 7 | 8 | 7 | **8.00** | ⭐⭐⭐ Excelente |
| L-M5 | Linking (ML/EIPD) | 8 | 9 | 9 | 7 | 8 | 8 | 8 | 8 | 7 | **8.00** | ⭐⭐⭐ Excelente |
| EX-M1 | Exclusion (WCAG) | 6 | 8 | 9 | 8 | 7 | 8 | 8 | 8 | 9 | **7.89** | ⭐⭐ Buena |
| U-M1 | Unawareness (legib.) | 7 | 8 | 8 | 7 | 8 | 8 | 9 | 6 | 9 | **7.78** | ⭐⭐ Buena |
| NR-M1 | Non-repudiation (logs) | 7 | 9 | 9 | 7 | 8 | 7 | 9 | 7 | 7 | **7.78** | ⭐⭐ Buena |
| L-M3 | Linking (ICAV) | 8 | 9 | 9 | 7 | 7 | 7 | 7 | 7 | 7 | **7.56** | ⭐⭐ Buena |
| D-M1 | Detecting (IPV) | 6 | 9 | 9 | 7 | 8 | 7 | 7 | 7 | 8 | **7.56** | ⭐⭐ Buena |
| IN-M3 | Inaccuracy (DIR) | 9 | 9 | 8 | 8 | 6 | 8 | 7 | 8 | 6 | **7.67** | ⭐⭐ Buena |
| L-M1 | Linking (DFDs) | 7 | 9 | 8 | 7 | 8 | 8 | 7 | 6 | 9 | **7.67** | ⭐⭐ Buena |
| I-M5 | Identifying (ε DP) | 8 | 8 | 7 | 9 | 4 | 9 | 7 | 9 | 5 | **7.33** | ⭐⭐ Buena |
| DD-M3 | Data Disclosure (IA) | 9 | 9 | 8 | 7 | 7 | 6 | 8 | 7 | 5 | **7.33** | ⭐⭐ Buena |
| L-M2 | Linking (quasi-id.) | 8 | 9 | 8 | 6 | 6 | 6 | 7 | 7 | 6 | **7.00** | ⭐⭐ Buena |
| L-M4 | Linking (TTDL) | 6 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | **7.00** | ⭐⭐ Buena |
| DD-M5 | Data Disclosure (IMD) | 7 | 9 | 8 | 6 | 7 | 7 | 6 | 6 | 6 | **6.89** | ⭐⭐ Buena |

---

## ANÁLISIS DE BRECHAS PRAGMATIC — CRITERIOS MÁS DÉBILES DEL CATÁLOGO

### Criterios con menor puntuación media por indicador:

| Indicador | Criterio más débil | Puntuación media | Acción de mejora recomendada |
|-----------|-------------------|-----------------|------------------------------|
| All | **C (Rentable)** | 6.7 | Automatizar recolección de métricas; integrar en herramientas existentes (SIEM, GRC) |
| I-M5 (ε DP) | **M (Significativo)** | 4.0 | Desarrollar dashboard de comunicación para directivos: traducir ε a "riesgo de identificación" |
| DD-M3 (IA prompts) | **C (Rentable)** | 5.0 | Roadmap de implementación DLP: empezar con herramientas cloud nativas antes de solución enterprise |
| L-M2 (quasi-id.) | **G (Genuino)** | 6.0 | Adoptar taxonomía ANONOS o ISO 29101 para definición operacional de quasi-identificadores |
| I-M5 (ε DP) | **C (Rentable)** | 5.0 | Priorizar para organizaciones con capacidad ML; no exigir en organizaciones sin modelos propios |

---

*Matriz PRAGMATIC elaborada conforme a la metodología de W. Krag Brotby y Gary Hinson (PRAGMATIC Security Metrics, CRC Press/Taylor & Francis, 2013), aplicada a los indicadores LINDDUN (KU Leuven/DistriNet) y LIINE4DU 1.0 (AEPD, octubre 2024). Puntuaciones basadas en análisis experto del marco regulatorio español vigente en abril de 2026. Versión 1.0.*
