# Plantilla de Excel para IGM y ROI SASE basada en GQM + PRAGMATIC

> Especificación técnica para implementar en Excel (u hoja similar) el Índice Global de Madurez (IGM) y el cálculo de ROI SASE, utilizando las métricas definidas en el marco GQM y priorizadas mediante PRAGMATIC.

---

## 1. Hojas recomendadas

1. **`Respuestas`** – Datos brutos de encuestas / auditorías.  
2. **`Metrics`** – Transformación de respuestas en valores Mx,y (0–4, 0–100, etc.).  
3. **`IGM`** – Cálculo del índice por dimensión y global.  
4. **`ROI`** – Modelo económico de costes/beneficios y ROI.  
5. **`Parametros`** – Ponderaciones, factores económicos y configuraciones.

---

## 2. Hoja `Respuestas`

Cada fila representa una organización o unidad (ministerio, consejería, empresa). Columnas mínimas:

- `ID_Org`  
- `Sector`  
- `Tamano`  
- `ENS_Nivel` (Bajo/Medio/Alto, si aplica)  
- `NIS2_Sujeta` (Sí/No)  
- Campos que codifican respuestas a preguntas relacionadas con métricas (por ejemplo, `A_MFA_Cobertura`, `A_ZTNA_Cobertura`, etc.) con valores discretos (1–4).

Ejemplo de codificación para coberturas:

- 1 → 0–25 %  
- 2 → 26–50 %  
- 3 → 51–75 %  
- 4 → 76–100 %

---

## 3. Hoja `Parametros`

### 3.1. Ponderaciones por dimensión del IGM

| Dimensión                         | Código | Peso sugerido |
|----------------------------------|--------|---------------|
| Rendimiento & QoE               | D1     | 0,15          |
| Zero Trust & Identidad          | D2     | 0,20          |
| SOC & Detección/Respuesta       | D3     | 0,15          |
| Cumplimiento ENS/NIS2 & Gobierno| D4     | 0,20          |
| Continuidad & Resiliencia       | D5     | 0,15          |
| Negocio & ROI                   | D6     | 0,15          |

Ajustable según contexto (por ejemplo, reforzar D4 para AAPP ENS).

### 3.2. Mapeo métricas → dimensiones

- D1 (Rendimiento & QoE): M1.1, M1.2, M1.4, M1.5, M1.6  
- D2 (Zero Trust): M2.1, M2.2, M2.3, M2.4  
- D3 (SOC): M3.1, M3.2, M3.3, M3.4, M3.5  
- D4 (Cumplimiento): M4.1, M4.2, M4.3, M4.4  
- D5 (Continuidad): M5.1, M5.2, M5.3, M5.4  
- D6 (Negocio/ROI): M6.1, M6.2, M6.3, M6.4, M6.5

### 3.3. Parámetros económicos para ROI

- `Coste_Licencias_SASE`  
- `Coste_Proyecto_Implantacion`  
- `Coste_Operacion_Anual`  
- `Coste_Licencias_Heredadas` (pre-SASE)  
- `Coste_Enlaces_Heredados`  
- `CosteIncidenteMayor`  
- `Incidentes_Anuales_Pre`  
- `ReduccionIncidentes_%`  
- `Horas_Operativas_Ahorradas`  
- `Coste_Hora_Tecnico`  
- `Horas_Prod_Ahorradas_Usu`  
- `Coste_Hora_Usuario`

Valores por defecto ajustables.

---

## 4. Hoja `Metrics`

Transforma las respuestas codificadas en valores de métrica normalizados (por ejemplo, 0–100).

Ejemplos:

- **M2.1 (% usuarios sensibles con MFA)**  
  - Si `Respuestas!A_MFA_Cobertura` ∈ {1..4}, entonces:  
    `= (Respuestas!A_MFA_Cobertura - 1) / 3 * 100`

- **M1.1 (latencia p95 hacia apps críticas)**  
  - Tomado de telemetría (ms); puede reescalarse a un índice inverso (cuanto menor, mejor):  
    `Indice_Latencia = MAX(0; MIN(100; 100 - (Latencia_p95 - Umbral_Bueno) * Factor))`

- **M5.4 (indisponibilidad anual SASE)**  
  - Convertir horas de indisponibilidad a un índice donde 0 = mala, 100 = excelente.

Se recomienda documentar en esta hoja, columna al lado de cada métrica, la fórmula usada y la fuente de datos.

---

## 5. Hoja `IGM`

Para cada organización (fila), y cada dimensión:

1. **Media de métricas de la dimensión**  
   Ejemplo D2 (Zero Trust) para fila 2:  
   `=PROMEDIO(Metrics!M2_1_Org2 : Metrics!M2_4_Org2)`

2. **Puntuación de dimensión (0–100)**  
   Si las métricas ya están normalizadas 0–100, la media ya está en ese rango.

3. **IGM total**  
   Supongamos:

   - `IGM_D1` en columna C  
   - `IGM_D2` en columna D  
   - ...  
   - Pesos en `Parametros!Peso_D1` … `Peso_D6`

   Fórmula:

   ```text
   IGM_Total = C2*Peso_D1 + D2*Peso_D2 + E2*Peso_D3 + F2*Peso_D4 + G2*Peso_D5 + H2*Peso_D6
   ```

El resultado es un valor 0–100 que sirve para comparar organizaciones, sectores o evolución temporal.

---

## 6. Hoja `ROI`

### 6.1. Bloque de costes (anuales)

- C1 = `Coste_Licencias_SASE`  
- C2 = `Coste_Proyecto_Implantacion` / años de amortización  
- C3 = `Coste_Operacion_Anual`  
- `Costes_Totales` = SUMA(C1:C3)

### 6.2. Bloque de beneficios (anuales)

- B1 = `Coste_Licencias_Heredadas` (ahorradas)  
- B2 = `Coste_Enlaces_Heredados` (si procede)  
- B3 = `Incidentes_Anuales_Pre * ReduccionIncidentes_% * CosteIncidenteMayor`  
- B4 = `Horas_Operativas_Ahorradas * Coste_Hora_Tecnico`  
- B5 = `Horas_Prod_Ahorradas_Usu * Coste_Hora_Usuario`  
- `Beneficios_Totales` = SUMA(B1:B5)

### 6.3. ROI

- `ROI% = ((Beneficios_Totales - Costes_Totales) / Costes_Totales) * 100`

Opcionalmente, usar tres escenarios (pesimista/base/optimista) con diferentes valores de reducción de incidentes y horas ahorradas, para mostrar rangos de ROI.

---

## 7. Relación entre IGM y ROI

Se recomienda incluir una tabla o gráfico que represente:

- Eje X: IGM_Total  
- Eje Y: ROI%  

y analizar si mayores niveles de madurez SASE (IGM) se correlacionan con mejores retornos económicos y menor riesgo. Esto permite argumentar que no se trata solo de “cumplir ENS/NIS2”, sino de gestionar bien inversiones.

---

## 8. Notas prácticas

- Documentar claramente las fuentes de datos (telemetría SASE, encuestas, sistemas financieros).  
- Versionar la hoja cuando cambien fórmulas o ponderaciones.  
- Realizar revisiones anuales de parámetros y ajustar según nuevas realidades de ENS, NIS2 o el propio servicio SASE.
(f) plantilla-reporte-ejecutivo-gqm-pragmatic.md
text
# Plantilla de Reporte Ejecutivo SASE basado en GQM + PRAGMATIC

> Estructura sugerida para una presentación ejecutiva (tipo PowerPoint) que comunique resultados de indicadores SASE, IGM y ROI alineados con GQM y filtrados por PRAGMATIC.

---

## Diapositiva 1 – Portada

- Título: **“Madurez SASE/Zero Trust y Valor para el Negocio en [Organización/Sector]”**  
- Subtítulo: “Resultados GQM + PRAGMATIC – [Año]”  
- Ponente, fecha, logos relevantes.

---

## Diapositiva 2 – Contexto y motivación

- Breve descripción de por qué SASE y Zero Trust son prioritarios (cloud, trabajo híbrido, ENS, NIS2).  
- Objetivos del ejercicio:  
  - Alinear métricas con objetivos nacionales y corporativos.  
  - Medir madurez SASE y su impacto.  
  - Identificar prioridades de mejora.

---

## Diapositiva 3 – Metodología GQM + PRAGMATIC

- Esquema simple (tres niveles): Objetivos → Preguntas → Métricas.  
- Una diapositiva visual con los nueve criterios PRAGMATIC.  
- Mensaje clave: “No medimos por amor a Excel, sino para tomar decisiones”.

---

## Diapositiva 4 – Objetivos de alto nivel

- Listado de 3–5 objetivos:  
  - Garantizar continuidad de servicios esenciales.  
  - Reducir riesgo de incidentes en acceso remoto/cloud.  
  - Mejorar experiencia de usuario segura.  
  - Cumplir ENS/NIS2 de forma eficiente.  
  - Optimizar gastos mediante consolidación.

---

## Diapositiva 5 – Vista global del IGM

- Gráfico radar con las dimensiones:  
  - Rendimiento & QoE  
  - Zero Trust & Identidad  
  - SOC & Detección/Respuesta  
  - Cumplimiento ENS/NIS2 & Gobierno  
  - Continuidad & Resiliencia  
  - Negocio & ROI

- Mensaje: dónde se concentran fortalezas y debilidades.

---

## Diapositiva 6 – Métricas clave seleccionadas (PRAGMATIC top)

- Tabla sencilla con 8–12 métricas “estrella”:  
  - Nombre de la métrica.  
  - Relación G (objetivo).  
  - Breve comentario.  

- Nota: se han priorizado por su alta puntuación PRAGMATIC.

---

## Diapositiva 7 – Rendimiento & QoE

- Gráficos:  
  - Latencia p95 vs. umbrales objetivo para apps críticas.  
  - Tiempo de transacción medio en servicios clave.

- Mensajes:  
  - ¿Dónde estamos respecto a umbrales “aceptables”?  
  - Impacto percibido en usuarios.

---

## Diapositiva 8 – Zero Trust & Identidad

- Gráfico de barras: % MFA, % apps críticas vía ZTNA, % accesos privilegiados bajo control ZT.  
- Comentario:  
  - Brecha entre discurso Zero Trust y realidad.  
  - Riesgos asociados a áreas con baja cobertura.

---

## Diapositiva 9 – SOC, detección y respuesta

- Tabla/gráfico: MTTD, MTTC, MTTR vs. objetivos.  
- Volumen y tipos de incidentes/amenazas.  
- Mensaje:  
  - ¿La telemetría SASE está bien explotada?  
  - ¿Dónde se atasca el flujo de respuesta?

---

## Diapositiva 10 – Cumplimiento ENS/NIS2

- % proyectos cloud integrados en SASE.  
- % sistemas ENS medio/alto canalizados vía SASE/ZTNA.  
- Grado de mapeo formal SASE–ENS/NIS2.  
- Mensaje:  
  - Desde el “cumplir en el papel” al “cumplir en la red”.

---

## Diapositiva 11 – Continuidad & Resiliencia

- Inclusión de SASE en planes de continuidad.  
- Tiempo de conmutación PoP/enlace.  
- Indisponibilidad anual atribuible a SASE.  
- Mensaje:  
  - ¿SASE ayuda a que todo falle de forma digna?  
  - ¿Se prueba la arquitectura en situaciones simuladas?

---

## Diapositiva 12 – Negocio & ROI

- Costes totales vs. beneficios totales anuales.  
- ROI estimado (con banda de escenarios).  
- Ejemplos de ahorro y coste evitado.  
- Mensaje:  
  - SASE como inversión en resiliencia y eficiencia, no solo como gasto obligado.

---

## Diapositiva 13 – Priorización (Matriz impacto–esfuerzo)

- Ejes: impacto en objetivo / esfuerzo de implantación.  
- Posicionar iniciativas:  
  - Migrar VPN → ZTNA.  
  - Integrar totalmente telemetría SASE en SIEM.  
  - Definir SLOs de QoE.  
  - Alinear formalmente SASE–ENS/NIS2.

---

## Diapositiva 14 – Recomendaciones y próximos pasos

- Top 5 acciones recomendadas.  
- Plazos sugeridos (corto/medio/largo).  
- Responsables.

---

## Diapositiva 15 – Cierre

- Síntesis: 1–2 mensajes clave (por ejemplo, “mejora visible en QoE, pero tareas pendientes en Zero Trust y mapeo ENS/NIS2”).  
- Propuesta de cadencia para repetir la medición (anual, bienal).  
- Invitación al debate con el comité de dirección.

---

## Notas de estilo

- Evitar exceso de métricas en cada slide; mejor pocas, seleccionadas por su calidad PRAGMATIC.  
- Añadir en notas del ponente la traza GQM de cada métrica (objetivo–pregunta–métrica) para uso interno.  
- Usar colores y códigos visuales consistentes para indicar “en verde / en ámbar / en rojo”.