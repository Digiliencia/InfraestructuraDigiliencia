# Narrativa explicativa del marco GQM + PRAGMATIC aplicado a indicadores COBIT

---

## 1. Del titular político al contador de logs

Los indicadores de ciberseguridad nacionales tienen la mala costumbre de quedarse en el titular: “somos resilientes”, “lideramos tal índice”, “cumplimos tal directiva”. El reto es aterrizar esas declaraciones en algo que pueda medirse sin cruzar los dedos.

De ahí el uso combinado de **GQM** y **PRAGMATIC**:

- GQM nos obliga a conectar cada número con un **Goal** explícito y unas **Questions** honestas.[web:53][web:57]  
- PRAGMATIC nos ayuda a distinguir las métricas útiles de las decorativas, evaluándolas con criterios concretos.[web:61][web:58][web:64]

En resumen, la métrica deja de ser un adorno en el PowerPoint y pasa a ser un instrumento de gobierno.

---

## 2. Cómo encaja todo con COBIT 2019

COBIT 2019 ya ofrece el mapa de los procesos y objetivos de gobierno de TI y seguridad.[web:18][web:21] Lo que hacemos aquí es:

1. Tomar los **objetivos COBIT** más relevantes para ciberseguridad (EDM03, APO12, APO13, BAI06, DSS04‑05, MEA01‑03).  
2. Traducir cada objetivo a un **Goal** nacional o sectorial comprensible.  
3. Formular **Questions** que permitan saber si vamos por buen camino.  
4. Diseñar **Metrics** que puedan contestar esas preguntas con datos razonables.

Al final, el cuadro de indicadores nacional se convierte en una versión amplificada de lo que COBIT propone para una organización, pero aplicado a escala país.

---

## 3. Para qué sirve PRAGMATIC, aparte de sonar bien

El acrónimo PRAGMATIC encapsula nueve cualidades que toda métrica decente debería tener: **Predictiva, Relevante, Accionable, Genuina, Significativa, Precisa, Oportuna, Independiente y Rentable**.[web:61][web:59]

Aplicar estos criterios obliga a hacerse preguntas incómodas:

- ¿Este indicador sirve para anticipar algo o solo para narrar el pasado?  
- ¿Es realmente relevante para las decisiones que se deben tomar?  
- ¿Qué acción concreta se derivaría de un valor alto o bajo?  
- ¿Es una métrica que puede manipularse fácilmente?  
- ¿El coste de recogerla está justificado?

Si la respuesta es “no lo sé” demasiadas veces, la métrica probablemente merece una jubilación anticipada.

---

## 4. Ejemplo ilustrativo: MTTD/MTTR frente a “nº de firewalls”

Pensemos en dos métricas:

- `Nº de firewalls desplegados`  
- `Tiempo medio de detección y respuesta (MTTD/MTTR)`

La primera puede ser más tranquilizadora en una presentación (“tenemos muchos firewalls”), pero PRAGMATIC la suspende en varios criterios: poco predictiva, difícilmente accionable y de significado limitado.

En cambio, MTTD/MTTR puntúa alto: anticipa impacto futuro, es relevante para cualquier estrategia de resiliencia y sugiere acciones claras (mejorar monitorización, automatizar respuesta, reforzar procesos). No es casualidad que marcos como NIST CSF y guías de métricas de seguridad recomienden este tipo de indicadores.[web:46][web:62][web:65]

Así, PRAGMATIC funciona como filtro: separa el ruido del dato que importa.

---

## 5. Beneficios para un informe país basado en COBIT

Adoptar el marco GQM + PRAGMATIC en un informe nacional de indicadores COBIT trae varias ventajas:

- **Trazabilidad total**: cada número puede explicarse desde el objetivo estratégico hasta el dato técnico.  
- **Comparabilidad honesta**: las métricas están definidas de forma uniforme, lo que facilita comparaciones entre sectores y países.[web:24][web:28]  
- **Priorización informada**: el análisis PRAGMATIC permite concentrarse en las métricas que realmente ayudan a decidir.  
- **Resistencia al maquillaje**: criterios como Independiente y Genuino reducen la tentación de inflar resultados.

En síntesis: se pasa de “tenemos indicadores” a “tenemos indicadores que sirven para algo”.

---

## 6. Un comentario sobre la ironía metrológica

Medir siempre tiene un punto de ironía: lo que se mide tiende a mejorar, pero también a ser “entrenado” para quedar bien en la foto. Reconocerlo abiertamente permite diseñar métricas más robustas, menos vulnerables a la manipulación.

El enfoque PRAGMATIC no elimina el teatro, pero al menos obliga a encender las luces: si una métrica es poco independiente o muy cara, lo sabremos y podremos decidir si merece un hueco en el cuadro de mandos o en la papelera.

---

## 7. Conclusión provisional

La combinación de COBIT 2019, GQM y PRAGMATIC proporciona:

- Un **marco conceptual sólido**.  
- Una **metodología práctica** para derivar métricas útiles.  
- Un **filtro crítico** para evaluar si las métricas propuestas merecen la pena.

El resto es voluntad política, disciplina técnica… y algo de humor para soportar el proceso.

_Fin de la narrativa._