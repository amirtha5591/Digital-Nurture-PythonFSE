# Hands-On 2 - Task 2: Agile QA & Shift-Left Testing

## 13. Problems with Waterfall

1.  Defects are discovered late, increasing fixing cost.
2.  Requirement misunderstandings remain unnoticed until testing.
3.  Delayed customer feedback may require major rework.

## 14. QA Role in Agile Ceremonies

  -----------------------------------------------------------------------
  Ceremony                            QA Responsibility
  ----------------------------------- -----------------------------------
  Sprint Planning                     Define acceptance criteria and
                                      estimate testing effort

  Daily Stand-up                      Report testing progress and
                                      blockers

  Sprint Review                       Validate completed stories and
                                      demonstrate functionality

  Retrospective                       Suggest process improvements and
                                      prevent recurring defects
  -----------------------------------------------------------------------

## 15. Shift-Left Practices

  -----------------------------------------------------------------------
  Practice                            Application to Course Management
                                      API
  ----------------------------------- -----------------------------------
  Requirements Review                 Verify requirements are complete
                                      and testable

  Test Cases Before Code (TDD/BDD)    Prepare scenarios before
                                      implementation

  Static Code Analysis                Detect coding issues using
                                      automated tools

  API Contract Testing                Validate API schema before service
                                      integration
  -----------------------------------------------------------------------

## 16. Acceptance Criteria (Given-When-Then)

### Scenario 1: Successful Course Creation

``` gherkin
Given the admin is logged in
When valid course details are submitted
Then the course is created successfully
```

### Scenario 2: Duplicate Course Code

``` gherkin
Given a course code already exists
When the admin submits the same course code
Then an appropriate duplicate error is displayed
```

### Scenario 3: Missing Required Fields

``` gherkin
Given the admin leaves mandatory fields empty
When the course is submitted
Then validation errors are displayed and the course is not created
```
