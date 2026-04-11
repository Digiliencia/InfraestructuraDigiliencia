# README – Kit de indicadores nacionales BCM / ciber‑resiliencia (GQM + PRAGMATIC)

Este README describe el contenido y el uso del **kit de indicadores nacionales** basado en el informe “Business Continuity Management (BCM) for Effective Cyber Risk Management” y en la metodología combinada **GQM + PRAGMATIC**.

La idea es sencilla: que el país (o territorio) pueda responder, con datos y no sólo con discursos, a preguntas del tipo «¿qué tan resilientes somos realmente ante ciberincidentes graves y fallos TIC?».

---

## 1. Contenidos del kit

El kit se compone de los siguientes ficheros Markdown:

1. `marco-gqm-prag.md`  
   - Define el **marco conceptual GQM + PRAGMATIC** aplicado a los indicadores nacionales IND‑01…IND‑14.
   - Incluye objetivos nacionales (G1–G3), preguntas GQM y definición de cada métrica.

2. `matriz-prag.md`  
   - Presenta la **Matriz de Evaluación PRAGMATIC Completa**: para cada indicador se valora su carácter predictivo, relevancia, accionabilidad, etc.

3. `mapeo-bcm-norm.md`  
   - Relaciona cada indicador con los principales **marcos normativos**: ENCS, PNC, ENS, NIS2, DORA, normas ISO, GCI, NCSI.

4. `plantilla-igm2.md`  
   - Describe cómo construir una **plantilla Excel** para:
     - Calcular un Índice Global de Madurez/Resiliencia (IGM).
     - Calcular índices por dimensión (gobernanza, capacidades, rendimiento, impacto, ecosistema).
     - Asociar programas nacionales a ROI e impacto en indicadores.

5. `ppt-bcm.md`  
   - Propone una **estructura de reporte ejecutivo** (PowerPoint u otra herramienta) para presentar resultados a altos decisores.

---

## 2. Cómo usar el kit (paso a paso)

### Paso 1. Aprobación del enfoque

- Compartir `marco-gqm-prag.md` con:
  - Equipos de estrategia, ciberseguridad nacional, continuidad de gobierno y analítica.
- Validar:
  - Objetivos nacionales (G1–G3).
  - Lista de indicadores IND‑01…IND‑14.
  - Definiciones GQM (preguntas, métricas).

> Consejo: este es el momento de ajustar el catálogo; cambiar indicadores a posteriori complica series históricas.

### Paso 2. Alineamiento normativo y político

- Revisar `mapeo-bcm-norm.md` con:
  - Unidades jurídicas/regulatorias.
  - Responsables del ENS, transposición NIS2, DORA, etc.
- Identificar:
  - Indicadores más sensibles por implicaciones de cumplimiento.
  - Posibles huecos entre lo medido y lo que las normas exigen observar.

### Paso 3. Diseño del modelo de datos y cálculo

- Utilizar `plantilla-igm2.md` para construir el libro Excel (u otra herramienta analítica):
  - `Catalogo_Indicadores` con pesos por dimensión y global.
  - `Datos_Anuales` con los valores brutos por año/ámbito.
  - `Calculos_Indices` para normalizar y producir IGM + índices por dimensión.
  - `ROI_Programas` para conectar políticas con resultados.
- Definir:
  - Responsables de aportar cada dato.
  - Frecuencia de actualización (anual, semestral…).
  - Reglas de normalización y gestión de datos faltantes.

### Paso 4. Evaluación PRAGMATIC

- Revisar `matriz-prag.md` para:
  - Entender fortalezas y debilidades de cada indicador.
  - Ajustar definiciones donde Preciso, Independiente o Rentable tengan valor bajo.
- Decidir si se mantienen todas las métricas o si alguna pasa a ser experimental.

### Paso 5. Recogida inicial de datos

- Lanzar una **primera iteración piloto** con unos pocos indicadores (por ejemplo, IND‑01, 02, 03, 05, 06, 08, 12, 14).
- Probar el flujo:
  - Obtención de datos.
  - Carga en Excel.
  - Cálculo de índices.
- Ajustar antes de escalar al catálogo completo.

### Paso 6. Elaboración del reporte ejecutivo

- Basarse en `ppt-bcm.md` para crear la presentación a:
  - Consejo de Ministros / órganos de coordinación de ciberseguridad.
  - Reguladores sectoriales, CCAA, etc.
- Asegurarse de que el reporte:
  - Explica la **metodología** con claridad (sin abrumar). 
  - Expone resultados clave y brechas.  
  - Propone un conjunto manejable de **iniciativas prioritarias**.

### Paso 7. Ciclo de mejora

- Establecer un ciclo anual (o bianual) de:
  - Actualización de datos.
  - Revisión de indicadores y metodología.
  - Ajuste de programas y prioridades.

---

## 3. Interacción con la encuesta organizacional

Este kit de indicadores nacionales está pensado para convivir con el **kit de encuesta organizacional** (orientado a empresas/administraciones individuales):

- El **IGM nacional** puede verse como una «media ponderada» de la madurez de muchos actores.
- La **encuesta organizacional** ayuda a explicar por qué ciertos indicadores nacionales están altos, bajos o estancados.

Combinados, ambos kits permiten un enfoque **top‑down** (indicadores país) y **bottom‑up** (madurez de organizaciones), con una narrativa coherente.

---

## 4. Gobernanza recomendada del sistema de indicadores

Roles sugeridos:

- **Autoridad coordinadora nacional** (p.ej. futuro Centro Nacional de Ciberseguridad):
  - Dueño del catálogo IND‑xx.
  - Responsable de `Catalogo_Indicadores` y `Calculos_Indices`.
- **Proveedores de datos**:
  - CERTs nacionales (INCIBE‑CERT, CCN‑CERT, ESDF‑CERT…).
  - Reguladores sectoriales (CNMV, BdE, CNMC, sanidad, energía…).
  - Ministerios y agencias implicadas en PNC y ENCS.
- **Analistas y modelizadores**:
  - Equipo encargado de mantenimiento de Excel / herramienta analítica.
  - Responsables de análisis de tendencias y escenarios.

---

## 5. Buenas prácticas y advertencias

- **No enamorarse de las métricas**: si un indicador resulta sistemáticamente poco útil o engañoso, se revisa o se jubila.
- **Documentar cambios**: cada modificación en definiciones o pesos afecta a la comparabilidad histórica; conviene dejar rastro.
- **Ser honestos con la incertidumbre**: especialmente en métricas como IND‑10 (impacto económico % PIB), explicitar márgenes y supuestos.
- **Evitar el «dashboard teatro»**: que los gráficos no sean decorado, sino el punto de partida de conversaciones difíciles pero necesarias.

---

## 6. Cierre

Este kit pretende ofrecer algo más que un conjunto de números: un **lenguaje compartido** para hablar de ciber‑resiliencia nacional de forma rigurosa, transparente y orientada a la acción.

Con un poco de disciplina, algo de sentido del humor y ganas de mejorar, puede convertirse en una de esas infraestructuras invisibles que, sin hacer ruido, marcan la diferencia cuando llegan los días complicados.
