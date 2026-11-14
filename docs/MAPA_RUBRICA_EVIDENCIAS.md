# Rúbrica y matriz de evidencias — Laboratorio 1

La evaluación considera **metodología, reproducibilidad, desempeño e interpretación**. Las rutas señalan dónde localizar las evidencias en este repositorio.

| Criterio | Puntaje | Evidencia principal | Estado / precisión |
|---|---:|---|---|
| CRISP-DM | 20 | [Seis fases](crisp_dm/README.md), notebook y [síntesis](crisp_dm/05_sintesis_final.md) | Documentado en seis fases |
| TDSP | 15 | Estructura `data/`, `notebooks/`, `src/`, `outputs/`, `tests/`, GitHub y `requirements.txt` | Implementado y versionado |
| Scrum ML | 15 | `scrum/backlog.md`, `scrum/tablero.md`, sprints, DoD, roles y retrospectiva | Plan y entregables documentados; roles y acuerdos por confirmar |
| Código reproducible | 20 | Notebook, scripts, `src/` y pruebas `pytest` | Notebook y 7 pruebas ejecutados en Windows; macOS pendiente |
| Evaluación del modelo | 15 | Comparación de Accuracy y F1 macro, reportes y matrices | Resultados registrados en notebook y gráficos |
| Interpretación y conclusiones | 15 | README, síntesis, explicaciones de errores y límites | Documentado; no se afirman impactos operativos no medidos |

## Criterios de finalización técnica

- [x] Notebook ejecutado de inicio a fin sin errores en Windows (confirmación del equipo).
- [x] Dataset cargado desde UCI durante el notebook. Copia local original opcional, aún no guardada.
- [x] Nulos y duplicados revisados.
- [x] Regresión logística y Random Forest entrenados.
- [x] Accuracy y F1 macro comparados.
- [x] Matrices de confusión disponibles.
- [x] Modelo guardado y carga con predicción comprobadas en Windows.
- [x] Resultados explicados en el README y documentos CRISP-DM.
- [x] CRISP-DM, TDSP y Scrum ML documentados; **pendiente** confirmar asignaciones de roles y acuerdos retrospectivos.

La evidencia técnica no debe confundirse con una reunión Scrum efectivamente celebrada ni con una validación del sistema en producción.
