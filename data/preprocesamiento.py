# data/preprocesamiento.py
import pandas as pd
from typing import Tuple, List

# ----------------------------------------------------------
# Maneja los valores nulos en un DataFrame
# ----------------------------------------------------------
def manejar_valores_nulos(df: pd.DataFrame, metodo: str = "fill", fill_value=None) -> pd.DataFrame:
    if metodo == "fill":
        return df.fillna(fill_value if fill_value is not None else "desconocido")
    elif metodo == "drop":
        return df.dropna()
    else:
        raise ValueError("El parámetro 'metodo' debe ser 'fill' o 'drop'.")


# ----------------------------------------------------------
# Convierte texto a minúsculas y elimina espacios extra
# ----------------------------------------------------------
def estandarizar_texto(df: pd.DataFrame, columnas: List[str]) -> pd.DataFrame:
    for col in columnas:
        if col in df.columns:
            df[col] = df[col].astype(str).str.lower().str.strip()
    return df


# ----------------------------------------------------------
# Elimina un símbolo específico de una columna
# ----------------------------------------------------------
def limpieza_especifica(df: pd.DataFrame, columna: str, simbolo: str = "$") -> pd.DataFrame:
    if columna in df.columns:
        df[columna] = df[columna].astype(str).str.replace(simbolo, "", regex=False).str.strip()
    return df


# ----------------------------------------------------------
# Carga los archivos CSV de pacientes y citas
# ----------------------------------------------------------
def cargar_datos(ruta_pacientes: str = "data/pacientes.csv", ruta_citas: str = "data/citas.csv") -> Tuple[pd.DataFrame, pd.DataFrame]:
    try:
        pacientes = pd.read_csv(ruta_pacientes)
        citas = pd.read_csv(ruta_citas)
    except FileNotFoundError as e:
        print(f"❌ Error al cargar archivos CSV: {e}")
        raise
    return pacientes, citas


# ----------------------------------------------------------
# Función principal de carga y limpieza
# ----------------------------------------------------------
def cargar_datos_limpios() -> Tuple[pd.DataFrame, pd.DataFrame]:
    pacientes, citas = cargar_datos()
    pacientes = manejar_valores_nulos(pacientes, metodo="fill", fill_value="desconocido")
    citas = manejar_valores_nulos(citas, metodo="drop")
    pacientes = estandarizar_texto(pacientes, ["nombre", "apellido", "ciudad"])
    pacientes = limpieza_especifica(pacientes, "telefono", simbolo="$")
    return pacientes, citas


# ----------------------------------------------------------
# Prueba rápida
# ----------------------------------------------------------
if __name__ == "__main__":
    pacientes, citas = cargar_datos_limpios()
    print("✅ Datos cargados y preprocesados correctamente.")
    print(pacientes.head())
    print(citas.head())
