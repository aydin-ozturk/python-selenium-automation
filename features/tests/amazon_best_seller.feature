Feature: User can see the header includes link names when clicked
  Scenario: Click thru top links
    Given Open best seller page
    Then Verify footer has 5 link(s)
    Then Click on each link and verify footer includes link name