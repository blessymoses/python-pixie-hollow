Feature: Validate data consistency in Datalake

  Scenario: Ensure no duplicate records in target
    Given the data is loaded into the target folder
    When we check for duplicate records
    Then there should be no duplicate records

  Scenario: Verify schema consistency between source and target
    Given the source and target schemas
    When we compare their structure
    Then the schemas should match