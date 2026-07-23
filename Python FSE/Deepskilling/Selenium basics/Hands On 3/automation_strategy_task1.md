# Hands-On 3 - Task 1: Automation Decision and Test Case Selection

## 17. Criteria for Automation

  -----------------------------------------------------------------------
  Criteria                Explanation             Applied to POST
                                                  /api/courses/
  ----------------------- ----------------------- -----------------------
  Repetitive              Frequently executed     Regression API test
                          tests                   should be automated

  Stable                  Requirements rarely     Endpoint behavior is
                          change                  stable

  High Risk               Business-critical       Course creation is
                          functionality           critical

  Data-Driven             Multiple input          Different course
                          combinations            payloads can be tested

  Time Saving             Reduces manual effort   Saves repeated manual
                                                  API validation
  -----------------------------------------------------------------------

## 18. Automate or Manual

  Test Case                 Decision   Reason
  ------------------------- ---------- ---------------------------------
  Regression CRUD           Automate   Executed after every build
  Exploratory Search        Manual     Requires human investigation
  Performance (100 users)   Automate   Load tools execute repeatedly
  Login UI                  Automate   Frequently validated
  Swagger Documentation     Manual     Mostly visual/content review
  Smoke Test                Automate   Executed after every deployment

## 19. Test Automation ROI

Automation effort = **4 hours**

Manual execution = **30 minutes (0.5 hour)**

Break-even = 4 ÷ 0.5 = **8 executions**

After the 10th execution, assume **20% maintenance overhead** per run.
Automation still provides significant long-term savings because
maintenance is much lower than recreating manual effort repeatedly.

## 20. Flaky Tests

**Definition:** A flaky test passes sometimes and fails other times
without application changes.

**Example:** A Selenium test fails because the page loads slower than
expected.

**Prevention** 1. Use Explicit Waits. 2. Avoid hard-coded sleeps. 3. Use
reliable locators and isolate test data.
