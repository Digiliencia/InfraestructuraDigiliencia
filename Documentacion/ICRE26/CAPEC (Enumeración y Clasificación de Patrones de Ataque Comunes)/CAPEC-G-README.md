# 📦 README — KIT DE ENCUESTA CAPEC-ESP 2026
## Guía de Inicio Rápido y Referencia del Consorcio de Investigación
### Kit de Encuesta CAPEC-ESP · Documento G · Versión 1.0 · Abril 2026

---

> *«El conocimiento que no se mide no se gestiona. El riesgo que no se nombra no se mitiga. Y la encuesta que no se distribuye no sirve de nada por bien diseñada que esté. Bienvenido/a al kit que lo hace todo posible.»*

---

## ¿QUÉ ES ESTE KIT?

El **Kit de Encuesta CAPEC-ESP 2026** es el primer instrumento de investigación en español diseñado específicamente para medir la adopción, uso y madurez del marco **CAPEC (Common Attack Pattern Enumeration and Classification) de MITRE** en organizaciones españolas, en el contexto del nuevo ecosistema regulatorio europeo (NIS2, DORA, ENS).

El kit produce como resultado central el **IGM-CAPEC** (Índice Global de Madurez CAPEC), un indicador compuesto que permite a cualquier organización:

1. Conocer su nivel real de adopción de CAPEC en una escala de 1 a 5
2. Compararse con organizaciones del mismo sector y tamaño (benchmarking)
3. Identificar sus brechas más críticas y priorizarlas para la acción
4. Cuantificar el ROSI (Return on Security Investment) de sus controles
5. Demostrar alineación con los requisitos de NIS2, ENS y DORA ante auditores y reguladores

---

## CONTENIDO DEL KIT

El kit contiene **7 documentos** en formato Markdown (`.md`), diseñados para ser usados en flujo secuencial:

| Documento | Archivo | Descripción breve |
|---|---|---|
| **A** | `CAPEC-A-encuesta.md` | Cuestionario completo: 50 preguntas en 11 secciones |
| **B** | `CAPEC-B-metodologia.md` | Diseño estadístico, validación y plan de análisis |
| **C** | `CAPEC-C-narrativa.md` | Contexto, justificación y preguntas incómodas |
| **D** | `CAPEC-D-mapeo-normativo.md` | Correspondencias con NIS2, ENS, DORA, ISO 27001 |
| **E** | `CAPEC-E-excel-IGM-ROI.md` | Plantilla Excel de cálculo IGM + ROSI (8 hojas) |
| **F** | `CAPEC-F-reporte-ppt.md` | Estructura de presentación ejecutiva (18+6 slides) |
| **G** | `CAPEC-README.md` | Este archivo — guía de inicio y referencia |

---

## GUÍA DE INICIO RÁPIDO

### Si eres el CISO o responsable de ciberseguridad que quiere autoevaluarse:

```
1. Leer el Documento C (narrativa) — 15 minutos para entender el contexto
2. Cumplimentar el Documento A (encuesta) — 35-45 minutos
3. Introducir las respuestas en el Documento E (Excel) — 20 minutos
4. Obtener el IGM-CAPEC y el dashboard ejecutivo automáticamente
5. Usar el Documento F (PowerPoint) para presentar al Consejo
```

### Si eres un investigador que quiere aplicar la encuesta a una muestra:

```
1. Leer el Documento B completo (metodología)
2. Someter el instrumento (Documento A) a validación por panel de expertos
3. Realizar el estudio piloto (n=50) y ajustar
4. Distribuir mediante los canales recomendados (ver Sección 5)
5. Importar respuestas al Documento E para análisis agregado
6. Revisar el Documento D para el análisis de cumplimiento normativo
```

### Si eres consultor de ciberseguridad que aplica el kit a un cliente:

```
1. Compartir el Documento C con el cliente (narrativa explicativa)
2. Administrar el Documento A mediante entrevista guiada (más rico que autocompletar)
3. Calcular el IGM-CAPEC con el Documento E
4. Generar el reporte con el Documento F, adaptado a la audiencia (Consejo / Regulador / Técnico)
5. Usar el Documento D para mapear brechas a obligaciones normativas específicas
```

---

## ÁRBOL DE DECISIÓN: ¿QUÉ DOCUMENTO NECESITO?

```
¿Quiero saber qué preguntas hace la encuesta?
    └─→ Documento A

¿Quiero entender la base científica del instrumento?
    └─→ Documento B

¿Quiero convencer a alguien de la importancia de participar?
    └─→ Documento C

¿Quiero vincular las preguntas a obligaciones legales concretas?
    └─→ Documento D

¿Quiero calcular el IGM-CAPEC y el ROI de mis controles?
    └─→ Documento E (Excel)

¿Quiero presentar los resultados al Consejo?
    └─→ Documento F (PowerPoint)

¿Estoy buscando el punto de partida?
    └─→ Estás aquí: Documento G (este README)
```

---

## FLUJO DE TRABAJO COMPLETO

```
DISTRIBUCIÓN          RECOGIDA           ANÁLISIS          OUTPUT
     ↓                    ↓                  ↓                ↓
[Doc C Narrativa]   [Doc A Encuesta]   [Doc E Excel]   [Doc F PPT]
     ↓                    ↓                  ↓                ↓
Comunicación a      Cumplimentación     IGM-CAPEC +     Reporte al
la audiencia        de respuestas       Sub-índices     Consejo /
objetivo                                                Regulador
                         ↓                  ↓
                    [Doc B Metodología] [Doc D Mapeo]
                    Validación del      Análisis de
                    instrumento         cumplimiento
```

---

## BASES CIENTÍFICAS DEL INSTRUMENTO

El kit está construido sobre las siguientes fuentes primarias y marcos de referencia:

| Marco / Fuente | Uso en el kit |
|---|---|
| **MITRE CAPEC v3.9** | Base taxonómica principal: 559 patrones, 9 mecanismos, 6 dominios |
| **ENISA Threat Landscape 2025** | Datos de referencia para amenazas emergentes y posicionamiento de España |
| **INCIBE Balance de Ciberseguridad España 2025** | Estadísticas nacionales de incidentes (122.223 incidentes, +26%) |
| **NIS2 Directiva (UE) 2022/2555** | Marco regulatorio principal; Art. 21.2 como eje del mapeo normativo |
| **ENS RD 311/2022** | Marco nacional; todas las secciones de cumplimiento para sector público |
| **DORA Reglamento (UE) 2022/2554** | Resiliencia operacional digital para el sector financiero |
| **NIST CSF 2.0** | Función de Identificación (ID.RA) y Gestión de Riesgos (GV.RM) |
| **NIST AI 100-2e2025** | Taxonomía de ataques adversariales a sistemas de IA |
| **NIST FIPS 203/204/205 (PQC)** | Estándares de criptografía post-cuántica; preparación quantum |
| **ISO/IEC 27001:2022** | Sistema de gestión de seguridad de la información |
| **ISO/IEC 42001:2023** | Gestión de sistemas de inteligencia artificial |
| **GQM (Basili, Caldiera & Rombach, 1994)** | Metodología de diseño del instrumento |
| **Alpha de Cronbach (1951) / Omega de McDonald (1999)** | Validación de fiabilidad del instrumento |
| **Lawshe (1975)** | Validez de contenido (CVR/CVI) |

---

## CANALES DE DISTRIBUCIÓN RECOMENDADOS

Para maximizar la representatividad muestral:

| Canal | Alcance | Tipo de entidad | Responsable de contacto |
|---|---|---|---|
| **INCIBE** | Nacional — sector empresarial | Empresas de todos los sectores | Área de empresas INCIBE |
| **CCN-CNI** | Nacional — sector público | Administraciones Públicas, FCS, Defensa | Subdirección CCN |
| **ISMS Forum Spain** | CISOs y directivos de seguridad | Grandes empresas y multinacionales | Secretaría ISMS Forum |
| **ISACA Spain Chapter** | Profesionales GRC y auditoría | Auditores, Compliance Officers | ISACA Spain |
| **(ISC)² Spain** | Profesionales certificados | CISOs, Arquitectos, Pentesters | Delegación España |
| **AMETIC** | Industria tecnológica | Empresas de tecnología y telecomunicaciones | Área de ciberseguridad |
| **LinkedIn** | Amplia cobertura | Todos los roles | Campaña patrocinada |
| **AENA, REE, CNMC** | Infraestructuras críticas | Operadores estratégicos | Contacto directo |
| **Universidades** | Investigación | Grupos de investigación en ciberseguridad | Redes universitarias |

---

## CONSIDERACIONES ÉTICAS Y PROTECCIÓN DE DATOS

### Principios de tratamiento
- **Anonimización:** Cada respuesta recibe un código alfanumérico. El correo del respondente (si se recoge para envío de resultados) se dissocia del cuestionario antes del análisis.
- **Minimización:** Solo se recogen datos profesionales relevantes para la investigación. Sin datos personales identificativos directos.
- **Proporcionalidad:** Los datos recogidos son estrictamente los necesarios para calcular el IGM-CAPEC y responder a las 5 preguntas de investigación definidas en el Documento B.
- **Seguridad:** Almacenamiento en servidor bajo jurisdicción española, cifrado en reposo (AES-256), acceso restringido al equipo investigador.

### Consentimiento
El formulario incluye checkbox de consentimiento explícito al inicio, conforme al Art. 6.1.a del RGPD. El consentimiento puede retirarse antes de la publicación de los resultados enviando un correo al equipo investigador con el código de encuesta.

### DPIA
Si la muestra incluye operadores de infraestructuras críticas o entidades ENS de categoría ALTA, se realizará una DPIA conforme al Art. 35 RGPD antes del inicio de la recogida de datos.

---

## LICENCIA DE USO

```
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
(CC BY-NC-SA 4.0)
```

**Puedes:**
- Compartir — copiar y redistribuir el material en cualquier medio o formato
- Adaptar — remezclar, transformar y construir sobre el material

**Bajo las siguientes condiciones:**
- **BY (Atribución):** Citar la fuente con la cita APA recomendada (ver abajo)
- **NC (No Comercial):** No usar el material con fines comerciales sin autorización expresa
- **SA (Compartir Igual):** Si adaptas el material, distribúyelo bajo la misma licencia

**Cita APA recomendada:**

```
Consorcio de Investigación CAPEC-ESP. (2026). Kit de Encuesta CAPEC-ESP 2026:
Instrumento para la medición de la adopción de patrones de ataque en 
organizaciones españolas (Versión 1.0). [Kit de investigación]. 
Publicado bajo licencia CC BY-NC-SA 4.0.
```

---

## REGISTRO DE VERSIONES

| Versión | Fecha | Cambios principales |
|---|---|---|
| 1.0 | Abril 2026 | Versión inicial completa. 50 ítems, 7 documentos, IGM-CAPEC con 5 sub-índices |

---

## CONTRIBUCIONES Y CONTACTO

Para sugerir mejoras al instrumento, reportar errores o proponer colaboraciones institucionales:

- Abrir una *issue* en el repositorio del kit (si está alojado en GitHub o equivalente)
- O contactar al equipo investigador a través de los canales institucionales indicados en el protocolo de distribución

**Contribuciones especialmente bienvenidas:**
- Traducciones validadas del instrumento (inglés, francés, portugués, alemán)
- Adaptaciones sectoriales (versión DORA para sector financiero, versión OT para sector industrial)
- Datos de benchmarking de estudios equivalentes en otros países de la UE
- Validación del instrumento en muestras de otros países para un índice IGM-CAPEC europeo comparable

---

## PREGUNTAS FRECUENTES

**¿Es obligatorio completar las 50 preguntas?**
No. El cuestionario acepta completitud mínima del 80% para ser incluido en el análisis. Las secciones más críticas para el IGM-CAPEC son I, III, V y VI.

**¿Cuánto tiempo lleva completar la encuesta?**
Entre 35 y 45 minutos para un CISO con conocimiento directo del estado de su organización. Puede reducirse a 20 minutos si solo se completan las secciones de mayor relevancia para el puesto del respondente.

**¿Cómo se garantiza la confidencialidad de mi organización?**
Los datos se analizan exclusivamente en forma agregada. No se publicará ningún dato que permita identificar a una organización específica. Los resultados sectoriales solo se publican cuando el grupo contiene n ≥ 10 organizaciones.

**¿Puedo adaptar la encuesta para uso interno en mi organización?**
Sí, bajo los términos de la licencia CC BY-NC-SA 4.0. Debes citar la fuente y no comercializar la adaptación sin autorización.

**¿Qué pasa si no conozco CAPEC en absoluto?**
La encuesta está diseñada para capturar esa realidad. Las respuestas de "no uso / no conozco" son igualmente valiosas estadísticamente, y la narrativa explicativa (Documento C) proporciona el contexto suficiente para completar el instrumento con rigor.

**¿El kit estará disponible en inglés?**
La versión 1.0 está en español. La versión en inglés (Kit CAPEC-EU Survey 1.0-EN) está planificada para el segundo semestre de 2026.

---

## AGRADECIMIENTOS

El diseño de este kit incorpora conocimiento colectivo de la comunidad de práctica de ciberseguridad española e internacional. Se agradece especialmente la contribución conceptual de:

- El equipo de MITRE ATT&CK/CAPEC por mantener el catálogo como bien público global
- INCIBE y CCN-CERT por su trabajo en datos de referencia nacionales
- ENISA por su Threat Landscape como marco de referencia europeo
- La comunidad académica de investigadores en ciberseguridad que ha sentado las bases metodológicas para instrumentos de medición de madurez

---

*Kit de Encuesta CAPEC-ESP · Documento G: README · Versión 1.0 · Abril 2026*
*Licencia: CC BY-NC-SA 4.0 · Idioma: Español*
