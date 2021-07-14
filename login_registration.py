import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")

myaccount_btn = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/my-account/"]')
myaccount_btn.click()
email = driver.find_element_by_name("email")
email.send_keys("13579@yandex.ru")
password = driver.find_element_by_id("reg_password")
password.send_keys("Gfnhbr1.")
time.sleep(3)

register_btn = driver.find_element_by_name("register")
register_btn.click()

driver.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")

myaccount_btn = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/my-account/"]')
myaccount_btn.click()

email = driver.find_element_by_name("username")
email.send_keys("13579@yandex.ru")
password = driver.find_element_by_id("password")
password.send_keys("Gfnhbr1.")
login_btn = driver.find_element_by_name("login")
login_btn.click()

some_element= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "pagewrap"), "Logout"))

driver.quit()
