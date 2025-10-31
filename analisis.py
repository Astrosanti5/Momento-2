import pandas as pd
import matplotlib.pyplot as plt

# =========================
#  CARGA DE DATOS
# =========================
try:
    citas = pd.read_csv("citas.csv")
    print("✅ Archivo cargado correctamente.\n")
except FileNotFoundError:
    print("❌ No se encontró el archivo 'citas.csv'. Asegúrate de tenerlo en la misma carpeta que analisis.py.")
    exit()

# =========================
#  VISTA INICIAL DE LOS DATOS
# =========================
print("Primeras 5 filas del archivo:")
print(citas.head(), "\n")

print("Información general del DataFrame:")
print(citas.info(), "\n")

# =========================
#  LIMPIEZA DE DATOS
# =========================
# Convertir fechas y horas a tipo datetime si es necesario
citas["fecha_cita"] = pd.to_datetime(citas["fecha_cita"], errors='coerce')
citas["hora_cita"] = pd.to_datetime(citas["hora_cita"], errors='coerce').dt.time

# Eliminar filas con fechas inválidas
citas = citas.dropna(subset=["fecha_cita"])

# =========================
#  ANÁLISIS GENERAL
# =========================
print("📊 Total de citas registradas:", len(citas))
print("👨‍⚕️ Médicos únicos:", citas["id_medico"].nunique())
print("🧍 Pacientes únicos:", citas["id_paciente"].nunique(), "\n")

# =========================
#  CITAS POR MÉDICO
# =========================
citas_por_medico = citas["id_medico"].value_counts()
print("Citas por médico:\n", citas_por_medico, "\n")

# Gráfico de citas por médico
plt.figure(figsize=(8, 4))
citas_por_medico.plot(kind="bar", color="skyblue")
plt.title("Número de citas por médico")
plt.xlabel("ID Médico")
plt.ylabel("Cantidad de citas")
plt.tight_layout()
plt.show()

# =========================
#  CITAS POR DÍA
# =========================
citas_por_dia = citas.groupby("fecha_cita").size()
print("Citas por día:\n", citas_por_dia, "\n")

plt.figure(figsize=(8, 4))
citas_por_dia.plot(kind="line", marker="o")
plt.title("Cantidad de citas por día")
plt.xlabel("Fecha")
plt.ylabel("Número de citas")
plt.tight_layout()
plt.show()

# =========================
#  HORAS MÁS FRECUENTES
# =========================
if "hora_cita" in citas.columns:
    horas = citas["hora_cita"].astype(str).value_counts().head(5)
    print("🕒 Horas más frecuentes de cita:\n", horas, "\n")

# =========================
#  MOTIVOS DE CONSULTA
# =========================
if "motivo" in citas.columns:
    motivos = citas["motivo"].value_counts()
    print("Motivos más comunes de cita:\n", motivos, "\n")

    plt.figure(figsize=(6, 4))
    motivos.head(5).plot(kind="barh", color="lightgreen")
    plt.title("Motivos más comunes de cita")
    plt.xlabel("Cantidad")
    plt.ylabel("Motivo")
    plt.tight_layout()
    plt.show()

print("✅ Análisis completado exitosamente.")
