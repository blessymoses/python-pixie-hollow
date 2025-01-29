from behave import given, then, when
from utils.data_validator import DataValidator

validator = DataValidator()

@given("the data is loaded into the target folder")
def step_impl(context):
    context.data_loaded = validator.check_data_loaded()
    assert context.data_loaded, "Data not loaded"

@when("we check for duplicate records")
def step_impl(context):
    context.duplicates = validator.get_duplicate_records()

@then("there should be no duplicate records")
def step_impl(context):
    assert context.duplicates == 0, "Duplicates found in target data"

@given("the source and target schemas")
def step_impl(context):
    context.source_schema = validator.get_schema("source_table")
    context.target_schema = validator.get_schema("target_table")

@when("we compare their structure")
def step_impl(context):
    context.schema_match = validator.compare_schemas()

@then("the schemas should match")
def step_impl(context):
    assert context.schema_match, "Schema mismatch between source and target"