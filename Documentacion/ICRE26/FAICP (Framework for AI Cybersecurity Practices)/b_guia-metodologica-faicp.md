# 🔬 GUÍA METODOLÓGICA DETALLADA
## Encuesta FAICP 2025–2026: Protocolo de Diseño, Aplicación, Análisis y Validación

---

> *"Una encuesta bien diseñada es una conversación diferida con cientos de personas. Su rigor metodológico es la cortesía mínima que les debemos a quienes invierten su tiempo en responderla."*

**Versión:** 1.0 — Abril 2026 | **Audiencia:** Equipo investigador | **Clasificación:** Público

---

## 1. FUNDAMENTOS TEÓRICOS

### 1.1. Enfoque GQM (Goal-Question-Metric)

La metodología **GQM (Goal-Question-Metric)** de Basili y Weiss garantiza que cada pregunta responde a un objetivo medible y cada métrica deriva de una necesidad de información específica.

**Objetivo principal:** Medir la madurez de las organizaciones españolas en ciberseguridad para IA, con desglose territorial por CCAA.

| ID Objetivo | Enunciado | Función FAICP | Secciones |
|-------------|-----------|--------------|-----------|
| G1 | Determinar nivel de gobernanza IA-ciberseguridad | GOBERNAR | Sección 1 |
| G2 | Evaluar capacidad de identificación activos y riesgos IA | IDENTIFICAR | Sección 2 |
| G3 | Medir implementación de controles de protección IA | PROTEGER | Sección 3 |
| G4 | Evaluar capacidades de detección de amenazas IA | DETECTAR | Sección 4 |
| G5 | Medir preparación para respuesta a incidentes IA | RESPONDER | Sección 5 |
| G6 | Evaluar planes de recuperación de sistemas IA | RECUPERAR | Sección 6 |
| G7 | Caracterizar exposición OT/ICS con componente IA | INDUSTRIAL | Sección 7 |
| G8 | Medir grado de cumplimiento normativo IA | CUMPLIMIENTO | Sección 8 |
| G9 | Establecer benchmarks por CCAA y sector | TERRITORIAL | Análisis cruzado |

### 1.2. Paradigma de Investigación

Diseño de **investigación mixta**:
- **Cuantitativa:** Escalas Likert 1-5, selección múltiple, índices compuestos (IGM-FAICP)
- **Cualitativa:** Preguntas abiertas, análisis temático, narrativas emergentes
- **Longitudinal:** Diseñada para reaplicación anual desde 2026

### 1.3. Modelos de Madurez de Referencia

| Nivel FAICP | CMM/CMMI | COBIT 2019 | ENS | Cisco CRI |
|-------------|----------|------------|-----|-----------|
| 1 · Inexistente | Initial (1) | Initial (1) | No aplica | Beginner |
| 2 · Inicial | Managed (2) | Managed (2) | Básico parcial | Formative |
| 3 · Definido | Defined (3) | Defined (3) | Básico completo | Progressive |
| 4 · Gestionado | Quant. Managed (4) | Established (4) | Medio | Mature |
| 5 · Optimizado | Optimizing (5) | Optimized (5) | Alto | Leader |

---

## 2. DISEÑO MUESTRAL

### 2.1. Población Objetivo

**Población diana:** Responsables de ciberseguridad, TI, riesgos o dirección en organizaciones españolas que operen o planifiquen sistemas de IA. Nivel mínimo del respondente: Director/a de Seguridad o equivalente.

### 2.2. Estratificación Muestral por CCAA

| CCAA | Cuota Mínima | Justificación |
|------|-------------|---------------|
| Madrid | 25% | ~40% del tejido empresarial TIC nacional |
| Cataluña | 20% | Segundo ecosistema tecnológico |
| País Vasco | 10% | Mayor densidad OT y referente industrial |
| C. Valenciana | 7% | Ecosistema emergente smart city + industria |
| Castilla y León | 5% | Sede INCIBE; hub formación ciber |
| Resto CCAA | 33% | Distribución proporcional a PIB regional |

### 2.3. Cuotas por Sector

| Sector | Cuota | Sector | Cuota |
|--------|-------|--------|-------|
| AAPP (todas) | 20% | Tecnología/TIC | 15% |
| Sanidad | 10% | Industria/Manufactura | 10% |
| Banca/Finanzas | 10% | Resto sectores | 27% |
| Energía/Utilities | 8% | | |

### 2.4. Tamaño Muestral

| Parámetro | Valor |
|-----------|-------|
| Margen de error | ±5% |
| Nivel de confianza | 95% |
| Proporción estimada | 50% (máxima varianza) |
| **n mínimo** | **384 respondentes válidos** |
| n objetivo (análisis CCAA) | 700–1.000 respondentes |

---

## 3. PROCESO DE APLICACIÓN

### 3.1. Fases del Proyecto

```
FASE 1 — Preparación (Semanas 1-4)
├── Revisión por panel de expertos (mínimo 5 CISOs + 1 experto EU AI Act + 1 académico)
├── Prueba piloto con 15-20 organizaciones
├── Ajuste lingüístico y técnico
└── Configuración de plataforma digital

FASE 2 — Reclutamiento (Semanas 5-8)
├── Distribución vía INCIBE, ISMS Forum, CCN-CERT, CIONET España
├── Difusión en asociaciones sectoriales (AEB, UNESA, SEOPAN...)
├── LinkedIn grupos CISO
└── Colaboración con CCAA vía CCN y organismos autonómicos

FASE 3 — Recolección (Semanas 9-16)
├── Período principal: 6 semanas
├── Recordatorios en semanas 3 y 5
├── Monitorización tasa de respuesta por CCAA y sector
└── Cierre con verificación de cuotas mínimas

FASE 4 — Análisis (Semanas 17-22)
├── Limpieza de datos (outliers, inconsistencias)
├── Cálculo IGM por organización, sector y CCAA
├── Análisis estadístico descriptivo e inferencial
├── Análisis cualitativo de preguntas abiertas
└── Benchmarking internacional

FASE 5 — Difusión (Semanas 23-26)
├── Informe ejecutivo nacional
├── Informes por CCAA (17 documentos personalizados)
├── Publicación académica peer-reviewed
└── Presentación en evento referencial (CYBERCAMP, RootedCON...)
```

### 3.2. Plataformas de Administración

| Plataforma | Ventajas | Inconvenientes | Recomendación |
|------------|----------|----------------|---------------|
| LimeSurvey (self-hosted) | Control total de datos, RGPD nativo | Requiere infraestructura | **Primera opción** |
| Google Forms | Sencillo, gratuito | Datos en servidores EE.UU. | Solo con consentimiento explícito |
| SurveyMonkey | Profesional, analytics integrado | Coste, servidores EE.UU. | Si presupuesto disponible |
| REDCap | Certificado para investigación | Requiere acceso institucional | Para versión académica |

---

## 4. CODIFICACIÓN Y ANÁLISIS

### 4.1. Cálculo del IGM-FAICP

**Fórmula:**

$$IGM = \sum_{f=1}^{6} w_f \cdot \bar{M}_f$$

Donde $w_f$ es el peso de la función $f$ y $\bar{M}_f$ la media de las puntuaciones de madurez de esa función.

**Pesos por función:**

| Función | Peso (w) | Justificación |
|---------|----------|---------------|
| Gobernar (GV) | 0.20 | Habilitadora de todas las demás |
| Identificar (ID) | 0.20 | Prerequisito para toda protección |
| Proteger (PR) | 0.25 | Mayor número de controles operativos |
| Detectar (DE) | 0.15 | Crítica pero parcialmente automatizable |
| Responder (RS) | 0.10 | Alta dependencia de GV, ID y PR |
| Recuperar (RC) | 0.10 | Complementaria a Responder |

**Interpretación del IGM:**

| Rango IGM | Nivel | Recomendación |
|-----------|-------|---------------|
| 1.0 – 1.5 | **Crítico** | Intervención urgente |
| 1.5 – 2.5 | **Emergente** | Plan de mejora prioritario |
| 2.5 – 3.5 | **Desarrollado** | Consolidación y extensión |
| 3.5 – 4.5 | **Avanzado** | Optimización y automatización |
| 4.5 – 5.0 | **Líder** | Compartir prácticas |

### 4.2. Análisis Estadístico

**Descriptivo:** Media, mediana, desviación típica, IC95%, distribución de frecuencias, tablas de contingencia.

**Inferencial:**
- ANOVA de un factor: comparar IGM entre sectores y CCAA
- Test de Mann-Whitney: comparaciones binarias (grande vs. pequeña empresa)
- Análisis de clústeres (K-means): perfiles de madurez organizativa
- Correlación de Spearman: IGM total vs. sub-índices por función

**Multivariante:**
- Regresión lineal múltiple: predictores del IGM (sector, tamaño, CCAA, presupuesto)
- Análisis factorial exploratorio: validar estructura interna de la escala

---

## 5. VALIDEZ Y FIABILIDAD

### 5.1. Validez de Contenido

**Panel de expertos:** Mínimo 3 CISOs con >10 años de experiencia + 1 experto EU AI Act + 1 académico.

**Criterios:**
- Coeficiente de Validez de Contenido (CVC) de Hernández-Nieto: umbral ≥ 0.80
- Índice de Adecuación de Ítems (IAI): umbral ≥ 0.85

### 5.2. Fiabilidad

**Alpha de Cronbach por sección:**
- Mínimo aceptable: α ≥ 0.70
- Recomendado: α ≥ 0.80

**Test-retest:**
- Submuestra: 30 organizaciones, intervalo 4 semanas
- Coeficiente de correlación intraclase (ICC) ≥ 0.75

### 5.3. Criterios del Piloto

| Criterio | Umbral | Acción |
|----------|--------|--------|
| Tiempo total > 75 min | Cualquier respondente | Reducir preguntas de selección |
| Tasa abandono sección > 10% | Acumulado | Revisar complejidad |
| "No lo sé" > 20% en ítem | Cualquier pregunta | Reformular o eliminar |
| Varianza ítem < 0.5 | Estadístico | Evaluar eliminación |
| Alpha Cronbach sección < 0.65 | Por sección | Revisar coherencia de ítems |

---

## 6. ÉTICA Y PROTECCIÓN DE DATOS

- **Base jurídica:** Interés legítimo (investigación de interés público) + consentimiento explícito
- **Anonimización:** Datos organizacionales anonimizados antes del análisis
- **Datos mínimos:** Solo CCAA, sector y tamaño (sin nombre ni CIF)
- **Conservación:** Datos crudos máximo 5 años; datos anonimizados indefinidamente
- **Derechos RGPD:** Acceso, rectificación, supresión, portabilidad, oposición

---

## 7. PRODUCTOS Y DIFUSIÓN

| Producto | Audiencia | Canal | Plazo |
|----------|-----------|-------|-------|
| Informe ejecutivo nacional | CISOs, directivos | Web FAICP + INCIBE | 3 meses |
| Informes por CCAA (17) | Gobiernos autonómicos | Envío directo + web | 4 meses |
| Artículo académico peer-reviewed | Investigadores | Computers & Security, IEEE TII | 9-12 meses |
| Dataset anonimizado | Investigadores | Zenodo / DIGITAL.CSIC | 12 meses |
| Dashboard interactivo | Público general | Web FAICP observatory | 5 meses |

---

*Kit FAICP 2025–2026 · Documento (b) · Versión 1.0 · Abril 2026*
*Metodología basada en: GQM (Basili & Weiss), CMM/CMMI, COBIT 2019, ISO/IEC 42001, NIST AI RMF*
