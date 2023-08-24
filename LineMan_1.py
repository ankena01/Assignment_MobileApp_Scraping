from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
from PIL import Image
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import io
import time
# from appium.webdriver.common.touch_action import W3CActions
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

# Set desired capabilities
desired_caps = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'udid' : '10e46a62'
}

# Start an Appium session
driver = webdriver.Remote('http://localhost:4723', desired_caps)


#  On home page after manually selecting the delivery location
#  Get username
ele_username = driver.find_element(AppiumBy.ID, 'com.linecorp.linemanth:id/tvTitle')
print(f"{ele_username.text}")

# time.sleep(3)
#  click on Mart
ele_mart = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Mart"]').click()

# time.sleep(3)
# Existing number of cupon codes
ele_cuponcodes = driver.find_element(AppiumBy.ID, 'com.linecorp.linemanth:id/tvAvailableCouponMessage')
print(f"{ele_cuponcodes.text}")

# click on coupon code
ele_cuponcodes.click()

# parse

all_coupons_list = []
all_coupons = driver.find_elements(AppiumBy.ID, 'com.linecorp.linemanth:id/textview_coupon_book_item_title')
for coupon_text in all_coupons:
    all_coupons_list.append(coupon_text.get_attribute("text") )

all_discounts_list = []
all_discounts = driver.find_elements(AppiumBy.ID, 'com.linecorp.linemanth:id/textview_coupon_book_item_discount')
for discount in all_discounts:
    all_discounts_list.append(discount.get_attribute("text"))

all_discounts_conditions_list = []
all_discounts_conditions = driver.find_elements(AppiumBy.ID, 'com.linecorp.linemanth:id/textview_coupon_book_item_short_description') 
for condition in all_discounts_conditions:
    all_discounts_conditions_list.append(condition.get_attribute("text"))  

all_coupons_expiry_list = []
all_coupons_expiry = driver.find_elements(AppiumBy.ID, 'com.linecorp.linemanth:id/textview_coupon_book_item_detail')
for expiry in all_coupons_expiry:
    all_coupons_expiry_list.append(expiry.get_attribute("text"))


# output in a tabular format
scrapped_data = {"Coupons" : all_coupons_list,
                 'Discount' : all_discounts_list,
                 'Discount Condition':all_discounts_conditions_list,
                 'Expiry':all_coupons_expiry_list}

df = pd.DataFrame(data=scrapped_data)
print(df)






