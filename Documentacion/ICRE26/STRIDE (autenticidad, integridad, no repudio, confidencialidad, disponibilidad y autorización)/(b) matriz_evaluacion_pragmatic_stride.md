# Matriz de Evaluación PRAGMATIC Completa

Escala usada por criterio (0–3):

- 0 = No cumple o irrelevante.
- 1 = Cumple parcialmente / utilidad limitada.
- 2 = Cumple de forma adecuada.
- 3 = Cumple de forma sobresaliente.

A continuación se ofrece una valoración de referencia para cada métrica STRIDE. Esta valoración debe adaptarse al contexto concreto de cada organización o, a nivel nacional, a la disponibilidad real de datos.

## 1. Métricas de Spoofing (S)

| ID | Métrica | P | R | A | G | M | Prc | O | I | C |
|----|---------|---|---|---|---|---|-----|---|---|---|
| S1 | % de accesos críticos con MFA | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 |
| S2 | % de cuentas privilegiadas bajo PAM con MFA | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 |
| S3 | % de APIs críticas con autenticación fuerte | 2 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 2 |
| S4 | Tasa de intentos de suplantación detectados | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |

## 2. Métricas de Tampering (T)

| ID | Métrica | P | R | A | G | M | Prc | O | I | C |
|----|---------|---|---|---|---|---|-----|---|---|---|
| T1 | % de sistemas críticos con logs/datos protegidos criptográficamente | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 |
| T2 | % de procesos críticos con doble control / SoD | 2 | 3 | 3 | 2 | 3 | 3 | 1 | 2 | 2 |
| T3 | % de dispositivos críticos con firmware firmado y arranque seguro | 2 | 3 | 2 | 2 | 3 | 3 | 1 | 2 | 1 |

## 3. Métricas de Repudiation (R)

| ID | Métrica | P | R | A | G | M | Prc | O | I | C |
|----|---------|---|---|---|---|---|-----|---|---|---|
| R1 | % de sistemas críticos con logging centralizado y completo | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 |
| R2 | % de logs críticos almacenados en soportes inmutables | 2 | 3 | 2 | 2 | 3 | 3 | 1 | 2 | 1 |
| R3 | Tiempo medio para reconstruir un incidente (TMR) | 3 | 3 | 3 | 2 | 3 | 2 | 1 | 2 | 2 |

## 4. Métricas de Information Disclosure (I)

| ID | Métrica | P | R | A | G | M | Prc | O | I | C |
|----|---------|---|---|---|---|---|-----|---|---|---|
| I1 | % de activos de información clasificados | 1 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 2 |
| I2 | % de datos sensibles cifrados en reposo | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 |
| I3 | % de flujos de red críticos bajo TLS fuerte | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 |
| I4 | % de integraciones críticas con evaluación de riesgo completada | 2 | 3 | 3 | 2 | 3 | 2 | 1 | 2 | 2 |

## 5. Métricas de Denial of Service (D)

| ID | Métrica | P | R | A | G | M | Prc | O | I | C |
|----|---------|---|---|---|---|---|-----|---|---|---|
| D1 | Horas de indisponibilidad anual por servicio crítico | 3 | 3 | 3 | 2 | 3 | 3 | 1 | 2 | 2 |
| D2 | % de servicios externos críticos con protección DoS/DDoS | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 |
| D3 | % de servicios esenciales con planes de continuidad probados | 2 | 3 | 3 | 2 | 3 | 2 | 1 | 2 | 2 |
| D4 | % de herramientas de seguridad con arquitectura redundante | 2 | 3 | 2 | 2 | 3 | 2 | 1 | 2 | 1 |

## 6. Métricas de Elevation of Privilege (E)

| ID | Métrica | P | R | A | G | M | Prc | O | I | C |
|----|---------|---|---|---|---|---|-----|---|---|---|
| E1 | % de cuentas privilegiadas bajo PAM | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 |
| E2 | % de roles/perfiles revisados anualmente | 2 | 3 | 3 | 2 | 3 | 2 | 1 | 2 | 2 |
| E3 | Nº de revisiones de permisos privilegiados/año | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 3 |
| E4 | % de funciones críticas con segregación definida | 2 | 3 | 3 | 2 | 3 | 2 | 1 | 2 | 2 |

## 7. Métricas de Gobierno y Métricas (GOV / MET)

| ID | Métrica | P | R | A | G | M | Prc | O | I | C |
|----|---------|---|---|---|---|---|-----|---|---|---|
| G1 | Nivel de formalización del threat modeling (0–3) | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 3 |
| G2 | % de proyectos críticos con threat modeling STRIDE | 2 | 3 | 3 | 2 | 3 | 2 | 1 | 2 | 2 |
| M1 | Índice de cobertura de métricas STRIDE (0–1) | 2 | 3 | 3 | 2 | 3 | 2 | 1 | 2 | 2 |
| M2 | Nº de decisiones de inversión justificadas por métricas/año | 2 | 3 | 3 | 2 | 3 | 2 | 1 | 2 | 2 |

La suma o media de los criterios PRAGMATIC por métrica permite priorizar cuáles conviene implantar primero.