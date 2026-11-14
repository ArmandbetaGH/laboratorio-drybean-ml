# Laboratorio 1 | Clasificación de variedades de frijol seco

**Asignatura:** Gestión de Proyectos en Inteligencia Artificial y Ciencia de Datos  
**Caso de estudio:** Dry Bean Dataset, UCI Machine Learning Repository  
**Equipo:** Mónica Giraldo · Andrés Hernández · Armando José Betancourt  
**Metodologías:** CRISP-DM + TDSP + Scrum ML

## 1. Propósito del proyecto

Una empresa agrícola ficticia busca explorar la clasificación automatizada de variedades de frijol como apoyo a un proceso parcialmente manual. El proyecto construye y evalúa un **prototipo de clasificación multiclase** a partir de 16 características geométricas de los granos. La variable que se desea predecir es `Class` (siete variedades).

**Alcance:** clasificación tabular y demostración local de inferencia. No se procesan imágenes en bruto ni se ha demostrado una mejora real de tiempos, costos o desempeño operativo de una empresa.

## 2. Enfoque metodológico y evidencias

| Enfoque | Aplicación en este laboratorio | Evidencia |
|---|---|---|
| **CRISP-DM** | Comprender negocio y datos; preparar, modelar, evaluar y demostrar uso local | [Notebook](notebooks/01_laboratorio_drybean.ipynb) · [Seis fases de CRISP-DM](docs/crisp_dm/README.md) |
| **TDSP** | Separación de datos, código, modelos, resultados y pruebas; control de versiones | Carpetas del repositorio · `requirements.txt` · historial Git |
| **Scrum ML** | Product Backlog, tablero, tres sprints, definición de terminado y retrospectiva | [Carpeta Scrum](scrum/) |

La documentación de Scrum ML distingue entre el plan de trabajo, las evidencias técnicas y los acuerdos de equipo pendientes de confirmación.

## 3. Datos y preparación

**Fuente:** [Dry Bean Dataset (UCI, ID 602)](https://archive.ics.uci.edu/dataset/602/dry+bean+dataset).

| Aspecto | Resultado |
|---|---:|
| Registros originales | 13.611 |
| Variables predictoras | 16 |
| Clases | 7 |
| Valores faltantes observados | 0 |
| Filas idénticas duplicadas | 68 |
| Registros después de retirar duplicados | 13.543 |
| Partición de entrenamiento y prueba | 80 % / 20 %, estratificada, semilla 42 |

Las clases no están uniformemente distribuidas: DERMASON tiene 3.546 registros en el CSV limpio (26,18 %) y BOMBAY 522 (3,85 %). Por eso se compara **F1 macro** junto con **Accuracy** y métricas por clase.

`data/processed/drybean_clean.csv` contiene el conjunto limpio. La fuente original se consulta desde UCI durante la ejecución del notebook. La carpeta `data/raw/` está preparada para conservar, cuando se genere, una copia local trazable de esa fuente.

## 4. Modelado y resultados

Se evalúan dos alternativas: **Logistic Regression**, con `StandardScaler` dentro de un `Pipeline`, como modelo de referencia, y **Random Forest**, con 200 árboles y pesos de clase balanceados.

| Modelo | Accuracy registrada en el notebook | F1 macro registrada en el notebook |
|---|---:|---:|
| Logistic Regression | 91,95 % | 93,06 % |
| Random Forest | 91,81 % | 92,92 % |

Se selecciona **Logistic Regression** como candidato de inferencia local por su ventaja marginal en las métricas registradas y su menor complejidad. La diferencia es pequeña y **no acredita superioridad estadística general**. Las matrices de confusión muestran dificultades particularmente entre DERMASON y SIRA.

Artefacto: [`outputs/models/logistic_regression_drybean.joblib`](outputs/models/logistic_regression_drybean.joblib). La carga y predicción local se comprueba mediante `scripts/verificar_modelo_guardado.py`.

## 5. Estructura del repositorio

```text
data/raw/                         Referencia y, cuando se genere, copia del origen UCI
data/processed/                   Dataset limpio
notebooks/                        Exploración, entrenamiento, evaluación y demo
outputs/models/                   Modelo serializado
outputs/reports/                  Matrices de confusión e informes de calidad
src/                              Funciones reutilizables
scripts/                          Scripts de validación y trazabilidad
tests/                            Pruebas automatizadas
docs/crisp_dm/                     Índice de las seis fases y material de apoyo
scrum/                            Backlog, tablero, sprints y Definition of Done
```

## 6. Reproducir la práctica

**Windows (PowerShell), desde la raíz del repositorio:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
python scripts/generar_reporte_calidad.py
python scripts/verificar_modelo_guardado.py
```

**macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
python scripts/verificar_modelo_guardado.py
```

Para ejecutar el notebook, abrir [`notebooks/01_laboratorio_drybean.ipynb`](notebooks/01_laboratorio_drybean.ipynb) en VS Code, seleccionar el kernel del `.venv`, reiniciarlo y ejecutar todas las celdas. La descarga UCI necesita conexión a Internet. No subir `.venv` al repositorio. Abrir archivos `.joblib` únicamente de fuentes confiables.

## 7. Estado de validación técnica

- **Entorno Windows:** notebook ejecutado de principio a fin según la comprobación del equipo; siete pruebas automatizadas aprobadas y reportes de calidad generados.
- **Inferencia:** modelo guardado cargado con `scikit-learn 1.6.1`; una muestra fue clasificada como SEKER, coincidiendo con su etiqueta real. Este resultado individual no sustituye la evaluación de modelos.
- **Colaboración:** repositorio versionado en GitHub. La reproducibilidad en macOS está pendiente de comprobar y la asignación definitiva de roles Scrum requiere acuerdo de los tres integrantes.

Los detalles de las verificaciones y las tareas pendientes figuran en [Validación del proyecto](docs/VALIDACION_FINAL.md).

## 8. Guía para la sustentación (10–12 minutos)

La demostración se propone con **GitHub como hilo conductor** y **VS Code como apoyo** para mostrar el notebook ejecutado y la predicción local:

1. Problema de negocio y objetivo; este README.
2. CRISP-DM y organización TDSP; `docs/crisp_dm/` y carpetas principales.
3. Comprensión y preparación de datos; notebook y reportes.
4. Entrenamiento, comparación, matrices de confusión y selección del modelo.
5. Inferencia local, evidencias Scrum ML y conclusiones.

**[Ruta de sustentación detallada](docs/RUTA_SUSTENTACION_PROFESOR.md)** · **[Mapa de rúbrica y evidencias](docs/MAPA_RUBRICA_EVIDENCIAS.md)**

## 9. Material de apoyo para los integrantes

- [Guía de estudio](docs/GUIA_ESTUDIO_EQUIPO.md)
- [Guion propuesto para tres integrantes](docs/GUION_SUSTENTACION_3_PERSONAS.md)
- [PDF para compartir](docs/material_presentacion/)
- [Validación técnica y pendientes](docs/VALIDACION_FINAL.md)
