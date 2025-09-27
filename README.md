# Proyecto: Análisis de Datos - Clínica Dermatológica  

## Momento 2 - Aplicación de análisis de datos en Python  

---

### 📌 Descripción del Proyecto  
Este proyecto implementa un sistema de análisis de datos para una *clínica dermatológica*.  
Incluye un módulo de *preprocesamiento* y un script principal (analisis.py) que permiten:  

- Limpiar y preparar datos.  
- Unir y combinar información de diferentes fuentes (.csv).  
- Responder preguntas clave de análisis.  
- Imprimir resultados en consola como evidencia.  

Los datos simulados representan:  
- Pacientes  
- Médicos  
- Consultorios  
- Clínicas  
- Diagnósticos  
- Citas médicas  

---

## 📂 Estructura del Proyecto  

MOMENTO-2/
│── data/
│ ├── citas.csv
│ ├── clinica.csv
│ ├── consultorio.csv
│ ├── diagnostico.csv
│ ├── medico.csv
│ ├── pacientes.csv
│── preprocesamiento.py
│── analisis.py
│── README.md
│── .venv/

yaml
Copiar código

---

## 🔀 Flujo de Git (Git Flow)  

El proyecto fue gestionado con *Git Flow*:  

- Rama principal protegida: main  
- Rama de trabajo base: develop  
- Ramas de características:  
  - feature/carga-datos → Función para cargar datos.  
  - feature/limpieza-datos → Manejo de nulos, estandarización y limpieza.  
  - feature/analisis-frecuencia → Pregunta de análisis #1.  
  - feature/analisis-agregacion → Pregunta de análisis #2.  
  - feature/analisis-filtrado → Pregunta de análisis #3.  
  - feature/consultas-extras → Últimos 50, intermedios, ciudad con más pacientes.  

Cada rama fue integrada a develop mediante *Pull Requests (PRs)*, y finalmente a main.  

---

## ⚙️ Configuración del entorno  

1. Clonar el repositorio:  
   ```bash
   git clone <URL_DEL_REPO>
   cd MOMENTO-2
Crear y activar entorno virtual:

bash
Copiar código
python -m venv .venv
.venv\Scripts\activate   # En Windows
source .venv/bin/activate   # En Linux/Mac
Instalar dependencias (pandas):

bash
Copiar código
pip install pandas
Ejecutar el análisis:

bash
Copiar código
python analisis.py
🧩 Funcionalidades Clave
1. Preprocesamiento
Carga de datos.

Manejo de valores nulos.

Normalización de texto.

Limpieza específica del proyecto.

2. Análisis
Preguntas respondidas:

Análisis de Frecuencia: elemento con mayor cantidad de registros (ejemplo: diagnóstico más repetido).

Agregación: métrica agrupada por categoría (ejemplo: número total de citas por médico).

Filtrado + Conteo: segmentación por condición (ejemplo: cuántos pacientes están en tratamiento dermatológico).

3. Consultas Extra
Número total de controles dermatológicos: 48

Últimos 50 registros.

50 intermedios.

Ciudad con más pacientes.

📝 Paso a paso: Cómo registrar nueva información
Nueva cita

Abrir citas.csv

Agregar una fila con: ID_CITA, ID_PACIENTE, ID_MEDICO, FECHA, CONSULTORIO, DIAGNOSTICO

Nuevo paciente

Abrir pacientes.csv

Agregar fila con: ID_PACIENTE, NOMBRE, EDAD, GENERO, CIUDAD

Nuevo médico

Abrir medico.csv

Agregar fila con: ID_MEDICO, NOMBRE, ESPECIALIDAD, CLINICA

Nueva clínica

Abrir clinica.csv

Agregar fila con: ID_CLINICA, NOMBRE, CIUDAD

Nuevo diagnóstico

Abrir diagnostico.csv

Agregar fila con: ID_DIAGNOSTICO, NOMBRE_DIAGNOSTICO

Nuevo consultorio

Abrir consultorio.csv

Agregar fila con: ID_CONSULTORIO, NUMERO, PISO, CLINICA

💻 Bloque final de código (analisis.py)
Este bloque imprime la evidencia extra:

python
Copiar código
import pandas as pd

# Cargar datos principales
pacientes = pd.read_csv("data/pacientes.csv")
citas = pd.read_csv("data/citas.csv")

print("\n=== CONSULTAS EXTRA ===")

# Últimos 50 registros
print("\n🔹 Últimos 50 registros de citas:")
print(citas.tail(50))

# 50 registros intermedios
mitad = len(citas) // 2
print("\n🔹 50 registros intermedios de citas:")
print(citas.iloc[mitad:mitad+50])

# Ciudad con más pacientes
print("\n🔹 Ciudad con más pacientes registrados:")
print(pacientes["CIUDAD"].value_counts().head(1))
📊 Ejemplo de salida esperada
yaml
Copiar código
=== CONSULTAS EXTRA ===

🔹 Últimos 50 registros de citas:
     ID_CITA   ID_PACIENTE   ID_MEDICO   FECHA   CONSULTORIO   DIAGNOSTICO
200  201 ...   ...

🔹 50 registros intermedios de citas:
     ID_CITA   ID_PACIENTE   ...

🔹 Ciudad con más pacientes registrados:
Bogotá    120
Name: CIUDAD, dtype: int64
✅ Con este README.md tienes:

Documentación del proyecto.

Explicación de Git Flow con ramas.

Paso a paso para agregar registros.

Código final integrado en analisis.py.

Ejemplo de resultados en consola.

yaml
Copiar código

---

Ahora tu README no tiene:  
- Bloques yaml innecesarios.  
- "Copiar código" duplicado.  
- Numeración mal indentada.  
- Comentarios dentro de bloques que rompen Markdown.  

👉 Con este formato ya no deberías ver alertas en VS Code ni en GitHub.  
