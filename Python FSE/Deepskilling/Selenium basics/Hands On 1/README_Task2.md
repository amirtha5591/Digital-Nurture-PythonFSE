# Hands-On 1 - Task 2

## Defect Lifecycle & Severity Classification

### 1. Defect Lifecycle

New → Assigned → Open → Fixed → Retest → Verified → Closed

Additional paths: - Rejected: Issue is not a defect or cannot be
reproduced. - Deferred: Fix postponed to a future release.

### 2. Severity & Priority

  -----------------------------------------------------------------------
  Bug               Severity          Priority          Justification
  ----------------- ----------------- ----------------- -----------------
  POST returns 500  Critical          P1                Core
  for all requests                                      functionality
                                                        unavailable

  Course name \>150 Medium            P2                Data integrity
  chars truncated                                       affected

  Swagger page typo Low               P4                Cosmetic issue
                                                        only

  Login             High              P1                Intermittent
  occasionally                                          authentication
  returns 401                                           failure
  -----------------------------------------------------------------------

### 3. Defect Report

  Field             Value
  ----------------- -------------------------------------
  Defect ID         DEF-001
  Title             POST /api/courses/ returns HTTP 500
  Environment       Windows 11, Chrome, Local API
  Build Version     v1.0
  Severity          Critical
  Priority          P1
  Steps             Start API → Send valid POST request
  Expected Result   Course created successfully
  Actual Result     HTTP 500 Internal Server Error
  Attachments       Screenshot of 500 error

### 4. Severity vs Priority

-   **Severity** measures the impact of the defect.
-   **Priority** measures how urgently it should be fixed.

**Example:** A spelling mistake on the CEO's dashboard has **Low
Severity** but **High Priority** because it affects an important
demonstration.

## Expected Outcome

-   Defect lifecycle documented
-   Severity and priority classified
-   Defect report completed
-   Severity vs Priority explained
