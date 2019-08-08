from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

import time
n=time.strftime("%Y,%m,%d")
v=datetime.strptime(n,"%Y,%m,%d")
default_args = {
    'owner': 'airflow',
    'depends_on_past': True,
    'start_date': v,
    'email': ['diego@agilytic.be'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),

}

dag = DAG('TimePrinterDag', default_args=default_args, schedule_interval='*/5 * * * *')

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='TimePrinter',
    bash_command='python /home/dmechelynck/Builds/Dummy-Api/code/Dummy-Api/TimePrinter.py',
    dag=dag)