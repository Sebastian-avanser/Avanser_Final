#1. Carga datos
#2. procesa features "x" y etiqueta "y"
#3. separa en entrenamiento y prueba
#4. Entrena 3 modelos (Regresion logistrica, arbol de decision y random forest)
#5. Evalua cada modelo sobre el set de prueba y muestra la precision
import pandas as pd
from load_data import load_data
from preprocess import preproceswher
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

