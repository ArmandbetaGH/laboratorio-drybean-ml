# Definition of Done — Laboratorio 1

Criterios técnicos y metodológicos que se utilizarán para valorar la finalización del laboratorio.

| ID | Criterio | Evidencia | Estado |
|---|---|---|---|
| DoD-01 | Notebook ejecutado de principio a fin sin errores | `notebooks/01_laboratorio_drybean.ipynb` | Confirmado en Windows por el equipo |
| DoD-02 | Dataset cargado desde la fuente | Celda `fetch_ucirepo(id=602)` | Confirmado mediante ejecución del notebook en Windows; copia en `data/raw/` opcional |
| DoD-03 | Revisión de nulos y duplicados | Notebook y reporte de calidad | Cumplido |
| DoD-04 | Entrenamiento de baseline y alternativa | Notebook con dos modelos | Cumplido en Windows |
| DoD-05 | Comparación de Accuracy y F1 macro | Tabla comparativa y reportes | Cumplido |
| DoD-06 | Matriz de confusión | Dos imágenes en `outputs/reports/` | Cumplido |
| DoD-07 | Modelo seleccionado guardado | `.joblib` y script de inferencia | Carga y predicción confirmadas en Windows |
| DoD-08 | Interpretación comprensible | README y síntesis metodológica | Documentado |
| DoD-09 | Relación CRISP-DM, TDSP y Scrum ML | Índice de fases, repositorio, backlog y sprints | Documentado; acuerdos Scrum personales pendientes |

**Validaciones complementarias pendientes:** ejecución en Mac, asignación definitiva de roles y retrospectiva basada en hechos confirmados. Los criterios técnicos cumplidos no implican automáticamente que todas las actividades de Scrum hayan ocurrido.
