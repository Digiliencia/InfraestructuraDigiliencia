# Matriz de Evaluación PRAGMATIC Completa  
## Métricas SQUARE bajo el microscopio

> Escala por criterio: 0 = no, 1 = parcialmente, 2 = sí.  
> Puntuación total máxima por métrica: 18.

---

## 1. Leyenda de métricas

- **M1.1** Cobertura de funciones de negocio críticas con requisitos de seguridad explícitos.  
- **M1.2** Cobertura de amenazas de alto impacto con requisitos mitigadores definidos.  
- **M1.3** Porcentaje de requisitos de seguridad que cumplen criterios de buena ingeniería (claros, verificables, trazables).  
- **M1.4** Porcentaje de requisitos que superan la revisión sin observaciones críticas.  
- **M1.5** Número medio de iteraciones de revisión necesarias hasta aceptar los requisitos.  

- **M2.1** Número de activos críticos sin requisitos de seguridad asociados.  
- **M2.2** Porcentaje de riesgos de alto impacto con requisitos esenciales asignados.  
- **M2.3** Porcentaje de requisitos mapeados explícitamente a marcos normativos (NIS2, ENS, etc.).  
- **M2.4** Frecuencia de revisión de requisitos tras incidentes o cambios importantes.  
- **M2.5** Índice de Gestión de Mandato (IGM) para requisitos de seguridad.

- **M3.1** Coste anual del proceso de requisitos de seguridad.  
- **M3.2** Beneficios estimados por incidentes evitados/mitigados.  
- **M3.3** Beneficios por reducción de retrabajo.  
- **M3.4** Beneficios en auditorías/certificaciones.  
- **M3.5** ROI de requisitos de seguridad.  
- **M3.6** Correlación entre IGM e indicadores de resultado (incidentología, sanciones, etc.).

---

## 2. Matriz PRAGMATIC

### 2.1. Métricas de madurez de requisitos (M1.x)

| Métrica | Predictivo | Relevante | Accionable | Genuino | Significativo | Preciso | Oportuno | Independiente | Rentable | Total |
|--------|------------|-----------|-----------|---------|--------------|---------|----------|--------------|----------|-------|
| M1.1 Cobertura funciones críticas | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 17 |
| M1.2 Cobertura amenazas alto impacto | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 16 |
| M1.3 % requisitos bien formados | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 15 |
| M1.4 % requisitos sin observaciones | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 15 |
| M1.5 Iteraciones de revisión | 1 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 15 |

Notas de juicio (resumidas):

- **M1.1** es extremadamente relevante, clara y medible; altamente predictiva de problemas de diseño si baja; muy barata de recoger si hay herramientas mínimas.  
- **M1.2** añade la dimensión de riesgo; ligeramente menos oportuna si los análisis de amenazas se actualizan con baja frecuencia.  
- **M1.3** y **M1.4** dependen de una checklist y proceso de revisión; genuinidad moderada (pueden maquillarse), pero de alto valor si el proceso es honesto.  
- **M1.5** es una métrica de fricción: muchas iteraciones pueden indicar complejidad o inmadurez; pocas, tanto eficiencia como desidia, según contexto.

---

### 2.2. Métricas de alineamiento riesgo–normativa (M2.x)

| Métrica | Predictivo | Relevante | Accionable | Genuino | Significativo | Preciso | Oportuno | Independiente | Rentable | Total |
|--------|------------|-----------|-----------|---------|--------------|---------|----------|--------------|----------|-------|
| M2.1 Activos críticos sin requisitos | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 17 |
| M2.2 % riesgos alto impacto con requisito esencial | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 16 |
| M2.3 % requisitos mapeados a normativa | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 15 |
| M2.4 Frecuencia de revisión tras incidentes/cambios | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | 15 |
| M2.5 Índice de Gestión de Mandato (IGM) | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 13 |

Notas:

- **M2.1** es una métrica demoledora y casi imposible de maquillar cuando se dispone de inventario fiable. Puntuación muy alta.  
- **M2.2** se acerca al ideal de ver cuántos riesgos “desnudos” quedan.  
- **M2.3** ayuda a conectar con cumplimiento; genuinidad limitada si el mapeo se hace solo por obligación.  
- **M2.4** mide reflejos organizativos tras shocks; precisión puede depender de registros internos.  
- **M2.5** (IGM) es sintética y útil, pero su construcción introduce subjetividad y costes de mantenimiento.

---

### 2.3. Métricas económicas y de resultado (M3.x)

| Métrica | Predictivo | Relevante | Accionable | Genuino | Significativo | Preciso | Oportuno | Independiente | Rentable | Total |
|--------|------------|-----------|-----------|---------|--------------|---------|----------|--------------|----------|-------|
| M3.1 Coste anual proceso requisitos | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 17 |
| M3.2 Beneficios por incidentes evitados | 2 | 2 | 2 | 0 | 2 | 0 | 1 | 1 | 1 | 11 |
| M3.3 Beneficios por retrabajo reducido | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 13 |
| M3.4 Beneficios en auditorías/certificaciones | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 12 |
| M3.5 ROI de requisitos de seguridad | 2 | 2 | 2 | 0 | 2 | 0 | 1 | 1 | 1 | 11 |
| M3.6 Correlación IGM–resultados | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 | 14 |

Notas:

- **M3.1** es fácil de medir, muy relevante para gestión; cuesta poco si la contabilidad distingue partidas.  
- **M3.2** y **M3.5** brillan en narrativa, pero sufren en precisión y genuinidad: estimar incidentes evitados es arte más que ciencia.  
- **M3.3** y **M3.4** son algo más tangibles, pero también requieren modelos de coste y datos de seguimiento.  
- **M3.6** es analíticamente poderosa, aunque dependiente de disponer de suficientes datos históricos.

---

## 3. Selección de métricas núcleo para cuadro de mando SQUARE

Sobre la base de la matriz, se recomiendan como **métricas núcleo** (alto puntaje y equilibrio entre valor y coste):

- M1.1 Cobertura funciones críticas con requisitos.  
- M1.2 Cobertura de amenazas de alto impacto.  
- M1.3 % requisitos bien formados.  
- M2.1 Activos críticos sin requisitos.  
- M2.2 % riesgos alto impacto con requisito esencial.  
- M3.1 Coste anual del proceso de requisitos.  
- M3.6 Correlación IGM–resultados (en análisis agregados).

El resto pueden actuar como métricas de apoyo o para estudios específicos de ROI.

---

## 4. Uso práctico de PRAGMATIC

En la implementación:

- Los juicios PRAGMATIC pueden adaptarse por sector (por ejemplo, en sanidad la oportunidad de actualización puede ser más crítica).  
- Es recomendable documentar las razones de cada valoración, para futuras revisiones.  
- Las métricas con puntuación PRAGMATIC baja pero alta utilidad política (por ejemplo, ROI) deben usarse con **discursos honestos** sobre sus limitaciones.

La tabla no pretende dogma; quiere ser más bien una lista de preguntas incómodas antes de enamorarse de un número.

---