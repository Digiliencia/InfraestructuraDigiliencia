# Plantilla Excel GQM+PRAGMATIC — Calculadora CSCRM
### Descripción funcional para implementación en Microsoft Excel / Google Sheets
**Versión 1.0 · Documento (e) del Kit GQM+PRAGMATIC CSCRM**

> *"Una hoja de cálculo bien diseñada no es un formulario: es un sistema de pensamiento que trabaja cuando su diseñador no está en la sala."*

---

## 1. Estructura del Libro — 10 Hojas

### Módulo I — Evaluación de Indicadores

| Hoja | Nombre | Función |
|------|--------|---------|
| 1 | `PORTADA` | Identificación de la organización, instrucciones, versión, contexto normativo |
| 2 | `INVENTARIO_INDICADORES` | 20 indicadores con metadata GQM completa + valores de referencia |
| 3 | `PRAGMATIC_SCORECARD` | Puntuación de los 9 criterios por indicador |
| 4 | `RANKING_PRAGMATIC` | Ranking automático + Conjunto Mínimo Viable |

### Módulo II — Medición Organizacional

| Hoja | Nombre | Función |
|------|--------|---------|
| 5 | `DATOS_MEDICION` | Valores actuales de cada indicador (entrada de datos) |
| 6 | `IGM_CALCULADO` | IGM global y subíndices calculados automáticamente |
| 7 | `BENCHMARK_GQM` | Comparativa con valores de referencia y objetivos |

### Módulo III — Análisis y Reporting

| Hoja | Nombre | Función |
|------|--------|---------|
| 8 | `ROI_INDICADORES` | ROI por indicador + modelo FAIR simplificado |
| 9 | `HOJA_RUTA_GQM` | Plan de acción priorizado GQM+PRAGMATIC+Normativa |
| 10 | `DASHBOARD_EJECUTIVO` | Panel con semáforos, radar y KPIs |

---

## 2. Hoja 2 — INVENTARIO_INDICADORES

Tabla de valores cargados en la hoja (referencia para implementación):

| ID | Indicador | Objetivo | Unidad | Val. Ref. España | Obj. 2028 | Obj. 2030 | PRAGMATIC | CMV |
|----|-----------|----------|--------|-----------------|----------|----------|-----------|-----|
| M01 | Tasa Incidentes CSCRM | O1 | % | ~22,5% | <18% | <12% | 63 | No |
| M02 | MTTD-SC | O1 | días | ~254d | <90d | <60d | 66 | **Sí** |
| M03 | Coste Medio Incidente | O1 | M€ | ~4,33 | <3,5 | <2,5 | 57 | No |
| M04 | Tasa Org. con Incidente | O1 | % | ~35% | <25% | <18% | 57 | No |
| M05 | Política CSCRM Formal | O2 | % | ~60% | ≥80% | ≥95% | 69 | No |
| M06 | Inventario Proveedores | O2 | % | ~55% | ≥85% | ≥95% | 69 | No |
| M07 | Distribución IGM | O2 | 0-5 | ~2,1 | ≥3,0 | ≥3,5 | 69 | **Sí** |
| M08 | Due Diligence | O2 | % | ~40% | ≥70% | ≥85% | 69 | No |
| M09 | Brecha por Dominio | O2 | 0-5 | — | ≤1,0 | ≤0,5 | 75 | **Sí** |
| M10 | Cobertura N-Tier | O3 | % | ~20% | ≥50% | ≥70% | 60 | No |
| M11 | Cobertura SBOM | O3 | % | ~15% | ≥50% | ≥75% | 72 | **Sí** |
| M12 | Madurez PQC | O3 | 0-4 | ~0,5 | ≥2,0 | ≥3,0 | 63 | No |
| M13 | PRI con CS | O4 | % | ~30% | ≥70% | ≥85% | 69 | **Sí** |
| M14 | Plazos NIS2 | O4 | % | — | ≥95% | ≥99% | 75 | **Sí** |
| M15 | ISACs | O4 | % | ~20% | ≥40% | ≥55% | 63 | No |
| M16 | Ejercicios con Prov. | O4 | N/año | ~0,3 | ≥1,5 | ≥2,0 | 69 | No |
| M17 | Zero Trust Prov. | O2+O3 | 0-5 | ~1,5 | ≥3,0 | ≥4,0 | 66 | No |
| M18 | Cláusulas Contractuales | O2 | % | ~45% | ≥80% | ≥95% | 75 | **Sí** |
| M19 | IA/ML Evaluados | O3 | % | ~10% | ≥40% | ≥65% | 63 | No |
| M20 | Ciclo de Vida Prov. | O2+O3 | 0-5 | ~1,8 | ≥3,5 | ≥4,5 | 78 | **Sí** |

*Fuentes de valores de referencia: ENISA NIS360 2025 · ENISA NIS Investments 2025 · Cipher/Prosegur Supply Chain Report 2026 · INCIBE-CERT IMC v2.8*

---

## 3. Hoja 3 — PRAGMATIC_SCORECARD

### Columnas:
```
A: ID indicador
B: Nombre indicador
C: P — Predictivo     (desplegable 0/3/6/9)
D: R — Relevante      (desplegable 0/3/6/9)
E: A — Accionable     (desplegable 0/3/6/9)
F: G — Genuino        (desplegable 0/3/6/9)
G: M — Significativo  (desplegable 0/3/6/9)
H: Ac — Preciso       (desplegable 0/3/6/9)
I: T — Oportuno       (desplegable 0/3/6/9)
J: I — Independiente  (desplegable 0/3/6/9)
K: C — Rentable       (desplegable 0/3/6/9)
L: TOTAL              =SUMA(C:K)
M: NIVEL              =SI(L>=65;"✅ Alta";SI(L>=40;"⚠️ Media";"❌ Débil"))
```

### Fórmulas de resumen (fila 23+):
```excel
=PROMEDIO(C2:C21)     → Media criterio P (repetir para D:K)
=CONTAR.SI(M2:M21;"✅ Alta")   → N.º de indicadores de Alta calidad
=CONTAR.SI(M2:M21;"⚠️ Media")  → N.º de indicadores de Media calidad
```

---

## 4. Hoja 5 — DATOS_MEDICION

### Columnas:
| Col | Contenido |
|-----|-----------|
| D | **Valor actual** (celda editable amarilla) |
| E | Fecha de medición |
| F | Fuente (desplegable: Encuesta / Auditoría / CCN-CERT / Cálculo interno) |
| G | Nivel de confianza (desplegable: Alta / Media / Baja) |
| J | Brecha = Objetivo - Valor actual |
| K | % avance = SI(D>=I;1;D/I)×100 |
| L | Semáforo = SI(K>=90;"🟢";SI(K>=60;"🟡";SI(K>=30;"🟠";"🔴"))) |

---

## 5. Hoja 6 — IGM_CALCULADO

### Fórmulas de cálculo del IGM:
```excel
IGM_GOBERNANZA     = media(M05, M06, M08, M18, M20) normalizados 0-5
IGM_IDENTIFICACION = media(M06, M08, M10) normalizados
IGM_PROTECCION     = media(M11, M12, M17, M18, M20) normalizados
IGM_DETECCION      = media(M01, M02, M04) con tabla de conversión
IGM_RESILIENCIA    = media(M13, M14, M15, M16) normalizados

IGM_GLOBAL = (IGM_G×0,20) + (IGM_I×0,20) + (IGM_P×0,25) + (IGM_D×0,20) + (IGM_R×0,15)

IGM_PONDERADO_PRAGMATIC =
  SUMA.PRODUCTO(valores_indicadores; pesos_PRAGMATIC_normalizados) / SUMA(pesos_PRAGMATIC)
```

### Tablas de conversión a escala 0-5:
```
MTTD-SC (días → 0-5):
  >365 = 0 | 181-365 = 1 | 91-180 = 2 | 31-90 = 3 | 8-30 = 4 | ≤7 = 5

Porcentajes (% → 0-5):
  <20% = 0 | 20-39% = 1 | 40-59% = 2 | 60-79% = 3 | 80-94% = 4 | ≥95% = 5

Cumplimiento NIS2 (% → 0-5):
  <60% = 0 | 60-74% = 1 | 75-84% = 2 | 85-94% = 3 | 95-98% = 4 | ≥99% = 5
```

---

## 6. Hoja 8 — ROI_INDICADORES

### Modelo FAIR simplificado:
```excel
ALE_base = N_proveedores × p_incidente × CMI_SC × Factor_IGM
  p_incidente = 0,08 (8% anual — Cipher/Prosegur 2026)
  CMI_SC = 4.330.000 € (coste medio — Cipher/Prosegur 2026)
  Factor_IGM = SI(IGM<2;1,6;SI(IGM<3;1,3;SI(IGM<4;1,0;0,75)))

ALE_mejorado = ALE_base × (1 - Reduccion_acumulada)
ROI_Mx = (Reduccion_ALE_Mx - Coste_mejora_Mx) / Coste_mejora_Mx × 100
Payback = Inversion_total / Reduccion_ALE_mensual
VAN_3a = VNA(8%; Rep1; Rep2; Rep3) - Inversion_año1
```

### Factores de reducción de riesgo por indicador (FAIR Institute 2025):
| Indicador | Factor |
|-----------|--------|
| M02 MTTD-SC | Cada -30 días = -8% riesgo |
| M06 Inventario | Cada +10% = -3% riesgo |
| M11 SBOM | Cada +10% cobertura = -4% riesgo |
| M13 PRI | Pasar <30% a >70% = -15% riesgo |
| M18 Contratos | Cada +10% = -2% riesgo |
| M20 Ciclo Vida | Cada nivel L = -12% riesgo |

---

## 7. Hoja 9 — HOJA_RUTA_GQM

### Fórmula de priorización integrada:
```excel
Puntuacion_prioridad =
  (Brecha_normalizada × 3)
  + (PRAGMATIC_score/81 × 2)
  + (Obligatoriedad × 4)
  + (Impacto_IGM × 3)
  - (Esfuerzo × 2)

Ranking = JERARQUIA(L_actual; $L$2:$L$21; 0)
```

---

## 8. Hoja 10 — DASHBOARD_EJECUTIVO

### Bloques del panel (formato A3 imprimible):

**Bloque 1 — KPIs de cabecera (4 celdas grandes):**
- IGM Global / 5,0 + semáforo
- Puntuación PRAGMATIC media
- MTTD-SC actual
- ROI programa + Payback

**Bloque 2 — Gráfico radar doble:**
- Eje: 5 dominios CSCRM
- Serie 1: valores actuales (azul)
- Serie 2: objetivos 2028 (verde)
- Serie 3: benchmark España (gris)

**Bloque 3 — Semáforos CMV (8 indicadores):**
```
| Indicador       | Valor | Obj. 2028 | Avance | Estado |
| M02 MTTD-SC     | [X]d  | <90d      | [XX]%  | [🔴]   |
| M07 IGM         | [X,X] | ≥3,0      | [XX]%  | [🟡]   |
| M09 Brecha Dom. | [X,X] | ≤1,0      | [XX]%  | [🟠]   |
| M11 SBOM        | [X]%  | ≥50%      | [XX]%  | [🔴]   |
| M13 PRI con CS  | [X]%  | ≥70%      | [XX]%  | [🟡]   |
| M14 Plazos NIS2 | [X]%  | ≥95%      | [XX]%  | [🟢]   |
| M18 Contratos   | [X]%  | ≥80%      | [XX]%  | [🟡]   |
| M20 Ciclo Vida  | [X,X] | ≥3,5      | [XX]%  | [🔴]   |
```

---

## 9. Compatibilidad y Configuración

| Software | Soporte | Notas |
|----------|---------|-------|
| Microsoft Excel 365/2021 | ✅ Completo | Recomendado para macros y formato condicional avanzado |
| Google Sheets | ✅ Funcional | VLOOKUP en lugar de BUSCARV; NPV en lugar de VNA |
| LibreOffice Calc 7.x | ⚠️ Parcial | Limitaciones en formato condicional complejo |

**Configuración recomendada:**
- Bloquear celdas de fórmula; solo editables las marcadas en **amarillo**
- Habilitar macros para actualización automática del ranking
- Aplicar formato condicional (semáforos) en todas las hojas de medición
- Habilitar Panel de Navegación para acceso rápido entre hojas

---
*© 2026 · Plantilla Excel GQM+PRAGMATIC CSCRM España · Documento (e)*
*Brotby & Hinson (2013) · NIST SP 800-55v2 dic. 2024 · FAIR Institute CRQ Guidelines 2025 · INCIBE-CERT IMC v2.8 · Cipher/Prosegur 2026*
