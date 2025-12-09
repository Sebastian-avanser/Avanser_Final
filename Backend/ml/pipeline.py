# pipeline.py (corregido)
from load_data import load_and_process       # supongamos que load_data(ruta) devuelve un pd.DataFrame
from target import generar_target
from preprocess import preprocess_data

def ejecutar_pipeline(ruta):
    # 1) Cargar datos (devuelve DataFrame)
    df = load_and_process(ruta)          # <- asegúrate de que load_data lea el archivo y retorne df
    print("Tipo de df tras load_data:", type(df))  # debug: debe mostrar <class 'pandas.core.frame.DataFrame'>

    # 2) Generar target usando el DataFrame
    df["riesgo"] = generar_target(df)   # ahora df es DataFrame, generar_target puede usar df.apply

    # 3) continuar pipeline...
    X, y = preprocess_data(df)
    return X, y, df

if __name__ == "__main__":
    ruta = "../data/encuesta.csv"
    X, y, _ = ejecutar_pipeline(ruta)
