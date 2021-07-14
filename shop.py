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

shop_btn = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/shop/"]')
shop_btn.click()
time.sleep(3)

HTML5Forms_btn = driver.find_element_by_css_selector('.post-181 .wp-post-image')
HTML5Forms_btn.click()

some_element= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "product_title.entry-title"), "HTML5 Forms"))

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

shop_btn = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/shop/"]')
shop_btn.click()
time.sleep(3)
HTML_btn = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/product-category/html/"]')
HTML_btn.click()

some_element= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".current-cat .count"), "3"))

driver.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select

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

shop_btn = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/shop/"]')
shop_btn.click()
time.sleep(2)

items_selector = driver.find_element_by_name('orderby')
items_selector_default = items_selector.get_attribute("value")
if items_selector_default == "menu_order":
    print("Выбрана сортировка по умолчанию")
else:
    print("Выбрана сортировка не по умолчанию")

element = driver.find_element_by_name("orderby")
select = Select(element)
select.select_by_value("price-desc")
time.sleep(2)

sort_selector = driver.find_element_by_name('orderby')
sort_selector_default = sort_selector.get_attribute("value")
if sort_selector_default == "price-desc":
    print("Выбрана сортировка от большего к меньшему")
else:
    print("Выбрана сортировка не от большего к меньшему")

driver.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select

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

shop_btn = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/shop/"]')
shop_btn.click()
time.sleep(2)

android_btn = driver.find_element_by_css_selector('.products .attachment-shop_catalog')
android_btn.click()
time.sleep(2)

price = driver.find_element_by_xpath("//span[@class='woocommerce-Price-amount amount']")
price_get_text = price.text
assert price_get_text == "₹600.00"
time.sleep(2)

android600_btn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "attachment-shop_single.size-shop_single.wp-post-image")))

android600_btn = driver.find_element_by_class_name("attachment-shop_single.size-shop_single.wp-post-image")
android600_btn.click()

android600min_btn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "fullResImage")))

close_btn = driver.find_element_by_class_name("pp_close")
close_btn.click()

driver.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select

import time
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
shop_btn = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/shop/"]')
shop_btn.click()
time.sleep(2)

HTML5WebAppDevelopment_btn = driver.find_element_by_xpath('//a[@href="/shop/?add-to-cart=182"]')
HTML5WebAppDevelopment_btn.click()
time.sleep(2)
basket = driver.find_element_by_xpath("//span[@class='cartcontents']")
basket_get_text = basket.text
assert basket_get_text == "1 Item"

element = driver.find_element_by_xpath("//span[@class='amount']")
element_get_text = element.text
assert element_get_text == "₹180.00"

basket_btn = driver.find_element_by_class_name("amount")
basket_btn.click()

subtotal_element= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), "₹180.00"))

total_element= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product-subtotal .woocommerce-Price-amount"), "₹180.00"))

driver.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select

import time
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
shop_btn = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/shop/"]')
shop_btn.click()
time.sleep(2)

HTML5WebAppDevelopment_btn = driver.find_element_by_xpath('//a[@href="/shop/?add-to-cart=182"]')
HTML5WebAppDevelopment_btn.click()
time.sleep(2)
JSDataStructures_btn = driver.find_element_by_xpath('//a[@href="/shop/?add-to-cart=180"]')
JSDataStructures_btn.click()

basket_btn = driver.find_element_by_class_name("amount")
basket_btn.click()
time.sleep(2)
remove_btn = driver.find_element_by_class_name("remove")
remove_btn.click()
time.sleep(2)
undo_btn = driver.find_element_by_link_text("Undo?")
undo_btn.click()

quantity = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
quantity.clear()

quantity = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
quantity.send_keys("3")
update_btn = driver.find_element_by_name("update_cart")
update_btn.click()
time.sleep(2)
quantity_field = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .product-quantity input")
quantity_field_value = quantity_field.get_attribute("value")
assert quantity_field_value == '3'

coupon_btn = driver.find_element_by_name("apply_coupon")
coupon_btn.click()

some_element= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".page-content .woocommerce-error"), "Please enter a coupon code."))

driver.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select

import time
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
shop_btn = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/shop/"]')
shop_btn.click()
time.sleep(2)
driver.execute_script("window.scrollBy(0, 300);")

HTML5WebAppDevelopment_btn = driver.find_element_by_xpath('//a[@href="/shop/?add-to-cart=182"]')
HTML5WebAppDevelopment_btn.click()
time.sleep(2)
basket_btn = driver.find_element_by_class_name("amount")
basket_btn.click()

checkout_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button.button.alt.wc-forward")) )
checkout_btn = driver.find_element_by_class_name("checkout-button.button.alt.wc-forward")
checkout_btn.click()

first_name_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "billing_first_name")) )

first_name = driver.find_element_by_id("billing_first_name")
first_name.send_keys("first")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("last")
email = driver.find_element_by_id("billing_email")
email.send_keys("13579@yandex.ru")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("123456789")
address_1 = driver.find_element_by_id("billing_address_1")
address_1.send_keys("address_1")
city = driver.find_element_by_id("billing_city")
city.send_keys("city")
state = driver.find_element_by_id("billing_state")
state.send_keys("state")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("postcode")

select_btn = driver.find_element_by_id("select2-chosen-1")
select_btn.click()
country = driver.find_element_by_id("s2id_autogen1_search")
country.send_keys("Russia")
russia_btn = driver.find_element_by_css_selector(".select2-result-label .select2-match")
russia_btn.click()

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
check_btn = driver.find_element_by_id("payment_method_cheque")
check_btn.click()
placeorder_btn = driver.find_element_by_name("woocommerce_checkout_place_order")
placeorder_btn.click()

some_element= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

some_element= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "method"), "Check Payments"))

driver.quit()


