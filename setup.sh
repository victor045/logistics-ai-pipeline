
#!/bin/bash
export AIRFLOW_HOME=.
airflow db init
airflow users create --username admin --password admin --firstname admin --lastname admin --role Admin --email admin@example.com
echo "Airflow configurado. Ejecuta: airflow scheduler & airflow webserver"

