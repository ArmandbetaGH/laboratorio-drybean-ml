"""Checks livianos que no ejecutan el artefacto pickle externo."""
from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def test_csv_procesado():
    df = pd.read_csv(ROOT / 'data/processed/drybean_clean.csv')
    assert df.shape == (13543, 17)
    assert df['Class'].nunique() == 7
    assert df.isna().sum().sum() == 0
    assert df.duplicated().sum() == 0

def test_notebook_formato():
    import nbformat
    nb = nbformat.read(ROOT / 'notebooks/01_laboratorio_drybean.ipynb', as_version=4)
    nbformat.validate(nb)
    assert len(nb.cells) >= 36

def test_entregables_existen():
    for rel in ('scrum/backlog.md', 'scrum/tablero.md',
                'docs/crisp_dm/01_comprension_negocio.md',
                'outputs/reports/matriz_random_forest.png'):
        assert (ROOT / rel).is_file()
