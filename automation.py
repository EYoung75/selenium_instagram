from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


# class Bot:
#     driver = webdriver.Chrome("./chromedriver")

#     def __init__(self, username, password):
#         super().__init__()
#         self.username = username
#         self.password = password
#         self.login()

#     def login(self):
#         if(self.username != ""):
#             self.driver.get(
#                 "https://www.instagram.com/accounts/login/?source=auth_switcher"
#             )
#             WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(self.username)
#             WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(self.password)
#             self.driver.find_elements_by_tag_name("button")[1].click()
#             WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "HoLwm"))).click()
        


# bot_one = Bot(input("username: "), input("password: "))


# ///// LOGIN SEQUENCE
driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
driver.maximize_window()

username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("USERNAME")
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("PASSWORD")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
print(driver.find_elements_by_tag_name("button")[1].click())

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "HoLwm"))).click()
# ////

# //// LIKE POST SEQUENCE
finished = 0

# while(EC.visibility_of_any_elements_located(driver.find_elements_by_xpath("//button/*[name()='svg'][@aria-label='Like']"))):
while finished < 20:
    time.sleep(1)
    doc_body = driver.find_element_by_tag_name("body")
    doc_body.send_keys(Keys.PAGE_DOWN)
    likes = driver.find_elements_by_xpath("//button/*[name()='svg'][@aria-label='Like']")
    for like in likes:
        like.click()
        print("like")
    try:
        # EC.invisibility_of_element_located(driver.find_elements_by_xpath("//button/*[name()='svg'][@aria-label='Like']"))
        driver.find_element_by_xpath("//button/*[name()='svg'][@aria-label='Unlike']")
        print("breaking")
        finished += 1
        # last_post = True
    except:
        continue
# //////
