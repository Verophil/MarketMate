### Scenario 1: Submit minimum rating (1 star)

Precondition: User is logged in and has purchased the product "Sample Product".

As a user of MarketMate, I am able to submit a a minimum rating (1 star).

| Step# | Action                        | Expected outcome  | OK/NOK | URL                      | Link to issue |
|-------|--------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1     | Go to product detail page of sample product                                        | Product detail page is displayed | OK     |[https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47991](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47991) |               |
| 2     | Scroll down to rating section       | Rating widget is visible  | OK     |                  |               |
| 3a    | Select 1 star rating  | 1 star is highlighted | OK      |                          |               |
| 3b    | Leave feedback field empty |                  |        |                          |               |
| 4     | Click on "Send"        | Rating is saved successfully   | OK        |                          |               |
| 5     | Verify rating display | The 1-star rating appears immediately under the product ratings | OK        |           |  |

<img width="1340" height="766" alt="Screenshot 2025-08-31 at 18 49 15" src="https://github.com/user-attachments/assets/9934bf83-42cb-4f07-8481-07e033df91c4" />
<img width="1255" height="514" alt="Screenshot 2025-08-31 at 18 50 32" src="https://github.com/user-attachments/assets/c4a308da-5350-41fa-bf90-fbdb1fd7a486" />
 

### Scenario 2: Submit maximum rating (5 stars)

Precondition: User is logged in and has purchased the product "Sample Product" (order status = Delivered).

As a user of MarketMate, I am not able to submit a maximum rating (5 stars)

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go to product detail page of "Sample Product"           | Product detail page is displayed | OK     | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47990](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47990)     |   |
| 2     | Scroll down to rating section  | Rating widget is visible  | OK     |           |                             |
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
| 9     | Click on Confirm                     | User is granted access to shop including alcohol           | NOK     |                                                    |                |




### Scenario 00: Templaate

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
| 9     | Click on Confirm                     | User is granted access to shop including alcohol           | NOK     |                                                    |                |
