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
