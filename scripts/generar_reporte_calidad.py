"""Ejecutar desde cualquier ruta: python scripts/generar_reporte_calidad.py"""
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parents[1]
if str(RAIZ) not in sys.path:
    sys.path.insert(0, str(RAIZ))

from src.data_quality import generar_reportes

if __name__ == "__main__":
    entrada = RAIZ / "data" / "processed" / "drybean_clean.csv"
    salida = RAIZ / "outputs" / "reports"
    json_file, csv_file = generar_reportes(entrada, salida)
    print("Perfil calculado desde datos procesados (no desde UCI original):")
    print(" -", json_file.relative_to(RAIZ))
    print(" -", csv_file.relative_to(RAIZ))
