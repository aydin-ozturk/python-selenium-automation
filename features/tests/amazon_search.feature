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
