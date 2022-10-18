Feature: Test for product results

  Scenario: User can see a name and image of every product in search result
    Given Open Amazon home page
    When Search for "coffee"
    Then Verify every product has a name and image
