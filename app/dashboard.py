
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Logistics AI Dashboard", layout="wide")
st.title("📦 Dashboard Logístico con IA")

# Mostrar predicción de demanda
st.header("🔮 Predicción de Demanda por Zona Postal")
pred_path = os.path.join('data', 'predicted_demand.csv')
if os.path.exists(pred_path):
    pred_df = pd.read_csv(pred_path)
    latest = pred_df['ds'].max()
    st.dataframe(pred_df[pred_df['ds'] == latest])
else:
    st.warning("No se encontró archivo de predicción")

# Mostrar ruta óptima
st.header("🗺️ Ruta Óptima Calculada")
route_path = os.path.join('data', 'optimized_route.txt')
if os.path.exists(route_path):
    with open(route_path, 'r') as f:
        route = f.read().split('->')
    st.markdown("**Secuencia de Entregas:**")
    st.write(" → ".join(route))
else:
    st.warning("Ruta no disponible")

# Mostrar KPIs logísticos
st.header("📊 Indicadores de Desempeño (KPIs)")
distance_path = os.path.join('data', 'route_distance.txt')
if os.path.exists(distance_path) and route_path:
    with open(distance_path, 'r') as f:
        distance = int(f.read())
    num_stops = len(route)
    avg = distance / num_stops if num_stops else 0
    st.metric("Paradas Totales", num_stops)
    st.metric("Distancia Total (m)", distance)
    st.metric("Distancia Promedio por Parada (m)", f"{avg:.2f}")
else:
    st.warning("No se encontraron datos para KPIs")

