# VALIDACIÓN FINAL - ejecutar antes de enviar invitaciones o sustentar

## A. Lo que YA se comprobó
- GitHub privado `ArmandbetaGH/laboratorio-drybean-ml` creado; primera versión `main` publicada desde Windows.
- Entorno Python 3.12.7 en Windows con `.venv` activado e instalación exitosa.
- `python -m pytest -q`: **6 passed** en la versión anterior (captura del equipo; volver a ejecutar porque ahora añadimos una prueba).
- `python scripts/generar_reporte_calidad.py`: ejecutado sin errores en Windows, dos reportes.
- Celdas iniciales del notebook ejecutadas en Windows: descarga, df.shape, df.info y df.describe. **No equivale a ejecución completa**.
- En entorno de revisión con sklearn 1.8.0 se pudo cargar el `.joblib` original y predecir SEKER; aparecieron advertencias de versión porque fue serializado con sklearn 1.6.1. Revalidar en Windows con 1.6.1.

## B. Lo que falta comprobar con el grupo
- [ ] Guardar fuente original UCI y su manifiesto: `python scripts/guardar_fuente_original.py`, con conexión a internet.
- [ ] `python -m pytest -q`: comprobar las siete pruebas tras esta actualización.
- [ ] `python scripts/verificar_modelo_guardado.py`: verificar que el modelo se abre y predice correctamente en Windows con sklearn 1.6.1.
- [ ] Notebook completo: kernel `.venv`, *Restart Kernel and Run All Cells*, sin errores. Guardar el archivo al concluir.
- [ ] Registrar los resultados de la ejecución final: versiones, Accuracy, F1 macro, matrices y advertencias.
- [ ] Confirmar nombres/funciones del equipo; actualizar `scrum/roles_equipo.md`.
- [ ] Revisar backlog, tablero y retrospectiva con Mónica y Andrés; no inventar eventos.
- [ ] Verificar que `.venv`, `.pytest_cache` y archivos secretos no se suban a Git.
- [ ] Subir la versión validada a `main` y comprobar que las carpetas estén visibles en GitHub.
- [ ] Invitar colaboradores y probar clonación en Mac.
- [ ] Practicar una sustentación de 11:30 siguiendo el guion de `docs/GUION_SUSTENTACION_3_PERSONAS.md`.

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
4. Verificar GitHub e invitar a los compañeros cuando el equipo esté conforme.
