from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.intervue.io/")

wait = WebDriverWait(driver, 20)

# Step 1: Click "Login" which opens a new tab
driver.find_element(By.CLASS_NAME, "ivhn-contact-link").click()

# Step 2: Switch to the newly opened tab
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)

# Step 3: Click on "Login button for Companies"
driver.find_element(By.CLASS_NAME, "AccessAccount-ColoredButton-Text").click()

# Step 4: Fill in login credentials
driver.find_element(By.ID, "login_email").send_keys("neha@intervue.io")
driver.find_element(By.ID, "login_password").send_keys("Ps@neha@123")

# Step 5: Click on "Login with email"
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Login with email']]")))
login_button.click()

# Step 6: Click on the search field
search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search_placeholder")))
search_button.click()

# Step 7: Type "hello" into the input box
search_input = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//input[@placeholder='Type what you want to search for']")
))
search_input.send_keys("hello")

# Step 8: Wait for the result to appear and click it
search_result = wait.until(EC.element_to_be_clickable((
    By.XPATH, "//div[contains(@class, 'SearchThrough__PlaceholderText') and contains(., 'hello')]"
)))
search_result.click()

# Step 9: Click on the user profile
avatar = wait.until(EC.element_to_be_clickable((
    By.XPATH, "//div[contains(@class, 'userAvatar') and contains(@class, 'Avatar__AvatarDiv')]"
)))
avatar.click()

# Step 10: Click on the "Logout" option
logout_btn = wait.until(EC.element_to_be_clickable((
    By.XPATH, "//a[@href='/logout' and text()='Logout']"
)))
logout_btn.click()

print("Successfully logged out.")
time.sleep(4)
