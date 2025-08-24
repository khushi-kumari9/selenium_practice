#slecting links
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.in")
time.sleep(5)

# Use partial link text with correct capitalization
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.in")
time.sleep(5)

# Use partial link text with correct capitalization
electronics_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Electronics")
electronics_link.click()


time.sleep(5)
electronics_link_1 = driver.find_element(By.PARTIAL_LINK_TEXT, "audio")
electronics_link_1.click()

time.sleep(5)

# NOTE: In newer versions of Chrome (115+), automation detection may block this element.
# Works fine on older Chrome versions as used in the lecture.


