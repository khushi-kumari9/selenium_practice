#getting data

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
search_box.send_keys("iphone")

search_button = driver.find_element(By.XPATH, '//input[@id="nav-search-submit-button"]')
search_button.click()

list_name= driver.find_elements(By.XPATH, '//span[@class="a-size-large product-title-word-break"]')
print(str(len(list_name))+"products found")

for item in list_name:
    print(item.text)
driver.quit()
# NOTE: In newer versions of Chrome (115+), automation detection may block this element.
# Works fine on older Chrome versions as used in the lecture.