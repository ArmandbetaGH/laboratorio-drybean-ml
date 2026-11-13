# Guía de estudio — CRISP-DM fase 2: comprensión de los datos

Material de aprendizaje basado en el notebook existente y el CSV procesado,
conservando las salidas históricas de la entrega. **No es una nueva ejecución
completa del notebook desde UCI.**

## Propósito
Antes de entrenar un modelo debemos conocer el origen de la información, las
variables, tipos, integridad y distribución de las clases. Esta fase responde:
¿qué tenemos?, ¿cuál es su calidad? y ¿qué riesgos puede introducir en el modelo?

## Paso A. Origen y carga — celda 3
`fetch_ucirepo(id=602)` solicita a UCI el Dry Bean Dataset. Las variables
predictoras (`features`) se guardan en `X`; la clase (`targets`) en `y`.
`pd.concat([X, y], axis=1)` reúne ambas partes en una tabla para estudiarlas.

**Dato del material del profesor:** 13.611 instancias originales, 16 variables
predictoras y una clase objetivo `Class`, es decir 17 columnas en total.
Para ejecutar esta celda es necesaria la descarga desde la fuente.

## Paso B. Descripción inicial — celdas 5 y 7
- `df.shape`: número de filas y columnas.
- `df.info()`: nombres, tipos y valores no nulos.
- `df.describe()`: resumen estadístico de variables numéricas.
- `df['Class'].unique()`: etiquetas de las siete variedades.

**Razón:** debemos comprobar que estamos usando una clasificación de siete
clases y que las 16 entradas son características geométricas, no imágenes.

## Paso C. Calidad — celda 8
- `df.isna().sum()` cuenta los nulos por columna.
- `df.duplicated().sum()` cuenta filas idénticas.

La salida histórica registra **0 valores faltantes y 68 filas duplicadas**
en el conjunto original. La decisión de eliminar duplicados se implementa
más adelante, en la fase 3 (preparación, celda 12).

## Paso D. Distribución de la variable objetivo — celda 10
`df['Class'].value_counts()` cuenta las observaciones de cada variedad; la
gráfica permite comparar visualmente las clases. Esto importa porque Accuracy
puede ocultar rendimientos pobres en clases minoritarias. Por ese motivo la
guía también pide F1 macro (cada clase pesa lo mismo en el promedio).

## Paso E. Resultado de la limpieza (fase 3, para contraste)
Se comprobó **directamente** el archivo `data/processed/drybean_clean.csv`:

| Clase | Registros en el CSV procesado |
|---|---:|
| DERMASON | 3.546 |
| SIRA | 2.636 |
| SEKER | 2.027 |
| HOROZ | 1.860 |
| CALI | 1.630 |
| BARBUNYA | 1.322 |
| BOMBAY | 522 |
| **Total** | **13.543** |

Tiene 17 columnas, 0 nulos y 0 filas duplicadas según la revisión.
La clase mayoritaria es DERMASON y la minoritaria es BOMBAY; por tanto, el
conjunto no tiene una distribución uniforme de clases.

## Preguntas de estudio antes de avanzar
1. ¿Por qué `Class` es la variable que queremos predecir y no una entrada del modelo?
2. ¿Qué diferencia hay entre 16 características y 17 columnas?
3. ¿Qué riesgo existe si una misma observación está tanto en entrenamiento como en prueba?
4. ¿Por qué necesitamos revisar F1 macro además de Accuracy?

## Evidencia que debemos presentar
Notebook con las celdas de exploración, reporte de nulos y duplicados,
distribución de clases y una interpretación breve de los resultados.
El equipo debe reejecutar y corroborar las salidas del notebook en sus equipos.
