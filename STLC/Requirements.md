## **The Software**

Webshop with the following existing functionalities:

- Register and login
- Search, filter, and sort products
- Add to favourites and basket
- Checkout: billing info, shipping address, payment methods
- Price calculation

## **New features**

- Product Rating System
- Age Verification for Alcoholic Products
- Shipping Cost Changes

## **New features**

### **1. Product Rating System**
      
**Vague Requirement:**

Users should be able to rate products with a 5-star system and have the option to add written feedback.

**Critical Questions:**

1. Who can rate products? Everyone or registered users only? After purchase only?
2.  Can users change or delete their ratings?
3.  Are there limitations to the feedback (e.g. character count, language moderation, content filters)?
4.  Are ratings published immediately or only after review?
5.  How many ratings per user and product are allowed?
6.  Is it possible to leave a star rating only, or must feedback always be included?

**Detailed Requirement:**

- Ratings are only possible after the product has been purchased.
- Users can submit either a star rating only or a star rating with written feedback.
- Feedback may contain up to 500 characters.
- Minimum rating is 1 star.
- No language or content filters are applied.
- Ratings and feedback are published immediately.
- Users can edit their rating and feedback at any time, but only one rating per product per user is allowed.

### **2. Age Verification for Alcoholic Products**

**Vague Requirement:**

1. Alcoholic products require age verification.
2. A modal should appear when navigating to the alcoholic products category asking if the user is 18+.
3. Users must input their age before accessing the alcoholic products.

**Critical Questions:**

1. How is the age requested (date of birth input, checkbox)?
2. What happens if the user is under 18 (partial access, full restriction, error message)?
3. When is the age verification required (when creating the account only or everytime when tryig to access alcoholic products)?
4. How is the age verified (self-disclosure only or document upload)?
5. When exactly does the modal appear (product link, category page, add-to-cart)?
6. How are products with alcohol content in food (e.g. cake, chocolates) handled?

**Detailed Requirement:**

- Age verification is required once when creating an account for the first time by entering the date of birth in the format MM-DD-YYYY.
- Self-disclosure of age is sufficient (no document upload required).
- Customers under 18 may browse the site but cannot view alcoholic products. They are shown an appropriate message instead.
- There are no products such as cakes or chocolates containing alcohol. 

### **3. Shipping Cost Changes**

**Vague Requirement:** 

1. Free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.

**Critical Questions**

1. What is the threshold for free shipping?
2. Does the threshold apply when using vouchers?
3. Does the threshold apply to all shipping methods or standard shipping only?
4. Are there different shipping methods (standard, express)?
5. How are shipping fees displayed (dynamically in cart or only at checkout)?
6. What are the shipping fees for the available methods? 

**Detailed Requirement:**

- Free shipping applies to orders above 20€.
- Orders below this threshold incur a standard shipping fee of 5€.
- Only one shipping method (standard) is available.
- Vouchers are not offered.
