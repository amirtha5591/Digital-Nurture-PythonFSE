# Hands-On 3 - Task 2: Automation Framework Types

## 21. Framework Comparison

  -------------------------------------------------------------------------------
  Framework        Description    Advantage         Disadvantage   Course
                                                                   Management
                                                                   Example
  ---------------- -------------- ----------------- -------------- --------------
  Linear           Sequential     Easy to learn     Poor           Small login
                   scripts                          maintenance    test

  Modular          Split into     High reusability  More planning  Reuse login
                   reusable                                        module
                   modules                                         

  Data-Driven      External test  Easy multiple     Test data      50 login
                   data           inputs            management     combinations

  Keyword-Driven   Keywords drive Non-programmers   Complex        Business users
                   execution      can contribute    framework      define steps

  Hybrid           Combines       Flexible and      Higher initial Enterprise
                   multiple       scalable          effort         Selenium suite
                   frameworks                                      
  -------------------------------------------------------------------------------

## 22. Recommendation

Recommended framework: **Hybrid (Modular + Data-Driven +
Keyword-Driven)**

Reasons: - Supports 50 login combinations using data files. - Login
module reused across many tests. - Keyword layer allows non-technical
team members to contribute.

## 23. Hybrid Framework Folder Structure

``` text
CourseManagementFramework/
│
├── config/
├── testdata/
│   └── login_data.xlsx
├── pages/
│   ├── LoginPage.py
│   └── DashboardPage.py
├── tests/
│   ├── test_login.py
│   └── test_courses.py
├── utilities/
│   ├── driver_factory.py
│   ├── logger.py
│   └── screenshot.py
├── keywords/
├── reports/
└── screenshots/
```
