# Fase 3 — Preparación de los datos

**Pregunta que responde:** ¿cómo transformamos los datos para que puedan usarse en el modelado?

**Proceso observado:** eliminación de 68 filas idénticas, con **13.543 registros finales**; separación de entradas `X` y objetivo `y`; partición **80 % entrenamiento / 20 % prueba**, estratificada, con semilla 42. La regresión logística usa escalamiento dentro del `Pipeline`.

**Evidencia:** [datos procesados](../../../data/processed/drybean_clean.csv) y [notebook](../../../notebooks/01_laboratorio_drybean.ipynb).

**Para explicar:** por qué eliminar duplicados antes de dividir, qué significa `stratify=y`, y por qué el escalador se ajusta solamente con el entrenamiento para evitar fuga de información.
