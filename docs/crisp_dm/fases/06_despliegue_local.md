# Fase 6 — Despliegue local

**Pregunta que responde:** ¿podemos guardar el modelo y utilizarlo fuera del entrenamiento?

**Alcance del laboratorio:** demostración local, **sin API ni despliegue productivo**. El modelo se guarda en `.joblib`, se carga de nuevo y se utiliza para predecir una muestra con 16 entradas.

**Comprobación en Windows:** `scikit-learn 1.6.1`; se cargó el modelo y predijo `SEKER` para una muestra cuya clase real era `SEKER`. Este acierto individual **no es una medida de rendimiento global**.

**Evidencia:** [modelo guardado](../../../outputs/models/logistic_regression_drybean.joblib), [script de verificación](../../../scripts/verificar_modelo_guardado.py) y [código reutilizable](../../../src/predict.py).

**Para explicar:** diferencia entre entrenamiento, persistencia e inferencia; límites de una prueba local.
