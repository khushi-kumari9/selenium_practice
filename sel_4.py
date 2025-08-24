#finding element by xpath

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome driver automatically
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open amazon
driver.get("https://www.amazon.com")
time.sleep(5)

# Locate the search box using XPath and type something
search_box = driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]')
search_box.send_keys("laptop")

search_button = driver.find_element(By.XPATH, '//input[@id="nav-search-submit-button"]')
search_button.click()