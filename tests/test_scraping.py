import os
import pandas as pd
import pytest
from src.scraping_branchos import ejecutar_scraping_multicanal

def test_ejecucion_scraping_devuelve_datos():
    """Valida que la función de scraping extraiga al menos un registro."""
    total_registros = ejecutar_scraping_multicanal(paginas=1)
    assert total_registros > 0, "El scraping no recolectó ningún producto."

def test_archivo_csv_generado_y_estructurado():
    """Valida que el archivo CSV exista y contenga las columnas requeridas."""
    ruta_csv = "data/productos_extraidos.csv"
    assert os.path.exists(ruta_csv), "El archivo CSV de datos no se generó."
    
    df = pd.read_csv(ruta_csv, sep=';')
    columnas_esperadas = ["SKU", "Producto", "Precio"]
    for col in columnas_esperadas:
        assert col in df.columns, f"Falta la columna requerida: {col}"
