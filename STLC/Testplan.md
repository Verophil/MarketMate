# **Test Plan for Webshop Enhancements**

## **1. Analyse the Product**
   
### **Objective**

The primary objective of the product is to enhance the existing online shopping platform for groceries, household essentials and pet supplies by introducing 3 new features (rating system, age verification, free shipping) and ensuring the smooth functioning of existing functionalities.

### **User Base**

The product will be used by existing and new customers of the online shopping platform, primarily individuals and families purchasing groceries, household essentials, and pet supplies.

### **Hardware and Software Specifications**

- **Hardware Requirements:**
   - Devices: PCs, laptops, smartphones, tablets
   - Specifications: Standard configurations for Android and iOS devices, desktops with minimum 4GB RAM, 2GHz processor
- **Software Requirements:**
   - Operating Systems: Windows, macOS, Android, iOS
   - Browsers: Chrome, Firefox, Safari, Edge
   - Dependencies: Backend services, third-party ad services, payment gateways

### **Product Functionality**

**Existing Features**

- Register and login
- Search, filter, and sort products
- Add to favourites and basket
- Checkout: billing info, shipping address, payment methods
- Price calculation

**New Features**
- Product Rating System – Customers can rate products (1–5 stars) and optionally add written feedback.
- Age Verification for Alcoholic Products – A modal prompts users to enter their age when accessing alcoholic products; only users 18+ may proceed.
- Shipping Cost Changes – Orders above a threshold of 20 € qualify for free shipping; orders below are charged a shipping fee of 5€.

## **2. Design the Test Strategy**

### **Scope of Testing**

- **In Scope:**
   - Age verification 
   - Product rating and feedback
   - Shipping cost calculation 
   - Product detail pages
   - Basket calculation
   - Checkout process
   - Search results

- **Out of Scope:**

   - Backend database operations not affecting the user interface
   - Third party payment services integration


### **Type of Testing:**

- Functional Testing – Validate new features against requirements.
- Boundary Value Testing – Especially relevant for age verification and shipping threshold.
- Equivalence Partitioning – For text input in rating feedback and valid/invalid inputs.
- State Transition Testing – For scenarios like re-entering age verification or basket total updates.
- Regression Testing – Ensure existing functionalities are not broken.
- Usability Testing – Ensure smooth and intuitive interaction with new features.

### **Risks and Issues**

- **Delays in development**
    - Mitigation: Implement a buffer period in the schedule.
- **Lack of test data**
    - Mitigation: Create mock data sets for testing purposes.
- **Resource unavailability**
    - Mitigation: Identify backup resources.

### **Test Logistics**

- **Jane Smith** - Test Manager
- **John Doe** - QA Engineer (Functional and Regression Testing)
- **Alice Johnson** - QA Engineer (Performance and Security Testing)
- **Robert Brown** - QA Engineer (Usability Testing)
- **Maria Garcia** - End User for UAT

## **3. Define Test Objectives**

### **Objectives**

- **Functionality:** Ensure new features and existing functionalities work as intended.
- **GUI:** Verify the graphical user interface for usability and consistency.
- **Performance:** Confirm the system's performance under expected load conditions.
- **Security:** Identify and mitigate potential security vulnerabilities.
- **Usability:** Assess the user-friendliness of the platform.

### **Expected Outcomes**

- **Functionality:** All features perform correctly according to specifications.
- **GUI:** The interface is intuitive, responsive, and free of defects.
- **Performance:** The platform meets performance benchmarks under load.
- **Security:** No significant vulnerabilities are detected.
- **Usability:** Users can navigate and use the platform easily.

## **4. Define Test Criteria**

### **Suspension Criteria**

- Testing will be suspended if critical defects are found that block further testing.
- Lack of necessary resources or test environment failures.

### **Exit Criteria**

- All planned tests have been executed.
- Run Rate: At least 95% of all test cases have been executed.
- Pass Rate: At least 90% of executed test cases have passed.
- All critical and high-priority defects have been resolved and closed.
- No severity 1 or severity 2 defects are open.
- Performance metrics meet the defined standards.
- Security vulnerabilities have been identified and addressed.
- User acceptance testing has been completed, and sign-off has been obtained.

## **5. Resource Planning**

- **Human Resources:** QA team, development team, end users for UAT
- **Hardware:** PCs, laptops, smartphones, tablets
- **Software:** Browsers (Chrome, Firefox, Safari, Edge), operating systems (Windows, macOS, Android, iOS)
- **Infrastructure:** Test environments, automation tools, performance testing tools

## **6. Plan Test Environment**

- **Test Environments:** Real devices installed with real browsers and operating systems to simulate user conditions.
- **Environments:** Development (DEV), Testing (TEST), Acceptance (ACC), Production (PROD)

## **7. Schedule and Estimation**

| Activity | Start Date | End Date | Environment | Responsible Person | Estimated Effort |
| --- | --- | --- | --- | --- | --- |
| Test Planning | 01/08/2024 | 05/08/2024 | All | Test Manager | 20 hours |
| Test Case Design | 06/08/2024 | 15/08/2024 | All | QA Team | 40 hours |
| Unit Testing | 16/08/2024 | 25/08/2024 | DEV | Development Team | 60 hours |
| Integration Testing | 26/08/2024 | 30/08/2024 | TEST | QA Team | 30 hours |
| System Testing | 01/09/2024 | 10/09/2024 | TEST | QA Team | 80 hours |
| Regression Testing | 11/09/2024 | 15/09/2024 | TEST | QA Team | 40 hours |
| Performance Testing | 16/09/2024 | 18/09/2024 | TEST | QA Team | 20 hours |
| Security Testing | 19/09/2024 | 21/09/2024 | TEST | QA Team | 20 hours |
| UAT | 22/09/2024 | 30/09/2024 | ACC | End Users | 50 hours |
| Production Release | 01/10/2024 | 01/10/2024 | PROD | DevOps Team | 10 hours |

## **8. Determine Test Deliverables**

Documents/tools that must be created to support testing activities in the project:

- **Test Plan Document**
- **Test Cases and Test Scripts**
- **Test Data**
- **Test Reports**
- **Defect Reports**
- **UAT Sign-off Document**

