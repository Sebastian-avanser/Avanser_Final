# train_models.py

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def entrenar_modelos(X_train, X_test, y_train, y_test):

    print("\nEntrenando modelos...")

    modelos = {
        "LogisticRegression": LogisticRegression(max_iter=2000),
        "DecisionTree": DecisionTreeClassifier(),
        "RandomForest": RandomForestClassifier()
    }

    resultados = {}

    for nombre, modelo in modelos.items():
        print(f"→ Entrenando {nombre}...")
        modelo.fit(X_train, y_train)

        pred = modelo.predict(X_test)
        acc = accuracy_score(y_test, pred)
        resultados[nombre] = acc

        print(f"✔ {nombre} completado. Accuracy: {acc:.4f}")

    print("\n=== RESULTADOS DE LOS MODELOS ===")
    for nombre, acc in resultados.items():
        print(f"{nombre}: {acc:.4f}")

    return modelos, resultados
