# Sprint 3 - Despliegue local y documentación

## Objetivo
Implementar una prueba de despliegue local del modelo seleccionado y documentar los resultados del proyecto.

## Entregables técnicos evidenciados
- [x] Seleccionar Logistic Regression.
- [x] Guardar el modelo utilizando joblib.
- [x] Cargar el modelo entrenado.
- [x] Crear el módulo src/predict.py.
- [x] Ejecutar una predicción desde el notebook.
- [x] README.md preparado y publicado en el repositorio.
- [x] Ejecución del notebook y pruebas automatizadas confirmadas en Windows.
- [x] Roles y responsabilidades documentados para el equipo de tres personas.
- [x] Retrospectiva de aprendizajes documentada.
- [ ] Comprobación integral en macOS y ensayo grupal.

## Resultados obtenidos
- Modelo: Logistic Regression
- Accuracy: 91,95 %
- F1 Macro: 93,06 %
- Predicción de prueba: SEKER
- Valor real: SEKER
- Resultado: Predicción correcta

## Revisión de entregables
Se implementó una función reutilizable para realizar predicciones mediante un modelo previamente entrenado.

## Reflexión técnica
### ¿Qué funcionó?
La separación del código de predicción permitió organizar mejor el proyecto.

### ¿Qué dificultad se presentó?
Una dificultad que se abordó fue gestionar rutas de archivos de manera compatible con Jupyter.

### ¿Cómo se solucionó?
La predicción reutilizable se organizó en `src/predict.py` y las rutas se resuelven desde la raíz del proyecto.

### ¿Qué mejoraríamos?
Ampliar las pruebas a macOS y considerar evaluación adicional de estabilidad antes de una implementación real.

> Los roles ya se encuentran definidos en `scrum/roles_equipo.md`. El ensayo grupal y la reproducción completa en macOS permanecen pendientes.
