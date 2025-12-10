def calcular_riesgo(fila):
    score = 0

    # ECONÓMICO
    fuente = fila.get(
        'Cuál es la principal fuente de ingresos que utiliza para cubrir sus gastos de sostenimiento (formación, alimentación, transporte, etc.)',
        ""
    )
    if fuente in ["Ninguno", "Subsidios", "Familiar sin ingresos estables"]:
        score += 3

    if fila.get(
        'Usted es la persona encargada de generar la mayor parte de los ingresos que cubren sus gastos de sostenimiento (formación, alimentación, transporte, etc.)',
        ""
    ) == "Sí":
        score += 3

    estrato = str(fila.get('Estrato socioeconómico', "")).strip()
    if estrato in ["1", "2"]:
        score += 1

    # TECNOLOGÍA
    if fila.get('Cuenta con dispositivos tecnológicos para estudiar', "") == "No":
        score += 3

    if fila.get(
        'Su dispositivo o medios tecnológicos se encuentran en estado optimo para realizar las tareas que se requieren en la formación',
        ""
    ) == "No":
        score += 2

    if fila.get('En su lugar de residencia tiene dificultades de conexión a internet', "") == "Sí":
        score += 3

    if fila.get('Comparte su dispositivo de estudio con otras personas', "") == "Sí":
        score += 1

    # FAMILIAR
    if fila.get('Tiene hijos', "") == "Sí":
        score += 2
        hijos = fila.get('Si respondido, si, a la pregunta anterior, Cuántos hijos tiene', 0)
        try:
            if int(hijos) >= 2:
                score += 1
        except:
            pass

    if fila.get('Con quien vive actualmente', "") in ["Solo", "Hogar disfuncional"]:
        score += 2

    if fila.get('Quién es la cabeza del hogar', "") == "Yo mismo":
        score += 3

    # TRANSPORTE
    try:
        if float(fila.get('Distancia aproximada de su hogar al centro de formación', 0)) > 20:
            score += 2
    except:
        pass

    try:
        if float(fila.get('Tiempo promedio de desplazamiento hacia su centro de formación', 0)) > 45:
            score += 2
    except:
        pass

    # MOTIVACIÓN
    if fila.get('Tiene algún conocimiento del programa al cual ingreso', "") == "No":
        score += 2

    if fila.get('Qué expectativas tiene del programa', "") in ["No sé", "Pocas expectativas"]:
        score += 2

    if fila.get('Su familia y amigos consideran su formación una prioridad', "") == "No":
        score += 3

    # APOYO
    if fila.get('Ha solicitado apoyos externos (subsidios, becas, etc.)', "") == "Sí":
        score += 1

    # EMOCIONAL
    if fila.get('Ha sido víctima de discriminación', "") == "Sí":
        score += 2

    if fila.get('Ha experimentado problemas o daños por el conflicto armado', "") == "Sí":
        score += 3

    # CLASIFICACIÓN FINAL
    if score >= 8:
        return 2  # Alto riesgo
    elif score >= 4:
        return 1  # Riesgo medio
    else:
        return 0  # Bajo riesgo

def generar_target(df):
    print("TIPO DE DF:", type(df))
    return df.apply(calcular_riesgo, axis=1)
