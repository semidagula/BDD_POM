Feature: Home page, welcome message
  As a user
  I want to be welcome
  So that I know I am on the right spot
@somke

  Scenario: Check welcome message
    When logo is displayed
    Then I should see "Welcome to Formy"


