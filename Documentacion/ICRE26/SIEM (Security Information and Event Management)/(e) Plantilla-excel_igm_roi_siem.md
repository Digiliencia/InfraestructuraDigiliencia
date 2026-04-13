# Plantilla de Excel para Cálculo de IGM y ROI a partir de la Encuesta SIEM

> Esta plantilla está descrita en texto Markdown para facilitar su implementación en Excel, LibreOffice o herramientas similares.

---

## 1. Estructura general del libro

Se recomienda crear un libro con las siguientes hojas:

1. `Datos_Encuesta` – Volcado estructurado de respuestas.
2. `IGM_Calculos` – Cálculo de índices de madurez.
3. `ROI_Calculos` – Estimación de ROI de SIEM/SOC.
4. `Resultados` – Cuadros de mando resumidos para uso ejecutivo.

---

## 2. Hoja `Datos_Encuesta`

Cada fila representa una organización encuestada. Cada columna corresponde a un campo relevante de la encuesta.

Ejemplo de columnas (no exhaustivo):

- `ID_Org` – Identificador anónimo.
- `Sector` – Según pregunta 1.1.
- `Tamano` – Rango de empleados (1.3).
- `Modelo_SOC` – Codificación de 1.5.
- `Sujeta_NIS2` – Valor de 4.1.
- `Cobertura_Activos_Criticos` – Rango de 2.4 (convertido a valor numérico medio del rango).
- `Madurez_Normalizacion_Datos` – Media de sub‑preguntas de 2.5.
- `Cobertura_MITRE` – Rango de 3.3.2 (valor numérico medio del rango).
- `Medicion_MTTD` – Codificación de 3.1.1 (por ejemplo, 1 = no, 2 = ad‑hoc, 3 = formal).
- `Objetivo_MTTD_Minutos` – Valor numérico estimado según 3.1.3.
- `Medicion_MTTR` – Codificación de 3.1.4.
- `Tasa_Falsos_Positivos` – Estimación basada en 3.2.1 y 3.2.2.
- `Carga_Por_Analista` – Si está disponible.
- `Madurez_Cumplimiento` – Derivada de 4.2–4.5.
- `Uso_IA` – Codificación de 5.1.
- `Uso_SOAR` – Codificación de 5.3.
- `Incidentes_Automatizados` – Codificación de 5.4.
- `Madurez_OT` – Derivada de 6.1–6.2.
- `Madurez_Riesgo` – Derivada de 7.1–7.3.
- `IGM_Autoevaluado` – 5.5.
- Otras variables que se consideren útiles.

---

## 3. Hoja `IGM_Calculos`

### 3.1 Definición de subíndices

Sugerencia de columnas de cálculo (por organización):

- `IGM_Arquitectura`:
  - Fórmula: media de `Cobertura_Activos_Criticos`, `Madurez_Normalizacion_Datos`, `Cobertura_MITRE` (escalados a 0–5).
- `IGM_Operacion`:
  - Considerar: existencia y formalidad de MTTD/MTTR, objetivos definidos, tasas de falsos positivos y conversión alerta‑incidente.
  - Ejemplo: asignar un valor 0–5 según una combinación ponderada.
- `IGM_Cumplimiento`:
  - Basado en `Sujeta_NIS2`, `Madurez_Cumplimiento`, uso de SIEM en notificación.
- `IGM_IA_SOAR`:
  - Basado en `Uso_IA`, `Uso_SOAR`, `Incidentes_Automatizados`.
- `IGM_OT`:
  - Basado en `Madurez_OT`.
- `IGM_Riesgo`:
  - Basado en `Madurez_Riesgo` y usos del SIEM para ROI.

### 3.2 Cálculo del IGM global

Definir pesos (celdas configurables):

- `Peso_Arquitectura`
- `Peso_Operacion`
- `Peso_Cumplimiento`
- `Peso_IA_SOAR`
- `Peso_OT`
- `Peso_Riesgo`

Ejemplo de fórmula en Excel para la fila 2:

```text
IGM_Global = (IGM_Arquitectura*Peso_Arquitectura +
              IGM_Operacion*Peso_Operacion +
              IGM_Cumplimiento*Peso_Cumplimiento +
              IGM_IA_SOAR*Peso_IA_SOAR +
              IGM_OT*Peso_OT +
              IGM_Riesgo*Peso_Riesgo) /
             (Peso_Arquitectura+Peso_Operacion+Peso_Cumplimiento+
              Peso_IA_SOAR+Peso_OT+Peso_Riesgo)
```

Se recomienda normalizar el resultado a escala 0–100 multiplicando por 20 si los subíndices están en 0–5.

---

## 4. Hoja `ROI_Calculos`

### 4.1 Entradas de coste

Por organización:

- `Coste_SIEM_Licencias_Anual`
- `Coste_SIEM_Infraestructura_Anual`
- `Coste_SOC_Personal_Anual`
- `Coste_Otras_Herramientas_Relacionadas` (EDR, SOAR, etc.)
- `Coste_Formacion_y_Consultoria`

Calcular:

- `Coste_Total_Anual` = suma de todos los costes anteriores.

### 4.2 Entradas de beneficio

Variables a estimar (idealmente con apoyo interno):

- `Num_Incidentes_Graves_Anual_Antes` – referencia histórica.
- `Num_Incidentes_Graves_Anual_Actual` – situación actual.
- `Coste_Promedio_Incidente_Grave` – estimado (incluyendo impacto de negocio).
- `Reduccion_MTTD_Minutos`
- `Reduccion_MTTR_Minutos`
- `Valor_Hora_Interrupcion_Servicio` – valoración económica.

Ejemplos de cálculos:

- `Incidentes_Evitados` = `Num_Incidentes_Graves_Anual_Antes` – `Num_Incidentes_Graves_Anual_Actual`.  
- `Perdidas_Evitadas_Por_Incidentes` = `Incidentes_Evitados` * `Coste_Promedio_Incidente_Grave`.  
- `Ahorro_Tiempo_Deteccion` = `Reduccion_MTTD_Minutos` * `Num_Incidentes_Graves_Anual_Actual`.  
- `Ahorro_Tiempo_Respuesta` = `Reduccion_MTTR_Minutos` * `Num_Incidentes_Graves_Anual_Actual`.  
- `Valor_Ahorro_Tiempo_Total` = (`Ahorro_Tiempo_Deteccion` + `Ahorro_Tiempo_Respuesta`) * (`Valor_Hora_Interrupcion_Servicio` / 60).

Total beneficios:

- `Beneficio_Total_Anual` = `Perdidas_Evitadas_Por_Incidentes` + `Valor_Ahorro_Tiempo_Total`.

### 4.3 Cálculo del ROI

Fórmulas típicas:

- `ROI_Anual` = (`Beneficio_Total_Anual` – `Coste_Total_Anual`) / `Coste_Total_Anual`.  
- `Periodo_Retorno` (años) = `Coste_Total_Anual` / `Beneficio_Total_Anual` (si los beneficios son constantes).  
- `Coste_Por_Incidente_Evitado` = `Coste_Total_Anual` / `Incidentes_Evitados` (si >0).

---

## 5. Hoja `Resultados`

Esta hoja puede contener:

- Tabla resumen con medias de `IGM_Global` por sector y tamaño.  
- Gráficos de barras comparando subíndices.  
- Semáforos (verde/ámbar/rojo) para IGM y ROI.  
- Espacios para comentarios cualitativos.

Ejemplos de indicadores:

- `IGM_Global_Promedio_Sector_Energia`.  
- `Porcentaje_Organizaciones_Con_IGM_Global>70`.  
- `Porcentaje_Organizaciones_Con_ROI_Anual_Positivo`.

---

## 6. Notas prácticas

- Mantener la plantilla flexible: permitir ajustar pesos, costes y supuestos sin cambiar estructuras.
- Documentar todas las fórmulas en una hoja de “Metodología” dentro del propio Excel.
- Evitar interpretaciones excesivamente precisas: el ROI en ciberseguridad es una estimación, no una verdad revelada.

---

_Fin de la plantilla descriptiva._