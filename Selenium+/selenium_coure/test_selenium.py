import time


#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver


#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By


#инициализация драйвера браузера.
driver = webdriver.Chrome()


#установили паузу на 15 секунд. Если все сделали верно при запуке откроется хром
time.sleep(5)


#С помощью метода GET мы скажем браузеру, что надо открыть
driver.get("https://www.google.com")
time.sleep(5)

#Метод  find_element позволяет найти нужный элемент на сайте.
textarea = driver.find_element(By.CSS_SELECTOR, ".gLFyf")


textarea.send_keys("get()")
time.sleep(5)

submit_button = driver.find_element(By.CSS_SELECTOR, ".gNO89b")


submit_button.click()
time.sleep(5)
driver.quit()