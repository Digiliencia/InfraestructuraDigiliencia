# Documentación de Requisitos: WikIA

## Introducción

El proyecto WikIA busca establecer una enciclopedia de ciberseguridad, similar a Wikipedia, utilizando el software MediaWiki. Esta enciclopedia será principalmente generada y mantenida por un modelo de lenguaje grande (LLM), sirviendo tanto como una base de conocimiento para el propio modelo en sus consultas, como una fuente de datos estructurada y accesible al público sobre conceptos de ciberseguridad.

## Requisitos generales

A continuación detallo las requisitos generales.

**Edición y Verificación por Desarrolladores:** Los desarrolladores deben poder visualizar y modificar la enciclopedia para verificar y mejorar la información generada por el modelo.

**Generación Autónoma por el Modelo:** El modelo debe ser capaz de generar nuevas entradas y modificar las existentes de acuerdo a información adquirida de otdiversasras fuentes, por ejemplo, del escrapeo.

**Realización de cambios por los desarrolladores:** La incorporación de entradas podrá realizarse directamente por parte de los desarrolladores, de forma general, añadiendo nuevas entradas y actualizando las existentes a criterio del modelo o de forma específica entradas individuales o conjuntos de ellas. Estos cambios pueden realizarse de forma general (a criterio del modelo) o específica (indicando entradas concretas) y mediante lenguaje natural o explícitamente.

**Grados de verdad:** La información puede tener diferentes "niveles de verdad" o de certeza que determinen la tendencia del modelo a modificar las entradas. En este sentido, las modificacioens manuales tendrían un "nivel de verdad" muy alto, incluso inalterables por parte del modelo. EL objetivo de esto es no saturar la revisión de cambios con infinidad de ellos.

**Control de Versiones y Verificación Previa:** Las ampliaciones de la enciclopedia por parte del modelo deben generar versiones que los desarrolladores deberán verificar antes de ser utilizadas por el LLM o accesibles a los usuarios. Esto es crucial para prevenir el "envenenamiento" del conocimiento.

**Sistema de Control de Versiones:** Debe implementarse un sistema que permita observar y auditar los cambios realizados tanto por el modelo como por los desarrolladores, facilitando así la verificación.

**Referenciación de Contenido:** Toda la información almacenada en la enciclopedia debe estar correctamente referenciada y respaldada por fuentes de información fiables.

**Temática de la información:** La enciclopedia se centrará en información relacionada con la ciberseguridad en un sentido amplio. Esto incluye datos específicos del campo, así como información necesaria para su comprensión (ej. informática básica, divulgación y formación en ciberseguridad).

**Soporte Multilingüe:** A largo plazo, se podría considerar la capacidad de la enciclopedia para ofrecer contenido en múltiples idiomas.

**Optimización del Rendimiento de Búsqueda:** Puesto que la enciclopedia será continuamente accedida tanto por el modelo como por los usuarios es vital, la búsqueda y recuperación de información debe ser rápida y eficiente, incluso a medida que la enciclopedia crezca en volumen de contenido.

**Auditoría y trazabilidad:** Se deben registrar *logs* detallados de cuándo se realizaron modificaciones manuales o verificaciones, complementando el control de versiones del contenido.

**API para Acceso Externo:** El acceso por parte del modelo no tiene porqué ser idéntico al de los usuarios. Podría ser interesante implementar una API para el acceso del modelo a la Wiki. Esto también facilitaría la integración con otras herrameintas.

**Generación Programada de Contenido:** Establecer rutinas para que el modelo genere o actualice contenido en intervalos definidos (ej. diariamente, semanalmente).

**Contenido Interactivo y Multimedia:** A largo plazo se podría integrar recursos multimedia genrados por la propia IA: Permitir la inclusión de elementos multimedia como vídeos cortos explicativos, simulaciones interactivas o laboratorios virtuales básicos que ayuden a los usuarios a comprender mejor ciertos conceptos o técnicas de ciberseguridad.

**Personalización de la Experiencia:** Ligado a la personalización del chatbot, sería interesante que la presentación de la infomración sea adaptable al usuario (nivel de conocimiento, edad...). No obstante, se debe mantener una versión estándar que represente el conocimiento del modelo y sea la base de las demás.