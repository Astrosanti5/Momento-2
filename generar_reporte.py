import os
import pandas as pd
from analisis import cargar_datos, manejar_valores_nulos, estandarizar_texto
from visualizacion import graficar_frecuencia_motivos, graficar_distribucion_por_ciudad

# ==============================
# 🔹 Funciones auxiliares
# ==============================

def insertar_tabla_en_html(df: pd.DataFrame, plantilla_html: str, salida_html: str):
    """Inserta una tabla de pandas en el HTML base."""
    with open(plantilla_html, "r", encoding="utf-8") as f:
        html_base = f.read()

    tabla_html = df.to_html(classes="display", index=False)
    html_final = html_base.replace("{{TABLA_HTML}}", tabla_html)

    with open(salida_html, "w", encoding="utf-8") as f:
        f.write(html_final)

    print(f"✅ Reporte HTML generado en: {salida_html}")


# ==============================
# 🔹 Generador principal
# ==============================

def generar_reporte():
    # Rutas de archivos
    ruta_html_base = "../reporte.html"
    ruta_html_final = "../reporte_final.html"
    ruta_assets = "../assets"

    # Crear carpeta para imágenes
    os.makedirs(ruta_assets, exist_ok=True)

    # Cargar datos limpios
    try:
        pacientes, citas = cargar_datos()
        pacientes = manejar_valores_nulos(pacientes)
        citas = manejar_valores_nulos(citas)
        pacientes = estandarizar_texto(pacientes, ["nombre"])
    except Exception as e:
        print("⚠️ Error al cargar datos. Se usarán datos de ejemplo:", e)
        pacientes = pd.DataFrame({
            "id_paciente": [1, 2, 3],
            "nombre": ["Ana", "Juan", "María"],
            "ciudad": ["Bogotá", "Medellín", "Cali"],
            "eps": ["Sura", "Sanitas", "Coomeva"]
        })
        citas = pd.DataFrame({
            "id_cita": [101, 102, 103, 104, 105],
            "id_paciente": [1, 1, 2, 3, 3],
            "motivo": ["Chequeo", "Dermatitis", "Consulta", "Control", "Chequeo"]
        })

    # Unir pacientes con citas
    merged = citas.merge(pacientes, on="id_paciente", how="inner")

    # Generar los gráficos reales
    graficar_frecuencia_motivos(citas, guardar=True, ruta=os.path.join(ruta_assets, "frecuencia_motivos.png"))
    graficar_distribucion_por_ciudad(merged, guardar=True, ruta=os.path.join(ruta_assets, "distribucion_ciudad.png"))

    # Insertar tabla de pacientes al reporte HTML
    insertar_tabla_en_html(pacientes.head(10), ruta_html_base, ruta_html_final)


if __name__ == "__main__":
    generar_reporte()
