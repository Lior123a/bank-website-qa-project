from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time


# This test verifies validation behavior when submitting empty login fields
# Expected result: an alert message should appear asking to fill all fields

driver = webdriver.Chrome()

# Open the login page (local demo site)
driver.get("file:///C:/Users/liorg/game%20for%20fun/bank-qa/index.html")
driver.maximize_window()

# Click login button without entering any data
driver.find_element(By.XPATH, "//button[text()='Log In']").click()

time.sleep(2)

# Handle the alert popup
alert = Alert(driver)
alert_text = alert.text

# Print alert message for debugging purposes
print("Alert text:", alert_text)

# Validate expected alert message
if "Please fill in both fields" in alert_text:
    print("Test Passed: Validation works as expected")
else:
    print("Test Failed: Unexpected validation behavior")

# Accept (close) the alert
alert.accept()

# Close the browser
driver.quit()