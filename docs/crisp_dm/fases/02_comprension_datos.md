# Fase 2 — Comprensión de los datos

**Pregunta que responde:** ¿qué datos existen y qué calidad tienen?

**Fuente:** Dry Bean Dataset, UCI (ID 602). Original: **13.611 registros**, **16 variables predictoras**, **una variable objetivo (`Class`)**, **siete clases**. En la exploración se observaron **cero nulos** y **68 duplicados exactos**.

**Evidencia:** [guía de estudio de la fase 2](../04_estudio_fase_2.md), [notebook](../../../notebooks/01_laboratorio_drybean.ipynb) y [reporte de calidad de datos procesados](../../../outputs/reports/calidad_datos_procesados.json).

**Para explicar:** `df.shape`, `df.info()`, `df.describe()`, `isna()`, `duplicated()` y distribución de clases. El reporte JSON describe **datos limpios**, no el archivo original.
