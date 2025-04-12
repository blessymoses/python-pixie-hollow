import logging
import time
from typing import Any, Dict, Optional

import boto3

logger = logging.getLogger(__name__)


def run_athena_query(
    query: str,
    database: str,
    output_location: str,
    workgroup: str = 'primary'
) -> str:
    """
    Run an Athena query and return the execution ID.

    :param query: SQL query to run in Athena.
    :param database: The name of the Athena database.
    :param output_location: S3 URI where the query results are stored.
    :param workgroup: Optional workgroup to run the query in.
    :return: Athena query execution ID.
    :raises Exception: If the query execution fails.
    """
    client = boto3.client('athena')
    try:
        response = client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={'Database': database},
            ResultConfiguration={'OutputLocation': output_location},
            WorkGroup=workgroup
        )
        execution_id = response['QueryExecutionId']
        logger.info(f"Athena query started: {execution_id}")
        return execution_id
    except Exception as e:
        logger.error(f"Failed to start Athena query: {e}")
        raise


def wait_for_query_completion(
    execution_id: str,
    timeout: int = 300,
    interval: int = 5
) -> str:
    """
    Wait for an Athena query to complete and return its final status.

    :param execution_id: The ID of the Athena query execution.
    :param timeout: Maximum time in seconds to wait for completion.
    :param interval: Polling interval in seconds.
    :return: Final state of the query (e.g., SUCCEEDED, FAILED).
    :raises TimeoutError: If the query does not complete within the timeout.
    """
    client = boto3.client('athena')
    start_time = time.time()
    while True:
        response = client.get_query_execution(QueryExecutionId=execution_id)
        status = response['QueryExecution']['Status']['State']
        if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            return status
        if time.time() - start_time > timeout:
            raise TimeoutError(f"Query {execution_id} timed out after {timeout} seconds.")
        time.sleep(interval)


def get_query_results(
    execution_id: str,
    max_results: int = 1000
) -> Dict[str, Any]:
    """
    Fetch the results of a completed Athena query.

    :param execution_id: The ID of the completed query.
    :param max_results: Maximum number of results to retrieve.
    :return: ResultSet dictionary containing the query results.
    :raises Exception: If the results cannot be retrieved.
    """
    client = boto3.client('athena')
    try:
        response = client.get_query_results(QueryExecutionId=execution_id, MaxResults=max_results)
        return response['ResultSet']
    except Exception as e:
        logger.error(f"Failed to fetch results for query {execution_id}: {e}")
        raise
