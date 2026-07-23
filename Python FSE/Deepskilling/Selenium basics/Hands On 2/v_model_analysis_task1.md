# Hands-On 2 - Task 1: V-Model Mapping

## 9. V-Model (ASCII)

``` text
Requirements -------------------------> Acceptance Testing
        \
System Design ------------------------> System Testing
          \
Architecture Design ------------------> Integration Testing
            \
Module Design ------------------------> Unit Testing
              \
               Coding
```

## 10. SDLC ↔ TDLC Mapping

  -----------------------------------------------------------------------
  SDLC Phase              TDLC Phase              Test Artifact Produced
  ----------------------- ----------------------- -----------------------
  Requirements            Acceptance Testing      Acceptance Test Plan &
                                                  Acceptance Test Cases

  System Design           System Testing          System Test Plan

  Architecture Design     Integration Testing     Integration Test Cases

  Module Design           Unit Testing            Unit Test Cases

  Coding                  Execution               Source Code & Test
                                                  Execution
  -----------------------------------------------------------------------

## 11. Entry & Exit Criteria

  -----------------------------------------------------------------------
  Testing Level           Entry Criteria          Exit Criteria
  ----------------------- ----------------------- -----------------------
  Unit Testing            Module completed        All unit tests pass, no
                                                  critical defects

  Integration Testing     Modules integrated      Interfaces verified,
                                                  major defects fixed

  System Testing          Complete application    Planned tests executed,
                          deployed                no High/Critical
                                                  defects

  Acceptance Testing      System testing          Customer approval
                          completed               received
  -----------------------------------------------------------------------

## 12. Early QA Engagement

1.  Review requirements to remove ambiguity and improve testability.
2.  Review architecture/design to identify integration risks and prepare
    test scenarios.
