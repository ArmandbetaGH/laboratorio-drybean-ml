"""Predicción local del modelo seleccionado en el laboratorio Dry Bean.

Precaución: joblib usa el mecanismo de serialización pickle; cargar únicamente
modelos de origen confiable y preferentemente con la misma versión de sklearn.
"""
from pathlib import Path
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "outputs" / "models" / "logistic_regression_drybean.joblib"

def predict_bean_class(input_data: pd.DataFrame) -> str:
    """Predice la variedad para la primera observación de un DataFrame."""
    if not isinstance(input_data, pd.DataFrame):
        raise TypeError("Los datos deben ser un DataFrame de pandas")
    if input_data.empty:
        raise ValueError("El DataFrame debe contener al menos una fila")
    if not MODEL_PATH.is_file():
        raise FileNotFoundError(f"No existe el modelo: {MODEL_PATH}")
    # Mantener el formato de entrada según el notebook: 16 variables geométricas.
    model = joblib.load(MODEL_PATH)
    expected = getattr(model, "feature_names_in_", None)
    if expected is not None:
        received = list(input_data.columns)
        if received != list(expected):
            raise ValueError("Las columnas deben coincidir en nombre y orden con las del entrenamiento")
    return str(model.predict(input_data)[0])
