# Created by brant at 9/28/2022
Feature: Cart

  Scenario: Users see "Your Amazon Cart is empty" notification after clicking on cart without adding any product
    Given Open Amazon home page
    When Click on Cart
    Then Verify "Your Amazon Cart is empty" notification is present


  Scenario: Users can search for coffee
    Given Open Amazon home page
    When Search for coffee
    Then Search results for "coffee" are shown


  Scenario Outline: Users can search for a product
    Given Open Amazon home page
    When Search for <product>
    Then Search results for <search_result> are shown
  Examples:
    | product                                   |search_result                                |
    | coffee                                    |"coffee"                                     |
    | mug                                       |"mug"                                        |
    | dress                                     |"dress"                                      |
    | Black Panther Luxury Car Seat Cover Front |"Black Panther Luxury Car Seat Cover Front"  |

  Scenario: Users can search products and add them to the cart
    Given Open Amazon home page
    When Search for Black Panther Luxury Car Seat Cover Front
    And Click on the first product
    And Store product name
    And Add the product to the cart
    And Click on Cart
    Then Verify cart has 1 item(s)
    And Verify cart has correct product



