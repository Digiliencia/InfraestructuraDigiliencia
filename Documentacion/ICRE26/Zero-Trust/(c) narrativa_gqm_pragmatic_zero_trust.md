# Narrativa explicativa del marco GQM + PRAGMATIC aplicado a Zero Trust

## 1. De los eslóganes a las métricas con fundamento

En los últimos años, Zero Trust ha pasado de ser un lema de conferencias a convertirse en un requisito implícito de marcos normativos como NIS2, ENS, DORA o las estrategias nacionales de ciberseguridad. [web:47][web:53] Sin embargo, la distancia entre el "hay que hacer Zero Trust" y el "demuestre usted su madurez Zero Trust con números" es considerable.

El marco GQM + PRAGMATIC nace precisamente para acortar esa distancia: no basta con tener muchos gráficos; hace falta saber qué se quiere conseguir (Goal), qué preguntas responden a ese objetivo (Question) y qué métricas, bien escogidas y bien evaluadas (Metric + PRAGMATIC), sirven para algo más que adornar informes.

## 2. Cómo se conectan los objetivos nacionales con los logs del SIEM

Una estrategia nacional puede hablar de "reforzar la resiliencia de los servicios esenciales" o "mejorar la confianza digital". [web:47][web:41] Traducido a GQM, esto implica bajar desde objetivos como:

- "Reducir el impacto de incidentes graves en operadores esenciales".  
- "Aumentar la confianza de ciudadanos y empresas en los servicios digitales".  

A preguntas del tipo:

- "¿Cuánto tardan las organizaciones en detectar y contener incidentes significativos?".  
- "¿Hasta qué punto el acceso a sistemas críticos se controla con MFA y principios de mínimo privilegio?".  

Y, por fin, a métricas concretas:

- MTTD, MTTR, % usuarios con MFA, % cuentas privilegiadas en PAM, % sistemas monitorizados en SIEM, etc. [web:51][web:6]

La gracia del enfoque GQM es que permite justificar cada métrica ante un regulador, un auditor o una aseguradora: no es un número arbitrario, sino la respuesta a una pregunta alineada con un objetivo claro.

## 3. Por qué PRAGMATIC (y no solo "que sea medible")

Si algo nos ha enseñado la experiencia con cuadros de mando es que no todas las métricas merecen el mismo cariño. Algunas son decorativas, otras son tóxicas (incentivan comportamientos perversos) y unas pocas son realmente útiles.

Los criterios PRAGMATIC ayudan a separar el grano de la paja:

- **Predictivo**: ¿sirve para anticipar problemas o solo para llorar después?  
- **Relevante**: ¿importa de verdad a quien toma decisiones?  
- **Accionable**: si cambia, ¿sabemos qué hacer al respecto?  
- **Genuino**: ¿refleja la realidad o fomenta el maquillaje estadístico?  
- **Significativo**: ¿se entiende sin una tesis doctoral?  
- **Preciso**: ¿se puede medir sin debates interminables?  
- **Oportuno**: ¿llega a tiempo para reaccionar?  
- **Independiente**: ¿aporta algo que otra métrica no dé ya mejor?  
- **Rentable**: ¿cuesta menos medirla que el beneficio que aporta?

Aplicar PRAGMATIC obliga a justificar por qué mantenemos una métrica en el cuadro de mando. Y, quizás más importante, por qué descartamos otras que, aunque suenen bien, no aportan valor real.

## 4. Un ejemplo con MFA: del objetivo al KPI creíble

Tomemos el caso del MFA en sistemas críticos:

- Objetivo: reducir el riesgo de compromiso de cuentas críticas.  
- Pregunta: ¿qué proporción de usuarios de sistemas críticos usa MFA robusto?  
- Métrica: % de usuarios con MFA.

Evaluada con PRAGMATIC, la métrica sale muy bien parada: es predictiva, relevante, accionable, significativa y barata de obtener, siempre que exista un IAM centralizado. [web:51] Eso justifica que se convierta en uno de los KPIs estrella de madurez Zero Trust a nivel nacional.

En cambio, métricas como "número total de alertas del SIEM" pueden tener menos puntuación PRAGMATIC: sin contexto, son difíciles de interpretar, fáciles de maquillar y poco accionables.

## 5. Cómo usar el marco sin perder la paciencia

En la práctica, no se trata de evaluar con PRAGMATIC las 200 métricas que se puedan imaginar, sino de:

1. Definir 10–20 objetivos GQM clave por pilar y nivel (nacional/organizativo/técnico).  
2. Asociar 2–4 métricas candidatas por objetivo.  
3. Evaluar esas métricas con PRAGMATIC y quedarse con las mejores (y alguna complementaria, si aporta perspectiva).  
4. Revisar el conjunto cada 1–2 años.

El resultado debería ser un cuadro de mando sobrio pero expresivo: suficiente para orientar políticas y decisiones de inversión, sin convertir a los equipos en esclavos de la hoja de cálculo.

## 6. Relación con la encuesta de madurez Zero Trust

La encuesta de madurez Zero Trust propuesta anteriormente ofrece una fotografía cualitativa y cuantitativa de prácticas en organizaciones. El marco GQM + PRAGMATIC permite:

- Mapear cada pregunta de la encuesta a objetivos GQM y métricas específicas.  
- Evaluar qué preguntas producen datos con mayor calidad PRAGMATIC.  
- Priorizar qué resultados se escalan a dashboards nacionales, sectoriales o corporativos.

Así, la encuesta deja de ser un "formulario curioso" para convertirse en un instrumento de política pública y de gobierno corporativo: se sabe por qué se pregunta cada cosa y qué se hará con la respuesta.

## 7. Epílogo: medir bien para confiar menos (y mejor)

Zero Trust, bien entendido, no va de paranoia, sino de lucidez: aceptar que la confianza no se regala, se verifica. Medir con GQM + PRAGMATIC es la versión analítica de esa lucidez: no creemos en métricas por fe, sino porque podemos demostrar que responden a objetivos claros y superan un examen exigente de utilidad.

Si la ciberseguridad es, en parte, una batalla por el relato, no hay mejor relato que el de unos indicadores que conectan los logs del SIEM con las estrategias nacionales, sin perder irónicamente el sentido del humor por el camino.