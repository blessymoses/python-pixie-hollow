# import boto3

from utils.logger import logger


class AWSClient:
    def __init__(self):
        # self.dms_client = boto3.client("dms")
        logger.info("Boto3 client Initialized")

    def get_dms_task_status(self, task_id="task_1"):
        status = "successful"
        logger.info(f"Fetching DMS Task Status - Task ID: {task_id}, Status: {status}")
        return status

    def get_record_count(self, table_name):
        count = 100
        logger.info(f"Fetching record count for {table_name}: {count}")
        return count

    def get_cdc_commit_dates(self):
        return ["2024-01-29T10:00:00Z"]

    def is_cdc_enabled(self):
        return True

    def insert_dummy_data(self, table_name):
        pass

    def update_dummy_data(self, table_name):
        pass

    def trigger_cdc(self):
        pass

    def get_cdc_timestamps(self):
        return ["2024-01-29T10:00:00Z", "2024-01-29T10:05:00Z"]