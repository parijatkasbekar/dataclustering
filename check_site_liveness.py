from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
 
# Create Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode
 
driver = webdriver.Chrome(options=chrome_options)
 
try:
    # Navigate to your web page
    driver.get('http://20.88.254.25/')
 
    # Wait for a few seconds to ensure the page is loaded (you can adjust this based on your page load time)
    time.sleep(5)
 
    # Check if a specific element is present on the page
    element = driver.find_element(By.ID, '_dash-renderer')
    if element.is_displayed():
        print("Page loaded successfully!")
    else:
        print("Page did not load as expected.")
 
finally:
    # Close the browser window
    driver.quit()