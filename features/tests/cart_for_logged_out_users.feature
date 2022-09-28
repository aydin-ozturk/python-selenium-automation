# Created by brant at 9/28/2022
Feature: Cart for logged out user

  Scenario: Logged out users see "Your Amazon Cart is empty" notification after clicking on cart
    Given Open Amazon home page
    When Click on Cart
    Then Verify "Your Amazon Cart is empty" notification is present