### Scenario 1: Submit minimum rating (1 star)

Precondition: User is logged in and has purchased the product "Sample Product".

As a user of MarketMate, I am able to submit a a minimum rating (1 star).

| Step# | Action                        | Expected outcome  | OK/NOK | URL                      | Link to issue |
|-------|--------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1     | Go to product detail page of sample product                                        | Product detail page is displayed | OK     |[https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47991](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47991) |               |
| 2     | Scroll down to rating section       | Rating widget is visible  | OK     |                  |               |
| 3a    | Select 1 star rating  | 1 star is highlighted | OK      |                          |               |
| 3b    | Leave feedback field empty |                  |        |                          |               |
| 4     | Click on "send"        | Rating is saved successfully   | OK        |                          |               |
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
| 4     | Click on "Submit Rating"              |  Rating is saved successfully   | OK     |    |                      |
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
| 3b    | Enter feedback text with exactly 500 characters  | Text is accepted, no error message displayed| NOK| |[https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479b6](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479b6)   |
| 4     | Click on "Submit Rating" | Rating + feedback are saved successfully | OK |     |       |
| 5     | Verify rating display | The 3-star rating and the 500-character feedback are displayed immediately under the product ratings | NOK  |   |   |

<img width="1470" height="956" alt="Screenshot 2025-08-31 at 20 03 49" src="https://github.com/user-attachments/assets/7d68b6d1-de43-43d9-9065-74e3b007bd74" />
<img width="1259" height="770" alt="Screenshot 2025-08-31 at 20 06 43" src="https://github.com/user-attachments/assets/d4db1930-1ba6-4304-87c1-fb1a85c91d7c" />


### Scenario 4: Submit rating with feedback exceeding 500 characters

Precondition: User is logged in and has purchased the product "Sample Product".

As a user of MarketMate, I am not able to sign up when I register with an invalid Date of Birth.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go to login page FindMate            | Login page appears                                         | OK     | [https://findmate.masterschool.com/](https://findmate.masterschool.com/)     |                             |
| 2     | Click on Sign up                     | You are directed to the sign up page                       | OK     | /auth                                              |                             |
| 3a    | Fill in 'InputValidationTest' as username |                                                            |        |                                                    |                             |
| 3b    | Fill 19-08-1820 as Date of Birth     |                                                            |        |                                                    |                             |
| 3c    | Write 'This is my Bio'               |                                                            |        |                                                    |                             |
| 3d    | Write karin@faculty.masterschool.com as e-mail address |                                                            |        |                                                    |                             |
| 3e    | Password is 'RandomPassword1'        |                                                            |        |                                                    |                             |
| 4     | Click sign up                        | You cannot be 200 years old, so I expect an error message  | NOK    |                                                    | [https://github.com/software-engineering-ms/example-portfolio/issues/2](https://github.com/software-engineering-ms/example-portfolio/issues/2) |

### Scenario 2: Invalid Date of Birth

As a user of FindMate, I am not able to sign up when I register with an invalid Date of Birth.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go to login page FindMate            | Login page appears                                         | OK     | [https://findmate.masterschool.com/](https://findmate.masterschool.com/)     |                             |
| 2     | Click on Sign up                     | You are directed to the sign up page                       | OK     | /auth                                              |                             |
| 3a    | Fill in 'InputValidationTest' as username |                                                            |        |                                                    |                             |
| 3b    | Fill 19-08-1820 as Date of Birth     |                                                            |        |                                                    |                             |
| 3c    | Write 'This is my Bio'               |                                                            |        |                                                    |                             |
| 3d    | Write karin@faculty.masterschool.com as e-mail address |                                                            |        |                                                    |                             |
| 3e    | Password is 'RandomPassword1'        |                                                            |        |                                                    |                             |
| 4     | Click sign up                        | You cannot be 200 years old, so I expect an error message  | NOK    |                                                    | [https://github.com/software-engineering-ms/example-portfolio/issues/2](https://github.com/software-engineering-ms/example-portfolio/issues/2) |
