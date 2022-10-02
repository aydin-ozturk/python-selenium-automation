# Created by brant at 9/28/2022
Feature: Cart

  Scenario: Users see "Your Amazon Cart is empty" notification after clicking on cart without adding any product
    Given Open Amazon home page
    When Click on Cart
    Then Verify "Your Amazon Cart is empty" notification is present


  Scenario: Users can search products and add them to the cart
    Given Open Amazon home page
    When Search for "Black Panther Luxury Car Seat Cover Front"
    When Select a product
    When Add the product to the cart
    When Click on Cart
    Then Then verify cart has 1 item(s)