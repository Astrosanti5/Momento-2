import pandas as pd

# ============================================================
# Manejo de valores nulos
# ============================================================
def manejar_valores_nulos(df: pd.DataFrame, metodo="fill", fill_value=None):
    """
    Maneja los valores nulos en un DataFrame.

    Parámetros:
    - df: DataFrame de entrada
    - metodo: "fill" (rellenar) o "drop" (eliminar)
    - fill_value: valor a usar si metodo="fill"

    Retorna:
    - DataFrame procesado
    """
    if metodo == "fill":
        return df.fillna(fill_value if fill_value is not None else "desconocido")
    elif metodo == "drop":
        return df.dropna()
    else:
        raise ValueError("El parámetro 'metodo' debe ser 'fill' o 'drop'")


# ============================================================
# Estandarización de texto
# ============================================================
def estandarizar_texto(df: pd.DataFrame, columnas: list):
    """
    Convierte texto a minúsculas y elimina espacios extra en las columnas indicadas.

    Parámetros:
    - df: DataFrame
    - columnas: lista de columnas a estandarizar

    Retorna:
    - DataFrame procesado
    """
    for col in columnas:
        if col in df.columns:
            df[col] = df[col].astype(str).str.lower().str.strip()
    return df


# ============================================================
# Limpieza específica de un campo
# ============================================================
def limpieza_especifica(df: pd.DataFrame, columna: str, simbolo="$"):
    """
    Limpia un símbolo específico de una columna (ejemplo: '$' en teléfonos).

    Parámetros:
    - df: DataFrame
    - columna: columna a limpiar
    - simbolo: símbolo o carácter a eliminar

    Retorna:
    - DataFrame procesado
    """
    if columna in df.columns:
        df[columna] = df[columna].astype(str).str.replace(simbolo, "", regex=False).str.strip()
    return df


# ============================================================
# Función para cargar CSV (antes estaba en analisis.py)
# ============================================================
def cargar_datos(ruta_pacientes="data/pacientes.csv", ruta_citas="data/citas.csv"):
    """
    Carga los archivos CSV de pacientes y citas.

    Retorna:
    - Tuple con DataFrames: (pacientes, citas)
    """
    pacientes = pd.read_csv(ruta_pacientes)
    citas = pd.read_csv(ruta_citas)
    return pacientes, citas
