import pandas as pd
import requests
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


def my_cool_fn(message):
    print(f'Secret message: {message}')

default_args = {
    'start_date': datetime(2024, 9, 9)
}

with DAG(
    dag_id='api_data_extraction',
    default_args=default_args,
    default_view='graph'
) as dag:

    first_task = PythonOperator(
        task_id='test_task_id',
        python_callable=my_cool_fn,
        op_args=['OMG IT WORKED? HURRAY!']
	)

    first_task

if __name__ == '__main__':
    dag.cli()
