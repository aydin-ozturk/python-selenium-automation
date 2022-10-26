Feature: Cart

  Scenario: Users see "Your Amazon Cart is empty" notification after clicking on cart without adding any product
    Given Open Amazon home page
    When Click on Cart
    Then Verify "Your Amazon Cart is empty" notification is present


  Scenario: Users can search products and add them to the cart
    Given Open Amazon home page
    When Search for Black Panther Luxury Car Seat Cover Front
    And Click on the first product
    And Store product name
    And Add the product to the cart
    And Click on Cart
    Then Verify cart has 1 item(s)
    And Verify cart has correct product



