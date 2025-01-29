Feature: Validate AWS DMS Full Load Process

  Scenario: Verify record count after full load
    Given the DMS task is completed successfully
    When we fetch the record count from source
    And we fetch the record count from target folder
    Then the record counts should match

  Scenario: Validate unique CDC source commit date
    Given the DMS full load is completed
    When we fetch the cdc_source_commit_date from the target table
    Then the cdc_source_commit_date should be a unique value