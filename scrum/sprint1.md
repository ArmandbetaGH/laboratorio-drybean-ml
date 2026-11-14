# Sprint 1 - Comprensión y preparación de datos

## Objetivo
Comprender, limpiar y preparar el Dry Bean Dataset para el entrenamiento de modelos de clasificación.

## Entregables técnicos evidenciados

- [x] Crear estructura del proyecto.
- [x] Configurar entorno virtual.
- [x] Descargar dataset Dry Bean desde UCI.
- [x] Realizar análisis exploratorio.
- [x] Revisar valores nulos y duplicados.
- [x] Analizar distribución de clases.
- [x] Eliminar registros duplicados.
- [x] Separar variables predictoras y objetivo.
- [x] Separar datos de entrenamiento y prueba.
- [x] Guardar dataset procesado.

## Resultados obtenidos

- Registros originales: 13.611
- Registros duplicados: 68
- Registros después de limpieza: 13.543
- Variables predictoras: 16
- Variable objetivo: Class
- Columnas totales: 17

## Decisión técnica

Se eliminaron 68 registros duplicados para evitar que observaciones idénticas influyan repetidamente en el entrenamiento.

Se utilizó una división de entrenamiento y prueba del 80% y 20%, respectivamente, con una semilla fija para garantizar reproducibilidad.

## Revisión de entregables

Se completó la preparación inicial del conjunto de datos, dejándolo listo para comenzar la fase de modelado.

> Las evidencias describen productos técnicos; la revisión grupal y los acuerdos de Scrum se documentan por separado.
