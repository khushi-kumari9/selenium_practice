#automatic google search and navigation

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome driver automatically
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Google
driver.get("https://www.google.com")

# Search for something
search_box = driver.find_element(By.NAME, "q") #updated version
search_box.send_keys("selenium")  # You can change the search term
search_box.submit()

# Wait and click the first link
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)

# Close the browser
driver.quit()
# Manual ChromeDriver setup skipped due to Chrome 115+ version changes.
# Used webdriver-manager for automatic handling of driver installation.
