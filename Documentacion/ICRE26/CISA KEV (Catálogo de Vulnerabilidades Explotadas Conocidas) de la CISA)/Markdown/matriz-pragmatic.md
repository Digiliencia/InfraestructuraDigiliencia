# Matriz de Evaluación PRAGMATIC Completa para Indicadores KEV Nacionales

Esta matriz evalúa cada métrica propuesta para los indicadores nacionales relacionados con KEV utilizando los nueve criterios PRAGMATIC:

- **P**: Predictivo
- **R**: Relevante
- **A**: Accionable
- **G**: Genuino
- **M**: Significativo
- **P2**: Preciso
- **O**: Oportuno
- **I**: Independiente
- **C**: Coste‑efectivo (Cost‑effective)

Puntuación por criterio: 0 (muy pobre) a 10 (excelente).  
La columna **Total** es la suma (0–90) y la columna **Comentario global** resume la idoneidad de la métrica.

Leyenda rápida de calidad:

- **> 70**: Métrica excelente, prioritaria.
- **50–70**: Métrica buena, recomendable.
- **< 50**: Métrica débil, revisar.

---

## 1. Indicadores de Exposición

### E1 – % de organizaciones con ≥1 KEV expuesta

> **Definición**: Número de organizaciones con al menos una vulnerabilidad incluida en KEV presente en activos expuestos a Internet / número total de organizaciones analizadas.

| Métrica | P | R | A | G | M | P2 | O | I | C | Total | Comentario global |
|--------|---|---|---|---|---|----|---|---|---|-------|--------------------|
| E1: % de organizaciones con ≥1 KEV expuesta | 8 | 10 | 9 | 8 | 10 | 8 | 8 | 9 | 8 | 78 | Excelente métrica de foto de riesgo agregado. Muy relevante para responsables nacionales, permite comparaciones internacionales y es accionable vía programas sectoriales. Requiere buena cobertura de fuentes, pero el esfuerzo es razonable frente al valor que aporta. |

---

### E2 – Densidad media de KEV por organización expuesta

> **Definición**: Nº total de KEV detectadas en organizaciones / Nº de organizaciones con al menos una KEV.

| Métrica | P | R | A | G | M | P2 | O | I | C | Total | Comentario global |
|--------|---|---|---|---|---|----|---|---|---|-------|--------------------|
| E2: Densidad media de KEV por organización | 7 | 9 | 8 | 8 | 9 | 7 | 7 | 8 | 8 | 71 | Métrica muy útil para distinguir «expuestos accidentales» de «expuestos crónicos». Facilita priorizar acompañamiento y regulación por tramos de madurez. Algo más exigente en análisis, pero claramente coste‑efectiva. |

---

### E3 – Distribución de KEV por tipo de tecnología

> **Definición**: Porcentaje de KEV detectadas en distintas categorías tecnológicas (perímetro, file transfer, colaboración, CI/CD, etc.).

| Métrica | P | R | A | G | M | P2 | O | I | C | Total | Comentario global |
|--------|---|---|---|---|---|----|---|---|---|-------|--------------------|
| E3: % de KEV por tipo de tecnología | 7 | 9 | 8 | 8 | 9 | 7 | 8 | 8 | 7 | 71 | Métrica clave para orientar políticas y guías técnicas (por ejemplo, foco en perímetro y plataformas de transferencia). Relevante y accionable. El coste técnico está en clasificar bien activos y vulnerabilidades, pero es asumible. |

---

## 2. Indicadores de Capacidad de Respuesta

### R1 – Tiempo medio/mediano de remediación de KEV

> **Definición**: Mediana de días desde la fecha de inclusión en KEV hasta la fecha de cierre (parche/mitigación) de la vulnerabilidad.

| Métrica | P | R | A | G | M | P2 | O | I | C | Total | Comentario global |
|--------|---|---|---|---|---|----|---|---|---|-------|--------------------|
| R1: Mediana de días de remediación KEV | 9 | 10 | 9 | 8 | 10 | 7 | 8 | 8 | 7 | 76 | Indicador estrella de capacidad de respuesta. Fuertemente predictivo (quien parchea rápido hoy lo hará mañana), muy relevante y directamente accionable mediante SLAs, campañas y regulación. Precisión moderada si las fechas de cierre no están bien registradas, pero suficiente. |

---

### R2 – % de KEV remediadas dentro del plazo objetivo

> **Definición**: Nº de KEV remediadas antes de la fecha límite (CISA u objetivo nacional equivalente) / Nº total de KEV observadas.

| Métrica | P | R | A | G | M | P2 | O | I | C | Total | Comentario global |
|--------|---|---|---|---|---|----|---|---|---|-------|--------------------|
| R2: % de KEV remediadas en plazo | 9 | 10 | 9 | 8 | 10 | 7 | 8 | 9 | 8 | 78 | Métrica casi «de manual» para supervisión regulatoria. Permite fijar objetivos claros, comparables con modelos como BOD 22‑01. Ligeramente exigente en integración de datos, pero muy coste‑efectiva. |

---

### R3 – % de dispositivos perimetrales críticos con KEV abiertas

> **Definición**: Nº de dispositivos perimetrales expuestos con alguna KEV abierta / Nº total de dispositivos perimetrales expuestos inventariados.

| Métrica | P | R | A | G | M | P2 | O | I | C | Total | Comentario global |
|--------|---|---|---|---|---|----|---|---|---|-------|--------------------|
| R3: % de dispositivos perimetrales con KEV abiertas | 8 | 10 | 9 | 8 | 10 | 7 | 8 | 8 | 7 | 75 | Métrica muy alineada con los patrones reales de explotación (foco en perímetro). Altamente relevante y accionable: permite lanzar programas específicos sobre VPNs, firewalls, pasarelas, etc. Requiere buen inventario, pero ese esfuerzo ya es, en sí mismo, una mejora. |

---

## 3. Indicadores de Impacto

### I1 – % de incidentes significativos vinculados a KEV

> **Definición**: Nº de incidentes de gravedad alta/muy alta en los que el vector inicial o de escalada explotó una CVE incluida en KEV / Nº total de incidentes de esa gravedad.

| Métrica | P | R | A | G | M | P2 | O | I | C | Total | Comentario global |
|--------|---|---|---|---|---|----|---|---|---|-------|--------------------|
| I1: % de incidentes graves asociados a KEV | 8 | 10 | 8 | 7 | 10 | 6 | 7 | 8 | 7 | 71 | Métrica poderosa para comunicar impacto real («no son teorías, son incidentes»). Algo menos precisa, porque depende de buen etiquetado de causas en los registros de incidentes, pero el valor estratégico compensa el esfuerzo. |

---

### I2 – Incidentes KEV por millón de habitantes / por mil organizaciones

> **Definición**: Nº de incidentes graves relacionados con KEV normalizado por población o por número de organizaciones.

| Métrica | P | R | A | G | M | P2 | O | I | C | Total | Comentario global |
|--------|---|---|---|---|---|----|---|---|---|-------|--------------------|
| I2: Tasa de incidentes KEV normalizada | 7 | 9 | 7 | 7 | 9 | 6 | 7 | 9 | 7 | 68 | Muy útil para comparaciones entre países y regiones, y para justificar programas específicos. Menos directamente accionable a nivel micro, pero excelente para macro‑política pública. Precisión dependiente del censo de referencia y de la calidad del registro de incidentes. |

---

### I3 – Incidentes KEV en infraestructuras críticas

> **Definición**: Nº de incidentes significativos relacionados con KEV en operadores de servicios esenciales/importantes (NIS2, sectores ENS críticos) / Nº total de incidentes significativos en esos sectores.

| Métrica | P | R | A | G | M | P2 | O | I | C | Total | Comentario global |
|--------|---|---|---|---|---|----|---|---|---|-------|--------------------|
| I3: Incidentes KEV en infraestructuras críticas | 9 | 10 | 9 | 7 | 10 | 6 | 7 | 8 | 7 | 73 | Métrica de alto impacto político y social. Directamente relacionada con resiliencia de servicios esenciales. Exige coordinación con CSIRTs sectoriales, pero el retorno en términos de priorización de recursos y regulación es muy alto. |

---

## 4. Resumen y priorización

| ID | Métrica | Total PRAGMATIC | Prioridad recomendada |
|----|---------|-----------------|------------------------|
| E1 | % de organizaciones con ≥1 KEV expuesta | 78 | Muy alta – indicador estructural de exposición nacional. |
| E2 | Densidad media de KEV por organización | 71 | Alta – refina y matiza E1, útil para segmentar. |
| E3 | % de KEV por tipo de tecnología | 71 | Alta – guía focos tecnológicos de política y ayuda sectorial. |
| R1 | Mediana de días de remediación KEV | 76 | Muy alta – núcleo de la capacidad de respuesta. |
| R2 | % de KEV remediadas dentro del plazo | 78 | Muy alta – métrica clave de cumplimiento/eficacia. |
| R3 | % de dispositivos perimetrales con KEV abiertas | 75 | Muy alta – directamente alineada con patrón de ataque real. |
| I1 | % de incidentes graves asociados a KEV | 71 | Alta – excelente para narrativa de riesgo y justificación de inversión. |
| I2 | Tasa de incidentes KEV por población/organizaciones | 68 | Media‑alta – muy útil para benchmarking geográfico/sectorial. |
| I3 | Incidentes KEV en infraestructuras críticas | 73 | Muy alta – foco regulatorio y de seguridad nacional. |

En conjunto, el paquete de métricas E/R/I supera holgadamente el umbral de «métricas decentes» y se sitúa en la franja de **métricas estratégicas**: conectan con objetivos nacionales, se pueden accionar y, con una inversión razonable en datos, resultan sostenibles en el tiempo.

Si en algún momento se siente tentado de añadir diez métricas más «porque ya que estamos…», puede pasar cada candidata por esta misma tabla PRAGMATIC. Si no pasa de 50 puntos, lo más probable es que acabe en el cajón de métricas decorativas, junto a esas gráficas que nadie mira pero quedan muy bien en la memoria USB.
