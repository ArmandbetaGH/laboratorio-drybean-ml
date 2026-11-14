# Registro de revisión técnica

## Verificaciones del proyecto

- Repositorio con estructura TDSP, versiones y documentación.
- Ejecución integral del notebook confirmada en Windows.
- Siete pruebas automáticas aprobadas en Windows.
- Reportes de calidad generados desde el conjunto procesado.
- Modelo de regresión logística cargado en Windows con `scikit-learn 1.6.1`; predicción individual SEKER coincidente con su etiqueta.
- Ejecución independiente de referencia conservada en [`reproduccion_desde_csv.json`](reproduccion_desde_csv.json). Sus versiones y cifras no deben mezclarse con las del notebook principal.

## Pendientes de trabajo

- [ ] Verificar la portabilidad completa en macOS.
- [ ] Registrar roles, responsables y retrospectiva acordados por el equipo.
- [ ] Verificar que las métricas presentadas correspondan a las salidas guardadas de la ejecución vigente.
- [ ] Conservar archivo original de UCI en `data/raw/`, si se requiere respaldo reproducible sin conexión.
- [ ] Ensayar la demostración con GitHub y VS Code.

**Alcance:** las pruebas técnicas no acreditan ceremonias Scrum realizadas ni desempeño en una empresa agrícola real. Los documentos de Scrum describen el plan y el estado de los entregables; las reuniones y responsabilidades personales deberán reflejar acuerdos auténticos.
