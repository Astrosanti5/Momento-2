<<<<<<< HEAD
<<<<<<< HEAD
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Configuración general de estilo visual
sns.set(style="whitegrid", palette="pastel")

# Gráfico de frecuencia (para variables categóricas)
def grafico_frecuencia(df: pd.DataFrame, columna: str, titulo: str = "Gráfico de Frecuencia"):
    if columna not in df.columns:
        raise ValueError(f"La columna '{columna}' no existe en el DataFrame.")

    conteo = df[columna].value_counts().reset_index()
    conteo.columns = [columna, "Frecuencia"]

    plt.figure(figsize=(8, 5))
    sns.barplot(x=columna, y="Frecuencia", data=conteo)
    plt.title(titulo)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Gráfico de distribución (para variables numéricas)
def grafico_distribucion(df: pd.DataFrame, columna: str, titulo: str = "Gráfico de Distribución"):
    if columna not in df.columns:
        raise ValueError(f"La columna '{columna}' no existe en el DataFrame.")

    plt.figure(figsize=(8, 5))
    sns.histplot(df[columna].dropna(), kde=True, color="skyblue")
    plt.title(titulo)
    plt.xlabel(columna)
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()

# Prueba del módulo con un DataFrame de ejemplo
if __name__ == "__main__":
    data = {
        "genero": ["F", "M", "F", "M", "F", "F", "M"],
        "edad": [23, 45, 31, 28, 35, 40, 22]
    }
    df = pd.DataFrame(data)

    grafico_frecuencia(df, "genero", "Distribución por Género")
    grafico_distribucion(df, "edad", "Distribución de Edad")
=======
=======

>>>>>>> 8392cb88ac37cd0533da496600641c6778a0521e
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
<<<<<<< HEAD
>>>>>>> bac5252b8b34a06c78a43a52917887fe45807db2
=======
>>>>>>> 8392cb88ac37cd0533da496600641c6778a0521e
