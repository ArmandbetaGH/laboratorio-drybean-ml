# Respuestas de estudio — siete reflexiones de la guía Lab1

Son propuestas razonadas a partir del caso y la evidencia disponible;
deben ser comprendidas, revisadas y explicadas por el equipo.

1. **¿Qué fase de CRISP-DM fue más importante?** La comprensión del
   negocio orienta el propósito y los indicadores. También es crucial la
   evaluación, porque permite decidir sin elegir modelos solo por complejidad.
   No existe una fase universalmente más importante fuera del contexto.

2. **¿Qué ofrece TDSP frente a archivos desordenados?** Separación clara
   entre datos, código, notebooks, modelos y evidencias; permite repetir,
   mantener y auditar los experimentos. Guardar el código no es suficiente
   si no se documentan datos, dependencias y decisiones.

3. **¿Cómo ayuda Scrum ML con resultados inciertos?** Permite organizar
   ciclos cortos, tareas y criterios verificables; el equipo puede revisar
   hallazgos y replantear experimentos sin asumir de antemano una métrica.
   Los roles y sprints aquí son **simulación académica** salvo evidencia real.

4. **¿Por qué un baseline?** Es un punto de comparación: permite comprobar
   si la complejidad de Random Forest compensa frente a la regresión logística.

5. **¿Qué métrica elegir y por qué?** F1 macro como criterio principal
   cuando interesa considerar todas las variedades. Accuracy es útil como
   resumen, pero puede ocultar errores concentrados en clases minoritarias.

6. **¿Qué hacer ante muchos errores en una clase?** Revisar soporte por
   clase y matriz de confusión, comprobar calidad/solapamiento de variables,
   evaluar el origen del dato y luego probar otros modelos o ajustes con
   validación adecuada. No garantizar mejoras antes de medir.

7. **¿Qué se necesitaría antes de producción?** Datos representativos de
   la operación, pruebas externas, análisis del costo de cada tipo de error,
   integración con la captura de medidas, seguridad, validación con usuarios,
   monitoreo y un plan de mantenimiento/reentrenamiento.
