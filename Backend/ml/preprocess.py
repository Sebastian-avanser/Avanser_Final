import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# ==========================
# CONFIGURACIÓN
# ==========================

TARGET_COLUMN = 'riesgo'

CATEGORICAL_COLS_TO_ENCODE = [
    'Genero', 'Estado civil', 'Nivel educativo', 'Grupo poblacional',
    'Estrato socioeconómico', 'Lugar actual de residencia',
    'Cambio su lugar o municipio de residencia debido a su programa de formación',
    'Ocupación actual', 'Tiene hijos',

    'Usted es la persona encargada de generar la mayor parte de los ingresos que cubren sus gastos de sostenimiento (formación, alimentación, transporte, etc.)',
    'Cuál es la principal fuente de ingresos que utiliza para cubrir sus gastos de sostenimiento (formación, alimentación, transporte, etc.)',

    'Con quien vive actualmente', 'Quién es la cabeza del hogar',
    'En qué tipo de vivienda reside actualmente',
    'Su familia y amigos consideran su formación una prioridad',

    'Medio de transporte que utiliza con frecuencia hacia su centro de formación',
    'Centro de formación',
    'Programa en el que está inscrito (nombre completo en minúsculas y tildes)',

    'Por qué eligió este programa',
    'Tiene algún conocimiento del programa al cual ingreso',
    'Qué expectativas tiene del programa',
    'Ha solicitado apoyos externos (subsidios, becas, etc.)',
    'Jornada de su formación',

    'Cuenta con dispositivos tecnológicos para estudiar',
    'Su dispositivo o medios tecnológicos se encuentran en estado optimo para realizar las tareas que se requieren en la formación',
    'En su lugar de residencia tiene dificultades de conexión a internet',
    'Comparte su dispositivo de estudio con otras personas',

    'Cuenta con algún conocimiento acerca de los medios y herramientas tecnológicas',
    'Con que frecuencia utiliza la tecnología como medio de aprendizaje',

    'cuenta con alguna discapacidad permanente que dificulte actividades diarias como (ver, oír, hablar, moverse, aprender, o relacionarse)',
    'Si la respuesta a la pregunta anterior es si, marque los tipos de discapacidad que presenta',
    'Cuenta con algún certificado de discapacidad',

    'Piensa ejercer los conocimientos adquiridos en su programa',
    'Considera que recibir apoyo emocional o psicológico mejoraría su experiencia',
    'Siente que en su entorno valoran su esfuerzo',
    'Está rodeado de personas que influyen positivamente en su aprendizaje',
    'Ha sido víctima de discriminación',
    'Ha experimentado problemas o daños por el conflicto armado',
]

# ==========================
# PREPROCESAMIENTO
# ==========================

def preprocess_data(df, target_col=TARGET_COLUMN):

    if target_col not in df.columns:
        raise ValueError(f"La columna objetivo '{target_col}' no existe")

    df = df.copy()

    # --------------------------
    # IMPUTACIÓN LÓGICA (HIJOS)
    # --------------------------

    col_hijos = "Si respondido, si, a la pregunta anterior, Cuántos hijos tiene"

    if col_hijos in df.columns:

        def convertir_hijos(valor):
            if pd.isna(valor):
                return 0
            valor = str(valor)

            if "-" in valor:      # '1-2'
                return int(valor.split("-")[0])
            if "más" in valor:
                return 3
            try:
                return int(valor)
            except:
                return 0

        df[col_hijos] = df[col_hijos].apply(convertir_hijos)

    # --------------------------
    # ONE HOT ENCODING
    # --------------------------

    cols_to_encode = [c for c in CATEGORICAL_COLS_TO_ENCODE if c in df.columns]
    df = pd.get_dummies(df, columns=cols_to_encode, drop_first=True)

    # --------------------------
    # ESCALADO
    # --------------------------

    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    numeric_cols.remove(target_col)

    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    # --------------------------
    # X / y
    # --------------------------

    X = df.drop(columns=[target_col])
    y = df[target_col]

    return X, y, scaler
