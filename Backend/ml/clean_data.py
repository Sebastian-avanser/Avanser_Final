import pandas as pd
import numpy as np


# 1. Cargar el DataFrame (ya verificamos que esta ruta y encoding funcionan)
# Usaremos 'latin1' (ISO-8859-1) que es común para archivos con caracteres en español
try:
    df = pd.read_csv("../data/encuesta.csv", encoding='latin1')
    print("Datos cargados exitosamente.")
except Exception as e:
    print(f"Error al cargar el archivo: {e}")
    # Si sigue habiendo error, revise el nombre del archivo o la codificación.
    exit()

# --- 2. LIMPIEZA Y ESTANDARIZACIÓN DE NOMBRES DE COLUMNAS ---

def limpiar_nombres_columnas(col_name):
    # Reemplazos para corregir la codificación rota
    col_name = col_name.replace('Ã³', 'ó').replace('Ã±', 'ñ').replace('Ã¡', 'á')
    col_name = col_name.replace('Ã©', 'é').replace('Ãº', 'ú').replace('Ã­', 'í')
    col_name = col_name.replace('Â¿', '').replace('¿', '').replace('Â', '')
    col_name = col_name.replace('?', '').replace(':', '')
    col_name = col_name.replace(' ', ' ') # Limpiar espacios no visibles
    col_name = col_name.replace('  ', ' ') # Reemplazar doble espacio
    col_name = col_name.strip() # Eliminar espacios al inicio/final
    return col_name

# Aplicamos la limpieza
df.columns = [limpiar_nombres_columnas(col) for col in df.columns]

print("\n--- Columnas Limpias ---")
print(df.columns.tolist())


# --- 3. LIMPIEZA Y MANEJO DE VALORES NULOS (IMPUTACIÓN) ---

# a. Eliminar columnas de identificación (no útiles para el modelo)
columnas_a_eliminar = [
    'Marca temporal', 
    'Nombres', 
    'Apellidos', 
    'Numero de identificación', 
    'Correo electrónico', 
    'Dirección de residencia (Calle / Carrera / Avenida / Diagonal / Transversal / Barrio)',
    'Numero de ficha'
]
df = df.drop(columns=columnas_a_eliminar, errors='ignore')


# b. Imputar variables Numéricas
# Utilizamos los nombres de columnas ya LIMPIOS
columnas_numericas = ['Número de teléfono', 'Número de personas que viven con usted'] # Agregue las que sean numéricas

for col in columnas_numericas:
    if col in df.columns:
        # 'coerce' convierte los valores no numéricos (ej. texto, respuestas vacías) a NaN
        df[col] = pd.to_numeric(df[col], errors='coerce') 
        # Imputamos con la mediana
        mediana = df[col].median()
        df[col] = df[col].fillna(mediana)

# c. Imputar variables Categóricas/Texto
# Utilizamos la Moda (valor más frecuente) para rellenar los nulos.
columnas_categoricas_basicas = ['Estado civil', 'Género', 'Ocupación actual'] # Puede agregar más

for col in columnas_categoricas_basicas:
    if col in df.columns:
        moda = df[col].mode()[0]
        df[col] = df[col].fillna(moda)

print("\n--- Nulos después de Imputación Básica ---")
print(df.isnull().sum())


# --- 4. PREPARACIÓN DE LA VARIABLE OBJETIVO (TARGET) ---

# *IMPORTANTE*: Necesita una columna que etiquete la deserción (1 o 0).
# Si la columna que contiene el estado del aprendiz existe, úsela:
# Ejemplo: df['Desercion'] = np.where(df['Estado_Aprendiz'] == 'Desertó', 1, 0)

# ***Simulación: Si no tiene datos históricos de deserción, este modelo NO FUNCIONARÁ***
# ***Reemplace esta sección con su lógica real para obtener la etiqueta 1 o 0.***
if 'Desercion' not in df.columns:
    print("\n⚠️ Creando variable 'Desercion' simulada (Todos 0) para fines de prueba.")
    df['Desercion'] = 0 
    # **DEBE TENER DATOS REALES DE DESERCIÓN (1) PARA ENTRENAR**
    

# --- 5. CODIFICACIÓN ONE-HOT ---

# Identificamos todas las columnas que aún son de tipo 'object' (texto) y necesitan codificación.
# Excluimos la variable objetivo.
columnas_para_one_hot = df.select_dtypes(include='object').columns.tolist()

df_codificado = pd.get_dummies(df, columns=columnas_para_one_hot, drop_first=True, dtype=int)

print(f"\n✅ Codificación One-Hot Finalizada. Total de características: {len(df_codificado.columns)}.")