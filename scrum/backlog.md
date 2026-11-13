# Product Backlog — laboratorio Dry Bean (revisión documental)

**Estados:** «Evidenciado» = existe un artefacto o resultado en los archivos;
**no significa** que se verificó la ejecución completa ni que consta una
reunión real. «Pendiente» = requiere información o trabajo adicional.

| ID | Historia o tarea | Prioridad | Rol propuesto (sin nombres asignados) | Estado documental | Evidencia / criterio de aceptación |
|---|---|---|---|---|---|
| PB-01 | Obtener y cargar datos de UCI | Alta | Data Engineer | Evidenciado parcialmente | Notebook carga UCI; `data/raw` sin copia local. |
| PB-02 | Examinar calidad, nulos, duplicados y clases | Alta | Data Analyst | Evidenciado | Celdas 7–10, interpretación y reporte reproducible en `outputs/reports/`. |
| PB-03 | Limpiar datos y conservar copia procesada | Alta | Data Engineer | Evidenciado | Celdas 12–15 y CSV procesado. |
| PB-04 | Separar entrenamiento/prueba reproduciblemente | Alta | Data Analyst | Evidenciado | Celda 14: 80/20, estratificada, semilla 42. |
| PB-05 | Entrenar y evaluar baseline | Alta | ML Engineer | Evidenciado; revisar advertencias | Celdas 16–18 y métricas. |
| PB-06 | Entrenar y evaluar Random Forest | Media | ML Engineer | Evidenciado | Celdas 19–21 y métricas. |
| PB-07 | Comparar métricas y justificar selección | Alta | Equipo | Evidenciado | Celdas 22–24, 29, README. |
| PB-08 | Generar matrices de confusión | Alta | ML Engineer | Evidenciado | Celdas 25–29 y dos PNG. |
| PB-09 | Guardar modelo y probar predicción local | Alta | ML Engineer | Evidenciado en notebook | Celdas 33–36, joblib, módulo. Validación de nuevo entorno pendiente. |
| PB-10 | Documentar entregables y preparar sustentación | Alta | Equipo | En progreso | README y docs disponibles; validar autoría/evidencia real. |
| PB-11 | Registrar responsables, avances y retrospectiva reales | Alta | Equipo | Pendiente | Completar `roles_equipo.md`, `tablero.md`, `retrospectiva.md` con información real. |
| PB-12 | Repetir ejecución íntegra y revisar RuntimeWarnings | Alta | Equipo técnico | Pendiente | Notebook ejecutado de principio a fin sin errores; registrar versiones usadas. |
