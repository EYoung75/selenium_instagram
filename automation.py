
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

def like(driver):
    finished = 0
    while finished < 20:
        time.sleep(2)
        doc_body = driver.find_element_by_tag_name("body")
        doc_body.send_keys(Keys.PAGE_DOWN)
        likes = driver.find_elements_by_xpath("//span[@class='fr66n']/button/*[name()='svg'][@aria-label='Like' ]")
        for like in likes:
            like.click()
            print("like")
        try:
            EC.invisibility_of_element_located(driver.find_elements_by_xpath("//button/*[name()='svg'][@aria-label='Like']"))
            driver.find_element_by_xpath("//button/*[name()='svg'][@aria-label='Unlike']")
            print("breaking")
            finished += 1
                # last_post = True
        except:
            continue


class IgBot:
    def __init__(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.get(
            "https://www.instagram.com/accounts/login/?source=auth_switcher"
        )
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)
        self.driver.find_element_by_xpath("//button/div[contains(text(),'Log In')]").click()
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "HoLwm"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
        like(self.driver)


IgBot()


# ///// LOGIN SEQUENCE
# driver = webdriver.Chrome("./chromedriver")

# driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
# driver.maximize_window()

# username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("evanyoung75")
# password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("NavyEvan75!")

# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
# print(driver.find_elements_by_tag_name("button")[1].click())
# driver.find_element_by_xpath("//button/div[contains(text(),'Log In')]").click()


# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "HoLwm"))).click()
# ////

# //// LIKE POST SEQUENCE

# while(EC.visibility_of_any_elements_located(driver.find_elements_by_xpath("//button/*[name()='svg'][@aria-label='Like']"))):

# //////

