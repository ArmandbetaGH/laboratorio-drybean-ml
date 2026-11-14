# Retrospectiva del Laboratorio 1 — Scrum ML

Esta retrospectiva recoge **aprendizajes y dificultades verificables del desarrollo del laboratorio**. Es un balance documental del trabajo y no pretende hacer constar una ceremonia o reunión de Scrum cuya realización no haya sido registrada.

## 1. ¿Qué funcionó?

- **Organización y trazabilidad:** el repositorio GitHub permitió versionar el notebook, la documentación y los resultados; se distinguieron código, datos procesados, pruebas y modelos.
- **Proceso metodológico:** CRISP-DM orientó las seis fases; TDSP aportó estructura y reproducibilidad, y Scrum ML permitió identificar tareas, entregables y responsabilidades.
- **Comprobaciones técnicas en Windows:** el notebook se ejecutó de principio a fin, las **7 pruebas automatizadas** pasaron y el modelo `.joblib` se cargó y produjo una predicción local.
- **Comparación de modelos:** se entrenaron Logistic Regression y Random Forest, comparando Accuracy, F1 macro y matrices de confusión.

## 2. ¿Qué dificultades se presentaron?

- **Configuración del entorno Jupyter:** inicialmente VS Code no iniciaba el kernel esperado; fue necesario identificar el entorno `.venv`, registrar `ipykernel` y ejecutar las celdas en orden.
- **Dependencia del estado del kernel:** al ejecutar celdas de forma aislada, aparecieron errores de variables no definidas (`X_train`, `baseline_model`). Se solucionaron con una ejecución secuencial completa.
- **Consistencia documental:** se detectaron enlaces a archivos retirados, indicaciones internas mezcladas con la entrega académica y estados que requerían actualización.
- **Trabajo multiplataforma:** la ejecución en Windows está comprobada, pero no hay constancia todavía de la ejecución integral en macOS.

## 3. ¿Qué mejoraríamos?

- Acordar y publicar desde el comienzo los responsables funcionales y los criterios de aceptación de cada tarea.
- Actualizar el tablero y los documentos al mismo tiempo que los cambios técnicos para evitar información desactualizada.
- Comprobar la reproducibilidad también en macOS, usando el archivo `requirements.txt` y el entorno virtual del proyecto.
- En una siguiente iteración, estudiar validación cruzada y análisis de estabilidad para no depender únicamente de una partición train/test.

## 4. Aprendizajes

El trabajo evidenció que **un proyecto de Machine Learning no termina al entrenar un modelo**: también requiere validar el dato, justificar las métricas, reproducir resultados, guardar artefactos y mantener una documentación coherente. Un modelo más complejo no necesariamente supera al baseline.

## 5. Acciones de mejora y seguimiento

| Acción | Responsable funcional | Situación |
|---|---|---|
| Mantener roles y backlog actualizados | Armando — Scrum Master / TDSP | Roles definidos; mantenimiento continuo |
| Revisar la claridad de las conclusiones y criterios de aceptación | Mónica — Product Owner / Data Analyst | Material documental disponible; revisión conjunta aún por realizar |
| Comprobar inferencia y métricas en un segundo entorno | Andrés — ML Engineer, con apoyo del equipo | Windows validado; macOS pendiente |
| Realizar ensayo de sustentación con los tres integrantes | Equipo | Pendiente |

**Alcance:** el presente documento registra aprendizajes del desarrollo. No presupone que los tres integrantes hayan asistido a una reunión de retrospectiva formal.
