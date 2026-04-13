# README: KIT DE ENCUESTA MITRE ATLAS
## Guía Completa de Implementación

**Versión:** 1.0  
**Clasificación:** Público - Implementación Operativa  
**Fecha:** Enero 2026

---

## INTRODUCCIÓN

Este README proporciona **guía paso-a-paso** para implementar encuesta nacional ciberseguridad IA (indicadores MITRE ATLAS) en organizaciones españolas.

**Público objetivo:** 400-600 organizaciones (CISOs, responsables seguridad, auditores)  
**Duración encuesta:** 35-45 minutos  
**Idioma:** Español (España)  
**Formato:** Online (Google Forms / Jotform recomendado)  

---

## CONTENIDO KIT ENCUESTA

```
Kit-Encuesta-ATLAS-2026/
├── 1-README.md (este archivo)
├── 2-Estructura-Encuesta.md (13 módulos, 140+ preguntas)
├── 3-Marco-GQM-PRAGMATIC.md (metodología)
├── 4-Matriz-PRAGMATIC-Completa.md (evaluación viabilidad)
├── 5-Mapeo-Preguntas-Normativa.md (regulatorio)
├── 6-Plantilla-Excel-IGM-ROI.md (cálculos)
├── 7-Plantilla-PowerPoint.md (presentación)
├── 8-Formato-Encuesta-GoogleForms.html (implementación)
├── 9-Protocolo-RGPD.md (privacidad datos)
├── 10-Validación-Datos.md (control calidad)
├── 11-Analisis-Estadistico.md (metodología análisis)
├── 12-Reportes-Plantillas.md (salidas)
└── LICENCIA.txt (CC BY-SA 4.0)

TOTAL: 12 documentos .md + 1 HTML
```

---

## GUÍA RÁPIDA IMPLEMENTACIÓN (5 PASOS)

### PASO 1: PREPARACIÓN (Semanas 1-2)

**Tareas:**
- [ ] Revisar este README completamente
- [ ] Leer "Estructura-Encuesta.md" (entender 13 módulos)
- [ ] Validar población target (CISOs España + sectores)
- [ ] Diseñar muestreo estratificado (PYME/Mediana/Grande × sector)
- [ ] Preparar lista contactos respondentes (n=600+ sugerido)

**Artefactos:**
```
Archivo: Target-Orgs-2026.xlsx
├─ Columnas: Empresa | Sector | Tamaño | Email_CISO | Contacto
└─ Filas: n=600+ organizaciones representativas
```

**Deliverable:** Lista contactos verificada, muestra estratificada validada

---

### PASO 2: CONFIGURACIÓN TÉCNICA (Semana 3)

**Tareas:**
- [ ] Crear proyecto Google Forms o Jotform
- [ ] Copiar preguntas encuesta (140+ del archivo "Estructura-Encuesta.md")
- [ ] Configurar lógica condicional (saltos según respuestas)
- [ ] Validar escalas (1-5, nominal, continua)
- [ ] Establecer SLA tiempo completar <45 min
- [ ] Implementar RGPD (consentimiento, privacidad, retención)
- [ ] Testear encuesta en 10 respondentes piloto

**Configuración Google Forms:**
```
Sección 1: Consentimiento RGPD
├─ Checkbox obligatorio: "Acepto tratamiento datos RGPD"
├─ Enlace a Política Privacidad
└─ Identificador anonimizado (ID_Org, no nombre público)

Sección 2: Datos Demográficos
├─ Empresa (opcional, anonimizado después)
├─ Sector (dropdown: 7 opciones)
├─ Tamaño (radio: PYME/Mediana/Grande)
├─ Experiencia CISO (años: 0-2 / 3-5 / 6-10 / >10)
└─ Email contacto (solo para reporte individual)

Secciones 3-15: 13 Módulos Encuesta
├─ M1: Gobernanza (Q1-Q6)
├─ M2: Gestión Activos (Q7-Q11)
├─ M3: Vulnerabilidades (Q12-Q19)
├─ ... (13 módulos total)
└─ Escala Likert 1-5: No implementado / Iniciado / Intermedio / Maduro / Optimizado

Sección 16: Observaciones Abiertas
├─ ¿Principales desafíos ciberseguridad IA?
├─ ¿Inversión planeada 2026?
├─ ¿Obstáculos implementación?
└─ Texto libre (500 caracteres max)

Final: Confirmación + Reporte Personalizado
└─ "Su respuesta fue guardada. Recibirá reporte personalizado en 2 semanas"
```

**Deliverable:** Encuesta online funcional, testada, lista lanzamiento

---

### PASO 3: LANZAMIENTO COMUNICACIÓN (Semana 4)

**Tareas:**
- [ ] Redactar email lanzamiento (ver plantilla abajo)
- [ ] Obtener endorsement AESIA / INCIBE / CCN (credibilidad)
- [ ] Programar envío masivo a 600 contactos
- [ ] Preparar recordatorios (semana 1, semana 2, semana 3)
- [ ] Crear landing page explicativa (por qué importante)
- [ ] Establecer línea soporte técnico

**Plantilla Email Lanzamiento:**

```
ASUNTO: "Encuesta Nacional: Ciberseguridad IA España 2026 (35 min)"

CUERPO:

Estimado [NOMBRE_CISO],

Le invitamos a participar en PRIMERA ENCUESTA NACIONAL de ciberseguridad 
en sistemas de IA, auspiciada por AESIA + INCIBE + CCN.

¿POR QUÉ IMPORTANTE?
• Mapear posición defensiva España vs. tácticas MITRE ATLAS
• Benchmarking sectorial (compararse con pares)
• Diagnóstico individual: score madurez + reporte personalizado
• Input para políticas públicas ciberseguridad IA 2026

¿QUÉ REQUIERE?
• 35-45 minutos de tiempo
• Responder honestamente (no hay "respuesta correcta")
• Datos tratados anónimamente (RGPD compliant)

¿QUÉ OBTIENE?
✓ Reporte personalizado: Score 0-100 + benchmarking vs. sector
✓ Acceso reporte benchmark público (julio 2026)
✓ Contacto con pares similares para best practice sharing
✓ Credibilidad ante reguladores (AESIA)

ENLACE ENCUESTA: [https://forms.google.com/...]
PLAZO RESPUESTA: 31 enero 2026
LÍNEA SOPORTE: encuesta@mitrelatlas.es

¿PREGUNTAS?
Lea FAQ: [enlace]
Contacte: [email + teléfono]

Agradecemos su participación.
AESIA + INCIBE + CCN
```

**Recordatorios (según respuesta):**
- Semana 1: "¿Ha participado? Le recordamos plazo 31 enero"
- Semana 2: "Última semana. 70% participación alcanzada. ¿Se une?"
- Semana 3: "Cierre inminente. 48 horas para responder"

**Deliverable:** Campaña comunicación lanzada, línea soporte operativa

---

### PASO 4: RECOLECCIÓN + VALIDACIÓN (Semanas 5-8)

**Tareas:**
- [ ] Monitorear tasa respuesta diaria
- [ ] Validar datos en tiempo real (ver "Validacion-Datos.md")
- [ ] Identificar respondentes duplicados/inconsistentes
- [ ] Seguimiento no-respondentes (recordatorios dirigidos)
- [ ] Documentar cualidades datos (sesgo, cobertura)
- [ ] Extraer data limpia semanalmente

**Validaciones Automáticas (en Google Forms):**
```
Validación 1: Rango Escala
IF(Respuesta < 1 OR Respuesta > 5) → Error "Escala 1-5 requerida"

Validación 2: Consistencia Lógica
IF(M6_SIEM = "No implementado" AND M3_1_MTTD < 2) 
  → Warning "¿SIEM inexistente pero MTTD bajo?"

Validación 3: Tiempo Mínimo
IF(Tiempo_Respuesta < 15 min) → Flag "Posible respuesta superficial"

Validación 4: Sin Blancos
IF(Count(Blancos) > 5) → Warning "Preguntas no respondidas"

Validación 5: Verificación Email
IF(Email_Format != válido) → Error "Email inválido"
```

**Monitoreo Calidad Semanal:**
```
Métrica | Semana 1 | Semana 2 | Semana 3 | Semana 4 | Meta
--------|----------|----------|----------|----------|------
Respuestas | 45 | 120 | 230 | 380 | 400+
Tasa Validez | 96% | 97% | 98% | 99% | 95%
Cobertura Sector | 3/7 | 5/7 | 7/7 | 7/7 | 100%
Cobertura Tamaño | Grandes | +Medianas | +PYMEs | Completo | Balanced
```

**Deliverable:** Dataset limpio n=400-600, validado, listo análisis

---

### PASO 5: ANÁLISIS + REPORTE (Semanas 9-12)

**Tareas:**
- [ ] Ejecutar análisis estadístico (ver "Analisis-Estadistico.md")
- [ ] Generar IGM scores (ver plantilla Excel)
- [ ] Calcular benchmarking sectorial
- [ ] Identificar hallazgos clave
- [ ] Crear reportes personalizados (1 por respondente)
- [ ] Generar reporte benchmark público
- [ ] Presentación stakeholders (AESIA, boards)

**Estructura Análisis:**
```
Paso 1: Estadística Descriptiva
├─ Media, mediana, desv. estándar por métrica
├─ Distribución scores (histograma)
└─ Percentiles (P25, P50, P75)

Paso 2: Benchmarking
├─ Agregación por sector (7 sectores)
├─ Agregación por tamaño (PYME/Mediana/Grande)
├─ Posición percentil cada org
└─ Identificar líderes + rezagados

Paso 3: Inferencial
├─ Correlación MTTD vs. Incidentes
├─ Regresión: Score Madurez → Probabilidad Incidente
├─ ANOVA: Diferencias significativas sectores
└─ Análisis Factorial: Cargas dimensionales

Paso 4: Cualitativo
├─ Codificación temática observaciones abiertas
├─ Entrevistas profundidad (n~30 CISOs)
├─ Validación hallazgos cuantitativos
└─ Identificación best practices

Paso 5: Reporte
├─ Resumen ejecutivo (2 págs)
├─ Hallazgos principales (10 págs)
├─ Benchmarking sectorial (8 págs)
├─ Recomendaciones (5 págs)
├─ Apéndices metodológicos (5 págs)
└─ Datos anonimizados acceso público
```

**Reportes Personalizados (por org):**
```
REPORTE PERSONALIZADO: [Org Name]
─────────────────────────────────

1. SCORE GENERAL
   IGM Score: [XX/100]
   Categoría: [Muy Fuerte / Fuerte / Moderado / Débil]
   Percentil vs. Pares: [P##]
   Brecha vs. Mediana Sector: [+/- X puntos]

2. HEATMAP 13 MÓDULOS (Tabla 13×1 con colores)
   M1_Gobernanza: [XX/100] ████████░░ Verde/Naranja/Rojo
   M2_Assets: [XX/100]
   ... (13 total)

3. TOP 5 FORTALEZAS
   • M1_Gobernanza (85/100) - Estructura CISO excelente
   • M5_Detección (82/100) - SIEM integrado
   ...

4. TOP 5 GAPS PRIORITARIOS
   • M3_IA_ATLAS (28/100) - Defensas IA inmaduras → Acción urgente Q1
   • M7_SupplyChain (35/100) - Vetting proveedores → Plan Q2
   ...

5. BENCHMARKING
   Posición vs. sector Financiero (n=45):
   - Mediana sector: 62/100
   - Su posición: 55/100 (Percentil 40)
   - Gap: -7 puntos vs. mediana
   - Top 5 Pares: [Lista contactos similar score]

6. ROADMAP 12 MESES SUGERIDO
   Q1 2026: Implementar defensas IA (estim. €100k)
   Q2 2026: Mejorar vetting supply chain (€50k)
   Q3 2026: Consolidar SIEM + monitoreo (€150k)
   Target EOY 2026: 75/100
   Target EOY 2027: 85/100

7. CONTACTOS PEER LEARNING
   Empresas similares (score ±5):
   - BancoY (score 58, P42) - contacto@bancoy.es
   - FinZ (score 52, P38) - ciso@finz.es
   (Solo si consienten compartir contacto)
```

**Reporte Benchmark Público (página web pública):**
```
CIBERSEGURIDAD IA ESPAÑA 2026: BENCHMARK NACIONAL
───────────────────────────────────────────────

HALLAZGOS PRINCIPALES

1. Brecha de Madurez IA
   - Media nacional: 54/100 (MODERADA)
   - Rango: 18-92
   - 25% orgs están en estado CRÍTICO (<40)
   - Solo 8% en estado OPTIMIZADO (>80)
   → Acción: Urgencia mejora defensas IA país

2. Disparidad Sectorial
   Financiero (71/100 media) > Telecom (65) > Manufactura (48) > Educación (38)
   → Oportunidad: Transferir buenas prácticas financiero a otros sectores

3. Brecha PYME-Grande
   Grande: 68/100 | Mediana: 52/100 | PYME: 38/100
   Diferencia: 30 puntos
   → Política: Necesario programa capacitación PYME específico

4. Detección Insuficiente
   % con SIEM: 62%
   MTTD Promedio: 8.2 horas (objetivo 4h)
   % Cobertura Técnicas ATLAS: 48% (objetivo 70%)
   → Inversión: Urgente mejorar SIEM nacional

5. Cumplimiento Regulatorio
   % Conformidad AI Act: 68% (objetivo 90%)
   % Conformidad NIS2: 72% (objetivo 100%)
   → Deadline: Acelerar cumplimiento antes jun 2026

RECOMENDACIONES NACIONALES
1. Programa capacitación PYME ciberseguridad IA (€500k/año)
2. Subsidios SIEM pequeña-mediana empresa (€1M/año)
3. Best practice transfer: Financiero → otros sectores
4. Auditorías AESIA aceleradas entidades críticas
5. Crear panel longitudinal (tracking 2026-2028)

DATOS ANONIMIZADOS DISPONIBLES
[Descargar CSV: empresa_anonimizada | sector | tamaño | score | percentil]

METODOLOGÍA
[Ver documento técnico completo: GQM-PRAGMATIC-Metodologia.md]

CONTACTOS
AESIA: info@aesia.es
INCIBE: ciberseguridad@incibe.es
CCN: contacto@ccn.cni.es

Fecha Reporte: junio 2026
Próxima Actualización: junio 2027
```

**Deliverable:** Reporte benchmark público + reportes personalizados enviados

---

## CRONOGRAMA DETALLADO

```
SEMANA  HITO                        RESPONSABLE    STATUS
──────────────────────────────────────────────────────────
1-2     Preparación + SME review    Equipo diseño   📋
3       Configuración técnica       Dev team        💻
4       Lanzamiento comunicación    Comms           📧
5       Recolección semana 1        Coordinador     📊
6       Recolección semana 2        Coordinador     📊
7       Recolección semana 3        Coordinador     📊
8       Recolección semana 4        Coordinador     📊 ✅ (n=400+)
9-10    Análisis estadístico        Data scientists 📈
11      Entrevistas profundidad     Investigadores  🎤
12      Reportes + presentación     Report team     📑

TOTAL: 12 semanas (3 meses)
```

---

## PREGUNTAS FRECUENTES (FAQ)

### ¿QUIÉN PUEDE RESPONDER?
**R:** Responsables ciberseguridad: CISOs, DPOs, auditorores internos, consultores ciberseguridad (validados).

### ¿CUÁNTO TIEMPO REQUIERE?
**R:** 35-45 minutos. Promedio reportado: 38 minutos.

### ¿ES CONFIDENCIAL?
**R:** Sí. Datos anonimizados, RGPD compliant. Reportes individuales solo para respondente + AESIA (supervisión).

### ¿RECIBO BENEFICIOS?
**R:** Reporte personalizado (score + benchmarking + recomendaciones), acceso reporte público, contacto con pares.

### ¿PUEDO RESPONDER PARCIALMENTE?
**R:** Se recomienda completar, pero aceptamos respuesta parcial. Nota: Incompleto afecta score (se imputa media sectorial).

### ¿CUÁNDO RECIBIRÉ RESULTADO?
**R:** Reporte personalizado en 4-6 semanas post-cierre encuesta. Reporte público en 8 semanas.

---

## CONTACTO + SOPORTE

**Email Soporte:** encuesta@mitrelatlas.es  
**Teléfono:** +34-91-XXXXXXX (INCIBE)  
**Horario:** Lun-Vie 09:00-18:00 CET  
**Línea urgencia:** [teléfono 24/7 si es necesario]

---

## LICENCIA + ATRIBUCIÓN

Este kit es **abierto + reutilizable** bajo licencia CC BY-SA 4.0:
- Atribuir autoría (AESIA + INCIBE + CCN)
- Permitir modificación (con atribución)
- Compartir resultados (anonimizados)

**Citar como:**
```
AESIA, INCIBE, CCN (2026). "Encuesta Nacional Ciberseguridad IA: 
Indicadores MITRE ATLAS". Disponible en [url]. Bajo licencia CC BY-SA 4.0.
```

---

**Kit Encuesta preparado:** Enero 2026  
**Versión:** 1.0  
**Estado:** Listo implementación Q1 2026

