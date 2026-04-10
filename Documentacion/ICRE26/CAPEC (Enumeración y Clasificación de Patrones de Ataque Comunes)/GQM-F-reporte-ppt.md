# 📊 PLANTILLA REPORTE EJECUTIVO — POWERPOINT
## Especificación Completa Slide por Slide para Presentación al Consejo
### Kit GQM+PRAGMATIC CAPEC-ESP · Documento F · Versión 1.0 · Abril 2026

---

> *«La diferencia entre un informe de ciberseguridad que el Consejo lee y uno que archiva sin abrir suele residir en los primeros 90 segundos de la presentación. Aquí están esos 90 segundos —y los 25 minutos siguientes.»*

---

## DISEÑO GENERAL

### Paleta de colores
| Nombre | Código HEX | Uso principal |
|---|---|---|
| Azul Profundo | #0A2342 | Fondo portada; encabezados principales |
| Azul Medio | #1B4F8A | Fondos de sección; elementos de marca |
| Verde Seguro | #1A7A4A | Indicadores positivos; zona verde |
| Ámbar Alerta | #E07B00 | Indicadores de advertencia; zona media |
| Rojo Crítico | #C0392B | Indicadores negativos; alertas críticas |
| Gris Neutro | #4A4A4A | Texto principal en fondos claros |
| Blanco | #FFFFFF | Texto en fondos oscuros; espacio negativo |
| Gris Claro | #F5F5F5 | Fondos de tablas; fondos de slides de datos |

### Tipografía
- **Títulos:** Calibri Bold — 28-36 pt
- **Subtítulos:** Calibri Regular — 20-24 pt
- **Cuerpo:** Calibri Regular — 14-16 pt
- **Notas:** Calibri Light — 11 pt
- **Código/métricas:** Consolas Regular — 12 pt

### Dimensiones
- Formato: 16:9 (33,87 × 19,05 cm)
- Márgenes: 1,5 cm todos los lados
- Área de contenido: 30,87 × 16,05 cm

---

## ESTRUCTURA DE LA PRESENTACIÓN

| # | Slide | Tipo | Duración | Audiencia |
|---|---|---|---|---|
| 1 | Portada | Diseño | — | Todas |
| 2 | Agenda y contexto | Orientación | 1 min | Todas |
| 3 | Resumen ejecutivo (3 mensajes clave) | KPI | 2 min | Consejo |
| 4 | IGM-CAPEC Global — Gauge | KPI | 2 min | Consejo |
| 5 | Radar por dominio | Datos | 3 min | Consejo + Técnico |
| 6 | Top 3 fortalezas | Análisis | 2 min | Consejo |
| 7 | Top 3 brechas críticas | Análisis | 3 min | Consejo |
| 8 | Evolución temporal del IGM-CAPEC | Tendencia | 2 min | Consejo |
| 9 | Benchmarking sectorial | Contexto | 2 min | Consejo |
| 10 | ROSI — Retorno de la inversión en seguridad | Financiero | 3 min | Consejo + CFO |
| 11 | Mapeo normativo NIS2/ENS/DORA | Cumplimiento | 2 min | Regulador + Legal |
| 12 | Hoja de ruta de mejora (próximos 18 meses) | Planificación | 3 min | Consejo |
| 13 | Recursos requeridos y presupuesto | Financiero | 2 min | CFO + Consejo |
| 14 | Indicadores de seguimiento (próxima revisión) | Gobernanza | 1 min | Consejo |
| 15 | Apéndice A: Detalle por dominio | Detalle | Backup | Técnico |
| 16 | Apéndice B: Metodología GQM+PRAGMATIC | Metodología | Backup | Técnico |
| 17 | Apéndice C: Marco CAPEC — referencia | Referencia | Backup | Técnico |
| 18 | Contacto y próximos pasos | Cierre | 1 min | Todas |

**Tiempo total presentación principal (slides 1-14):** ~28 minutos
**Tiempo con Q&A:** ~45 minutos
**Backup disponible:** Slides 15-18 (bajo demanda)

---

## ESPECIFICACIÓN DETALLADA SLIDE A SLIDE

---

### SLIDE 1 — PORTADA

**Fondo:** Color sólido Azul Profundo (#0A2342)

**Contenido:**
```
[Logo organización — superior izquierda, 4×2 cm]

[Línea decorativa horizontal — color Verde Seguro, 2px]

POSTURA DE CIBERSEGURIDAD
[Título principal — Calibri Bold 36pt — BLANCO]

Marco CAPEC · Indicadores GQM+PRAGMATIC
[Subtítulo — Calibri Regular 22pt — Azul Medio claro]

[Espacio]

[Nombre Organización]  |  [Sector NIS2]
[Período de evaluación: Q1 2026]
[Nombre del Responsable del Informe]
[Calibri Regular 14pt — Gris Claro]

[Pie de slide: CONFIDENCIAL — Solo para miembros del Consejo de Administración]
[Calibri Light 10pt — Ámbar Alerta]
```

**Notas para ponente:**
> "Buenos días. En los próximos 30 minutos les presento el estado de la postura de ciberseguridad de [organización] medida con el marco CAPEC, el estándar de patrones de ataque del MITRE. A diferencia de los informes de cumplimiento habituales, lo que van a ver hoy son métricas que los atacantes también comprenden —y que, por tanto, nos dicen si somos un objetivo fácil o uno que requiere demasiado esfuerzo para el retorno que ofrece."

---

### SLIDE 2 — AGENDA Y CONTEXTO

**Fondo:** Gris Claro (#F5F5F5)

**Estructura de dos columnas:**

**Columna izquierda (60%):**
```
AGENDA DE HOY
[H2 — Azul Profundo]

1. Resumen ejecutivo (3 mensajes)       2 min
2. Índice de Madurez CAPEC global       2 min
3. Fortalezas y brechas críticas        5 min
4. Tendencia y benchmark sectorial      4 min
5. Retorno de la inversión (ROSI)       3 min
6. Hoja de ruta 18 meses               3 min
7. Recursos y próximos pasos            3 min
────────────────────────────────────────────
                              TOTAL    22 min + Q&A
```

**Columna derecha (40%):**
```
¿POR QUÉ CAPEC?
[H3 — Azul Medio]

CAPEC es el catálogo de referencia del MITRE
que clasifica los 559 patrones de ataque 
más documentados en el mundo.

Usar CAPEC como base de medición significa
que nuestras métricas están alineadas con
cómo piensan los adversarios —no con cómo
nos gustaría que pensaran.

[Icono: mapa/escudo]
```

---

### SLIDE 3 — RESUMEN EJECUTIVO (3 MENSAJES CLAVE)

**Fondo:** Blanco con franja izquierda Azul Profundo (3 cm)

**Diseño: Tres bloques horizontales de igual altura**

**BLOQUE 1 (Verde Seguro):**
```
[Icono trofeo]
FORTALEZA PRINCIPAL
──────────────────
[Dominio más alto: ej. "Ingeniería Social"]
IGD: [valor]/5  ●●●●○

"Nuestros empleados han reducido la tasa
de respuesta a phishing al [X]% —por debajo
del benchmark sectorial del [Y]%."
```

**BLOQUE 2 (Ámbar Alerta):**
```
[Icono objetivo]
BRECHA PRIORITARIA
──────────────────
[Dominio más bajo: ej. "Supply Chain"]
IGD: [valor]/5  ●●○○○

"El [X]% de nuestros componentes de software
de terceros carecen de SBOM verificado, lo que
representa un riesgo de tipo XZ Utils activo."
```

**BLOQUE 3 (Azul Medio):**
```
[Icono flecha tendencia]
TENDENCIA GLOBAL
──────────────────
IGM-CAPEC: [valor]/5  [▲/▼ X,X vs. Q anterior]

"En los últimos 12 meses el índice ha mejorado
[X] puntos. Al ritmo actual, alcanzaremos el
nivel 'Establecido' (3,0) en [fecha estimada]."
```

**Notas para ponente:**
> "Tres noticias en un slide. Empezamos por la buena porque sí, hay buenas noticias. Seguimos con la que más atención requiere —y esta sí que conviene que quede grabada. Y terminamos con la foto del progreso, porque un número sin tendencia no informa; solo asusta."

---

### SLIDE 4 — IGM-CAPEC GLOBAL — GAUGE

**Fondo:** Blanco

**Diseño central: Medidor semicircular grande (70% del ancho del slide)**

```
                    IGM-CAPEC GLOBAL
                    ─────────────────

        INICIAL    EN DESARROLLO    ESTABLECIDO    AVANZADO
        (0-2)         (2-3)           (3-4)          (4-5)
         🔴            🟠              🟡             🟢

                         ▲
                    [VALOR ACTUAL]
                      [X,X / 5,0]

              Nivel: [ETIQUETA DEL NIVEL]
```

**Panel lateral derecho (30%):**
```
DIMENSIONES CLAVE

Más alto:
[Dominio] ████████░░ [X,X]

Promedio sector:
[Sector] ██████░░░░ [X,X]

Objetivo año:
Meta 2026  ████████░░ 3,5

Evolución:
Q4 2025 → Q1 2026: [▲/▼ X,X]
```

**Notas para ponente:**
> "Este número resume los 50 indicadores de la encuesta en una escala del 0 al 5. El umbral de 3,0 es el nivel 'Establecido' según el benchmarking sectorial europeo de ENISA. Estamos en [valor]. Si estamos por encima, bien. Si estamos por debajo, el slide siguiente les explica exactamente por qué y qué hacemos al respecto."

---

### SLIDE 5 — RADAR POR DOMINIO

**Fondo:** Blanco

**Diseño: Gráfico de radar central (65% del slide)**

```
Gráfico de araña con 9 ejes:
- Gobernanza
- Software  
- Ingeniería Social
- Supply Chain
- Comunicaciones
- Hardware
- OT/ICS
- IA Adversarial
- Resiliencia

Serie 1 (Azul): Puntuación actual (0-5)
Serie 2 (Verde punteado): Referencia sectorial
Serie 3 (Rojo punteado): Umbral mínimo aceptable (2,0)
```

**Tabla derecha (35%):**
```
DOMINIO          ACTUAL  SECTOR  ESTADO
─────────────────────────────────────
Gobernanza       [X,X]   [X,X]   [🟢/🟡/🔴]
Software         [X,X]   [X,X]   [🟢/🟡/🔴]
Ing. Social      [X,X]   [X,X]   [🟢/🟡/🔴]
Supply Chain     [X,X]   [X,X]   [🟢/🟡/🔴]
Comunicaciones   [X,X]   [X,X]   [🟢/🟡/🔴]
Hardware         [X,X]   [X,X]   [🟢/🟡/🔴]
OT/ICS           [X,X]   [X,X]   [🟢/🟡/🔴]
IA Adversarial   [X,X]   [X,X]   [🟢/🟡/🔴]
Resiliencia      [X,X]   [X,X]   [🟢/🟡/🔴]
─────────────────────────────────────
IGM-CAPEC        [X,X]   [X,X]   [🟢/🟡/🔴]
```

---

### SLIDE 6 — TOP 3 FORTALEZAS

**Fondo:** Blanco con franja superior Verde Seguro

**Título:** "Dónde somos más difíciles de atacar" [Calibri Bold 26pt]

**3 tarjetas horizontales:**

```
TARJETA 1:                    TARJETA 2:                    TARJETA 3:
[Icono dominio 1]              [Icono dominio 2]              [Icono dominio 3]
[Nombre dominio]               [Nombre dominio]               [Nombre dominio]
Puntuación: [X,X]/5            Puntuación: [X,X]/5            Puntuación: [X,X]/5

Métrica destacada:             Métrica destacada:             Métrica destacada:
[M-XX-X.X]                     [M-XX-X.X]                     [M-XX-X.X]
Valor: [dato real]             Valor: [dato real]             Valor: [dato real]

"Lo que esto significa         "Lo que esto significa         "Lo que esto significa
 para un atacante:"             para un atacante:"             para un atacante:"
[Implicación táctica]          [Implicación táctica]          [Implicación táctica]
```

---

### SLIDE 7 — TOP 3 BRECHAS CRÍTICAS

**Fondo:** Blanco con franja superior Rojo Crítico

**Título:** "Dónde debemos actuar con urgencia" [Calibri Bold 26pt]

**Subtítulo:** "Clasificadas por impacto potencial × facilidad de explotación" [Calibri 16pt]

**3 tarjetas con diseño de alerta:**

```
BRECHA 1 [CRÍTICA 🔴]          BRECHA 2 [ALTA 🟠]             BRECHA 3 [MEDIA 🟡]
───────────────────────────────────────────────────────────────────────────────
Dominio: [nombre]               Dominio: [nombre]               Dominio: [nombre]
Puntuación actual: [X,X]/5     Puntuación actual: [X,X]/5     Puntuación actual: [X,X]/5

Métrica crítica:               Métrica crítica:               Métrica crítica:
[M-XX-X.X] = [valor]          [M-XX-X.X] = [valor]          [M-XX-X.X] = [valor]

Patrón CAPEC expuesto:         Patrón CAPEC expuesto:         Patrón CAPEC expuesto:
[CAPEC-XXX: nombre]            [CAPEC-XXX: nombre]            [CAPEC-XXX: nombre]

Acción prioritaria:            Acción prioritaria:            Acción prioritaria:
[Acción concreta 1]            [Acción concreta 2]            [Acción concreta 3]

Plazo: [X meses]               Plazo: [X meses]               Plazo: [X meses]
Coste estimado: [€]            Coste estimado: [€]            Coste estimado: [€]
```

**Notas para ponente:**
> "Estas tres brechas son las que, si yo fuera un adversario y tuviera este informe, atacaría mañana. No es retórica: es el resultado directo de aplicar los indicadores de probabilidad y severidad del catálogo CAPEC a nuestro entorno específico."

---

### SLIDE 8 — EVOLUCIÓN TEMPORAL

**Fondo:** Gris Claro (#F5F5F5)

**Gráfico de línea principal (70% del slide):**
```
IGM-CAPEC — EVOLUCIÓN ÚLTIMOS 5 TRIMESTRES
──────────────────────────────────────────
5,0 ┤
4,5 ┤                                    ○ Objetivo 2027
4,0 ┤                                  ╱
3,5 ┤                         ○ Meta 2026
3,0 ┤ ·····················  [LÍNEA UMBRAL ESTABLECIDO]
2,5 ┤       ●     ●     ●──●──●  [LÍNEA ACTUAL]
2,0 ┤
    └──────────────────────────────────────────────────
     Q1-25  Q2-25  Q3-25  Q4-25  Q1-26  Q2-26  Q3-26
                                  ▲ HOY
```

**Panel estadístico derecho (30%):**
```
ESTADÍSTICAS DE PROGRESO
────────────────────────
Variación anual:
[▲/▼ X,X puntos] ([X,X%])

Velocidad de mejora:
[X,X puntos/trimestre]

Al ritmo actual, nivel 3,0:
[Fecha proyectada]

Hitos alcanzados:
[Lista 2-3 logros cuantificados]
```

---

### SLIDE 9 — BENCHMARKING SECTORIAL

**Fondo:** Blanco

**Gráfico de barras horizontales agrupadas:**

```
POSICIONAMIENTO EN EL SECTOR [NOMBRE SECTOR]
───────────────────────────────────────────────

[Organización]  ████████████░░░  [X,X]  ← TÚ ESTÁS AQUÍ
P90 sector      ████████████████  [X,X]
Mediana (P50)   ██████████░░░░░░  [X,X]
P25 sector      ██████░░░░░░░░░░  [X,X]
                0    1    2    3    4    5
```

**Tabla complementaria:**
```
COMPARATIVA DIMENSIONAL VS. MEDIANA SECTORIAL

Dominio         Nosotros  Sector  Δ
────────────────────────────────────
Gobernanza      [X,X]     [X,X]   [▲▼X,X]
Software        [X,X]     [X,X]   [▲▼X,X]
...
────────────────────────────────────
IGM-CAPEC       [X,X]     [X,X]   [▲▼X,X]
```

---

### SLIDE 10 — ROSI (RETORNO DE LA INVERSIÓN EN SEGURIDAD)

**Fondo:** Blanco con acento financiero

**Estructura de tres paneles:**

```
PANEL 1: EXPOSICIÓN ACTUAL
─────────────────────────
Pérdida Esperada Anual (ALE)
SIN controles: €[X.XXX.XXX]

• Software:     €[XXX.XXX]
• IS/Phishing:  €[XXX.XXX]
• Supply Chain: €[XXX.XXX]
• OT/Ransomware:€[X.XXX.XXX]


PANEL 2: IMPACTO DE LOS CONTROLES
───────────────────────────────────
Pérdida Esperada Anual (ALE)
CON controles actuales: €[X.XXX.XXX]

Reducción lograda:
€[XXX.XXX] / año

Coste del programa de controles:
€[XXX.XXX] / año


PANEL 3: RETORNO DE LA INVERSIÓN
──────────────────────────────────
ROSI: [XXX]%

Por cada €1 invertido en seguridad:
€[X,XX] de pérdida evitada

Período de recuperación:
[X,X] meses

VAN 3 años (8% descuento):
€[X.XXX.XXX]
```

**Nota al pie:** "Cálculo basado en metodología FAIR (Factor Analysis of Information Risk). Valores de referencia: IBM Cost of Data Breach 2024, ENISA ETL 2025."

---

### SLIDE 11 — CUMPLIMIENTO NORMATIVO

**Fondo:** Gris Claro

**Matriz de cobertura:**

```
COBERTURA DE INDICADORES CAPEC vs. MARCOS NORMATIVOS

                     NIS2   ENS   DORA   ISO27001   NIST CSF
                     ────   ───   ────   ────────   ────────
Gobernanza           ✅     ✅    ✅        ✅          ✅
Software             ✅     ✅    —         ✅          ✅
Ingeniería Social    ✅     ✅    ✅        ✅          ✅
Supply Chain         ✅     ✅    ✅        ✅          ✅
Comunicaciones       ✅     ✅    ✅        ✅          —
Hardware             ✅     ✅    —         ✅          —
OT/ICS               ✅     ✅    ✅        —           ✅
IA Adversarial       ✅     —     —         ✅          —
Post-Quantum         ✅     ✅    ✅        —           —
Resiliencia          ✅     ✅    ✅        ✅          ✅
────────────────────────────────────────────────────────
COBERTURA           10/10  9/10  8/10     8/10        7/10
```

**Mensaje clave:** "Cada indicador que medimos está anclado a al menos un requisito normativo. Esto no es security theater: es evidencia directa de cumplimiento."

---

### SLIDE 12 — HOJA DE RUTA 18 MESES

**Fondo:** Blanco

**Diagrama de Gantt simplificado:**

```
HOJA DE RUTA DE MEJORA CAPEC — 2026–2027
──────────────────────────────────────────────────────────

                 Q1 26  Q2 26  Q3 26  Q4 26  Q1 27  Q2 27
                 ─────  ─────  ─────  ─────  ─────  ─────
[Brecha 1]       ████████████
  Acción 1.1     ████
  Acción 1.2            ████████
  Acción 1.3                   ████████

[Brecha 2]              ████████████████
  Acción 2.1            ████████
  Acción 2.2                   ████████████

[Brecha 3]                     ████████████████████████
  Acción 3.1                   ████████████
  Acción 3.2                               ████████████

Hito 1: IGM ≥ 2,5          ⬥
Hito 2: IGM ≥ 3,0                    ⬥
Meta 2027: IGM ≥ 3,5                              ⬥
──────────────────────────────────────────────────────────
```

---

### SLIDE 13 — RECURSOS Y PRESUPUESTO

**Fondo:** Blanco

**Dos tablas:**

**TABLA 1: Recursos humanos requeridos**
```
Rol                          Dedicación  Estado      Coste anual
──────────────────────────────────────────────────────────────
CISO / Líder del programa    20%         Existente   (asignación)
Analista GRC (métricas CAPEC) 50%        ¿Contratar? €45.000
Ingeniero DevSecOps          30%         Existente   (asignación)
Especialista Supply Chain    25%         ¿Contratar? €22.500
Soporte externo / consultoría Variable   Presupuestar €30.000/año
```

**TABLA 2: Inversión en herramientas**
```
Herramienta / Control          Dominio      Coste/año  Prioridad
──────────────────────────────────────────────────────────────
SAST/DAST con mapeo CAPEC      Software     €18.000    🔴 Inmediata
Plataforma simulación phishing Ing. Social  €12.000    🔴 Inmediata
SCA para SBOM                  Supply Chain €15.000    🔴 Inmediata
Escáner TLS/criptográfico      Comunicac.   €2.000     🔴 Inmediata
Herramienta crypto-discovery   PQC          €8.000     🟡 Q2 2026
Red teaming IA (externo)       IA Advers.   €25.000    🟡 Q3 2026
──────────────────────────────────────────────────────────────
TOTAL INVERSIÓN ADICIONAL                   €80.000/año
```

---

### SLIDE 14 — SEGUIMIENTO Y PRÓXIMA REVISIÓN

**Fondo:** Azul Profundo (#0A2342)

**Contenido en blanco:**

```
COMPROMISOS PARA LA PRÓXIMA REVISIÓN
[Q2 2026 — Fecha estimada: [fecha]]

ACCIÓN 1: [nombre]
Responsable: [nombre/cargo]    Fecha: [fecha]    KPI: [métrica]

ACCIÓN 2: [nombre]
Responsable: [nombre/cargo]    Fecha: [fecha]    KPI: [métrica]

ACCIÓN 3: [nombre]
Responsable: [nombre/cargo]    Fecha: [fecha]    KPI: [métrica]

────────────────────────────────────────────────────────
INDICADORES A REVISAR EN PRÓXIMA SESIÓN:
☐ IGM-CAPEC ≥ [objetivo Q2]
☐ M-SC-1.1 (SBOM) ≥ [porcentaje objetivo]
☐ M-IS-1.1 (phishing) ≤ [tasa objetivo]
────────────────────────────────────────────────────────

"No medimos para reportar. Medimos para mejorar.
 Y mejoramos para que atacarnos no valga la pena."
```

---

## APÉNDICES (SLIDES 15-18)

### SLIDE 15 — Apéndice A: Detalle por Dominio
**Contenido:** Tabla completa con los 24 indicadores, valores actuales, umbrales y tendencia. Una tabla por dominio o tabla consolidada según tiempo disponible.

### SLIDE 16 — Apéndice B: Metodología GQM+PRAGMATIC
**Contenido:** Diagrama del árbol GQM (Goal → Question → Metric). Tabla de criterios PRAGMATIC con puntuaciones Top 5 métricas. Referencia a los Documentos A y B del kit.

### SLIDE 17 — Apéndice C: Marco CAPEC
**Contenido:** Descripción de CAPEC v3.9 (559 patrones, 9 mecanismos, 6 dominios). Mapa de calor de patrones por severidad × probabilidad. URL oficial: https://capec.mitre.org

### SLIDE 18 — Contacto y Próximos Pasos
**Contenido:**
```
[Nombre CISO]
[Email]  |  [Teléfono]

Próximos pasos acordados:
1. [Acción]  —  [Responsable]  —  [Fecha]
2. [Acción]  —  [Responsable]  —  [Fecha]
3. [Acción]  —  [Responsable]  —  [Fecha]

Próxima revisión del IGM-CAPEC:
[Fecha]  |  [Hora]  |  [Sala/Plataforma]
```

---

## ADAPTACIONES POR AUDIENCIA

### Para Consejo de Administración (slides 1-14, 28 min)
- Énfasis en slides 3, 10 y 12 (resumen ejecutivo, ROSI, hoja de ruta)
- Simplificar slides técnicos (5, 9, 11) con lenguaje de negocio
- Tiempo para Q&A: 15-20 minutos

### Para Comité de Auditoría / Regulador (slides 1-11, añadir 15-16)
- Énfasis en slides 11 (cumplimiento normativo) y mapeo NIS2/ENS/DORA
- Añadir Apéndice B (metodología) para credibilidad técnica
- Tiempo para Q&A: 20-25 minutos

### Para Equipo Técnico (slides 4-9, 14-18)
- Énfasis en slides 5 (radar dominio), 15 (detalle indicadores) y 16 (metodología)
- Presentar datos brutos; no simplificar
- Sesión de trabajo, no presentación; 45-60 minutos con tabla redonda

---

*Kit GQM+PRAGMATIC CAPEC-ESP · Documento F: Plantilla PowerPoint · Versión 1.0 · Abril 2026*
