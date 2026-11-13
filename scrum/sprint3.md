# Sprint 3 - Despliegue local y documentación

## Objetivo
Implementar una prueba de despliegue local del modelo seleccionado y documentar los resultados del proyecto.

## Actividades realizadas
- [x] Seleccionar Logistic Regression.
- [x] Guardar el modelo utilizando joblib.
- [x] Cargar el modelo entrenado.
- [x] Crear el módulo src/predict.py.
- [x] Ejecutar una predicción desde el notebook.
- [x] README.md disponible; actualización editorial en copia revisada.
- [ ] Equipo debe validar las evidencias finales y la ejecución en su propio entorno.

## Resultados obtenidos
- Modelo: Logistic Regression
- Accuracy: 91,95 %
- F1 Macro: 93,06 %
- Predicción de prueba: SEKER
- Valor real: SEKER
- Resultado: Predicción correcta

## Sprint Review
Se implementó una función reutilizable para realizar predicciones mediante un modelo previamente entrenado.

## Retrospectiva
### ¿Qué funcionó?
La separación del código de predicción permitió organizar mejor el proyecto.

### ¿Qué dificultad se presentó?
Durante la implementación apareció un error relacionado con el uso de __file__ dentro de Jupyter Notebook.

### ¿Cómo se solucionó?
Se trasladó el código reutilizable a src/predict.py y se importó desde el notebook.

### ¿Qué mejoraríamos?
Implementar pruebas automatizadas y revisar la estabilidad numérica del entrenamiento antes de una implementación real.

> Nota: la revisión del README es documental; la socialización y validación del equipo siguen pendientes.
