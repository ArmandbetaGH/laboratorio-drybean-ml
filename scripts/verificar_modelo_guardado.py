"""Verifica la inferencia del `.joblib` confiable incluido en el proyecto.

Usar con scikit-learn==1.6.1, versión original del artefacto.
"""
from pathlib import Path
import sys
import pandas as pd
import sklearn

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.predict import predict_bean_class


def main():
    data=pd.read_csv(ROOT/'data'/'processed'/'drybean_clean.csv')
    X=data.drop(columns=['Class']).iloc[[0]]
    resultado=predict_bean_class(X)
    clase_real=str(data['Class'].iloc[0])
    assert resultado in set(data['Class'].unique()), 'Predicción fuera de las clases conocidas'
    print('scikit-learn:', sklearn.__version__)
    print('Columnas de entrada:', len(X.columns))
    print('Predicción modelo guardado:', resultado)
    print('Clase real muestra seleccionada:', clase_real)
    print('Modelo cargado y predicción ejecutada. Esta prueba NO mide Accuracy general.')

if __name__=='__main__':
    main()
