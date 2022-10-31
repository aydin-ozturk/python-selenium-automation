Feature: Product search

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

  Scenario Outline: Users can search products in a specific department
    Given Open Amazon home page
    When Select department by value <value>
    And Search for <product>
    Then Verify <department> department is selected
  Examples:
    |value        |product        |department       |
    |pets         |aquarium       |pet-supplies     |
    |electronics  |camera         |electronics      |
    |computers    |dell           |pc               |


