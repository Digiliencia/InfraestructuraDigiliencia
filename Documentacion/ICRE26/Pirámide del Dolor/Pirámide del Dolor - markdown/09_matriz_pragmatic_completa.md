# Matriz de Evaluación PRAGMATIC Completa
## Métricas GQM para la Pirámide del Dolor

> Escala sugerida: 0 (muy pobre) – 3 (alto).  
> Estas valoraciones iniciales son orientativas; cada organización puede ajustarlas.

---

## 1. Leyenda de criterios

- P: Predictivo  
- R: Relevante  
- A: Accionable  
- G: Genuino  
- M: Significativo  
- P2: Preciso  
- T: Oportuno (Timely)  
- I: Independiente  
- C: Rentable (Cost-effective)

---

## 2. Métricas de IoC de bajo nivel (M1.x, M2.x)

| Métrica | Descripción | P | R | A | G | M | P2 | T | I | C | Comentario |
|--------|-------------|---|---|---|---|---|----|---|---|---|-----------|
| M1.1 | Mediana tiempo detección→distribución IoC | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 2 | Muy alineada con capacidad de reacción; requiere cierto esfuerzo de instrumentación. |
| M1.2 | % IoC distribuidos en menos de X horas | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 2 | Fácil de comunicar; útil para SLAs nacionales/sectoriales. |
| M1.3 | % incidentes donde IoC distribuido fue útil | 2 | 3 | 3 | 2 | 3 | 1 | 1 | 2 | 1 | Difícil de medir con precisión; requiere buen forense, pero muy accionable. |
| M2.1 | Vida media de IoC en listas activas | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | Ayuda a detectar listas “cementerio”; más descriptiva que predictiva. |
| M2.2 | Frecuencia de revisión de listas | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 3 | Sencilla de obtener; buena como indicador de disciplina operativa. |
| M2.3 | % IoC no observados en X días que siguen activos | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | Identifica sobrecarga de listas; requiere datos históricos de observación. |

---

## 3. Métricas de artefactos de red y host (M3.x, M4.x)

| Métrica | Descripción | P | R | A | G | M | P2 | T | I | C | Comentario |
|--------|-------------|---|---|---|---|---|----|---|---|---|-----------|
| M3.1 | % incidentes críticos con alerta de artefacto previa | 3 | 3 | 3 | 2 | 3 | 2 | 1 | 3 | 1 | Muy potente para ver si las reglas “sirven”; requiere buen enlace entre casos y alertas. |
| M3.2 | Antelación media de la primera alerta | 3 | 3 | 3 | 2 | 3 | 2 | 1 | 3 | 1 | Excelente como métrica de capacidad preventiva; algo costosa de calcular bien. |
| M3.3 | % alertas previas correctamente gestionadas | 2 | 3 | 3 | 2 | 3 | 2 | 1 | 3 | 1 | Pone el foco en procesos del SOC; requiere datos de workflow. |
| M4.1 | % falsos positivos en reglas de artefactos | 2 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | Clásica pero esencial; muy accionable para tuning. |
| M4.2 | Frecuencia de revisión de reglas | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 3 | Indicador de higiene del SOC; barato de obtener. |
| M4.3 | Variación % de falsos positivos tras revisión | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | Permite evaluar si el tuning tiene efectos reales. |

---

## 4. Métricas de TTP / ATT&CK (M5.x, M6.x)

| Métrica | Descripción | P | R | A | G | M | P2 | T | I | C | Comentario |
|--------|-------------|---|---|---|---|---|----|---|---|---|-----------|
| M5.1 | % reglas por nivel de la Pirámide | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | Buena para ver el “perfil” de detección; algo estática. |
| M5.2 | % incidentes detectados inicialmente por TTP | 3 | 3 | 3 | 2 | 3 | 2 | 1 | 3 | 1 | Muy alineada con el espíritu de la Pirámide; cálculo no trivial. |
| M5.3 | Incremento anual en M5.2 | 3 | 3 | 3 | 2 | 3 | 1 | 1 | 3 | 1 | Útil para medir progreso estratégico, aunque con inercia. |
| M6.1 | Cobertura ATT&CK de técnicas prioritarias | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | Métrica estrella para madurez en TTP; requiere buena gestión de matriz. |
| M6.2 | Tiempo medio de implementación de nuevas detecciones ATT&CK | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | Mide agilidad frente a nuevas técnicas; importante a nivel nacional. |
| M6.3 | % detecciones ATT&CK revisadas anualmente | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | Mide disciplina de mantenimiento de contenido de seguridad. |

---

## 5. Métricas de tiempo, eficacia y coste (M7.x, M8.x)

| Métrica | Descripción | P | R | A | G | M | P2 | T | I | C | Comentario |
|--------|-------------|---|---|---|---|---|----|---|---|---|-----------|
| M7.1 | MTTD con primera detección en IoC | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | Clásica; sirve de base para comparación con TTP. |
| M7.2 | MTTD con primera detección en TTP | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | Crítica para justificar inversión en TTP. |
| M7.3 | MTTR (IoC vs TTP) | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | Mide impacto operativo de la calidad de detección. |
| M7.4 | Diferencial MTTD/MTTR IoC vs TTP | 3 | 3 | 3 | 2 | 3 | 1 | 1 | 3 | 1 | Muy poderosa como narrativa, pero derivada de M7.1–7.3. |
| M8.1 | Incidentes graves/año pre vs post mejora TTP | 3 | 3 | 3 | 2 | 3 | 1 | 1 | 2 | 1 | Depende de una atribución rigurosa; alta relevancia estratégica. |
| M8.2 | Horas de analista por incidente pre vs post | 3 | 3 | 3 | 2 | 3 | 1 | 1 | 2 | 1 | Vincula directamente detección con carga de trabajo. |
| M8.3 | Ahorro anual y ROI estimado | 3 | 3 | 3 | 1 | 3 | 1 | 1 | 2 | 1 | Ideal para comités de presupuesto; requiere supuestos explícitos. |

---

## 6. Métricas de gobernanza y coordinación (M9.x)

| Métrica | Descripción | P | R | A | G | M | P2 | T | I | C | Comentario |
|--------|-------------|---|---|---|---|---|----|---|---|---|-----------|
| M9.1 | % info compartida por nivel de Pirámide | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | Indica calidad del intercambio (más allá de IoC). |
| M9.2 | # campañas/TTP compartidas por año | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | Potencia ecosistema de inteligencia; útil para índices nacionales. |
| M9.3 | # detecciones locales creadas a partir de info compartida | 3 | 3 | 3 | 2 | 3 | 1 | 1 | 3 | 1 | Excelente indicador de valor práctico del intercambio; medirlo requiere disciplina. |

---

## 7. Uso de la matriz

1. Seleccione las métricas propuestas que tengan mejor puntuación PRAGMATIC para su contexto.  
2. Ajuste las puntuaciones si dispone de información más precisa sobre coste, frecuencia, etc.  
3. Elimine (o deje en segundo plano) métricas con baja rentabilidad o baja accionabilidad, aunque sean conceptualmente atractivas.  
4. Revise las puntuaciones periódicamente, especialmente cuando cambien herramientas o procesos.

La idea no es coleccionar métricas con acrónimos impactantes, sino quedarse con un núcleo de indicadores que, además de ser técnicamente interesantes, pasen la prueba PRAGMATIC sin sonrojo.