# PLANTILLA EXCEL: CÁLCULO DE IGM Y ROI
## Indicadores GQM+PRAGMATIC Aplicados a OWASP SAMM

**Versión**: 1.0 | **Fecha**: Enero 2026  
**Propósito**: Estructura de hoja Excel para calcular IGM (Índice Global de Madurez) y ROI de ciberseguridad  
**Compatibilidad**: Microsoft Excel 2016+, Google Sheets, LibreOffice Calc

---

## 1. ARQUITECTURA DEL LIBRO EXCEL

Se recomienda un libro con 7 hojas:

```
┌─────────────────────────────────────────┐
│         LIBRO: Madurez_SAMM_IGM_ROI.xlsx│
├─────────────────────────────────────────┤
│ 1. CONFIG      — Parámetros globales    │
│ 2. METRICAS    — Valores observados     │
│ 3. PRAGMATIC   — Scores PRAGMATIC       │
│ 4. DOMINIO     — Índices por dominio    │
│ 5. IGM_GLOBAL  — Índice Global Madurez │
│ 6. COSTES      — Inversiones propuestas │
│ 7. ROI         — Cálculo de retorno     │
└─────────────────────────────────────────┘
```

---

## 2. HOJA "CONFIG" — PARÁMETROS GLOBALES

### Tabla 2.1 – Configuración general

**Estructura de columnas**:
- Col A: `Parámetro`
- Col B: `Valor`
- Col C: `Descripción/Notas`

**Filas recomendadas**:

| Fila | Parámetro | Valor (Ejemplo) | Descripción |
|------|-----------|---|---|
| 2 | `Org_Name` | Acme Corp | Nombre de la organización |
| 3 | `Eval_Date` | 2026-01-21 | Fecha de evaluación |
| 4 | `Evaluator` | CISO Team | Responsable de la medición |
| 5 | `IGM_Max` | 100 | Puntuación máxima IGM posible |
| 6 | `IGM_Target` | 80 | Meta IGM para 2026 |
| 7 | `Currency` | EUR | Moneda de costes |
| 8 | | | |
| 9 | **PESOS POR DOMINIO** | | |
| 10 | `Peso_GOV` | 0.15 | Gobernanza (15%) |
| 11 | `Peso_DES` | 0.15 | Diseño (15%) |
| 12 | `Peso_IMP` | 0.20 | Implementación (20%) |
| 13 | `Peso_VER` | 0.15 | Verificación (15%) |
| 14 | `Peso_OPS` | 0.20 | Operaciones (20%) |
| 15 | `Peso_TRAIN` | 0.15 | Capacitación (15%) |
| 16 | `TOTAL_PESOS` | =SUMA(B10:B15) | Debe ser 1.00 |

**Notas de implementación**:
- Los pesos pueden ajustarse según contexto (ej: si CRA es crítica, aumentar Peso_DES a 0.25).
- Las sumas de pesos deben sumar exactamente 1.00.

---

## 3. HOJA "METRICAS" — VALORES OBSERVADOS

### Tabla 3.1 – Estructura principal

**Columnas**:
- A: `ID_Metrica` (ej: M-IMP-01)
- B: `Dominio` (GOV/DES/IMP/VER/OPS/TRAIN/VULN/SIEM)
- C: `Nombre_Metrica` (ej: SAST Integration Coverage)
- D: `Valor_Actual` (valor observado)
- E: `Objetivo` (meta)
- F: `Unidad` (%, horas, #, etc.)
- G: `Normalizado_0_1` (valor normalizado 0-1)
- H: `Peso_Dominio` (ej: 1/6 si hay 6 métricas en IMP)
- I: `Score_Metrica` (contribución al dominio)

### Tabla 3.2 – Ejemplo de datos

| A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|
| M-IMP-01 | IMP | SAST Integration Coverage | 80 | 100 | % | =D3/E3 | =1/6 | =G3*H3 |
| M-OPS-01 | OPS | MTTD Mean | 12 | 4 | horas | =MIN(1;E4/D4) | =1/7 | =G4*H4 |
| M-TRAIN-02 | TRAIN | Phishing Click Rate | 8 | 5 | % | =1-(D5/E5) | =1/4 | =G5*H5 |

### Tabla 3.3 – Fórmulas detalladas

**En columna G (Normalizado_0_1)**: 

Para métricas "más alto es mejor" (ej: SAST Coverage):
```excel
=MIN(1; MAX(0; D3/E3))
```
Resultado: si D3=80%, E3=100% → G3=0.8

Para métricas "más bajo es mejor" (ej: MTTD):
```excel
=MIN(1; MAX(0; E4/D4))
```
Resultado: si D4=12h, E4=4h → G4=0.333... (a mejorar)

Para métricas "inversas" (ej: Phishing Click Rate, donde menos es mejor):
```excel
=MIN(1; MAX(0; 1-(D5/100)))
```
Resultado: si D5=8% → G5=0.92 (bueno)

**En columna I (Score_Metrica)**:
```excel
=G3*H3
```
Cada métrica contribuye al score del dominio proporcionalmente a su peso.

---

## 4. HOJA "PRAGMATIC" — EVALUACIÓN DE CALIDAD

### Tabla 4.1 – Estructura

**Columnas**:
- A: `ID_Metrica`
- B: `P_Predictivo` (1-5)
- C: `R_Relevante` (1-5)
- D: `A_Accionable` (1-5)
- E: `G_Genuino` (1-5)
- F: `M_Significativo` (1-5)
- G: `A_Preciso` (1-5)
- H: `T_Oportuno` (1-5)
- I: `I_Independiente` (1-5)
- J: `C_Rentable` (1-5)
- K: `Score_PRAGMATIC` (0-1)
- L: `Categoría_Calidad` (Excellente/Buena/Aceptable/Débil)
- M: `Recomendación` (Adoptar/Adoptar con cuidado/Evitar)

### Tabla 4.2 – Ejemplo

| A | B | C | D | E | F | G | H | I | J | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M-IMP-01 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | =SUMA(B2:J2)/(9*5) | Excellente | Adoptar |
| M-TRAIN-01 | 3 | 4 | 4 | 3 | 3 | 5 | 3 | 5 | 5 | =SUMA(B3:J3)/(9*5) | Aceptable | Adoptar con cuidado |

**Fórmula en columna K**:
```excel
=SUMA(B2:J2) / (9*5)
```
Resultado: score 0-1 (multiplicar ×100 para %).

**Fórmula en columna L** (categorización):
```excel
=SI(K2>0.89;"Excellente";SI(K2>0.79;"Buena";SI(K2>0.69;"Aceptable";"Débil")))
```

**Fórmula en columna M** (recomendación):
```excel
=SI(K2>0.85;"Adoptar";SI(K2>0.70;"Adoptar con cuidado";"Evitar"))
```

---

## 5. HOJA "DOMINIO" — ÍNDICES POR DOMINIO SAMM

### Tabla 5.1 – Agregación por dominio

**Columnas**:
- A: `Dominio`
- B: `Score_Bruto` (suma de scores de métricas)
- C: `Nº_Metricas` (count)
- D: `Score_Normalizado_0_1` (promedio)
- E: `Score_Madurez_%` (Score × 100)
- F: `Peso_Global`
- G: `Score_Ponderado`
- H: `Comentario`

### Tabla 5.2 – Ejemplo

| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| GOV | 1.85 | 4 | =B2/C2 | =D2*100 | 0.15 | =D2*F2 | Gobernanza débil |
| DES | 2.10 | 3 | =B3/C3 | =D3*100 | 0.15 | =D3*F3 | Mejorando |
| IMP | 2.65 | 4 | =B4/C4 | =D4*100 | 0.20 | =D4*F4 | Fuerte |
| VER | 1.95 | 4 | =B5/C5 | =D5*100 | 0.15 | =D5*F5 | A mejorar |
| OPS | 2.40 | 7 | =B6/C6 | =D6*100 | 0.20 | =D6*F6 | Maduro |
| TRAIN | 1.70 | 4 | =B7/C7 | =D7*100 | 0.15 | =D7*F7 | Muy débil |

**Nota**: Score bruto (B) se calcula automáticamente sumando scores de métricas en hoja METRICAS que pertenecen a cada dominio:

```excel
=SUMAR.SI(METRICAS!$B:$B; A2; METRICAS!$I:$I)
```

---

## 6. HOJA "IGM_GLOBAL" — ÍNDICE GLOBAL DE MADUREZ

### Tabla 6.1 – Resumen ejecutivo

**Sección superior: IGM actual vs. objetivo**

| Item | Fórmula | Valor |
|------|---------|-------|
| **IGM Actual** | =SUMA(DOMINIO!G2:G7)*CONFIG!B5 | (calcula automáticamente) |
| **IGM Objetivo (2026)** | CONFIG!B6 | 80 |
| **IGM Brecha** | =B2-B3 | (diferencia) |
| **% Cumplimiento Objetivo** | =B2/B3 | (porcentaje) |

**Sección media: Scores por dominio**

| Dominio | Score Madurez (%) | Posición Ranking | Color Status |
|---------|---|---|---|
| Gobernanza | =DOMINIO!E2 | (auto-ranking) | 🟡 Amarillo |
| Diseño | =DOMINIO!E3 | | 🟢 Verde |
| Implementación | =DOMINIO!E4 | | 🟢 Verde |
| Verificación | =DOMINIO!E5 | | 🟡 Amarillo |
| Operaciones | =DOMINIO!E6 | | 🟢 Verde |
| Capacitación | =DOMINIO!E7 | | 🔴 Rojo |

**Sección inferior: Gráfico recomendado**

- Tipo: Gráfico de barras horizontal (dominio vs. madurez)
- Rango: A9:B15
- Ejes: Nombres dominio (A), Scores % (B)

### Tabla 6.2 – Fórmula maestra de IGM

```excel
=SUMAR.PRODUCTO(DOMINIO!D2:D7; CONFIG!B10:B15)
```

Esto calcula: (Score GOV × Peso GOV) + (Score DES × Peso DES) + ... + (Score TRAIN × Peso TRAIN)

---

## 7. HOJA "COSTES" — INICIATIVAS DE MEJORA

### Tabla 7.1 – Estructura

**Columnas**:
- A: `ID_Iniciativa` (ej: INIT-SAST-01)
- B: `Nombre_Iniciativa`
- C: `Dominio_Impactado` (GOV/DES/IMP/etc.)
- D: `Métrica_Principal` (ej: M-IMP-01)
- E: `Descripción`
- F: `Valor_Actual_Metrica`
- G: `Valor_Target_Metrica`
- H: `Coste_Anual` (€)
- I: `Horizonte_Años`
- J: `Coste_Total` (€)
- K: `ΔIGM_Esperado` (puntos adicionales en IGM)
- L: `Prioridad` (Alta/Media/Baja)

### Tabla 7.2 – Ejemplo

| A | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|
| INIT-SAST-01 | Integrar SAST en CI/CD | IMP | M-IMP-01 | Extender SAST a todas las apps | 80% | 100% | 25000 | 3 | =H2*I2 | 5 | Alta |
| INIT-MTTD-01 | Mejorar SIEM (MTTD) | OPS | M-OPS-01 | ML rules en SIEM | 12h | 4h | 45000 | 3 | =H3*I3 | 8 | Alta |
| INIT-TRAIN-01 | Programa modular formación | TRAIN | M-TRAIN-01 | Rediseño curriculum | 85% | 95% | 15000 | 2 | =H4*I4 | 3 | Media |

---

## 8. HOJA "ROI" — CÁLCULO DE RETORNO DE INVERSIÓN

### Tabla 8.1 – Estructura ROI

**Columnas**:
- A: `ID_Iniciativa`
- B: `Coste_Total` (€) [vinculado a COSTES!J]
- C: `Tipo_Beneficio` (Reducción incidentes / Mejora compliance / ΔIGM / Múltiple)
- D: `Beneficio_Anual_Estimado` (€) [ahorro anual esperado]
- E: `Horizonte_Años` (años de beneficio)
- F: `Beneficio_Total` (€) [= D × E]
- G: `ROI_Simple_%` [= (F-B)/B × 100]
- H: `Payback_Años` [= B/D]
- I: `ΔIGM` (puntos madurez) [vinculado a COSTES!K]
- J: `Índice_Prioridad` (ROI + IGM)

### Tabla 8.2 – Ejemplo con cálculos

| A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|
| INIT-SAST-01 | 75000 | Reducción vulns | 35000 | 3 | 105000 | 40% | 2.1 | 5 | (G+I/100)*50 |
| INIT-MTTD-01 | 135000 | Reducción incidentes | 60000 | 3 | 180000 | 33% | 2.3 | 8 | (G+I/100)*50 |
| INIT-TRAIN-01 | 30000 | Reducción phishing | 15000 | 2 | 30000 | 0% | 2.0 | 3 | (G+I/100)*50 |

### Tabla 8.3 – Fórmulas detalles

**ROI Simple**:
```excel
=(F2-B2)/B2*100
```

**Payback**:
```excel
=B2/D2
```

**Índice Prioridad** (pondera ROI + ΔIGM):
```excel
=(G2 + I2)*0.5
```

---

## 9. CÁLCULO ALTERNATIVO: ROI FINANCIERO EXTENDIDO

Si desea incluir métricas más sofisticadas (EVA, TIR, VAN), considere:

### Tabla 9.1 – Flujos de caja descontados

| Año | Flujo Anual | Factor Desc. (10%) | Flujo Descontado |
|-----|---|---|---|
| 0 | -75000 | 1.00 | -75000 |
| 1 | 35000 | 0.909 | 31815 |
| 2 | 35000 | 0.826 | 28910 |
| 3 | 35000 | 0.751 | 26285 |
| **VAN** | | | **11010** |

**Fórmula VAN**:
```excel
=VAN(10%; D2:D4) + B2
```
(donde 10% es tasa de descuento corporativa)

**Fórmula TIR**:
```excel
=TIR(B2:B5)
```

---

## 10. USO PRÁCTICO: WORKFLOW MENSUAL

1. **Primera semana de mes**: Recopilar datos observados de cada métrica (columna D en METRICAS).
2. **Segunda semana**: Refrescar normalizaciones (col G).
3. **Tercera semana**: Sistema calcula automáticamente:
   - IGM Global
   - Scores por dominio
   - Tendencias
4. **Cuarta semana**: Reportar a gobernanza.

---

## 11. VALIDACIONES Y CONTROLES

Recomendaciones para evitar errores:

1. **Data validation en columnas de entrada**: Rango 0-5 para PRAGMATIC, % para valores percentuales.
2. **Fórmulas de chequeo**:
   - `=SI(SUMA(CONFIG!B10:B15)<>1;"ERROR: Pesos no suman 1";"OK")`
   - `=CONTAR.SI(METRICAS!B:B;DOMINIO!A2)` (verifica que cada métrica esté asignada)
3. **Formato condicional**: Colorear celdas de Score según rango (rojo <50%, amarillo 50-75%, verde >75%).

---

## CONCLUSIÓN

Este template Excel proporciona un sistema coherente para:
- ✅ Recopilar métricas observadas
- ✅ Normalizar valores a escala 0-1
- ✅ Calcular IGM global ponderado
- ✅ Modelar iniciativas y ROI
- ✅ Priorizar inversiones (ROI + ΔIGM)
- ✅ Reportar a ejecutivos en dashboard claro

**Descargable**: Implementación en Excel disponible en kit complementario.

