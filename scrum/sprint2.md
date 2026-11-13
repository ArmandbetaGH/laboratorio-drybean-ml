# Sprint 2 - Modelado y evaluación

## Objetivo

Entrenar, evaluar y comparar modelos de clasificación para identificar la variedad de fríjol a partir de características geométricas.

## Actividades realizadas

- [x] Entrenar Logistic Regression como modelo baseline.
- [x] Entrenar Random Forest como modelo alternativo.
- [x] Evaluar los modelos con Accuracy y F1 Macro.
- [x] Comparar resultados.
- [x] Generar matrices de confusión.
- [x] Analizar la importancia de variables.
- [x] Seleccionar un modelo candidato.

## Resultados

| Modelo | Accuracy | F1 Macro |
|---|---|---|
| Logistic Regression | 91,95 % | 93,06 % |
| Random Forest | 91,81 % | 92,92 % |

## Principales hallazgos

1. Ambos modelos obtuvieron un desempeño superior al 91 % en Accuracy.
2. Logistic Regression presentó resultados ligeramente superiores.
3. Las principales confusiones ocurrieron entre DERMASON y SIRA.
4. BOMBAY fue clasificada correctamente en todos los registros de prueba.
5. Las variables más importantes en Random Forest estuvieron relacionadas con el tamaño y la forma del grano.

## Decisión técnica

Se selecciona Logistic Regression como modelo candidato para el despliegue local debido a su desempeño ligeramente superior y su menor complejidad relativa.

## Sprint Review

Se completaron los experimentos de modelado y la evaluación comparativa.

Los resultados permiten avanzar a la etapa de despliegue local.

## Retrospectiva

### ¿Qué funcionó?
La preparación de los datos y la implementación de dos modelos permitieron obtener resultados satisfactorios.

### ¿Qué fue difícil?
Interpretar las métricas y comprender las confusiones entre las diferentes variedades de fríjol.

### ¿Qué mejoraríamos?
Realizar validación cruzada y evaluar configuraciones adicionales para comprobar la estabilidad de los resultados.

### ¿Qué aprendimos?
Que un modelo más complejo no necesariamente obtiene mejores resultados que uno más sencillo.

> Nota: los resultados están registrados en las salidas del notebook original; verificar advertencias numéricas antes de cerrar la reproducción.
