# Product Backlog — Dry Bean

Las responsabilidades de seguimiento se distribuyen según los roles definidos en [`roles_equipo.md`](roles_equipo.md). **Responsable funcional** no implica autoría histórica exclusiva de los archivos.

| ID | Historia o tarea | Prioridad | Responsable funcional | Estado | Evidencia o criterio de aceptación |
|---|---|---|---|---|---|
| PB-01 | Obtener y cargar los datos UCI | Alta | Mónica | Hecho en Windows | Carga de UCI en notebook; copia local original opcional. |
| PB-02 | Analizar nulos, duplicados y distribución | Alta | Mónica | Hecho | Notebook y reportes de calidad. |
| PB-03 | Limpiar datos y conservar CSV procesado | Alta | Mónica | Hecho | `data/processed/drybean_clean.csv`. |
| PB-04 | Separar train/test reproduciblemente | Alta | Mónica | Hecho | Partición estratificada 80/20, semilla 42. |
| PB-05 | Entrenar baseline | Alta | Andrés | Hecho | Regresión logística y métricas. |
| PB-06 | Entrenar Random Forest | Media | Andrés | Hecho | Modelo alternativo y métricas. |
| PB-07 | Comparar modelos y justificar selección | Alta | Andrés + Mónica | Hecho | Comparación en notebook y síntesis CRISP-DM. |
| PB-08 | Generar matrices de confusión | Alta | Andrés | Hecho | Dos matrices en `outputs/reports/`. |
| PB-09 | Guardar y comprobar modelo seleccionado | Alta | Andrés | Hecho en Windows | `.joblib`, carga y predicción local. |
| PB-10 | Organizar documentación, repositorio y evidencias | Alta | Armando | Hecho para versión Windows | README, GitHub, reporte breve, guías de reproducción y pruebas. |
| PB-11 | Definir roles y preparar retrospectiva | Alta | Armando + equipo | Documentado | Roles acordados y retrospectiva de aprendizajes en `scrum/`. |
| PB-12 | Confirmar portabilidad en macOS | Media | Andrés + equipo | Pendiente | Repetir instalación y pruebas en un Mac. |
| PB-13 | Ensayar sustentación grupal | Media | Equipo | Pendiente | Ensayo de 10–12 minutos y revisión de intervenciones. |

**Nota metodológica:** los estados «Hecho» describen entregables técnicos observables; no representan por sí solos ceremonias Scrum celebradas ni atribución individual de ejecución.
