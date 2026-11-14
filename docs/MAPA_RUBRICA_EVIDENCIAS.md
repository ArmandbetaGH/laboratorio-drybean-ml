# Mapa de evidencias de la rúbrica - Laboratorio 1

Fuente: `Lab1(1).pdf`, sección *Rúbrica de evaluación*, p. 16, y *Definition of Done*, p. 16. Las ubicaciones se refieren a este repositorio, no a resultados nuevos.

| Criterio | Peso | Evidencia verificable | Verificación antes de entregar |
|---|---:|---|---|
| CRISP-DM | 20 | Notebook: comprensión de negocio, EDA, preparación, modelos, evaluación, despliegue local; `docs/crisp_dm/`; `docs/crisp_dm/05_sintesis_final.md` | Revisar que las seis fases estén explicadas y demostrables |
| TDSP | 15 | `data/`, `notebooks/`, `src/`, `outputs/`, `requirements.txt`, `README.md`, historial GitHub | Confirmar rutas, dependencias y acceso para el equipo |
| Scrum ML | 15 | `scrum/backlog.md`, `scrum/tablero.md`, `scrum/sprint1.md`-`sprint3.md`, `scrum/definition_of_done.md`, `scrum/roles_equipo.md`, `scrum/retrospectiva.md` | Confirmar roles reales, fechas y revisión auténtica |
| Código reproducible | 20 | Notebook, `src/predict.py`, scripts de calidad y pruebas `tests/` | Ejecución completa y carga `.joblib` confirmadas en Windows; repetir en Mac |
| Evaluación del modelo | 15 | Notebook: Accuracy, F1 macro, classification_report, matriz de confusión; `outputs/reports/*.png` | Contrastar métricas de la ejecución y versiones; interpretar errores |
| Interpretación/conclusiones | 15 | `docs/crisp_dm/03_reflexiones_guia.md`, `docs/crisp_dm/05_sintesis_final.md`, guía de estudio | Sustentar por qué se elige el baseline y límites del prototipo |

## Checklist de Definition of Done del profesor (9 criterios)

- [x] El equipo confirmó que el notebook corre de principio a fin sin errores en Windows. Queda por verificar Mac.
- [ ] El dataset se descarga o carga desde UCI, o se utiliza la copia original verificable, con su procedencia declarada.
- [x] Se reportan nulos y duplicados en el notebook. Comprobar de nuevo al ejecutar.
- [x] Se documentan baseline (Logistic Regression) y alternativo (Random Forest).
- [x] Se documentan Accuracy y F1 macro para ambos.
- [x] Hay matrices de confusión de ambos modelos.
- [x] Existe un artefacto `.joblib` del candidato; **carga y predicción verificadas en Windows** con sklearn 1.6.1.
- [x] Existen interpretaciones en lenguaje accesible.
- [ ] Equipo valida explícitamente relación con CRISP-DM, TDSP y Scrum ML y su retrospectiva real.

`[x]` refleja archivo/salida y, cuando se indica, comprobación en Windows; **no implica validación en Mac**. Los sprints y roles deben representar decisiones y hechos confirmados.
