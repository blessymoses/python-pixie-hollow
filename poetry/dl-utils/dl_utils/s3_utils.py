"""
s3_utils.py

This module provides utility functions for interacting with Amazon S3 using Boto3.

Functions:
    list_objects(bucket_name: str, prefix: str = '') -> list[str]
    upload_file(file_path: str, bucket_name: str, object_name: str) -> None
    download_file(bucket_name: str, object_name: str, destination_path: str) -> None
"""

import logging
from typing import List

import boto3

logger = logging.getLogger(__name__)


def list_objects(bucket_name: str, prefix: str = '') -> List[str]:
    """
    List object keys in an S3 bucket under a given prefix.

    :param bucket_name: Name of the S3 bucket.
    :param prefix: Optional prefix to filter objects.
    :return: List of object keys.
    :raises: Exception if listing fails.
    """
    s3 = boto3.client('s3')
    try:
        paginator = s3.get_paginator('list_objects_v2')
        page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix)
        object_keys = []
        for page in page_iterator:
            for obj in page.get('Contents', []):
                object_keys.append(obj['Key'])
        return object_keys
    except Exception as e:
        logger.error(f"Error listing objects in bucket {bucket_name} with prefix {prefix}: {e}")
        raise


def upload_file(file_path: str, bucket_name: str, object_name: str) -> None:
    """
    Upload a file to an S3 bucket.

    :param file_path: Local path to the file.
    :param bucket_name: Name of the S3 bucket.
    :param object_name: S3 object name (key).
    :return: None
    :raises: Exception if upload fails.
    """
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        logger.info(f"Uploaded {file_path} to s3://{bucket_name}/{object_name}")
    except Exception as e:
        logger.error(f"Failed to upload {file_path} to s3://{bucket_name}/{object_name}: {e}")
        raise


def download_file(bucket_name: str, object_name: str, destination_path: str) -> None:
    """
    Download a file from an S3 bucket.

    :param bucket_name: Name of the S3 bucket.
    :param object_name: S3 object key to download.
    :param destination_path: Local path to save the downloaded file.
    :return: None
    :raises: Exception if download fails.
    """
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, object_name, destination_path)
        logger.info(f"Downloaded s3://{bucket_name}/{object_name} to {destination_path}")
    except Exception as e:
        logger.error(f"Failed to download s3://{bucket_name}/{object_name} to {destination_path}: {e}")
        raise
