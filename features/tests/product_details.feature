Feature: Tests for product details page

  Scenario: User can select colors
    Given Open amazon product B081YS2F7N page
    Then Verify user can click through colors
    
  Scenario: User can see New Arrivals in any clothing product result
    Given Open amazon product B074TBCSC8 page
    When Hover over New Arrivals
    Then Verify Women category is present in deals