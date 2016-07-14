Feature: User Management

  Scenario Outline: Available user types appear in the user list
    Given I've added the user "<users>"
    When I go to the user list in the Admin application
    Then I should find the name "<name>", admin role "<admin>" and active state "<active>"

    Examples:
      | users              | name | admin | active |
      | admin001@gmail.com | John | True  | True   |
      | user002@gmail.com  | Eric | False | True   |
      | user003@gmail.com  | John | False | False  |