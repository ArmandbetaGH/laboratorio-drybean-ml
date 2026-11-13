# CRISP-DM — Mapa de evidencias de las seis fases

Estado documentado a partir de los **archivos aportados**, no de una
ejecución íntegra verificada en la máquina del estudiante.

| Fase | Evidencia verificable | Decisión / límite |
|---|---|---|
| 1. Comprensión del negocio | `docs/crisp_dm/01_comprension_negocio.md` | Beneficio organizacional hipotético; sin KPI operativo medido. |
| 2. Comprensión de los datos | Celdas 3–10 y nota interpretativa del notebook; `outputs/reports/calidad_datos_procesados.json` | Original: 13.611 filas, 17 columnas, siete clases, cero nulos, 68 duplicados. Reporte complementario sobre CSV limpio: 13.543 filas, cero duplicados. |
| 3. Preparación | Celdas 12–15 y `data/processed/drybean_clean.csv` | Elimina duplicados; 13.543 filas, `train_test_split` 80/20 estratificado. |
| 4. Modelado | Celdas 16–21 del notebook | Regresión logística estandarizada y Random Forest; registros de ajustes guardados. |
| 5. Evaluación | Celdas 22–32 y `outputs/reports/` | Accuracy y F1 macro, matrices y errores DERMASON/SIRA; modelo candidato Logistic Regression. |
| 6. Despliegue (local) | Celdas 33–36, `src/predict.py`, `outputs/models/` | Guarda, vuelve a cargar y utiliza un modelo en el notebook original. No hay API. |

**Advertencias:** las salidas guardadas del notebook reportan avisos
`RuntimeWarning` en el entrenamiento de regresión logística.
`data/raw/` sigue sin archivo original; para reproducir el notebook desde
su primera celda se necesita acceder a UCI. Las cifras de las salidas
son las reportadas por el experimento del compañero.

## Qué se interpreta de las métricas
- **Accuracy:** proporción de aciertos totales.
- **F1 macro:** promedio simple del F1 de cada clase, útil para no dar
  un peso mayor automáticamente a las variedades más numerosas.
- **Matriz de confusión:** clases reales por filas frente a predichas
  por columnas; permite identificar parejas que se confunden.
- **Importancia de variables (Random Forest):** relevancia predictiva en
  el algoritmo entrenado; no demuestra causalidad.

## Verificación final recomendada
Re-ejecutar con entorno limpio y conexión, revisar advertencias y
coherencia entre notebooks, gráficas, README, modelo y tablero Scrum.
