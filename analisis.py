import csv
import random
import os
from faker import Faker
from datetime import datetime, timedelta
import pandas as pd

# SQLAlchemy (configurable via DATABASE_URL)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Intento de importar el modelo Diagnostico (si está disponible)
diagnosticos_df = pd.read_csv("data/diagnostico.csv")

# Intentar importar el modelo Diagnostico
try:
    diagnosticos_df = pd.read_csv("data/diagnostico.csv")
    DIAGNOSTICO_AVAILABLE = True
except Exception:
    diagnosticos_df = None
    DIAGNOSTICO_AVAILABLE = False

def mostrar_diagnosticos(n=5):
    """Muestra los primeros n diagnósticos del archivo CSV."""
    print(diagnosticos_df.head(n))

def generar_diagnosticos(num_diagnosticos=200):
    print("⚠️  No se utiliza el modelo Diagnostico. Función vacía o pendiente de implementación.")

# Importar módulo de preprocesamiento (asegúrate que src/__init__.py existe)
try:
    from data import preprocesamiento as pp
except Exception as e:
    raise ImportError(
        "No se pudo importar src.preprocesamiento. "
        "Asegúrate que src/preprocesamiento.py existe y src es un paquete."
    ) from e

fake = Faker("es_CO")

# -------------------------
# Configuración de la BD
# -------------------------
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# ============================================================
# Función para generar pacientes
# ============================================================
def generar_pacientes(num_pacientes=200, archivo="data/pacientes.csv"):
    os.makedirs(os.path.dirname(archivo), exist_ok=True)
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
    os.makedirs(os.path.dirname(archivo), exist_ok=True)
    citas = []
    for i in range(1, num_citas + 1):
        id_paciente = random.randint(1, num_pacientes)
        id_medico = random.randint(1, 100)       # médicos cargados
        id_consultorio = random.randint(1, 20)   # consultorios cargados
        fecha_cita = (datetime.today() + timedelta(days=random.randint(1, 90))).strftime("%Y-%m-%d")
        hora_cita = f"{random.randint(8, 16)}:{random.choice(['00', '15', '30', '45'])}"
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
    if not DIAGNOSTICO_AVAILABLE:
        print("⚠️  Modelo Diagnostico no disponible — se omite la inserción en BD.")
        return

    session = SessionLocal()
    try:
        pacientes_ids = list(range(1, 201))   # 200 pacientes
        medicos_ids = list(range(1, 101))     # 100 médicos

        diagnosticos = []
        for _ in range(num_diagnosticos):
            diagnostico = diagnostico(
                id_paciente=random.choice(pacientes_ids),
                id_medico=random.choice(medicos_ids),
                fecha=fake.date_between(start_date="-2y", end_date="today"),
                descripcion=fake.sentence(nb_words=10),
                tratamiento=fake.text(max_nb_chars=100),
                observaciones=fake.sentence(nb_words=8)
            )
            diagnosticos.append(diagnostico)

        session.add_all(diagnosticos)
        session.commit()
        print(f"✅ Se insertaron {num_diagnosticos} diagnósticos en la base de datos")
    except Exception as e:
        session.rollback()
        print("❌ Error al insertar diagnósticos en la BD:", e)
    finally:
        session.close()


# ============================================================
# Función principal
# ============================================================
def generar_datos():
    generar_pacientes()
    generar_citas()
    generar_diagnosticos()


# ============================================================
# Cargar y preprocesar (usa funciones desde src.preprocesamiento)
# ============================================================
def cargar_y_preprocesar():
    pacientes, citas = pp.cargar_datos(
        ruta_pacientes="data/pacientes.csv",
        ruta_citas="data/citas.csv"
    )

    pacientes = pp.manejar_valores_nulos(pacientes, metodo="fill", fill_value="desconocido")
    citas = pp.manejar_valores_nulos(citas, metodo="drop")

    pacientes = pp.estandarizar_texto(pacientes, ["nombre", "apellido", "ciudad"])
    pacientes = pp.limpieza_especifica(pacientes, "telefono", simbolo="$")

    return pacientes, citas


# ============================================================
# Punto de entrada
# ============================================================
if __name__ == "__main__":
    # Generar los datos (si ya existen los CSV puedes comentar esta línea)
    generar_datos()

    # ============================================================
# Punto de entrada
# ============================================================
if __name__ == "__main__":
    # Generar los datos (si ya existen, puedes comentar esta línea)
    generar_datos()

    # Cargar y limpiar los datos
    pacientes, citas = cargar_y_preprocesar()

    # ========================================================
    # 1. Análisis de Frecuencia:
    # ¿Cuál es el motivo de cita más frecuente?
    # ========================================================
    motivo_mas_frecuente = citas["motivo"].value_counts().idxmax()
    print("\n📊 Análisis de Frecuencia")
    print("Motivo más frecuente de cita:", motivo_mas_frecuente)

    # ========================================================
    # 2. Análisis de Agregación:
    # Número de citas por ciudad del paciente
    # (requiere merge entre citas y pacientes)
    # ========================================================
    merged = citas.merge(pacientes, on="id_paciente", how="inner")
    citas_por_ciudad = merged.groupby("ciudad")["id_cita"].count()
    print("\n📊 Análisis de Agregación")
    print("Número de citas por ciudad:")
    print(citas_por_ciudad)

    # ========================================================
    # 3. Análisis con Filtrado y Conteo:
    # ¿Cuántas citas son de 'Control dermatológico'?
    # ========================================================
    control_count = citas[citas["motivo"] == "Control dermatológico"].shape[0]
    print("\n📊 Análisis con Filtrado y Conteo")
    print("Número de controles dermatológicos:", control_count)

