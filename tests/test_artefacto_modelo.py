"""Prueba de inferencia del artefacto original de origen conocido."""
from pathlib import Path
import sys
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.predict import predict_bean_class


def test_modelo_guardado_predice_clase_conocida():
    tabla=pd.read_csv(ROOT/'data'/'processed'/'drybean_clean.csv')
    X=tabla.drop(columns=['Class']).iloc[[0]]
    etiqueta=predict_bean_class(X)
    assert isinstance(etiqueta,str)
    assert etiqueta in set(tabla['Class'])
