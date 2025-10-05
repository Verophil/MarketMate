import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

@pytest.mark.parametrize("username", [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user"
])
def test_login_with_multiple_users(driver, username):
    password = "secret_sauce"

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    if username == "locked_out_user":
        error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        assert "locked out" in error_message.text.lower()
    else:
        title = driver.find_element(By.CLASS_NAME, "title")
        assert title.text == "Products"

