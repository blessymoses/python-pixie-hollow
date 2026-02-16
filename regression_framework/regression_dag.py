import os
import subprocess
from datetime import datetime

from airflow import DAG
from airflow.providers.python.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup

# Path to the features directory
FEATURES_DIR = os.path.join(os.path.dirname(__file__), "features")

def run_behave_tests(feature_file):
    """Execute behave tests for a given feature file."""
    subprocess.run(["behave", f"features/{feature_file}"])

# Define default DAG arguments
default_args = {
    "start_date": datetime(2025, 1, 1),
    "catchup": False
}

# Create the DAG
with DAG("datalake-regression-framework", default_args=default_args, schedule_interval="@daily") as dag:

    # Dynamically create task groups based on feature files
    feature_files = [f for f in os.listdir(FEATURES_DIR) if f.endswith(".feature")]

    task_groups = {}
    
    for feature_file in feature_files:
        task_group_name = feature_file.replace(".feature", "_tests")  # Example: full_load.feature → full_load_tests
        
        with TaskGroup(task_group_name) as task_group:
            PythonOperator(
                task_id=feature_file.replace(".feature", "_test"),
                python_callable=run_behave_tests,
                op_args=[feature_file]
            )

        task_groups[task_group_name] = task_group

    # Define dependencies dynamically (Sequential execution)
    prev_task_group = None
    for task_group_name, task_group in task_groups.items():
        if prev_task_group:
            prev_task_group >> task_group
        prev_task_group = task_group