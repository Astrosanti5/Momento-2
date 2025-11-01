# integracion_visualizacion.py
"""
Script de integración entre preprocesamiento y visualización
"""

import os
import pandas as pd
from data.preprocesamiento import cargar_datos_limpios
from visualizacion import graficar_frecuencia_motivos, graficar_distribucion_por_ciudad


# ----------------------------------------------------------
# Cargar y combinar datos
# ----------------------------------------------------------
def cargar_datos_integrados() -> tuple[pd.DataFrame | None, pd.DataFrame | None, pd.DataFrame | None]:
    try:
        pacientes, citas = cargar_datos_limpios()
        if "id_paciente" not in pacientes.columns or "id_paciente" not in citas.columns:
            raise KeyError("La columna 'id_paciente' no existe en pacientes o citas.")
        merged_df = citas.merge(pacientes, on="id_paciente", how="inner")
        print("✅ Datos cargados y combinados correctamente.")
        return pacientes, citas, merged_df
    except Exception as e:
        print(f"❌ Error al cargar datos: {e}")
        return None, None, None


# ----------------------------------------------------------
# Generar gráficos
# ----------------------------------------------------------
def generar_graficos(pacientes: pd.DataFrame, citas: pd.DataFrame, merged_df: pd.DataFrame):
    if merged_df is None:
        print("⚠️ No se pueden generar gráficos porque los datos combinados son nulos.")
        return
    os.makedirs("graficos", exist_ok=True)
    try:
        graficar_frecuencia_motivos(citas, guardar=True)
        graficar_distribucion_por_ciudad(merged_df, guardar=True)
        print("✅ Gráficos generados y guardados correctamente en 'graficos/'.")
    except Exception as e:
        print(f"❌ Error al generar gráficos: {e}")


# ----------------------------------------------------------
# Bloque principal
# ----------------------------------------------------------
if __name__ == "__main__":
    pacientes, citas, merged_df = cargar_datos_integrados()
    generar_graficos(pacientes, citas, merged_df)
