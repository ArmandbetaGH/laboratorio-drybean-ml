# Auditoría de ajustes y pendientes — Laboratorio 1

## Modificaciones ejecutadas en la copia revisada
- Se corrigió la doble definición de la función en `src/predict.py` y
  se añadieron controles básicos de tipo, vacío y orden de columnas.
- Se documentó la comprensión del negocio, mapa de evidencias y las
  siete preguntas de reflexión de la guía.
- Se revisó el README, se añadieron instrucciones Windows/Linux/macOS
  y se eliminaron dependencias indirectas innecesarias del requirements.
- Se actualizó el backlog de acuerdo con lo **evidenciado en archivos**;
  se creó tablero y plantilla de roles sin inventar integrantes.
- Se conservó el notebook original con salidas, añadiendo celdas Markdown
  académicas. No se alteraron algoritmos, parámetros ni valores de resultados.
- Se omitió `.venv` del ZIP nuevo porque es un entorno local no portable.
- Se conservaron los dos gráficos y el modelo entregados por el compañero.

## Verificación adicional realizada en esta revisión
- Entrenamiento **nuevo** desde el CSV procesado con Python 3.13.5 y sklearn 1.8.0:
  Logistic Regression Accuracy 0,91952750 y F1 macro 0,93055087;
  Random Forest Accuracy 0,91915836 y F1 macro 0,93015400.
- Se registraron los resultados y versiones en `reproduccion_desde_csv.json`.
  No se presentaron advertencias en esa ejecución. Estos resultados **no
  sustituyen** las salidas históricas del notebook de sklearn 1.6.1.

## Pendientes antes de la entrega/sustentación
- [ ] Confirmar integrantes, roles y qué colaboración ocurrió realmente.
- [ ] Actualizar tablero con estados y seguimiento real del equipo.
- [ ] Validar la retrospectiva con los participantes y completar fechas.
- [ ] Ejecutar el notebook íntegro desde cero en el computador del equipo,
      con acceso a UCI; registrar versión de Python y paquetes.
- [ ] Investigar las advertencias numéricas original `RuntimeWarning` de
      `sklearn`; evitar afirmar que están resueltas.
- [ ] Probar la carga del `.joblib` de origen confiable en entorno con
      versión de sklearn compatible.
- [ ] Si procede, guardar la copia realmente descargada en `data/raw/`
      y documentar fecha, fuente y checksum (no crear datos sintéticos).
- [x] Repositorio privado creado y primer push completado desde Windows.
      URL: https://github.com/ArmandbetaGH/laboratorio-drybean-ml
- [ ] Incorporar actualización fase 2 en `main` y verificar ejecución Windows.
- [ ] Invitar a la compañera al terminar ajustes y verificar clonación en Mac.
- [ ] Hacer la socialización de 10–12 minutos basada en los archivos y
      responder las preguntas de la guía.

## Diferencia respecto a otros laboratorios
Según la clase del 13 de noviembre, DataOps/MLOps/LLMOps con MLflow,
Airflow, FastAPI y monitorización pertenecen a prácticas siguientes y
no son requisitos nuevos del Laboratorio 1.

## Qué NO está verificado todavía
- Ejecución completa del notebook desde descarga UCI y entrenamiento
  en un entorno limpio tras estas modificaciones.
- Correcta deserialización del modelo original en otro computador.
- Roles personales, dailies o retrospectivas reales, por ausencia de
  documentos que los acrediten.

## Actualización posterior — fase 2 (comprensión de datos)
- Se añadió una interpretación en Markdown al notebook (sin modificar código ni resultados históricos).
- Se agregó un script multiplataforma para generar evidencias desde `data/processed/drybean_clean.csv`.
- Se añadieron pruebas de validación del esquema y generación del reporte.
- El reporte del CSV limpio **no es** una descarga nueva de UCI ni valida los 68 duplicados originales.
