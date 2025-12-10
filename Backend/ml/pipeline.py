from load_data import load_and_process

def ejecutar_pipeline(ruta):
    X, y, df = load_and_process(ruta)
    return X, y, df

if __name__ == "__main__":
    ruta = "../data/encuesta.csv"

    X, y, df = ejecutar_pipeline(ruta)

    print("Pipeline ejecutado correctamente")
    print("Shape X:", X.shape)
    print("Ejemplo de y:")
    print(y.head())
