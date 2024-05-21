from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from src.product_availability_alert_run import run
# from userdata_test import main
from datetime import datetime, timedelta


dag_args ={
            "owner": "airflow",
            "retries": 1,
            "retry_delay": timedelta(minutes=5),
            "start_date": datetime(2021, 1, 1),
        }

dag = DAG (
    dag_id="product_availability_alert",
    schedule_interval="@daily",
    default_args=dag_args,
    catchup=False,
    description="product_availability_alert"
)

task = PythonOperator(
        task_id="product_availability_alert_run",
        python_callable=run,
        dag=dag
    )

task