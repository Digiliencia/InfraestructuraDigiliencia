# Plantilla Excel – IGM y ROI (GQM + PRAGMATIC)

Esta plantilla amplía la anterior incorporando referencias a objetivos GQM y evaluaciones PRAGMATIC.[web:46][web:40][web:44][web:47]

## Hoja 1: `Respuestas`

- A: ID Pregunta / Métrica  
- B: Función CSF  
- C: Objetivo GQM asociado (texto breve)  
- D: Valor de madurez (0–4)  
- E: Valor de la métrica (numérico, %, tiempo, etc.)

Cada fila representa una métrica o pregunta del cuestionario.

## Hoja 2: `Madurez_CSFFunciones`

- A: Función CSF (GV, ID, PR, DE, RS, RC, SC, ME)  
- B: Descripción  
- C: Madurez media

Ejemplo en C2:

```excel
=PROMEDIO.SI(Respuestas!$B:$B;"GV";Respuestas!$D:$D)
```

Repetir por función.

## Hoja 3: `IGM`

- C2–C9: madurez por función (referencias a hoja anterior).  
- C11: IGM global:

```excel
=PROMEDIO(C2:C9)
```

- C12: Nivel cualitativo (ejemplo):

```excel
=SI(C11<1;"Nivel 1 - Inicial / ad hoc";
 SI(C11<2;"Nivel 2 - Básico / fragmentado";
 SI(C11<3;"Nivel 3 - Definido / en despliegue";
 SI(C11<3,5;"Nivel 4 - Gestionado / repetible";
 "Nivel 5 - Optimizado / integrado"))))
```

## Hoja 4: `PRAGMATIC`

Columnas:

- A: Métrica  
- B: Función CSF  
- C: P (Predictivo)  
- D: R (Relevante)  
- E: A (Accionable)  
- F: G (Genuino)  
- G: M (Significativo)  
- H: A2 (Preciso)  
- I: T (Oportuno)  
- J: I2 (Independiente)  
- K: C (Rentable)  
- L: Puntuación media PRAGMATIC

En L2:

```excel
=PROMEDIO(C2:K2)
```

Aplicar formato condicional para resaltar métricas con media alta (>4) o baja (<3).

## Hoja 5: `ROI_Ciberseguridad`

Igual que en la plantilla anterior:

- Entradas: costes, nº incidentes antes/después, MTTD/MTTR antes y después, valor hora de indisponibilidad.  
- Cálculos: reducción de incidentes, ahorro por reducción de indisponibilidad, beneficios totales, ROI.

## Hoja 6: `Dashboard`

- Gráficos de barras/radar para madurez por función CSF.  
- Tarjetas con IGM y nivel cualitativo.  
- Gráficos de barras con puntuaciones PRAGMATIC por métrica.  
- Indicadores de ROI y principales beneficios estimados.