# Narrativa Explicativa del Marco GQM + PRAGMATIC aplicado a SASE

---

## 1. De los KPI sueltos al relato conectado

Durante años se han coleccionado métricas de red (latencia, ancho de banda), de seguridad (incidentes, vulnerabilidades) y de negocio (costes, ROI) como quien colecciona cromos: muchas cifras, poca historia. El marco GQM + PRAGMATIC pretende acabar con esa afición al numerismo huérfano.

La idea es sencilla pero exigente: **ninguna métrica vive por sí sola**. Cada número debe poder trazarse hacia arriba hasta un objetivo claro (“garantizar continuidad”, “reducir incidentes”, “cumplir ENS/NIS2”) y hacia abajo hasta decisiones concretas (“activar redundancia”, “endurecer políticas”, “invertir en consolidación”). Si no puede hacerse esa traza, la métrica es decorativa.

---

## 2. Qué aporta GQM en el contexto SASE

GQM obliga a formular primero el objetivo, luego las preguntas y por último las métricas. En el ámbito SASE, esto evita clásicos como:

- “Medir la latencia” sin saber qué decisión se tomará si sube.  
- “Contar incidentes” sin distinguir severidad ni relación con SASE.  
- “Sumar amenazas bloqueadas” sin preguntarse si el dato es más ruido que señal.

Aplicar GQM a SASE implica, por ejemplo, pasar de:

> “Queremos medir la QoE”

a algo más honesto:

> “Queremos saber si la experiencia de los médicos usando la historia clínica en remoto sigue siendo aceptable tras endurecer las políticas de inspección TLS, para decidir si ajustamos rutas, ampliamos capacidad o escalamos la inversión.”

A partir de ahí, preguntas y métricas caen por su propio peso.

---

## 3. Por qué PRAGMATIC es el filtro necesario

Una vez que se han elegido candidatas de métricas, aparece el segundo problema: **no todas merecen un lugar en el panel**. PRAGMATIC entra en escena como ese comité antipático, pero necesario, que pregunta:

- ¿Predice algo o solo describe el pasado?  
- ¿Le importa a alguien que tome decisiones?  
- ¿Sabemos qué hacer si empeora?  
- ¿Se entiende? ¿Podría manipularse fácilmente?  
- ¿Nos sale a cuenta medirla?

Este tamiz evita, por ejemplo, inundar a un comité ENS/NIS2 con histogramas de jitter por interfaz y, al mismo tiempo, descartar métricas baratas y valiosas como el porcentaje de proyectos cloud que pasan por SASE/ZTNA.

---

## 4. Cómo se conectan los objetivos nacionales con los datos técnicos

El puente se construye en tres tramos:

1. **ENS/NIS2 → Objetivos G (alto nivel)**  
   Ej.: “Garantizar la disponibilidad de sistemas ENS alto y servicios esenciales NIS2”.

2. **Objetivos G → Preguntas Q (diagnóstico)**  
   Ej.: “¿Qué indisponibilidad anual atribuible a SASE han tenido nuestros servicios críticos?”; “¿Qué porcentaje de acceso a estos sistemas está realmente canalizado por SASE/ZTNA?”.

3. **Preguntas Q → Métricas M (implementación)**  
   Ej.: M5.4 (indisponibilidad anual atribuible a SASE), M4.2 (% sistemas ENS M/A a través de SASE/ZTNA), M5.3 (tiempo de conmutación PoP/enlace).

El mismo proceso se repite para experiencia de usuario, Zero Trust, detección y respuesta, y ROI. A partir de ahí, PRAGMATIC ayuda a decidir cuáles de esas métricas suben a la “primera división” del cuadro de mando.

---

## 5. Cómo leer y utilizar las puntuaciones PRAGMATIC

Las puntuaciones PRAGMATIC **no son una verdad revelada**, sino una forma disciplinada de ventilar un debate que, de otro modo, se quedaría en “a mí me gusta esta métrica porque sí”.

- Una métrica con alta P, R y A (Predictiva, Relevante, Accionable) suele ser buena candidata a KPI principal.  
- Una métrica con alta C (barata) y razonable R y M puede ser útil como soporte, aunque no “brille” tanto.  
- Métricas con baja M o G (no significativas o poco genuinas) suelen acabar generando más confusión que claridad.

La matriz permite compararlas en frío, sin enamorarse de ninguna por razones estéticas o inercia histórica.

---

## 6. Qué gana la organización (y el país) con este enfoque

Aplicar GQM + PRAGMATIC a los indicadores SASE tiene varios efectos colaterales beneficiosos:

- **Mejor alineamiento entre técnicos, cumplimiento y negocio**: todos hablan de los mismos objetivos, preguntas y métricas.  
- **Cuadros de mando más frugales y útiles**: menos KPIs, pero mejor elegidos.  
- **Evidencias más sólidas para ENS/NIS2**: las métricas no son solo “números bonitos”, sino pruebas trazables de que los requisitos se operativizan.  
- **Disciplina para revisar métricas**: cuando una deja de ser predictiva, relevante o accionable, se documenta y se sustituye.

---

## 7. Epílogo: del fetichismo del dashboard a la medición con propósito

En un entorno donde todo genera datos, es tentador acumular gráficos hasta que el panel parece una cabina de avión. El marco GQM + PRAGMATIC aplicado a SASE propone un gesto casi revolucionario: **medir menos, pero mejor**.

Si, al aplicar este enfoque, algunas métricas queridas no pasan el filtro, no es una derrota, sino una señal de madurez. Y si otras métricas hasta ahora ignoradas emergen como candidatas principales, mejor todavía: significa que por fin se están haciendo las preguntas incómodas, pero correctas.