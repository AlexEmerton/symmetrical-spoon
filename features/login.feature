@fixture.browser.chrome @login
Feature: Test the login page on Hudl.com

  Scenario: Login successfully when valid credentials are given
    Given the Hudl homepage is opened
    When I go to the login page
    And I enter the following credentials:
      | username      | password      |
      | env_user_name | env_user_pass |
    And I click on 'log in'
    Then I should see the logged-in dashboard

  Scenario Outline: Login successfully when valid credentials are given but username is in wrong casing
    Given the Hudl homepage is opened
    And the user login is in "<case>" case
    When I go to the login page
    And I enter the following credentials:
      | username      | password      |
      | env_user_name | env_user_pass |
    And I click on 'log in'
    Then I should see the logged-in dashboard
    Examples:
      | case        |
      | upper       |
      | lower       |
      | capitalized |

  Scenario: Login successfully when valid credentials are given and "Enter" key is pressed
    Given the Hudl homepage is opened
    When I go to the login page
    And I enter the following credentials:
      | username      | password      |
      | env_user_name | env_user_pass |
    And I hit "ENTER" on the keyboard
    Then I should see the logged-in dashboard

  Scenario Outline: Fail login when invalid credentials are given
    Given the Hudl homepage is opened
    When I go to the login page
    And I enter the following credentials:
      | username   | password   |
      | <username> | <password> |
    And I click on 'log in'
    Then the login should fail with the following message 'We didn't recognize that email and/or password. Need help?'
    Examples:
      | username            | password           |
      | some.email@mail.com | env_user_pass      |
      | env_user_name       | someWrongPassword? |

  Scenario Outline: Fail login when incomplete credentials are given
    Given the Hudl homepage is opened
    When I go to the login page
    And I enter the following credentials:
      | username   | password   |
      | <username> | <password> |
    And I click on 'log in'
    Then the login should fail with the following message 'We didn't recognize that email and/or password. Need help?'
    And the 'log in' button is disabled
    Examples:
      | username      | password      |
      | null          | env_user_pass |
      | env_user_name | null          |
      | null          | null          |

  Scenario Outline: Fail login when user password is correct but is in the wrong casing
    Given the Hudl homepage is opened
    And the user password is in "<case>" case
    When I go to the login page
    And I enter the following credentials:
      | username      | password        |
      | env_user_name | <env_user_pass> |
    And I click on 'log in'
    Then the login should fail with the following message 'We didn't recognize that email and/or password. Need help?'
    And the 'log in' button is disabled
    Examples:
      | case        |
      | upper       |
      | lower       |
      | capitalized |

  Scenario: Login page should be shown if user attempts to skip login
    Given the Hudl homepage is opened
    When I go to the logged-in dashboard
    Then I should see the login page

  Scenario: Remember me checkbox is clickable
    Given the Hudl homepage is opened
    When I go to the login page
    Then the 'Remember me' checkbox is clickable

  Scenario: Remember me checkbox is not on by default
    Given the Hudl homepage is opened
    When I go to the login page
    Then the 'Remember me' checkbox is not enabled

  Scenario: Log out should return user to the landing page
    Given the Hudl homepage is opened
    When I go to the login page
    And I enter the following credentials:
      | username      | password      |
      | env_user_name | env_user_pass |
    And I click on 'log in'
    Then I should see the logged-in dashboard
    When I log out
    Then I should see the landing page

  Scenario: the "Sign up" link works from the login page
    Given the Hudl homepage is opened
    When I go to the login page
    And I click on 'Sign up'
    Then I should see the sign up page

  Scenario: Show "Login Help" page when "Need Help?" is clicked
    Given the Hudl homepage is opened
    When I go to the login page
    And I click on 'Need help?'
    Then Login help is displayed
    And the 'send password reset' button is shown

  Scenario Outline: XSS in user credentials fields should not be executed
    Given the Hudl homepage is opened
    When I go to the login page
    And I enter the following credentials:
      | username   | password   |
      | <username> | <password> |
    And I click on 'log in'
    Then the login should fail with the following message 'We didn't recognize that email and/or password. Need help?'
    And no alert box should be displayed
    Examples:
      | username                        | password                        |
      | env_user_name                   | <script>alert("TEST");</script> |
      | <script>alert("TEST");</script> | env_user_pass                   |
