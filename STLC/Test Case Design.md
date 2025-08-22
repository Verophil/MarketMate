### **1. Product Rating System**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), State Transition Testing, Error Guessing

### Test Cases

1. **Boundary Value Analysis**
  - **Test Case**: Verify minimum rating (1 star) can be submitted.
    - **Input**: Rating = 1 star, no feedback.
    - **Expected Outcome**: Rating saved successfully and displayed immediately.

2. **Boundary Value Analysis**
  - **Test Case**: Verify maximum rating (5 stars) can be submitted.
    - **Input**: Rating = 5 stars, no feedback.
    - **Expected Outcome**: Rating saved successfully and displayed immediately.

3. **Boundary Value Analysis**
  - **Test Case**: Verify feedback with exactly 500 characters.
    - **Input**: Rating = 3 stars, Feedback = 500 characters.
    - **Expected Outcome**: Rating + feedback saved successfully.

4. **Boundary Value Analysis**
  - **Test Case**: Verify feedback exceeding 500 characters is rejected.
    - **Input**: Rating = 4 stars, Feedback = 501 characters.
    - **Expected Outcome**: Error message "Feedback cannot exceed 500 characters."

5. **Equivalence Partitioning**
  - **Test Case**: Verify rating without purchase is not possible.
    - **Input**: User without purchase tries to rate.
    - **Expected Outcome**: Error message "You can only rate purchased products."

6. **Equivalence Partitioning**
  - **Test Case**: Verify rating with and without feedback.
    - **Input**:
      - Case 1: Rating = 5 stars, Feedback = empty.
      - Case 2: Rating = 4 stars, Feedback = "Great product".
    - **Expected Outcome**: Both cases accepted.

7. **State Transition Testing**
  - **Test Case**: Verify user can edit rating after submission.
    - **Input**: Submit 2 stars → Edit to 4 stars.
    - **Expected Outcome**: Updated rating displayed immediately.

8. **Error Guessing**
  - **Test Case**: Verify behavior when feedback contains only spaces.
    - **Input**: Rating = 3 stars, Feedback = "   ".
    - **Expected Outcome**: Treated as empty → Rating saved without feedback.Error Guessing

9. **Error Guessing**
  - **Test Case**: Verify system behavior when user attempts to submit 0 stars with feedback.
    - **Input**: Rating = 0 stars, Feedback = "Bad product".
    - **Expected Outcome**: Error message "Minimum rating is 1 star."


### **2. Age Verification for Alcoholic Products**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing

### Test Cases

1. **Boundary Value Analysis**
  - **Test Case**: Verify access for user exactly 18 years old.
    - **Input**: Date of Birth = Today - 18 years.
    - **Expected Outcome**: Access to alcoholic products granted.

2. **Boundary Value Analysis**
  - **Test Case**: Verify restriction for user 1 day below 18.
    - **Input**: Date of Birth = Today - 18 years + 1 day.
    - **Expected Outcome**: Message "You are underage. You can still browse the site, but you will not be able to view alcohol products."

3. **Equivalence Partitioning**
  - **Test Case**: Verify users under 18 can still browse non-alcoholic products.
    - **Input**: User 17 years old logs in and searches for "bread".
    - **Expected Outcome**: Bread is visible, alcoholic products are hidden.

4. **Equivalence Partitioning**
  - **Test Case**: Verify adult user can browse all products.
    - **Input**: User 25 years old logs in.
    - **Expected Outcome**: Both alcoholic and non-alcoholic products visible.

5. **Error Guessing**
  - **Test Case**: Verify system behavior when DOB field left empty during registration.
    - **Input**: No date entered.
    - **Expected Outcome**: Error message "Date of Birth is required."

6. **Error Guessing**
  - **Test Case**: Verify invalid DOB format.
    - **Input**: "13/25/2008"
    - **Expected Outcome**: Error message "Invalid Date of Birth format. Please use MM-DD-YYYY.“

7. **Error Guessing**
  - **Test Case**: Verify system behavior when user enters an unrealistic age (e.g. 150 years old).
    - **Input**: Date of Birth = 01-01-1875 (→ 150 years old).
    - **Expected Outcome**: Error message "Please enter a valid date of birth."

### **3. Shipping Cost Changes**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), State Transition Testing, Error Guessing

### Test Cases

1. **Boundary Value Analysis**
  - **Test Case**: Verify order exactly at 20€ qualifies for free shipping.
    - **Input**: Basket total = 20€.
    - **Expected Outcome**: Free shipping applied, final cost = 20€.

2. **Boundary Value Analysis**
  - **Test Case**: Verify order at 19.99€ incurs 5€ shipping.
    - **Input**: Basket total = 19.99€.
    - **Expected Outcome**: Shipping fee = 5€, final cost = 24.99€.

3. **Equivalence Partitioning**
  - **Test Case**: Verify orders below threshold always incur shipping fee.
    - **Input**: Basket total = 10€.
    - **Expected Outcome**: Shipping fee applied.

4. **Equivalence Partitioning**
  - **Test Case**: Verify orders above threshold always free shipping.
    - **Input**: Basket total = 50€.
    - **Expected Outcome**: Free shipping applied.
    
5. **State Transition Testing**
  - **Test Case**: Verify shipping fee updates dynamically when basket value crosses threshold.
    - **Input**: Add items: Basket = 15€ → Add product → Basket = 25€.
    - **Expected Outcome**: Shipping changes from 5€ to 0€ automatically.

6. **Error Guessing**
  - **Test Case**: Verify system behavior when basket is empty.
    - **Input**: Basket total = 0€.
    - **Expected Outcome**: Checkout blocked, message "Your basket is empty."
