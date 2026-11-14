# Fase 5 — Evaluación

**Pregunta que responde:** ¿qué modelo cumple mejor el objetivo técnico y dónde se equivoca?

**Resultados registrados en el notebook:**

| Modelo | Accuracy | F1 macro |
|---|---:|---:|
| Logistic Regression | 91,95 % | 93,06 % |
| Random Forest | 91,81 % | 92,92 % |

Se propone la regresión logística como candidato por ventaja marginal y simplicidad, sin afirmar que su superioridad sea estadísticamente definitiva. Se observaron confusiones entre DERMASON y SIRA.

**Evidencia:** [matriz logística](../../../outputs/reports/matriz_logistic_regression.png), [matriz Random Forest](../../../outputs/reports/matriz_random_forest.png), [notebook](../../../notebooks/01_laboratorio_drybean.ipynb).

**Para explicar:** diferencias entre Accuracy y F1 macro, y qué muestra una matriz de confusión.
