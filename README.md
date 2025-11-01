# 🧠 Proyecto de Análisis y Visualización de Datos Médicos

## 📋 Descripción General

Este proyecto tiene como objetivo **limpiar, analizar, visualizar y generar reportes automáticos en HTML** a partir de un conjunto de datos médicos previamente procesados.  
Se emplean librerías como **Pandas**, **Matplotlib** y **Seaborn**, además de técnicas de integración y control de versiones con **Git y GitHub**.

Cada integrante del equipo trabajó en una rama independiente (*feature branch*) de acuerdo a su rol, y todos los desarrollos fueron integrados a las ramas de desarrollo (`Develop`, `Develop1`, `Develop2`, `Develop3`, `Develop4`) siguiendo buenas prácticas de versionamiento.

---

## 👥 Integrantes del Equipo y Roles

| Rol | Integrante | Rama Principal | Archivos / Responsabilidades |
|------|-------------|----------------|------------------------------|
| 🧹 **1. Data Engineer (Carga y Limpieza)** | **Santiago Cardona** | `Develop1` → `feature/preprocesamiento-limpio` | `src/preprocesamiento.py` — Revisión y documentación del módulo de limpieza, carga y estandarización de datos. |
| 📊 **2. Data Analyst (Análisis y Preparación)** | **Jerónimo Giraldo** | `Develop2` | `src/analisis.py` — Ejecución de análisis exploratorios (frecuencias, agrupaciones y conteos). Generación de DataFrames listos para graficar. |
| 📈 **3. Data Visualizer (Gráficos)** | **Nataly Álvarez** | `Develop3` | `src/visualizacion.py` — Creación del módulo de visualización con gráficos de frecuencia y distribución utilizando Matplotlib/Seaborn. |
| 🧾 **4. Report Designer (HTML y CSS)** | **George Valle** | `Develop4` | `reporte.html`, `estilos.css`, `src/generar_reporte.py` — Generación del reporte final en HTML que integra gráficos y tablas con estilo visual propio. |
| 🧠 **5. Documentador / Integrador Git** | **Gustavo Montoya (Tavo)** | `Develop` | `README.md`, `.gitignore`, estructura general — Creación de la rama `develop`, revisión de PRs, merges y documentación del proyecto. |

---

## 🧩 Estructura del Proyecto

📦 proyecto_datos_medicos/
┣ 📂 data/
┃ ┣ pacientes.csv
┃ ┗ citas.csv
┣ 📂 src/
┃ ┣ preprocesamiento.py # Carga y limpieza de datos
┃ ┣ analisis.py # Agrupaciones, conteos y análisis descriptivo
┃ ┣ visualizacion.py # Creación de gráficos con Matplotlib/Seaborn
┃ ┗ generar_reporte.py # Ensamble del reporte HTML final
┣ 📄 reporte.html # Reporte HTML con visualizaciones y tablas
┣ 📄 estilos.css # Estilos CSS aplicados al reporte
┣ 📄 requirements.txt # Librerías necesarias
┣ 📄 README.md # Documentación general del proyecto
┗ 📄 .gitignore # Archivos y carpetas ignoradas en Git

yaml
Copiar código

---

## ⚙️ Instalación y Ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone <URL-del-repositorio>
cd proyecto_datos_medicos
2️⃣ Crear y activar entorno virtual (opcional)
bash
Copiar código
python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows
3️⃣ Instalar dependencias
bash
Copiar código
pip install -r requirements.txt
4️⃣ Ejecutar el flujo de análisis completo
bash
Copiar código
python src/preprocesamiento.py
python src/analisis.py
python src/visualizacion.py
python src/generar_reporte.py
🧠 Flujo de Trabajo con Git
Cada integrante trabajó en su rama feature/ correspondiente.

Las ramas fueron integradas en orden:

feature/preprocesamiento-limpio → Develop1

feature/analisis-datos → Develop2

feature/visualizacion → Develop3

feature/reporte-html → Develop4

Finalmente, Gustavo Montoya (Integrador) fusionó todas las ramas en Develop, verificó la estructura final y actualizó la documentación.

Se generó un Pull Request desde Develop hacia main como entrega final.

🎨 Resultados Visuales
El reporte final (reporte.html) incluye:

Tablas interactivas exportadas desde Pandas.

Gráficos de barras y distribuciones generados con Matplotlib y Seaborn.

Estilo visual limpio y moderno definido en estilos.css.

(Opcional) Integración con DataTables.js para ordenar, filtrar y paginar las tablas.

📚 Librerías Principales
Pandas → Limpieza, análisis y exportación de datos.

Matplotlib / Seaborn → Visualización de gráficos.

Jinja2 / HTML / CSS → Generación del reporte HTML.

Git / GitHub → Control de versiones y gestión colaborativa.

🧹 Buenas Prácticas del Proyecto
Uso del flujo de ramas: main → develop → feature/*

Commits descriptivos y PRs revisados antes del merge.

Documentación actualizada en cada entrega.

Archivos temporales y datos sensibles excluidos mediante .gitignore.

🏁 Conclusión
El proyecto demuestra la integración completa de un flujo de análisis de datos:

Carga y limpieza de datos (Data Engineer).

Análisis exploratorio (Data Analyst).

Visualización efectiva (Data Visualizer).

Presentación profesional del resultado (Report Designer).

Integración y documentación final (Documentador Git).

El producto final es un reporte HTML autocontenido, con datos limpios, gráficos claros y una presentación coherente.

✍️ Autor del README y Documentación:
Gustavo Montoya (Tavo)
📅 Versión final integrada — Octubre 2025