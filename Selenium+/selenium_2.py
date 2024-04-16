
from selenium import webdriver

from selenium.webdriver.common.by import By
import math
def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
import time
try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/get_attribute.html")
    img = browser.find_element(By.ID, 'treasure')
    value_x = img.get_attribute('valuex')
    x = value_x
    y = calc(x)
    time.sleep(1)
    element = browser.find_element (By.ID, 'answer' )
    element.send_keys(y)
    robot_checkbox = browser.find_element(By.ID,'robotCheckbox')
    robot_checkbox.click()
    robot_radio = browser.find_element(By.ID, 'robotsRule')
    robot_radio.click()
    button = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
    button.click()

finally:
    time.sleep(5)
    browser.quit()