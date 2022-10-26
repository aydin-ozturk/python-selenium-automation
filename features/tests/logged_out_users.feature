Feature: Tests for returns and orders

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon home page
    When Click on returns and orders
    Then Verify Sign In page is opened

