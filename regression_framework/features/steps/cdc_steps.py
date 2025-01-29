from behave import given, then, when
from utils.aws_client import AWSClient

aws_client = AWSClient()

@given("CDC is enabled for the DMS task")
def step_impl(context):
    context.cdc_enabled = aws_client.is_cdc_enabled()
    assert context.cdc_enabled, "CDC is not enabled"

@when("new records are inserted into the source table")
def step_impl(context):
    aws_client.insert_dummy_data("source_table")

@when("the CDC process runs")
def step_impl(context):
    aws_client.trigger_cdc()

@then("the new records should be available in the target folder")
def step_impl(context):
    source_count = aws_client.get_record_count("source_table")
    target_count = aws_client.get_record_count("target_table")
    assert source_count == target_count, "CDC data replication failed!"

@when("updates are made in the source table")
def step_impl(context):
    aws_client.update_dummy_data("source_table")

@then("the CDC event timestamps should be in sequential order")
def step_impl(context):
    timestamps = aws_client.get_cdc_timestamps()
    assert timestamps == sorted(timestamps), "CDC timestamps are not in order"