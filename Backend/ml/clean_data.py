# clean_data.py

import pandas as pd
import unicodedata
import re

def limpiar_nombres_columnas(df: pd.DataFrame):
    columnas_limpias = []

    for col in df.columns:
        col = col.lower()
        col = "".join(
            c for c in unicodedata.normalize("NFKD", col) if not unicodedata.combining(c)
        )
        col = re.sub(r"[^a-z0-9]+", "_", col)
        col = col.strip("_")

        columnas_limpias.append(col)

    df.columns = columnas_limpias
    return df

