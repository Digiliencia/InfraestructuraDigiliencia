# README del Kit GQM + PRAGMATIC para la encuesta APT

Este repositorio (o conjunto de archivos) contiene todo lo necesario para diseñar, aplicar, analizar y presentar una encuesta de madurez frente a Amenazas Persistentes Avanzadas (APT) a nivel organizativo en España, siguiendo el método **Goal‑Question‑Metric (GQM)** y validando cada métrica con los nueve criterios **PRAGMATIC** (Predictivo, Relevante, Accionable, Genuino, Significativo, Preciso, Oportuno, Independiente y Rentable).

## 📁 Estructura del kit

| Archivo | Descripción |
|---------|-------------|
| `marco_GQM_PRAGMATIC_APT.md` | (a) Marco integrativo: define los Goals nacionales, deriva las Questions y muestra cómo se aplican los criterios PRAGMATIC a cada métrica. |
| `matriz_PRAGMATIC_APT.md` | (b) Matriz de evaluación PRAGMATIC completa: puntuación y justificación para cada métrica bajo los nueve atributos. |
| `narrativa_GQM_PRAGMATIC_APT.md` | (c) Narrativa explicativa: razonamiento de por qué se usa GQM + PRAGMATIC y beneficios para la organización y el ámbito nacional. |
| `mapeo_normativo_GQM_PRAGMATIC_APT.md` | (d) Mapeo detallado de cada pregunta de la encuesta a requisitos normativos (NIS2, NIST CSF 2.0, ISO 27001:2022, ENS/CCN‑STIC, MITRE ATT&CK). |
| `plantilla_excel_GQM_IGM_ROI_APT.md` | (e) Instrucciones para implementar en Excel (o LibreOffice) el cálculo del Índice Global de Madurez (IGM) y el ROI de ciberseguridad, usando únicamente las métricas aprobadas por GQM + PRAGMATIC. |
| `plantilla_PPT_GQM_PRAGMATIC_APT.md` | (f) Guía de diapositivas para un Reporte Ejecutivo en PowerPoint (o Google Slides/Keynote) que comunica los resultados a alta dirección. |
| `README_GQM_PRAGMATIC_APT.md` | (g) Este archivo: presentación del kit, instrucciones de uso y pasos siguientes. |

## 🚀 Cómo usar el kit

1. **Revisar el Marco (a)**  
   - Entender los Goals nacionales de resiliencia frente a APT.  
   - Ver cómo cada pregunta de la encuesta responde a una Question concreta y qué métrica se propone.  

2. **Consultar la Matriz PRAGMATIC (b)**  
   - Verificar que cada métrica propuesta cumple con los atributos de calidad.  
   - Si alguna métrica obtiene una puntuación baja en algún atributo, considerar ajustarla o descartarla.  

3. **Leer la Narrativa (c)** para internalizar la filosofía del enfoque y poder explicarla a stakeholders.  

4. **Confirmar el Mapeo a Normativas (d)**  
   - Asegurarse de que la encuesta también cumple con los requerimientos legales y de buenas prácticas (NIS2, etc.).  
   - Este mapeo es útil para auditorías o para demostrar alineamiento con marcos de referencia.  

5. **Implementar la Plantilla Excel (e)**  
   - Crear el libro de trabajo siguiendo las indicaciones de las hojas **1_Respuestas**, **2_Puntuaciones**, **3_IGM_Cálculo** y **4_ROI_Escenarios**.  
   - Usar listas desplegables y validación de datos para asegurar consistencia.  
   - Ejecutar el cálculo del IGM y del ROI bajo diferentes escenarios de mejora.  

6. **Generar el Reporte PowerPoint (f)**  
   - Tomar los valores de IGM, sub‑índices por bloque, métricas operativas (MTTD, MTTR, etc.) y ROI de la hoja de Excel.  
   - Rellenar las diapositivas de la plantilla con los gráficos y tablas sugeridas.  
   - Añadir el logo institucional y ajustar los colores según la guía de estilo de su organización.  

7. **Distribuir y aplicar la encuesta**  
   - Utilizar el modelo de encuesta del informe APT previo (o adaptarlo según su sector).  
   - Recopilar las respuestas (Google Forms, Microsoft Forms, LimeSurvey, etc.) y exportarlas a CSV para importarlas a la hoja **1_Respuestas** del libro de Excel.  

8. **Analizar y comunicar**  
   - Calcular el IGM_global y los sub‑índices de bloque.  
   - Interpretar los resultados respecto a los Goals nacionales (ver tabla de Goals en el Marco).  
   - Elaborar el informe ejecutivo usando la plantilla de PowerPoint y compartirlo con la alta dirección, comités de riesgo y, si procede, con órganos reguladores (ej. INCIBE, CCN‑CERT).  

9. **Plan de mejora**  
   - Basarse en las áreas con IGM_b bajo (< 0.4) para definir proyectos concretos (mejorar gobernanza, automatizar parcheo, incrementar capacidades de detección TTPs, etc.).  
   - Establecer objetivos de mejora trimestrales y usar la encuesta en rondas sucesivas para medir el avance.  

## 🛠️ Requisitos técnicos

- **Hoja de cálculo**: Microsoft Excel 2016+ o LibreOffice Calc (las fórmulas usan funciones estándar: PROMEDIO, SUMPRODUCTO, SI, BUSCARV, etc.).  
- **Encuesta**: cualquier herramienta que permita exportar respuestas a CSV/TSV (Google Forms, Microsoft Forms, SurveyMonkey, LimeSurvey, etc.).  
- **Presentación**: Microsoft PowerPoint, Google Slides o Apple Keynote.  
- **Conexión a internet** solo necesaria para descargar plantillas o actualizar referencias; el cálculo se realiza totalmente offline.  

## 📄 Licencia y uso

El contenido de este kit se ofrece bajo una **licencia CC‑BY‑4.0** (Atribución).  
Usted es libre de:
- **Compartir** — copiar y redistribuir el material en cualquier medio o formato.  
- **Adaptar** — remixar, transformar y crear obras derivadas a partir del material.  

Bajo la condición de dar **crédito adecuado**, proporcionar un enlace a la licencia y indicar si se realizaron cambios.  
Se recomienda mantener la referencia a los marcos originales (NIS2, NIST CSF, ISO 27001, MITRE ATT&CK, etc.) en cualquier obra derivada.

## 📬 Soporte y retroalimentación

Si tiene preguntas, desea reportar un error o sugerir mejoras, por favor:
- Abrir un *issue* en el repositorio (si está alojado en Git/Gitlab).  
- Enviar un correo a: **apt-survey@ejemplo.es** (ejemplo de dirección de contacto).  

Agradecemos su interés en elevar la resiliencia de las organizaciones españolas frente a las APT. ¡Que los datos guíen mejores decisiones!

---  
*Última actualización: 7 abril 2026*  