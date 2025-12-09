import pandas as pd
import numpy as np
import re   

try:
    df = pd.read_csv("../data/encuesta.csv", encoding='utf-8')
    print("Datos cargados exitosamente.")
except Exception as e:
    print(f"Error al cargar el archivo: {e}")
    exit()

def limpiar_nombres_columnas(col_name):
    col_name = str(col_name)  

    col_name = col_name.replace('Ã³', 'ó').replace('Ã±', 'ñ').replace('Ã¡', 'á')
    col_name = col_name.replace('Ã©', 'é').replace('Ãº', 'ú').replace('Ã­', 'í')
    col_name = col_name.replace('Â¿', '').replace('¿', '').replace('Â', '')
    col_name = col_name.replace('?', '').replace(':', '')
    col_name = col_name.replace('  ', ' ')  # doble espacio
    col_name = col_name.strip()             # quita espacios al inicio/fin

    return col_name

df.columns = [limpiar_nombres_columnas(col) for col in df.columns]

print("\n--- Columnas Limpias ---")
print(df.columns.tolist())
