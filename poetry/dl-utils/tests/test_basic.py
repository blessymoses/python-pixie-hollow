import pytest
from dl_utils import athena_utils, s3_utils


def test_list_objects_empty(monkeypatch):
    class MockS3Client:
        def get_paginator(self, name):
            class Paginator:
                def paginate(self, Bucket, Prefix):
                    return [{'Contents': []}]
            return Paginator()

    monkeypatch.setattr("boto3.client", lambda service: MockS3Client())

    result = s3_utils.list_objects("dummy-bucket", prefix="test/")
    assert result == []

def test_run_athena_query(monkeypatch):
    class MockAthenaClient:
        def start_query_execution(self, QueryString, QueryExecutionContext, ResultConfiguration, WorkGroup):
            return {'QueryExecutionId': 'test-id'}

    monkeypatch.setattr("boto3.client", lambda service: MockAthenaClient())
    execution_id = athena_utils.run_athena_query("SELECT * FROM test", "default", "s3://output")
    assert execution_id == "test-id"
