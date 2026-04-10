# Plantilla de Excel: Cálculo IGM-FAICP y ROI de Ciberseguridad IA
## Especificación técnica completa lista para implementar en Microsoft Excel o Google Sheets

> **Versión:** 1.0 — Abril 2026  
> **Descripción:** Esta plantilla implementa el cálculo del Índice de Gobernanza y Madurez FAICP (IGM-FAICP) y el modelo de ROI de Ciberseguridad IA, con todas las fórmulas, validaciones de datos y formateo condicional especificados para implementación directa.

---

## HOJA 1: "INSTRUCCIONES"

### Estructura de la Hoja

**Celda A1:** Título: `KIT IGM-FAICP 2025-2026 — Calculadora de Índice de Madurez y ROI`  
**Celda A2:** Versión: `v1.0 — Abril 2026 | NIST IR 8596 · EU AI Act · GQM + PRAGMATIC`

### Contenido de las instrucciones

| Sección | Contenido |
|---------|-----------|
| **Cómo usar** | 1. Completar HOJA 2 (Datos de la Organización), 2. Puntuar todos los indicadores en HOJA 3 (Autoevaluación), 3. Ver resultados automáticos en HOJA 4 (IGM-FAICP), 4. Completar datos de costes en HOJA 5 (ROI) |
| **Escala de puntuación** | 1 = Inexistente / 2 = Inicial / 3 = Definido / 4 = Gestionado / 5 = Optimizado |
| **Frecuencia recomendada** | Evaluación inicial + revisión semestral de indicadores Tier 1 + revisión anual completa |
| **Contacto técnico** | INCIBE (017) · AESIA (supervisión EU AI Act) · CCN-CERT (sectores AAPP y defensa) |

---

## HOJA 2: "DATOS ORGANIZACIÓN"

### Estructura de Campos

| Celda | Campo | Tipo | Ejemplo |
|-------|-------|------|---------|
| B3 | Nombre de la organización | Texto libre | `Empresa Ejemplo S.A.` |
| B4 | CIF / NIF | Texto | `B12345678` |
| B5 | CCAA | Lista desplegable | *(ver lista validación abajo)* |
| B6 | Sector | Lista desplegable | *(ver lista validación abajo)* |
| B7 | Tamaño | Lista desplegable | `Microempresa / PYME / Grande / AAPP` |
| B8 | Perfil regulatorio | Casillas de verificación | `OE_NIS2 / OI_NIS2 / AAPP_ENS / ProvIA_AIA / DesplIA_AIA / EntFin_DORA` |
| B9 | Fecha de evaluación | Fecha | `=HOY()` |
| B10 | Evaluador responsable | Texto libre | `Nombre Apellidos — Rol` |
| B11 | Próxima revisión | Fórmula | `=B9+180` (6 meses) |

### Listas de Validación de Datos

**CCAA (lista desplegable en B5):**
```
Andalucía, Aragón, Asturias, Baleares, Canarias, Cantabria, Castilla-La Mancha, 
Castilla y León, Cataluña, Comunitat Valenciana, Extremadura, Galicia, 
La Rioja, Madrid, Murcia, Navarra, País Vasco, Ceuta, Melilla
```

**Sectores (lista desplegable en B6 — basado en Anexo I y II NIS2):**
```
Energía, Transporte, Banca y Finanzas, Infraestructura de mercados financieros,
Sanidad, Agua potable, Aguas residuales, Infraestructura digital,
Gestión de servicios TIC, Administración pública, Espacio,
Servicios postales, Gestión de residuos, Fabricación, Alimentación,
Investigación, Otros servicios digitales, Otros
```

---

## HOJA 3: "AUTOEVALUACIÓN"

### Estructura Completa de Columnas

| Col | Contenido |
|-----|-----------|
| A | Código indicador (IGM-GV-01, etc.) — protegido, solo lectura |
| B | Nombre del indicador — protegido, solo lectura |
| C | Función CSF 2.0 — protegido, solo lectura |
| D | Marco fuente — protegido, solo lectura |
| E | Tier (1 = Crítico / 2 = Importante / 3 = Avanzado) — protegido |
| F | **Puntuación actual (1-5)** — campo de entrada con validación |
| G | **Evidencia / notas** — texto libre |
| H | **Fecha de última verificación** — campo fecha |
| I | **Plan de acción (si puntuación ≤ 3)** — texto libre |
| J | **Responsable del plan** — texto libre |
| K | **Fecha objetivo mejora** — campo fecha |
| L | Puntuación PRAGMATIC total — protegido, solo lectura (precargado) |
| M | Calificación PRAGMATIC — protegido, solo lectura (IF anidado) |

### Datos Pre-cargados (Filas 4-32)

```
Fila 4:  IGM-GV-01 | Política formal de ciberseguridad para IA           | GOBERNAR  | NIST IR 8596 GV.OC-04  | Tier 1 | [entrada] | ... | 23 | Recomendada
Fila 5:  IGM-GV-02 | Mapa de dependencias de infraestructura IA           | GOBERNAR  | NIST IR 8596 GV.OC-05  | Tier 1 | [entrada] | ... | 21 | Recomendada
Fila 6:  IGM-GV-03 | Riesgos IA adversarial en formación RRHH             | GOBERNAR  | NIST IR 8596 GV.RR-04  | Tier 1 | [entrada] | ... | 23 | Recomendada
Fila 7:  IGM-GV-04 | Evaluación sistemática de proveedores IA             | GOBERNAR  | NIST IR 8596 GV.SC-07  | Tier 1 | [entrada] | ... | 21 | Recomendada
Fila 8:  IGM-GV-05 | Función de gobernanza de IA (comité/rol)             | GOBERNAR  | AI RMF GOVERN 1.1      | Tier 1 | [entrada] | ... | 25 | Recomendada
Fila 9:  IGM-GV-06 | Registro y clasificación EU AI Act                   | GOBERNAR  | EU AI Act Art. 49      | Tier 2 | [entrada] | ... | 22 | Recomendada
Fila 10: IGM-ID-01 | AI-BOM: Inventario completo de sistemas de IA       | IDENTIFICAR| NIST IR 8596 ID.AM-07  | Tier 1 | [entrada] | ... | 22 | Recomendada
Fila 11: IGM-ID-02 | Evaluación vulnerabilidades específicas IA           | IDENTIFICAR| OWASP LLM Top 10       | Tier 1 | [entrada] | ... | 22 | Recomendada
Fila 12: IGM-ID-03 | Consumo CTI IA adversarial                           | IDENTIFICAR| MITRE ATLAS v5.5       | Tier 2 | [entrada] | ... | 20 | Condicional
Fila 13: IGM-ID-04 | Modelado velocidad ataques IA en gestión riesgos    | IDENTIFICAR| NIST IR 8596 ID.RA-04  | Tier 2 | [entrada] | ... | 21 | Recomendada
Fila 14: IGM-ID-05 | Análisis riesgos cadena suministro IA               | IDENTIFICAR| NIST IR 8596 ID.SC-02  | Tier 1 | [entrada] | ... | 21 | Recomendada
Fila 15: IGM-PR-01 | IAM específico para sistemas y agentes de IA        | PROTEGER  | NIST IR 8596 PR.AA-01  | Tier 1 | [entrada] | ... | 22 | Recomendada
Fila 16: IGM-PR-02 | Menor privilegio en agentes IA autónomos            | PROTEGER  | NIST IR 8596 PR.AA-05  | Tier 1 | [entrada] | ... | 22 | Recomendada
Fila 17: IGM-PR-03 | Cobertura y frecuencia formación amenazas IA        | PROTEGER  | EU AI Act Art. 4       | Tier 1 | [entrada] | ... | 23 | Recomendada
Fila 18: IGM-PR-04 | Protección datos de entrenamiento e inferencia       | PROTEGER  | EU AI Act Art. 10      | Tier 1 | [entrada] | ... | 21 | Recomendada
Fila 19: IGM-PR-05 | Control versiones y MLOps seguros                   | PROTEGER  | NIST IR 8596 PR.PS-01  | Tier 2 | [entrada] | ... | 22 | Recomendada
Fila 20: IGM-PR-06 | Evaluación y control agencia excesiva (LLM06)       | PROTEGER  | OWASP LLM06; EU AI Act | Tier 2 | [entrada] | ... | 21 | Recomendada
Fila 21: IGM-DE-01 | Monitorización de APIs de IA externas               | DETECTAR  | NIST IR 8596 DE.CM-06  | Tier 1 | [entrada] | ... | 23 | Recomendada
Fila 22: IGM-DE-02 | Monitorización en tiempo de ejecución de IA         | DETECTAR  | NIST IR 8596 DE.CM-09  | Tier 1 | [entrada] | ... | 23 | Recomendada
Fila 23: IGM-DE-03 | Frecuencia y método evaluación model drift          | DETECTAR  | EU AI Act Art. 72.1    | Tier 2 | [entrada] | ... | 23 | Recomendada
Fila 24: IGM-DE-04 | Capacidades SOC para amenazas IA adversariales      | DETECTAR  | MITRE ATLAS v5.5       | Tier 2 | [entrada] | ... | 20 | Condicional
Fila 25: IGM-DE-05 | Controles detección prompt injection               | DETECTAR  | OWASP LLM01            | Tier 1 | [entrada] | ... | 22 | Recomendada
Fila 26: IGM-RS-01 | Playbooks respuesta específicos para IA             | RESPONDER | NIST IR 8596 RS.MA-01  | Tier 1 | [entrada] | ... | 25 | Recomendada
Fila 27: IGM-RS-02 | Capacidad análisis forense de sistemas de IA        | RESPONDER | NIST IR 8596 RS.AN-03  | Tier 2 | [entrada] | ... | 20 | Condicional
Fila 28: IGM-RS-03 | Conocimiento plazos de notificación IA             | RESPONDER | EU AI Act Art. 73      | Tier 1 | [entrada] | ... | 26 | Recomendada
Fila 29: IGM-RS-04 | MTTR-AI: Tiempo medio respuesta incidentes IA       | RESPONDER | NIST IR 8596 RS.AN-03  | Tier 1 | [entrada] | ... | 26 | Recomendada
Fila 30: IGM-RC-01 | Planes recuperación con rollback de modelos         | RECUPERAR | NIST IR 8596 RC.RP-02  | Tier 1 | [entrada] | ... | 22 | Recomendada
Fila 31: IGM-RC-02 | RTO-AI para sistemas de IA críticos                 | RECUPERAR | NIS2 Art. 21.2.c       | Tier 1 | [entrada] | ... | 25 | Recomendada
Fila 32: IGM-RC-03 | Revisión decisiones del sistema comprometido        | RECUPERAR | EU AI Act Art. 72.1    | Tier 2 | [entrada] | ... | 21 | Recomendada
```

### Validación de Datos en Columna F (Puntuación)

```
Tipo: Número entero
Mínimo: 1
Máximo: 5
Mensaje de entrada: "Puntúe de 1 (Inexistente) a 5 (Optimizado)"
Mensaje de error: "Introduzca un valor entre 1 y 5"
```

### Formato Condicional en Columna F

```
= 1 → Fondo Rojo (#FF4444), Texto Blanco — Crítico
= 2 → Fondo Naranja (#FF8C00), Texto Blanco — Inicial
= 3 → Fondo Amarillo (#FFD700), Texto Negro — Definido
= 4 → Fondo Verde claro (#90EE90), Texto Negro — Gestionado
= 5 → Fondo Verde (#228B22), Texto Blanco — Optimizado
```

---

## HOJA 4: "IGM-FAICP" (Resultados)

### Cálculo por Función

**Celda F4 — Media GOBERNAR (6 indicadores):**
```excel
=PROMEDIO(Autoevaluación!F4:F9)
```

**Celda F5 — Media IDENTIFICAR (5 indicadores):**
```excel
=PROMEDIO(Autoevaluación!F10:F14)
```

**Celda F6 — Media PROTEGER (6 indicadores):**
```excel
=PROMEDIO(Autoevaluación!F15:F20)
```

**Celda F7 — Media DETECTAR (5 indicadores):**
```excel
=PROMEDIO(Autoevaluación!F21:F25)
```

**Celda F8 — Media RESPONDER (4 indicadores):**
```excel
=PROMEDIO(Autoevaluación!F26:F29)
```

**Celda F9 — Media RECUPERAR (3 indicadores):**
```excel
=PROMEDIO(Autoevaluación!F30:F32)
```

### Cálculo IGM-FAICP Ponderado

**Celda F11 — IGM-FAICP Total:**
```excel
=(F4*0.20)+(F5*0.20)+(F6*0.25)+(F7*0.15)+(F8*0.10)+(F9*0.10)
```

**Celda G11 — Nivel de Madurez (texto):**
```excel
=SI(F11>=4.5,"💎 LÍDER",SI(F11>=3.5,"🟢 AVANZADO",SI(F11>=2.5,"🟡 DESARROLLADO",SI(F11>=1.5,"🟠 EMERGENTE","🔴 CRÍTICO"))))
```

**Celda F13 — Indicadores Tier 1 con puntuación crítica (≤2):**
```excel
=CONTAR.SI.CONJUNTO(Autoevaluación!E4:E32,"Tier 1",Autoevaluación!F4:F32,"<=2")
```

**Celda F14 — % de indicadores ≥ 3:**
```excel
=CONTAR.SI(Autoevaluación!F4:F32,">=3")/CONTAR(Autoevaluación!F4:F32)
```

**Celda F15 — Puntuación media indicadores condicionales PRAGMATIC:**
```excel
=PROMEDIO.SI(Autoevaluación!M4:M32,"Condicional",Autoevaluación!F4:F32)
```

### Tabla de Benchmarking

| Referencia | IGM Estimado | Fuente |
|------------|-------------|--------|
| Media global (Cisco CRI 2025, "AI Fortification Mature") | 1.40 ≈ | Cisco CRI 2025 |
| España (2% "Mature" total) | 1.40 ≈ | Cisco CRI 2025 |
| Objetivo mínimo regulatorio EU AI Act | 3.00 | EU AI Act 2024/1689 |
| Objetivo recomendado operadores esenciales NIS2 | 3.50 | NIS2 2022/2555 |
| Nivel CISO Clase Mundial (Cisco CRI "Mature") | 4.50 | Cisco CRI 2025 |

**Celda H11 — Brecha vs. objetivo mínimo regulatorio:**
```excel
=3.00-F11
```

**Celda H12 — Brecha vs. objetivo recomendado NIS2:**
```excel
=3.50-F11
```

### Gráfico Radar Polar (Spider Chart)

**Datos del gráfico:**
```
Serie: "Mi Organización"
Categorías: GOBERNAR | IDENTIFICAR | PROTEGER | DETECTAR | RESPONDER | RECUPERAR
Valores: F4 | F5 | F6 | F7 | F8 | F9

Serie: "Objetivo Mínimo EU AI Act" (línea discontinua)
Valores: 3 | 3 | 3 | 3 | 3 | 3

Serie: "Objetivo NIS2 Operadores Esenciales" (línea punteada)
Valores: 3.5 | 3.5 | 3.5 | 3.5 | 3.5 | 3.5
```

**Configuración:**
- Tipo: Gráfico de radar
- Escala: 0 a 5
- Colores: Organización=Azul sólido, EU AI Act=Naranja discontinuo, NIS2=Verde punteado
- Título: "Perfil IGM-FAICP — " & 'Datos Organización'!B3

---

## HOJA 5: "ROI CIBERSEGURIDAD IA"

### Modelo de Entradas (Costes)

| Celda | Campo | Descripción | Fórmula/Entrada |
|-------|-------|-------------|-----------------|
| C4 | Coste incidente IA promedio (€) | Estimado o histórico | Entrada numérica |
| C5 | Incidentes IA esperados sin mejoras (año) | Baseline de incidentes | Entrada numérica |
| C6 | Probabilidad de reducción con IGM ≥ 3.5 | Reducción probabilística | `50%` (basado en Cisco CRI data) |
| C7 | Inversión anual en mejora FAICP (€) | Total de medidas de mejora | Entrada numérica |
| C8 | Costes de multas regulatorias (esperado) | P(sanción) × Sanción media | Entrada numérica |
| C9 | Coste de formación y sensibilización (€/año) | Programa de formación IA | Entrada numérica |
| C10 | Coste herramientas de monitorización IA (€/año) | SIEM + MLOps + AI-BOM | Entrada numérica |
| C11 | Coste consultoría/auditoría FAICP (€/año) | Evaluación externa + GRC | Entrada numérica |

### Cálculo ROI

**Celda C14 — Pérdida esperada sin mejoras (ALE baseline):**
```excel
=C4*C5
```

**Celda C15 — Pérdida esperada con IGM ≥ 3.5 (ALE objetivo):**
```excel
=C4*C5*(1-C6)
```

**Celda C16 — Reducción de pérdida esperada (ROSI bruto):**
```excel
=C14-C15
```

**Celda C17 — Inversión total en mejora FAICP:**
```excel
=C7+C9+C10+C11
```

**Celda C18 — ROI Neto (€):**
```excel
=C16+C8-C17
```

**Celda C19 — ROI (%):**
```excel
=C18/C17
```

**Celda C20 — Período de recuperación de la inversión (meses):**
```excel
=SI(C16>0,(C17/(C16/12)),"N/A — Revisar supuestos")
```

**Celda C21 — ROSI (Return on Security Investment):**
```excel
=(C16-C17)/C17
```

### Tabla de Escenarios Automáticos

| Escenario | IGM Actual | IGM Objetivo | Inversión | ROSI | Período Recuperación |
|-----------|-----------|-------------|-----------|------|---------------------|
| Conservador | `='Autoevaluación'!F11 actual` | 3.0 | C17*0.5 | fórmula | fórmula |
| Base | `='Autoevaluación'!F11 actual` | 3.5 | C17 | fórmula | fórmula |
| Optimista | `='Autoevaluación'!F11 actual` | 4.5 | C17*1.5 | fórmula | fórmula |

### Notas Metodológicas del Modelo ROI

```
SUPUESTOS INCORPORADOS:
- La reducción de probabilidad de incidente del 50% para IGM ≥ 3.5 se basa en:
  Cisco CRI 2025: diferencial de incidentes entre niveles "Mature" vs. "Beginner"
  (dato: 87% de organizaciones con bajo IGM sufrieron incidentes vs. ~23% en Mature)
  
- El coste promedio de incidente IA no está estandarizado globalmente.
  Referencia: IBM Cost of a Data Breach Report 2025 (media global: 4.45M USD)
  Para España, ajustar al índice PPP y al perfil de sector específico.

- Las multas regulatorias esperadas se calculan como:
  P(incidente grave) × P(sanción) × Sanción media del sector
  
- El modelo NO incluye:
  Costes de reputación / pérdida de clientes
  Costes de interrupción de servicio (solo aplica si se incluyen en C4)
  Beneficios derivados de la habilitación de nuevos casos de uso IA seguros
  
ADVERTENCIA: Este modelo es orientativo. El ROSI en ciberseguridad tiene
limitaciones inherentes de medición (Hubbard & Seiersen, 2023). Se recomienda
complementar con análisis de montaje de Monte Carlo para escenarios de cola.
```

---

## HOJA 6: "PLAN DE ACCIÓN"

### Tabla Automática de Brechas Prioritarias

La hoja extrae automáticamente los indicadores con puntuación ≤ 3 y los ordena por:
1. Tier (Tier 1 primero)
2. Puntuación (más baja primero)
3. Puntuación PRAGMATIC (más alta primero — mayor valor de mejora)

**Fórmula de extracción (Excel 365 con FILTRAR):**
```excel
=ORDENAR(FILTRAR(Autoevaluación!A4:K32, Autoevaluación!F4:F32<=3), {5,6,12}, {1,1,-1})
```

**Para versiones anteriores de Excel (sin FILTRAR dinámico):**
Usar tabla dinámica con filtros manuales sobre la hoja Autoevaluación.

### Secciones de la Hoja

| Sección | Contenido |
|---------|-----------|
| **Top 5 Brechas Críticas** | Indicadores Tier 1 con puntuación ≤ 2, ordenados por impacto |
| **Calendario de Mejora** | Gantt simplificado con hitos a 90, 180 y 365 días |
| **Presupuesto por Función** | Desglose de la inversión total (C17 de HOJA 5) por función CSF 2.0 |
| **Métricas de Seguimiento** | KPIs de seguimiento del plan de acción (% completado, fechas objetivo) |

---

## HOJA 7: "BENCHMARKING CCAA" (Opcional)

### Estructura para Comparativa Territorial

Si la organización forma parte de un programa de benchmarking sectorial o autonómico (coordinado por INCIBE o el CCAA correspondiente), esta hoja permite comparar el IGM-FAICP propio con datos agregados del sector/CCAA.

| Columna | Contenido |
|---------|-----------|
| A | Función CSF 2.0 |
| B | IGM Propio (vinculado desde HOJA 4) |
| C | Media sectorial (dato externo — introducir manualmente) |
| D | Media CCAA (dato externo — introducir manualmente) |
| E | Media nacional (dato externo — basado en INCIBE/AESIA publicaciones) |
| F | Percentil de la organización en el sector |

**Gráfico de barras comparativo:** Barras agrupadas por función, con 4 series de datos (propio + 3 benchmarks).

---

## Especificaciones Técnicas de Implementación

### Protección de la Hoja

```
Hojas protegidas (sin contraseña de edición — solo protección estructural):
- INSTRUCCIONES: completamente bloqueada
- AUTOEVALUACIÓN: bloqueadas columnas A-E y H-M; editables F y G solamente
- IGM-FAICP: completamente bloqueada (solo lectura de fórmulas)
- PLAN DE ACCIÓN: tabla dinámica + campos editables de fechas y responsables

Hojas editables por el usuario:
- DATOS ORGANIZACIÓN: todos los campos de entrada
- ROI CIBERSEGURIDAD IA: todos los campos de entrada numérica
- BENCHMARKING CCAA: columnas C, D, E (datos externos)
```

### Nombres de Rango Definidos

```
IGM_GV = 'IGM-FAICP'!F4
IGM_ID = 'IGM-FAICP'!F5
IGM_PR = 'IGM-FAICP'!F6
IGM_DE = 'IGM-FAICP'!F7
IGM_RS = 'IGM-FAICP'!F8
IGM_RC = 'IGM-FAICP'!F9
IGM_TOTAL = 'IGM-FAICP'!F11
NIVEL_MADUREZ = 'IGM-FAICP'!G11
```

### Compatibilidad

```
Microsoft Excel: 2019 y superior (funcionalidades completas)
Microsoft Excel: 2016 (compatible con limitaciones: sin función FILTRAR dinámica)
Google Sheets: Compatible (traducir funciones SI→IF, PROMEDIO→AVERAGE, etc.)
LibreOffice Calc: Compatible con adaptaciones menores
```

---

*Documento parte del Kit FAICP 2025-2026 — Versión 1.0 — Abril 2026*  
*La implementación real en formato .xlsx requiere trasladar estas especificaciones a la herramienta de hojas de cálculo elegida siguiendo las instrucciones de cada sección.*
