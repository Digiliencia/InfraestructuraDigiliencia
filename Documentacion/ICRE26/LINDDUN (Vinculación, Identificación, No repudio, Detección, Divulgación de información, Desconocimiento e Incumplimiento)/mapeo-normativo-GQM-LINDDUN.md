# 🗺️ MAPEO NORMATIVO GQM+PRAGMATIC
## Trazabilidad de Métricas → Requisitos Regulatorios
### RGPD · AI Act · NIS2 · ENS · LIINE4DU · ISO/IEC · NIST
#### Kit GQM + PRAGMATIC · España 2025–2026 · Versión 1.0

---

> *"Una métrica sin ancla normativa es una opinión. Una norma sin métrica asociada es una promesa. La combinación de ambas es la única forma de demostrar cumplimiento efectivo ante un regulador que cada vez pregunta más por evidencias y menos por documentos."*

---

## INSTRUCCIONES DE USO

Esta tabla proporciona la trazabilidad completa entre:
- Cada **métrica GQM** del catálogo (columna 1)
- El **indicador LINDDUN/LIINE4DU** al que pertenece (columna 2)
- El **objetivo GQM** del que deriva (columna 3)
- La **normativa primaria** que obliga a medir este aspecto (columnas 4–8)
- La **norma técnica de referencia** para la implementación (columna 9)
- El **nivel de riesgo** si la métrica supera su umbral negativo (columna 10)

**Leyenda de riesgo regulatorio:**
- 🔴 **Crítico**: Incumplimiento con sanción directa o sanción máxima aplicable
- 🟠 **Alto**: Incumplimiento con alta probabilidad de sanción o actuación de la AEPD
- 🟡 **Medio**: Incumplimiento que incrementa la exposición pero sin consecuencia inmediata directa
- 🟢 **Bajo**: Métrica de buenas prácticas sin consecuencia sancionatoria directa

---

## TABLA MAESTRA DE TRAZABILIDAD NORMATIVA

| Métrica | Indicador | Objetivo GQM | RGPD | AI Act | NIS2 | ENS | LIINE4DU | ISO/NIST | Riesgo |
|---------|-----------|-------------|------|--------|------|-----|----------|----------|--------|
| **L-M1** % DFDs actualizados | L – Linking | OBJ-L: Cartografiar flujos de datos con riesgo de vinculación | **Art. 30** (Registro de actividades); Art. 25 (PbD) | Annex IV (documentación técnica para IA de alto riesgo) | Art. 21.2 NIS2 (gestión activos) | ENS op.pl.1 (Análisis de riesgos) | L – Linking | ISO 27701 §7.2.1 | 🟠 Alto |
| **L-M2** Quasi-identificadores no controlados | L – Linking | OBJ-L: Evaluar riesgo de re-identificación por datos indirectos | Art. 4.5 (seudonimización); Art. 25.1 (minimización); Art. 32.1.a | — | — | ENS mp.si.2 (Criptografía) | L – Linking; I – Identifying | ISO 29101; ISO 20889 | 🟠 Alto |
| **L-M3** ICAV (Índice Controles Anti-Vinculación) | L – Linking | OBJ-L: Verificar efectividad de controles técnicos anti-linking | Art. 25 (PbD/PbDf); Art. 32.1.a (seudonimización y cifrado) | Art. 9.2 AI Act (robustez y ciberseguridad) | Art. 21.2 NIS2 (medidas de seguridad) | ENS mp.si.2; op.exp.1 | L – Linking | ISO 27001 A.8.11; ISO 29101 | 🟠 Alto |
| **L-M4** TTDL (tiempo detección vinculación) | L – Linking | OBJ-L: Medir capacidad de detección de vinculación no autorizada | **Arts. 33–34** (brechas; límite 72h); Art. 32 (seguridad) | — | **Art. 23 NIS2** (notificación incidentes; 24h alerta) | ENS op.exp.7 (Gestión incidentes) | L – Linking; Data Breach | ISO 27035; NIST SP 800-61 | 🔴 Crítico |
| **L-M5** % modelos ML con EIPD de linking | L – Linking | OBJ-L: Garantizar evaluación de linking en sistemas ML/IA | **Art. 35** (EIPD obligatoria); Art. 36 (consulta previa) | **Arts. 9, 10 AI Act** (gestión de riesgos; calidad de datos) | — | — | L – Linking; NC – Non-compliance | ISO 29134 (EIPD); ISO 42001 §6.1 | 🔴 Crítico |
| **I-M1** K-anonimato de datasets publicados | I – Identifying | OBJ-I: Verificar que datos publicados no permiten re-identificación | Art. 4.1 (datos personales); Art. 5.1.e; Art. 89 (investigación) | — | — | — | I – Identifying | ISO 20889; GT29 WP216 (Dictamen 05/2014 sobre anonimización) | 🔴 Crítico |
| **I-M2** Datasets con análisis re-identificación | I – Identifying | OBJ-I: Documentar proceso de análisis antes de cada publicación | Art. 25 (PbD); Art. 32 (evaluación de riesgos) | Art. 10.3 AI Act (datos de entrenamiento anonimizados) | — | — | I – Identifying | ISO 29134; ENISA Pseudonymisation Guidelines 2019 | 🟠 Alto |
| **I-M3** FAR — False Acceptance Rate biométrica | I – Identifying | OBJ-I: Controlar la tasa de error en identificación biométrica | **Art. 9 RGPD** (categorías especiales); **Art. 35** (EIPD obligatoria); Art. 22 LOPDGDD | **Art. 5.1.e AI Act** (prohibición reconocimiento facial en espacio público en tiempo real) | — | ENS (datos de categoría alta) | I – Identifying; D – Detecting | ISO/IEC 19795 (biometría); ISO 27701 §7.2.3 | 🔴 Crítico |
| **I-M4** % sistemas biométricos con EIPD válida | I – Identifying | OBJ-I: Cumplir obligación de EIPD para tratamientos biométricos | **Art. 9 + Art. 35 RGPD**; Art. 22 LOPDGDD; Listado AEPD de tratamientos que requieren EIPD | **Arts. 5.1.e, 6 AI Act** | — | — | I – Identifying; NC – Non-compliance | ISO 29134; ISO 27701 §7.2.8 | 🔴 **Máximo**: caso AENA 2025 (10,04 M€) |
| **I-M5** Epsilon (ε) privacidad diferencial | I – Identifying | OBJ-I: Cuantificar riesgo de re-identificación en modelos ML | Art. 32 (seguridad técnica adecuada); Art. 35 (EIPD para tecnologías innovadoras) | **Art. 9.2 AI Act** (robustez y ciberseguridad de sistemas IA) | — | — | I – Identifying | NIST SP 800-188; Dwork & Roth (2014) | 🟠 Alto |
| **NR-M1** Completitud de logs de acceso | NR – Non-repudiation | OBJ-NR: Garantizar trazabilidad completa de accesos a datos | Art. 5.2 (responsabilidad proactiva); Art. 32 (seguridad) | — | **Art. 21.2 NIS2** (trazabilidad como medida de seguridad) | **ENS op.exp.8** (Registro de actividades del operador); op.exp.10 | NR – Non-repudiation | ISO 27001 A.8.15; ISO 27701 §8.4.2 | 🟠 Alto |
| **NR-M2** Desviación retención logs vs. política | NR – Non-repudiation | OBJ-NR: Asegurar que la retención de logs respeta principio de limitación del plazo | **Art. 5.1.e RGPD** (limitación del plazo de conservación); Art. 30 | — | Art. 21.2 NIS2 | ENS op.exp.8; op.exp.10 | NR – Non-repudiation | ISO 27001 A.8.15 | 🟠 Alto |
| **NR-M3** % supresiones IA en ≤ 30 días | NR – Non-repudiation | OBJ-NR: Garantizar ejercicio efectivo del derecho de supresión en sistemas IA | **Art. 17 RGPD** (derecho al olvido); Art. 12.3 (plazo 30 días); Art. 19 | **Art. 13 AI Act** (transparencia); Art. 52 (sistemas de IA de relación con usuarios) | — | — | NR – Non-repudiation; U – Unawareness | ISO 27701 §7.3.4 | 🔴 Crítico |
| **NR-M4** TMRS — Tiempo Medio Respuesta Supresión | NR – Non-repudiation | OBJ-NR: Medir eficiencia del proceso de atención de derechos de supresión | **Art. 12.3 RGPD** (plazo legal 30 días); Art. 17 (supresión); LOPDGDD Art. 12 | — | — | — | NR – Non-repudiation; U – Unawareness | ISO 27701 §7.3.4 | 🔴 Crítico |
| **NR-M5** % consentimientos con firma eIDAS | NR – Non-repudiation | OBJ-NR: Verificar no repudio de consentimientos con firma digital válida | **Art. 7 RGPD** (consentimiento documentado); eIDAS2 Reg. 2024/1183 | — | — | ENS mp.si.3 (Firma electrónica) | NR – Non-repudiation | ETSI EN 319 series; ISO 27001 A.5.36 | 🟡 Medio |
| **D-M1** IPV — Índice Proporcionalidad Videovigilancia | D – Detecting | OBJ-D: Verificar proporcionalidad y conformidad de sistemas CCTV | Arts. 5.1.b, 5.1.c (limitación del propósito; minimización); Art. 13 | Art. 5.1.d AI Act (prohibición vigilancia masiva en tiempo real con IA) | — | — | D – Detecting | ISO 27701 §7.2.3 | 🔴 Crítico |
| **D-M1** (cont.) | D – Detecting | — | **Art. 22 LOPDGDD** (videovigilancia); Instrucción AEPD 1/2006 | — | — | — | D – Detecting | — | 🔴 Crítico |
| **D-M2** % cámaras con EIPD válida | D – Detecting | OBJ-D: Garantizar evaluación de impacto para cada sistema CCTV | **Art. 35 RGPD** (EIPD para "observación sistemática de una zona de acceso público a gran escala") | — | — | — | D – Detecting; NC – Non-compliance | ISO 29134 | 🔴 Crítico |
| **D-M3** Inventario IoT con evaluación privacidad | D – Detecting | OBJ-D: Controlar el riesgo de detección no autorizada por IoT | Art. 25 (PbD); Art. 32 (seguridad adecuada para IoT) | Arts. 6, 9 AI Act (IA integrada en dispositivos) | **Art. 21.2 NIS2** (seguridad de dispositivos conectados) | ENS (infraestructuras críticas) | D – Detecting; L – Linking | ETSI EN 303 645 (ciberseg. IoT); ISO 27001 A.8.1 | 🟠 Alto |
| **D-M4** Vulnerabilidades side-channel sin remediar | D – Detecting | OBJ-D: Identificar y remediar vulnerabilidades de canal lateral en IoT | Art. 32 (medidas técnicas adecuadas); Art. 32.1.d (planes de contingencia) | Art. 9.2 AI Act (robustez frente a ataques) | **Art. 21.2.e NIS2** (gestión de vulnerabilidades) | ENS mp.si.2 | D – Detecting | NIST SP 800-90B; ISO 27001 A.8.16 | 🟠 Alto |
| **D-M5** % empleados informados de monitorización | D – Detecting | OBJ-D: Cumplir obligación de información previa en monitorización laboral | **Art. 87 LOPDGDD** (derecho a la intimidad en relaciones laborales); Arts. 13–14 RGPD | — | — | — | D – Detecting; U – Unawareness | ISO 27701 §7.3.2 | 🔴 Crítico |
| **DD-M1** % encargados con DPA vigente | DD – Data Disclosure | OBJ-DD: Garantizar que todos los encargados cuentan con contrato Art. 28 | **Art. 28 RGPD** (contratos con encargados); Art. 29 (instrucciones); Art. 82 (responsabilidad solidaria) | Art. 28 AI Act (obligaciones del operador de IA) | **Art. 21.2 NIS2** (cadena de suministro) | ENS (subcontratación) | DD – Data Disclosure | ISO 27701 §6.12; ISO 27001 A.5.19–5.22 | 🔴 Crítico |
| **DD-M2** % transferencias internacionales con garantía | DD – Data Disclosure | OBJ-DD: Verificar base legal para todas las transferencias a terceros países | **Arts. 44–49 RGPD** (transferencias internacionales); SCC UE (2021); DPF UE-EE.UU. (2023) | Art. 10 AI Act (datos de entrenamiento transfronterizos) | Art. 21.5 NIS2 | — | DD – Data Disclosure | ISO 27701 §8.5 | 🔴 **Máximo**: caso TikTok 530 M€ (2025) |
| **DD-M3** % prompts IA con datos personales | DD – Data Disclosure | OBJ-DD: Controlar divulgación de datos en herramientas IA generativa | Art. 5.1.c (minimización); Art. 5.1.b (limitación del propósito); Art. 32 | **Arts. 10, 13, 53 AI Act** (GPAI: transparencia y protección de datos) | — | — | DD – Data Disclosure | ISO 42001 §8.3; EDPB Report LLMs 2025 | 🔴 Crítico |
| **DD-M4** % herramientas IA gen. con EIPD | DD – Data Disclosure | OBJ-DD: Garantizar evaluación de impacto previa al despliegue de IA generativa | **Art. 35 RGPD** (EIPD para tratamientos con nuevas tecnologías); Art. 36 | **Arts. 10, 27 AI Act** (FRIA: Fundamental Rights Impact Assessment) | — | — | DD – Data Disclosure; NC – Non-compliance | ISO 29134; ISO 42001 §6.1.2 | 🔴 Crítico |
| **DD-M5** IMD — Índice Minimización de Datos | DD – Data Disclosure | OBJ-DD: Medir implementación efectiva del principio de minimización | **Art. 5.1.c RGPD** (minimización); **Art. 25.2** (privacidad por defecto) | Art. 10.3 AI Act (minimización en datos de entrenamiento) | — | — | DD – Data Disclosure | ISO 27701 §7.4.1; ISO 29101 §8.3 | 🟠 Alto |
| **U-M1** ILPP — Legibilidad política privacidad | U – Unawareness | OBJ-U: Verificar que la información al interesado es comprensible | **Art. 12.1 RGPD** ("lenguaje claro y sencillo"); Arts. 13–14 (contenido informativo) | **Art. 13 AI Act** (transparencia a usuarios de IA de alto riesgo) | — | — | U – Unawareness | ISO 27701 §7.3.2; GT29 WP260 | 🔴 Crítico |
| **U-M2** % ARCO+ atendidos en plazo | U – Unawareness | OBJ-U: Garantizar la atención de derechos en los plazos legales | **Art. 12.3 RGPD** (plazo 30 días); Arts. 15–22 (catálogo de derechos); LOPDGDD Arts. 12–18 | — | — | — | U – Unawareness | ISO 27701 §7.3.4 | 🔴 Crítico |
| **U-M3** % consentimientos válidos (4 requisitos) | U – Unawareness | OBJ-U: Auditar la validez jurídica de los consentimientos recabados | **Arts. 6, 7 RGPD** (base jurídica y condiciones del consentimiento); Cdo. 32; GT29 WP259 | Art. 13 AI Act (información previa antes de uso de IA) | — | — | U – Unawareness | ISO 27701 §7.2.3; IAB TCF v2.2 | 🔴 **Máximo**: consentimiento inválido = base jurídica inexistente |
| **U-M4** % decisiones automatizadas con explicación | U – Unawareness | OBJ-U: Garantizar el derecho a explicación en decisiones automatizadas | **Art. 22 RGPD** (decisiones automatizadas y perfilado); Cdo. 71; GT29 WP251 | **Arts. 13, 14, 86 AI Act** (derecho a explicación en IA de alto riesgo) | — | — | U – Unawareness; L – Linking | ISO 27701 §7.3.5 | 🔴 Crítico |
| **U-M5** % empleados formados en privacidad | U – Unawareness | OBJ-U: Medir cobertura de formación en privacidad de personal con acceso a datos | Art. 39.1.b (función del DPO: concienciación); Art. 32.4 (formación como medida de seguridad) | **Art. 4.2 AI Act** (alfabetización en IA para todo el personal) | **Art. 20 NIS2** (formación obligatoria de órganos de dirección) | ENS mp.per.2 | U – Unawareness | ISO 27001 A.6.3; ISO 27701 §5.3 | 🟠 Alto |
| **NC-M1** IMC — Índice Madurez Cumplimiento | NC – Non-compliance | OBJ-NC: Evaluar la solidez del sistema de gestión de cumplimiento | **Art. 24 RGPD** (responsabilidad proactiva); Art. 5.2 (accountability) | Arts. 9, 17 AI Act (sistemas de gestión de riesgos) | Art. 21 NIS2 (obligaciones de seguridad) | ENS op.pl.1 | NC – Non-compliance | ISO 27701 §5.2.1; ISO 27001 §6.1.2 | 🟠 Alto |
| **NC-M2** % tratamientos alto riesgo con EIPD | NC – Non-compliance | OBJ-NC: Asegurar cobertura completa de EIPDs obligatorias | **Art. 35 RGPD** (EIPD obligatoria para alto riesgo); Listado AEPD; GT29 WP248 | **Art. 27 AI Act** (FRIA para sistemas de IA de alto riesgo) | — | — | NC – Non-compliance | ISO 29134 (EIPD) | 🔴 **Máximo**: caso AENA 10,04 M€ |
| **NC-M3** Tasa brechas notificadas ≤ 72h | NC – Non-compliance | OBJ-NC: Medir cumplimiento del plazo legal de notificación de brechas | **Art. 33 RGPD** (notificación a AEPD en 72h); Art. 34 (comunicación a interesados); GT29 WP250 | — | **Art. 23 NIS2** (24h alerta; 72h notificación; 1 mes informe final) | ENS op.exp.7 | Data Breach – LIINE4DU | ISO 27001 A.5.24–5.28; ISO 27035 | 🔴 **Máximo**: incumplimiento plazo = infracción directa |
| **NC-M4** TMNB — Tiempo Medio Notificación Brecha | NC – Non-compliance | OBJ-NC: Medir eficiencia operativa de respuesta a brechas | **Art. 33 RGPD** (plazo 72 horas contadas desde conocimiento); Art. 34 | — | **Art. 23 NIS2** | ENS op.exp.7 | Data Breach – LIINE4DU | ISO 27035; NIST SP 800-61 | 🔴 Crítico |
| **NC-M5** IPAA — Índice Preparación AI Act | NC – Non-compliance | OBJ-NC: Evaluar nivel de preparación para obligaciones AI Act 2025–2027 | Art. 24 (responsabilidad proactiva) | **Arts. 5, 6, 9, 10, 13, 17, 22, 27 AI Act**; calendario de implementación 2024–2027 | — | — | NC – Non-compliance | ISO 42001 (SGAI); NIST AI RMF 1.0 | 🔴 **Máximo**: hasta 35 M€ o 7% facturación global |
| **IN-M1** Tasa registros con verificación exactitud | IN – Inaccuracy | OBJ-IN: Evaluar la implementación del principio de exactitud | **Art. 5.1.d RGPD** (exactitud); Art. 16 (rectificación); Art. 5.1.f (integridad) | **Art. 10 AI Act** (calidad y exactitud de datos de entrenamiento) | — | — | Inaccuracy – LIINE4DU | ISO 8000 (calidad del dato); ISO 27701 §7.4.1 | 🟠 Alto |
| **IN-M2** TMRR — Tiempo Medio Resolución Rectificación | IN – Inaccuracy | OBJ-IN: Medir eficiencia del proceso de rectificación de datos inexactos | **Art. 16 RGPD** (derecho a rectificación); Art. 12.3 (plazo 30 días) | — | — | — | Inaccuracy – LIINE4DU; U – Unawareness | ISO 27701 §7.3.4 | 🔴 Crítico |
| **IN-M3** DIR — Disparate Impact Ratio | IN – Inaccuracy | OBJ-IN: Detectar y cuantificar el sesgo discriminatorio en modelos IA | Art. 22 RGPD (perfilado discriminatorio); Cdo. 71 | **Arts. 9, 10, 15 AI Act** (exactitud, robustez, no discriminación en IA de alto riesgo) | — | — | Inaccuracy – LIINE4DU | ISO 42001 §9.1; IEEE 7003 (transparencia algorítmica) | 🔴 Crítico |
| **IN-M4** % modelos IA alto riesgo con auditoría sesgo | IN – Inaccuracy | OBJ-IN: Garantizar cobertura de auditorías de equidad algorítmica | Art. 22 RGPD (obligación de salvaguardas ante perfilado) | **Arts. 9, 10, 43 AI Act** (evaluación de conformidad; auditoría de terceros para sistemas de alto riesgo) | — | — | Inaccuracy – LIINE4DU; NC – Non-compliance | ISO 42001 §9.1; NIST AI RMF (GOVERN 1.7) | 🔴 Crítico |
| **EX-M1** Conformidad WCAG 2.1 AA | EX – Exclusion | OBJ-EX: Eliminar barreras de acceso a derechos para personas con diversidad funcional | Art. 12.1 RGPD (comunicación accesible); Art. 5.1.a (transparencia universal) | Art. 14 AI Act (supervisión humana accesible) | — | ENS (accesibilidad de servicios digitales) | Exclusion – LIINE4DU | ISO 9241-171; WCAG 2.1 AA; RD 1112/2018 | 🟠 Alto |
| **EX-M2** Formatos accesibles disponibles | EX – Exclusion | OBJ-EX: Garantizar acceso a información de privacidad en múltiples formatos | Art. 12 RGPD (información "concisa, transparente, inteligible"); LOPDGDD | — | — | — | Exclusion – LIINE4DU | ISO 9241-171; Ley 11/2023 (brecha digital) | 🟡 Medio |
| **EX-M3** Canales no digitales para ejercicio derechos | EX – Exclusion | OBJ-EX: Asegurar que el ejercicio de derechos no requiere competencia digital | Art. 12 RGPD (no puede exigirse canal exclusivamente digital); Art. 15–22 (derechos accesibles para todos) | — | — | — | Exclusion – LIINE4DU | ISO 27701 §7.3.4 | 🟡 Medio |

---

## TABLA DE CONCENTRACIÓN DE RIESGO — TOP 10 MÉTRICAS POR SANCIÓN POTENCIAL

| Rango | Métrica | Normativa Principal | Sanción Máxima | Caso Referencia |
|-------|---------|--------------------|--------------:|-----------------|
| 1 | NC-M5 (IPAA) | AI Act Arts. 5, 9, 17 | **35 M€ o 7% facturación** | — (vigente desde 2025) |
| 2 | IN-M3 (DIR) + IN-M4 | AI Act Art. 10 + RGPD Art. 22 | **35 M€ o 7% facturación** | — (acumulación de infracciones) |
| 3 | U-M3 (consentimiento) | RGPD Arts. 6 + 7 | **20 M€ o 4% facturación** | Meta 1.200 M€ (2023) |
| 4 | DD-M2 (transf. intern.) | RGPD Arts. 44–49 | **20 M€ o 4% facturación** | TikTok 530 M€ (2025) |
| 5 | I-M4 (EIPD biométrica) | RGPD Art. 9 + Art. 35 | **20 M€ o 4% facturación** | AENA 10,04 M€ (2025) |
| 6 | NC-M2 (EIPDs alto riesgo) | RGPD Art. 35 | **20 M€ o 4% facturación** | AENA 10,04 M€ (2025) |
| 7 | U-M1 (legibilidad) + U-M2 (ARCO+) | RGPD Arts. 12–14 | **20 M€ o 4% facturación** | Actividad AEPD 2024–2025 |
| 8 | NC-M3 + NC-M4 (notificación brechas) | RGPD Art. 33 + NIS2 Art. 23 | **10 M€ o 2% facturación** | Múltiples casos AEPD 2024 |
| 9 | DD-M1 (DPAs encargados) | RGPD Art. 28 | **10 M€ o 2% facturación** | Actividad AEPD 2023–2025 |
| 10 | D-M1 + D-M2 (videovigilancia) | LOPDGDD Art. 22 | Hasta **20 M€** si incluye biometría | Actividad AEPD (videovigilancia: caso más frecuente) |

---

## COBERTURA NORMATIVA POR INDICADOR LINDDUN

| Indicador | RGPD (arts.) | AI Act (arts.) | NIS2 (arts.) | ENS | ISO |
|-----------|-------------|---------------|-------------|-----|-----|
| **L – Linking** | 5.1.c, 25, 30, 32, 35 | Annex IV; 9.2; 10 | 21.2 | op.pl.1; mp.si.2 | 27001 A.8.11; 27701 §7.2.1; 29101 |
| **I – Identifying** | 4.1, 4.5, 5.1.e, 9, 25, 32, 35 | 5.1.d, e; 10.3 | — | (datos cat. alta) | 19795; 20889; 27701 §7.2.3; 29101 |
| **NR – Non-repudiation** | 5.1.e, 5.2, 7, 12.3, 17, 19, 30, 32 | 13; 52 | 21.2 | op.exp.8; op.exp.10; mp.si.3 | 27001 A.8.15; 27701 §8.4.2; ETSI EN 319 |
| **D – Detecting** | 5.1.b, 5.1.c, 9, 13, 25, 32, 35 | 5.1.d, e; 6; 9.2 | 21.2 | op.exp.9 | 19795; 27701 §7.2.3; ETSI EN 303 645 |
| **DD – Data Disclosure** | 5.1.b, 5.1.c, 5.1.e, 6, 17, 25.2, 28, 29, 32, 35, 44–49 | 10; 13; 27; 28; 53 | 21.2; 21.5 | (subcontratación) | 27001 A.5.19–5.22; 27701 §6.12, §8.5; 29101 §8.3 |
| **U – Unawareness** | 5.1.a, 6, 7, 12–22, 22, 39.1.b | 4.2; 13; 14; 52; 86 | 20 | mp.per.2 | 27001 A.6.3; 27701 §7.3.2–7.3.5 |
| **NC – Non-compliance** | 5.2, 24, 32–35, 37–39 | 5; 6; 9; 10; 13; 17; 22; 27; 43 | 20; 21; 23; 32 | op.pl.1; op.exp.7 | 27001 §6.1.2; 27035; 29134; 42001 |
| **IN – Inaccuracy** | 5.1.d, 5.1.f, 16, 22 | 9; 10; 15; 43 | — | — | 8000; 42001 §9.1; IEEE 7003 |
| **EX – Exclusion** | 5.1.a, 12, 15–22 | 14 | — | (accesibilidad) | 9241-171; WCAG 2.1 AA; RD 1112/2018 |

---

*Mapeo normativo elaborado conforme al estado del Derecho europeo y español en abril de 2026. AI Act: Reglamento (UE) 2024/1689, prohibiciones vigentes desde feb. 2025; obligaciones alto riesgo desde ago. 2026. NIS2: Directiva (UE) 2022/2555. ENS: RD 311/2022. LIINE4DU 1.0: AEPD, octubre 2024. Versión 1.0.*
