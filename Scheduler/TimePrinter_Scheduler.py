from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import sys
import os

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

current_file_name=os.path.splitext(os.path.basename(sys.argv[0]))[0]

dag = DAG(current_file_name, default_args=default_args, schedule_interval='*/5 * * * *')


t1 = BashOperator(
    task_id='TimePrinter',
    bash_command='python /home/dmechelynck/Builds/Dummy-Api/code/Dummy-Api/TimePrinter.py',
    dag=dag)

t2 = BashOperator(
    task_id='TimePrinter2',
    bash_command='python /home/dmechelynck/Builds/Dummy-Api/code/Dummy-Api/TimePrinter.py',
    dag=dag)


t1.set_downstream(t2)
