import pandas as pd

# Maneja los valores nulos en un DataFrame
def manejar_valores_nulos(df: pd.DataFrame, metodo: str = "fill", fill_value=None) -> pd.DataFrame:
    if metodo == "fill":
        return df.fillna(fill_value if fill_value is not None else "desconocido")
    elif metodo == "drop":
        return df.dropna()
    else:
        raise ValueError("El parámetro 'metodo' debe ser 'fill' o 'drop'.")

# Convierte texto a minúsculas y elimina espacios extra
def estandarizar_texto(df: pd.DataFrame, columnas: list[str]) -> pd.DataFrame:
    for col in columnas:
        if col in df.columns:
            df[col] = df[col].astype(str).str.lower().str.strip()
    return df

# Elimina un símbolo específico de una columna
def limpieza_especifica(df: pd.DataFrame, columna: str, simbolo: str = "$") -> pd.DataFrame:
    if columna in df.columns:
        df[columna] = df[columna].astype(str).str.replace(simbolo, "", regex=False).str.strip()
    return df

# Carga los archivos CSV de pacientes y citas
def cargar_datos(ruta_pacientes: str = "data/pacientes.csv", ruta_citas: str = "data/citas.csv") -> tuple[pd.DataFrame, pd.DataFrame]:
    pacientes = pd.read_csv(ruta_pacientes)
    citas = pd.read_csv(ruta_citas)
    return pacientes, citas

# Prueba rápida del módulo
if __name__ == "__main__":
    data = {
        "nombre": [" Ana ", "JUAN", None],
        "telefono": ["$123", "$456", "$789"],
        "edad": [25, None, 30]
    }

    df = pd.DataFrame(data)
    print("=== DataFrame original ===")
    print(df)

    df = manejar_valores_nulos(df, metodo="fill")
    df = estandarizar_texto(df, ["nombre"])
    df = limpieza_especifica(df, "telefono", simbolo="$")

    print("\n=== DataFrame limpio ===")
    print(df)
