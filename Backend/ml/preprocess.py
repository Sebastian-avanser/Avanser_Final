#Se preparan los datos

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

#  CONFIGURACIÓN 

CLEAN_DATA_FILE = 'encuesta.csv' 


TARGET_COLUMN = 'riesgo_desercion' # 

CATEGORICAL_COLS_TO_ENCODE = [
    
    'Genero', 'Estado civil', 'Nivel educativo', 'Grupo poblacional', 'Estrato socioeconómico',
    'Lugar actual de residencia', 'Cambio su lugar o municipio de residencia debido a su programa de formación',
    'Ocupación actual', 'Tiene hijos', 
    'Usted es la persona encargada de generar la mayor parte de los ingresos que cubren sus gastos de sostenimiento (formación, alimentación, transporte, etc.)',
    'Cuál es la principal fuente de ingresos que utiliza para cubrir sus gastos de sostenimiento (formación, alimentación, transporte, etc.)',
    'Con quien vive actualmente', 'Quién es la cabeza del hogar', 'En qué tipo de vivienda reside actualmente',
    'Su familia y amigos consideran su formación una prioridad',
    

    'Medio de transporte que utiliza con frecuencia hacia su centro de formación',
    'Centro de formación', 'Programa en el que está inscrito (nombre completo en minúsculas y tildes)',
    'Por qué eligió este programa', 'Tiene algún conocimiento del programa al cual ingreso',
    'Qué expectativas tiene del programa', 'Ha solicitado apoyos externos (subsidios, becas, etc.)',
    'Jornada de su formación', 'Cuenta con dispositivos tecnológicos para estudiar',
    'Su dispositivo o medios tecnológicos se encuentran en estado optimo para realizar las tareas que se requieren en la formación',
    'En su lugar de residencia tiene dificultades de conexión a internet', 'Comparte su dispositivo de estudio con otras personas',
    'Cuenta con algún conocimiento acerca de los medios y herramientas tecnológicas', 'Con que frecuencia utiliza la tecnología como medio de aprendizaje',
    
    'cuenta con alguna discapacidad permanente que dificulte actividades diarias como (ver, oír, hablar, moverse, aprender, o relacionarse)',
    'Si la respuesta a la pregunta anterior es si, marque los tipos de discapacidad que presenta',
    'Cuenta con algún certificado de discapacidad', 'Piensa ejercer los conocimientos adquiridos en su programa',
    'Considera que recibir apoyo emocional o psicológico mejoraría su experiencia', 'Siente que en su entorno valoran su esfuerzo',
    'Está rodeado de personas que influyen positivamente en su aprendizaje', 'Ha sido víctima de discriminación',
    'Ha experimentado problemas o daños por el conflicto armado',
]

# FUNCIÓN DE CARGA 

def load_clean_data(file_path):
    """Carga los datos limpios generados por clean_data.py."""
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
        print(f"Datos limpios cargados exitosamente. Dimensiones: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: El archivo de datos limpios '{file_path}' no fue encontrado. Asegúrate de que clean_data.py se haya ejecutado.")
        return None

# FUNCIÓN DE PREPROCESAMIENTO 

def preprocess_data(df, target_col = None):
    """
    Aplica transformaciones de ML (imputación, escalado, codificación)
    y separa las variables X e y.
    """
    # 1. Verificación de Columna Objetivo
    if target_col not in df.columns:
        print(f"Error: La columna '{target_col}' no se encontro")
        return None, None, None
    
    # IMPUTACION LOGICA DE NULOS 


    col_hijos = 'Si respondido, si, a la pregunta anterior, Cuántos hijos tiene'
    if col_hijos in df.columns:
        df[col_hijos].fillna(0, inplace=True)
        df[col_hijos] = df[col_hijos].astype(int)
            
    col_discapacidad = 'Si la respuesta a la pregunta anterior es si, marque los tipos de discapacidad que presenta'
    if col_discapacidad in df.columns:
        df[col_discapacidad].fillna('Ninguna', inplace=True)
        
    for col in CATEGORICAL_COLS_TO_ENCODE:
        if col in df.columns and df[col].isnull().sum() > 0:
            moda = df[col].mode()[0]
            df[col].fillna(moda, inplace=True)

    # CODIFICACION DE VARIABLES (ONEE-HOT ENCONDING)

    cols_to_encode_in_df = [col for col in CATEGORICAL_COLS_TO_ENCODE if col in df.columns]
    df = pd.get_dummies(df, columns=cols_to_encode_in_df, 
                         dummy_na=False, drop_first=True) 

    # ESCALADO DE VARIABLES NUMERICAS  (standarScaler)

    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    if target_col in numeric_cols:
        numeric_cols.remove(target_col)
    
    if numeric_cols:
        scaler = StandardScaler()
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
        
    #  SEPARACION DE X AND Y

    X = df.drop(columns=[target_col])
    y = df[target_col]

    return X, y, None
