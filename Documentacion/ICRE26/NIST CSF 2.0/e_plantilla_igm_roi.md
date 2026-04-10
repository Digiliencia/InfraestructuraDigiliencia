# Plantilla para Excel – Cálculo de IGM y ROI de Ciberseguridad

La siguiente descripción permite construir un libro de Excel con varias hojas para calcular:

1. Índice Global de Madurez (IGM).  
2. Índices de madurez por función CSF.  
3. Estimaciones básicas de ROI de ciberseguridad.

---

## Hoja 1: `Respuestas`

Columnas sugeridas:

- A: ID Pregunta (p.ej., P-GV-01, P-ID-03, etc.)  
- B: Función CSF (GV, ID, PR, DE, RS, RC, SC, ME)  
- C: Descripción abreviada  
- D: Valor de madurez (0–4)  

Cada fila corresponde a una pregunta cerrada de la encuesta. El valor de la columna D se introduce manualmente o mediante listas desplegables.

---

## Hoja 2: `Madurez_CSFFunciones`

Objetivo: calcular la madurez media por función.

Columnas:

- A: Función CSF (GV, ID, PR, DE, RS, RC, SC, ME)  
- B: Descripción (Gobernanza, Identificar, Proteger, Detectar, etc.)  
- C: Madurez media (fórmula)  

Ejemplo de fórmula para C2 (función = GV):

```excel
=PROMEDIO.SI(Respuestas!$B:$B;"GV";Respuestas!$D:$D)
```

Repetir para el resto de funciones cambiando el criterio (“ID”, “PR”, etc.).

---

## Hoja 3: `IGM`

En esta hoja se resume el IGM y se asigna un nivel cualitativo.

Campos recomendados:

- C2: GV_madurez (referencia a Madurez_CSFFunciones!C2)  
- C3: ID_madurez  
- C4: PR_madurez  
- C5: DE_madurez  
- C6: RS_madurez  
- C7: RC_madurez  
- C8: SC_madurez  
- C9: ME_madurez  

En C11: IGM global:

```excel
=PROMEDIO(C2:C9)
```

En C12: Nivel cualitativo (usando BUSCARV o SI anidados), por ejemplo:

```excel
=SI(C11<1;"Nivel 1 - Inicial / ad hoc";
 SI(C11<2;"Nivel 2 - Básico / fragmentado";
 SI(C11<3;"Nivel 3 - Definido / en despliegue";
 SI(C11<3,5;"Nivel 4 - Gestionado / repetible";
 "Nivel 5 - Optimizado / integrado"))))
```

También se pueden insertar gráficos de radar o barras para visualizar las funciones CSF.

---

## Hoja 4: `ROI_Ciberseguridad`

### 4.1. Entradas de datos

Campos sugeridos:

- C2: Costes anuales de ciberseguridad (OPEX + CAPEX)  
- C3: Costes iniciales de proyectos de mejora (CAPEX proyectos clave)  
- C4: Número de incidentes graves “antes” (periodo de referencia)  
- C5: Número de incidentes graves “después” (periodo actual)  
- C6: Coste medio estimado por incidente grave  
- C7: MTTD antes (en horas)  
- C8: MTTD después (en horas)  
- C9: MTTR antes (en horas)  
- C10: MTTR después (en horas)  
- C11: Valor estimado por hora de indisponibilidad (impacto monetario)  

### 4.2. Cálculos intermedios

En C13: Reducción de incidentes:

```excel
=MAX(C4-C5;0)
```

En C14: Beneficio por reducción de incidentes:

```excel
=C13*C6
```

En C15: Reducción de MTTD (horas):

```excel
=MAX(C7-C8;0)
```

En C16: Reducción de MTTR (horas):

```excel
=MAX(C9-C10;0)
```

En C17: Ahorro por reducción de indisponibilidad:

```excel
=(C15+C16)*C11
```

En C18: Otros beneficios monetizables (campo manual, opcional).

En C19: Beneficio total estimado:

```excel
=C14+C17+C18
```

### 4.3. Cálculo del ROI

En C21: Coste total de ciberseguridad en el periodo:

```excel
=C2+C3
```

En C22: ROI:

```excel
=SI(C21=0;"";(C19-C21)/C21)
```

Formatear C22 como porcentaje.  

Opcional: añadir campo C23 con texto interpretativo:

```excel
=SI(C22="";"N/D";
 SI(C22<0;"ROI negativo (costes > beneficios estimados)";
 SI(C22<0,2;"ROI moderado";
 SI(C22<0,5;"ROI positivo";
 "ROI muy positivo"))))
```

---

## Hoja 5: `Dashboard`

Construir un tablero visual con:

- Gráficos de barras para madurez por función CSF.  
- Indicador del IGM global y su nivel.  
- Tarjetas con ROI, reducción de incidentes, reducción de tiempos MTTD/MTTR.  

De este modo se facilita la reutilización directa para cuadros de mando ejecutivos y presentaciones.