# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# time.sleep(5)
# driver.get("https://www.google.com")
# time.sleep(5)
# textarea = driver.find_element(By.CSS_SELECTOR, ".gLFyf")
# textarea.send_keys("get()")
# time.sleep(5)
# submit_button = driver.find_element(By.CSS_SELECTOR, ".gNO89b")
# submit_button.click()
# time.sleep(5)
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# link = "https://www.degreesymbol.net"
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")
#     button.click()
# finally:
#     time.sleep(10)
#     browser.quit()
  #Webdriver - это и есть набор команд для управления браузером

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# link = "https://easysmarthub.ru/contact/"

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     input_1 = browser.find_element(By.NAME, "your-name")
#     input_1.send_keys('Egor')
#     input_2 = browser.find_element(By.NAME, "your-email")
#     input_2.send_keys('e.chiberin@gmail.com')
#     input_3 = browser.find_element(By.NAME, "your-subject")
#     input_3.send_keys('Тестировщик ')
#     input_4 = browser.find_element(By.NAME, "your-message")
#     input_4.send_keys('Тут должен быть код,но я не смог его встваить')
#     button_5 = browser.find_element(By.CSS_SELECTOR,'[type="checkbox"]')
#     button_5.click()
#     button_6 = browser.find_element(By.CSS_SELECTOR,'[type="submit"]' )
#     button_6.click()
  




# finally:
#     time.sleep(6)
#     browser.quit() 
   

   
