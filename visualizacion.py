# visualizacion.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid", palette="pastel")

# ----------------------------------------------------------
# Gráfico de frecuencia (categorías)
# ----------------------------------------------------------
def graficar_frecuencia_motivos(citas: pd.DataFrame, guardar=False, ruta="graficos/frecuencia_motivos.png"):
    if "motivo" not in citas.columns:
        raise ValueError("La columna 'motivo' no existe en el DataFrame de citas.")
    conteo_motivos = citas["motivo"].value_counts()
    plt.figure(figsize=(8, 5))
    sns.barplot(x=conteo_motivos.values, y=conteo_motivos.index, palette="viridis")
    plt.title("Frecuencia de motivos de cita")
    plt.xlabel("Número de citas")
    plt.ylabel("Motivo")
    if guardar:
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        plt.savefig(ruta, bbox_inches="tight")
        print(f"Gráfico guardado en {ruta}")
    else:
        plt.show()


# ----------------------------------------------------------
# Gráfico de distribución por ciudad
# ----------------------------------------------------------
def graficar_distribucion_por_ciudad(merged_df: pd.DataFrame, guardar=False, ruta="graficos/distribucion_ciudad.png"):
    if "ciudad" not in merged_df.columns or "id_cita" not in merged_df.columns:
        raise ValueError("El DataFrame combinado debe tener las columnas 'ciudad' e 'id_cita'.")
    citas_por_ciudad = merged_df.groupby("ciudad")["id_cita"].count().sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=citas_por_ciudad.index, y=citas_por_ciudad.values, palette="coolwarm")
    plt.title("Distribución de citas por ciudad")
    plt.xlabel("Ciudad")
    plt.ylabel("Número de citas")
    plt.xticks(rotation=45, ha="right")
    if guardar:
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        plt.savefig(ruta, bbox_inches="tight")
        print(f"Gráfico guardado en {ruta}")
    else:
        plt.show()
