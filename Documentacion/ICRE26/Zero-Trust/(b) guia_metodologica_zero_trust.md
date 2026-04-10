# Guía metodológica de la Encuesta de Madurez Zero Trust

## 1. Objetivo de la encuesta

El objetivo de esta encuesta es medir de forma estructurada y comparable el grado de madurez de las organizaciones en la adopción del modelo Zero Trust, tanto en España como en otros países, alineando las respuestas con marcos de referencia internacionales (NIST SP 800-207, CISA, ENISA) y con la normativa aplicable (ENS, NIS2, DORA, RGPD, etc.). [web:51][web:53][web:47]

La encuesta se orienta a responsables con visión global de la organización (CISO, CIO, responsables de riesgo, OT, etc.) y busca capturar:  
- Nivel de adopción estratégica de Zero Trust.  
- Madurez por pilares (identidad, dispositivos, red, aplicaciones y datos).  
- Indicadores de monitoreo, respuesta y resiliencia.  
- Alineamiento con requisitos normativos y de ciberseguro.  
- Percepción cultural y barreras prácticas.  

## 2. Marco conceptual

La encuesta se inspira en los principios de Zero Trust definidos por NIST SP 800-207 (no confiar nunca, verificar siempre, asumir compromiso, aplicar el mínimo privilegio y realizar decisiones de acceso continuas), así como en los modelos de madurez propuestos por CISA, el Departamento de Defensa de EE. UU. y marcos de evaluación europeos de estrategias nacionales de ciberseguridad. [web:51][web:49][web:53]

A su vez, se alinea con las prioridades de la Década Digital Europea y el informe país España 2025, que sitúan la ciberseguridad y la confianza digital como pilares para la digitalización de la economía y el sector público. [web:47][web:52]

## 3. Población objetivo y tamaño muestral

### 3.1. Población objetivo

- Entidades sujetas a NIS2 (operadores de servicios esenciales, entidades importantes, proveedores críticos).  
- Organismos de la administración pública estatal, autonómica y local, sujetos al ENS.  
- Empresas privadas medianas y grandes con fuerte dependencia digital.  
- Proveedores de servicios TIC, cloud y de ciberseguridad.  

### 3.2. Tamaño muestral recomendado

Para obtener resultados estadísticamente significativos a nivel país, se recomienda:  
- Al menos 200–300 respuestas en el caso de España, con representación equilibrada por sector y tamaño.  
- Estratificación por sector crítico (energía, finanzas, sanidad, administración pública) para análisis comparativos.  

## 4. Estructura de la encuesta

La encuesta se organiza en once bloques:  
- Datos generales de la organización.  
- Visión estratégica y marco Zero Trust.  
- Identidad y acceso.  
- Dispositivos y endpoints.  
- Red, ZTNA y microsegmentación.  
- Aplicaciones, nube y cargas de trabajo.  
- Datos, clasificación y protección.  
- Monitorización, respuesta y resiliencia.  
- Cumplimiento normativo, riesgo y ciberseguro.  
- Cultura, formación y estado de ánimo Zero Trust.  
- Indicadores cuantitativos adicionales.  

Cada bloque alimenta un subconjunto de indicadores de madurez, que se consolidan en un Índice Global de Madurez (IGM) y en un cálculo aproximado del retorno de la inversión (ROI) en iniciativas Zero Trust.

## 5. Escalas de respuesta y ponderaciones

### 5.1. Escalas de madurez

Muchas preguntas utilizan escalas ordinales de cinco niveles (de “inexistente” a “avanzado”) que pueden codificarse como valores numéricos 0–4 o 1–5, según el modelo analítico escogido. Se sugiere una codificación 0–4 para facilitar interpretaciones donde 0 indica ausencia y 4 indica madurez avanzada.

Ejemplo:  
- 0 = No existe / No se aplica.  
- 1 = Inicial / Ad hoc.  
- 2 = Parcial / Básico.  
- 3 = Sistemático.  
- 4 = Avanzado / Dinámico / Automatizado.  

### 5.2. Ponderación por pilares

Se recomienda asignar ponderaciones a cada pilar, por ejemplo:  
- Identidad y acceso: 25 %.  
- Dispositivos y endpoints: 15 %.  
- Red y ZTNA: 20 %.  
- Aplicaciones y cargas de trabajo: 20 %.  
- Datos y protección de la información: 20 %.  

Estas ponderaciones se pueden ajustar según sector (por ejemplo, más peso en OT para industria, más peso en datos para sanidad y finanzas).

### 5.3. Tratamiento de “no aplica” y “no medido”

Las respuestas que indiquen “no aplica” deben tratarse como valores ausentes y no penalizar ni beneficiar artificialmente la madurez. Las respuestas “no medido” sí reflejan una carencia de gobernanza y deberían ponderarse como el nivel más bajo de madurez para esa dimensión.

## 6. Recogida de datos

### 6.1. Canal de encuesta

- Plataforma en línea (preferentemente con soporte para exportación a CSV/Excel).  
- Garantizar anonimato o seudonimización cuando sea requerido.  
- Ofrecer versión en varios idiomas si se realiza un estudio comparativo internacional.  

### 6.2. Consentimiento y confidencialidad

- Informar al encuestado de los objetivos, uso de datos y medidas de protección.  
- Garantizar que los datos se utilizarán con fines estadísticos y de mejora de políticas, no para auditoría punitiva.  

## 7. Cálculo del Índice Global de Madurez (IGM)

### 7.1. Definición

El IGM es una métrica agregada (0–100) que refleja el grado de madurez Zero Trust de la organización. Se construye a partir de:  
- Puntuación media por pilar (escala 0–4),  
- Ponderaciones por pilar,  
- Normalización final a escala 0–100.  

### 7.2. Fórmula general

1. Asignar un valor 0–4 a cada respuesta relevante.  
2. Calcular el promedio por pilar (identidad, dispositivos, red, aplicaciones, datos).  
3. Aplicar ponderaciones a cada pilar.  
4. Calcular el IGM total como suma ponderada y multiplicar por 25 para obtener escala 0–100.  

IGM ≈ (Σ (puntuación_pilar × peso_pilar)) × 25  

Ejemplo: si cada pilar tiene media 3 (sobre 4) y los pesos suman 1, el IGM sería 75.

### 7.3. Segmentación por tipos de organización

Es recomendable calcular IGM separados por:  
- Sector.  
- Tamaño de organización.  
- Tipo (público/privado).  
- Aplicabilidad de NIS2 / ENS.  

## 8. Estimación del ROI de Zero Trust

### 8.1. Lógica básica

El ROI de iniciativas Zero Trust puede estimarse como la relación entre beneficios (reducción de costes de incidentes, reducción de primas de ciberseguro, mayor disponibilidad) e inversión en las iniciativas.

ROI (%) ≈ ((Beneficios anuales atribuibles a Zero Trust − Coste anual de Zero Trust) / Coste anual de Zero Trust) × 100  

### 8.2. Estimación de beneficios

Se pueden usar las preguntas 11.1–11.4 de la encuesta:  
- Número de incidentes antes/después de Zero Trust.  
- Coste medio por incidente.  
- Inversión anual aproximada en Zero Trust.  

Con la evidencia de estudios industriales, se pueden asumir rangos orientativos de reducción de incidentes o impacto (por ejemplo, 30–60 % de reducción en determinados tipos de ataques cuando se alcanzan niveles avanzados de madurez). [web:18][web:26]

### 8.3. Uso en análisis actuarial

Los resultados del IGM, combinados con los datos de incidentes y ciberseguro, pueden alimentar modelos de riesgo actuarial para ajustar primas, franquicias y coberturas, siguiendo prácticas emergentes en el mercado europeo. [web:26][web:45]

## 9. Calidad de los datos y sesgos

- Sesgo de autoselección: es probable que respondan más las organizaciones con mayor sensibilidad a la ciberseguridad.  
- Sesgo de optimismo: los responsables pueden valorar su madurez de forma más positiva que una auditoría externa.  
- Sesgo de sector: algunos sectores (finanzas, energía) tienden a estar más regulados y avanzados.  

Se recomienda:  
- Complementar la encuesta con entrevistas cualitativas.  
- Contrastar resultados con auditorías y métricas objetivas cuando sea posible.  

## 10. Presentación de resultados

- Informes sectoriales (energía, finanzas, sanidad, etc.).  
- Comparativa territorial (por país o región autonómica).  
- Mapas de calor por pilar y nivel de madurez.  
- Casos de éxito y lecciones aprendidas.  

Todo ello, idealmente, narrado con un equilibrio sano entre rigor técnico y el ligero sarcasmo que exige hablar de “confianza” en un mundo de ciberataques diarios.