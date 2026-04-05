from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time


# Test Case: TC-002 - Invalid Login
# This test verifies that login should fail with incorrect credentials
# Expected result: user should NOT be redirected to dashboard

driver = webdriver.Chrome()

# Open login page
driver.get("file:///C:/Users/liorg/game%20for%20fun/bank-qa/index.html")
driver.maximize_window()

# Enter invalid credentials
driver.find_element(By.ID, "username").send_keys("12345")
driver.find_element(By.ID, "password").send_keys("wrong")
driver.find_element(By.XPATH, "//button[text()='Log In']").click()

time.sleep(2)

# Handle alert
alert = Alert(driver)
print("Alert text:", alert.text)
alert.accept()

time.sleep(2)

# Check URL
current_url = driver.current_url
print("Current URL:", current_url)

# ✅ Expected behavior (what SHOULD happen)
if "dashboard.html" not in current_url:
    print("Test Passed: Login failed as expected")
else:
    print("Test Failed: User logged in with invalid credentials (BUG) ❌")

driver.quit()