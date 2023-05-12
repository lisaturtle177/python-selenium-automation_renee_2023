# Created by reneeherscovici at 5/12/23
Feature: Amazon Signin tests, Cart, etc.
    Scenario: Logged out User sees Sign In Page When clicking Returns and Orders
    Given Go to amazon main page
    When Click on Orders and Returns
    Then Verify sign in page opens


    Scenario: Clicking on Cart icon verifies cart is empty
    Given Go to amazon main page
    When Click on cart icon
    Then Verify cart is empty

#this fails when I try to place the item in the cart, need to work on that
    Scenario: Add Items to cart and verify in cart
    Given Go to amazon main page
    When User adds item to cart
    When Click on cart icon
    Then Verify item is in cart