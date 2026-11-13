"""Perfil básico y validaciones reproducibles del Dry Bean Dataset procesado.

El análisis de este módulo se hace sobre el CSV limpio aportado por el equipo.
No sustituye el análisis de la fuente original UCI (13.611 observaciones).
"""
from pathlib import Path
import json
import pandas as pd


def resumir_calidad(df: pd.DataFrame) -> dict:
    """Devuelve un resumen descriptivo de un DataFrame de Dry Bean.

    No modifica el DataFrame, no entrena modelos ni elimina duplicados.
    """
    if "Class" not in df.columns:
        raise ValueError("Falta la columna objetivo 'Class'")
    caracteristicas = df.drop(columns="Class")
    if caracteristicas.shape[1] != 16:
        raise ValueError("Se esperaban 16 características predictoras")
    if not all(pd.api.types.is_numeric_dtype(tipo) for tipo in caracteristicas.dtypes):
        raise ValueError("Todas las características predictoras deben ser numéricas")
    frecuencias = df["Class"].value_counts()
    if frecuencias.empty:
        raise ValueError("No hay clases en el archivo")
    mas_frecuente, menos_frecuente = int(frecuencias.max()), int(frecuencias.min())
    return {
        "filas": int(len(df)),
        "columnas_totales": int(df.shape[1]),
        "variables_predictoras": int(caracteristicas.shape[1]),
        "variable_objetivo": "Class",
        "numero_clases": int(frecuencias.size),
        "valores_nulos_totales": int(df.isna().sum().sum()),
        "nulos_por_columna": {nombre: int(n) for nombre, n in df.isna().sum().items()},
        "filas_duplicadas": int(df.duplicated().sum()),
        "tipos_de_datos": {nombre: str(tipo) for nombre, tipo in df.dtypes.items()},
        "clases": [
            {"clase": str(nombre), "registros": int(n),
             "porcentaje": round(100 * int(n) / len(df), 2)}
            for nombre, n in frecuencias.items()
        ],
        "razon_mayor_menor": round(mas_frecuente / menos_frecuente, 2),
    }


def generar_reportes(csv_path: Path, reports_dir: Path) -> tuple[Path, Path]:
    """Genera JSON y CSV deterministas desde la copia procesada."""
    df = pd.read_csv(csv_path)
    reporte = {
        "fuente_analizada": "data/processed/drybean_clean.csv",
        "nota_procedencia": "Archivo procesado de la entrega; NO contiene los 13.611 registros UCI originales",
        **resumir_calidad(df),
    }
    reports_dir.mkdir(parents=True, exist_ok=True)
    destino_json = reports_dir / "calidad_datos_procesados.json"
    destino_csv = reports_dir / "distribucion_clases_procesadas.csv"
    destino_json.write_text(json.dumps(reporte, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    pd.DataFrame(reporte["clases"]).to_csv(destino_csv, index=False)
    return destino_json, destino_csv
