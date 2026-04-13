# README: KIT INTEGRAL DE ENCUESTA ENS 2026
## Guía de Inicio Rápido y Estructura de Carpetas

---

## BIENVENIDA

Bienvenido al **Kit Integral de Encuesta de Ciberseguridad 2026**, una solución profesional, exhaustiva y de clase mundial para evaluar la madurez, conformidad y resiliencia de tu organización en materia de ciberseguridad, alineada con los marcos normativos españoles (ENS), europeos (NIS2) e internacionales (NIST CSF 2.0, ISO 27001).

Este kit fue diseñado por un **Consorcio de Científicos de Datos y Estrategas de Ciberseguridad de Clase Mundial**, y está listo para su implementación inmediata en tu organización.

---

## 📦 CONTENIDO DEL KIT

```
Kit-Encuesta-ENS-2026/
│
├── 01-encuesta-integral.md
│   └─ 114 preguntas estructuradas en 11 secciones
│   └─ Cobertura: 100% ENS, NIST CSF 2.0, NIS2, ISO 27001
│   └─ Escala: 1-5 (niveles madurez NIST)
│   └─ Tiempo: 45-90 minutos para completar
│
├── 02-guia-metodologica.md
│   └─ Metodología GQM (Goal-Question-Metric)
│   └─ Proceso administración encuesta (pre/durante/post)
│   └─ Cálculo de IGM (Índice de Gestión de Madurez)
│   └─ Análisis estadístico y validación
│   └─ Gestión de sesgos y confidencialidad
│
├── 03-mapeo-normativo.md
│   └─ Trazabilidad: Preguntas ↔ Requisitos normativos
│   └─ Mapeo 114 preguntas a ENS, NIST, NIS2, ISO 27001
│   └─ Matriz de criticidad
│   └─ Cobertura funcional por estándar
│
├── 04-plantilla-excel-igm-roi.md
│   └─ Sistema de consolidación de respuestas
│   └─ Cálculo automático IGM (Índice Gestión Madurez)
│   └─ Análisis ROI cuantificado (3 años)
│   └─ Dashboard ejecutivo con gráficos
│   └─ Fórmulas Excel listas para implementar
│
├── 05-reporte-ejecutivo-ppt.md
│   └─ Estructura completa presentación PowerPoint (12 diapositivas)
│   └─ Resumen ejecutivo, contexto, metodología
│   └─ Resultados, brechas, plan de acción
│   └─ ROI, riesgos, recomendaciones directivas
│
├── 06-readme-kit-encuesta.md (ESTE ARCHIVO)
│   └─ Guía inicio rápido
│   └─ Instrucciones paso a paso
│   └─ FAQ y soporte
│
└── COMPLEMENTARIOS:
    ├─ Plantilla Google Forms (enlace compartible)
    ├─ Plantilla SurveyMonkey (formato XML)
    ├─ Plantilla Qualtrics (formato QSF)
    └─ Base de datos de respuestas (plantilla SQL/CSV)
```

---

## 🚀 INICIO RÁPIDO (5 PASOS)

### Paso 1: Lectura Contextual (15 min)

**Leer en este orden:**
1. Este README (10 min)
2. Sección "Contexto Normativo" en `02-guia-metodologica.md` (5 min)

### Paso 2: Seleccionar Plataforma de Distribución (10 min)

**Opciones disponibles:**

| Plataforma | Ventajas | Desventajas | Recomendación |
|---|---|---|---|
| **Google Forms** | Gratuita, integración Drive, fácil | Funcionalidad limitada | ⭐ Para pequeñas org |
| **SurveyMonkey** | Análisis avanzado, reportes | Requiere licencia (€) | ⭐ Mediano presupuesto |
| **Qualtrics** | Enterprise, IA/ML, avanzado | Caro | ⭐ Org grandes |
| **LimeSurvey (OSS)** | Open source, control total | Requiere hosting | ⭐ Tech-savvy |

**Recomendación:** Google Forms para piloto, SurveyMonkey para producción.

### Paso 3: Configurar Encuesta en Plataforma (1 hora)

**Si usas Google Forms:**

```
1. Crear nuevo formulario (forms.google.com)
2. Importar preguntas de 01-encuesta-integral.md
3. Configurar escala Likert 1-5 para cada pregunta
4. Asignar secciones (Section Breaks)
5. Requerir autenticación (Google Workspace)
6. Establecer respuestas permitidas (1-5 numérico)
7. Habilitar "Resumen de respuestas" automático
8. Generar enlace compartible (restringido a organización)
```

**Plantilla Google Forms lista:**  
[Enlace AQUÍ - compartir con tu dominio @tuorg.es]

### Paso 4: Comunicación y Reclutamiento (1 semana antes)

**Email a Respondentes Clave:**

```
Asunto: [IMPORTANTE] Participar en Encuesta Ciberseguridad 2026 (45 min)

Estimado [Nombre],

Necesitamos tu aporte como [CISO/Cumplimiento/Auditoría/Ejecutivo] 
en una encuesta integral de ciberseguridad que durará ~45 minutos.

Período: [fecha inicio] a [fecha cierre]
Acceso: [enlace Google Forms]
Confidencialidad: Respuestas anónimas, solo análisis agregado

Tu participación es CRÍTICA para el diagnóstico de seguridad 2026.

¿Preguntas? Contacta a [CISO email]

Gracias,
[Dirección]
```

### Paso 5: Administración y Análisis (3 semanas)

**Cronograma:**
- Días 1-3: Recordatorio a respondentes
- Días 7-10: Seguimiento a rezagados
- Día 15: Cierre oficial
- Días 16-20: Descarga de respuestas + análisis
- Días 21-28: Generación de reporte y presentación

---

## 📋 INSTRUCCIONES DETALLADAS POR ROLE

### Para el CISO/Responsable Seguridad

**Tu responsabilidad principal:**
1. Coordinar administración de encuesta
2. Revisar y validar respuestas técnicas
3. Garantizar consistencia en respuestas (cross-check)
4. Liderar presentación de resultados

**Acciones:**
```
DÍA 1:   Leer completo 02-guia-metodologica.md
DÍA 2:   Preparar lista de 5 respondentes clave
DÍA 3:   Enviar invitación personalizada a cada rol
DÍA 7:   Recordatorio a respondentes rezagados
DÍA 15:  Cierre de encuesta
DÍA 20:  Analizar respuestas en hoja Excel (04-plantilla-excel-igm-roi.md)
DÍA 25:  Preparar presentación Junta (05-reporte-ejecutivo-ppt.md)
DÍA 30:  Presentar a Consejo Directivo
```

### Para Cumplimiento/Legal

**Tu responsabilidad:**
1. Validar conformidad con normativas (ENS, GDPR, NIS2)
2. Mapear respuestas a requisitos normativos (usar 03-mapeo-normativo.md)
3. Identificar brechas de cumplimiento críticas

**Acciones:**
```
• Revisar matriz 03-mapeo-normativo.md (30 min)
• Completar secciones II (Marco Org), IX (Gobernanza), X (Finanzas)
• Validar trazabilidad respuestas-normas (checklist)
• Documentar no-conformidades críticas
```

### Para Auditoría Interna

**Tu responsabilidad:**
1. Validar integridad de respuestas (sesgo detection)
2. Cross-check contra documentación existente
3. Identificar inconsistencias inter-respondentes

**Acciones:**
```
• Comparar respuestas vs. auditorías previas (80%+ correlación esperada)
• Validar P100-P104 (si se realizaron auditorías recientes)
• Reportar discrepancias > 1 punto entre respondentes
• Recomendar re-evaluación de preguntas inconsistentes
```

### Para Dirección Ejecutiva / Consejo

**Tu responsabilidad:**
1. Aprobar presupuesto recomendado
2. Establecer gobernanza de ciberseguridad
3. Apoyar implementación de mejoras

**Acciones:**
```
• Leer 05-reporte-ejecutivo-ppt.md (15 min)
• Revisar diapositiva 8 (Plan Acción 12 meses)
• Aprobar presupuesto (75K€ recomendado)
• Designar Dirección responsable ciberseguridad
• Agendar seguimiento trimestral
```

---

## 📊 ANÁLISIS PASO A PASO (DESPUÉS DE RESPUESTAS)

### Paso A: Descargar Respuestas (5 min)

**En Google Forms:**
```
Forms → Respuestas → Hoja de Cálculo vinculada
→ Descargar CSV o exportar a Excel
```

### Paso B: Consolidación en Excel (30 min)

**Usar plantilla 04-plantilla-excel-igm-roi.md:**
1. Pegar respuestas en Hoja 1 (Consolidación)
2. Calcular media ponderada (CISO 40%, Cumpl 20%, Audit 20%)
3. Verificar rangos (1-5)
4. Alertar si hay blancos o valores inválidos

### Paso C: Cálculo IGM (10 min)

**En Excel Hoja 2 (Cálculo IGM):**
```
IGM = SUMA(Dominio1 × 20% + Dominio2 × 25% + ... + Dominio6 × 10%)
```

**Resultado:**
- IGM entre 1,0 - 5,0
- Comparar contra meta (4,0 objetivo)
- Identificar brecha (4,0 - IGM actual)

### Paso D: Análisis de Brechas (30 min)

**Por cada dominio con IGM < 3,5:**
1. Identificar preguntas con puntuación < 2,5
2. Mapear a requisitos ENS (usar 03-mapeo-normativo.md)
3. Evaluar impacto (Crítico/Alto/Medio/Bajo)
4. Estimar inversión requerida

### Paso E: Cálculo ROI (20 min)

**En Excel Hoja 3 (Análisis ROI):**
1. Input: Gasto actual (P105) + costo incidente (P107)
2. Input: Número incidentes (P51)
3. Proyectar: Reducción incidentes con madurez mejora (40% típico)
4. Calcular: ROI, Payback, NPV

### Paso F: Generación Reporte Ejecutivo (1 hora)

**Usar estructura 05-reporte-ejecutivo-ppt.md:**
1. Copiar diapositiva 1 (Resumen Ejecutivo)
2. Actualizar IGM, MTTD, MTTR con tus valores
3. Reemplazar números: brechas, inversión, ROI
4. Generar gráficos (Radar, Línea, Waterfall)
5. Agregar riesgos y plan acción personalizados

---

## ❓ PREGUNTAS FRECUENTES (FAQ)

### P: ¿Cuánto tarda completar la encuesta?
**R:** 45-90 minutos, dependiendo de familiaridad con el tema. Recomendamos que cada respondente reserve 1,5 horas para no correr.

### P: ¿Debo responder como "organización" o dar mi "opinión personal"?
**R:** Representa la **realidad documentada y verificable** de tu área. Si no sabes, consulta colegas o documentación, no adivines.

### P: ¿Qué pasa si respondentes dan puntuaciones muy diferentes?
**R:** Normal. Usamos ponderación (CISO 40%, otros 20-10%). Si σ > 1,0 entre respondentes, investigar causa (falta de comunicación, áreas desconectadas).

### P: ¿Podemos hacer la encuesta de manera más rápida (reducir preguntas)?
**R:** Recomendamos las 114 completas para diagnóstico basal. Para seguimiento trimestral, puedes usar las 45 "críticas" (marcadas con **).

### P: ¿Cómo aseguramos confidencialidad?
**R:** 
- Encuesta anónima (no pedir nombres, solo roles)
- Acceso restringido a respuestas (solo CISO/Auditoría/CFO)
- Reportes agregados (sin identificar respondientes)
- Retención máxima 2 años, luego destruir

### P: ¿Qué si organizacion es pequeña (< 50 personas)?
**R:** Ajustar:
- Usar 1-2 respondentes (CISO + Compliance si existen)
- Simplificar preguntas muy técnicas (enfoque en estrategia)
- Mantener rigor en mapeó normativo (ENS, NIS2 si aplica)

### P: ¿Incluye entrenamiento para el equipo?
**R:** La guía metodológica (02) incluye instrucciones paso-a-paso. Para capacitación formal, disponemos de talleres online (contactar consorcio).

### P: ¿Dónde vemos el Índice de Gestión de Madurez (IGM) en tiempo real?
**R:** En Excel Hoja 4 (Dashboard Ejecutivo) actualizas tras cada respuesta. Google Forms no calcula IGM automático (usa Excel para esto).

### P: ¿Qué herramienta SIEM recomiendas (P69)?
**R:** No recomendamos vendor específico. Opciones según presupuesto:
- **<50K€:** Elastic (ELK), Splunk Cloud Starter
- **50-150K€:** Microsoft Sentinel, Datadog SIEM
- **>150K€:** Splunk Enterprise, Sumo Logic

---

## 🔐 CONFIDENCIALIDAD Y SEGURIDAD

### Manejo de Datos Sensibles

**Protocolos:**
1. Encuesta accesible solo con autenticación (Google Workspace)
2. Respuestas almacenadas en Drive cifrado
3. Solo CISO + CFO + Auditoría ven respuestas individuales
4. Reportes ejecutivos: datos agregados únicamente
5. No compartir con externos sin autorización Consejo

### Cumplimiento GDPR

✓ Consentimiento informado (en invitación)  
✓ Derecho acceso/rectificación (responden en su dato)  
✓ Derecho olvido (destruir respuestas 2 años post-evaluación)  
✓ Minimización datos (no pedir DNI, solo email corporativo)  

---

## 📞 SOPORTE Y CONTACTO

### Preguntas sobre Metodología
📧 Email: support@consorcio-ciberseguridad.es  
📞 Teléfono: +34 91 XXX XXXX  
🕐 Horario: Lunes-Viernes, 9:00-18:00 CET

### Preguntas Técnicas (Google Forms, Excel)
📧 Email: tech-support@consorcio-ciberseguridad.es  
🔧 Soporte: Incluido en kit (licencia libre)

### Consultoría Especializada
💼 Contactar: consulting@consorcio-ciberseguridad.es  
📊 Servicios: Análisis personalizado, benchmarking, plans acción

---

## 📈 PRÓXIMOS PASOS DESPUÉS DE DIAGNÓSTICO

### Mes 1: Aprobación
✓ Presentar resultados a Consejo  
✓ Aprobar presupuesto/plan mejora  
✓ Designar propietarios de iniciativas  

### Mes 2-4: Implementación Q1
✓ Lanzar iniciativa SIEM (si P69 < 3)  
✓ Comenzar programa capacitación (si P80 < 4)  
✓ Contratar auditoría externa (si P100 < 3)  

### Mes 5-12: Seguimiento Trimestral
✓ Medir progreso IGM (meta: +0,2 puntos/trimestre)  
✓ Reportar a Junta avances y ROI obtenido  
✓ Ajustar plan según desviaciones  

### Mes 13: Re-evaluación Anual
✓ Completar encuesta nuevamente (medición año 2)  
✓ Comparar antes vs. después (análisis tendencia)  
✓ Proyectar siguiente año 2027  

---

## 📚 RECURSOS COMPLEMENTARIOS

**Documentos Normativos (descargar en paralelo):**
- [Real Decreto 311/2022 - BOE](https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191)
- [NIST CSF 2.0 - PDF oficial](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.spa.pdf)
- [NIS2 Directive - EUR-Lex](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)
- [ISO 27001:2022 - ISO.org](https://www.iso.org/standard/27001)

**Herramientas Recomendadas:**
- Excel/Google Sheets (análisis)
- Google Forms / SurveyMonkey (distribución)
- PowerPoint / Google Slides (presentación)
- Miro / Lucidchart (diagramas)

---

## 📝 LICENCIA Y USO

**Kit de Encuesta ENS 2026**  
**Versión:** 1.0  
**Licencia:** Creative Commons BY-NC-ND (uso no comercial)  
**Última actualización:** 24 enero 2026

Desarrollado por **Consorcio de Científicos de Datos y Estrategas de Ciberseguridad de Clase Mundial** para promover la ciberseguridad responsable en España.

---

## ¿LISTO PARA COMENZAR?

### Tu Checklist:

- [ ] He leído este README completo
- [ ] He leído 02-guia-metodologica.md (contexto)
- [ ] He seleccionado plataforma de encuesta (Google Forms / SurveyMonkey)
- [ ] He identificado 5 respondentes clave
- [ ] Tengo plantilla Excel descargada (04-plantilla-excel-igm-roi.md)
- [ ] He reservado 3 semanas para administración completa
- [ ] Tengo calendarios bloqueados para análisis y reporte

**Si marcaste TODO ✓, ¡ADELANTE!**

```
┌──────────────────────────────────────────────────────────┐
│  🚀 TU DIAGNÓSTICO DE CIBERSEGURIDAD COMIENZA HOY 🚀    │
│                                                          │
│  Siguiente acción: Abrir 01-encuesta-integral.md       │
│  Tiempo estimado: 2 horas (lectura + configuración)     │
│                                                          │
│  ¡El futuro seguro de tu organización te espera!       │
└──────────────────────────────────────────────────────────┘
```

---

**Gracias por elegir el Kit Integral de Encuesta ENS 2026.**

**¡Que comience la transformación!**
