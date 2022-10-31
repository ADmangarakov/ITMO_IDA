from datetime import datetime

from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

with DAG(
        dag_id="get_dataset",
        start_date=datetime(2022, 11, 1),
        catchup=False,
        schedule_interval="@once",
        tags=['test'],
) as dag:
    trigger = TriggerDagRunOperator(
        task_id="load_and_prepare_dataset",
        trigger_dag_id="get_dataset",  # Ensure this equals the dag_id of the DAG to trigger
        conf={"message": "Hello World"},
    )