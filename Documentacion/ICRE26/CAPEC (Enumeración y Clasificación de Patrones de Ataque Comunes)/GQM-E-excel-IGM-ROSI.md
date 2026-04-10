# 📊 PLANTILLA EXCEL — CÁLCULO IGM-CAPEC Y ROI/ROSI
## Especificación Técnica Completa para Implementación
### Kit GQM+PRAGMATIC CAPEC-ESP · Documento E · Versión 1.0 · Abril 2026

---

> *«Una hoja Excel bien diseñada es el puente entre el rigor metodológico y el ejecutivo que necesita un número para defender el presupuesto de ciberseguridad ante el Consejo. Que ese número esté bien calculado es, precisamente, la diferencia entre un argumento y una anécdota.»*

---

## ESTRUCTURA GENERAL DEL LIBRO EXCEL

El libro Excel del Kit GQM+PRAGMATIC CAPEC-ESP consta de **8 hojas** con las siguientes funciones:

| # | Nombre de Hoja | Color de Pestaña | Función Principal |
|---|---|---|---|
| 1 | `INICIO` | Azul oscuro | Panel de navegación, instrucciones y estado global |
| 2 | `DATOS_ENCUESTA` | Gris claro | Entrada de datos brutos de la encuesta |
| 3 | `IGM_CAPEC` | Verde | Cálculo del Índice Global de Madurez CAPEC |
| 4 | `PRAGMATIC_SCORES` | Azul claro | Evaluación PRAGMATIC de cada métrica |
| 5 | `ROSI_CALCULATOR` | Naranja | Cálculo de ROI de Seguridad (ROSI/FAIR) |
| 6 | `DASHBOARD` | Rojo oscuro | Panel ejecutivo con gráficos e indicadores |
| 7 | `BENCHMARK` | Morado | Comparación sectorial y por tamaño de organización |
| 8 | `PLAN_ACCION` | Verde oscuro | Hoja de ruta de mejora basada en resultados |

---

## HOJA 1: `INICIO` — Panel de Navegación

### Estructura de la hoja INICIO

```
Fila 1: Título: "Kit GQM+PRAGMATIC CAPEC-ESP v1.0 — [Nombre Organización]"
Fila 2: Fecha de última actualización: [Fórmula =HOY()]
Fila 3-5: Bloque de identificación de la organización
Filas 7-20: Panel de estado de implementación (semáforo por hoja)
Filas 22-40: Instrucciones de uso
```

### Campos de identificación

| Campo | Celda | Tipo | Validación |
|---|---|---|---|
| Nombre organización | B3 | Texto | Libre |
| Sector NIS2 | B4 | Lista desplegable | Lista: Energía; Transporte; Banca; Infraestructura mercados; Salud; Agua; Digital; Administración; Otro |
| Tamaño | B5 | Lista desplegable | Lista: Grande (>250 emp.); Mediana (50-250); Pequeña (<50) |
| Fecha de evaluación | B6 | Fecha | Formato DD/MM/AAAA |
| Responsable | B7 | Texto | Libre |
| Categoría ENS | B8 | Lista desplegable | Lista: Alta; Media; Básica; No aplica |

### Panel de estado (semáforo)

```excel
Celda D10: =SI(DATOS_ENCUESTA!C5<>"","✅ DATOS INTRODUCIDOS","⬜ PENDIENTE")
Celda D11: =SI(IGM_CAPEC!B50>0,"✅ IGM CALCULADO","⬜ PENDIENTE")
Celda D12: =SI(ROSI_CALCULATOR!B30>0,"✅ ROSI CALCULADO","⬜ PENDIENTE")
```

---

## HOJA 2: `DATOS_ENCUESTA` — Entrada de Datos

### Estructura de columnas

| Col. | Campo | Tipo | Valores |
|---|---|---|---|
| A | ID_Pregunta | Texto | P01, P02, ... P50 |
| B | Sección | Texto | S1_Gobernanza, S2_Software, etc. |
| C | Texto_Pregunta | Texto | Pregunta completa (protegida) |
| D | Métrica_CAPEC | Texto | M-SW-1.1, M-IS-1.1, etc. |
| E | Respuesta_Cuantitativa | Número | Valor numérico directo (si aplica) |
| F | Respuesta_Likert | Número entero | 1-5 |
| G | Respuesta_Binaria | Número | 0 o 1 |
| H | Respuesta_Porcentaje | Porcentaje | 0%-100% |
| I | Notas_Respondente | Texto | Texto libre |
| J | Fuente_Verificación | Texto | Documento de evidencia |
| K | Fecha_Dato | Fecha | Fecha del dato reportado |
| L | Confianza | Número | 1=Baja; 2=Media; 3=Alta |

### Tabla de preguntas por sección

#### SECCIÓN 1: GOBERNANZA (P01-P07)

| ID | Pregunta | Métrica | Tipo Respuesta | Fórmula de Normalización |
|---|---|---|---|---|
| P01 | ¿Con qué frecuencia reporta el CISO al Consejo métricas CAPEC? | M-GOV-1.1 | Likert 1-5 | Directa: E5/5 |
| P02 | ¿El Consejo ha recibido formación específica en ciberseguridad en los últimos 12 meses? | M-GOV-1.3 | Binaria (0/1) | G6 * 1 |
| P03 | ¿Cuántos KRIs basados en CAPEC se reportan al Consejo? | M-GOV-1.3 | Cuantitativa (0-15) | MIN(E7/15, 1) |
| P04 | ¿Existe un inventario formal de activos críticos mapeado a patrones CAPEC? | M-GOV-1.2 | Likert 1-5 | E8/5 |
| P05 | ¿La política de gestión de riesgos referencia explícitamente CAPEC? | M-GOV-1.2 | Binaria (0/1) | G9 * 1 |
| P06 | ¿Se realizan revisiones formales del modelo de amenazas CAPEC? | M-GOV-1.2 | Likert 1-5 | E10/5 |
| P07 | Presupuesto de ciberseguridad como % del presupuesto TI total | M-GOV-1.2 | Porcentaje | MIN(H11/0.15, 1) |

#### SECCIÓN 2: SOFTWARE Y DESARROLLO SEGURO (P08-P14)

| ID | Pregunta | Métrica | Tipo Respuesta | Fórmula de Normalización |
|---|---|---|---|---|
| P08 | % patrones CAPEC Software (Likelihood=High) con control verificado | M-SW-1.1 | Porcentaje | H12 |
| P09 | MTTD medio para incidentes de dominio Software (horas) | M-SW-1.2 | Cuantitativa | MAX(0, 1-(E13/24)) |
| P10 | Número de CVEs activos críticos sin plan de remediación < 15 días | M-SW-1.3 | Cuantitativa | MAX(0, 1-(E14/10)) |
| P11 | % defectos SAST/DAST CAPEC remediados antes de producción | M-SW-2.1 | Porcentaje | H15 |
| P12 | ¿Existe pipeline CI/CD con quality gates de seguridad? | M-SW-2.1 | Likert 1-5 | E16/5 |
| P13 | ¿Los desarrolladores reciben formación en patrones CAPEC? | M-SW-1.1 | Likert 1-5 | E17/5 |
| P14 | ¿Se realizan pruebas de penetración alineadas con CAPEC? | M-SW-1.1 | Likert 1-5 | E18/5 |

#### SECCIÓN 3: INGENIERÍA SOCIAL (P15-P21)

| ID | Pregunta | Métrica | Tipo Respuesta | Fórmula de Normalización |
|---|---|---|---|---|
| P15 | Tasa de clic en simulaciones de phishing (último trimestre) | M-IS-1.1 | Porcentaje | MAX(0, 1-H19) |
| P16 | Frecuencia de campañas de simulación de phishing | M-IS-1.1 | Likert 1-5 | E20/5 |
| P17 | % incidentes IS clasificados con ID CAPEC | M-IS-1.2 | Porcentaje | H21 |
| P18 | MTTC para ataques de ingeniería social (minutos) | M-IS-1.3 | Cuantitativa | MAX(0, 1-(E22/240)) |
| P19 | ¿Existe programa formal de concienciación por perfil de riesgo? | M-IS-1.1 | Likert 1-5 | E23/5 |
| P20 | % personal con formación anti-phishing en los últimos 6 meses | M-IS-1.1 | Porcentaje | H24 |
| P21 | ¿Se realizan simulaciones de vishing y smishing (CAPEC-163)? | M-IS-1.1 | Binaria (0/1) | G25 * 1 |

#### SECCIÓN 4: CADENA DE SUMINISTRO (P22-P28)

| ID | Pregunta | Métrica | Tipo Respuesta | Fórmula de Normalización |
|---|---|---|---|---|
| P22 | % componentes SW terceros con SBOM generado y verificado | M-SC-1.1 | Porcentaje | H26 |
| P23 | ¿Existe proceso formal de evaluación de riesgo de proveedores TIC? | M-SC-1.1 | Likert 1-5 | E27/5 |
| P24 | Ratio detección pre-producción vulns supply chain | M-SC-1.2 | Porcentaje | H28 |
| P25 | MTTR vulns supply chain críticas (días) | M-SC-1.3 | Cuantitativa | MAX(0, 1-(E29/90)) |
| P26 | ¿Los contratos con proveedores TIC incluyen cláusulas de ciberseguridad? | M-SC-1.1 | Likert 1-5 | E30/5 |
| P27 | ¿Se verifican las cadenas de custodia de los artefactos software (firmas)? | M-SC-1.2 | Likert 1-5 | E31/5 |
| P28 | ¿Existe proceso de evaluación de seguridad de componentes open source? | M-SC-1.1 | Likert 1-5 | E32/5 |

#### SECCIÓN 5: COMUNICACIONES Y CRIPTOGRAFÍA (P29-P34)

| ID | Pregunta | Métrica | Tipo Respuesta | Fórmula de Normalización |
|---|---|---|---|---|
| P29 | % tráfico de red protegido con TLS 1.3 o mTLS | M-NET-1.1 | Porcentaje | H33 |
| P30 | Número de certificados TLS con algoritmos vulnerables (SHA-1, RSA<2048) | M-NET-1.2 | Cuantitativa | MAX(0, 1-(E34/10)) |
| P31 | ¿Existe inventario criptográfico completo actualizado? | M-PQC-1.1 | Likert 1-5 | E35/5 |
| P32 | % algoritmos criptográficos catalogados y evaluados vs. quantum | M-PQC-1.1 | Porcentaje | H36 |
| P33 | % sistemas con datos longa vida migrados o en migración a PQC | M-PQC-1.2 | Porcentaje | H37 |
| P34 | ¿Existe plan formal de migración post-cuántica con hitos? | M-PQC-1.2 | Likert 1-5 | E38/5 |

#### SECCIÓN 6: HARDWARE Y OT (P35-P40)

| ID | Pregunta | Métrica | Tipo Respuesta | Fórmula de Normalización |
|---|---|---|---|---|
| P35 | % dispositivos críticos con firmware verificado y actualizado | M-HW-1.1 | Porcentaje | H39 |
| P36 | ¿Existe proceso de verificación criptográfica de firmware? | M-HW-1.1 | Likert 1-5 | E40/5 |
| P37 | % activos OT críticos segmentados del entorno IT (verificado) | M-OT-1.1 | Porcentaje | H41 |
| P38 | ¿Se aplica el modelo Purdue o IEC 62443 como referencia de segmentación? | M-OT-1.1 | Likert 1-5 | E42/5 |
| P39 | ¿Existe inventario diferenciado de activos IT y OT? | M-OT-1.1 | Binaria (0/1) | G43 * 1 |
| P40 | Frecuencia de auditorías de segmentación IT/OT | M-OT-1.1 | Likert 1-5 | E44/5 |

#### SECCIÓN 7: IA ADVERSARIAL (P41-P45)

| ID | Pregunta | Métrica | Tipo Respuesta | Fórmula de Normalización |
|---|---|---|---|---|
| P41 | % modelos IA en producción con controles adversariales probados | M-AI-1.1 | Porcentaje | H45 |
| P42 | ¿Existe registro formal de modelos de IA (model registry)? | M-AI-1.1 | Binaria (0/1) | G46 * 1 |
| P43 | Nivel de madurez del proceso de Prompt Injection Testing (0-4) | M-AI-1.2 | Cuantitativa | E47/4 |
| P44 | ¿Se realizan evaluaciones de red teaming adversarial sobre modelos IA? | M-AI-1.1 | Likert 1-5 | E48/5 |
| P45 | ¿Existe política formal de seguridad de IA (AI security policy)? | M-AI-1.1 | Binaria (0/1) | G49 * 1 |

#### SECCIÓN 8: RESILIENCIA Y CONTINUIDAD (P46-P50)

| ID | Pregunta | Métrica | Tipo Respuesta | Fórmula de Normalización |
|---|---|---|---|---|
| P46 | % patrones CAPEC alta severidad del sector incluidos en BCP/DRP | M-RES-1.2 | Porcentaje | H50 |
| P47 | Número de tabletop exercises con escenarios CAPEC en el último año | M-RES-1.3 | Cuantitativa | MIN(E51/4, 1) |
| P48 | ¿El BCP incluye escenarios de ransomware alineados con CAPEC-549? | M-RES-1.2 | Binaria (0/1) | G52 * 1 |
| P49 | ¿El RTO definido por tipo de activo ha sido probado en ejercicio real? | M-RES-1.1 | Likert 1-5 | E53/5 |
| P50 | Tiempo desde el último ejercicio de recuperación completo (meses) | M-RES-1.1 | Cuantitativa | MAX(0, 1-(E54/12)) |

---

## HOJA 3: `IGM_CAPEC` — Cálculo del Índice Global de Madurez

### Fórmula maestra del IGM-CAPEC

El IGM-CAPEC es un índice ponderado que agrega los 8 dominios en un valor entre 0 y 5:

```
IGM-CAPEC = (w_GOV × IGD_GOV) + (w_SW × IGD_SW) + (w_IS × IGD_IS) + 
            (w_SC × IGD_SC) + (w_NET × IGD_NET) + (w_HW × IGD_HW) + 
            (w_OT × IGD_OT) + (w_AI × IGD_AI) + (w_RES × IGD_RES)
```

### Pesos por dominio (configurables)

| Celda | Dominio | Peso defecto | Justificación del peso |
|---|---|---|---|
| B5 | w_GOV — Gobernanza | 0,20 | Gobernanza habilita todos los demás dominios |
| B6 | w_SW — Software | 0,18 | Mayor superficie de ataque en organizaciones digitales |
| B7 | w_IS — Ingeniería Social | 0,15 | Vector de entrada más frecuente en incidentes graves |
| B8 | w_SC — Supply Chain | 0,15 | Crecimiento exponencial del vector (2024-2025) |
| B9 | w_NET — Comunicaciones | 0,10 | Base tecnológica; controlada por controles criptográficos |
| B10 | w_HW — Hardware | 0,07 | Relevante pero con menor frecuencia de explotación exitosa |
| B11 | w_OT — ICS/OT | 0,05 | Solo para organizaciones con activos OT (ajustar a 0 si no aplica) |
| B12 | w_AI — IA Adversarial | 0,05 | Peso bajo por madurez emergente; aumentar en 2027-2028 |
| B13 | w_RES — Resiliencia | 0,05 | Capacidad de recuperación como complemento a prevención |
| B14 | **TOTAL** | **1,00** | Verificación: `=SUMA(B5:B13)` — debe ser exactamente 1,00 |

**Validación de pesos:**
```excel
B15: =SI(SUMA(B5:B13)=1,"✅ Pesos válidos","⚠️ REVISAR: los pesos no suman 1,00")
```

### Cálculo de puntuaciones por dominio

#### Dominio Gobernanza (IGD_GOV)

```excel
E5: =PROMEDIO(
    DATOS_ENCUESTA!E5/5,              [P01 - Frecuencia reporte Consejo]
    DATOS_ENCUESTA!G6,                 [P02 - Formación directivos]
    MIN(DATOS_ENCUESTA!E7/15,1),      [P03 - KRIs CAPEC reportados]
    DATOS_ENCUESTA!E8/5,              [P04 - Inventario activos mapeado]
    DATOS_ENCUESTA!G9,                 [P05 - Política referencia CAPEC]
    DATOS_ENCUESTA!E10/5,             [P06 - Revisiones modelo amenazas]
    MIN(DATOS_ENCUESTA!H11/0.15,1)    [P07 - % presupuesto seguridad]
    )
```

Puntuación IGD_GOV en escala 1-5:
```excel
F5: =E5*5
```

#### Dominio Software (IGD_SW)

```excel
E6: =PROMEDIO(
    DATOS_ENCUESTA!H12,               [P08 - Cobertura M-SW-1.1]
    MAX(0,1-(DATOS_ENCUESTA!E13/24)), [P09 - MTTD normalizado M-SW-1.2]
    MAX(0,1-(DATOS_ENCUESTA!E14/10)),[P10 - CVEs sin plan M-SW-1.3]
    DATOS_ENCUESTA!H15,               [P11 - Remediación pre-prod M-SW-2.1]
    DATOS_ENCUESTA!E16/5,             [P12 - Pipeline CI/CD M-SW-2.1]
    DATOS_ENCUESTA!E17/5,             [P13 - Formación desarrolladores]
    DATOS_ENCUESTA!E18/5              [P14 - Pruebas penetración CAPEC]
    )
F6: =E6*5
```

#### Dominio Ingeniería Social (IGD_IS)

```excel
E7: =PROMEDIO(
    MAX(0,1-DATOS_ENCUESTA!H19),      [P15 - Tasa clic invertida M-IS-1.1]
    DATOS_ENCUESTA!E20/5,             [P16 - Frecuencia simulaciones]
    DATOS_ENCUESTA!H21,               [P17 - Clasificación CAPEC incidentes]
    MAX(0,1-(DATOS_ENCUESTA!E22/240)),[P18 - MTTC normalizado M-IS-1.3]
    DATOS_ENCUESTA!E23/5,             [P19 - Programa concienciación formal]
    DATOS_ENCUESTA!H24,               [P20 - % personal formado]
    DATOS_ENCUESTA!G25                [P21 - Simulaciones vishing/smishing]
    )
F7: =E7*5
```

#### Dominio Supply Chain (IGD_SC)

```excel
E8: =PROMEDIO(
    DATOS_ENCUESTA!H26,               [P22 - Cobertura SBOM M-SC-1.1]
    DATOS_ENCUESTA!E27/5,             [P23 - Proceso evaluación proveedores]
    DATOS_ENCUESTA!H28,               [P24 - Ratio detección pre-prod M-SC-1.2]
    MAX(0,1-(DATOS_ENCUESTA!E29/90)), [P25 - MTTR normalizado M-SC-1.3]
    DATOS_ENCUESTA!E30/5,             [P26 - Cláusulas seguridad contratos]
    DATOS_ENCUESTA!E31/5,             [P27 - Verificación cadena custodia]
    DATOS_ENCUESTA!E32/5              [P28 - Evaluación open source]
    )
F8: =E8*5
```

#### Dominio Comunicaciones (IGD_NET)

```excel
E9: =PROMEDIO(
    DATOS_ENCUESTA!H33,               [P29 - Cobertura TLS M-NET-1.1]
    MAX(0,1-(DATOS_ENCUESTA!E34/10)), [P30 - Certificados vulnerables M-NET-1.2]
    DATOS_ENCUESTA!E35/5,             [P31 - Inventario criptográfico M-PQC-1.1]
    DATOS_ENCUESTA!H36,               [P32 - Cobertura inventory PQC]
    DATOS_ENCUESTA!H37,               [P33 - Progreso migración PQC M-PQC-1.2]
    DATOS_ENCUESTA!E38/5              [P34 - Plan migración PQC formal]
    )
F9: =E9*5
```

#### Dominio Hardware (IGD_HW)

```excel
E10: =PROMEDIO(
    DATOS_ENCUESTA!H39,               [P35 - Cobertura firmware M-HW-1.1]
    DATOS_ENCUESTA!E40/5              [P36 - Proceso verificación firmware]
    )
F10: =E10*5
```

#### Dominio OT/ICS (IGD_OT)

```excel
E11: =PROMEDIO(
    DATOS_ENCUESTA!H41,               [P37 - Segmentación OT M-OT-1.1]
    DATOS_ENCUESTA!E42/5,             [P38 - Modelo referencia IEC 62443]
    DATOS_ENCUESTA!G43,               [P39 - Inventario IT/OT diferenciado]
    DATOS_ENCUESTA!E44/5              [P40 - Auditorías segmentación]
    )
F11: =E11*5
```

#### Dominio IA Adversarial (IGD_AI)

```excel
E12: =PROMEDIO(
    DATOS_ENCUESTA!H45,               [P41 - Cobertura controles IA M-AI-1.1]
    DATOS_ENCUESTA!G46,               [P42 - Model registry]
    DATOS_ENCUESTA!E47/4,             [P43 - Madurez Prompt Injection M-AI-1.2]
    DATOS_ENCUESTA!E48/5,             [P44 - Red teaming adversarial]
    DATOS_ENCUESTA!G49                [P45 - Política seguridad IA]
    )
F12: =E12*5
```

#### Dominio Resiliencia (IGD_RES)

```excel
E13: =PROMEDIO(
    DATOS_ENCUESTA!H50,               [P46 - BCP con patrones CAPEC M-RES-1.2]
    MIN(DATOS_ENCUESTA!E51/4,1),      [P47 - Tabletop exercises anuales]
    DATOS_ENCUESTA!G52,               [P48 - BCP incluye ransomware CAPEC]
    DATOS_ENCUESTA!E53/5,             [P49 - RTO probado en ejercicio]
    MAX(0,1-(DATOS_ENCUESTA!E54/12))  [P50 - Recencia ejercicio recuperación]
    )
F13: =E13*5
```

### Cálculo del IGM-CAPEC Global

```excel
[Celda B20] IGM-CAPEC (normalizado 0-1):
=B5*E5 + B6*E6 + B7*E7 + B8*E8 + B9*E9 + B10*E10 + B11*E11 + B12*E12 + B13*E13

[Celda B21] IGM-CAPEC (escala 0-5):
=B20*5

[Celda B22] Nivel de Madurez:
=SI(B21>=4,"🟢 AVANZADO (4-5): Programa maduro con mejora continua",
 SI(B21>=3,"🟡 ESTABLECIDO (3-4): Controles implementados con brechas menores",
 SI(B21>=2,"🟠 EN DESARROLLO (2-3): Controles básicos; brechas significativas",
 "🔴 INICIAL (0-2): Exposición alta; acción urgente requerida")))
```

### Tabla de tendencia (comparación histórica)

| Celda | Período | IGM | Variación |
|---|---|---|---|
| C30 | Q1 2025 | [dato previo] | [baseline] |
| C31 | Q2 2025 | [dato previo] | `=C31-C30` |
| C32 | Q3 2025 | [dato previo] | `=C32-C31` |
| C33 | Q4 2025 | [dato previo] | `=C33-C32` |
| **C34** | **Q1 2026** | **=B21** | **=C34-C33** |

---

## HOJA 5: `ROSI_CALCULATOR` — Cálculo de ROI de Seguridad

### Metodología ROSI (Return on Security Investment)

La fórmula base del ROSI es:

```
ROSI = (ALE_antes - ALE_después - Coste_control) / Coste_control × 100%

Donde:
ALE (Annual Loss Expectancy) = ARO × SLE
ARO (Annual Rate of Occurrence) = Frecuencia anual de un tipo de incidente
SLE (Single Loss Expectancy) = Coste medio por incidente de ese tipo
```

### Tabla de cálculo ROSI por dominio CAPEC

#### Parámetros de entrada

| Celda | Parámetro | Valor defecto | Fuente de referencia |
|---|---|---|---|
| B5 | Coste medio incidente Software (€) | 285.000 | IBM Cost of Data Breach 2024 (ajustado España) |
| B6 | ARO incidente Software (sin controles) | 0,45 | INCIBE 2025 + sector |
| B7 | Coste medio incidente IS (€) | 185.000 | ENISA ETL 2025 |
| B8 | ARO incidente IS (sin controles) | 0,65 | Alta frecuencia vector phishing |
| B9 | Coste medio incidente Supply Chain (€) | 520.000 | Ponemon 2024 Supply Chain |
| B10 | ARO incidente Supply Chain (sin controles) | 0,25 | Frecuencia creciente pero menor que phishing |
| B11 | Coste medio incidente ransomware/OT (€) | 1.200.000 | ENISA / CCN-CERT 2024 |
| B12 | ARO incidente OT/ransomware (sin controles) | 0,15 | Alta consecuencia, menor frecuencia |

#### Reducción de riesgo basada en IGM-CAPEC

```excel
[Celda D5] Factor de reducción de riesgo (Software):
=MIN(IGM_CAPEC!E6 * 0.18, 0.85)
[Explicación: un IGD_SW de 1,0 (máximo) reduce el riesgo un 85%; 
la relación es lineal con tope para evitar sobreestimación]

[Celda D6] ALE Software ANTES de controles:
=B5 * B6

[Celda D7] ALE Software DESPUÉS de controles:
=D6 * (1 - D5)

[Celda D8] Coste anual controles Software (entrada manual):
[Ingresar coste real de controles del dominio]

[Celda D9] ROSI Software (%):
=(D6 - D7 - D8) / D8 * 100
```

#### Cálculo ROSI agregado

```excel
[Celda B40] ALE Total antes de todos los controles:
=(B5*B6) + (B7*B8) + (B9*B10) + (B11*B12)

[Celda B41] ALE Total después de controles CAPEC (ponderado por IGM):
=B40 * (1 - IGM_CAPEC!B20 * 0.75)
[Interpretación: un IGM-CAPEC de 1,0 reduce el ALE un 75%]

[Celda B42] Coste total anual programa de controles:
=SUMA(D8, D12, D16, D20)  [suma de costes por dominio]

[Celda B43] ROSI Global (%):
=(B40 - B41 - B42) / B42 * 100

[Celda B44] Período de recuperación de la inversión (meses):
=B42 / ((B40 - B41) / 12)

[Celda B45] VAN del programa de seguridad a 3 años (tasa descuento 8%):
=-B42 + ((B40-B41)/(1+0,08)) + ((B40-B41)/(1+0,08)^2) + ((B40-B41)/(1+0,08)^3)
```

---

## HOJA 6: `DASHBOARD` — Panel Ejecutivo

### Gráficos a generar en Excel

#### Gráfico 1: Radar Chart — IGM-CAPEC por Dominio
```
Tipo: Gráfico de radar (araña)
Datos: F5:F13 (puntuaciones 1-5 por dominio)
Categorías: Gobernanza, Software, Ing.Social, SupplyChain, Comunicaciones, Hardware, OT, IA, Resiliencia
Umbral verde: Línea de referencia en 3,0
Colores: Área < 2: Rojo transparente; 2-3: Naranja transparente; > 3: Verde transparente
Título: "Índice de Madurez CAPEC por Dominio — [Nombre Org] — [Trimestre]"
```

#### Gráfico 2: Gauge Chart — IGM-CAPEC Global
```
Tipo: Medidor (simulado con gráfico de anillo)
Valor: IGM_CAPEC!B21 (escala 0-5)
Zonas: 0-2 Rojo; 2-3 Naranja; 3-4 Amarillo; 4-5 Verde
```

#### Gráfico 3: Barras — Score PRAGMATIC vs. Implementación
```
Tipo: Gráficas de barras horizontales dobles
Eje X1: Score PRAGMATIC (calidad de la métrica, 0-5)
Eje X2: Puntuación actual de implementación (0-5)
Orden: De mayor a menor brecha (PRAGMATIC - Implementación)
Interpretación: Mayor brecha = mayor prioridad de mejora
```

#### Gráfico 4: Línea de tendencia — Evolución IGM-CAPEC
```
Tipo: Gráfico de líneas
Datos: IGM_CAPEC!C30:C34 (histórico trimestral)
Línea de referencia: y = 3,0 (umbral "Establecido")
Proyección: Tendencia lineal a 4 trimestres
```

### Panel de KPIs ejecutivos

```excel
[Dashboard!B10] IGM-CAPEC actual: =IGM_CAPEC!B21 (formato: 0,0)
[Dashboard!B11] Tendencia vs. trimestre anterior: =IGM_CAPEC!C34-IGM_CAPEC!C33 (formato con flecha ▲▼)
[Dashboard!B12] Dominio más fuerte: =INDICE({"GOV";"SW";"IS";"SC";"NET";"HW";"OT";"AI";"RES"},COINCIDIR(MAX(IGM_CAPEC!F5:F13),IGM_CAPEC!F5:F13,0))
[Dashboard!B13] Dominio más crítico: =INDICE({"GOV";"SW";"IS";"SC";"NET";"HW";"OT";"AI";"RES"},COINCIDIR(MIN(IGM_CAPEC!F5:F13),IGM_CAPEC!F5:F13,0))
[Dashboard!B14] ROSI Global: =ROSI_CALCULATOR!B43 (formato: 0,0%)
[Dashboard!B15] Período recuperación inversión: =ROSI_CALCULATOR!B44 (formato: 0,0 " meses")
```

---

## HOJA 7: `BENCHMARK` — Comparación Sectorial

### Valores de referencia para benchmarking

| Sector NIS2 | IGM-CAPEC Referencia (P50) | IGM-CAPEC Excelencia (P90) | Fuente |
|---|---|---|---|
| Banca / Finanzas | 3,2 | 4,1 | ENISA NIS360 2024; DORA baseline |
| Energía / Utilities | 2,8 | 3,7 | ENISA ETL 2025 sector energía |
| Salud | 2,4 | 3,3 | ENISA NIS360 2024 sector salud |
| Administración Pública | 2,6 | 3,5 | CCN-CERT Informe ENS 2024 |
| Transporte | 2,5 | 3,4 | ENISA 2024 sector transporte |
| Telecomunicaciones | 3,0 | 4,0 | ENISA NIS360 2024 |
| Manufactura / Industria | 2,2 | 3,0 | IBM X-Force 2025 sector industrial |

```excel
[Benchmark!B5] Sector seleccionado: =INICIO!B4
[Benchmark!C5] IGM actual organización: =IGM_CAPEC!B21
[Benchmark!D5] Referencia sectorial (P50): 
=BUSCARV(B5,{"Banca";3,2;"Energía";2,8;"Salud";2,4;"Adm. Pública";2,6;"Transporte";2,5;"Telecomunicaciones";3,0;"Manufactura";2,2},2,0)
[Benchmark!E5] Brecha vs. referencia:
=C5-D5
[Benchmark!F5] Posicionamiento:
=SI(C5>=D5,"Por encima de la mediana sectorial","Por debajo de la mediana sectorial")
```

---

## HOJA 8: `PLAN_ACCION` — Hoja de Ruta de Mejora

### Generación automática de prioridades

```excel
[Plan_Accion!A5:G20] Tabla de acciones por prioridad:

Columna A: Dominio (de menor a mayor puntuación IGD)
=ORDENAR({"GOV";"SW";"IS";"SC";"NET";"HW";"OT";"AI";"RES"},
          IGM_CAPEC!F5:F13, 1) [ordenado por puntuación ascendente]

Columna B: Puntuación actual IGD
[Valor del dominio correspondiente de IGM_CAPEC!F5:F13]

Columna C: Objetivo a 6 meses
=B5 + 0,5 [mejora realista de +0,5 puntos en 6 meses]

Columna D: Gap a cerrar
=C5 - B5

Columna E: Prioridad de acción (TOP 3 dominios con menor puntuación)
=SI(JERARQUIA(B5,IGM_CAPEC!F5:F13,1)<=3,"🔴 CRÍTICO","🟡 SEGUIMIENTO")

Columna F: Acción principal recomendada
=SI(B5<2,
    "Implementar controles básicos y establecer línea base de medición",
    SI(B5<3,
        "Formalizar procesos y automatizar recolección de métricas",
        SI(B5<4,
            "Optimizar controles existentes y reducir brechas específicas",
            "Mantener y mejorar incrementalmente; compartir mejores prácticas")))

Columna G: Responsable (entrada manual)
```

---

*Kit GQM+PRAGMATIC CAPEC-ESP · Documento E: Plantilla Excel IGM-CAPEC y ROSI · Versión 1.0 · Abril 2026*
*Implementar con Microsoft Excel 365 o Google Sheets (ajustar sintaxis de fórmulas de array según plataforma)*
