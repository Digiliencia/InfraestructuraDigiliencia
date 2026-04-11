# README – Kit de Encuesta de Ciberseguridad, Continuidad de Negocio y Ciber‑Resiliencia

Bienvenido al **Kit de Encuesta**, un conjunto de herramientas diseñado para ayudar a tu organización (o conjunto de organizaciones) a:

- Diagnosticar su nivel de madurez en ciberseguridad y continuidad.
- Compararse consigo misma en el tiempo y, si se desea, con otras entidades.
- Priorizar acciones de mejora e inversiones con criterio.

Este README explica **qué contiene el kit, cómo usar cada pieza y en qué orden**.

---

## 1. Contenidos del kit

El kit está compuesto por los siguientes elementos en formato Markdown:

1. `encuesta-modelo.md`  
   Modelo completo de encuesta, con todas las preguntas y opciones de respuesta.

2. `guia-metodo.md`  
   Guía metodológica para aplicar la encuesta, puntuarla y calcular el Índice Global de Madurez (IGM).

3. `narrativa-exp.md`  
   Narrativa explicativa para acompañar la encuesta (correo de invitación, mensajes a la dirección, FAQ, etc.).

4. `mapeo-normas.md`  
   Tabla de mapeo de cada pregunta con los principales marcos normativos (ENS, NIS2, DORA, ISO 27001, ISO 22301, etc.).

5. `plantilla-igm-roi.md`  
   Descripción de la plantilla Excel para cálculo del IGM, índices por dominio y modelado sencillo de ROI.

6. `ppt-reporte.md`  
   Plantilla conceptual para construir un reporte ejecutivo en PowerPoint u otra herramienta de presentación.

Este README es el **manual de instrucciones** para orquestar todos estos componentes.

---

## 2. Orden recomendado de uso

### Paso 1. Adaptar la encuesta a tu contexto

- Abre `encuesta-modelo.md`.
- Revisa secciones, preguntas y opciones de respuesta.
- Adapta, si es necesario:
  - Terminología sectorial (por ejemplo, salud, energía, administración local).
  - Referencias a regulaciones específicas adicionales.
  - Número de preguntas, si necesitas reducir o ampliar el alcance.

> Consejo: Mantén los **códigos de pregunta (GOV‑01, BCM‑03, etc.)**, aunque cambies el texto, para preservar la compatibilidad con el mapeo normativo y la plantilla Excel.

### Paso 2. Preparar la campaña de encuesta

- Lee `narrativa-exp.md` y selecciona/ajusta el texto de invitación a:
  - Participantes técnicos (CISO, TI, BCM, riesgos).
  - Alta dirección (nota ejecutiva).
- Decide la **modalidad de aplicación**:
  - Entrevistas estructuradas.
  - Autoevaluación guiada.
  - Enfoque mixto.

### Paso 3. Construir la plantilla de recogida de datos

- Usa `plantilla-igm-roi.md` como guía para crear el archivo Excel (o herramienta equivalente):
  - Hoja `Diccionario_Preguntas` con todos los códigos e información básica.
  - Hoja `Datos_Respuestas` para registrar las contestaciones.
  - Hojas `Cálculos_Madurez`, `ROI_Costes_Beneficios` y `Cuadro_Mando` para el análisis.

### Paso 4. Aplicar la encuesta

- Sigue los pasos de `guia-metodo.md`:
  - Definir ámbito, participantes y calendario.
  - Estimar duración por sesión.
  - Gestionar discrepancias con elegancia y sin juicios sumarísimos.

### Paso 5. Cargar y revisar datos

- Volcar las respuestas en la hoja `Datos_Respuestas`.
- Comprobar que las fórmulas de puntuación y de cálculo de IMD/IGM funcionan según lo esperado.
- Corregir errores de codificación (por ejemplo, respuestas fuera de a–d).

### Paso 6. Analizar resultados

- Usar `guia-metodo.md` para interpretar IMD y IGM.
- Apoyarse en `mapeo-normas.md` para identificar:
  - Preguntas con implicaciones regulatorias significativas.
  - Dominios con mayor brecha frente a ENS, NIS2, DORA o ISO.

### Paso 7. Preparar el reporte ejecutivo

- Basarse en `ppt-reporte.md` para estructurar una presentación clara:
  - Foto global.
  - Detalle por dominios clave.
  - Riesgos de incumplimiento.
  - Plan de acción y roadmap.

---

## 3. Roles recomendados en el proyecto

Para sacar el máximo partido al kit, conviene asignar ciertos roles (que pueden solaparse en organizaciones pequeñas):

- **Patrocinio ejecutivo**: miembro de la alta dirección que avala el ejercicio.
- **Coordinación del proyecto**: responsable de riesgos, ciberseguridad o continuidad que lidera la iniciativa.
- **Equipo técnico**: especialistas de ciberseguridad, TI, BCM, riesgos, cumplimiento.
- **Soporte de datos / analítica**: persona que se encarga de la plantilla Excel y cuadros de mando.

---

## 4. Versionado y mantenimiento

Este kit está pensado para **evolucionar en el tiempo**.

Se recomienda:

- Mantener un **control de versiones** (por ejemplo, usar un repositorio Git interno o numerar versiones en los ficheros).
- Actualizar:
  - Preguntas de la encuesta cuando cambien las prioridades o el contexto tecnológico.
  - El mapeo normativo (`mapeo-normas.md`) cuando se actualicen ENS, NIS2, DORA o las normas ISO.
  - La plantilla Excel cuando se incorporen nuevos indicadores o fórmulas de ROI.

---

## 5. Buenas prácticas de uso

- Emplear la encuesta **al menos una vez al año** para medir progreso.
- Compartir resultados de forma **transparente pero constructiva**: mostrar también las fortalezas, no sólo las carencias.
- Evitar usar los resultados como arma arrojadiza entre áreas; la idea es **hablar de procesos, no de culpables**.
- Combinar el diagnóstico con otras fuentes de información:
  - Resultados de auditorías.
  - Incidentes reales.
  - Evaluaciones de riesgos y pruebas técnicas.

---

## 6. Preguntas frecuentes sobre el kit

**¿Podemos añadir o quitar preguntas?**  
Sí. La encuesta es una base sólida, no un dogma. Sólo se recomienda mantener los **códigos de identificación** para conservar compatibilidad con el mapeo y la plantilla de datos.

**¿Este kit sustituye a una auditoría formal?**  
No. Es un **instrumento de autoevaluación estructurada** y de apoyo a auditorías, no un sustituto de éstas.

**¿Se puede usar entre varias organizaciones (por ejemplo, a nivel nacional o sectorial)?**  
Sí. De hecho, está diseñado para poder comparar resultados entre organizaciones de forma agregada, siempre que se respeten los códigos de pregunta y el modelo de datos.

**¿Qué pasa si no queremos calcular ROI de forma cuantitativa?**  
Nada grave. Las secciones relacionadas con ROI pueden usarse de forma cualitativa, pero animamos a intentarlo; incluso estimaciones gruesas ayudan a argumentar inversiones.

---

## 7. Cierre

Si has llegado hasta aquí, enhorabuena: ya dominas la teoría. Ahora viene la parte interesante: **poner en marcha el kit, recoger datos y conversar sobre lo que revelan**.

La ciber‑resiliencia no es una foto fija, sino una película. Este kit aspira a ser, al menos, una buena cámara y un guion decente. El final feliz dependerá de lo que hagáis con lo que descubráis.