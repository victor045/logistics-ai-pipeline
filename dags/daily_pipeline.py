import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.data_processing import load_data
from src.demand_model import predict_demand
from src.route_optimizer import optimize_routes
from src.kpi_calculator import calculate_kpis

with DAG(
    'daily_logistics_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['logistics', 'ai'],
) as dag:

    task_load_data = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
    )

    task_predict_demand = PythonOperator(
        task_id='predict_demand',
        python_callable=predict_demand,
    )

    task_optimize_routes = PythonOperator(
        task_id='optimize_routes',
        python_callable=optimize_routes,
    )

    task_calculate_kpis = PythonOperator(
        task_id='calculate_kpis',
        python_callable=calculate_kpis,
    )

    task_load_data >> task_predict_demand >> task_optimize_routes >> task_calculate_kpis
