from selenium import webdriver
from selenium.webdriver.common.by import By

def test_saucedemo_login_and_product():
    # Browser starten
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # --- Login ---
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    # --- Verify succefull login ---
    # Check: we land on the page with products (h1 or div with title "Products")
    products_title = driver.find_element(By.CLASS_NAME, "title")
    assert products_title.text == "Products"

    # --- Check whether product is available ---
    product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    assert product_name.text == "Sauce Labs Backpack"

    driver.quit()
