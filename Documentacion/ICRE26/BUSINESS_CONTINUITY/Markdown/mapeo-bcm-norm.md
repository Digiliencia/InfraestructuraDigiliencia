# Mapeo normativo detallado de indicadores nacionales BCM / ciber‑resiliencia

Este documento relaciona cada indicador nacional (IND‑xx) con los principales marcos normativos y de referencia: Estrategia Nacional de Ciberseguridad (ENCS), Plan Nacional de Ciberseguridad (PNC), Esquema Nacional de Seguridad (ENS), NIS2, DORA, normas ISO relevantes (27001, 22301, 27005, 27036), y grandes índices internacionales (GCI, NCSI).

No pretende ser un análisis jurídico exhaustivo, sino una **brújula de alineamiento**.

---

## 1. Convenciones

- `Marco_Principal`: marco o norma con relación más directa al indicador.
- `Otros_Marcos`: referencias adicionales de interés.
- `Tipo`: carácter del requisito en la mayoría de casos de uso:
  - `OBLIGATORIO`: deriva de exigencias legales/regulatorias para ciertos sujetos (por ejemplo, OSE bajo NIS2, AAPP bajo ENS, entidades financieras bajo DORA).
  - `PROGRAMÁTICO`: deriva de estrategias y planes (ENCS, PNC), de obligado cumplimiento para la Administración, pero con margen de implementación.
  - `BUENA_PRACTICA`: alineado con recomendaciones de normas ISO u organismos internacionales.

---

## 2. Tabla de mapeo por indicador

| Código | Indicador | Marco_Principal | Otros_Marcos | Tipo | Comentario de alineamiento |
|---|---|---|---|---|---|
| IND-01 | Estrategia Nacional de Ciberseguridad vigente (S/N) | ENCS 2019 | Estrategia de Seguridad Nacional, GCI | PROGRAMÁTICO | Refleja la existencia de una estrategia país, requisito clave en GCI y en la arquitectura española de seguridad nacional. |
| IND-02 | % de medidas del PNC ejecutadas o en curso | PNC, ENCS | Estrategia de Seguridad Nacional | PROGRAMÁTICO | Mide el grado de implementación real de la estrategia; directamente vinculado al cumplimiento interno de los compromisos del PNC. |
| IND-03 | Posición y puntuación en GCI y NCSI | GCI (ITU), NCSI | ENCS, PNC | BUENA_PRACTICA | Indica alineamiento global con marcos de referencia; no es exigencia legal, pero sí señal reputacional y de benchmarking internacional. |
| IND-04 | Nº de CERT/CSIRT nacionales con mandato operativo | ENCS, normativa de ciberseguridad nacional | NIS/NIS2, GCI | PROGRAMÁTICO / BUENA_PRACTICA | La existencia de CERTs/CSIRTs nacionales está prevista en ENCS y reflejada en GCI; NIS2 exige CSIRTs nacionales eficaces. |
| IND-05 | % de OSE con BCP/BCM ISO 22301 probado anual | NIS2 (transposición nacional) | ISO 22301, ISO 27001/27031, DORA (sector financiero) | OBLIGATORIO / BUENA_PRACTICA | Relacionado con requisitos de gestión de riesgos y continuidad para OSE e «entidades importantes» bajo NIS2 y DORA, y buenas prácticas ISO 22301. |
| IND-06 | % sistemas públicos críticos con controles ENS de continuidad implantados | ENS 2022 (RD 311/2022) | ENCS 2019, ISO 22301 | OBLIGATORIO / BUENA_PRACTICA | Directamente vinculado a los principios y medidas ENS sobre continuidad y disponibilidad de servicios públicos. |
| IND-07 | Incidentes significativos por 100.000 hab. y sector | NIS2 (reporting incidentes) | ENCS, ENS, GCI, NCSI | OBLIGATORIO / PROGRAMÁTICO | Conecta con obligaciones de notificación de incidentes (NIS2, ENS) y con el seguimiento estratégico de ENCS. |
| IND-08 | MTTR nacional de servicios esenciales tras incidentes TIC | NIS2, DORA | ISO 22301, ISO 27031, ENCS | OBLIGATORIO / BUENA_PRACTICA | Aunque la métrica concreta no esté siempre explicitada, el espíritu de NIS2 y DORA exige capacidad de recuperación rápida de servicios esenciales. |
| IND-09 | % de incidentes críticos que activan BCP | NIS2, ENS | ISO 22301 | OBLIGATORIO / BUENA_PRACTICA | Relacionado con requisitos de planes de continuidad y gestión de incidentes; mide uso práctico de BCP exigidos por ENS y NIS2. |
| IND-10 | Pérdidas económicas anuales por ciberincidentes (% PIB) | ENCS, PNC | Estrategias económicas nacionales, estudios OCDE/UE | PROGRAMÁTICO / BUENA_PRACTICA | Indicador macroeconómico alineado con el seguimiento estratégico del impacto de la ciberinseguridad; sin obligación legal específica, pero muy recomendado. |
| IND-11 | Días/año en modo degradado de servicios clave por incidentes TIC | ENS, NIS2 | ISO 22301, ISO 27031 | OBLIGATORIO / BUENA_PRACTICA | Conecta con obligación de garantizar continuidad del servicio público y de servicios esenciales; operacionaliza la disponibilidad esperada. |
| IND-12 | Nº ejercicios nacionales de cibercrisis/continuidad y % participación | ENCS, PNC | NIS2, DORA, GCI | PROGRAMÁTICO / BUENA_PRACTICA | ENCS y PNC prevén ejercicios nacionales; NIS2 y DORA animan a pruebas periódicas. Importante también para buena clasificación en GCI. |
| IND-13 | Personas formadas en ciberseguridad/continuidad por 100.000 hab. | ENCS, PNC | ENS, GCI, ISO 27001 (concienciación) | PROGRAMÁTICO / BUENA_PRACTICA | Alineado con objetivos de cultura de ciberseguridad y formación de ENCS y ENS; también pilar de desarrollo de capacidades en GCI. |
| IND-14 | % org. públicas/OSE con al menos un ejercicio BCP anual con escenarios ciber | ENS, NIS2, DORA | ISO 22301 | OBLIGATORIO / BUENA_PRACTICA | Toca de lleno las obligaciones de prueba de planes de continuidad bajo ENS, NIS2 y DORA y las buenas prácticas ISO 22301. |

---

## 3. Uso práctico del mapeo

- Permite identificar **qué indicadores son más sensibles desde el punto de vista regulatorio** (por ejemplo, IND‑05, IND‑06, IND‑07, IND‑08, IND‑09, IND‑11, IND‑14) y deberían estar en el radar permanente de reguladores y supervisores.
- Ayuda a conectar resultados de indicadores con **narrativa normativa** en informes y presentaciones (por ejemplo, «esta brecha en IND‑06 implica riesgo de incumplimiento ENS en X sistemas críticos»).
- Sirve como base para diseñar **cuadros de mando regulatorios** que integren cumplimiento y resiliencia, evitando tener un tablero para cada sigla (ENS, NIS2, DORA, ISO…).

Si en el futuro se ajustan ENS, se despliegan plenamente NIS2 y DORA, o se actualiza la ENCS, este mapeo deberá revisarse y versionarse explícitamente para mantener su valor.
