import csv
import random
from faker import Faker
from datetime import datetime, timedelta
import pandas as pd

# Importar conexión y modelo de Diagnóstico
from config.db import SessionLocal
from models.diagnostico import Diagnostico

fake = Faker("es_CO")

# ============================================================
# Función para generar pacientes
# ============================================================
def generar_pacientes(num_pacientes=200, archivo="data/pacientes.csv"):
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


# ============================================================
# Función para generar citas
# ============================================================
def generar_citas(num_citas=200, num_pacientes=200, archivo="data/citas.csv"):
    citas = []
    for i in range(1, num_citas + 1):
        id_paciente = random.randint(1, num_pacientes)
        id_medico = random.randint(1, 100)       # médicos cargados
        id_consultorio = random.randint(1, 20)   # consultorios cargados
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


# ============================================================
# Función para generar diagnósticos (BD con SQLAlchemy)
# ============================================================
def generar_diagnosticos(num_diagnosticos=200):
    db = SessionLocal()
    pacientes_ids = list(range(1, 201))   # 200 pacientes
    medicos_ids = list(range(1, 101))     # 100 médicos

    diagnosticos = []
    for _ in range(num_diagnosticos):
        diagnostico = Diagnostico(
            id_paciente=random.choice(pacientes_ids),
            id_medico=random.choice(medicos_ids),
            fecha=fake.date_between(start_date="-2y", end_date="today"),
            descripcion=fake.sentence(nb_words=10),
            tratamiento=fake.text(max_nb_chars=100),
            observaciones=fake.sentence(nb_words=8)
        )
        diagnosticos.append(diagnostico)

    db.add_all(diagnosticos)
    db.commit()
    db.close()

    print(f"✅ Se insertaron {num_diagnosticos} diagnósticos en la base de datos")


# ============================================================
# Función principal
# ============================================================
def generar_datos():
    generar_pacientes()
    generar_citas()
    generar_diagnosticos()


# ============================================================
# Función para cargar CSV
# ============================================================
def cargar_datos():
    pacientes = pd.read_csv("data/pacientes.csv")
    citas = pd.read_csv("data/citas.csv")
    return pacientes, citas


# ============================================================
# Punto de entrada
# ============================================================
if __name__ == "__main__":
    # Generar los datos
    generar_datos()

    # Cargar CSV y mostrar registros
    pacientes, citas = cargar_datos()

    print("\n👩‍⚕️ Pacientes (primeros 20):")
    print(pacientes.head(20))

    print("\n📅 Citas (primeros 20):")
    print(citas.head(20))
