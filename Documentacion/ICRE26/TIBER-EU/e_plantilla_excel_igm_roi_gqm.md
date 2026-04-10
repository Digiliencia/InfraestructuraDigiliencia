# Plantilla de Excel para cálculo de IGM y ROI (GQM + PRAGMATIC)

---

## 1. Principios de diseño

- Mantener una correspondencia directa entre:  
  - Metas GQM → Dimensiones del IGM.  
  - Métricas GQM → Columnas calculadas.  
- Incorporar factores PRAGMATIC como **pesos** opcionales en la agregación.

---

## 2. Hojas propuestas

1. `DatosEncuesta` – Respuestas por entidad.  
2. `Codificacion_GQM` – Conversión de categorías a valores.  
3. `PRAGMATIC` – Puntuaciones PRAGMATIC por métrica (PRED, REL, etc.).  
4. `IGM_Entidad` – Cálculo por entidad.  
5. `IGM_Sector` – Estadísticos agregados.  
6. `ROI_TIBER` – Cálculos de ROI.  

---

## 3. Codificación y pesos

### 3.1. Valores 0–5

Cada métrica M‑X‑Y debe tener:

- Columna `Valor_M_X_Y` en `Codificacion_GQM`.  
- Opcionalmente, columna `Peso_PRAGMATIC_M_X_Y` = media de (REL, ACC, GEN, SIG), por ejemplo.

### 3.2. Uso de pesos PRAGMATIC

En `IGM_Entidad`, la dimensión GOV podría calcularse como:

```text
= SUMAPRODUCTO(Rango_Valores_GOV; Rango_Pesos_GOV) / SUMA(Rango_Pesos_GOV)
```

De este modo, métricas más relevantes/accionables pesan más.

---

## 4. Cálculo del IGM

### 4.1. Dimensiones

- `GOV` basado en M‑GOV‑1, M‑GOV‑2, M‑GOV‑3, M‑GOV‑4.  
- `TI` basado en M‑TI‑1 a M‑TI‑4.  
- `RT` basado en M‑RT‑1 a M‑RT‑4.  
- `BLUE` basado en M‑BLUE‑1 a M‑BLUE‑4.  
- `PRP` basado en M‑PRP‑1 a M‑PRP‑4.

### 4.2. IGM total

```text
= PROMEDIO(GOV; TI; RT; BLUE; PRP)
```

o bien ponderado según relevancia nacional.

---

## 5. ROI con conexión GQM

En `ROI_TIBER`:

- Añadir columna que indique la **meta GQM principal** asociada a cada beneficio estimado (por ejemplo, BLUE‑1 para mejora de MTTD).  
- Documentar en comentarios de celda cómo se ha inferido la reducción de riesgo a partir de cambios en métricas clave.

---

_Fin de la plantilla GQM + PRAGMATIC._