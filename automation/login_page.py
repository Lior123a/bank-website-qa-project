from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time


# This test checks login with invalid credentials
# and verifies the bug (user still logs in)

driver = webdriver.Chrome()

driver.get("file:///C:/Users/liorg/game%20for%20fun/bank-qa/index.html")
driver.maximize_window()

# Enter wrong password
driver.find_element(By.ID, "username").send_keys("12345")
driver.find_element(By.ID, "password").send_keys("wrong")
driver.find_element(By.XPATH, "//button[text()='Log In']").click()

time.sleep(2)

# Handle alert popup
alert = Alert(driver)
print("Alert text:", alert.text)
alert.accept()

time.sleep(2)

# Check current URL
current_url = driver.current_url
print("Current URL:", current_url)

# Validate bug
if "dashboard.html" in current_url:
    print("BUG FOUND: User logged in with wrong password")
else:
    print("Test Passed: Login failed as expected")

driver.quit()