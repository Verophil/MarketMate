Requirements


1. Product Rating System
   
   
Vague Requirement:


Users should be able to rate products with a 5-star system and have the option to add written feedback.


Critical Questions:

1.1. Who can rate products? Everyone or registered users only? After purchase only?

1.2. Can users change or delete their ratings?

1.3. Are there limitations to the feedback (e.g. character count, language moderation, content filters)?

1.4. Are ratings published immediately or only after review?

1.5. How many ratings per user and product are allowed?

1.6. Is it possible to leave a star rating only, or must feedback always be included?


Detailed Requirement:


- Ratings are only possible after the product has been purchased.
- Users can submit either a star rating only or a star rating with written feedback.
- Feedback may contain up to 500 characters.
- Minimum rating is 1 star.
- No language or content filters are applied.
- Ratings and feedback are published immediately.
- Users can edit their rating and feedback at any time, but only one rating per product per user is allowed.


2. Age Verification for Alcoholic Products


Vague Requirement:


Alcoholic products require age verification. A modal should appear when navigating to the alcoholic products category asking if the user is 18+. Users must input their age before accessing the alcoholic products.


Critical Questions:

2.1. How is the age requested (date of birth input, checkbox)?

2.2. What happens if the user is under 18 (partial access, full restriction, error message)?

2.3. Is age verification required every time or stored after the first attempt?

2.4. How is the age verified (self-disclosure only or document upload)?

2.5. When exactly does the modal appear (product link, category page, add-to-cart)?

2.6. How are products with alcohol content in food (e.g. cake, chocolates) handled?


Detailed Requirement:

- Age verification is required when creating an account for the first time by entering the date of birth in the format MM-DD-YYYY.
- Age verification is also requested every time before entering the shop: a modal appears when clicking the Shop or „Shop now“ button on the Home page. ????
- Self-disclosure of age is sufficient (no document upload required).
- Customers under 18 may browse the site but cannot view alcoholic products. They are shown an appropriate message instead.
- There are no products such as cakes or chocolates containing alcohol. 

3. Shipping Cost Changes

Vague Requirement: 

3.1. Free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.

3.2. Critical Questions

3.3. What is the threshold for free shipping?

3.4. Does the threshold apply when using vouchers?

3.5. Does the threshold apply to all shipping methods or standard shipping only?

3.6. Are there different shipping methods (standard, express)?

3.7. How are shipping fees displayed (dynamically in cart or only at checkout)?

3.8. What are the shipping fees for the available methods?

Detailed Requirement:

- Free shipping applies to orders above 20€.
- Orders below this threshold incur a standard shipping fee of 5€.
- Only one shipping method (standard) is available.
- Vouchers are not offered.
