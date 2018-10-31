Feature: Just a basic test that google still works.

    Scenario: Test that google comes up.
        Given I open 'http://google.com/'
        When I check the page title
        Then the page title contains 'Google'
