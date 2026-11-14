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

**Reproducibilidad:** [Instrucciones para instalar dependencias, ejecutar el notebook y validar los resultados](docs/REPRODUCIBILIDAD.md).

## 6. Rúbrica y matriz de evidencias — Laboratorio 1

La correspondencia entre los criterios de evaluación, los resultados y los archivos verificables se presenta en la [matriz de evidencias](docs/MAPA_RUBRICA_EVIDENCIAS.md).
