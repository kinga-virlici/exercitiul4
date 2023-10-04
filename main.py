
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Așteaptă până când elementul cu id-ul "my-text-id" devine vizibil
text_box = driver.find_element(By.ID, "my-text-id")

submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")

text_box.send_keys("Selector44")
time.sleep(5)
submit_button.click()
time.sleep(5)
driver.quit()


