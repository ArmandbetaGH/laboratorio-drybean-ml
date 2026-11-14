# Síntesis del proyecto según CRISP-DM

## 1. Comprensión del negocio
El caso simula una empresa agrícola que busca apoyar la identificación de variedades de frijol seco. El objetivo técnico es clasificar siete variedades a partir de 16 características geométricas; no se midieron beneficios operativos reales.

## 2. Comprensión de los datos
El Dry Bean Dataset de UCI (ID 602) contiene 13.611 registros, 16 variables predictoras numéricas y una categoría objetivo (`Class`). Se observaron cero nulos y 68 duplicados exactos.

## 3. Preparación
Se eliminaron duplicados (13.543 filas finales), se separaron variables predictoras y objetivo y se realizó una partición 80/20 estratificada con `random_state=42`. El escalamiento de regresión logística está dentro del `Pipeline`, ajustado solo con entrenamiento.

## 4. Modelado
Se entrenaron regresión logística como modelo base y Random Forest (200 árboles, `class_weight="balanced"`) como alternativa.

## 5. Evaluación

| Modelo | Accuracy | F1 macro |
|---|---:|---:|
| Logistic Regression | 91,95 % | 93,06 % |
| Random Forest | 91,81 % | 92,92 % |

Las cifras son las registradas en el notebook. Regresión logística es el candidato por su pequeña ventaja y menor complejidad. Las matrices evidencian confusiones entre DERMASON y SIRA. No se infiere superioridad estadística concluyente a partir de una única partición.

## 6. Despliegue local
El modelo seleccionado se guarda en formato `.joblib` y puede recuperarse para predecir una nueva observación con las 16 variables requeridas. La inferencia local fue comprobada en Windows; no se desarrolló una API ni un sistema en producción.

## Limitaciones
- No existe validación externa con muestras de una operación agrícola real.
- La reproducción en macOS permanece por comprobar.
- Validación cruzada y ajuste de hiperparámetros se consideran extensiones futuras, no resultados de este ejercicio.
