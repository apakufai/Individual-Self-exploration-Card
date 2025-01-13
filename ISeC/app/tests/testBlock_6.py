from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os


# Инициализация веб-драйвера
browser = webdriver.Chrome()

try:
    browser.get('http://127.0.0.1:5000/test_6')


# СТАРТ БЛОКА 6
    time.sleep(1.5)
    btn_6_start = browser.find_element(By.ID, 'test_6_start')
    btn_6_start.click()

# ВОПРОС 6_1
    time.sleep(0.8)

    # Находим элементы input type="range" для каждого ползунка
    range_input_6_1_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_1_1 input[type="range"]')
    range_input_6_1_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_1_2 input[type="range"]')
    range_input_6_1_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_1_3 input[type="range"]')
    range_input_6_1_4 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_1_4 input[type="range"]')

    # Устанавливаем значение для ползунка range_input_6_1_1
    desired_value_6_1_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_6_1_1 = range_input_6_1_1.get_attribute(
        'max')  # Получаем максимальное значение ползунка
    # Устанавливаем значение на ползунок, если оно меньше или равно максимальному значению ползунка
    if desired_value_6_1_1 <= int(max_value_6_1_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_1_1, desired_value_6_1_1)

    # Устанавливаем значение для ползунка range_input_6_1_2
    desired_value_6_1_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_6_1_2 = range_input_6_1_2.get_attribute(
        'max')  # Получаем максимальное значение ползунка
    # Устанавливаем значение на ползунок, если оно меньше или равно максимальному значению ползунка
    if desired_value_6_1_2 <= int(max_value_6_1_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_1_2, desired_value_6_1_2)

    # Устанавливаем значение для ползунка range_input_6_1_3
    desired_value_6_1_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_6_1_3 = range_input_6_1_3.get_attribute(
        'max')  # Получаем максимальное значение ползунка
    # Устанавливаем значение на ползунок, если оно меньше или равно максимальному значению ползунка
    if desired_value_6_1_3 <= int(max_value_6_1_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_1_3, desired_value_6_1_3)

    # Устанавливаем значение для ползунка range_input_6_1_4
    desired_value_6_1_4 = 4  # Значение, которое нужно установить на ползунке 4
    max_value_6_1_4 = range_input_6_1_4.get_attribute(
        'max')  # Получаем максимальное значение ползунка
    # Устанавливаем значение на ползунок, если оно меньше или равно максимальному значению ползунка
    if desired_value_6_1_4 <= int(max_value_6_1_4):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_1_4, desired_value_6_1_4)

    # Нажимаем кнопку "Далее"
    btn_6_1_next = browser.find_element(By.ID, 'btn_6_1_next')
    btn_6_1_next.click()

# ВОПРОС 6_2
    time.sleep(0.8)
    range_input_6_2_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_2_1 input[type="range"]')
    range_input_6_2_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_2_2 input[type="range"]')
    range_input_6_2_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_2_3 input[type="range"]')
    range_input_6_2_4 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_2_4 input[type="range"]')
    desired_value_6_2_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_6_2_1 = range_input_6_2_1.get_attribute('max')
    if desired_value_6_2_1 <= int(max_value_6_2_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_2_1, desired_value_6_2_1)
    desired_value_6_2_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_6_2_2 = range_input_6_2_2.get_attribute('max')
    if desired_value_6_2_2 <= int(max_value_6_2_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_2_2, desired_value_6_2_2)
    desired_value_6_2_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_6_2_3 = range_input_6_2_3.get_attribute('max')
    if desired_value_6_2_3 <= int(max_value_6_2_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_2_3, desired_value_6_2_3)
    desired_value_6_2_4 = 4  # Значение, которое нужно установить на ползунке 4
    max_value_6_2_4 = range_input_6_2_4.get_attribute('max')
    if desired_value_6_2_4 <= int(max_value_6_2_4):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_2_4, desired_value_6_2_4)
    btn_6_2_next = browser.find_element(By.ID, 'btn_6_2_next')
    btn_6_2_next.click()

# ВОПРОС 6_3
    time.sleep(0.8)
    range_input_6_3_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_3_1 input[type="range"]')
    range_input_6_3_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_3_2 input[type="range"]')
    range_input_6_3_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_3_3 input[type="range"]')
    range_input_6_3_4 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_3_4 input[type="range"]')
    desired_value_6_3_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_6_3_1 = range_input_6_3_1.get_attribute('max')
    if desired_value_6_3_1 <= int(max_value_6_3_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_3_1, desired_value_6_3_1)
    desired_value_6_3_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_6_3_2 = range_input_6_3_2.get_attribute('max')
    if desired_value_6_3_2 <= int(max_value_6_3_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_3_2, desired_value_6_3_2)
    desired_value_6_3_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_6_3_3 = range_input_6_3_3.get_attribute('max')
    if desired_value_6_3_3 <= int(max_value_6_3_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_3_3, desired_value_6_3_3)
    desired_value_6_3_4 = 4  # Значение, которое нужно установить на ползунке 4
    max_value_6_3_4 = range_input_6_3_4.get_attribute('max')
    if desired_value_6_3_4 <= int(max_value_6_3_4):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_3_4, desired_value_6_3_4)
    btn_6_3_next = browser.find_element(By.ID, 'btn_6_3_next')
    btn_6_3_next.click()

# ВОПРОС 6_4
    time.sleep(0.8)
    range_input_6_4_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_4_1 input[type="range"]')
    range_input_6_4_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_4_2 input[type="range"]')
    range_input_6_4_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_4_3 input[type="range"]')
    range_input_6_4_4 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_4_4 input[type="range"]')
    desired_value_6_4_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_6_4_1 = range_input_6_4_1.get_attribute('max')
    if desired_value_6_4_1 <= int(max_value_6_4_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_4_1, desired_value_6_4_1)
    desired_value_6_4_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_6_4_2 = range_input_6_4_2.get_attribute('max')
    if desired_value_6_4_2 <= int(max_value_6_4_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_4_2, desired_value_6_4_2)
    desired_value_6_4_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_6_4_3 = range_input_6_4_3.get_attribute('max')
    if desired_value_6_4_3 <= int(max_value_6_4_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_4_3, desired_value_6_4_3)
    desired_value_6_4_4 = 4  # Значение, которое нужно установить на ползунке 4
    max_value_6_4_4 = range_input_6_4_4.get_attribute('max')
    if desired_value_6_4_4 <= int(max_value_6_4_4):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_4_4, desired_value_6_4_4)
    btn_6_4_next = browser.find_element(By.ID, 'btn_6_4_next')
    btn_6_4_next.click()

# ВОПРОС 6_5
    time.sleep(0.8)
    range_input_6_5_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_5_1 input[type="range"]')
    range_input_6_5_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_5_2 input[type="range"]')
    range_input_6_5_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_5_3 input[type="range"]')
    range_input_6_5_4 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_5_4 input[type="range"]')
    desired_value_6_5_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_6_5_1 = range_input_6_5_1.get_attribute('max')
    if desired_value_6_5_1 <= int(max_value_6_5_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_5_1, desired_value_6_5_1)
    desired_value_6_5_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_6_5_2 = range_input_6_5_2.get_attribute('max')
    if desired_value_6_5_2 <= int(max_value_6_5_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_5_2, desired_value_6_5_2)
    desired_value_6_5_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_6_5_3 = range_input_6_5_3.get_attribute('max')
    if desired_value_6_5_3 <= int(max_value_6_5_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_5_3, desired_value_6_5_3)
    desired_value_6_5_4 = 4  # Значение, которое нужно установить на ползунке 4
    max_value_6_5_4 = range_input_6_5_4.get_attribute('max')
    if desired_value_6_5_4 <= int(max_value_6_5_4):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_5_4, desired_value_6_5_4)
    btn_6_5_next = browser.find_element(By.ID, 'btn_6_5_next')
    btn_6_5_next.click()

# ВОПРОС 6_6
    time.sleep(0.8)
    range_input_6_6_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_6_1 input[type="range"]')
    range_input_6_6_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_6_2 input[type="range"]')
    range_input_6_6_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_6_3 input[type="range"]')
    range_input_6_6_4 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_6_4 input[type="range"]')
    desired_value_6_6_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_6_6_1 = range_input_6_6_1.get_attribute('max')
    if desired_value_6_6_1 <= int(max_value_6_6_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_6_1, desired_value_6_6_1)
    desired_value_6_6_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_6_6_2 = range_input_6_6_2.get_attribute('max')
    if desired_value_6_6_2 <= int(max_value_6_6_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_6_2, desired_value_6_6_2)
    desired_value_6_6_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_6_6_3 = range_input_6_6_3.get_attribute('max')
    if desired_value_6_6_3 <= int(max_value_6_6_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_6_3, desired_value_6_6_3)
    desired_value_6_6_4 = 4  # Значение, которое нужно установить на ползунке 4
    max_value_6_6_4 = range_input_6_6_4.get_attribute('max')
    if desired_value_6_6_4 <= int(max_value_6_6_4):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_6_4, desired_value_6_6_4)
    btn_6_6_next = browser.find_element(By.ID, 'btn_6_6_next')
    btn_6_6_next.click()

# ВОПРОС 6_7
    time.sleep(0.8)
    range_input_6_7_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_7_1 input[type="range"]')
    range_input_6_7_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_7_2 input[type="range"]')
    range_input_6_7_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_7_3 input[type="range"]')
    range_input_6_7_4 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_7_4 input[type="range"]')
    desired_value_6_7_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_6_7_1 = range_input_6_7_1.get_attribute('max')
    if desired_value_6_7_1 <= int(max_value_6_7_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_7_1, desired_value_6_7_1)
    desired_value_6_7_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_6_7_2 = range_input_6_7_2.get_attribute('max')
    if desired_value_6_7_2 <= int(max_value_6_7_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_7_2, desired_value_6_7_2)
    desired_value_6_7_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_6_7_3 = range_input_6_7_3.get_attribute('max')
    if desired_value_6_7_3 <= int(max_value_6_7_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_7_3, desired_value_6_7_3)
    desired_value_6_7_4 = 4  # Значение, которое нужно установить на ползунке 4
    max_value_6_7_4 = range_input_6_7_4.get_attribute('max')
    if desired_value_6_7_4 <= int(max_value_6_7_4):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_7_4, desired_value_6_7_4)
    btn_6_7_next = browser.find_element(By.ID, 'btn_6_7_next')
    btn_6_7_next.click()

# ВОПРОС 6_8
    time.sleep(0.8)
    range_input_6_8_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_8_1 input[type="range"]')
    range_input_6_8_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_8_2 input[type="range"]')
    range_input_6_8_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_8_3 input[type="range"]')
    range_input_6_8_4 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_8_4 input[type="range"]')
    desired_value_6_8_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_6_8_1 = range_input_6_8_1.get_attribute('max')
    if desired_value_6_8_1 <= int(max_value_6_8_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_8_1, desired_value_6_8_1)
    desired_value_6_8_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_6_8_2 = range_input_6_8_2.get_attribute('max')
    if desired_value_6_8_2 <= int(max_value_6_8_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_8_2, desired_value_6_8_2)
    desired_value_6_8_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_6_8_3 = range_input_6_8_3.get_attribute('max')
    if desired_value_6_8_3 <= int(max_value_6_8_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_8_3, desired_value_6_8_3)
    desired_value_6_8_4 = 4  # Значение, которое нужно установить на ползунке 4
    max_value_6_8_4 = range_input_6_8_4.get_attribute('max')
    if desired_value_6_8_4 <= int(max_value_6_8_4):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_8_4, desired_value_6_8_4)
    btn_6_8_next = browser.find_element(By.ID, 'btn_6_8_next')
    btn_6_8_next.click()

# ВОПРОС 6_9
    time.sleep(0.8)
    range_input_6_9_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_9_1 input[type="range"]')
    range_input_6_9_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_9_2 input[type="range"]')
    range_input_6_9_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_9_3 input[type="range"]')
    range_input_6_9_4 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_9_4 input[type="range"]')
    desired_value_6_9_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_6_9_1 = range_input_6_9_1.get_attribute('max')
    if desired_value_6_9_1 <= int(max_value_6_9_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_9_1, desired_value_6_9_1)
    desired_value_6_9_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_6_9_2 = range_input_6_9_2.get_attribute('max')
    if desired_value_6_9_2 <= int(max_value_6_9_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_9_2, desired_value_6_9_2)
    desired_value_6_9_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_6_9_3 = range_input_6_9_3.get_attribute('max')
    if desired_value_6_9_3 <= int(max_value_6_9_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_9_3, desired_value_6_9_3)
    desired_value_6_9_4 = 4  # Значение, которое нужно установить на ползунке 4
    max_value_6_9_4 = range_input_6_9_4.get_attribute('max')
    if desired_value_6_9_4 <= int(max_value_6_9_4):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_9_4, desired_value_6_9_4)
    btn_6_9_next = browser.find_element(By.ID, 'btn_6_9_next')
    btn_6_9_next.click()

# ВОПРОС 6_10
    time.sleep(0.8)
    range_input_6_10_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_10_1 input[type="range"]')
    range_input_6_10_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_10_2 input[type="range"]')
    range_input_6_10_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_10_3 input[type="range"]')
    range_input_6_10_4 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_6_10_4 input[type="range"]')
    desired_value_6_10_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_6_10_1 = range_input_6_10_1.get_attribute('max')
    if desired_value_6_10_1 <= int(max_value_6_10_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_10_1, desired_value_6_10_1)
    desired_value_6_10_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_6_10_2 = range_input_6_10_2.get_attribute('max')
    if desired_value_6_10_2 <= int(max_value_6_10_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_10_2, desired_value_6_10_2)
    desired_value_6_10_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_6_10_3 = range_input_6_10_3.get_attribute('max')
    if desired_value_6_10_3 <= int(max_value_6_10_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_10_3, desired_value_6_10_3)
    desired_value_6_10_4 = 4  # Значение, которое нужно установить на ползунке 4
    max_value_6_10_4 = range_input_6_10_4.get_attribute('max')
    if desired_value_6_10_4 <= int(max_value_6_10_4):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_6_10_4, desired_value_6_10_4)
    btn_6_10_next = browser.find_element(By.ID, 'btn_6_10_next')
    btn_6_10_next.click()


# ПЕРЕЛИСТЫВАНИЯ НАЗАД

    time.sleep(0.8)
    end_test_6_prev = browser.find_element(By.ID, 'end_test_6_prev')
    end_test_6_prev.click()

    time.sleep(0.8)
    btn_6_10_prev = browser.find_element(By.ID, 'btn_6_10_prev')
    btn_6_10_prev.click()

    time.sleep(0.8)
    btn_6_9_prev = browser.find_element(By.ID, 'btn_6_9_prev')
    btn_6_9_prev.click()

    time.sleep(0.8)
    btn_6_8_prev = browser.find_element(By.ID, 'btn_6_8_prev')
    btn_6_8_prev.click()

    time.sleep(0.8)
    btn_6_7_prev = browser.find_element(By.ID, 'btn_6_7_prev')
    btn_6_7_prev.click()

    time.sleep(0.8)
    btn_6_6_prev = browser.find_element(By.ID, 'btn_6_6_prev')
    btn_6_6_prev.click()

    time.sleep(0.8)
    btn_6_5_prev = browser.find_element(By.ID, 'btn_6_5_prev')
    btn_6_5_prev.click()

    time.sleep(0.8)
    btn_6_4_prev = browser.find_element(By.ID, 'btn_6_4_prev')
    btn_6_4_prev.click()

    time.sleep(0.8)
    btn_6_3_prev = browser.find_element(By.ID, 'btn_6_3_prev')
    btn_6_3_prev.click()

    time.sleep(0.8)
    btn_6_2_prev = browser.find_element(By.ID, 'btn_6_2_prev')
    btn_6_2_prev.click()

    time.sleep(0.8)
    btn_6_1_prev = browser.find_element(By.ID, 'btn_6_1_prev')
    btn_6_1_prev.click()


except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    # Ожидание ввода от пользователя, чтобы браузер не закрылся
    input("Нажмите Enter, чтобы закрыть браузер...")
    browser.quit()