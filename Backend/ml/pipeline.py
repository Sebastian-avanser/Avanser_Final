# pipeline.py

from load_data import load_and_process
from preprocess import preprocess_data
from train_models import entrenar_modelos

def ejecutar_pipeline(ruta_csv):
    print("\n=== INICIANDO PIPELINE ===")

    # 1. Cargar y procesar datos base
    print("\n Cargando datos y generando columna objetivo...")
    df = load_and_process(ruta_csv)

    # 2. Preprocesar → separar X e y, codificar, rellenar nulos y dividir en train/test
    print("\nPreprocesando datos...")
    X_train, X_test, y_train, y_test = preprocess_data(df)

    # 3. Entrenar 3 modelos (Reg Log, Árbol, RandomForest)
    print("\nEntrenando modelos...")
    modelos, resultados = entrenar_modelos(X_train, X_test, y_train, y_test)

    print("\n=== PIPELINE COMPLETO ===")

    print("\n Resultados de precisión:")
    for nombre, score in resultados.items():
        print(f"  - {nombre}: {score:.4f}")

    return modelos, resultados


if __name__ == "__main__":
    ruta = "../data/encuesta.csv"
    modelos, resultados = ejecutar_pipeline(ruta)
