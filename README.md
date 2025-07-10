# 📦 Logistics AI Project

Este proyecto demuestra una solución integral de Inteligencia Artificial aplicada a la logística y transporte. Incluye predicción de demanda, optimización de rutas y cálculo de KPIs logísticos usando Python, Prophet, OR-Tools, Airflow y Streamlit.

## 🔧 Requisitos
- Python 3.10
- Docker (opcional para despliegue)

## 🚀 Instalación Local
```bash
pip install -r requirements.txt
streamlit run app/dashboard.py
```

## 🐳 Despliegue con Docker
```bash
docker build -t logistics-ai .
docker run -p 8501:8501 logistics-ai
```

## 🧠 Componentes
- `src/`: Lógica de procesamiento, predicción, ruteo y KPIs
- `dags/`: Pipeline automatizado con Apache Airflow
- `app/`: Visualización interactiva con Streamlit

## 📊 Dashboard
Muestra:
- Predicción de demanda por zona postal
- Ruta óptima generada
- KPIs logísticos clave (número de paradas, distancia total, eficiencia)

## 📅 Automatización (Airflow)
Puedes ejecutar el DAG desde la interfaz de Airflow para automatizar el pipeline:
```bash
airflow db init
airflow users create --username admin --password admin --role Admin --email admin@example.com
export AIRFLOW_HOME=.
airflow scheduler & airflow webserver
```

## ✨ Créditos
Creado como demostración para aplicar a posiciones de Desarrollador Senior de IA en logística y transporte.

    
