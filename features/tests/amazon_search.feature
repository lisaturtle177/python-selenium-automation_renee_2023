# Created by reneeherscovici at 5/12/23
Feature: Amazon Search tests

  Scenario: User can search for table on Amazon
    Given Open amazon main page
    When Search for table
    Then Verify search results shown for "table"

   Scenario: User can search for coffee on Amazon
    Given Open amazon main page
    When Search for coffee
    Then Verify search results shown for "coffee"

     #hw 5 extra exercise
  Scenario: User can search for dress on Amazon
    Given Open amazon main page
    When Search for dress
    Then Verify that every product has a name and an image

   Scenario Outline:User can search on Amazon
     Given Open amazon main page
     When Search for <search_word>
     Then Verify search results shown for <search_result>
     Examples:
     |search_word|  |search_result|
     |table|        |"table"      |
     |coffee|       |"coffee"       |