import pandas as pd


#   CALCULO DE RIESGO POR PERSONA

def calcular_riesgo(row):
    score = 0


    # FACTORES ECONÓMICOS

    fuente = row.get(
        '¿Cuál es la principal fuente de ingresos que utiliza para cubrir sus gastos de sostenimiento (formación, alimentación, transporte, etc.)?  ',
        ""
    )
    if fuente in ["Ninguno", "Subsidios", "Familiar sin ingresos estables"]:
        score += 3

    if row.get(
        '¿Usted es la persona encargada de generar la mayor parte de los ingresos que cubren sus gastos de sostenimiento (formación, alimentación, transporte, etc.)?  ',
        ""
    ) == "Sí":
        score += 3

    estrato = str(row.get('Estrato socioeconómico ', "")).strip()
    if estrato in ["1", "2"]:
        score += 1

 
    # TECNOLOGÍA Y ACCESO DIGITAL

    if row.get('¿Cuenta con dispositivos tecnológicos para estudiar? ', "") == "No":
        score += 3

    if row.get(
        '¿Su dispositivo o medios tecnológicos se encuentran en estado optimo para realizar las tareas que se requieren en la formación?',
        ""
    ) == "No":
        score += 2

    if row.get('¿En su lugar de residencia tiene dificultades de conexión a internet?', "") == "Sí":
        score += 3

    if row.get('Comparte su dispositivo de estudio con otras personas? ', "") == "Sí":
        score += 1


    # FAMILIAR

    if row.get('¿Tiene hijos ?', "") == "Sí":
        score += 2
        try:
            hijos = int(row.get(
                'Si respondido, si, a la pregunta anterior, ¿Cuántos hijos tiene ?',
                0
            ))
            if hijos >= 2:
                score += 1
        except:
            pass

    if row.get('¿Con quien vive actualmente? ', "") in ["Solo", "Hogar disfuncional"]:
        score += 2

    if row.get('¿Quién es la cabeza del hogar?', "") == "Yo mismo":
        score += 3


    # TANSPORTE Y UBI

    try:
        distancia = float(row.get('Distancia aproximada de su hogar al centro de formación', 0))
        if distancia > 10:
            score += 1
        if distancia > 20:
            score += 2
    except:
        pass

    try:
        tiempo = float(row.get('Tiempo promedio de desplazamiento hacia su centro de formación', 0))
        if tiempo > 45:
            score += 2
    except:
        pass

    # MOTIVACION

    if row.get('¿Tiene algún conocimiento del programa al cual ingreso?', "") == "No":
        score += 2

    if row.get('¿Qué expectativas tiene del programa?', "") in ["No sé", "Pocas expectativas"]:
        score += 2

    if row.get('¿Su familia y amigos consideran su formación una prioridad?', "") == "No":
        score += 3


    # APOYO
    
    if row.get('¿Ha solicitado apoyos externos (subsidios, becas, etc.)?', "") == "Sí":
        score += 1

 
    # TECNOLOGIA COMO APRENDIZAJE

    if row.get(
        '¿Con que frecuencia utiliza la tecnología como medio de aprendizaje?',
        ""
    ) in ["Nunca", "Rara vez"]:
        score += 1


    # DISCAPACIDAD

    if row.get(
        '¿cuenta con alguna discapacidad  permanente que dificulte actividades diarias como  (ver, oír, hablar, moverse, aprender, o relacionarse)? ',
        ""
    ) == "Sí":
        score += 3


    # BIENESTAR EMOCIONAL

    if row.get(
        '¿Considera que recibir apoyo emocional o psicológico mejoraría su experiencia?',
        ""
    ) == "Sí":
        score += 2

    if row.get('¿Ha sido víctima de discriminación? ', "") == "Sí":
        score += 2

    if row.get('¿Ha experimentado problemas o daños por el conflicto armado?', "") == "Sí":
        score += 3


    # CLASIFICACIÓN FINAL

    if score >= 8:
        return 2   # ALTO
    elif score >= 4:
        return 1   # MEDIO
    else:
        return 0   # BAJO



#   FUNCIÓN PRINCIPAL (TARGET)

def generar_target(df):
    return df.apply(calcular_riesgo, axis=1)
