import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker("es_CO")

# -------------------------
# Función para generar pacientes
# -------------------------
def generar_pacientes(num_pacientes=200, archivo="patients.csv"):
    pacientes = []

    for i in range(1, num_pacientes + 1):
        nombre = fake.first_name()
        apellido = fake.last_name()
        documento = str(10000000 + i)
        telefono = str(3000000000 + i)
        correo = f"{nombre.lower()}.{apellido.lower()}@mail.com"
        fecha_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=80).strftime("%Y-%m-%d")
        ciudad = fake.city()
        pacientes.append([i, nombre, apellido, documento, telefono, correo, fecha_nacimiento, ciudad])

    with open(archivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "id_paciente", "nombre", "apellido", "documento", 
            "telefono", "correo", "fecha_nacimiento", "ciudad"
        ])
        writer.writerows(pacientes)

    print(f"✅ Se generaron {num_pacientes} pacientes en {archivo}")


# -------------------------
# Función para generar citas
# -------------------------
def generar_citas(num_citas=200, num_pacientes=200, archivo="appointments.csv"):
    citas = []

    for i in range(1, num_citas + 1):
        id_paciente = random.randint(1, num_pacientes)
        id_medico = random.randint(1, 100)       # médicos cargados en tu dataset
        id_consultorio = random.randint(1, 20)   # consultorios cargados en tu dataset
        fecha_cita = (datetime.today() + timedelta(days=random.randint(1, 90))).strftime("%Y-%m-%d")
        hora_cita = f"{random.randint(8, 16)}:{random.choice(['00','15','30','45'])}"
        motivo = random.choice([
            "Control dermatológico", 
            "Consulta estética", 
            "Tratamiento láser", 
            "Revisión postoperatoria", 
            "Chequeo preventivo"
        ])
        citas.append([i, id_paciente, id_medico, id_consultorio, fecha_cita, hora_cita, motivo])

    with open(archivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "id_cita", "id_paciente", "id_medico", 
            "id_consultorio", "fecha_cita", "hora_cita", "motivo"
        ])
        writer.writerows(citas)

    print(f"✅ Se generaron {num_citas} citas en {archivo}")


# -------------------------
# Función principal
# -------------------------
def generar_datos():
    generar_pacientes()
    generar_citas()


# -------------------------
# Punto de entrada
# -------------------------
if __name__ == "__main__":
    generar_datos()

    import pandas as pd

def cargar_datos():
    pacientes = pd.read_csv("patients.csv")
    citas = pd.read_csv("appointments.csv")
    return pacientes, citas


if __name__ == "__main__":
    # Generar los datos
    generar_datos()

    # Cargar los datos
    pacientes, citas = cargar_datos()

    # Mostrar primeros registros
    print("\n👩‍⚕️ Pacientes (primeros 5):")
    print(pacientes.head())

    print("\n📅 Citas (primeros 5):")
    print(citas.head())

