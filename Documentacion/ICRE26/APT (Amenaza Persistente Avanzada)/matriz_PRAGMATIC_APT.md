# Matriz de Evaluación PRAGMATIC Completa para las métricas APT

**Escala de puntuación por criterio**  
- 0 = No cumple / muy bajo  
- 1 = Cumple parcialmente / medio  
- 2 = Cumple totalmente / alto  
(En la columna “Comentario” se explica la justificación.)

| Métrica | P (Predictivo) | R (Relevante) | A (Accionable) | G (Genuino) | M (Significativo) | A (Preciso) | T (Oportuno) | I (Independiente) | C (Rentable) | Total (0‑18) | Comentario global |
|---------|----------------|---------------|----------------|-------------|-------------------|-------------|--------------|-------------------|--------------|--------------|-------------------|
| MTTD (horas) | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 16 | Muy fuerte en todos los aspectos; solo la independencia se ve ligeramente afectada por la dependencia de fuentes internas de SIEM. |
| MTTR (horas) | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 16 | Similar a MTTD; la acción de mejora es directa (reducir tiempos). |
| % Phishing | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 17 | Muy fácil de obtener (costo bajo) y altamente independiente; la capacidad predictiva es moderada porque el phishing puede variar por campañas. |
| Cobertura TTPs MITRE (promedio) | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 15 | La precisión depende de la granularidad de las herramientas (EDR/XDR); la oportunidad mejora con actualizaciones frecuentes. |
| MTTP (días) | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 16 | Excelente en todos los rubros salvo la independencia (depende de parches de proveedores). |
| IGM (índice 0‑1) | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 12 | Es un indicador sintético; su independencia y rentabilidad son menores porque requiere agregación y mantenimiento. |
| ROI ciberseguridad (ratio) | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 14 | La precisión y oportunidad dependen de la calidad de las estimaciones de pérdida evitada; es rentable porque justifica la inversión. |

**Interpretación del total**  
- 16‑18 → Métrica de alta calidad PRAGMATIC.  
- 12‑15 → Métrica buena, con algún aspecto que mejorar (normalmente independencia o rentabilidad).  
- < 12 → Métrica que necesita revisión profunda antes de su adopción.

---  