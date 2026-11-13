"""Verifica la estructura y el CSV local sin ejecutar ML ni abrir pickle."""
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parent.parent
required = [
    "README.md", "requirements.txt", "src/predict.py",
    "notebooks/01_laboratorio_drybean.ipynb",
    "data/processed/drybean_clean.csv", "scrum/backlog.md",
    "scrum/tablero.md", "scrum/roles_equipo.md",
    "docs/crisp_dm/01_comprension_negocio.md",
    "outputs/models/logistic_regression_drybean.joblib",
    "outputs/reports/matriz_logistic_regression.png",
    "outputs/reports/matriz_random_forest.png",
]
missing = [str(p) for p in required if not (ROOT / p).is_file()]
if missing:
    raise SystemExit("Faltan archivos: " + ", ".join(missing))
notebook = json.loads((ROOT / "notebooks/01_laboratorio_drybean.ipynb").read_text(encoding="utf-8"))
assert notebook["nbformat"] == 4 and len(notebook["cells"]) >= 36
with (ROOT / "data/processed/drybean_clean.csv").open(newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    cols = next(reader)
    n = sum(1 for _ in reader)
assert len(cols) == 17 and cols[-1] == "Class", (len(cols), cols[-1])
assert n == 13543, n
print(f"Estructura y datos locales OK: {n} registros, {len(cols)} columnas, {len(notebook['cells'])} celdas")
print("No ejecutó entrenamiento, ni UCI, ni la carga del modelo .joblib.")
