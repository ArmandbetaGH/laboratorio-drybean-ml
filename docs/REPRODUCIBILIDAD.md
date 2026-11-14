# Reproducibilidad técnica — Laboratorio Dry Bean

## Requisitos

Python 3.12 y acceso a Internet para recuperar el dataset original desde UCI. Ejecutar los comandos desde la raíz del repositorio. Las dependencias se encuentran en `requirements.txt`.

## Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
python scripts/generar_reporte_calidad.py
python scripts/verificar_modelo_guardado.py
```

## macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
python scripts/generar_reporte_calidad.py
python scripts/verificar_modelo_guardado.py
```

## Notebook e inferencia

Abrir `notebooks/01_laboratorio_drybean.ipynb` en VS Code o JupyterLab, seleccionar el intérprete del entorno `.venv` y ejecutar todas las celdas en orden. El notebook consulta la fuente UCI, por lo que la descarga requiere conectividad. Se recomienda no volver a entrenar durante la exposición si ya existen salidas reproducidas y guardadas.

La carga del archivo `outputs/models/logistic_regression_drybean.joblib` y la predicción local se verifican mediante `scripts/verificar_modelo_guardado.py`. Por seguridad, cargar archivos `.joblib` únicamente de fuentes confiables.

## Alcance de la verificación

El equipo confirmó la ejecución completa del notebook en Windows. Adicionalmente se aprobaron siete pruebas automáticas y se ejecutó una predicción local con `scikit-learn 1.6.1`. La ejecución en macOS aún debe comprobarse. La predicción individual no sustituye las métricas de evaluación del conjunto de prueba.

El entorno virtual `.venv` no debe incluirse en el control de versiones.
