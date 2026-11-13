"""Descarga una copia verificable del dataset UCI ID 602 (requiere internet).

No crea datos sintéticos y no altera `data/processed/` ni el notebook.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import pandas as pd
from ucimlrepo import fetch_ucirepo

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'data' / 'raw'

def main():
    original = fetch_ucirepo(id=602)
    df = pd.concat([original.data.features, original.data.targets], axis=1)
    if df.shape != (13611, 17) or 'Class' not in df.columns:
        raise ValueError(f'Esquema UCI inesperado: {df.shape}, Class: {"Class" in df.columns}')
    DEST.mkdir(parents=True, exist_ok=True)
    ruta = DEST / 'drybean_uci_original.csv'
    # Se guarda una copia observada de UCI, sin eliminar duplicados.
    df.to_csv(ruta, index=False)
    sha256 = hashlib.sha256(ruta.read_bytes()).hexdigest()
    datos = {
        'fuente': 'UCI Machine Learning Repository, Dry Bean Dataset, ID 602',
        'url': 'https://archive.ics.uci.edu/dataset/602/dry+bean+dataset',
        'descarga_utc': datetime.now(timezone.utc).isoformat(),
        'archivo': 'data/raw/drybean_uci_original.csv',
        'filas': len(df), 'columnas': len(df.columns),
        'nulos': int(df.isna().sum().sum()),
        'duplicados': int(df.duplicated().sum()),
        'sha256_archivo_csv': sha256,
        'nota': 'El hash refleja este CSV exportado, no el archivo original del sitio UCI.'
    }
    (DEST / 'procedencia_uci.json').write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Fuente guardada: {ruta.relative_to(ROOT)}; filas={len(df)}; duplicados={datos["duplicados"]}')
    print(f'SHA256: {sha256}')

if __name__=='__main__':
    main()
