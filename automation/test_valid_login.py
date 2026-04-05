from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Test Case: TC-001 - Valid Login
# This test verifies that a user can successfully log in with valid credentials

driver = webdriver.Chrome()

# Open the login page
driver.get("file:///C:/Users/liorg/game%20for%20fun/bank-qa/index.html")
driver.maximize_window()

# Enter valid credentials
driver.find_element(By.ID, "username").send_keys("12345")
driver.find_element(By.ID, "password").send_keys("admin")

# Click login
driver.find_element(By.XPATH, "//button[text()='Log In']").click()

time.sleep(2)

# Verify navigation to dashboard page
current_url = driver.current_url
print("Current URL:", current_url)

if "dashboard.html" in current_url:
    print("Test Passed: Login successful")
else:
    print("Test Failed: Login did not work")

driver.quit()