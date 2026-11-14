# Ruta de sustentación - Laboratorio 1 Dry Bean

**Formato recomendado:** GitHub como pantalla principal. VS Code como apoyo para enseñar el notebook ejecutado y realizar una predicción local. **Duración objetivo: 11 minutos y 30 segundos**, con una distribución breve entre los tres integrantes. **La demostración se realizará sobre las evidencias del repositorio y el notebook.**

## Preparación antes de ingresar

- Tener abierto el repositorio privado en la rama `main`, con sesión iniciada y acceso autorizado.
- Tener abierto en VS Code `notebooks/01_laboratorio_drybean.ipynb`, kernel del `.venv`, resultados guardados y terminal lista. **No volver a entrenar durante la exposición**: puede consumir tiempo y crear diferencias; mostrar las salidas guardadas.
- Abrir con anticipación `docs/MAPA_RUBRICA_EVIDENCIAS.md`, `scrum/tablero.md` y las matrices PNG.
- Acordar los roles Scrum reales, actualizar la retrospectiva y las tareas verificables. La distribución oral siguiente **no sustituye** este acuerdo.
- Si hay dificultad de Internet o con GitHub, usar VS Code en local como respaldo.

## Secuencia propuesta de pantallas

| Momento | Quién | Pantalla / ruta | Qué debe demostrar |
|---|---|---|---|
| 0:00–1:20 | Armando | GitHub → `README.md` | Problema de negocio, objetivo de clasificación y límites del prototipo |
| 1:20–2:50 | Armando | GitHub → carpetas y `docs/crisp_dm/README.md` | Índice de seis fases CRISP-DM con sus evidencias; TDSP como orden técnico |
| 2:50–4:35 | Mónica | VS Code → notebook, celdas de carga, `df.info()`, nulos y duplicados | Dataset UCI, 13.611 filas, 17 columnas, siete clases y 68 duplicados |
| 4:35–6:05 | Mónica | VS Code → distribución y separación `train_test_split` | 13.543 filas limpias, desbalance, partición 80/20 estratificada, prevención de fuga de información |
| 6:05–8:30 | Andrés | VS Code → entrenamiento y tabla comparativa | Logistic Regression baseline, Random Forest alternativo, Accuracy y F1 macro |
| 8:30–9:40 | Andrés | GitHub → `outputs/reports/` | Matrices de confusión, errores entre DERMASON/SIRA y razones de selección |
| 9:40–10:10 | Andrés | VS Code → prueba de predicción local | Modelo `.joblib` cargado y predicción local; aclarar que un acierto no es la métrica general |
| 10:10–11:30 | Armando | GitHub → `scrum/`, Definition of Done y mapa de rúbrica | Backlog, sprints, estados verificables, criterios de terminado, aprendizajes y cierre |

> En caso de atrasos, priorizar **metodologías, evidencia y conclusiones**. El recorrido prioriza las metodologías, la evidencia técnica y las conclusiones sobre un nuevo entrenamiento en vivo.

## Guion de transiciones (una frase)

- **Armando → Mónica:** «Con el problema y la estructura definidos, Mónica explicará qué datos encontramos y cómo los preparamos».
- **Mónica → Andrés:** «Con el conjunto listo para el entrenamiento, Andrés nos mostrará cómo comparamos los dos modelos».
- **Andrés → Armando:** «Finalmente, mostraremos cómo documentamos la gestión del trabajo y verificamos que la práctica quedó reproducible».

## Cinco preguntas para ensayar

1. **¿Qué aporta CRISP-DM frente a escribir código directamente?** Organiza la secuencia del problema, los datos, los modelos, la evaluación y la inferencia.
2. **¿Qué aporta TDSP?** Evidencias organizadas, control de versiones, reproducibilidad y separación de responsabilidades del código.
3. **¿Qué aporta Scrum ML?** Priorización, entregables incrementales, responsables y criterios de terminado; no afirmar ceremonias que no ocurrieron.
4. **¿Por qué F1 macro si ya existe Accuracy?** Porque promedia F1 por clase dando igual peso a cada variedad, incluso a las menos frecuentes.
5. **¿Por qué elegir el baseline?** En la evaluación registrada obtuvo una ventaja pequeña sobre Random Forest, con menor complejidad; no implica superioridad definitiva.

## Evidencias que deben estar a mano

- `README.md` y `docs/crisp_dm/01_comprension_negocio.md`.
- `notebooks/01_laboratorio_drybean.ipynb` con salidas guardadas.
- `outputs/reports/matriz_logistic_regression.png` y `matriz_random_forest.png`.
- `scrum/backlog.md`, `scrum/tablero.md`, `scrum/sprint1.md`–`sprint3.md`, `scrum/definition_of_done.md`, `scrum/retrospectiva.md`.
- `docs/MAPA_RUBRICA_EVIDENCIAS.md`.
- Script para la predicción local: `scripts/verificar_modelo_guardado.py`.

**No confundir:** el equipo confirmó la ejecución completa del notebook y 7 pruebas aprobadas **en Windows**. La ejecución en Mac permanece por verificar. Los roles Scrum siguen sujetos al acuerdo entre los tres.
