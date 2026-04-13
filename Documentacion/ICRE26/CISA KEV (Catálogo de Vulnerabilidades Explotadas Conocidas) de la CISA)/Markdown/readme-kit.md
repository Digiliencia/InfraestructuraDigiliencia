# README del Kit de Encuesta sobre Gestión de Vulnerabilidades KEV, Pentesting, SIEM y Capacitación

## 1. ¿Qué es este kit?

Este kit reúne todos los materiales necesarios para diseñar, aplicar y explotar una encuesta de madurez en ciberseguridad centrada en:

- Gestión de vulnerabilidades (con foco en las Known Exploited Vulnerabilities – KEV).
- Pruebas de penetración y ejercicios de Red/Purple Team.
- Monitorización y gestión de eventos de seguridad (SIEM/SOC).
- Capacitación y cultura de seguridad de los empleados.

Su propósito es ofrecer una base **coherente, reutilizable y extensible** para diagnósticos organizativos, sectoriales o nacionales.

## 2. Contenidos del kit

El kit incluye los siguientes componentes en formato Markdown:

1. **Modelo de encuesta integral** (`encuesta-modelo.md`)
   - Cuestionario completo con preguntas estructuradas e identificadores únicos.
   - Opciones de respuesta diseñadas para facilitar la codificación y, de paso, arrancar alguna sonrisa.

2. **Guía metodológica detallada** (`guia-metodo.md`)
   - Instrucciones para aplicar la encuesta.
   - Diseño de escalas, tratamiento estadístico y cálculo del Índice Global de Madurez (IGM).
   - Orientaciones para estimar el ROI de iniciativas de mejora.

3. **Narrativa explicativa** (`narrativa.md`)
   - Texto de acompañamiento que explica el sentido de la encuesta.
   - Útil para introducir el proyecto a la dirección y a las personas encuestadas.

4. **Mapeo normativo** (`mapeo-normas.md`)
   - Tabla que relaciona cada pregunta con estándares y marcos de referencia (ISO, NIST, ENS, NIS2, etc.).
   - Facilita auditorías, alineamiento regulatorio y justificación de contenidos.

5. **Plantilla de Excel para IGM y ROI** (`plantilla-igm-roi.md`)
   - Descripción de la estructura de un libro Excel recomendado.
   - Incluye el esquema de hojas, campos y fórmulas clave para implementar el cálculo de IGM y ROI.

6. **Plantilla de Reporte Ejecutivo** (`ppt-reporte.md`)
   - Guion de diapositivas para presentar resultados a la alta dirección.
   - Pensado para convertir datos en decisiones, evitando que nadie huya de la sala.

## 3. Cómo empezar (paso a paso)

1. **Adaptar el modelo de encuesta**
   - Revise `encuesta-modelo.md` y, si es necesario, ajuste la redacción para adaptarla al lenguaje y cultura de su organización.
   - Mantenga los identificadores de pregunta (GOV-01, VUL-01, etc.) para preservar la compatibilidad con el resto del kit.

2. **Definir el plan de aplicación**
   - Consulte `guia-metodo.md` para decidir:
     - Población objetivo (quién responde).
     - Modalidad (online, entrevistas, mixto).
     - Calendario y responsable de la coordinación.

3. **Implementar el cuestionario en una herramienta**
   - Pase el contenido del modelo de encuesta a la plataforma que utilice (formularios web, herramienta de encuestas, etc.).
   - Asegúrese de que los identificadores de pregunta quedan reflejados en los campos de datos exportados.

4. **Preparar el libro de Excel**
   - Utilice `plantilla-igm-roi.md` como guía para crear el libro Excel.
   - Configure las hojas `Respuestas`, `Diccionario`, `Ponderaciones`, `IGM_Organizaciones`, `Resumen_Segmentos` y `ROI`.

5. **Recoger y volcar las respuestas**
   - Exporte los datos de la herramienta de encuesta.
   - Impórtelos en la hoja `Respuestas` siguiendo la estructura recomendada.

6. **Calcular indicadores y generar gráficos**
   - Aplique las fórmulas de IGM y puntuaciones por dimensión.
   - Prepare tablas y gráficos para uso interno y para el reporte ejecutivo.

7. **Construir la presentación ejecutiva**
   - Siga el guion descrito en `ppt-reporte.md` para montar su presentación.
   - Incorpore gráficos procedentes del libro de Excel y mensajes clave adaptados a su audiencia.

## 4. Preguntas frecuentes (FAQ)

**P: ¿Es obligatorio utilizar todas las preguntas del cuestionario?**  
R: No, pero es altamente recomendable. Si se eliminan preguntas, revise `mapeo-normas.md` y las ponderaciones del IGM para mantener la coherencia.

**P: ¿Podemos añadir preguntas propias?**  
R: Sí. Puede extender el cuestionario con preguntas adicionales (por ejemplo, específicas de su sector), asignándoles nuevos identificadores y añadiéndolas al diccionario y a las ponderaciones.

**P: ¿Es este kit un sustituto de auditorías formales o pentests?**  
R: No. Es un complemento de diagnóstico que ayuda a saber dónde poner el foco, pero no reemplaza pruebas técnicas ni revisiones de cumplimiento.

**P: ¿Qué hacemos si los resultados son «malos»?**  
R: Felicitarse: ahora disponen de un mapa claro de por dónde empezar. Lo preocupante no es tener áreas rojas; es no saber dónde están.

## 5. Recomendaciones de uso responsable

- Tratar los resultados con **confidencialidad** adecuada: reflejan debilidades que no deben circular alegremente fuera del círculo de responsabilidad.
- Enfocar los hallazgos como **oportunidades de mejora**, no como armas arrojadizas entre departamentos.
- Comunicar a las personas encuestadas el resultado global y las principales conclusiones, como forma de **devolver valor** a su participación.

## 6. Personalización y versiones

Se recomienda mantener un sencillo esquema de versionado, por ejemplo:

- `v1.0` – Primera versión aplicada.
- `v1.1` – Ajustes menores en redacción sin cambios en estructura.
- `v2.0` – Cambios estructurales (nuevas preguntas, reponderación significativa, etc.).

Incluya esta información en la documentación interna y, si es posible, en las propias hojas de cálculo y presentaciones.

## 7. Licencia y créditos

Este kit está pensado para ser reutilizado y adaptado. Siempre que lo modifique:

- Indique la **fuente original** de inspiración.
- Documente claramente sus cambios para que futuros usuarios internos no tengan que hacer arqueología documental.

Y, sobre todo, úselo para impulsar conversaciones informadas, constructivas y (si se puede) un poco más amenas sobre ciberseguridad. Porque hablar de vulnerabilidades y KEV no tiene por qué ser sinónimo de bostezos ni de apocalipsis inevitable.
