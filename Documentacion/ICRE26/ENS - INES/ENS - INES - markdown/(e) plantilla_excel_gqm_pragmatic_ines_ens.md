# Plantilla de Excel para IGM y ROI con enfoque GQM + PRAGMATIC

> Una hoja de cálculo que no solo calcula, sino que recuerda por qué está calculando.

---

## 1. Hojas propuestas

1. `Diccionario_Metricas`: definición GQM + PRAGMATIC de cada métrica.  
2. `Datos_Encuesta`: datos brutos (encuesta ENS–INES).  
3. `IGM_Madurez`: cálculo de índices de madurez.  
4. `ROI_Seguridad`: cálculo de ROI básico.  
5. `PRAGMATIC_Score`: evaluación global de la “salud” del sistema de métricas.  
6. `Cuadros_Mando`: gráficos y tablas para directivos.

---

## 2. Hoja `Diccionario_Metricas`

Columnas mínimas:

- `ID_Metrica` (ej. 2.2.1).  
- `Dominio` (Implantación, Incidentes, Proveedores, etc.).  
- `Goal_GQM` (referencia) y `Question_GQM` resumen.  
- `Definicion_Metrica` (texto).  
- `Fuente_Dato` (herramienta, sistema, encuesta).  
- `Periodicidad`.  
- PRAGMATIC: `PRED`, `REL`, `ACC`, `GEN`, `SIG`, `PRE`, `OPO`, `IND`, `REN` (valores A/M/B).  
- `Comentario_Interpretacion` (cómo usarla en decisiones).

Esta hoja sirve como contrato explícito sobre qué significa cada número.

---

## 3. Hoja `Datos_Encuesta`

Muy similar a la plantilla ya descrita para ENS–INES, con algunas columnas adicionales para enlazar con GQM:

- `Org_ID`, `Nombre_Org`, `Sector`, `Tamaño`, `Criticidad_ENS`.  
- Métricas base:  
  - `Pct_Medidas_ENS_Implantadas` (1.1.1).  
  - `Frecuencia_Revision_Medidas_Meses` (1.2.1).  
  - `Pct_Evidencias_Automatizadas` (1.3.1).  
  - `Incidentes_Graves_por_1000_Activos` (2.1.1).  
  - `MTTD_Horas` (2.2.1).  
  - `MTTR_Horas` (2.2.2).  
  - `Pct_Presupuesto_Seguridad` (2.3.1 / 7.1.1).  
  - `FTE_Seguridad` (2.3.2).  
  - `Interrupciones_Servicios_Criticos` (3.1.1).  
  - `Pct_Cumplimiento_RTO` (3.2.1).  
  - `Pct_Incidentes_Causa_Raiz` (3.3.1).  
  - `Pct_Contratos_Clausulas_ENS_NIS2` (4.1.1).  
  - `Pct_Proveedores_Evaluados` (4.2.1).  
  - `Ejercicios_Con_Proveedores` (4.3.1).  
  - `Mad_*` (madurez dominio) e `IGM_Global`.  
  - `ROI_Percibido`.  
  - Etc.

---

## 4. Hoja `IGM_Madurez`

Igual que en la plantilla anterior, pero explicitando referencias GQM:

- Para cada organización, se calculan:  
  - `IGM_Riesgos`, `IGM_Identidades`, `IGM_Incidentes`, `IGM_Continuidad`, `IGM_Proveedores`, `IGM_Formacion`, `IGM_Metricas`.  
  - `IGM_Global` como media (o media ponderada).  

Se pueden incluir:

- `Delta_IGM_Global` = `IGM_Global_Año_Actual – IGM_Global_Año_Anterior`.  
- `Delta_IGM_*` por dominio.

Estas métricas se mapean directamente a Goal 5 (mejora de madurez).

---

## 5. Hoja `ROI_Seguridad`

Variables:

- `Gasto_TIC_Total`.  
- `Gasto_Seguridad` = `Pct_Presupuesto_Seguridad * Gasto_TIC_Total`.  
- `Coste_Medio_Incidente_Grave` (parámetro configurable).  
- `Incidentes_Graves_Observados`.  
- `Incidentes_Graves_Estimados_sin_Medidas` (modelo o escenario).  
- `Incidentes_Graves_Evitados` = `Incidentes_Estimados – Observados`.  
- `Beneficio_Estimado` = `Incidentes_Evitados * Coste_Medio_Incidente_Grave`.  
- `ROI_Basico` = `(Beneficio_Estimado – Gasto_Seguridad) / Gasto_Seguridad` (7.2.1).

Las celdas pueden comentarse con la referencia GQM/PRAGMATIC correspondiente.

---

## 6. Hoja `PRAGMATIC_Score`

Objetivo: evaluar, a nivel de sistema, si el conjunto de métricas es saludable.

- Filas: métricas (`ID_Metrica`).  
- Columnas: PRED, REL, ACC, GEN, SIG, PRE, OPO, IND, REN (valores numéricos: A=3, M=2, B=1).  
- `Score_Total` = suma o media de los nueve criterios.  
- `Score_Medio` = `Score_Total/9`.  

Se pueden generar:

- Distribución de puntuaciones totales.  
- Identificación de métricas con `Score_Medio < 2` (candidatas a revisión/eliminación).  
- Métricas estrella (`Score_Medio > 2,5`).

---

## 7. Hoja `Cuadros_Mando`

- Gráficos de IGM vs. incidentes.  
- Gráficos de inversión vs. ROI.  
- Gráficos de distribución PRAGMATIC (por dominio).

---

## 8. Comentarios de implementación

- Conviene centralizar definiciones en `Diccionario_Metricas` para evitar divergencias entre hojas.  
- La plantilla puede nutrirse de exportaciones de INES, SIEM, GRC, etc.  
- La complejidad puede escalar gradualmente: empezar con un subconjunto de métricas de alto valor PRAGMATIC e ir ampliando.

> Excel no hará el milagro solo, pero al menos podrá demostrar que las decisiones se tomaron mirando algo más que el horóscopo.