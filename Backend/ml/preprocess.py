# preprocess.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

TARGET_COLUMN = "riesgo"

# columnas categóricas limpias
CATEGORICAL_COLS_TO_ENCODE = [
    'genero', 'estado_civil', 'nivel_educativo', 'grupo_poblacional',
    'estrato_socioeconomico', 'lugar_actual_de_residencia',
    'cambio_su_lugar_o_municipio_de_residencia_debido_a_su_programa_de_formacion',
    'ocupacion_actual', 'tiene_hijos',
    'usted_es_la_persona_encargada_de_generar_la_mayor_parte_de_los_ingresos_que_cubren_sus_gastos_de_sostenimiento_formacion_alimentacion_transporte_etc',
    'cual_es_la_principal_fuente_de_ingresos_que_utiliza_para_cubrir_sus_gastos_de_sostenimiento_formacion_alimentacion_transporte_etc',
    'con_quien_vive_actualmente', 'quien_es_la_cabeza_del_hogar',
    'en_que_tipo_de_vivienda_reside_actualmente',
    'su_familia_y_amigos_consideran_su_formacion_una_prioridad',
    'medio_de_transporte_que_utiliza_con_frecuencia_hacia_su_centro_de_formacion',
    'centro_de_formacion',
    'programa_en_el_que_esta_inscrito_nombre_completo_en_minusculas_y_tildes',
    'por_que_eligio_este_programa',
    'tiene_algun_conocimiento_del_programa_al_cual_ingreso',
    'que_expectativas_tiene_del_programa',
    'ha_solicitado_apoyos_externos_subsidios_becas_etc',
    'jornada_de_su_formacion',
    'cuenta_con_dispositivos_tecnologicos_para_estudiar',
    'su_dispositivo_o_medios_tecnologicos_se_encuentran_en_estado_optimo_para_realizar_las_tareas_que_se_requieren_en_la_formacion',
    'en_su_lugar_de_residencia_tiene_dificultades_de_conexion_a_internet',
    'comparte_su_dispositivo_de_estudio_con_otras_personas',
    'cuenta_con_algun_conocimiento_acerca_de_los_medios_y_herramientas_tecnologicas',
    'con_que_frecuencia_utiliza_la_tecnologia_como_medio_de_aprendizaje',
    'cuenta_con_alguna_discapacidad_permanente_que_dificulte_actividades_diarias_como_ver_oir_hablar_moverse_aprender_o_relacionarse',
    'si_la_respuesta_a_la_pregunta_anterior_es_si_marque_los_tipos_de_discapacidad_que_presenta',
    'cuenta_con_algun_certificado_de_discapacidad',
    'piensa_ejercer_los_conocimientos_adquiridos_en_su_programa',
    'considera_que_recibir_apoyo_emocional_o_psicologico_mejoraria_su_experiencia',
    'siente_que_en_su_entorno_valoran_su_esfuerzo',
    'esta_rodeado_de_personas_que_influyen_positivamente_en_su_aprendizaje',
    'ha_sido_victima_de_discriminacion',
    'ha_experimentado_problemas_o_danos_por_el_conflicto_armado'
]


def preprocess_data(df):

    print("\n==== INICIANDO PREPROCESAMIENTO ====")

    df = df.copy()

    # 1. ELIMINAR COLUMNAS 
    columnas_fuera = [
        "marca_temporal", "nombres", "apellidos",
        "numero_de_identificacion", "correo_electronico", "numero_de_telefono",
        "direccion_de_residencia_calle_carrera_avenida_diagonal_transversal_barrio",
        "fecha_de_nacimiento"
    ]
    df = df.drop(columns=[c for c in columnas_fuera if c in df.columns])
    print("Columnas removidas:", columnas_fuera)

    # 2. PROCESAR "NUMERO DE HIJOS"
    hijos_col = "si_respondido_si_a_la_pregunta_anterior_cuantos_hijos_tiene"
    if hijos_col in df.columns:

        def conv(valor):
            if pd.isna(valor):
                return 0
            s = str(valor).strip()
            if "-" in s:
                return int(s.split("-")[0])
            try:
                return int(s)
            except:
                return 0

        df["hijos"] = df[hijos_col].apply(conv)
        df = df.drop(columns=[hijos_col])
        print("✔ Columna 'hijos' convertida correctamente.")

    # 3. ONE-HOT
    cols = [c for c in CATEGORICAL_COLS_TO_ENCODE if c in df.columns]
    print("\nColumnas categóricas encontradas para one-hot:")
    print(cols)

    df = pd.get_dummies(df, columns=cols, drop_first=True)
    print("✔ One-hot encoding aplicado.")

    # 4. ESCALAR
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    numeric_cols.remove("riesgo")

    print("\nColumnas numéricas a escalar:")
    print(numeric_cols)

    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    print("✔ Escalamiento aplicado.")

    # 5. SEPARAR X e y
    X = df.drop(columns=["riesgo"])
    y = df["riesgo"]

    # 6. SPLIT
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("\n==== PREPROCESAMIENTO COMPLETO ====")

    return X_train, X_test, y_train, y_test
