from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import datetime



driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
).send_keys("USERNAME")
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
).send_keys("PASSWORD")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
print(driver.find_elements_by_tag_name("button")[1].click())

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "HoLwm"))).click()

WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "M9sTE")))

for post in driver.find_elements_by_class_name("M9sTE"):
    print(post)

