import logging
import uuid
from typing import Any, Dict, Optional

import boto3

logger = logging.getLogger(__name__)

def submit_emr_on_eks_job(
    job_name: str,
    virtual_cluster_id: str,
    execution_role_arn: str,
    release_label: str,
    job_driver: Dict[str, Any],
    configuration_overrides: Optional[Dict[str, Any]] = None,
    tags: Optional[Dict[str, str]] = None
) -> str:
    """
    Submit a job to EMR on EKS.

    :param job_name: The name of the job.
    :param virtual_cluster_id: The ID of the EMR virtual cluster.
    :param execution_role_arn: The ARN of the IAM role for execution.
    :param release_label: EMR release label (e.g., emr-6.9.0-latest).
    :param job_driver: Dictionary specifying the job driver, such as sparkSubmitJobDriver.
    :param configuration_overrides: Optional configuration overrides.
    :param tags: Optional dictionary of tags to assign to the job.
    :return: Job run ID of the submitted EMR job.
    :raises Exception: If job submission fails.
    """
    client = boto3.client('emr-containers')
    try:
        response = client.start_job_run(
            name=job_name,
            virtualClusterId=virtual_cluster_id,
            executionRoleArn=execution_role_arn,
            releaseLabel=release_label,
            jobDriver=job_driver,
            configurationOverrides=configuration_overrides or {},
            tags=tags or {}
        )
        job_run_id = response['id']
        logger.info(f"Job submitted successfully. Job run ID: {job_run_id}")
        return job_run_id
    except Exception as e:
        logger.error(f"Failed to submit EMR on EKS job: {e}")
        raise

def get_job_status(virtual_cluster_id: str, job_run_id: str) -> str:
    """
    Get the status of a submitted EMR on EKS job.

    :param virtual_cluster_id: The ID of the EMR virtual cluster.
    :param job_run_id: The ID of the submitted job run.
    :return: The current state of the job run (e.g., RUNNING, SUCCEEDED, FAILED).
    :raises Exception: If job status retrieval fails.
    """
    client = boto3.client('emr-containers')
    try:
        response = client.describe_job_run(
            virtualClusterId=virtual_cluster_id,
            id=job_run_id
        )
        status = response['jobRun']['state']
        logger.info(f"Job status: {status}")
        return status
    except Exception as e:
        logger.error(f"Failed to get job status: {e}")
        raise
