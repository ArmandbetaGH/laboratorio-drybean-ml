# Product Backlog — Dry Bean

Estado de entregables al cierre de la revisión técnica en Windows. Los roles son **funciones previstas**, no asignaciones personales confirmadas.

| ID | Historia o tarea | Prioridad | Función propuesta | Estado | Evidencia / aceptación |
|---|---|---|---|---|---|
| PB-01 | Obtener y cargar datos de UCI | Alta | Data Engineer | Hecho en Windows | Notebook ejecutado; respaldo local del original opcional. |
| PB-02 | Analizar nulos, duplicados y clases | Alta | Data Analyst | Hecho | Notebook y reporte de calidad. |
| PB-03 | Limpiar datos y guardar CSV procesado | Alta | Data Engineer | Hecho | `data/processed/drybean_clean.csv`. |
| PB-04 | Separar train/test reproduciblemente | Alta | Data Analyst | Hecho | Estratificación 80/20 y semilla 42. |
| PB-05 | Entrenar baseline y medir resultados | Alta | ML Engineer | Hecho | Regresión logística, Accuracy y F1 macro. |
| PB-06 | Entrenar Random Forest | Media | ML Engineer | Hecho | Modelo alternativo y métricas. |
| PB-07 | Comparar modelos y justificar selección | Alta | Equipo | Hecho | Tabla comparativa y README. |
| PB-08 | Obtener matrices de confusión | Alta | ML Engineer | Hecho | Dos imágenes en `outputs/reports/`. |
| PB-09 | Guardar y recuperar modelo | Alta | ML Engineer | Hecho en Windows | `.joblib`, carga y predicción local. |
| PB-10 | Preparar documentación y sustentación | Alta | Equipo | En progreso | README y material de exposición; falta ensayo. |
| PB-11 | Acordar roles, seguimiento y retrospectiva | Alta | Equipo | Por hacer | Completar archivos de Scrum con acuerdos reales. |
| PB-12 | Comprobar portabilidad en macOS | Media | Equipo técnico | Por hacer | Ejecución y pruebas en el equipo Mac. |

Los estados técnicos se basan en archivos y verificaciones del entorno Windows. Las reuniones Scrum y la autoría individual solo se documentarán cuando el equipo las confirme.
