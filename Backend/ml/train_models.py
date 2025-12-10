from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


def train_models(X, y):
    # 1. Separar train / test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    print("Train:", X_train.shape)
    print("Test :", X_test.shape)

    # ==================================
    # MODELOS
    # ==================================

    models = {
        "Regresión Logística": LogisticRegression(
            max_iter=2000,
            multi_class="multinomial",
            solver="lbfgs"
        ),
        "Árbol de Decisión": DecisionTreeClassifier(
            max_depth=6,
            random_state=42
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=200,
            max_depth=10,
            random_state=42
        )
    }

    trained_models = {}

    for name, model in models.items():
        print(f"\n===== {name} =====")

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Matriz de Confusión:\n", confusion_matrix(y_test, y_pred))
        print("Reporte de Clasificación:\n", classification_report(y_test, y_pred))

        trained_models[name] = model

    return trained_models
