### Scenario 1: Submit minimum rating (1 star)

Precondition: User is logged in and has purchased the product "Sample Product".

As a user of MarketMate, I am able to submit a a minimum rating (1 star).

| Step# | Action                         | Expected outcome  | OK/NOK | URL                      | Link to issue |
|-------|--------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1     | Go to product detail page of sample product | Product detail page is displayed | OK     | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47991](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47991) |               |
| 2     | Scroll down to rating section  | Rating widget is visible | OK     |                  |               |
| 3a    | Select 1 star rating           | 1 star is highlighted | OK      |                          |               |
| 3b    | Leave feedback field empty     |                   |        |                          |               |
| 4     | Click on "Send"                | Rating is saved successfully   | OK        |                          |               |
| 5     | Verify rating display          | The 1-star rating appears immediately under the product ratings | OK        |           |  |

<img width="1340" height="766" alt="Screenshot 2025-08-31 at 18 49 15" src="https://github.com/user-attachments/assets/9934bf83-42cb-4f07-8481-07e033df91c4" />
<img width="1255" height="514" alt="Screenshot 2025-08-31 at 18 50 32" src="https://github.com/user-attachments/assets/c4a308da-5350-41fa-bf90-fbdb1fd7a486" />
 

### Scenario 2: Submit maximum rating (5 stars)

Precondition: User is logged in and has purchased the product "Sample Product" (order status = Delivered).

As a user of MarketMate, I am not able to submit a maximum rating (5 stars)

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go to product detail page of "Sample Product"           | Product detail page is displayed        | OK     | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47990](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47990)     |   |
| 2     | Scroll down to rating section  | Rating widget is visible                                         | OK     |           |                             |
| 3a    | Select 5 stars rating | 5 stars are highlighted | OK        |              |                             |
| 3b    | Leave feedback field empty    |                                |        |        |                             |
| 4     | Click on "Send"              |  Rating is saved successfully   | OK     |    |                      |
| 5     | Verify rating display | The 5-star rating appears immediately under the product ratings | OK       |     |  |

<img width="1220" height="762" alt="Screenshot 2025-08-31 at 19 11 58" src="https://github.com/user-attachments/assets/89c4c48f-e628-4ce7-804b-834f13fd5ed7" />
<img width="1259" height="533" alt="Screenshot 2025-08-31 at 19 13 00" src="https://github.com/user-attachments/assets/e4a573cd-93e3-4ac0-a2b4-ef8e2189c3b2" />


### Scenario 3: Submit rating with feedback of exactly 500 characters

Precondition: User is logged in and has purchased the product "Sample Product".

As a user of MarketMate, I am able to submit a feedback of exactly 500 characters

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go to product detail page of "Sample Product" | Product detail page is displayed | OK     | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f)     |                             |
| 2     |Scroll down to rating section  | Rating widget is visible  | OK     |       |                             |
| 3a    | Select 3 stars rating | 3 stars are highlighted | OK     |                     |                             |
| 3b    | Enter feedback text with exactly 500 characters  | Text is accepted, no error message displayed| NOK| |[https://github.com/Verophil/MarketMate/issues/1](https://github.com/Verophil/MarketMate/issues/1)   |
| 4     | Click on "Send" | Rating + feedback are saved successfully | OK |     |       |
| 5     | Verify rating display | The 3-star rating and the 500-character feedback are displayed immediately under the product ratings | NOK  |   |   |

<img width="1470" height="956" alt="Screenshot 2025-08-31 at 20 03 49" src="https://github.com/user-attachments/assets/7d68b6d1-de43-43d9-9065-74e3b007bd74" />
<img width="1259" height="770" alt="Screenshot 2025-08-31 at 20 06 43" src="https://github.com/user-attachments/assets/d4db1930-1ba6-4304-87c1-fb1a85c91d7c" />


### Scenario 4: Submit rating with feedback exceeding 500 characters

Precondition: User is logged in and has purchased the product "Sample Product".

As a user of MarketMate, I am not able to sign up when I register with an invalid Date of Birth.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go to product detail page of "Sample Product" | Product detail page is displayed | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479b7](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479b7) | |
| 2     | Scroll down to rating section | Rating widget is visible | OK     |              |                             |
| 3a    | Select 4 stars rating | 4 stars are highlighted | OK |   |                             |
| 3b    | Enter feedback text with 501 characters | Error message is shown: ...  | NOK |                                                    |[https://github.com/Verophil/MarketMate/issues/2](https://github.com/Verophil/MarketMate/issues/2)|
| 4     | Click on "send" | Submission is blocked; rating + feedback are not saved |        |                                                    |                             |
| 5     | Verify no new rating is displayed | No new rating or feedback appears in the product ratings                                                          |        |                                                    |                             |

<img width="1213" height="769" alt="Screenshot 2025-08-31 at 20 57 17" src="https://github.com/user-attachments/assets/18f6f357-65cf-4f4d-b886-68bf9f2b1f05" />


### Scenario 5: Verify rating without purchase is not possible

Precondition: User is logged in but has not purchased the product "Sample Product".

As a user of MarketMate, I am not able to rate a product before having purchased it.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go to product detail page of "Sample Product" | Product detail page is displayed | OK     |[https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47997](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47997)     |                             |
| 2     | Scroll down to rating section | Instead of rating widget the message "You need to buy this product to tell us your opinion!" is shown | OK     |            |               |

<img width="1014" height="735" alt="Screenshot 2025-08-31 at 20 50 26" src="https://github.com/user-attachments/assets/a08553cb-93a3-4e40-bd8c-40bc8fc9d8ed" />


### Scenario 6: Verify rating without feedback

Precondition: User is logged in and has purchased the product "Sample Product".

As a user of MarketMate, I am able to submit a rating without writing a feedback.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go to product detail page of "Sample Product" | Product detail page is displayed                  | OK     | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479ec](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479ec) |                             |
| 2     | Scroll down to rating section        | Rating widget is visible                                   | OK     |                                          |                             |
| 3a    | Select 4 stars rating                | 4 stars are highlighted                                    | OK     |                                                    |                             |
| 3b    | Leave feeback field empty            | No error message shown                                     | OK     |                                                    |                             |
| 4     | Click on "Send"                      | Rating is saved successfully                               | OK     |                                                    |                             |
| 5     | Verify rating display                | The 4-star rating is displayed immediately under the product ratings |OK     |                                                    |                             |

<img width="1277" height="763" alt="Screenshot 2025-09-01 at 11 52 30" src="https://github.com/user-attachments/assets/32cfded2-ebbb-400e-94a4-e517db084753" />


### Scenario 7: Verify rating with feedback

Precondition: User is logged in and has purchased the product "Sample Product".

As a user of MarketMate, I am able to submit a rating with feedback.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go to product detail page of "Sample Product" | Product detail page is displayed                  | OK     | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a5b](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a5b) |                             |
| 2     | Scroll down to rating section        | Rating widget is visible                                   | OK     |                                          |                             |
| 3a    | Select 4 stars rating                | 4 stars are highlighted                                    | OK     |                                                    |                             |
| 3b    | Enter feedback: "Great product"      | Text is accepted                                           | OK     |                                                    |                             |
| 4     | Click on "Send"                      | Rating + feedback are saved successfully                   | OK     |                                                    |                             |
| 5     | Verify rating display                | The 4-star rating with feedback "Great product" is displayed immediately | NOK  |                                        |  [https://github.com/Verophil/MarketMate/issues/3](https://github.com/Verophil/MarketMate/issues/3) |

<img width="1177" height="672" alt="Screenshot 2025-09-01 at 12 03 19" src="https://github.com/user-attachments/assets/b59c5358-d089-4669-b260-5639ebd6a7a3" />
<img width="1252" height="761" alt="Screenshot 2025-09-01 at 12 04 15" src="https://github.com/user-attachments/assets/17e914c0-68b2-4f7b-9abf-9c5ac1c62c3e" />


### Scenario 8: Verify user can change rating down after submission

Precondition: User is logged in and has purchased the product "Sample Product".

As a user of MarketMate, I am able to change my rating up after submission.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go to product detail page of "Sample Product" | Product detail page is displayed                  | OK     | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a5c](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a5c)     |   |
| 2     | Scroll down to rating section        | Rating widget is visible                                   | OK     |                                                    |                             |
| 3     | Select 3 stars rating                | 3 stars are highlighted                                    | OK     |                                                    |                             |
| 4     | Click on "Send"                      | Rating is saved successfully                               | OK     |                                                    |                             |
| 5     | Verify rating display                | The 3 star rating is displayed immediately                 | OK     |                                                    |                             |
| 6     | Click on "Edit"                      | An "Edit rating" pop-up appears with the previous rating (3 stars) pre-selected | OK     |                               |                             |
| 7     | Change rating to 2 stars             | The change is accepted - no error message                  | OK     |                                                    |                             |
| 8     | Click on "Submit"                    | Updated rating is submitted sucessfully                    | OK     |                                                    |                             |
| 9     | Verify rating display                | The updated 2-star rating is displayed immediately         | OK     |                                                    |                             |


<img width="1240" height="777" alt="Screenshot 2025-09-01 at 12 44 58" src="https://github.com/user-attachments/assets/4f3aa450-ddb0-45d1-8a7f-9bed1dfb0a83" />


### Scenario 9: Verify user can change rating up after submission

Precondition: User is logged in and has purchased the product "Sample Product".

As a user of MarketMate, I am  able to sign up when I register with an invalid Date of Birth.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go to product detail page of "Sample Product" | Product detail page is displayed                  | OK     | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a9d](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a9d)     |                             |
| 2     | Scroll down to rating section        | Rating widget is visible                                   | OK     |                                                    |                             |
| 3     | Select 3 stars rating                | 3 stars are highlighted                                    | OK     |                                                    |                             |
| 4     | Click on "Send"                      | Rating is saved successfully                               | OK     |                                                    |                             |
| 5     | Verify rating display                | The 3 star rating is displayed immediately                 | OK     |                                                    |                             |
| 6     | Click on "Edit"                      | An "Edit rating" pop-up appears with the previous rating (3 stars) pre-selected | OK     |                                                    |                             |
| 7     | Change rating to 4 stars             | The change is accepted - no error message                  | OK     |                                                    |                             |
| 8     | Click on "Submit"                    | Updated rating is submitted sucessfully                    | OK     |                                                    | [https://github.com/software-engineering-ms/example-portfolio/issues/2](https://github.com/software-engineering-ms/example-portfolio/issues/2) |
| 9     | Verify rating display                | The updated 4-star rating is displayed immediately         | OK     |                                                    |                             |


<img width="1169" height="782" alt="Screenshot 2025-09-01 at 12 56 19" src="https://github.com/user-attachments/assets/e70ec2c5-c26e-4e92-9f47-54228d70fa31" />


### Scenario 10: Verify behavior when feedback contains only spaces

Precondition: User is logged in and has purchased the product "Sample Product".

If a user of MarketMate tries to submit a feedback containing only empty spaces the star rating submitted and the feedback is treated as empty.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go to product detail page of "Sample Product" | Product detail page is displayed                  | OK     | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a9e](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a9e)     |                             |
| 2     | Scroll down to rating section        | Rating widget is visible                                   | OK     |                                                    |                             |
| 3a    | Select 3 stars rating                | 3 stars are highlighted                                    | OK     |                                                    |                             |
| 3b    | Enter feedback containing only spaces (" ")| Input is treated as empty                            | OK     |                                                    |                             |
| 4     | Click on "Send"                      | Rating is saved successfully                               | OK     |                                                    |                             |
| 5     | Verify rating display                | The 3-star rating is displayed, no feedback field displayed| OK    |                                                    |                             |

<img width="1295" height="733" alt="Screenshot 2025-09-01 at 13 29 13" src="https://github.com/user-attachments/assets/d8814b57-ff98-4f8d-9ef8-4f43366b8ee7" />


### Scenario 11: Template

Precondition: User is logged in and has purchased the product "Sample Product".

As a user of MarketMate, I am not allowed to submit a feedback with a 0 star rating.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go to product detail page of "Sample Product" | Product detail page is displayed                  | OK     | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a9f](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a9f     |                             |
| 2     | Scroll down to rating section        | Rating widget is visible                                   | OK     |                                                    |                             |
| 3a    | Select 0 stars                       | 0 stars are highlighted                                    | OK     |                                                    |                             |
| 3b    | Enter feedback: "Bad product"        | Feedback can be entered                                    | OK     |                                                    |                             |
| 4     | Click on "Send"                      | Error message displayed: "Invalid input for the field 'rating'. Please check your input"| OK     |                       |                             |

<img width="1470" height="956" alt="Screenshot 2025-09-01 at 13 24 45" src="https://github.com/user-attachments/assets/1819c83c-cdae-4e07-b760-45c708c50a6f" />


### Scenario 12: Verify access for user exactly 18 years old

As a user of MarketMate, I As a user of MarketMate, I am able to sign up and access alcoholic products when I am 18 years old.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go too sign-up page                  | Sign-up page is displayed                                  | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth)     |                             |
| 2     | Click on "Create a new account"      | Account creation form is displayed                         | OK     |                                                    |                             |
| 3a    | Fill in RandomUsername               | UserName is accepted                                       | OK     |                                                    |                             |
| 3b    | Fill in RandomEmailAdress            | RandomEmailAdress is accepted                              | OK     |                                                    |                             |
| 3c    | Choose RandomPassword                | RandomPassword                                             | OK     |                                                    |                             |
| 4     | Click on Sign Up                     | User is redirected to the login page                       | OK     |                                                    |                             |
| 5     | Fill in Username and Password        | Username and Passord are accepted                          | OK     |                                                    |                             |
| 6     | Click on Sign up                     | Login successfull                                          | OK     |                                                    |                |
| 7     | Click on Shop                        | Age verification form is displayed                         | OK     |                                                    |                |
| 8     | Enter date of birth = today minus 18 years (format: MM-DD-YYYY) | DOB is accepted                 | OK     |                                                    |                |
| 9     | Click on Confirm                     | User is granted access to shop including alcohol           | OK     |                                                    |                |
| 10    | Verify product visibility            | Alcoholic products are visible and accessible              | OK     |                                                    |                |

<img width="1304" height="768" alt="Screenshot 2025-09-01 at 15 36 51" src="https://github.com/user-attachments/assets/80d6e88a-fe06-4fe6-afb7-213677365bc1" />

<img width="1470" height="956" alt="Screenshot 2025-09-01 at 16 10 44" src="https://github.com/user-attachments/assets/78638197-2ad9-476d-b7bc-ec7aad650ffa" />


### Scenario 13: Verify restriction for user 1 day below 18

As a user of MarketMate, I can not access alcoholic products if younger than 18.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go too sign-up page                  | Sign-up page is displayed                                  | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth)     |                             |
| 2     | Click on "Create a new account"      | Account creation form is displayed                         | OK     |                                                    |                             |
| 3a    | Fill in RandomUsername               | UserName is accepted                                       | OK     |                                                    |                             |
| 3b    | Fill in RandomEmailAdress            | RandomEmailAdress is accepted                              | OK     |                                                    |                             |
| 3c    | Choose RandomPassword                | RandomPassword                                             | OK     |                                                    |                             |
| 4     | Click on Sign Up                     | User is redirected to the login page                       | OK     |                                                    |                             |
| 5     | Fill in Username and Password        | Username and Passord are accepted                          | OK     |                                                    |                             |
| 6     | Click on Sign up                     | Login successfull                                          | OK     |                                                    |                |
| 7     | Click on Shop                        | Age verification form is displayed                         | OK     |                                                    |                |
| 8     | Enter date of birth = today minus 18 years + 1 day (format: MM-DD-YYYY) | DOB is accepted         | OK     |                                                    |                |
| 9     | Click on Confirm                     | User sees message: "You are underage. You can still browse the site, but you will not be able to view alcohol products."  | Ok     |                                                    |                |
| 10    | Attempt to browse alcoholic products section | Access is denied, alcoholic products are not visible | OK     |                                                    |                |

<img width="1470" height="956" alt="Screenshot 2025-09-01 at 16 04 28" src="https://github.com/user-attachments/assets/913fef92-fd07-4f2d-ae08-f343432c6819" />

<img width="1338" height="787" alt="Screenshot 2025-09-01 at 16 06 25" src="https://github.com/user-attachments/assets/36150e8a-da29-4b93-b4a0-eb24174002d8" />

### Scenario 13: Verify users under 18 can browse non-alcoholic products

As a user of MarketMate, I can not access alcoholic products if younger than 18 but I can still browse all the other categories.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go too sign-up page                  | Sign-up page is displayed                                  | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth)     |                             |
| 2     | Click on "Create a new account"      | Account creation form is displayed                         | OK     |                                                    |                             |
| 3a    | Fill in RandomUsername               | UserName is accepted                                       | OK     |                                                    |                             |
| 3b    | Fill in RandomEmailAdress            | RandomEmailAdress is accepted                              | OK     |                                                    |                             |
| 3c    | Choose RandomPassword                | RandomPassword                                             | OK     |                                                    |                             |
| 4     | Click on Sign Up                     | User is redirected to the login page                       | OK     |                                                    |                             |
| 5     | Fill in Username and Password        | Username and Passord are accepted                          | OK     |                                                    |                             |
| 6     | Click on Sign up                     | Login successfull                                          | OK     |                                                    |                |
| 7     | Click on Shop                        | Age verification form is displayed                         | OK     |                                                    |                |
| 8     | Enter date of birth = today minus 18 years + 1 day (format: MM-DD-YYYY) | DOB is accepted         | OK     |                                                    |                |
| 9     | Click on Confirm                     | User sees message: "You are underage. You can still browse the site, but you will not be able to view alcohol products." | OK     |                                                    |                |
| 10    | Search for non-alcoholic product (e.g., "bread") | Product is visible                            | OK     |                                                    |                |

<img width="1150" height="667" alt="Screenshot 2025-09-01 at 16 21 49" src="https://github.com/user-attachments/assets/c6576f0c-28f6-4a56-81e4-5f72f3ed696f" />



### Scenario 14: Verify users under 18 can browse non-alcoholic products

As a user of MarketMate, I can not access alcoholic products if younger than 18 but I can still browse all the other categories.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go too sign-up page                  | Sign-up page is displayed                                  | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth)     |                             |
| 2     | Click on "Create a new account"      | Account creation form is displayed                         | OK     |                                                    |                             |
| 3a    | Fill in RandomUsername               | UserName is accepted                                       | OK     |                                                    |                             |
| 3b    | Fill in RandomEmailAdress            | RandomEmailAdress is accepted                              | OK     |                                                    |                             |
| 3c    | Choose RandomPassword                | RandomPassword                                             | OK     |                                                    |                             |
| 4     | Click on Sign Up                     | User is redirected to the login page                       | OK     |                                                    |                             |
| 5     | Fill in Username and Password        | Username and Passord are accepted                          | OK     |                                                    |                             |
| 6     | Click on Sign up                     | Login successfull                                          | OK     |                                                    |                |
| 7     | Click on Shop                        | Age verification form is displayed                         | OK     |                                                    |                |
| 8     | Enter date of birth = today minus 25 years (format: MM-DD-YYYY) | DOB is accepted                 | OK     |                                                    |                |
| 9     | Click on Confirm                     | User is granted full access to the shop                    | OK     |                                                    |                |
| 10    | Browse alcoholic products section    | Alcoholic products are visible                             | OK     |                                                    |                |
| 11    | Browse non-alcoholic products section (e.g., "bread")   | Non-alcoholic products are visible      | OK     |                                                    |                |

<img width="1327" height="770" alt="Screenshot 2025-09-01 at 16 25 35" src="https://github.com/user-attachments/assets/ddbf2884-428e-4840-824a-a92e0b7b0961" />
<img width="1343" height="725" alt="Screenshot 2025-09-01 at 16 29 31" src="https://github.com/user-attachments/assets/06271d98-8d11-4631-92a7-12cfbd8f9d22" />
<img width="1335" height="790" alt="Screenshot 2025-09-01 at 16 29 42" src="https://github.com/user-attachments/assets/c9a1f199-81ee-4b47-8050-f312ff2d70eb" />

### Scenario 15: Verify system behavior when DOB field left empty during age verification

As a user of MarketMate, I have to fill in the age verification form.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go too sign-up page                  | Sign-up page is displayed                                  | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth)     |                             |
| 2     | Click on "Create a new account"      | Account creation form is displayed                         | OK     |                                                    |                             |
| 3a    | Fill in RandomUsername               | UserName is accepted                                       | OK     |                                                    |                             |
| 3b    | Fill in RandomEmailAdress            | RandomEmailAdress is accepted                              | OK     |                                                    |                             |
| 3c    | Choose RandomPassword                | RandomPassword                                             | OK     |                                                    |                             |
| 4     | Click on Sign Up                     | User is redirected to the login page                       | OK     |                                                    |                             |
| 5     | Fill in Username and Password        | Username and Passord are accepted                          | OK     |                                                    |                             |
| 6     | Click on Sign up                     | Login successfull                                          | OK     |                                                    |                             |
| 7     | Click on Shop                        | Age verification form is displayed                         | OK     |                                                    |                             |
| 8     | Leave DOB field empty                | Field remains empty                                        | OK     |                                                    |                             |
| 9     | Click on Confirm                     | Error message is displayed: "Date of Birth is required."   | NOK    |                                                    |[https://github.com/Verophil/MarketMate/issues/4](https://github.com/Verophil/MarketMate/issues/4) |

<img width="2940" height="1912" alt="Screenshot 2025-09-01 at 16 46 28" src="https://github.com/user-attachments/assets/54ff196c-e542-47cd-bbbe-7f8c623eaab8" />



### Scenario 16: Verify invalid DOB format

As a user of MarketMate, I have to fill in the age verification using the valid format.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go too sign-up page                  | Sign-up page is displayed                                  | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth)|                             |
| 2     | Click on "Create a new account"      | Account creation form is displayed                         | OK     |                                                    |                             |
| 3a    | Fill in RandomUsername               | UserName is accepted                                       | OK     |                                                    |                             |
| 3b    | Fill in RandomEmailAdress            | RandomEmailAdress is accepted                              | OK     |                                                    |                             |
| 3c    | Choose RandomPassword                | RandomPassword                                             | OK     |                                                    |                             |
| 4     | Click on Sign Up                     | User is redirected to the login page                       | OK     |                                                    |                             |
| 5     | Fill in Username and Password        | Username and Passord are accepted                          | OK     |                                                    |                             |
| 6     | Click on Sign up                     | Login successfull                                          | OK     |                                                    |                             |
| 7     | Click on Shop                        | Age verification form is displayed                         | OK     |                                                    |                             |
| 8     | Enter DOB = "13/25/2008"             | Field input is displayed                                   | OK     |                                                    |                             |
| 9     | Click on Confirm                     | Error message is displayed: "Invalid Date of Birth format. Please use MM-DD-YYYY."   | NOK    |                          | [https://github.com/Verophil/MarketMate/issues/5](https://github.com/Verophil/MarketMate/issues/5)|


<img width="2940" height="1912" alt="Screenshot 2025-09-01 at 17 59 38" src="https://github.com/user-attachments/assets/4314ccb3-bd11-4881-b33e-eab18b5d7c78" />



### Scenario 17: Verify system behavior when user enters an unrealistic age (150 years old)

As a user of MarketMate, I have to aneter a realistic age.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go too sign-up page                  | Sign-up page is displayed                                  | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth)     |                             |
| 2     | Click on "Create a new account"      | Account creation form is displayed                         | OK     |                                                    |                             |
| 3a    | Fill in RandomUsername               | UserName is accepted                                       | OK     |                                                    |                             |
| 3b    | Fill in RandomEmailAdress            | RandomEmailAdress is accepted                              | OK     |                                                    |                             |
| 3c    | Choose RandomPassword                | RandomPassword                                             | OK     |                                                    |                             |
| 4     | Click on Sign Up                     | User is redirected to the login page                       | OK     |                                                    |                             |
| 5     | Fill in Username and Password        | Username and Passord are accepted                          | OK     |                                                    |                             |
| 6     | Click on Sign up                     | Login successfull                                          | OK     |                                                    |                             |
| 7     | Click on Shop                        | Age verification form is displayed                         | OK     |                                                    |                             |
| 8     |Enter DOB = 01-01-1875 (150 years old)| Field input is displayed                                   | OK     |                                                    |                             |
| 9     | Click on Confirm                     | Error message is displayed: "Please enter a valid date of birth."   | NOK    |                                           | [https://github.com/Verophil/MarketMate/issues/6](https://github.com/Verophil/MarketMate/issues/6)               |

<img width="1470" height="956" alt="Screenshot 2025-09-01 at 18 15 48" src="https://github.com/user-attachments/assets/756c0dc4-cff4-47c1-8769-ebb318de8bd9" />
<img width="2940" height="1912" alt="Screenshot 2025-09-01 at 18 15 57" src="https://github.com/user-attachments/assets/9910bc95-0892-4b79-818f-d0735a91b975" />



### Scenario 18: Verify order exactly at 20€ qualifies for free shipping

As a user of MarketMate, I get free shipping when purchasing goods of the value 20+ Euro.

Precondition: User is logged in and has an empty basket.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Add items to basket until total = 20€| Basket total shows exactly 20€                             | OK     | [https://grocerymate.masterschool.com/store](https://grocerymate.masterschool.com/store)|             |
| 2     | Review shipping costs                | Free shipping is applied                                   | OK     |                                                    |                             |

<img width="1274" height="698" alt="Screenshot 2025-09-01 at 18 50 56" src="https://github.com/user-attachments/assets/3b7915e2-8ece-4571-919c-864c5aef1f66" />



### Scenario 00: Template

As a user of MarketMate, I can not access alcoholic products if younger than 18 but I can still browse all the other categories.

Precondition: User is logged in and has an empty basket.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Add items to basket until total = 19.99€| Basket total shows exactly 19.99€                       | OK     | [https://grocerymate.masterschool.com/store](https://grocerymate.masterschool.com/store)|                             |
| 2     | Click on "Create a new account"      | Account creation form is displayed                         | OK     |                                                    |                             |
| 3a    | Fill in RandomUsername               | UserName is accepted                                       | OK     |                                                    |                             |
| 3b    | Fill in RandomEmailAdress            | RandomEmailAdress is accepted                              | OK     |                                                    |                             |
| 3c    | Choose RandomPassword                | RandomPassword                                             | OK     |                                                    |                             |
| 4     | Click on Sign Up                     | User is redirected to the login page                       | OK     |                                                    |                             |
| 5     | Fill in Username and Password        | Username and Passord are accepted                          | OK     |                                                    |                             |
| 6     | Click on Sign up                     | Login successfull                                          | OK     |                                                    |                |
| 7     | Click on Shop                        | Age verification form is displayed                         | OK     |                                                    |                |
| 8     | Leave DOB field empty                | Field remains empty                                        | OK     |                                                    |                |
| 9     | Click on Confirm                     | Error message is displayed: "Date of Birth is required."   | OK     |                                                    |                |
| 10    | Click on Confirm                     | Alcoholic products are visible                             | OK     |                                                    |                |
| 11    | Browse non-alcoholic products section (e.g., "bread")   | Non-alcoholic products are visible      | OK     |                                                    |                |


### Scenario 00: Template

As a user of MarketMate, I can not access alcoholic products if younger than 18 but I can still browse all the other categories.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go too sign-up page                  | Sign-up page is displayed                                  | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth)     |                             |
| 2     | Click on "Create a new account"      | Account creation form is displayed                         | OK     |                                                    |                             |
| 3a    | Fill in RandomUsername               | UserName is accepted                                       | OK     |                                                    |                             |
| 3b    | Fill in RandomEmailAdress            | RandomEmailAdress is accepted                              | OK     |                                                    |                             |
| 3c    | Choose RandomPassword                | RandomPassword                                             | OK     |                                                    |                             |
| 4     | Click on Sign Up                     | User is redirected to the login page                       | OK     |                                                    |                             |
| 5     | Fill in Username and Password        | Username and Passord are accepted                          | OK     |                                                    |                             |
| 6     | Click on Sign up                     | Login successfull                                          | OK     |                                                    |                |
| 7     | Click on Shop                        | Age verification form is displayed                         | OK     |                                                    |                |
| 8     | Leave DOB field empty                | Field remains empty                                        | OK     |                                                    |                |
| 9     | Click on Confirm                     | Error message is displayed: "Date of Birth is required."   | OK     |                                                    |                |
| 10    | Click on Confirm                     | Alcoholic products are visible                             | OK     |                                                    |                |
| 11    | Browse non-alcoholic products section (e.g., "bread")   | Non-alcoholic products are visible      | OK     |                                                    |                |





