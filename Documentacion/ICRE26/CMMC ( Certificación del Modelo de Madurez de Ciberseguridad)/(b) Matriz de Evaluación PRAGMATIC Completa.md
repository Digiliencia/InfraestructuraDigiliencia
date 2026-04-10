# Matriz de Evaluación PRAGMATIC Completa para Métricas CMMC / NIS2 / ENS

> Versión: 1.0  
> Nota: Puntuaciones 0–5 basadas en juicio experto; ajustar según contexto sectorial.

---

## 1. Leyenda de puntuaciones

- 0 = Nulo / No cumple.  
- 1 = Muy bajo.  
- 2 = Bajo.  
- 3 = Aceptable.  
- 4 = Bueno.  
- 5 = Excelente.

---

## 2. Matriz principal

### 2.1. Métricas de control de acceso y MFA

| Métrica | Descripción | P | R | A | G | M | A(c) | T | I | C | Total | Comentario |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| %_Cuentas_criticas_MFA | Porcentaje de cuentas con acceso a sistemas críticos que usan MFA robusta | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 4 | 39 | Métrica central para ataques de credenciales; muy útil para gobernanza. |
| %_Accesos_remotos_MFA | Porcentaje de accesos remotos a sistemas críticos protegidos con MFA | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 38 | Gran impacto en riesgo; datos pueden requerir cierto esfuerzo de agregación. |
| Nº_excepciones_MFA | Número de cuentas críticas sin MFA por excepción aprobada | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 33 | Muy útil para auditoría y reducción progresiva de excepciones. |

---

### 2.2. Métricas de vulnerabilidades y parcheo

| Métrica | Descripción | P | R | A | G | M | A(c) | T | I | C | Total | Comentario |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MTTP_critico | Tiempo medio de parcheo de vulnerabilidades críticas en sistemas expuestos | 4 | 5 | 5 | 4 | 4 | 4 | 3 | 3 | 3 | 35 | Fuertemente correlacionado con probabilidad de explotación. |
| %_Sistemas_cumplen_SLA_parcheo_critico | Porcentaje de sistemas que cumplen el plazo objetivo de parcheo | 4 | 5 | 5 | 4 | 4 | 4 | 3 | 3 | 3 | 35 | Métrica muy adecuada para cuadros de mando y acuerdos de nivel de servicio internos. |
| Media_vuln_criticas_por_activo | Número medio de vulnerabilidades críticas abiertas por activo crítico | 3 | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 3 | 31 | Útil, pero puede ser más sensible a errores de inventario. |

---

### 2.3. Métricas de monitorización y respuesta (MTTD / MTTR)

| Métrica | Descripción | P | R | A | G | M | A(c) | T | I | C | Total | Comentario |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MTTD_incidentes_significativos | Tiempo medio de detección de incidentes significativos | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 3 | 3 | 35 | Métrica estrella para SOC, aunque requiere definición clara de “incidente significativo”. |
| MTTR_incidentes_significativos | Tiempo medio de recuperación/contención | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 3 | 3 | 35 | Directamente relacionada con impacto de negocio. |
| %_Incidentes_con_postmortem | Porcentaje de incidentes con análisis y plan de acción | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 34 | Impulsa la mejora continua, relativamente barata de medir. |

---

### 2.4. Métricas de clasificación y cifrado de información sensible

| Métrica | Descripción | P | R | A | G | M | A(c) | T | I | C | Total | Comentario |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| %_Activos_datos_clasificados | Porcentaje de activos de datos sensibles formalmente clasificados | 4 | 5 | 4 | 4 | 4 | 3 | 3 | 3 | 3 | 33 | Requiere un esfuerzo inicial de clasificación; excelente para madurez estratégica. |
| %_Datos_sensibles_cifrados_en_reposo | Porcentaje de datos sensibles cifrados en reposo | 4 | 5 | 5 | 4 | 4 | 4 | 3 | 3 | 3 | 35 | Métrica clave para cumplimiento ENS/RGPD/NIS2. |
| %_Canales_sensibles_cifrados_en_transito | Porcentaje de canales que transportan datos sensibles con cifrado robusto | 4 | 5 | 5 | 4 | 4 | 4 | 3 | 3 | 3 | 35 | Muy útil para auditorías técnicas y revisiones de arquitectura. |

---

### 2.5. Métricas de proveedores y cadena de suministro

| Métrica | Descripción | P | R | A | G | M | A(c) | T | I | C | Total | Comentario |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| %_Proveedores_criticos_identificados | Porcentaje de proveedores críticos formalmente identificados | 3 | 5 | 4 | 4 | 4 | 3 | 3 | 3 | 3 | 32 | Condición necesaria para todo lo demás; muy alineada con NIS2/DORA. |
| %_Contratos_criticos_con_clausulas_seguridad_robustas | Porcentaje de contratos críticos con requisitos de seguridad verificables | 4 | 5 | 5 | 4 | 4 | 4 | 3 | 4 | 3 | 36 | Fuerte impacto en gobernanza de terceros; indicador muy valioso. |
| %_Proveedores_criticos_evaluados_anualmente | Porcentaje de proveedores críticos evaluados con métricas | 4 | 5 | 5 | 4 | 4 | 3 | 3 | 3 | 3 | 34 | Refuerza la supervisión continua de la cadena de suministro. |

---

### 2.6. Métricas de formación, cultura y comportamiento

| Métrica | Descripción | P | R | A | G | M | A(c) | T | I | C | Total | Comentario |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| %_Plantilla_formacion_anual | Porcentaje de plantilla con formación anual en ciberseguridad | 3 | 5 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 34 | Métrica casi obligatoria, fácil de obtener. |
| Tasa_clicks_phishing | Porcentaje de usuarios que caen en simulaciones de phishing | 4 | 5 | 5 | 4 | 4 | 3 | 3 | 3 | 3 | 34 | Muy accionable, pero requiere cuidado en la gestión cultural. |
| Nº_reportes_voluntarios_por_100_empleados | Reportes voluntarios de incidentes por cada 100 empleados | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 3 | 33 | Buen indicador de cultura de reporte, no tan trivial de medir de forma homogénea. |

---

### 2.7. Métricas de documentación y evidencias

| Métrica | Descripción | P | R | A | G | M | A(c) | T | I | C | Total | Comentario |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Estado_SSP (0–4) | Nivel de existencia/actualización del SSP | 3 | 5 | 4 | 4 | 4 | 3 | 3 | 3 | 3 | 32 | Sintética y muy usada en CMMC; algo subjetiva si no se define bien la escala. |
| %_Controles_con_evidencias_actualizadas | Porcentaje de controles con evidencias vigentes | 4 | 5 | 5 | 4 | 4 | 4 | 3 | 3 | 3 | 35 | Indicador potente de calidad de cumplimiento. |
| %_Acciones_POAM_completadas_en_plazo | Porcentaje de acciones de mejora completadas en plazo | 4 | 5 | 5 | 4 | 4 | 4 | 3 | 3 | 3 | 35 | Conecta claramente con la mejora continua. |

---

## 3. Selección de métricas “estrella”

Se pueden considerar como métricas prioritarias aquellas con **≥ 34 puntos**, por ejemplo:

- `%_Cuentas_criticas_MFA`  
- `%_Accesos_remotos_MFA`  
- `MTTP_critico`  
- `MTTD_incidentes_significativos`  
- `MTTR_incidentes_significativos`  
- `%_Datos_sensibles_cifrados_en_reposo`  
- `%_Canales_sensibles_cifrados_en_transito`  
- `%_Contratos_criticos_con_clausulas_seguridad_robustas`  
- `%_Plantilla_formacion_anual`  
- `Tasa_clicks_phishing`  
- `%_Controles_con_evidencias_actualizadas`  
- `%_Acciones_POAM_completadas_en_plazo`

Estas son las mejores candidatas para figurar en cuadros de mando ejecutivos y en informes nacionales sectoriales.

---

_Fin de la Matriz de Evaluación PRAGMATIC._