# Plantilla de Excel para Cálculo de IGM y ROI
## Extensión GQM + PRAGMATIC para la Pirámide del Dolor

Esta plantilla complementa la ya definida para IGM y ROI, incorporando explícitamente:

- El vínculo GQM (qué objetivo y pregunta alimenta cada métrica).  
- Las puntuaciones PRAGMATIC asociadas a cada métrica, para priorización.

---

## 1. Estructura del libro

Se sugiere un libro con las siguientes hojas:

1. `Catalogo_Metricas`  
2. `Puntuacion_PRAGMATIC`  
3. `Datos_Encuesta`  
4. `IGM_GQM`  
5. `ROI`  
6. `Resumen_Ejecutivo`

---

## 2. Hoja `Catalogo_Metricas`

Columnas:

- A: ID_Metrica (M1.1, M1.2, …, M9.3)  
- B: Descripción  
- C: Objetivo_GQM (G1, G2, …, G9)  
- D: Pregunta_GQM (Q1.1, Q2.1, etc.)  
- E: Nivel_Piramide (IoC, Artefactos, TTP, Gobernanza)  
- F: Tipo (tiempo, porcentaje, conteo, etc.)  
- G: Unidad (horas, %, nº, etc.)  
- H: Instrucciones de cálculo (texto breve)

---

## 3. Hoja `Puntuacion_PRAGMATIC`

Columnas:

- A: ID_Metrica  
- B: P (Predictivo)  
- C: R (Relevante)  
- D: A (Accionable)  
- E: G (Genuino)  
- F: M (Significativo)  
- G: P2 (Preciso)  
- H: T (Oportuno)  
- I: I (Independiente)  
- J: C (Rentable)  
- K: PRAGMATIC_Total (suma o media)  
- L: Comentario

Las puntuaciones pueden partir de la matriz propuesta y ajustarse a la realidad específica de cada implementación.  
Una fórmula sencilla para `PRAGMATIC_Total` sería:

```excel
=SUMA(B2:J2)
```

o bien una media:

```excel
=PROMEDIO(B2:J2)
```

---

## 4. Hoja `Datos_Encuesta`

Se reutiliza la estructura anterior, añadiendo columnas para aquellas métricas GQM que requieran datos adicionales (por ejemplo, tiempos, conteos).

Columnas:

- A: ID_Organizacion  
- B: Sector  
- C: Tamaño  
- …  
- Z en adelante: métricas cuantitativas (M1.1, M1.2, …) rellenadas con valores reales.

---

## 5. Hoja `IGM_GQM`

### 5.1 Selección de métricas según PRAGMATIC

En esta hoja se recomienda:

1. Importar desde `Puntuacion_PRAGMATIC` las métricas con `PRAGMATIC_Total` por encima de un umbral (por ejemplo, ≥18 sobre 27 si escala 0–3).  
2. Utilizar esas métricas para construir los subíndices de madurez (IoC, Artefactos, TTP, Gobernanza).

Se puede utilizar una columna auxiliar en `Catalogo_Metricas`:

- M: Usar_en_IGM (Sí/No según puntuación PRAGMATIC).

### 5.2 Cálculo de subíndices

Para cada organización:

- IGM_IoC_GQM  
- IGM_Artefactos_GQM  
- IGM_TTP_GQM  
- IGM_Gobernanza_GQM

Cálculo general (similar al anterior):

```excel
=SUMAPRODUCTO(Valores_Metrica_IoC, Pesos_IoC) / SUMA(Pesos_IoC)
```

Donde los pesos pueden ponderar tanto la importancia del objetivo GQM como la puntuación PRAGMATIC.

Por ejemplo, un **peso compuesto**:

```text
Peso_Final = Peso_GQM * (PRAGMATIC_Total / PRAGMATIC_Maximo)
```

Así, las métricas con alto valor PRAGMATIC pesan más en el índice final.

---

## 6. Hoja `ROI`

La estructura se mantiene como en la plantilla anterior, pero se recomienda:

- Referenciar explícitamente las métricas M7.x y M8.x como base de cálculo.  
- Documentar en comentarios o celdas de texto qué objetivos GQM respaldan el modelo de ROI (principalmente G7 y G8).

Ejemplo de referencias:

- M7.2 (MTTD con detección TTP) → influye en reducción de impacto.  
- M8.1 (incidentes graves pre/post) → base de ahorro en costes.  
- M8.2 (horas de analista) → ahorro operativo.

---

## 7. Hoja `Resumen_Ejecutivo`

Elementos sugeridos:

- Tabla con los subíndices IGM por nivel de la Pirámide.  
- Lista de 5–10 métricas “estrella”, con alta puntuación PRAGMATIC, destacadas.  
- Gráfico sencillo del ROI estimado asociado a la mejora en TTP.  
- Nota textual: “Estas métricas se seleccionan por su alto valor PRAGMATIC (relevancia, accionabilidad y coste razonable).”

---

## 8. Recomendaciones de implementación

- **No intentar calcular todas las métricas a la vez**: empezar por un subconjunto con alta puntuación PRAGMATIC.  
- **Documentar el linaje GQM**: tener claro qué objetivo respalda cada indicador en la hoja `Catalogo_Metricas`.  
- **Revisar anual o bianualmente las métricas seleccionadas**, para ajustar ponderaciones o introducir nuevas conforme evolucione el contexto.

Si la hoja de cálculo empieza a parecer una novela rusa, es señal de que quizá se han incorporado demasiadas métricas sin pasar la criba PRAGMATIC.