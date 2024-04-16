from selenium import webdriver
import math
import time

# Открываем браузер и переходим на страницу
browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/get_attribute.html")

try:
    # Находим элемент с картинкой и получаем значение атрибута valuex
    treasure_img = browser.find_element_by_id("treasure")
    x_value = treasure_img.get_attribute("valuex")
    
    # Рассчитываем математическую функцию по значению x
    y = str(math.log(abs(12*math.sin(int(x_value)))))
    
    # Вводим ответ в текстовое поле
    answer_input = browser.find_element_by_id("answer")
    answer_input.send_keys(y)

    # Отмечаем чекбокс "I'm the robot"
    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()

    # Выбираем радиокнопку "Robots rule"
    robot_radio = browser.find_element_by_id("robotsRule")
    robot_radio.click()

    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element_by_css_selector("button.btn")
    submit_button.click()

finally:
    # Ждем загрузки страницы
    time.sleep(5)
    # Закрываем браузер
    browser.quit()