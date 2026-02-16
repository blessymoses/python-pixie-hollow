Feature: Validate AWS DMS Change Data Capture (CDC)

  Scenario: Verify incremental data replication
    Given CDC is enabled for the DMS task
    When new records are inserted into the source table
    And the CDC process runs
    Then the new records should be available in the target folder

  Scenario: Verify CDC timestamp ordering
    Given CDC is enabled for the DMS task
    When updates are made in the source table
    Then the CDC event timestamps should be in sequential order