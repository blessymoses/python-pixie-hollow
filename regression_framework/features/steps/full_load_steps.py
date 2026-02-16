from behave import given, then, when
from utils.aws_client import AWSClient
from utils.data_validator import DataValidator

aws_client = AWSClient()
validator = DataValidator()

@given("the DMS task is completed successfully")
def step_impl(context):
    context.dms_task = aws_client.get_dms_task_status()
    assert context.dms_task == "successful"

@when("we fetch the record count from source")
def step_impl(context):
    context.source_count = aws_client.get_record_count("source_table")

@when("we fetch the record count from target folder")
def step_impl(context):
    context.target_count = aws_client.get_record_count("target_table")

@then("the record counts should match")
def step_impl(context):
    assert context.source_count == context.target_count, "Record count mismatch!"

@given("the DMS full load is completed")
def step_impl(context):
    raise NotImplementedError('Not Implemented')

@when("we fetch the cdc_source_commit_date from the target table")
def step_impl(context):
    context.commit_dates = aws_client.get_cdc_commit_dates()

@then("the cdc_source_commit_date should be a unique value")
def step_impl(context):
    assert len(set(context.commit_dates)) == 1, "CDC source commit date is not unique"