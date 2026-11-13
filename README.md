# Laboratorio 1 — Clasificación de variedades de frijol (Dry Bean)

Proyecto académico de Gestión de Proyectos en IA y Ciencia de Datos, basado en
**CRISP-DM + TDSP + Scrum ML**. Esta es una **copia revisada** del proyecto
entregado por un compañero; el original no ha sido modificado.


## Material para el equipo (Mónica, Andrés y Armando)

**Para estudiar y preparar la sustentación:**

1. [`docs/GUIA_ESTUDIO_EQUIPO.md`](docs/GUIA_ESTUDIO_EQUIPO.md) - explicación completa, conceptos, ejemplos y preguntas.
2. [`docs/GUION_SUSTENTACION_3_PERSONAS.md`](docs/GUION_SUSTENTACION_3_PERSONAS.md) - intervención propuesta de cada integrante, 11:30 min.
3. [`docs/MAPA_RUBRICA_EVIDENCIAS.md`](docs/MAPA_RUBRICA_EVIDENCIAS.md) - evidencia por criterio y 9 puntos de Definition of Done.
4. [`docs/VALIDACION_FINAL.md`](docs/VALIDACION_FINAL.md) - comprobaciones pendientes y comandos Windows/Mac.
5. [`docs/material_presentacion/`](docs/material_presentacion/) - versiones PDF para compartir y estudiar.
6. [`scrum/definition_of_done.md`](scrum/definition_of_done.md) - criterios del laboratorio.

**Situación:** la carga y exploración inicial del notebook ya se comprobó en Windows; las 6 pruebas existentes pasaron y se generaron reportes de calidad. **El notebook íntegro y los roles reales aún requieren verificación final.** Esta versión no afirma que hayan ocurrido reuniones Scrum o una validación con usuarios.

## 1. Problema y alcance

Caso simulado: una empresa agrícola clasifica parcialmente de forma manual
variedades de frijol y quiere explorar un sistema de apoyo a la clasificación.
El objetivo **técnico** es predecir una de siete variedades a partir de 16
características geométricas. No se realizaron pruebas de tiempos, costos,
operación agrícola real ni validación con usuarios. Ver
[`docs/crisp_dm/01_comprension_negocio.md`](docs/crisp_dm/01_comprension_negocio.md).

## 2. Dataset y tratamiento

Fuente: [Dry Bean Dataset, UCI, ID 602](https://archive.ics.uci.edu/dataset/602/dry+bean+dataset).
Original: 13.611 filas, 16 predictoras y `Class` como objetivo (17 columnas).
En el notebook original se observan 68 duplicados exactos y cero nulos;
tras remover duplicados quedan 13.543 registros. División estratificada
train/test 80/20 con `random_state=42` (10.834/2.709).

- `data/raw/`: no contiene una copia de la fuente original. **El notebook
  descarga la fuente oficial vía Internet**; no atribuir a esta carpeta
  archivos que no existen.
- `data/processed/drybean_clean.csv`: datos procesados proporcionados
  en la entrega original. Sirven para inspección y comprobaciones locales.

## 3. Resultados del notebook original (no resultados de una nueva ejecución)

| Algoritmo | Accuracy | F1 macro |
|---|---:|---:|
| Logistic Regression (baseline) | 91,95 % | 93,06 % |
| Random Forest | 91,81 % | 92,92 % |

Candidato: **Logistic Regression** por diferencia pequeña a favor en una
partición de prueba y menor complejidad. No prueba superioridad general.
Se identificaron confusiones DERMASON/SIRA, e identificación correcta de
los 104 registros BOMBAY del conjunto de prueba original.
El notebook original presenta advertencias numéricas durante el ajuste de
Logistic Regression; **pendiente** investigar con entorno equivalente.

## 4. Organización metodológica

- **CRISP-DM:** `docs/crisp_dm/` contiene problema, evidencias y decisiones.
- **TDSP:** `data/`, `notebooks/`, `src/`, `outputs/` y este README.
- **Scrum ML:** `scrum/` contiene backlog, tablero, sprints y plantillas de
  roles / retrospectiva. Los responsables personales y eventos reales
  deben ser validados por el equipo; no se han inventado.

## 5. Ejecución en Windows (PowerShell)

Desde la carpeta raíz, con Python disponible:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m jupyter lab
```

En macOS/Linux: `python3 -m venv .venv`,
`source .venv/bin/activate` y luego los dos comandos `python -m ...`.
Abrir `notebooks/01_laboratorio_drybean.ipynb` y ejecutar las celdas
en orden **con conexión a Internet**, pues descarga datos desde UCI.
Si se ejecuta desde `notebooks/`, el propio notebook resuelve la raíz
relativa del proyecto; la fuente en bruto no está precargada.

Para comprobar solo estructura/datos locales (sin descarga ni entrenamiento):

```bash
python scripts/verificar_estructura.py
```

### Evidencia reproducible de la fase 2: calidad del CSV limpio

Sin descargar de UCI ni entrenar modelos, podemos validar la copia procesada:

```bash
python scripts/generar_reporte_calidad.py
python -m pytest -q
```

Genera `outputs/reports/calidad_datos_procesados.json` y
`outputs/reports/distribucion_clases_procesadas.csv`. Esta comprobación
analiza **13.543 registros del CSV limpio**, no los 13.611 registros
originales de UCI. Para ver los 68 duplicados originales hay que
consultar las salidas guardadas del notebook o ejecutar su descarga.

## 6. Demostración de inferencia local

El notebook guarda un pipeline Logistic Regression con `joblib` y luego
realiza una predicción de muestra. `src/predict.py` implementa la función
reutilizable `predict_bean_class(df_con_las_16_columnas)`.
**Seguridad:** abrir archivos `.joblib` únicamente si su origen es confiable
(internamente usan pickle); no tratar como datos pasivos. Para cargar un
modelo serializado en otra máquina, mantener versiones compatibles, en
particular `scikit-learn==1.6.1` para este artefacto original.

## 7. Carpetas principales

```text
data/{raw,processed}/       Origen (pendiente descarga local) y CSV procesado
notebooks/                EDA, experimentación, modelos y evaluación
src/predict.py            Inferencia modular
outputs/{models,reports}/ Modelo original y matrices de confusión
docs/crisp_dm/            Evidencia de metodología
docs/revision/            Auditoría y asuntos pendientes
scrum/                   Tablero, backlog, sprints y retrospectiva
scripts/                 Verificador sin dependencia de ML
tests/                   Pruebas estructurales básicas
```

## 8. Alcance de la entrega

El profesor indicó que el Laboratorio 1 se socializa desde el repositorio
o el código, sin exigir una presentación independiente, y que DataOps,
MLOps y LLMOps se abordarán en laboratorios posteriores.
La simulación Scrum **no acredita por sí misma** reuniones, asignaciones
o colaboración real; documentar solo lo efectivamente ocurrido.
Consultar `docs/revision/pendientes_para_equipo.md` antes de entregar.

## 9. GitHub y colaboración Windows/macOS

Repositorio privado existente: https://github.com/ArmandbetaGH/laboratorio-drybean-ml

La primera versión ya se publicó en `main` desde Windows. La fase 2 ya se validó localmente en Windows; las actualizaciones posteriores deben publicarse sin crear otro repositorio.
- Guía completa de publicación, ramas y Pull Requests: [`docs/GITHUB_COLABORACION.md`](docs/GITHUB_COLABORACION.md).
- Fase 2 explicada paso a paso: [`docs/crisp_dm/04_estudio_fase_2.md`](docs/crisp_dm/04_estudio_fase_2.md).
- `.gitignore` excluye entornos locales, cachés y archivos del sistema; `.gitattributes`
  normaliza finales de línea de archivos de texto en Windows/macOS.
- El notebook busca la raíz del proyecto por `requirements.txt` y `src/predict.py`
  en la carpeta actual o cualquiera de sus carpetas superiores, para evitar rutas absolutas.
- El primer `git push` debe hacerse a un **repositorio nuevo** (diferente de Series).

Antes de presentar, ejecutar en **cada sistema** `python scripts/verificar_estructura.py`,
`python -m pytest -q`, y posteriormente el notebook completo con conexión a UCI.
Las pruebas rápidas disponibles no son sustituto de la ejecución integral.
