# Created by brant at 9/28/2022
Feature: Cart

  Scenario: Users see "Your Amazon Cart is empty" notification after clicking on cart without adding any product
    Given Open Amazon home page
    When Click on Cart
    Then Verify "Your Amazon Cart is empty" notification is present