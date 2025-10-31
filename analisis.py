# analisis.py
import pandas as pd
from data.preprocesamiento import (
    cargar_datos,
    manejar_valores_nulos,
    estandarizar_texto,
    limpieza_especifica
)

# ==========================================
# 🔹 FUNCIONES DE ANÁLISIS PRINCIPALES
# ==========================================

# 1️⃣ Muestra información general del DataFrame
def resumen_general(df: pd.DataFrame, nombre_df: str = "DataFrame"):
    print(f"\n=== Resumen general de {nombre_df} ===")
    print(df.info())
    print("\nPrimeras filas:")
    print(df.head())
    print("\nEstadísticas descriptivas:")
    print(df.describe(include="all", datetime_is_numeric=True))

# 2️⃣ Cuenta la cantidad de valores nulos por columna
def valores_nulos(df: pd.DataFrame):
    print("\n=== Valores nulos por columna ===")
    print(df.isnull().sum())

# 3️⃣ Calcula cuántos pacientes hay por EPS o ciudad (si existen esas columnas)
def distribucion_por_columna(df: pd.DataFrame, columna: str):
    if columna in df.columns:
        print(f"\n=== Distribución por {columna} ===")
        print(df[columna].value_counts())
    else:
        print(f"\n⚠️ La columna '{columna}' no existe en el DataFrame.")

# 4️⃣ Analiza la frecuencia de citas por paciente
def citas_por_paciente(citas: pd.DataFrame):
    if "id_paciente" in citas.columns:
        print("\n=== Número de citas por paciente ===")
        resumen = citas["id_paciente"].value_counts().reset_index()
        resumen.columns = ["id_paciente", "cantidad_citas"]
        print(resumen.head())
        return resumen
    else:
        print("⚠️ La columna 'id_paciente' no existe en el archivo de citas.")
        return pd.DataFrame()

# 5️⃣ Muestra la cantidad de citas por mes (si existe 'fecha_cita')
def citas_por_mes(citas: pd.DataFrame):
    if "fecha_cita" in citas.columns:
        citas["fecha_cita"] = pd.to_datetime(citas["fecha_cita"], errors="coerce")
        resumen = citas["fecha_cita"].dt.to_period("M").value_counts().sort_index()
        print("\n=== Citas por mes ===")
        print(resumen)
        return resumen
    else:
        print("⚠️ No existe la columna 'fecha_cita'.")
        return pd.Series()

# ==========================================
# 🔹 BLOQUE PRINCIPAL DE EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    # Cargar datos
    pacientes, citas = cargar_datos()

    # Preprocesamiento básico
    pacientes = manejar_valores_nulos(pacientes, metodo="fill")
    pacientes = estandarizar_texto(pacientes, ["nombre", "apellido"])
    citas = manejar_valores_nulos(citas, metodo="fill")

    # Limpiar símbolos si hay columnas de costo o teléfono
    if "telefono" in pacientes.columns:
        pacientes = limpieza_especifica(pacientes, "telefono", simbolo="$")
    if "costo" in citas.columns:
        citas = limpieza_especifica(citas, "costo", simbolo="$")

    # Análisis general
    resumen_general(pacientes, "Pacientes")
    resumen_general(citas, "Citas")

    # Conteo de valores nulos
    valores_nulos(pacientes)
    valores_nulos(citas)

    # Distribución por EPS (si existe)
    distribucion_por_columna(pacientes, "eps")

    # Análisis de citas
    citas_por_paciente(citas)
    citas_por_mes(citas)
