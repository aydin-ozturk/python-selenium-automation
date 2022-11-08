Feature: Tests for Amazon main page

  Scenario: User can see language options
    Given Open Amazon home page
    When Hover over language options
    Then Verify Spanish option is present