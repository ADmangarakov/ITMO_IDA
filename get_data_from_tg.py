from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator

with DAG(
        dag_id='get_from_tg',
        schedule_interval='@daily',
        start_date=datetime(2022, 10, 25),
        catchup=False,
        tags=['test']
) as dag:
    get_and_save = BashOperator(
        task_id='get_from_tg_and_save',
        bash_command='echo "get from tg success"',
    )



if __name__ == "__main__":
    dag.cli()