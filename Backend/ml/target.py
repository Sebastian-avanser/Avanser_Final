# target.py

def calcular_riesgo(fila):
    score = 0

    # =============== ECONÓMICO ===============
    fuente = fila.get(
        'cual_es_la_principal_fuente_de_ingresos_que_utiliza_para_cubrir_sus_gastos_de_sostenimiento_formacion_alimentacion_transporte_etc',
        ""
    )
    if fuente in ["Ninguno", "Subsidios", "Familiar sin ingresos estables"]:
        score += 3

    if fila.get(
        'usted_es_la_persona_encargada_de_generar_la_mayor_parte_de_los_ingresos_que_cubren_sus_gastos_de_sostenimiento_formacion_alimentacion_transporte_etc',
        ""
    ) == "Sí":
        score += 3

    estrato = str(fila.get('estrato_socioeconomico', "")).strip()
    if estrato in ["1", "2"]:
        score += 1

    # =============== TECNOLOGÍA ===============
    if fila.get('cuenta_con_dispositivos_tecnologicos_para_estudiar', "") == "No":
        score += 3

    if fila.get(
        'su_dispositivo_o_medios_tecnologicos_se_encuentran_en_estado_optimo_para_realizar_las_tareas_que_se_requieren_en_la_formacion',
        ""
    ) == "No":
        score += 2

    if fila.get('en_su_lugar_de_residencia_tiene_dificultades_de_conexion_a_internet', "") == "Sí":
        score += 3

    if fila.get('comparte_su_dispositivo_de_estudio_con_otras_personas', "") == "Sí":
        score += 1

    # =============== FAMILIAR ===============
    if fila.get('tiene_hijos', "") == "Sí":
        score += 2

        hijos = fila.get('si_respondido_si_a_la_pregunta_anterior_cuantos_hijos_tiene', 0)
        try:
            if int(hijos) >= 2:
                score += 1
        except:
            pass

    if fila.get('con_quien_vive_actualmente', "") in ["Solo", "Hogar disfuncional"]:
        score += 2

    if fila.get('quien_es_la_cabeza_del_hogar', "") == "Yo mismo":
        score += 3

    # =============== TRANSPORTE ===============
    try:
        if float(fila.get('distancia_aproximada_de_su_hogar_al_centro_de_formacion', 0)) > 20:
            score += 2
    except:
        pass

    try:
        if float(fila.get('tiempo_promedio_de_desplazamiento_hacia_su_centro_de_formacion', 0)) > 45:
            score += 2
    except:
        pass

    # =============== MOTIVACIÓN ===============
    if fila.get('tiene_algun_conocimiento_del_programa_al_cual_ingreso', "") == "No":
        score += 2

    if fila.get('que_expectativas_tiene_del_programa', "") in ["No sé", "Pocas expectativas"]:
        score += 2

    if fila.get('su_familia_y_amigos_consideran_su_formacion_una_prioridad', "") == "No":
        score += 3

    # =============== APOYO ===============
    if fila.get('ha_solicitado_apoyos_externos_subsidios_becas_etc', "") == "Sí":
        score += 1

    # =============== EMOCIONAL ===============
    if fila.get('ha_sido_victima_de_discriminacion', "") == "Sí":
        score += 2

    if fila.get('ha_experimentado_problemas_o_danos_por_el_conflicto_armado', "") == "Sí":
        score += 3

    # =============== CLASIFICACIÓN FINAL ===============
    if score >= 8:
        return 2  # Alto riesgo
    elif score >= 4:
        return 1  # Riesgo medio
    else:
        return 0  # Bajo riesgo


def generar_target(df):
    return df.apply(calcular_riesgo, axis=1)
