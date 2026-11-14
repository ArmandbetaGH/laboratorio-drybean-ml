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
| **CRISP-DM** | Comprender negocio y datos; preparar, modelar, evaluar y demostrar uso local | [Notebook](notebooks/01_laboratorio_drybean.ipynb) · [Documentación de fases](docs/crisp_dm/) |
| **TDSP** | Separación de datos, código, modelos, resultados y pruebas; control de versiones | Carpetas del repositorio · `requirements.txt` · historial Git |
| **Scrum ML** | Product Backlog, tablero, tres sprints, definición de terminado y retrospectiva | [Carpeta Scrum](scrum/) |

Los roles personales y la retrospectiva deben reflejar los acuerdos y hechos confirmados por los integrantes; no se deben confundir los **roles Scrum** con las **partes de la exposición**.

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

`data/processed/drybean_clean.csv` contiene el conjunto limpio. El notebook descarga el original de UCI; `data/raw/` no debe describirse como completo hasta que efectivamente se ejecute el script `scripts/guardar_fuente_original.py` y se conserve su salida.

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
docs/crisp_dm/                     Evidencias de CRISP-DM
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

## 7. Estado de las verificaciones

- **Windows:** notebook completo ejecutado sin errores, según la revisión realizada por el equipo; 7 pruebas `pytest` aprobadas; generación de reportes de calidad exitosa.
- **Inferencia local:** `scikit-learn 1.6.1`; modelo cargado; una muestra fue clasificada como SEKER y la etiqueta real de esa muestra también era SEKER. Esto no reemplaza la evaluación sobre todo el conjunto de prueba.
- **GitHub:** cambios publicados en la rama `main` (commit `2d1dbcc` anterior a esta edición del README).
- **Pendiente de comprobación:** instalación y ejecución integral en el Mac del equipo; confirmar roles y retrospectiva reales; conservar copia del origen UCI si se decide exigirla como evidencia.

## 8. Guía para la sustentación (10–12 minutos)

El profesor autorizó presentar directamente desde GitHub o el código. La ruta propuesta utiliza **GitHub como hilo conductor** y **VS Code como apoyo** para mostrar el notebook ejecutado o una predicción, sin requerir diapositivas:

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

**Referencia del laboratorio:** guía docente *Laboratorio práctico de Machine Learning con datos reales: CRISP-DM + TDSP + Scrum ML usando Dry Bean Dataset*, de Juan Manuel Núñez Velasco.
