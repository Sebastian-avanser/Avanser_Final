from pipeline import ejecutar_pipeline
from train_models import train_models

ruta = "../data/encuesta.csv"

X, y, _ = ejecutar_pipeline(ruta)
models = train_models(X, y)