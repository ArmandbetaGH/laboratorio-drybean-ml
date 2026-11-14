# VALIDACIÓN TÉCNICA Y PENDIENTES DE EQUIPO

## A. Confirmado por las capturas y la revisión del equipo en Windows
- Repositorio privado `ArmandbetaGH/laboratorio-drybean-ml` publicado en `main`, segundo commit `2d1dbcc`.
- Python 3.12.7, entorno `.venv`, `scikit-learn==1.6.1` y dependencias instaladas en Windows.
- `python -m pytest -q`: **7 passed**.
- `python scripts/generar_reporte_calidad.py`: ejecutado con dos archivos de salida.
- `python scripts/verificar_modelo_guardado.py`: modelo cargado con 16 columnas, predicción **SEKER**, clase real **SEKER**; es una sola muestra y no mide Accuracy general.
- El usuario confirmó ejecución integral del notebook en VS Code sin errores y guardó y publicó la versión resultante.
- Se enviaron invitaciones a Mónica y Andrés; las capturas mostraban ambas pendientes de aceptación.

## B. Pendientes reales, sin atribuir actividades no comprobadas
- [ ] Verificar la ejecución completa desde Mac y la carga del `.joblib` en su entorno.
- [ ] Confirmar con los tres integrantes la asignación Scrum ML, fechas y responsabilidades reales; actualizar `scrum/roles_equipo.md`.
- [ ] Revisar y completar retrospectiva y tablero con actividades realmente realizadas (no fabricar ceremonias).
- [ ] Si se requiere conservar fuente original, ejecutar `python scripts/guardar_fuente_original.py` y verificar `data/raw/`.
- [ ] Comparar métricas y salidas de la última ejecución en Windows con los valores registrados en el informe.
- [ ] Ensayar la exposición de 11:30 minutos con `docs/RUTA_SUSTENTACION_PROFESOR.md`.

## C. Comandos de ejecución en Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
python -m pytest -q
python scripts/generar_reporte_calidad.py
python scripts/verificar_modelo_guardado.py
python scripts/guardar_fuente_original.py
```

El último comando consulta UCI y necesita internet. No reemplaza las celdas originales de carga del notebook; deja respaldo trazable en `data/raw/`.

## D. Comandos en macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
python scripts/verificar_modelo_guardado.py
python -m jupyter lab
```

Abrir notebook y seleccionar kernel de `.venv`. Para el `.joblib`, la compatibilidad exacta con scikit-learn 1.6.1 se debe probar en Mac.

## E. Publicar los cambios sin borrar Git
1. Copiar los archivos de la actualización **dentro** de la carpeta existente `laboratorio_drybean_ml`, fusionando carpetas. No borrar `.git` ni `.venv` y no sobrescribir el notebook que estén ejecutando.
2. `git status` para revisar qué cambió.
3. Tras validar: `git add .`, `git commit -m "Laboratorio 1 - guia equipo guion y validaciones"`, `git push origin main`.
4. Verificar GitHub y que los compañeros aceptaron las invitaciones ya enviadas.
