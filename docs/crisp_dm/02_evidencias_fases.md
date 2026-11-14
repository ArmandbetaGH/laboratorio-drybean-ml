# Matriz de evidencias — CRISP-DM

La metodología se documenta en seis fases; su ejecución técnica está concentrada en el notebook y en los artefactos del repositorio.

| Fase | Evidencia | Decisión o resultado |
|---|---|---|
| 1. Negocio | [`01_comprension_negocio.md`](01_comprension_negocio.md) | Prototipo de clasificación multiclase como apoyo a un caso agrícola simulado; sin indicadores empresariales medidos. |
| 2. Datos | [Notebook](../../notebooks/01_laboratorio_drybean.ipynb) y [reporte de calidad](../../outputs/reports/calidad_datos_procesados.json) | Fuente UCI: 13.611 registros; 17 columnas; cero nulos y 68 duplicados. El reporte JSON describe el conjunto **procesado**. |
| 3. Preparación | [CSV limpio](../../data/processed/drybean_clean.csv) y notebook | 13.543 registros; separación `X`/`y`; entrenamiento/prueba 80/20, estratificados y con semilla fija. |
| 4. Modelado | Notebook, sección de entrenamiento | `LogisticRegression` con `StandardScaler` y alternativa `RandomForestClassifier`. |
| 5. Evaluación | [Matrices y reportes](../../outputs/reports/) | Comparación de Accuracy y F1 macro; análisis de confusiones, especialmente DERMASON/SIRA. |
| 6. Despliegue local | [`src/predict.py`](../../src/predict.py), [modelo guardado](../../outputs/models/logistic_regression_drybean.joblib) y [script de prueba](../../scripts/verificar_modelo_guardado.py) | Carga del artefacto y predicción local comprobadas en Windows. No es un servicio productivo. |

## Lectura de resultados

- **Accuracy:** proporción de predicciones correctas en el conjunto de prueba.
- **F1 macro:** promedio de F1 por clase, sin ponderar por cantidad de ejemplos.
- **Matriz de confusión:** recuento de clases reales frente a predichas.
- **Importancia de variables:** relevancia predictiva dentro de Random Forest; no prueba causalidad.

## Alcance de la validación

La ejecución completa del notebook y las siete pruebas automatizadas fueron confirmadas en Windows. La portabilidad a macOS está pendiente y la documentación Scrum ML deberá reflejar la asignación real de roles y acuerdos del equipo.
