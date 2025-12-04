#Carga archivos
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname (os.path.dirname(__file__)))

def load_data(filename = "Formulario de Caracterizacion"):
    ruta = os.path.join(BASE_DIR, "data", filename)
    return pd.read_csv (ruta)

df = pd.read_csv("../data/encuesta.csv", encoding='latin1')
print(df.columns)
