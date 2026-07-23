# Hands-On 1 - Task 1

## QA Testing Types

### 1. Testing Levels

  -----------------------------------------------------------------------
  Testing Type            Test Case               Classification
  ----------------------- ----------------------- -----------------------
  Unit Testing            Test the function that  Functional
                          validates course        
                          details before saving.  

  Integration Testing     Verify the POST         Functional
                          `/api/courses/`         
                          endpoint correctly      
                          stores data in the      
                          database.               

  System Testing          Create a course through Functional
                          the API and verify it   
                          is stored and retrieved 
                          successfully.           

  User Acceptance Testing A college administrator Functional
  (UAT)                   creates a new course    
                          and confirms it appears 
                          in the course list.     
  -----------------------------------------------------------------------

### 2. Functional vs Non-Functional

Functional testing verifies whether the API behaves according to
requirements.

**Non-Functional Example**

-   Performance Testing: Verify the Course Management API responds
    within **2 seconds** for 100 concurrent users.

### 3. Black-Box vs White-Box Testing

  -----------------------------------------------------------------------
  Black-Box Testing                   White-Box Testing
  ----------------------------------- -----------------------------------
  Tests functionality without seeing  Tests internal code, logic,
  the source code.                    branches, and conditions.

  Focuses on inputs and outputs.      Focuses on implementation.

  Mostly performed by QA Engineers.   Mostly performed by Developers.
  -----------------------------------------------------------------------

### 4. Formal Test Cases

  ----------------------------------------------------------------------------------------
  Test Case  Description   Preconditions   Test Steps  Expected     Actual     Pass/Fail
  ID                                                   Result       Result     
  ---------- ------------- --------------- ----------- ------------ ---------- -----------
  TC-001     Create a      API running     Send POST   HTTP 201 and            
             course with                   request     course                  
             valid data                    with valid  created                 
                                           JSON                                

  TC-002     Create course API running     Omit course HTTP 400                
             with missing                  name        validation              
             required                                  error                   
             field                                                             

  TC-003     Create        Existing course Send        Duplicate               
             duplicate     present         duplicate   rejected                
             course                        course      with proper             
                                           request     message                 
  ----------------------------------------------------------------------------------------

## Expected Outcome

-   Testing levels identified
-   Functional and non-functional testing explained
-   Black-box vs White-box comparison completed
-   Three formal test cases documented
