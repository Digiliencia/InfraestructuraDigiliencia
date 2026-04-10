# README — Kit de Encuesta CSCRM España 2026
### Guía de inicio rápido e inventario completo del kit
**Versión 1.0 · Documento (g) del Kit de Encuesta CSCRM**

---

```
 ██████╗███████╗ ██████╗██████╗ ███╗   ███╗    ██╗  ██╗██╗████████╗
██╔════╝██╔════╝██╔════╝██╔══██╗████╗ ████║    ██║ ██╔╝██║╚══██╔══╝
██║     ███████╗██║     ██████╔╝██╔████╔██║    █████╔╝ ██║   ██║   
██║     ╚════██║██║     ██╔══██╗██║╚██╔╝██║    ██╔═██╗ ██║   ██║   
╚██████╗███████║╚██████╗██║  ██║██║ ╚═╝ ██║    ██║  ██╗██║   ██║   
 ╚═════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚═╝  ╚═╝╚═╝   ╚═╝  

     Gestión de Riesgos de Ciberseguridad en la Cadena de Suministro
                     España · 2026 · Versión 1.0
```

---

## ¿Qué es este kit?

El **Kit de Encuesta CSCRM España 2026** es un conjunto integrado de siete instrumentos de investigación, análisis y comunicación diseñados para evaluar, medir y mejorar la madurez de las organizaciones españolas en la **Gestión de Riesgos de Ciberseguridad en la Cadena de Suministro (CSCRM)**.

No es un cuestionario de cumplimiento normativo. No es una auditoría. Es un espejo de diagnóstico que permite a cada organización saber exactamente dónde está, adónde necesita llegar y cuánto le costará —en euros y en meses— el camino.

---

## Inventario del Kit

| Archivo | Documento | Descripción |
|---------|-----------|-------------|
| `CSCRM-encuesta-integral.md` | **(a)** Modelo de Encuesta — Parte 1 | Bloques 0 a VI (perfil, gobernanza, inventario, contratos, supervisión, respuesta, continuidad) |
| `CSCRM-encuesta-p2.md` | **(a)** Modelo de Encuesta — Parte 2 | Bloques VII a XI (SBOM, PQC, IA, Zero Trust, intercambio de información, cumplimiento, madurez global) |
| `CSCRM-guia-metodologica.md` | **(b)** Guía Metodológica | Fundamento epistemológico, diseño muestral, sistema de puntuación IGM, análisis de datos, consideraciones éticas |
| `CSCRM-narrativa-explicativa.md` | **(c)** Narrativa Explicativa | Por qué esta encuesta, por qué ahora, anatomía del problema, contexto normativo español |
| `CSCRM-mapeo-normativo.md` | **(d)** Mapeo Normativo | Tabla completa de correspondencia de cada pregunta con ENS, NIS2, NIST CSF 2.0, ISO 27001:2022, IMC INCIBE-CERT, CRA, PQC, IA |
| `CSCRM-plantilla-igm-roi.md` | **(e)** Plantilla Excel IGM/ROI | Descripción funcional completa del libro Excel de 8 hojas: entrada de datos, cálculo IGM, benchmark, ROI, hoja de ruta, dashboard |
| `CSCRM-reporte-ejecutivo-ppt.md` | **(f)** Reporte Ejecutivo PPT | Estructura de 16 diapositivas para presentación ante Consejo / Comité de Dirección, con notas del presentador |
| `README-CSCRM.md` | **(g)** Este archivo | Guía de inicio rápido, inventario, instrucciones de uso, licencia, contacto |

---

## Inicio Rápido (Quick Start)

### Para el investigador / equipo de ciberseguridad:

```
PASO 1 → Leer la Narrativa Explicativa (c) para comprender el contexto
PASO 2 → Revisar la Guía Metodológica (b) para entender el diseño y la puntuación
PASO 3 → Revisar el Mapeo Normativo (d) para identificar los marcos aplicables
PASO 4 → Distribuir la Encuesta Integral (a) = Parte 1 + Parte 2
PASO 5 → Introducir las respuestas en la Plantilla Excel IGM/ROI (e)
PASO 6 → El Excel genera automáticamente: IGM, benchmark, brecha, hoja de ruta y ROI
PASO 7 → Usar la Plantilla PPT (f) para presentar los resultados a la Dirección
```

### Para el encuestado (CISO / CSO / CIO):

```
1. Leer las Instrucciones Generales al inicio de la Encuesta Integral
2. Cumplimentar los 12 bloques temáticos (tiempo estimado: 45-75 minutos)
3. Ser honesto. La encuesta no audita; diagnostica.
4. Completar el campo abierto P11.6 — es el más valioso de todos.
5. Enviar al responsable de la investigación o introducir en la plataforma digital
```

### Para la Alta Dirección / Consejo de Administración:

```
→ Ir directamente a la Narrativa Explicativa (c): lectura de 15 minutos
→ Ver la Diapositiva 2 del Reporte Ejecutivo (f): "El problema en un número"
→ Revisar las Diapositivas 5, 10 y 13: IGM, ROI y decisiones requeridas
```

---

## Arquitectura del Sistema de Indicadores

```
ENCUESTA (55 preguntas)
    │
    ├── BLOQUE 0: Perfil organizativo (6P)
    │
    ├── DOMINIO GOBERNANZA (Bloques I + parte XI)
    │   ├── P1.1–P1.8: Estrategia, política, roles, formación
    │   └── IGM-G (peso 20%)
    │
    ├── DOMINIO IDENTIFICACIÓN (Bloque II)
    │   ├── P2.1–P2.8: Inventario, clasificación, BIA, n-tier, due diligence
    │   └── IGM-I (peso 20%)
    │
    ├── DOMINIO PROTECCIÓN (Bloques III + VII + VIII)
    │   ├── P3.1–P3.6: Contratos, SBOM, PQC, subcontratistas
    │   ├── P7.1–P7.8: SBOM, PQC, AIBOM, integridad artefactos, drift IA
    │   ├── P8.1–P8.5: Zero Trust, mínimo privilegio, PAM, logging
    │   └── IGM-P (peso 25%)
    │
    ├── DOMINIO DETECCIÓN (Bloque IV)
    │   ├── P4.1–P4.7: Monitorización, ANS, reporte proveedor, tiempo detección
    │   └── IGM-D (peso 20%)
    │
    └── DOMINIO RESILIENCIA (Bloques V + VI + IX + X + XI)
        ├── P5.1–P5.4: PRI con CS, ejercicios, notificación, alternativas
        ├── P6.1–P6.3: BCP, pruebas, RTO real
        ├── P9.1–P9.4: ISACs, cooperación, alertas, evaluaciones coordinadas
        ├── P10.1–P10.5: Gap analysis, ciclo de vida, incidentes, marcos
        └── IGM-R (peso 15%)

IGM GLOBAL = (IGM-G × 0,20) + (IGM-I × 0,20) + (IGM-P × 0,25) + (IGM-D × 0,20) + (IGM-R × 0,15)
```

---

## Marco Normativo de Referencia

Este kit está alineado con los siguientes marcos y normas:

| Marco | Versión | Relevancia |
|-------|---------|------------|
| NIST SP 800-161r1 | Nov. 2024 update | Marco C-SCRM principal de referencia |
| NIST Cybersecurity Framework 2.0 | Feb. 2024 | Subcategorías GV.SC-01 a GV.SC-10 |
| NIST SP 800-55 Vol. 2 | Dic. 2024 | Guía de medición para seguridad de la información |
| ENS RD 311/2022 | May. 2022 | Marco obligatorio España; controles op.ext, POC |
| Anteproyecto Ley Coordinación y Gobernanza Ciberseguridad | Ene. 2025 | Transposición NIS2 España |
| NIS2 (UE 2022/2555) | Oct. 2022 | Marco europeo; Art. 21, 22, 23, 29 |
| ISO/IEC 27001:2022 | Oct. 2022 | Cláusulas 5.19–5.23 (seguridad en relaciones con proveedores) |
| ISO/IEC 27036 | 2021-2023 | Seguridad en relaciones con proveedores (serie completa) |
| IEC 62443 | 2018-2023 | Ciberseguridad en sistemas de automatización industrial (OT) |
| DORA (UE 2022/2554) | En vigor desde ene. 2025 | Resiliencia operativa digital; sector financiero |
| Cyber Resilience Act (CRA) | 2024 | SBOM y requisitos de seguridad para productos digitales |
| INCIBE-CERT IMC v2.8 | Feb. 2023 | 46 métricas de ciberresiliencia; escala L0-L5 |
| CCN-CERT / ISMS Forum Cuestionario Unificado | Feb. 2025 | Modelo español de evaluación de proveedores |
| FAIR Institute | 2025 | Cuantificación de riesgo cibernético (modelo ROI) |
| ENISA NIS Investments 2025 | Dic. 2025 | Benchmarks europeos |
| ENISA NIS360 | Mar. 2025 | Madurez sectorial NIS2 |
| ENISA SBOM Landscape Analysis | Dic. 2025 | Estado del arte SBOM en la UE |
| ACSC AI/ML Supply Chain Guidance | Oct. 2025 | Riesgos IA en cadena de suministro; AIBOM |
| Cipher/Prosegur Supply Chain Report | Feb. 2026 | Indicadores cuantitativos de situación España/global |
| NIST FIPS 203/204/205 | Ago. 2024 | Estándares PQC: ML-KEM, ML-DSA, SLH-DSA |

---

## Preguntas Frecuentes

**¿Cuánto tiempo lleva cumplimentar la encuesta?**
Entre 45 y 75 minutos para un encuestado con conocimiento del estado de ciberseguridad de su organización. Para organizaciones donde el CISO debe consultar con otros departamentos (Compras, Legal, TI), puede requerir hasta 2 horas de trabajo coordinado.

**¿Es obligatorio responder todas las preguntas?**
No. Las preguntas marcadas con (*) son opcionales. Sin embargo, las preguntas no respondidas generarán una puntuación L0 en el cálculo del IGM, lo que puede distorsionar el resultado a la baja.

**¿Con qué frecuencia debe realizarse esta evaluación?**
Se recomienda con carácter anual, idealmente en el primer trimestre de cada año, para poder incorporar los resultados al proceso de planificación estratégica y presupuestaria.

**¿Los resultados son confidenciales?**
Sí. En el contexto de investigación académica, todas las respuestas son tratadas de forma agregada y anonimizada. Las organizaciones que participen individualmente para uso interno conservarán la confidencialidad total de sus resultados.

**¿Este kit sustituye a una auditoría de ciberseguridad?**
No. Es un instrumento de autoevaluación basado en declaración del encuestado. Los resultados son indicativos, no certificatorios. Para una evaluación auditada se recomienda complementar con el proceso de certificación ENS o ISO 27001, o con una auditoría por tercero acreditado.

**¿Puedo adaptar el kit a las necesidades específicas de mi organización?**
Sí, con atribución a las fuentes originales. El kit está diseñado para ser modular: pueden incorporarse preguntas sectoriales adicionales, ajustarse los pesos del IGM según el perfil de riesgo de la organización o integrarse con metodologías propias ya existentes.

**¿Existe versión digital del formulario (Google Forms / Microsoft Forms / LimeSurvey)?**
La versión digital está disponible bajo petición. Contacte con el equipo de investigación para acceder a la versión digital con cálculo automático del IGM y generación automática del informe individual.

---

## Registro de Cambios (Changelog)

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0 | Abr. 2026 | Versión inicial del kit completo |
| 1.1 (prevista) | Oct. 2026 | Actualización benchmarks con ENISA NIS Investments 2026; incorporación requisitos CRA en vigor |
| 1.2 (prevista) | Ene. 2027 | Revisión tras publicación de la Ley de Coordinación y Gobernanza de la Ciberseguridad española |

---

## Licencia y Atribución

Este kit se distribuye bajo licencia **Creative Commons BY-NC-SA 4.0**:
- ✅ Puede usarse libremente con fines académicos, de investigación y no comerciales
- ✅ Puede adaptarse y distribuirse con atribución al trabajo original
- ❌ No puede usarse con fines comerciales sin autorización expresa
- ❌ Las adaptaciones deben distribuirse bajo la misma licencia

**Atribución recomendada:**
> *Kit de Encuesta CSCRM España 2026, v1.0. Elaborado con base en NIST SP 800-161r1, NIST CSF 2.0, INCIBE-CERT IMC v2.8, CCN-CERT/ISMS Forum Cuestionario Unificado (feb. 2025), ENS RD 311/2022, ENISA NIS Investments 2025 y Cipher/Prosegur Supply Chain Report 2026.*

---

## Contacto y Soporte

Para consultas sobre el kit, solicitar la versión digital de la encuesta, participar en el estudio sectorial agregado o solicitar formación en la aplicación del modelo IGM/ROI:

- **Foro Nacional de Ciberseguridad** (DSN): [www.dsn.gob.es](https://www.dsn.gob.es)
- **INCIBE-CERT**: [www.incibe-cert.es](https://www.incibe-cert.es) · Línea 017
- **CCN-CERT**: [www.ccn-cert.cni.es](https://www.ccn-cert.cni.es)
- **ISMS Forum Spain**: [www.ismsforum.es](https://www.ismsforum.es)

---

> *"La cadena de suministro no tiene un problema de tecnología. Tiene un problema de visibilidad. Este kit es, ante todo, un instrumento de visibilidad."*

---

*© 2026 · README del Kit de Encuesta CSCRM España · Documento (g)*
*Versión 1.0 · Abril 2026*
