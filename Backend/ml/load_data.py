import os
import pandas as pd
from clean_data import limpiar_nombres_columnas
from preprocess import preprocess_data
from target import generar_target

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

def load_and_process(file_path):

    df = pd.read_csv(file_path)

    df = limpiar_nombres_columnas(df)

    df["riesgo"] = generar_target(df)

    X, y, preprocessor = preprocess_data(df, target_col="riesgo")

    return X, y, preprocessor


if __name__ == "__main__":
    data_path = "../data/encuesta.csv"

    X, y, preprocessor = load_and_process(data_path)

    print("Datos cargados y procesados")
    print("Shape X:", X.shape)
    print("Ejemplo de y:")
    print(y.head())
