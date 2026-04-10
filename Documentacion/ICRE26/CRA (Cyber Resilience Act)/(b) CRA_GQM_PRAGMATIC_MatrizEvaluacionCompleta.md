# Matriz de Evaluación PRAGMATIC Completa para indicadores CRA

> Escala 1–5: 1 = Muy bajo, 5 = Muy alto.  
> El objetivo no es que todas las métricas saquen un 5 en todo, sino entender su perfil.

---

## 1. Convención de lectura

- Columna “Métrica” = nombre breve del indicador.  
- Columnas P–R–A–G–M–Prc–O–I–Rnt = puntuaciones PRAGMATIC.  
- Columna “Comentario” = síntesis cualitativa.

---

## 2. Matriz PRAGMATIC

```markdown
| ID | Métrica                                                      | P (Pred) | R (Rel) | A (Acc) | G (Gen) | S (Sig) | Prc (Prec) | O (Oport) | I (Indep) | Rnt (Rent) | Comentario breve                                                                                 |
|----|--------------------------------------------------------------|----------|---------|---------|---------|---------|------------|-----------|-----------|------------|--------------------------------------------------------------------------------------------------|
| M1.1 | % modelos declarados CRA                                   | 3        | 5       | 4       | 4       | 4       | 4          | 4         | 3         | 4          | Buen indicador de alineamiento de catálogo; moderadamente predictivo del riesgo global.         |
| M1.2 | Cuota de mercado productos CRA                             | 4        | 5       | 4       | 4       | 5       | 3          | 3         | 3         | 4          | Más significativo que el mero nº de modelos; exige datos de mercado menos precisos.             |
| M2.1 | % fabricantes con procesos de vulnerabilidades certificados| 3        | 5       | 4       | 4       | 4       | 4          | 3         | 4         | 4          | Mide madurez estructural; buena base para políticas de supervisión.                             |
| M2.2 | % productos de fabricantes certificados                    | 3        | 5       | 4       | 4       | 5       | 3          | 3         | 3         | 3          | Relevante pero dependiente de datos comerciales; precisión moderada.                            |
| M3.1 | Nº certificados EUCC por nivel                             | 3        | 4       | 3       | 4       | 4       | 5          | 4         | 5         | 4          | Datos sólidos, fáciles de obtener; dan una visión estructural del esfuerzo de certificación.    |
| M3.2 | Distribución % por nivel EUCC                              | 3        | 4       | 3       | 4       | 4       | 5          | 4         | 5         | 4          | Útil para ver dónde se concentra el nivel de garantía; análisis comparativo entre países.       |
| M4.1 | % activos críticos con productos CRA-conformes             | 4        | 5       | 5       | 4       | 5       | 3          | 3         | 3         | 3          | Altamente accionable pero requiere buenos inventarios OT/IT; coste de medición no trivial.      |
| M5.1 | TTP medio vulnerabilidades críticas                        | 5        | 5       | 5       | 4       | 5       | 4          | 3         | 3         | 3          | Excelente predictor de exposición; clave para supervisión y diálogo con fabricantes.            |
| M5.2 | Distribución TTP (p90, mediana)                            | 5        | 5       | 5       | 4       | 5       | 4          | 3         | 3         | 3          | Añade matices; permite identificar colas largas de riesgo.                                       |
| M6.1 | % vulns explotadas > 12 meses                              | 5        | 5       | 5       | 4       | 5       | 3          | 3         | 3         | 3          | Métrica estrella de “deuda de vulnerabilidades”; exige datos coordinados de varias fuentes.     |
| M6.2 | Edad media vulns explotadas                                | 4        | 4       | 4       | 4       | 4       | 3          | 3         | 3         | 3          | Complementaria a M6.1; algo menos intuitiva para decisores no técnicos.                         |
| M7.1 | % instalaciones parcheadas ≤ plazo objetivo                | 5        | 5       | 5       | 4       | 5       | 3          | 3         | 3         | 3          | Muy accionable; refleja disciplina del ecosistema, no sólo del fabricante.                      |
| M8.1 | Nº vulns notificadas por criticidad                        | 3        | 4       | 3       | 4       | 4       | 4          | 4         | 4         | 4          | Útil para ver volumen y mezcla, aunque sin contexto puede inducir a alarmismo.                 |
| M8.2 | Tiempo medio mitigación (descubrir-parchear-desplegar)    | 5        | 5       | 5       | 4       | 5       | 3          | 3         | 3         | 3          | Captura la cadena completa de respuesta; complejo de medir, pero muy valioso.                   |
| M9.1 | Nº incidentes significativos por sector/año                | 3        | 5       | 4       | 4       | 5       | 3          | 3         | 3         | 4          | Métrica clásica; buena para discurso público, menos para fine-tuning técnico.                   |
| M9.2 | Clasificación de impacto de incidentes                     | 3        | 5       | 4       | 4       | 5       | 3          | 3         | 3         | 4          | Enlaza con prioridades sectoriales; requiere criterios de clasificación consensuados.           |
| M10.1| % incidentes notificados en plazo CRA                      | 3        | 5       | 4       | 4       | 4       | 4          | 4         | 4         | 4          | Indica disciplina proactiva y madurez de reporting.                                             |
| M10.2| % informes de incidente completos y útiles                 | 3        | 4       | 4       | 4       | 4       | 3          | 3         | 3         | 3          | Más subjetiva; valiosa si se define bien qué es “completo y útil”.                              |
| M11.1| MTTD medio                                                 | 4        | 5       | 4       | 4       | 4       | 3          | 3         | 3         | 3          | Indicador conocido; su interpretación depende de contexto (tipo de entorno y monitorización).   |
| M11.2| MTTR medio                                                 | 4        | 5       | 4       | 4       | 4       | 3          | 3         | 3         | 3          | Clave para resiliencia; similar perfil a MTTD.                                                  |
| M12.1| % orgs con ciberseguro                                     | 2        | 4       | 3       | 3       | 3       | 4          | 3         | 4         | 4          | Más socioeconómico que técnico; útil para diálogo con mercado asegurador.                       |
| M12.2| % orgs con certificaciones de seguridad                    | 3        | 4       | 3       | 4       | 4       | 4          | 3         | 4         | 4          | Métrica de madurez general; nivel de detalle depende de disponibilidad de registros.            |
| M13.1| Pérdidas incidentes CRA / PIB                              | 4        | 5       | 3       | 4       | 5       | 2          | 2         | 3         | 2          | Altamente significativa pero difícil de estimar bien; riesgo de grandes márgenes de error.      |
| M13.2| Pérdidas / VAB sectorial                                   | 4        | 5       | 3       | 4       | 5       | 2          | 2         | 3         | 2          | Igual que M13.1, con mayor granularidad sectorial; exige modelos económicos robustos.          |
| M14.1| % presupuesto TIC en ciberseguridad                        | 3        | 4       | 3       | 4       | 4       | 3          | 3         | 4         | 3          | Métrica de esfuerzo; no garantiza efectividad, pero orienta el discurso de suficiencia.        |
| M14.2| % gasto ciber dedicado a CRA                               | 3        | 4       | 3       | 3       | 3       | 2          | 2         | 3         | 2          | Difícil de separar de otros programas; riesgo de contabilidad creativa.                         |
| M15.1| Índice HHI de proveedores críticos                         | 4        | 4       | 4       | 4       | 4       | 3          | 2         | 4         | 3          | Buen indicador estructural; obtención de datos puede ser compleja.                              |
| M15.2| % activos críticos con productos no certificados           | 4        | 5       | 5       | 4       | 5       | 3          | 3         | 3         | 3          | Muy accionable para políticas de sustitución o mitigación; exige inventarios fiables.           |
| M16.1| Nº inspecciones y recursos por inspector                   | 3        | 4       | 4       | 4       | 4       | 4          | 4         | 4         | 4          | Buena métrica de capacidad institucional; relativamente barata de obtener.                      |
| M16.2| Tiempo medio de tramitación de expedientes                 | 3        | 4       | 4       | 4       | 4       | 4          | 4         | 4         | 4          | Refleja eficacia supervisora; accionable para reformas internas.                                |
| M17.1| % hitos CRA-relevantes completados en planes nacionales    | 3        | 5       | 4       | 4       | 4       | 3          | 3         | 3         | 3          | Conecta estrategia con ejecución; depende de claridad en la definición de hitos.                |
| M18.1| Profesionales ciber por 100.000 habitantes                 | 3        | 4       | 3       | 4       | 3       | 3          | 3         | 4         | 4          | Útil para planes de talento; menos directamente ligada a CRA, más a ecosistema global.         |
| M18.2| % vacantes no cubiertas                                    | 3        | 4       | 4       | 4       | 3       | 3          | 3         | 4         | 4          | Sirve para anticipar cuellos de botella; importante para diseño de programas educativos.        |
| M19.1| Índice de satisfacción de autoridades con apoyo ENISA      | 2        | 3       | 2       | 3       | 3       | 3          | 3         | 3         | 4          | Métrica más política que técnica; válida para gobernanza multinivel.                           |
| M20.1| % organizaciones críticas con dashboard CRA                | 3        | 4       | 4       | 4       | 4       | 3          | 3         | 3         | 3          | Indicador de cultura data-driven; el contenido de los dashboards importa tanto o más.          |
```

---

## 3. Uso práctico de la matriz

- Las métricas con puntuaciones altas en **Relevante + Accionable + Significativo** son candidatas a “núcleo duro” del cuadro de mando nacional.  
- Las métricas con alta **Predicción** (P) pueden usarse para modelos de riesgo y para priorizar intervenciones preventivas.  
- Las métricas con baja **Rentabilidad** (Rnt) requieren cautela: quizá merezcan un piloto antes de escalarlas.

La matriz puede exportarse a Excel o a una herramienta de BI para jugar con ponderaciones y escenarios.
