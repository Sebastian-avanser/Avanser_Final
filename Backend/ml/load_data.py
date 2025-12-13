# load_data.py

import pandas as pd
from clean_data import limpiar_nombres_columnas
from target import generar_target

def load_and_process(ruta):
    df = pd.read_csv(ruta)

    df = limpiar_nombres_columnas(df)

    df["riesgo"] = generar_target(df)

    return df
