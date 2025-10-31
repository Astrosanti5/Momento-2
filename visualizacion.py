import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Función para graficar la frecuencia de los motivos de cita
def graficar_frecuencia_motivos(citas: pd.DataFrame, guardar=False, ruta="graficos/frecuencia_motivos.png"):
    # Contar cuántas veces aparece cada motivo de cita
    conteo_motivos = citas["motivo"].value_counts()

    # Crear la figura y el gráfico de barras
    plt.figure(figsize=(8, 5))
    sns.barplot(x=conteo_motivos.values, y=conteo_motivos.index, palette="viridis")

    # Título y etiquetas de ejes
    plt.title("Frecuencia de motivos de cita")
    plt.xlabel("Número de citas")
    plt.ylabel("Motivo")

    # Si guardar=True, se guarda la imagen en una carpeta
    if guardar:
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        plt.savefig(ruta, bbox_inches="tight")
        print(f"Gráfico guardado en {ruta}")
    else:
        # Si no, solo se muestra en pantalla
        plt.show()


# Función para graficar la distribución de citas por ciudad
def graficar_distribucion_por_ciudad(merged_df: pd.DataFrame, guardar=False, ruta="graficos/distribucion_ciudad.png"):
    # Agrupar por ciudad y contar cuántas citas tiene cada una
    citas_por_ciudad = merged_df.groupby("ciudad")["id_cita"].count().sort_values(ascending=False)

    # Crear la figura y el gráfico de barras
    plt.figure(figsize=(10, 5))
    sns.barplot(x=citas_por_ciudad.index, y=citas_por_ciudad.values, palette="coolwarm")

    # Título y etiquetas de ejes
    plt.title("Distribución de citas por ciudad")
    plt.xlabel("Ciudad")
    plt.ylabel("Número de citas")

    # Rotar los nombres de las ciudades para que se lean bien
    plt.xticks(rotation=45, ha="right")

    # Guardar o mostrar según el parámetro
    if guardar:
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        plt.savefig(ruta, bbox_inches="tight")
        print(f"Gráfico guardado en {ruta}")
    else:
        plt.show()


# Bloque principal: permite ejecutar el archivo directamente
if __name__ == "__main__":
    # Importar la función de análisis para cargar los datos ya limpios
    from analisis import cargar_y_preprocesar

    # Cargar los DataFrames de pacientes y citas
    pacientes, citas = cargar_y_preprocesar()

    # Unir pacientes y citas para poder analizar por ciudad
    merged = citas.merge(pacientes, on="id_paciente", how="inner")

    # Llamar las dos funciones de graficado
    graficar_frecuencia_motivos(citas)
    graficar_distribucion_por_ciudad(merged)