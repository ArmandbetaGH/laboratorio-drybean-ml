# Fase 4 — Modelado

**Pregunta que responde:** ¿qué algoritmos entrenamos y por qué?

**Modelo base:** `LogisticRegression` con `StandardScaler` dentro de un `Pipeline`.

**Modelo alternativo:** `RandomForestClassifier` con 200 árboles y `class_weight="balanced"`, según la configuración evaluada.

**Evidencia:** [notebook ejecutado](../../../notebooks/01_laboratorio_drybean.ipynb), sección de entrenamiento.

**Para explicar:** qué es un *baseline* y por qué una alternativa más compleja debe demostrar una mejora, no suponerse mejor de antemano.
