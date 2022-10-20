Feature: Footer
  Scenario: Best seller footer links
    Given Open best seller page
    Then Verify footer has 5 link(s)
    Then Click on each link and verify header includes link name