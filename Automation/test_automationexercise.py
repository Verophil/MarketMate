import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_register_new_user():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automationexercise.com/")

    # 1️⃣ Verify that home page is visible
    assert "Automation Exercise" in driver.title

    # 2️⃣ Click on 'Signup / Login'
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    # 3️⃣ Verify 'New User Signup!' is visible
    new_user_text = driver.find_element(By.XPATH, "//h2[text()='New User Signup!']")
    assert new_user_text.is_displayed()

    # 4️⃣ Enter name and email address
    driver.find_element(By.NAME, "name").send_keys("TestUser123")
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("testuser12345@example.com")

    # 5️⃣ Click 'Signup' button
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

    # 6️⃣ Verify 'ENTER ACCOUNT INFORMATION' is visible
    enter_info = driver.find_element(By.XPATH, "//b[text()='Enter Account Information']")
    assert enter_info.is_displayed()

    # 7️⃣ Fill account details
    driver.find_element(By.ID, "id_gender1").click()
    driver.find_element(By.ID, "password").send_keys("TestPassword123")
    driver.find_element(By.ID, "days").send_keys("1")
    driver.find_element(By.ID, "months").send_keys("January")
    driver.find_element(By.ID, "years").send_keys("2000")

    # 8️⃣ Check both checkboxes
    driver.find_element(By.ID, "newsletter").click()
    driver.find_element(By.ID, "optin").click()

    # 9️⃣ Fill address info
    driver.find_element(By.ID, "first_name").send_keys("Test")
    driver.find_element(By.ID, "last_name").send_keys("User")
    driver.find_element(By.ID, "company").send_keys("QA Academy")
    driver.find_element(By.ID, "address1").send_keys("123 Test Street")
    driver.find_element(By.ID, "address2").send_keys("Suite 456")
    driver.find_element(By.ID, "country").send_keys("Canada")
    driver.find_element(By.ID, "state").send_keys("Ontario")
    driver.find_element(By.ID, "city").send_keys("Toronto")
    driver.find_element(By.ID, "zipcode").send_keys("A1B2C3")
    driver.find_element(By.ID, "mobile_number").send_keys("1234567890")

    # 🔟 Click 'Create Account' button
    driver.find_element(By.XPATH, "//button[text()='Create Account']").click()

    # 1️⃣1️⃣ Verify account creation
    account_created = driver.find_element(By.XPATH, "//b[text()='Account Created!']")
    assert account_created.is_displayed()

    # 1️⃣2️⃣ Click 'Continue' and verify login
    driver.find_element(By.LINK_TEXT, "Continue").click()
    time.sleep(2)
    logged_in_text = driver.find_element(By.XPATH, "//a[contains(text(),'Logged in as')]")
    assert logged_in_text.is_displayed()

    # 1️⃣3️⃣ Delete account
    driver.find_element(By.LINK_TEXT, "Delete Account").click()
    deleted_msg = driver.find_element(By.XPATH, "//b[text()='Account Deleted!']")
    assert deleted_msg.is_displayed()

    driver.quit()
