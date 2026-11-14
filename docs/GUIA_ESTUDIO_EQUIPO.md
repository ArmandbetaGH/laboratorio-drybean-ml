# GUÍA DE ESTUDIO - EQUIPO DRY BEAN

**Asignatura:** Gestión de Proyectos en IA y Ciencia de Datos  
**Laboratorio 1:** Clasificación de variedades de frijol  
**Integrantes que presentarán:** Mónica Giraldo, Andrés Hernández y Armando  
**Base:** enunciado del Laboratorio 1, planificación de Scrum ML y resultados del repositorio.  
**Nota de actualización:** el equipo confirmó la ejecución completa del notebook en Windows, siete pruebas automatizadas aprobadas y una predicción SEKER correcta al cargar el modelo guardado con scikit-learn 1.6.1. Quedan pendientes la ejecución en Mac y la confirmación democrática de roles Scrum ML.

## Requisitos y criterios de evaluación
El laboratorio evalúa tres metodologías: CRISP-DM (seis fases), TDSP (organización técnica, trazabilidad, reproducibilidad) y Scrum ML (roles, backlog, sprints, tablero y Definition of Done). También exige carga, exploración, limpieza, dos modelos, métricas, matriz de confusión, modelo guardado y conclusiones. No exige API, Airflow, MLflow ni Docker para el primer laboratorio.

**Rúbrica (100 puntos):** CRISP-DM 20; TDSP 15; Scrum ML 15; código reproducible 20; evaluación 15; interpretación y conclusiones 15. Ver `docs/MAPA_RUBRICA_EVIDENCIAS.md`.

## 1. Entender el caso de negocio (CRISP-DM, fase 1)
- **Problema:** una empresa agrícola simulada necesita apoyo en la identificación de variedades de frijol.
- **Objetivo técnico:** predecir la variedad a partir de 16 mediciones geométricas; salida `Class`.
- **Alcance real:** prototipo de clasificación tabular, no clasificador de imágenes crudas; no se midieron ahorro, tiempo, ni mejora operativa.
- **Por qué importa:** el modelo es un medio para una decisión; una buena Accuracy no equivale a mejorar 92 % una operación.
- **Dónde mostrar:** primera sección Markdown del notebook, `docs/crisp_dm/01_comprension_negocio.md`.

## 2. Comprender los datos (fase 2)
- **Fuente original:** UCI Dry Bean Dataset (ID 602): 13.611 filas, 16 variables predictoras, 1 variable objetivo (`Class`), siete clases.
- **Variables:** `Area`, `Perimeter`, `MajorAxisLength`, `MinorAxisLength`, `AspectRatio`, `Eccentricity`, `ConvexArea`, `EquivDiameter`, `Extent`, `Solidity`, `Roundness`, `Compactness` y cuatro `ShapeFactor`.
- **Tipos:** 2 enteras, 14 decimales, `Class` categórica. En el conjunto original no se reportaron nulos.
- **Duplicados:** el notebook registró 68; el conjunto limpio tiene 13.543 filas y cero duplicados.
- **Desbalance:** DERMASON 3.546 (26,18 %), SIRA 2.636 (19,46 %), SEKER 2.027 (14,97 %), HOROZ 1.860 (13,73 %), CALI 1.630 (12,04 %), BARBUNYA 1.322 (9,76 %), BOMBAY 522 (3,85 %). Proporción mayor/menor ≈ 6,79.
- **Comandos:** `df.shape`, `df.info()`, `df.describe()`, `df.isna().sum()`, `df.duplicated().sum()`, `df['Class'].value_counts()`.
- **Por qué importa F1 macro:** el promedio da igual peso a cada clase y permite ver un resultado global menos dominado por la clase más numerosa. No reemplaza métricas individuales.
- **Dónde mostrar:** notebook (celdas de EDA), `outputs/reports/calidad_datos_procesados.json`, `outputs/reports/distribucion_clases_procesadas.csv`.

## 3. Preparar datos (fase 3)
- `drop_duplicates()` elimina filas enteramente idénticas; no se debe confundir duplicados con mediciones similares.
- `X = df_clean.drop(columns='Class')` conserva las 16 variables de entrada; `y = df_clean['Class']` define la etiqueta de cada registro.
- `train_test_split(test_size=0.2, random_state=42, stratify=y)` crea entrenamiento 80 % (10.834) y prueba 20 % (2.709), con proporciones de clases similares.
- La semilla 42 permite repetir la partición; `stratify=y` ayuda a mantener representatividad relativa de las clases.
- `StandardScaler` ajusta escala dentro de `Pipeline` en entrenamiento para la regresión logística; nunca ajustar el escalador con datos de prueba por adelantado.
- **Dónde mostrar:** notebook (bloques de preparación y división).

## 4. Entrenar dos modelos (fase 4)
**Regresión logística (baseline):** primer punto de comparación. Se usa `Pipeline(StandardScaler, LogisticRegression(max_iter=1000, random_state=42))`. Aunque su nombre incluya «regresión», aquí clasifica siete categorías.  
**Random Forest:** conjunto de 200 árboles con `class_weight='balanced'`, que intenta compensar la frecuencia de clases. Generalmente no requiere escalar variables para tomar decisiones por umbrales.  
**Lección:** más complejidad no garantiza mejor desempeño.

## 5. Evaluar y elegir (fase 5)

| Modelo | Accuracy histórico | F1 macro histórico |
|---|---:|---:|
| Logistic Regression | 91,95 % | 93,06 % |
| Random Forest | 91,81 % | 92,92 % |

- **Accuracy:** predicciones correctas / total del conjunto de prueba.
- **Precisión por clase:** entre las predicciones de una clase, qué fracción fue correcta.
- **Recall por clase:** entre los casos reales de una clase, cuántos identificó el modelo.
- **F1 por clase:** media armónica entre precisión y recall; F1 macro es promedio de F1 de las clases.
- **Matriz de confusión:** filas suelen representar clases reales y columnas predicciones; la diagonal son aciertos. Revisar DERMASON/SIRA.
- **Resultado:** la regresión logística es candidata por ventaja marginal de F1 macro y menor complejidad. No afirmar superioridad estadística.
- **Importancia de variables de Random Forest:** muestra utilidad para dividir los datos, NO relaciones causales.
- **Dónde mostrar:** notebook (comparación, reportes de clasificación y matrices) y `outputs/reports/`.

## 6. Despliegue local (fase 6)
- `joblib.dump()` guarda el pipeline; `joblib.load()` lo recupera. Un `.joblib` puede ejecutar contenido malicioso al cargarse: usar solo el artefacto confiable del equipo.
- `src/predict.py` recibe un DataFrame con las 16 columnas en el orden requerido y devuelve una variedad.
- Esta es una prueba local de inferencia, no un servicio productivo en nube.
- **Dónde mostrar:** notebook (últimas celdas), `src/predict.py`, `outputs/models/logistic_regression_drybean.joblib`.

## 7. ¿Para qué TDSP?
Estructurar y conservar: `data/raw` (original, al descargarlo), `data/processed` (limpio), `notebooks` (EDA/modelado), `src` (funciones), `outputs/models` (modelo), `outputs/reports` (resultados), `docs` (decisiones), `tests` (comprobaciones), `README.md` (ejecución) y `requirements.txt` (versiones). GitHub guarda los cambios para Windows y Mac; NO subir `.venv`.

## 8. ¿Para qué Scrum ML?
- **Product Backlog:** lista priorizada de historias y tareas con criterios de aceptación.
- **Sprint:** periodo corto con una meta entregable. Aquí se documentaron tres: preparación, modelado/evaluación y despliegue/documentación.
- **Tablero:** Por hacer / En progreso / Hecho. Debe representar el estado real.
- **Definition of Done:** lista de pruebas exigidas para cerrar un ítem.
- **Retrospectiva:** qué funcionó, qué fue difícil y qué cambiaríamos. NO declarar reuniones que no ocurrieron.
- **Roles Scrum sugeridos:** Product Owner, Scrum Master y capacidades de ingeniería de datos/ML. Equipo de tres puede compartir funciones, si se acuerda y se documenta.

## 9. Preguntas para preparar la sustentación
1. **¿Por qué CRISP-DM?** Para conectar problema, datos, preparación, modelado, evaluación e inferencia local.
2. **¿Por qué no entrenar con todo el dataset?** Necesitamos prueba independiente sobre observaciones no usadas para ajustar el modelo.
3. **¿Por qué eliminar duplicados antes del split?** Evita que filas idénticas aparezcan simultáneamente en entrenamiento y prueba.
4. **¿Por qué `stratify`?** Mantiene proporciones de variedades en ambos subconjuntos.
5. **¿Por qué escalar regresión logística?** Favorece optimización cuando las variables usan escalas muy diferentes; `Pipeline` evita fuga de datos.
6. **¿Por qué F1 macro?** Considera todas las clases con el mismo peso; Accuracy puede ocultar fallos en clases escasas.
7. **¿Qué clases se confunden más?** DERMASON y SIRA en las matrices guardadas. Ver la matriz antes de afirmarlo en una nueva corrida.
8. **¿Por qué se eligió Logistic Regression?** Tuvo F1 macro algo mayor y es más simple; la ventaja es pequeña.
9. **¿Por qué no API?** La guía pide una demostración local con modelo guardado; una API se estudia después.
10. **¿Qué falta para producción?** Datos operativos, validación externa, costos de error, mantenimiento, seguridad y seguimiento.
11. **¿Qué aportó GitHub?** Versionado, colaboración controlada y trazabilidad del código y documentación.
12. **¿Se hicieron tres sprints reales?** Hay tres sprints documentados como esquema académico; solo se deben afirmar reuniones reales si el equipo las confirma.

## 10. Practicar la sustentación
- Abrir `README.md`, `docs/MAPA_RUBRICA_EVIDENCIAS.md`, `scrum/tablero.md`, notebook y `outputs/reports/`.
- Ensayar sin diapositivas, usando código y evidencias en GitHub o VS Code.
- Cada integrante debe poder explicar su parte y contestar al menos dos preguntas de otra sección.
- La comprobación de **7 pruebas pytest** y la **ejecución íntegra del notebook en Windows** son evidencias distintas; ambas fueron confirmadas. La prueba en Mac sigue pendiente.
- Consultar el guion: `docs/GUION_SUSTENTACION_3_PERSONAS.md`.

## 11. Comprobaciones antes de compartir la versión definitiva
Consultar `docs/VALIDACION_FINAL.md`. En Windows, el archivo `.joblib` se cargó con `scikit-learn==1.6.1` y produjo la clase SEKER, coincidente con la etiqueta real de la muestra. Todavía corresponde comprobar portabilidad en Mac y registrar los roles Scrum acordados realmente.
