import pandas as pd
from clean_data import limpiar_nombres_columnas
from target import generar_target

def load_and_process(ruta):
    df = pd.read_csv(ruta)

    print("Datos cargados exitosamente.\n")
    print("--- Columnas Limpias ---")
    
    df = limpiar_nombres_columnas(df)
    print(df.columns.tolist())

    # genera target
    df["riesgo"] = generar_target(df)

    #  RETORNA DATAFRAME
    return X, y, df
