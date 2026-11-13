"""Pruebas de calidad sin descargar datos ni abrir modelos pickle."""
from pathlib import Path
import json
import pandas as pd
import pytest

from src.data_quality import resumir_calidad, generar_reportes

RAIZ = Path(__file__).resolve().parents[1]
CSV = RAIZ / "data/processed/drybean_clean.csv"


def test_perfil_csv_procesado():
    resultado = resumir_calidad(pd.read_csv(CSV))
    assert resultado["filas"] == 13543
    assert resultado["columnas_totales"] == 17
    assert resultado["variables_predictoras"] == 16
    assert resultado["numero_clases"] == 7
    assert resultado["valores_nulos_totales"] == 0
    assert resultado["filas_duplicadas"] == 0
    clases = {fila["clase"]: fila["registros"] for fila in resultado["clases"]}
    assert clases["DERMASON"] == 3546
    assert clases["BOMBAY"] == 522
    assert clases["HOROZ"] == 1860


def test_valida_existencia_columna_objetivo():
    with pytest.raises(ValueError, match="Class"):
        resumir_calidad(pd.DataFrame({"Area": [1]}))


def test_reportes_son_reproducibles(tmp_path):
    reporte_json, reporte_csv = generar_reportes(CSV, tmp_path)
    datos = json.loads(reporte_json.read_text(encoding="utf-8"))
    assert datos["fuente_analizada"] == "data/processed/drybean_clean.csv"
    assert datos["filas"] == 13543
    assert int(pd.read_csv(reporte_csv)["registros"].sum()) == 13543
