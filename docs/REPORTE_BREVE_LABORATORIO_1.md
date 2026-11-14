# Reporte breve — Laboratorio 1

**Asignatura:** Gestión de Proyectos en Inteligencia Artificial y Ciencia de Datos  
**Título:** Clasificación de variedades de frijol seco (Dry Bean Dataset)  
**Integrantes:** Mónica Giraldo, Andrés Hernández y Armando José Betancourt Millán  
**Enfoque:** CRISP-DM + TDSP + Scrum ML

## 1. Comprensión del negocio

Se plantea un caso académico simulado: apoyar la identificación de siete variedades de frijol mediante un clasificador basado en medidas geométricas. El objetivo es desarrollar, evaluar y demostrar un prototipo reproducible. **No se midieron ahorros, tiempos operativos ni impacto real en una empresa.**

## 2. Comprensión de los datos

Se emplea el **Dry Bean Dataset** de UCI Machine Learning Repository ([ID 602](https://archive.ics.uci.edu/dataset/602/dry+bean+dataset)), compuesto por **13.611 observaciones originales**, **16 características geométricas** y la variable objetivo `Class` (7 variedades). En la exploración se identificaron **0 valores faltantes** y **68 filas duplicadas**. La distribución no es uniforme: DERMASON representa 3.546 observaciones (26,18 %) y BOMBAY 522 (3,85 %) en el conjunto limpio.

## 3. Preparación de los datos

Se eliminaron los 68 duplicados y quedaron **13.543 observaciones**. Se separaron predictores `X` y etiquetas `y`, y se aplicó una partición **80 % entrenamiento / 20 % prueba**, estratificada (`stratify=y`) con semilla 42. La distribución es de **10.834 registros para entrenar** y **2.709 para probar**. En la regresión logística se aplicó `StandardScaler` dentro de un `Pipeline`, aprendido solamente con entrenamiento.

## 4. Modelado

Se entrenó **Logistic Regression** como modelo de referencia (*baseline*) y **Random Forest** como alternativa. El modelo base integra escalamiento y clasificador; Random Forest incorpora 200 árboles y ponderación de clases. Se compararon sobre el conjunto de prueba.

## 5. Evaluación

| Modelo | Accuracy | F1 macro |
|---|---:|---:|
| Logistic Regression | **91,95 %** | **93,06 %** |
| Random Forest | 91,81 % | 92,92 % |

Las métricas corresponden a las registradas en el notebook del proyecto. Se eligió **Logistic Regression** como candidato para inferencia local por su pequeña ventaja en ambas métricas y menor complejidad. Las matrices de confusión muestran dificultades entre las clases DERMASON y SIRA. **Una diferencia pequeña en una sola partición no prueba superioridad estadística general.** Se empleó F1 macro porque las clases presentan frecuencias desiguales.

## 6. Despliegue local

El clasificador seleccionado se guardó con `joblib` como `outputs/models/logistic_regression_drybean.joblib`. El script `scripts/verificar_modelo_guardado.py` cargó el modelo y predijo **SEKER** para una muestra cuya etiqueta real también era **SEKER**. Esto verifica la inferencia de una muestra, **no representa la exactitud general del modelo**. No se implementó una API ni se desplegó un servicio productivo.

## 7. TDSP y Scrum ML

**TDSP:** el repositorio separa `data/`, `notebooks/`, `src/`, `scripts/`, `tests/`, `outputs/`, `docs/` y `scrum/`. Se registran dependencias en `requirements.txt` y cambios en GitHub. La ejecución completa del notebook, **7 pruebas automatizadas** y la carga del artefacto se comprobaron en Windows. La reproducción en macOS permanece pendiente.

**Scrum ML:** se dispuso de un Product Backlog, un tablero de estados, tres sprints, roles combinados para tres personas y Definition of Done. Mónica Giraldo asume Product Owner + Data Analyst; Andrés Hernández, ML Engineer; y Armando José Betancourt Millán, Scrum Master + coordinación TDSP. El balance retrospectivo documenta aprendizajes, dificultades y acciones de mejora sin afirmar que se realizó una reunión formal no registrada.

## 8. Conclusión y limitaciones

Los resultados demuestran que un pipeline de clasificación tabular relativamente sencillo puede distinguir siete variedades con desempeño cercano al 92 % de Accuracy en este conjunto de prueba. El laboratorio evidencia la complementariedad de CRISP-DM (proceso analítico), TDSP (estructura reproducible) y Scrum ML (seguimiento de entregables).

Las conclusiones se limitan a este caso académico. Como mejoras futuras se proponen validación cruzada, pruebas multiplataforma y validación externa en un contexto operativo real.

**Evidencias:** [notebook](../notebooks/01_laboratorio_drybean.ipynb) · [índice CRISP-DM](crisp_dm/README.md) · [matriz de rúbrica](MAPA_RUBRICA_EVIDENCIAS.md) · [backlog y sprints](../scrum/) · [instrucciones de reproducción](REPRODUCIBILIDAD.md).
