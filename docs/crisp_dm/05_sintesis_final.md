# Síntesis y decisiones - seis fases CRISP-DM

## 1. Comprensión del negocio
La empresa agrícola simulada busca apoyar la identificación de variedades de frijol seco. No existen pruebas reales de ahorro, tiempo o calidad de producción. Objetivo técnico: clasificar siete variedades a partir de 16 rasgos geométricos.

## 2. Comprensión de los datos
Fuente UCI Dry Bean Dataset ID 602: 13.611 instancias, 17 columnas (16 numéricas y `Class`). El notebook original registró cero nulos y 68 registros duplicados. La distribución es desigual: DERMASON 3.546 registros limpios frente a BOMBAY 522.

## 3. Preparación de datos
Eliminar duplicados exactos (13.543 filas), separar `X` y `y`, y particionar train/test 80/20 con semilla 42 y estratificación. Para la regresión logística el escalamiento ocurre dentro de un `Pipeline` ajustado sobre entrenamiento; evita fuga de información del conjunto de prueba.

## 4. Modelado
Regresión logística con StandardScaler es baseline. Random Forest es alternativa con 200 árboles y pesos por clase balanceados. No se debe deducir de antemano que el modelo complejo será superior.

## 5. Evaluación
Las salidas históricas del notebook registran Logistic Regression Accuracy 91,95 %, F1 macro 93,06 % y Random Forest Accuracy 91,81 %, F1 macro 92,92 %. Se propone el baseline por desempeño ligeramente mejor y simplicidad. El resultado depende del conjunto de prueba, versiones y configuración; no demuestra rendimiento operativo real.

## 6. Despliegue local
Se guarda un modelo `.joblib`, se vuelve a cargar y se usa una muestra de prueba para inferencia. Esto constituye una demo local (no API ni producción). `src/predict.py` encapsula la predicción. Los `.joblib` se cargan solo desde fuentes confiables.

## Limitaciones y siguientes pasos
- El notebook ha sido ejecutado parcialmente en Windows por el equipo; falta comprobación completa de principio a fin.
- La versión de sklearn declarada es 1.6.1; revalidar el artefacto con esta versión al presentarlo.
- No tenemos una evaluación externa ni mediciones empresariales.
- Validación cruzada e hiperparámetros son extensiones opcionales en la guía del profesor.
