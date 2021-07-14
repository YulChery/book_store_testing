import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")

selenium_btn = driver.find_element_by_css_selector('.themify_builder_row .attachment-shop_catalog')
selenium_btn.click()
reviews_btn = driver.find_element_by_xpath('//a[@href="#tab-reviews"]')
reviews_btn.click()
star_btn = driver.find_element_by_class_name("star-5")
star_btn.click()
review = driver.find_element_by_name("comment")
review.send_keys("Nice book!")
name = driver.find_element_by_name("author")
name.send_keys("13579")
email = driver.find_element_by_name("email")
email.send_keys("13579@yandex.ru")
submit_btn = driver.find_element_by_name("submit")
submit_btn.click()
driver.quit()