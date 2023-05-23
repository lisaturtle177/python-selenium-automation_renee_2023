# Created by reneeherscovici at 5/22/23
Feature: Tests for Best Sellers page
  # Enter feature description here

  Scenario: Open Best Sellers page and verify 5 links
    Given Open amazon main page
    When User click on Best Sellers
    Then Verify 5 Best Sellers links

   