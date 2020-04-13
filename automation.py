from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

def login(driver, username, password):
    driver.get(
        "https://www.instagram.com/accounts/login/?source=auth_switcher"
    )
    driver.maximize_window()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)
    driver.find_element_by_xpath("//button/div[contains(text(),'Log In')]").click()
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "HoLwm"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

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

def getUnfollowers(driver, username):
    driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(username)).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'following')]"))).click()
    sugs = driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
    driver.execute_script('arguments[0].scrollIntoView()', sugs)
    scroll_box = driver.find_element_by_xpath("//div[contains(@class, 'isgrP')]")
    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        time.sleep(1)
        ht = driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)

class IgBot:
    def __init__(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
       
        self.driver = webdriver.Chrome("./chromedriver")
        login(self.driver, username, password)
        # like(self.driver)
        getUnfollowers(self.driver, username)
        


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

