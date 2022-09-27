# Created by brant at 9/27/2022
Feature: Tests for returns and orders

  Scenario: Users are directed to sign in page when logged out
    Given Open Amazon home page
    When Click on returns and orders
    Then Redirected to sign in page with "Sign in" header and email input field

