from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    
    book_button = browser.find_element (By.ID, "book")
    book_button.click()

    btn = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
    btn.click()
    def calc(x):
        return str(math.log(abs(12*math.sin(x))))
    math_element = browser.find_element(By.CSS_SELECTOR,'[id="input_value"]')
    x = int(math_element.text)
    input_form = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input_form.send_keys(calc(x))
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    btn.click()


finally:
   time.sleep(10)
   browser.quit()