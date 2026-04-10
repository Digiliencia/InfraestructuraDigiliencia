# README — KIT DE ENCUESTA FISMA 2025
## Guía de Inicio Rápido y Documentación del Paquete Completo
### Diagnóstico de Madurez en Ciberseguridad Institucional para España

---

```
╔══════════════════════════════════════════════════════════════════════════════╗
║          KIT DE ENCUESTA FISMA 2025 — DIAGNÓSTICO DE MADUREZ               ║
║          Ciberseguridad Institucional · España · Enfoque Autonómico         ║
║          Versión 1.0 · Abril 2026                                           ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## ¿QUÉ ES ESTE KIT?

Este kit es un **instrumento completo de diagnóstico, análisis y comunicación** del nivel de madurez en ciberseguridad de organizaciones públicas y privadas en España, con especial énfasis en las Comunidades Autónomas y las Administraciones Locales.

Está construido sobre los **FY2025 IG FISMA Reporting Metrics v2.0** (publicados el 3 de abril de 2025), el estándar de medición de madurez en ciberseguridad institucional más riguroso disponible a nivel mundial, adaptado al contexto normativo español: **ENS (RD 311/2022)** y **Directiva NIS2** (en transposición mediante el Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad, enero 2025).

No es otro cuestionario de cumplimiento. Es una herramienta de diagnóstico que produce datos accionables, conversaciones estratégicas y planes de mejora medibles.

---

## ESTRUCTURA DEL KIT: LOS 7 DOCUMENTOS

```
kit-encuesta-fisma-2025/
│
├── (a) encuesta-fisma-modelo.md
│       Modelo de encuesta integral con 60 preguntas en 14 módulos
│
├── (b) guia-metodologica.md
│       Metodología, codificación, análisis estadístico y consideraciones éticas
│
├── (c) narrativa-explicativa.md
│       Por qué existe esta encuesta, qué mide y qué hacer con los resultados
│
├── (d) mapeo-normativo.md
│       Tabla de correspondencia: cada pregunta ↔ FISMA ↔ ENS ↔ NIS2 ↔ NIST SP
│
├── (e) plantilla-igm-rosi.md
│       Diseño completo de la hoja de cálculo Excel: IGM + ROSI + POA&M
│
├── (f) reporte-ejecutivo-ppt.md
│       Plantilla PowerPoint completa: 18 diapositivas descritas en detalle
│
└── (g) README.md
        Este fichero
```

---

## GUÍA DE INICIO RÁPIDO

### Para el CISO / Responsable de Seguridad:

**¿Por dónde empiezo?**

1. Lea la **Narrativa Explicativa** `(c)` para entender el propósito del instrumento y cómo comunicarlo a su organización.
2. Revise el **Mapeo Normativo** `(d)` para verificar que las preguntas cubren los requisitos que su organización necesita evaluar.
3. Personalice el **Modelo de Encuesta** `(a)` si necesita añadir preguntas específicas de su sector o eliminar módulos no aplicables.
4. Implemente la **Plantilla Excel** `(e)` para calcular el IGM y el ROSI de su organización.
5. Presente los resultados usando la **Plantilla PowerPoint** `(f)`.

### Para el Investigador / Analista:

1. Lea la **Guía Metodológica** `(b)` en su totalidad antes de diseñar el plan de muestreo.
2. Utilice el **Modelo de Encuesta** `(a)` como instrumento base; documente cualquier adaptación realizada.
3. El **Mapeo Normativo** `(d)` le permitirá justificar la validez de contenido del instrumento ante revisores académicos.
4. La **Plantilla Excel** `(e)` incluye las fórmulas de cálculo del IGM para procesamiento cuantitativo de resultados.

### Para el Directivo / Jefe de Área:

1. Lea la **Narrativa Explicativa** `(c)` — especialmente la Parte III ("El coste de no actuar").
2. Solicite al CISO que complete la encuesta versión directiva (Módulos I, II, IX, XII, XIV).
3. Revise el **Reporte Ejecutivo** `(f)` como formato de presentación de resultados.

---

## DESCRIPCIÓN DETALLADA DE CADA DOCUMENTO

### (a) Modelo de Encuesta Integral — `encuesta-fisma-modelo.md`

**Contenido:** 60 preguntas organizadas en 14 módulos temáticos.

**Módulos:**
| # | Módulo | Preguntas | Función FISMA | Marco normativo principal |
|---|---|---|---|---|
| I | Gobernanza de la Ciberseguridad | P1-P5 | GOVERN | ENS Art. 13 / NIS2 Art. 20 |
| II | Gestión Cadena de Suministro (C-SCRM) | P6-P10 | GOVERN | ENS Art. 19 / NIS2 Art. 21.2.d |
| III | Gestión de Riesgos y Activos | P11-P14 | IDENTIFY | ENS op.exp.1 / MAGERIT |
| IV | Gestión de Configuración | P15-P18 | PROTECT | ENS mp.eq.3 / CIS Controls |
| V | IDAM y Zero Trust | P19-P23 | PROTECT | ENS mp.acc / CISA ZTMM v2.0 |
| VI | Protección de Datos y Privacidad | P24-P27 | PROTECT | LOPDGDD / RGPD / NIST FIPS |
| VII | Formación y Concienciación | P28-P30 | PROTECT | ENS Art. 15-16 / NIST NICE |
| VIII | Monitorización Continua (ISCM) | P31-P35 | DETECT | ENS Art. 24 / CDM Program |
| IX | Respuesta a Incidentes | P36-P40 | RESPOND | ENS Art. 25 / NIS2 Art. 23 |
| X | Continuidad de Negocio | P41-P44 | RECOVER | ENS Art. 26 / ISO 22301 |
| XI | Cumplimiento Normativo | P45-P48 | Transversal | ENS Cert. / NIS2 / LOPDGDD |
| XII | Métricas y Madurez | P49-P52 | Transversal | FISMA 5 niveles / INES CCN |
| XIII | Tendencias Emergentes | P53-P55 | DETECT/IDENTIFY | CTI / IA / PQC |
| XIV | Reflexión Estratégica (Abierto) | P56-P60 | Transversal | Análisis cualitativo |

**Versiones disponibles:**
- **Versión completa:** 60 preguntas, todos los módulos (45-60 min)
- **Versión abreviada:** Módulos I, II, IX, XII (15 preguntas, 20 min)
- **Versión directiva:** Módulos I, II, IX, XI, XII, XIV (20 preguntas, 25 min)

---

### (b) Guía Metodológica — `guia-metodologica.md`

**Contenido:** Instrucciones completas para administrar, codificar y analizar la encuesta.

**Secciones principales:**
- Fundamentos metodológicos y marco teórico
- Población objetivo y modalidades de aplicación
- Sistema de codificación A-E → 1-5 puntos
- Ponderaciones por módulo para el cálculo del IGM
- Cálculo del ROI/ROSI con metodología ALE
- Correspondencia perfil del respondente → módulos aplicables
- Análisis cuantitativo (univariado, bivariado, regresión)
- Análisis cualitativo de preguntas abiertas
- Validación del instrumento (alfa Cronbach, validez contenido, test-retest)
- Consideraciones éticas y protección de datos (RGPD)
- Tamaños muestrales por Comunidad Autónoma
- Cronograma de implementación (20 semanas)

---

### (c) Narrativa Explicativa — `narrativa-explicativa.md`

**Contenido:** Documento de contexto, justificación y guía de uso de los resultados.

**Audiencia:** Directivos, investigadores, policy-makers, comunicadores.

**Partes:**
- Parte I: El problema de las métricas ausentes en España
- Parte II: Por qué FISMA como referencia; arquitectura de los 14 módulos; el tono del instrumento
- Parte III: Qué hacer con los resultados (organización individual, investigador, policy-maker)
- Parte IV: Las preguntas implícitas que la encuesta plantea

---

### (d) Mapeo Normativo — `mapeo-normativo.md`

**Contenido:** Cuatro tablas de correspondencia normativa exhaustiva.

**Tablas incluidas:**
- **Tabla 1:** Mapeo completo pregunta ↔ Dominio FISMA ↔ Función CSF 2.0 ↔ ENS ↔ NIS2 ↔ NIST SP (60 filas)
- **Tabla 2:** Cobertura de los 29 indicadores FISMA FY2025 por pregunta de la encuesta
- **Tabla 3:** Cobertura del ENS artículo por artículo del RD 311/2022
- **Tabla 4:** Cobertura de la Directiva NIS2 artículo por artículo

**Uso principal:** Validación de contenido del instrumento para publicación académica; justificación de la cobertura normativa ante auditores o reguladores.

---

### (e) Plantilla IGM y ROSI — `plantilla-igm-rosi.md`

**Contenido:** Diseño completo de libro Excel con 8 pestañas.

**Pestañas descritas:**
1. INICIO — Portada e instrucciones
2. DATOS_ORG — 13 campos de datos de la organización
3. RESPUESTAS — Codificación de las 60 respuestas con fórmulas SI anidadas
4. IGM_CALCULO — Índice Global de Madurez ponderado + gráfico radar
5. ROSI_CALCULO — Cálculo de ALE, ROSI, payback y VAN a 3 años
6. DASHBOARD — Panel visual de KPIs con formato condicional de color
7. BENCHMARKS — Datos sectoriales de referencia (España + EU + FISMA EE.UU.)
8. POA_M — Plan de Acción y Mejora con priorización automática

**Fórmulas clave incluidas:**
- IGM ponderado: `Σ(Puntuación_media_módulo × Ponderación)`
- ROSI: `(ALE_antes - ALE_después - Coste_control) / Coste_control`
- VAN 3 años: `VNA(8%, ahorro_año1, ahorro_año2, ahorro_año3) - inversión_inicial`
- Priorización POA&M: función SI anidada con 4 niveles (CRÍTICA/ALTA/MEDIA/BAJA)

---

### (f) Plantilla Reporte Ejecutivo — `reporte-ejecutivo-ppt.md`

**Contenido:** Descripción diapositiva a diapositiva de una presentación PowerPoint de 18+5 slides.

**Estructura:**
- Diapositivas 1-4: Contexto, metodología, portada
- Diapositivas 5-8: Resultados principales (IGM, radar, tabla, benchmarks)
- Diapositivas 9-11: Hallazgos críticos, análisis de riesgo, acciones prioritarias
- Diapositivas 12-15: Hoja de ruta, marco normativo, comparativa FISMA/ENS/NIS2, amenazas emergentes
- Diapositivas 16-18: Decisiones propuestas, fuentes, cierre
- Diapositivas 19-23 (opcionales): Detalle técnico ampliado

**Paleta de colores:** Azul corporativo #003366 | Rojo alerta #DC2626 | Ámbar #D97706 | Verde efectivo #16A34A

---

### (g) README — `README.md`

**Contenido:** Este documento. Guía de inicio rápido, descripción del kit y referencias.

---

## BASES NORMATIVAS DEL KIT

| Documento | Organismo | Fecha | Relevancia |
|---|---|---|---|
| FY2025 IG FISMA Reporting Metrics v2.0 | CIGIE / OMB / CISA | 3 abril 2025 | Marco métrico primario |
| OMB Memorándum M-25-04 | OMB / White House | 14 enero 2025 | Guía de reporte FY2025 |
| NIST Cybersecurity Framework 2.0 | NIST | Febrero 2024 | Estructura de funciones y dominios |
| NIST SP 800-53 Rev. 5 | NIST | Septiembre 2020 | Controles técnicos de referencia |
| NIST SP 800-207 (Zero Trust) | NIST | Agosto 2020 | Arquitectura Zero Trust |
| CISA Zero Trust Maturity Model v2.0 | CISA | Abril 2023 | Métricas ZTA suplementarias |
| Real Decreto 311/2022 (ENS) | Gobierno de España | 3 mayo 2022 | Marco normativo español |
| Directiva UE 2022/2555 (NIS2) | Parlamento Europeo | 14 diciembre 2022 | Marco europeo |
| Anteproyecto Ley Coord. y Gobernanza Ciberseg. | DSN / Gobierno España | 14 enero 2025 | Transposición NIS2 |
| ENISA NIS Investments 2025 | ENISA | Diciembre 2025 | Benchmarks europeos |
| CCN-CERT Informe Ciberamenazas 2025 | CCN-CERT / CNI | 2025 | Contexto nacional |
| INCIBE Balance Ciberseguridad 2025 | INCIBE | Febrero 2026 | Estadísticas nacionales |

---

## LICENCIA Y CONDICIONES DE USO

Este kit se distribuye bajo licencia **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**:

- ✅ **Permitido:** Usar, copiar, distribuir y adaptar el instrumento para fines de investigación, docencia y autodiagnóstico no comercial.
- ✅ **Permitido:** Publicar resultados basados en este instrumento citando la fuente.
- ❌ **No permitido:** Uso comercial sin autorización expresa del equipo investigador.
- 📝 **Requisito:** Citar el instrumento como: *"Kit de Encuesta FISMA 2025 — Diagnóstico de Madurez en Ciberseguridad Institucional, Versión 1.0, Abril 2026. Basado en FY2025 IG FISMA Reporting Metrics v2.0, NIST CSF 2.0, ENS RD 311/2022 y Directiva NIS2."*

---

## CÓMO CITAR ESTE KIT

**Formato APA 7:**
> Consorcio de Investigación FISMA 2025. (2026). *Kit de Encuesta para el Diagnóstico de Madurez en Ciberseguridad Institucional basado en Indicadores FISMA FY2025: Aplicación territorial en España*. Versión 1.0. Publicación independiente.

**Formato IEEE:**
> Consorcio de Investigación FISMA 2025, "Kit de Encuesta para el Diagnóstico de Madurez en Ciberseguridad Institucional basado en Indicadores FISMA FY2025," Versión 1.0, abril 2026.

---

## CONTACTO Y ACTUALIZACIONES

**Versiones futuras previstas:**

- **v1.1 (Q3 2026):** Incorporación de primeros datos empíricos de la encuesta piloto; calibración de benchmarks con datos reales.
- **v2.0 (2027):** Actualización a FY2026 FISMA Metrics; incorporación de métricas PQC (criptografía post-cuántica); extensión al sector privado NIS2.

**Para reportar errores, sugerir mejoras o solicitar colaboración:**
Dirigirse al equipo investigador a través de los canales institucionales indicados en el protocolo de investigación asociado.

---

## AGRADECIMIENTOS

Este kit no habría sido posible sin la generosidad intelectual de:
- El **NIST**, por publicar sus marcos de referencia en acceso abierto.
- El **CCN-CERT** y el **INCIBE**, por sus informes anuales que proveen el contexto nacional.
- La **ENISA**, por su trabajo de benchmarking europeo en el informe NIS Investments 2025.
- Los **Inspectores Generales federales** que publican sus auditorías FISMA cada año, demostrando que la transparencia y el rigor no son incompatibles con la seguridad nacional.
- Y todos los CISOs, directivos y responsables de seguridad que, cada día, hacen el trabajo invisible de mantener en pie los sistemas de los que dependen los ciudadanos.

---

```
Kit de Encuesta FISMA 2025 · Versión 1.0 · Abril 2026
"Medir es el primer acto de inteligencia."
```
