Feature: Add a content to the form
  As a user
  I want to be welcome
  So that I know I am on the right spot

  Background:
    When Logo is displayed
  @somke
  Scenario: Test transition between pages is ok
    Given Go to Form Page
    Then The Form Page should be displayed
    When go to home page
    Then the home page should be displayed

