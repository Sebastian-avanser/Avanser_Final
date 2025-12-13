from pathlib import Path
from load_data import load_and_process

BASE_DIR = Path(__file__).resolve().parent
ruta = BASE_DIR.parent / "data" / "encuesta.csv"


ruta = "../data/encuesta.csv"  

print("Ruta:", ruta)
print("Existe?:", ruta.exists())



X, y, df = load_and_process(ruta)

print("\n--- RESULTADOS ---")
print("Tipo X:", type(X))
print("Tipo y:", type(y))
print("Tipo df:", type(df))

print("\nDimensiones:")
print("X:", X.shape)
print("y:", y.shape)
print("df:", df.shape)

print("\nClases del target (riesgo):")
print(y.value_counts())
