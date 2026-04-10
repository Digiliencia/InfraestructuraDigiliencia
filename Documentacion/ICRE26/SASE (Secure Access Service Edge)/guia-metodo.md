# Guía metodológica de la Encuesta SASE

> Documento de referencia para el diseño, despliegue, análisis y uso estratégico de la Encuesta Integral sobre Adopción, Madurez e Indicadores SASE.

---

## 1. Objetivos de la encuesta

La encuesta persigue tres objetivos principales:

1. **Medir el grado de adopción real de arquitecturas SASE/SSE y Zero Trust** en organizaciones españolas y, en su caso, compararlo con tendencias internacionales.
2. **Cuantificar la madurez SASE desde varias dimensiones**: técnica (red/seguridad), gobernanza, cumplimiento ENS/NIS2, experiencia de usuario (QoE), continuidad de negocio y retorno de la inversión.
3. **Proporcionar insumos cuantitativos y cualitativos** para priorizar iniciativas de transformación, justificar inversiones y refinar políticas públicas y corporativas relacionadas con SASE/Zero Trust.

---

## 2. Población objetivo y roles

La encuesta está dirigida especialmente a organizaciones con dependencia significativa de servicios digitales, nube y trabajo remoto/híbrido. Se recomienda dirigirla a los siguientes perfiles:

- **CISO / Responsable de Ciberseguridad**.
- **Responsable de Redes / Infraestructura / Arquitectura**.
- **Responsable de Continuidad de Negocio y/o Resiliencia Operacional**.
- **Responsable de Riesgos / Cumplimiento / Auditoría de TI**.
- En organizaciones grandes, puede resultar útil que varios de estos roles respondan de forma coordinada.

Es perfectamente lícito que la misma persona lleve varias de estas gorras; la encuesta está pensada para capturar la visión “global” de la casa, no para generar conflictos internos.

---

## 3. Estructura de la encuesta y lógica de secciones

La encuesta se divide en diez bloques:

1. **Datos generales**: tamaño, sector, tipo de organización, volumen de usuarios remotos.
2. **Arquitectura de red y seguridad**: estado actual de VPN, SD‑WAN, SASE/SSE.
3. **Identidad y Zero Trust**: MFA, políticas contextuales, segmentación, ZTNA.
4. **Rendimiento, QoS y QoE**: medición de latencia, SLOs, experiencia percibida.
5. **Seguridad, detección y respuesta**: telemetría, MTTD/MTTR, amenazas, falsos positivos.
6. **Cumplimiento ENS/NIS2**: uso de SASE para implantar medidas, mapeo regulatorio, terceros.
7. **Adopción, madurez y consolidación**: nivel de despliegue, gobernanza, percepción directiva.
8. **Continuidad de negocio y resiliencia**: uso de SASE en planes de continuidad y diseño HA.
9. **Indicadores de negocio, IGM y ROI**: existencia de índices de madurez y modelos financieros.
10. **Preguntas abiertas**: lecciones aprendidas y visiones cualitativas.

Cada bloque se ha diseñado para que pueda agregarse a un **Índice Global de Madurez (IGM)** y para que algunas respuestas puedan alimentar un modelo de **ROI y coste evitado**.

---

## 4. Tipo de preguntas y escalas recomendadas

La encuesta combina varios tipos de preguntas:

- **Elección única nominal** (tipo de organización, sector, etc.).
- **Escalas ordinales** (0–25 %, 26–50 %, 51–75 %, 76–100 %) para medir coberturas y grados de adopción.
- **Escalas de madurez cualitativa** (exploratorio, táctico, estratégico, optimizado).
- **Selección múltiple** (beneficios percibidos, obstáculos principales).
- **Preguntas abiertas** para obtener narrativas y ejemplos concretos.

Se recomienda mapear cada opción ordinal a un valor numérico (por ejemplo, 1–4) para facilitar la construcción del IGM y del análisis estadístico.

---

## 5. Modalidad de administración

### 5.1. Formato

- Se recomienda un **formulario online** (herramienta de encuestas o portal corporativo) que facilite la recogida y exportación de resultados a formato CSV/XLSX.
- Alternativamente, puede distribuirse en formato PDF o DOCX para respuestas manuales, pero esto complica la agregación.

### 5.2. Duración estimada

- La encuesta está pensada para completarse en **20–30 minutos** por un responsable informado.
- Si varios roles responden de manera conjunta, se puede reservar una sesión de trabajo de 45–60 minutos y completar el cuestionario de forma consensuada.

### 5.3. Frecuencia de aplicación

- **Primera aplicación**: establecer la línea base (año 0).
- **Aplicaciones posteriores**: anual o bienal, para evaluar evolución del IGM y ROI y el efecto de proyectos SASE.

---

## 6. Cálculo del Índice Global de Madurez (IGM)

### 6.1. Dimensiones del IGM

Se propone estructurar el IGM en las siguientes dimensiones (ponderaciones ajustables):

1. **Arquitectura y cobertura SASE/SSE** (peso sugerido: 20 %).
2. **Identidad, Zero Trust y control de acceso** (20 %).
3. **Rendimiento y experiencia (QoE/QoS)** (15 %).
4. **Seguridad, detección y respuesta** (15 %).
5. **Cumplimiento ENS/NIS2 y gobernanza** (15 %).
6. **Continuidad de negocio y resiliencia** (10 %).
7. **Indicadores de negocio y ROI/IGM formalizado** (5 %).

Estas ponderaciones son meramente sugeridas; pueden adaptarse según el contexto sectorial (por ejemplo, reforzar cumplimiento en sectores altamente regulados).

### 6.2. Puntuación de las respuestas

- Cada respuesta cerrada se mapea a una puntuación entre 1 y 4 (o 0–3 cuando sea necesario representar ausencia total).
- Las preguntas con varias opciones (beneficios, obstáculos) pueden mapearse mediante recuento de selección o pesos predefinidos.
- Las preguntas abiertas no forman parte del IGM numérico, pero enriquecen el análisis cualitativo.

### 6.3. Cálculo por dimensión

1. Para cada dimensión, seleccione las preguntas correspondientes.
2. Transforme las respuestas en valores numéricos según la escala definida.
3. Calcule la media de la dimensión y reescálela a un rango 0–100 (por ejemplo, `puntuación_dimensión = (media_respuestas - 1) / (4 - 1) * 100`).
4. Multiplique por el peso de la dimensión.

### 6.4. Cálculo del IGM total

- El IGM total será la **suma de las puntuaciones ponderadas** de todas las dimensiones (rango 0–100).
- Puede segmentarse por tipo de organización, sector, tamaño, etc., para análisis comparativos.

---

## 7. Cálculo de ROI y coste evitado (nivel conceptual)

La plantilla de Excel (descrita en otro documento) permite calcular el ROI asociado a SASE combinando:

- **Costes**: licencias, proyectos, operación, formación, transición desde tecnología heredada, etc.
- **Beneficios “duros”**: reducción de licencias heredadas, ahorro en enlaces, consolidación de hardware, reducción de horas de operación.
- **Beneficios “blandos” pero cuantificables**: reducción de incidentes, reducción del tiempo de inactividad, mejora de productividad, mejora de cumplimiento (multas evitadas, sanciones regulatorias mitigadas).

La fórmula general de ROI es:

- `ROI (%) = ((Beneficios totales – Costes totales) / Costes totales) * 100`.

La guía metodológica recomienda vincular algunas respuestas de la encuesta (por ejemplo, consolidación de herramientas, reducción de incidentes, mejoras de QoE) con hipótesis de ahorro y coste evitado, para construir un modelo razonable y defendible ante la dirección.

---

## 8. Consideraciones de calidad de datos

- **Fiabilidad interna**: si se va a utilizar el IGM para comparativas serias, se recomienda pilotar la encuesta con un grupo reducido y revisar consistencia de respuestas.
- **Validez de contenido**: revisar periódicamente la encuesta para incorporar nuevas capacidades SASE (por ejemplo, WAAP, RBI, inspección TLS avanzada) y nuevos requisitos regulatorios.
- **Sesgo de respuesta**: advertir a los participantes de que la encuesta no es un examen, sino un espejo; se busca un diagnóstico útil, no una medalla inmediata.

---

## 9. Uso de resultados y comunicación

### 9.1. Para la organización encuestada

- Identificar **áreas fuertes** (por ejemplo, buena QoE, alta cobertura ZTNA) y **áreas débiles** (baja integración con SIEM, ausencia de métricas de ROI).
- Priorizar proyectos: migración de VPN a ZTNA, consolidación de plataformas, mejora de telemetría y paneles de QoE, etc.
- Construir un relato de evolución (pasar de “táctico” a “estratégico” y “optimizado”).

### 9.2. Para análisis sectorial o nacional

- Elaborar comparativas por sector (sanidad vs. educación vs. administración general, etc.).
- Identificar brechas de madurez entre tipos de organización (AAPP vs. empresas privadas, operadores críticos, etc.).
- Informar políticas públicas, programas de apoyo y priorización de recursos (por ejemplo, ayuda a sectores con baja madurez SASE).

### 9.3. Comunicación ejecutiva

- Traducir los resultados a **gráficos sencillos** (radar de madurez, barras comparativas, mapa de calor por dimensión).
- Enfatizar el vínculo entre madurez SASE, reducción de riesgo, mejora de experiencia de usuario y continuidad de negocio.

---

## 10. Recomendaciones prácticas para la implantación de la encuesta

1. **Patrocinio claro**: la encuesta debe estar respaldada por un responsable de alto nivel (CISO, CIO, Dir. de Riesgos) para que las respuestas se tomen en serio.
2. **Comunicación previa**: explicar objetivos, confidencialidad y beneficios a los participantes.
3. **Simplicidad operativa**: utilizar herramientas que faciliten exportación y análisis (no subestimar la logística).
4. **Devolver valor**: ofrecer a los participantes un informe de resultados y recomendaciones; nadie disfruta rellenando encuestas “a cambio de nada”.
5. **Iteración**: aprender de la primera ronda y ajustar preguntas, escalas y ponderaciones.

---

## 11. Epílogo metodológico

Esta guía no pretende ser un tratado estadístico, sino un manual de campo honesto para convertir una colección de preguntas SASE en un instrumento de diagnóstico y mejora continua. Si al usarla descubre contradicciones, zonas grises o nuevas necesidades, enhorabuena: significa que la realidad está viva. Ajústela, documente los cambios y, sobre todo, úsela para que la conversación sobre SASE y Zero Trust deje de ser un debate de fe tecnológica y se convierta en una discusión informada sobre riesgos, costes, beneficios y servicios que simplemente funcionan.