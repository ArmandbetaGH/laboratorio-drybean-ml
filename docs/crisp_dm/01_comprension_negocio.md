# CRISP-DM — Fase 1: Comprensión del negocio

## Contexto del proyecto (caso simulado)
Una empresa agrícola realiza parcialmente una clasificación manual de
variedades de frijol y desea estudiar si el reconocimiento automático de
variedades podría apoyar el control de calidad.

## Problema de negocio
Se requiere **apoyar** la identificación de variedades de frijol de forma
consistente. El enunciado no cuantifica errores manuales, costos, tiempos
ni volumen operativo: no asumimos esas cifras ni aseguramos mejoras reales.

## Objetivo general del prototipo
Construir y evaluar un clasificador multiclase a partir de **16 variables
geométricas ya extraídas de imágenes**, comparando un modelo base y una
alternativa para establecer su desempeño técnico y documentar una prueba
local de inferencia.

## Usuarios y partes interesadas potenciales (supuestos)
- Operador o analista de calidad agrícola: potencial usuario de la predicción.
- Responsable del proceso de clasificación: potencial decisor sobre el uso.
- Equipo académico de datos: desarrolla y evalúa el prototipo.
Estos roles son **hipotéticos**; no representan entrevistas ni validaciones.

## Pregunta de negocio
¿Puede un modelo basado en características geométricas contribuir a
identificar las siete variedades y qué tipos de errores presenta?

## Objetivo de Machine Learning
Entrenar algoritmos supervisados de **clasificación multiclase** para
predecir `Class` usando 16 características numéricas (`X`).

## Criterios para evaluar el prototipo
- **F1 macro** como criterio técnico principal porque considera por igual
  el F1 de cada una de las siete variedades, independientemente de su tamaño.
- **Accuracy** como indicador complementario de aciertos globales.
- **Matriz de confusión** para localizar variedades con errores frecuentes.
- **Baseline** de regresión logística y alternativa Random Forest.
- **Reproducibilidad:** partición train/test estratificada, semilla fijada,
  documentación de versiones y modelo guardado para inferencia local.

No se definió umbral contractual mínimo para aprobar el modelo, ni un KPI
empresarial medido. Por ello, un F1 alto sería evidencia de desempeño
**técnico**, no de beneficios operativos realizados.

## Entregables y límites
Artefactos: notebook, exploración/limpieza, evaluación comparativa,
matrices de confusión, modelo guardado, prueba local, repositorio y evidencia
de CRISP-DM/TDSP/Scrum ML. **Fuera de alcance del Laboratorio 1**: integrar
cámaras reales, construir una API, Docker, monitoreo continuo o una
solución de control de calidad desplegada en una empresa.

## Riesgos y supuestos
- El dataset de UCI representa el caso de estudio; no hay prueba de que
  represente todas las variedades o condiciones de una operación real.
- El clasificador recibe mediciones, **no imágenes**.
- Una buena puntuación en una partición no asegura generalización fuera
  de muestra, estabilidad temporal o impacto operativo.
- Las muestras y sus etiquetas provienen del repositorio académico.
