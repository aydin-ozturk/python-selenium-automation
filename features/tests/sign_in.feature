
Feature: Sign in test cases

  Scenario: Sign in page can be opened from sign in pop up button
    Given Open Amazon home page
    When Click on sign in pop up
    Then Verify Sign In page is opened


  Scenario: Users can see sign in pop up button
    Given Open Amazon home page
    Then Verify sign in pop up button is clickable
    When Wait for 5 sec
    Then Verify sign in pop up button is clickable
    Then Verify sign in pop up button disappears

