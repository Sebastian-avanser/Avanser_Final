import re

def limpiar_nombre_columna(col_name):
    col_name = str(col_name)

    col_name = col_name.replace('Ã³', 'ó').replace('Ã±', 'ñ').replace('Ã¡', 'á')
    col_name = col_name.replace('Ã©', 'é').replace('Ãº', 'ú').replace('Ã­', 'í')
    col_name = col_name.replace('Â¿', '').replace('¿', '').replace('Â', '')
    col_name = col_name.replace('?', '').replace(':', '')
    col_name = re.sub(r'\s+', ' ', col_name)  
    col_name = col_name.strip()

    return col_name


def limpiar_nombres_columnas(df):
    df = df.copy()
    df.columns = [limpiar_nombre_columna(col) for col in df.columns]

    print("\n--- Columnas Limpias ---")
    print(df.columns.tolist())

    return df
