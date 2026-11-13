# GUIÓN DE SUSTENTACIÓN - 11 a 12 minutos

**Presentan:** Armando, Mónica Giraldo y Andrés Hernández.  
**Formato:** recorrer GitHub/VS Code y mostrar evidencias; no se requieren diapositivas.  
**Carácter:** distribución propuesta de intervención, **no atribución de autoría o roles Scrum**. Ajustar nombres y responsabilidades si el equipo lo decide.

## 0:00-2:50 - Armando | Introducción, negocio y gestión
**Mostrar:** `README.md`, `docs/crisp_dm/01_comprension_negocio.md`, `docs/MAPA_RUBRICA_EVIDENCIAS.md` y carpetas del repositorio.

> Buenas tardes, profesor. Somos el equipo integrado por Mónica Giraldo, Andrés Hernández y Armando. Presentamos el Laboratorio 1 de clasificación de variedades de frijol usando CRISP-DM, TDSP y Scrum ML. El caso plantea una empresa agrícola que busca apoyar una clasificación parcialmente manual. Nuestro objetivo técnico es determinar la variedad del grano a partir de 16 medidas geométricas, no procesar directamente las imágenes ni afirmar mejoras reales de costos.
>
> Aplicamos CRISP-DM como secuencia de seis fases: negocio, datos, preparación, modelado, evaluación y despliegue local. TDSP orienta la estructura y reproducibilidad: vemos carpetas diferenciadas para datos, notebooks, código, resultados, pruebas y documentación. Centralizamos todo en GitHub para versionar cambios y facilitar la colaboración entre Windows y Mac.
>
> En Scrum ML usamos un Product Backlog, un tablero de estados, criterios de terminado y tres sprints documentados: primero preparación, después modelado y finalmente inferencia y documentación. Estos archivos son el marco de gestión de la práctica. Las responsabilidades y las reuniones efectivamente realizadas se indicarán según la evidencia que confirme el equipo. Ahora Mónica explicará los datos.

**Transición:** «Mónica, cuéntanos qué encontramos al explorar y preparar el dataset».

## 2:50-6:05 - Mónica Giraldo | Comprensión y preparación de datos
**Mostrar:** notebook en Actividad 1, `df.info()`, `df.describe()`, nulos/duplicados, gráfico de clases y train/test; opcional `outputs/reports/distribucion_clases_procesadas.csv`.

> Trabajamos con el Dry Bean Dataset, disponible en UCI. El conjunto original contiene 13.611 registros y 17 columnas: 16 características geométricas y una etiqueta, `Class`, con siete variedades. Estamos frente a un problema supervisado de clasificación multiclase.
>
> En la comprensión inicial inspeccionamos dimensiones, tipos y estadísticas descriptivas; además contamos valores nulos, registros duplicados y distribución de clases. En las salidas originales no se reportaron nulos y se identificaron 68 filas duplicadas. Tras eliminarlas, el conjunto procesado contiene 13.543 observaciones. Esta eliminación ayuda a evitar que una misma fila aparezca tanto en entrenamiento como en prueba.
>
> Detectamos desbalance: DERMASON tiene 3.546 ejemplos en el conjunto limpio y BOMBAY 522. Por eso no nos limitamos a Accuracy; usaremos también F1 macro para dar importancia a cada variedad. Después separamos X, nuestras 16 variables de entrada, de y, la variedad real. Hicimos partición 80/20 estratificada con semilla 42: 10.834 datos para entrenamiento y 2.709 para prueba. El escalamiento de regresión logística se hace dentro de un Pipeline, para ajustarse solo con entrenamiento y evitar fuga de información.
>
> Esta fase deja un dataset procesado, el notebook explicativo y reportes de calidad reproducibles.

**Transición:** «Andrés nos mostrará qué modelos probamos y qué evidencian las métricas».

## 6:05-10:10 - Andrés Hernández | Modelos, evaluación, demo local
**Mostrar:** celdas de Logistic Regression y Random Forest, tabla comparativa, matrices PNG, importancia de variables y celdas de joblib.

> Entrenamos dos algoritmos. La regresión logística es el baseline, es decir, el punto de comparación; usa un escalador y un clasificador dentro de un Pipeline. Random Forest es la alternativa, entrenada con 200 árboles y pesos de clase balanceados. Un algoritmo más complejo no necesariamente tiene mejor desempeño.
>
> En las salidas históricas del notebook, regresión logística obtuvo Accuracy de 91,95 % y F1 macro de 93,06 %. Random Forest obtuvo Accuracy de 91,81 % y F1 macro de 92,92 %. Priorizamos F1 macro y revisamos también las matrices de confusión. Se observan confusiones especialmente entre DERMASON y SIRA. La regresión logística queda como candidata porque supera ligeramente al Random Forest y es relativamente más sencilla, sin afirmar que esa diferencia sea concluyente fuera de esta partición.
>
> Para la etapa de despliegue local guardamos el modelo con joblib, lo cargamos de nuevo y realizamos una predicción sobre una muestra de prueba. La función `src/predict.py` permite reutilizar este comportamiento, siempre con las 16 columnas esperadas. Es una demo local reproducible, no una API ni un sistema desplegado en producción.
>
> Los resultados son prometedores para el ejercicio académico, pero antes de producción sería necesario validar con nuevos datos y con el proceso real de la empresa.

**Transición:** «Armando cerrará con evidencias metodológicas y aprendizajes».

## 10:10-11:30 - Armando | Cierre
**Mostrar:** `scrum/definition_of_done.md`, `scrum/retrospectiva.md`, `docs/VALIDACION_FINAL.md`.

> Como conclusión, CRISP-DM nos permitió estructurar las decisiones, TDSP mantener un repositorio ordenado y Scrum ML visibilizar tareas, responsables y entregables. Lo importante no fue buscar un número alto sin explicación, sino poder demostrar de dónde vienen los datos, qué se hizo con ellos, por qué se compararon dos modelos y cómo reutilizar el elegido. Antes del cierre final validaremos la ejecución integral del notebook, la carga del modelo en nuestro entorno y los acuerdos reales del equipo. Muchas gracias; quedamos atentos a las preguntas.

## Ruta de pantallas recomendada
1. Inicio: README y carpetas principales.
2. `docs/crisp_dm/01_comprension_negocio.md`.
3. Notebook: importaciones, EDA y limpieza.
4. Notebook: train/test, baseline y Random Forest.
5. Notebook: comparación y matrices de confusión.
6. Notebook: joblib y `src/predict.py`.
7. `scrum/` y mapa de rúbrica.

## Cuidados antes de presentar
- Si ya ejecutaron íntegramente el notebook y validaron los sprints, actualizar las frases «pendiente» por hechos confirmados.
- Si la ejecución arroja métricas ligeramente distintas, usar las de esa ejecución y registrar versiones; no mezclar cifras históricas.
- Si alguien pregunta quién fue Product Owner o Scrum Master, decir solo lo acordado y documentado por el equipo, nunca inventarlo.
- Ensayar una vez con cronómetro: total propuesto 11 min 30 s. Cada integrante debe saber navegar su bloque.
