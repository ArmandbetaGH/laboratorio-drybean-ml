# Verificación técnica y estado de entrega

## Evidencias confirmadas en Windows

| Comprobación | Resultado |
|---|---|
| Entorno de desarrollo | Python 3.12.7, entorno virtual `.venv` |
| Librería de modelado | `scikit-learn==1.6.1` |
| Pruebas automáticas | `python -m pytest -q`: 7 pruebas aprobadas |
| Reportes de calidad | Generados desde el CSV procesado |
| Persistencia del modelo | Archivo `.joblib` cargado y utilizado con 16 variables de entrada |
| Predicción individual | SEKER (predicción), SEKER (valor real) |
| Notebook | Ejecución completa sin errores confirmada por el equipo en Windows |
| Repositorio | Publicado en GitHub, rama `main` |

La predicción de una sola muestra no equivale a la evaluación global. Para comparar modelos se utilizan las métricas del conjunto de prueba y las matrices de confusión.

## Por completar o confirmar

- [ ] Probar instalación, notebook e inferencia en macOS.
- [ ] Aprobar entre los tres integrantes los roles y responsabilidades Scrum ML.
- [ ] Registrar retrospectiva y estados de tareas según actividades realmente realizadas.
- [ ] Contrastar el cuadro de métricas del README con la última ejecución guardada del notebook.
- [ ] Conservar en `data/raw/` una copia original con procedencia, si se desea mantener ese respaldo local.
- [ ] Ensayar la exposición y sus transiciones.

## Reproducir las pruebas

En Windows (PowerShell), desde la raíz del repositorio y con `.venv` activo:

```powershell
python -m pytest -q
python scripts/generar_reporte_calidad.py
python scripts/verificar_modelo_guardado.py
```

En macOS, después de crear `.venv` e instalar `requirements.txt`:

```bash
python -m pytest -q
python scripts/verificar_modelo_guardado.py
```

La ejecución del notebook requiere seleccionar el kernel del entorno y acceder a UCI para la carga inicial. Los artefactos serializados deben proceder de una fuente confiable.
