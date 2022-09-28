# Created by brant at 9/28/2022
Feature: Search a product and add to cart

  Scenario: Users can search products and add them to the cart
    Given Open Amazon home page
    When Search a product using search bar
    When Select a product
    When Add the product to the cart
    Then Verify "Added to Cart" is seen
