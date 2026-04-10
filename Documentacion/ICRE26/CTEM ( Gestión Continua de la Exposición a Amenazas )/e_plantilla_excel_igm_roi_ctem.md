# Plantilla de Excel para cál- [ ] ParcialmROI CTEM

Este documento describe la estructura lógica que debe implement- [ ] Parcialmja de cálculo (Excel, LibreOffice, Google Sheets) para:

- Calcular un Índice Global de Madurez (IGM) CTEM por organización.
- Estimar un ROI simplifi- [ ] Parcialmama CTEM a partir de datos de exposición e incidentes.

## 1. Hojas recomendadas

Se proponen al menos cinco hojas:

1. `Respuestas`: volcados de respuestas de la encu- [ ] Parcialmización.
2. `Ponderaciones`: asignación de pesos por pregunta y eje de madurez.
3. `IGM_CTEM`: cálculo de puntuaciones por eje y- [ ] Parcialmobal.
4. `ROI_CTEM`: cálculo de indicadores financieros y ROI.
5. `Parametros`: supuestos y constantes (valores medios, costes, etc.).

## 2- [ ] Parcialmstas”

Columnas mínimas:

- `ID_Org`: identificador anónimo de la organiza- [ ] Parcialmr`: sector o tipo de entidad.
- `Tamano`: tamaño (categoría).
- `Pais`: (si aplica).
- Una columna por pregunta, con códigos de respuesta normalizados.

Ejemplo:

- `Q2_1`: valor numérico 0–3 según la respu- [ ] Parcialmunta 2.1.
- `Q4_1`: valor 0–3 según nivel de descubrimiento continuo.
-- [ ] Parcialmficación debe estar documentada (por ejemplo, en la hoja `Ponderaciones`).

## 3. Hoja “Ponderaciones”

Co- [ ] Parcialmas:

- `Pregunta`: referencia (por ejemplo, Q2_1).
- `Descripcion`: texto resumen de la pregunta.
- `Eje_Madurez`: uno de {Gobernanza, Superficie, V- [ ] Parcialmilizacion, Resultad- [ ] Parcialmje`: peso relativo dentro del eje (0–1, que sumen 1 por eje).
- `Max_Punt`: puntuación máxima posible para la preg- [ ] Parcialm o 5).
- `Escala_Normalizada`: factor para llevar la puntuaci- [ ] Parcialmmplo de fila:

| Pregunta | Descripcion                     | Eje_Madurez | Peso_Eje | Max_Punt |- [ ] Parcialmizada |
|----------|---------------------------------|-------------|----------|----------|--------------------|
| Q2_1     | Programa CTEM formal/exist- [ ] Parcialmnza  | 0,10     | 3        | =1/3               |

## 4. Hoja “IGM_CTEM”

### 4.1. Cál- [ ] Parcialmnta

Para cada organización y pregunta:

- `Punt_Normalizada = (Respuesta / Max_Punt) * Peso_Eje`.

Esto puede implementarse con- [ ] Parcialmue combine datos de `Respuestas` y `Ponderaciones` mediante búsqueda (BUSCARV/XLOOKUP).

### 4.2. Cálculo por eje

Para cada organiza- [ ] Parcialm Sumar las puntuaciones normalizadas de las preguntas asignadas a ese eje.
- Opcionalmente normalizar el resul- [ ] Parcialmala 0–5:

`Madurez_Eje = (Suma_Punt_Eje / Suma_Pesos_Ej- [ ] Parcialmte modo, una organización que puntúe al máximo en todas las preguntas de un eje obtendrá un 5 en ese- [ ] Parcialm. Índice Global de Madurez (IGM)

- Definir p- [ ] Parcialms (por ejemplo, todos igual o según importancia relativa).
- `IGM = SUMA( Madurez_Eje_i * Peso_Eje_Global_i )`.

Resultado en escala 0–5 (o 0- [ ] Parcialmtiplica por 20).

## 5. Hoja “ROI_CTEM”

### 5.1. Varia- [ ] Parcialma

Por organiza- [ ] Parcialmdentes_Graves_Antes`: número de incidentes graves (periodo de refere- [ ] Parcialmdentes_Graves_Despues`: número tras implementar CTEM (si aplica).
- `Coste_Medio_Incidente`: estimación de coste total medio- [ ] Parcialm (operativo, reputacional, sanciones,- [ ] Parcialmte_Anual_CTEM`: coste anual del programa CTEM (- [ ] Parcialmpersonal, servicios).
- `Periodo`: número de años considerado.

Opci- [ ] Parcialm`Reduccion_MTTR`: reducción en tiempo medio de recupera- [ ] Parcialm[ ] ParcialmHora_Interrupcion`: coste estimado por hora de interrupción de servicios crítico- [ ] Parcialmálculo de pérdidas evitadas

- `Incidentes_Evitados = Incidente- [ ] Parcialm - Incidentes_Graves_Despues` (si el valor es negativo, tomar 0 para la estima- [ ] Parcialmora).
- `Perdidas_Evitadas = Incidentes_Evitados * Coste_Medio_Incidente`.

Si se quiere incluir la mejora en continuidad:

- `Horas_Evitadas = Reduccion_MTTR * Inci- [ ] Parcialm_- [ ] Parcialmoste_Interrupcion_Evitado = Horas_Evitadas * - [ ] Parcialmerrupcion`.

- `Beneficio_Total_CTEM = Perdidas_Evitadas + Co- [ ] Parcialmon_Evitado`.

### 5.3. Cálculo del ROI

ROI simplificado:

`ROI_CTEM = (Beneficio_Total_CTEM - - [ ] ParcialmEM * Periodo)- [ ] Parcialml_CTEM * Periodo)`

Opcionalmente expresado en porcen- [ ] Parcialm= ROI_CTEM * 100`

### 5.4. Relación con IGM

Se pu- [ ] Parcialmráficos que relacionen:

- IGM vs. número de incidentes gr- [ ] Parcialm. pérdidas evitadas.
- IGM vs. RO- [ ] Parcialmra demostrar causalidad férrea (eso requiere más cienc- [ ] Parcialmel), sino para observar tendencias: organizaciones con mayor madurez CTEM tienden, i- [ ] Parcialmener menos incidentes graves y mej- [ ] Parcialm retorno.

## 6. Hoja “Paramet- [ ] Parcialms globales o por sector:

- Costes medios por incidente (por sector / ta- [ ] Parcialms medios por hora de interrupción.
- Periodos de refere- [ ] Parcialm Pesos por eje de madurez.
- Umbrales de clasificación de IGM (por eje- [ ] Parcialmbajo; 2–3,4 = medio; 3,5–5 = alto).

Esta hoja per- [ ] Parcialml modelo sin reescribir fórmulas, y hacer escenarios (optimista, conservador, et- [ ] Parcialmnsideraciones prácticas

- Docume- [ ] Parcialm supuestas simplificaciones del modelo (por ejemplo, linealidad entre - [ ] Parcialme incidentes evitados).
- Permitir a las organizaciones introducir sus propios paráme- [ ] Parcialmner resultados más ajustados.
- Mantener la plantilla limpia y comentada para facilitar su adopción por equipos no especializados en riesgo c- [ ] ParcialmCon esta estructura, cualquier equipo co- [ ] Parcialmzonable de hojas de cálculo puede implementar la plantilla y empezar a traducir CTEM de un idioma técnico a otro que la direc- [ ] Parcialmuladores entienden con cierta facilidad: el de los números que afectan al neg- [ ] Parcialm

## (f) Plantilla de Reporte Ejecutivo en PowerPoint  

Archivo: `f_plantilla_reporte_ejecutivo_pp- [ ] Parcialm```markdown
# Plantilla de Reporte Ejecutivo CTEM (para PowerPoint)

Esta plantilla describe la estructura recomendada de una presentación ejecutiva s- [ ] Parcialms de la Encuesta CTEM para una organización concreta, un sector o un conjunto de organizaciones.

## Diapositiva 1 – Título

- **Título:** Resultados de la Encuesta CTEM - [ ] Parcialma organización / sector / país]
- **Subtítulo:** Gestión Continua de la Exposición a Amenazas – [Fecha]
- **Contenido adicional:** Logo de la organización o co- [ ] Parcialmsable.

## Diapositiva 2 – Resumen ejecutivo

- 3–5 mensajes clave:
  - Nivel global de madurez (IGM) y posición rela- [ ] Parcialmor o benchmark).
  - Principales fortalezas (ejes con mayor madurez- [ ] Parcialmales áreas de mejora (ejes con menor madurez).
  - Posibles im- [ ] Parcialmra riesgo, resiliencia y cumplimiento.

## Diapositiva 3 – Qué es CTEM y por qué importa

- Breve defini- [ ] Parcialm- [ ] Parcialmes.
- Idea central: de vulnerabilidades sueltas a exposi- [ ] Parcialma y validada.
- En una o dos frases, conectar con el negocio: continuidad, reputación, costes.

## Diapositiva 4 – Metodología de la encuesta

- Tamaño de muestra (n- [ ] Parcialmiones / respuestas).
- Sectores representados.
- Periodo de recogida de datos.
- Notas sobre anonimato y tratamiento de la informa- [ ] Parcialmositiva 5 – Perfil de la organización (o segmento)

- Tipo de entidad, tamaño, alcance geográf- [ ] Parcialmnormativos relevantes (NIS2, DORA, otros).
- Nivel de digitalización / exposición general.

## Diaposi- [ ] Parcialme Global de Madurez (IGM)

- Gráfico de marcador (gauge) o barra mostrando IGM (0–5).
- Co- [ ] Parcialm
  - Media de su sector.
  - Media del total de la muestra.
- Clasificación: Bajo, Medio, Alto, con breve interpretación.

## Diapositivas 7–11 – Detalle por eje de madurez

*- [ ] Parcialmva por eje:**

1. Gobernanza CTEM.
2. Superficie y exposición.
3. Valida- [ ] Parcialmes.
4. Moviliza- [ ] Parcialmción.
5. Resultados y resiliencia.

Para cada eje:

- Puntuación (0–5) y comparación con el bench- [ ] Parcialmllazgos clave.
- Buenas prácticas observadas (si las hay).
- Riesgos asociados si no se mejora.

## Diapositiva 12 – Indicadores CTEM c- [ ] Parcialmo gráfico con:
  - % con descubrimiento continuo.
  - % con SLAs de remediación y nivel de cumplimiento.
  - % que v- [ ] Parcialmbil- [ ] Parcialmciones críticas.
  - % que reportan exposición a dirección.

La idea es mostrar dónde se- [ ] Parcialmnización respecto a estos indicadores.

## Diapositiva 13 – Incidentes, resilie- [ ] Parcialmidad

- Datos de incidentes relevantes (si se proporcionan).
- Tiempo medio de recuperación de servicios críticos.
- Co- [ ] Parcialm la relación (observada o potencial) con la madurez CTEM.

## Diapositiva - [ ] Parcialmva normativa

- Resumen de cómo CTEM ayuda a:
  - NIS2: gestión de riesgos, incident reporting, continuidad.
  - DORA: resiliencia digital, pruebas, terc- [ ] Parcialmr si el nivel actual de madurez facilita o dificulta la conversa- [ ] Parcialmvisores/auditores.

## Diapositiva - [ ] Parcialmn de valor y ROI (si aplic- [ ] Parcialmsenc- [ ] Parcialm:
  - Coste estimado del programa CTEM.
  - Pérdidas evitadas e- [ ] ParcialmROI aproximado (si se ha calculado).
- Nota explícita de que se trata de una estimación ba- [ ] Parcialmtos razonables.

## Diapositiva 16 – Principales obstáculos

- Top 3 obstáculos declarad- [ ] Parcialmd- [ ] Parcialm etc.).
- Comentario sobre cuáles están bajo control interno y cuáles requieren apoyo externo (reguladores, sector, etc.).

## Diapositiva 17 – Recomendaciones prioriz- [ ] Parcialmcomendaciones concretas:
  - “Quick wins” (0–12 meses).
  - Acciones estructurales (1–3 años).
- Vincular cada recomendación a uno o varios ejes de madurez.

## Diapositiva 18 – Próximos pasos

- Propuesta de:
  - Revisión periódica del IGM - [ ] Parcialmanual).
  - Integración de indicadores CTEM en cuadros de mando de dirección.
  - Participación en ejercicios sectoriales/nacionales (si aplica).

## Diapositiva 19 – Anexos (opcional)

-- [ ] Parcialmonal de metodología.
- Definiciones de términos clave.
- Mapas de calor por pregunta (para equipos técnicos).

## Diapositiva 20 – Cierre

- Mensaje final: CTEM como capacidad estratégica, no sólo técnica.
- Person- [ ] Parcialmpara aclaraciones o profundización.

Esta estructura puede adapt- [ ] Parcialmde madurez de la audiencia, pero sirve como esqueleto razonablemente robusto para traducir los resultados de la encu- [ ] Parcialmato que un comité ejecutivo pueda entender sin necesida- [ ] Parcialmun diccionario de acrónimos a la sala.