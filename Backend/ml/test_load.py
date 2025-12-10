from load_data import load_and_process

ruta = "../data/encuesta.csv"   # ⚠️ AJUSTA LA RUTA A TU CSV

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
