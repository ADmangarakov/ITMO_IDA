from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator

with DAG(
        dag_id='get_dataset',
        schedule_interval='@once',
        start_date=datetime(2022, 10, 25),
        catchup=False,
        tags=['test']
) as dag:
    run_this = BashOperator(
        task_id='get_dataset_and_prepare',
        bash_command='echo "get dataset success"',
    )



if __name__ == "__main__":
    dag.cli()