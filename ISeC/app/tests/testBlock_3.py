from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os


# Инициализация веб-драйвера
browser = webdriver.Chrome()

try:
    browser.get('http://127.0.0.1:5000/test_3')


# СТАРТ БЛОКА 3
    time.sleep(1.5)
    btn_3_start = browser.find_element(By.ID, 'test_3_start')
    btn_3_start.click()

# ВОПРОС 3_1
    time.sleep(0.8)

    # Находим элементы input type="range" для каждого ползунка
    range_input_3_1_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_1_1 input[type="range"]')
    range_input_3_1_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_1_2 input[type="range"]')
    range_input_3_1_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_1_3 input[type="range"]')

    # Устанавливаем значение для ползунка range_input_3_1_1
    desired_value_3_1_1 = 1 # Значение, которое нужно установить на ползунке 1
    max_value_3_1_1 = range_input_3_1_1.get_attribute(
        'max')  # Получаем максимальное значение ползунка
    # Устанавливаем значение на ползунок, если оно меньше или равно максимальному значению ползунка
    if desired_value_3_1_1 <= int(max_value_3_1_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_1_1, desired_value_3_1_1)

    # Устанавливаем значение для ползунка range_input_3_1_2
    desired_value_3_1_2 = 2 # Значение, которое нужно установить на ползунке 2
    max_value_3_1_2 = range_input_3_1_2.get_attribute(
        'max')  # Получаем максимальное значение ползунка
    # Устанавливаем значение на ползунок, если оно меньше или равно максимальному значению ползунка
    if desired_value_3_1_2 <= int(max_value_3_1_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_1_2, desired_value_3_1_2)

    # Устанавливаем значение для ползунка range_input_3_1_3
    desired_value_3_1_3 = 3 # Значение, которое нужно установить на ползунке 3
    max_value_3_1_3 = range_input_3_1_3.get_attribute(
        'max')  # Получаем максимальное значение ползунка
    # Устанавливаем значение на ползунок, если оно меньше или равно максимальному значению ползунка
    if desired_value_3_1_3 <= int(max_value_3_1_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_1_3, desired_value_3_1_3)

    # Нажимаем кнопку "Далее"
    btn_3_1_next = browser.find_element(By.ID, 'btn_3_1_next')
    btn_3_1_next.click()

# ВОПРОС 3_2
    time.sleep(0.8)
    range_input_3_2_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_2_1 input[type="range"]')
    range_input_3_2_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_2_2 input[type="range"]')
    range_input_3_2_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_2_3 input[type="range"]')
    desired_value_3_2_1 = 1 # Значение, которое нужно установить на ползунке 1
    max_value_3_2_1 = range_input_3_2_1.get_attribute('max')
    if desired_value_3_2_1 <= int(max_value_3_2_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_2_1, desired_value_3_2_1)
    desired_value_3_2_2 = 2 # Значение, которое нужно установить на ползунке 2
    max_value_3_2_2 = range_input_3_2_2.get_attribute('max')
    if desired_value_3_2_2 <= int(max_value_3_2_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_2_2, desired_value_3_2_2)
    desired_value_3_2_3 = 3 # Значение, которое нужно установить на ползунке 3
    max_value_3_2_3 = range_input_3_2_3.get_attribute('max')
    if desired_value_3_2_3 <= int(max_value_3_2_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_2_3, desired_value_3_2_3)
    btn_3_2_next = browser.find_element(By.ID, 'btn_3_2_next')
    btn_3_2_next.click()

# ВОПРОС 3_3
    time.sleep(0.8)
    range_input_3_3_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_3_1 input[type="range"]')
    range_input_3_3_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_3_2 input[type="range"]')
    range_input_3_3_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_3_3 input[type="range"]')
    desired_value_3_3_1 = 1 # Значение, которое нужно установить на ползунке 1
    max_value_3_3_1 = range_input_3_3_1.get_attribute('max')
    if desired_value_3_3_1 <= int(max_value_3_3_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_3_1, desired_value_3_3_1)
    desired_value_3_3_2 = 2 # Значение, которое нужно установить на ползунке 2
    max_value_3_3_2 = range_input_3_3_2.get_attribute('max')
    if desired_value_3_3_2 <= int(max_value_3_3_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_3_2, desired_value_3_3_2)
    desired_value_3_3_3 = 3 # Значение, которое нужно установить на ползунке 3
    max_value_3_3_3 = range_input_3_3_3.get_attribute('max')
    if desired_value_3_3_3 <= int(max_value_3_3_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_3_3, desired_value_3_3_3)
    btn_3_3_next = browser.find_element(By.ID, 'btn_3_3_next')
    btn_3_3_next.click()

# ВОПРОС 3_4
    time.sleep(0.8)
    range_input_3_4_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_4_1 input[type="range"]')
    range_input_3_4_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_4_2 input[type="range"]')
    range_input_3_4_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_4_3 input[type="range"]')
    desired_value_3_4_1 = 1 # Значение, которое нужно установить на ползунке 1
    max_value_3_4_1 = range_input_3_4_1.get_attribute('max')
    if desired_value_3_4_1 <= int(max_value_3_4_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_4_1, desired_value_3_4_1)
    desired_value_3_4_2 = 2 # Значение, которое нужно установить на ползунке 2
    max_value_3_4_2 = range_input_3_4_2.get_attribute('max')
    if desired_value_3_4_2 <= int(max_value_3_4_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_4_2, desired_value_3_4_2)
    desired_value_3_4_3 = 3 # Значение, которое нужно установить на ползунке 3
    max_value_3_4_3 = range_input_3_4_3.get_attribute('max')
    if desired_value_3_4_3 <= int(max_value_3_4_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_4_3, desired_value_3_4_3)
    btn_3_4_next = browser.find_element(By.ID, 'btn_3_4_next')
    btn_3_4_next.click()

# ВОПРОС 3_5
    time.sleep(0.8)
    range_input_3_5_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_5_1 input[type="range"]')
    range_input_3_5_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_5_2 input[type="range"]')
    range_input_3_5_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_5_3 input[type="range"]')
    desired_value_3_5_1 = 1 # Значение, которое нужно установить на ползунке 1
    max_value_3_5_1 = range_input_3_5_1.get_attribute('max')
    if desired_value_3_5_1 <= int(max_value_3_5_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_5_1, desired_value_3_5_1)
    desired_value_3_5_2 = 2 # Значение, которое нужно установить на ползунке 2
    max_value_3_5_2 = range_input_3_5_2.get_attribute('max')
    if desired_value_3_5_2 <= int(max_value_3_5_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_5_2, desired_value_3_5_2)
    desired_value_3_5_3 = 3 # Значение, которое нужно установить на ползунке 3
    max_value_3_5_3 = range_input_3_5_3.get_attribute('max')
    if desired_value_3_5_3 <= int(max_value_3_5_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_5_3, desired_value_3_5_3)
    btn_3_5_next = browser.find_element(By.ID, 'btn_3_5_next')
    btn_3_5_next.click()

# ВОПРОС 3_6
    time.sleep(0.8)
    range_input_3_6_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_6_1 input[type="range"]')
    range_input_3_6_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_6_2 input[type="range"]')
    range_input_3_6_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_6_3 input[type="range"]')
    desired_value_3_6_1 = 1 # Значение, которое нужно установить на ползунке 1
    max_value_3_6_1 = range_input_3_6_1.get_attribute('max')
    if desired_value_3_6_1 <= int(max_value_3_6_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_6_1, desired_value_3_6_1)
    desired_value_3_6_2 = 2 # Значение, которое нужно установить на ползунке 2
    max_value_3_6_2 = range_input_3_6_2.get_attribute('max')
    if desired_value_3_6_2 <= int(max_value_3_6_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_6_2, desired_value_3_6_2)
    desired_value_3_6_3 = 3 # Значение, которое нужно установить на ползунке 3
    max_value_3_6_3 = range_input_3_6_3.get_attribute('max')
    if desired_value_3_6_3 <= int(max_value_3_6_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_6_3, desired_value_3_6_3)
    btn_3_6_next = browser.find_element(By.ID, 'btn_3_6_next')
    btn_3_6_next.click()

# ВОПРОС 3_7
    time.sleep(0.8)
    range_input_3_7_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_7_1 input[type="range"]')
    range_input_3_7_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_7_2 input[type="range"]')
    range_input_3_7_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_7_3 input[type="range"]')
    desired_value_3_7_1 = 1 # Значение, которое нужно установить на ползунке 1
    max_value_3_7_1 = range_input_3_7_1.get_attribute('max')
    if desired_value_3_7_1 <= int(max_value_3_7_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_7_1, desired_value_3_7_1)
    desired_value_3_7_2 = 2 # Значение, которое нужно установить на ползунке 2
    max_value_3_7_2 = range_input_3_7_2.get_attribute('max')
    if desired_value_3_7_2 <= int(max_value_3_7_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_7_2, desired_value_3_7_2)
    desired_value_3_7_3 = 3 # Значение, которое нужно установить на ползунке 3
    max_value_3_7_3 = range_input_3_7_3.get_attribute('max')
    if desired_value_3_7_3 <= int(max_value_3_7_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_7_3, desired_value_3_7_3)
    btn_3_7_next = browser.find_element(By.ID, 'btn_3_7_next')
    btn_3_7_next.click()

# ВОПРОС 3_8
    time.sleep(0.8)
    range_input_3_8_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_8_1 input[type="range"]')
    range_input_3_8_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_8_2 input[type="range"]')
    range_input_3_8_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_8_3 input[type="range"]')
    desired_value_3_8_1 = 1 # Значение, которое нужно установить на ползунке 1
    max_value_3_8_1 = range_input_3_8_1.get_attribute('max')
    if desired_value_3_8_1 <= int(max_value_3_8_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_8_1, desired_value_3_8_1)
    desired_value_3_8_2 = 2 # Значение, которое нужно установить на ползунке 2
    max_value_3_8_2 = range_input_3_8_2.get_attribute('max')
    if desired_value_3_8_2 <= int(max_value_3_8_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_8_2, desired_value_3_8_2)
    desired_value_3_8_3 = 3 # Значение, которое нужно установить на ползунке 3
    max_value_3_8_3 = range_input_3_8_3.get_attribute('max')
    if desired_value_3_8_3 <= int(max_value_3_8_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_8_3, desired_value_3_8_3)
    btn_3_8_next = browser.find_element(By.ID, 'btn_3_8_next')
    btn_3_8_next.click()

# ВОПРОС 3_9
    time.sleep(0.8)
    range_input_3_9_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_9_1 input[type="range"]')
    range_input_3_9_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_9_2 input[type="range"]')
    range_input_3_9_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_3_9_3 input[type="range"]')
    desired_value_3_9_1 = 1 # Значение, которое нужно установить на ползунке 1
    max_value_3_9_1 = range_input_3_9_1.get_attribute('max')
    if desired_value_3_9_1 <= int(max_value_3_9_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_9_1, desired_value_3_9_1)
    desired_value_3_9_2 = 2 # Значение, которое нужно установить на ползунке 2
    max_value_3_9_2 = range_input_3_9_2.get_attribute('max')
    if desired_value_3_9_2 <= int(max_value_3_9_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_9_2, desired_value_3_9_2)
    desired_value_3_9_3 = 3 # Значение, которое нужно установить на ползунке 3
    max_value_3_9_3 = range_input_3_9_3.get_attribute('max')
    if desired_value_3_9_3 <= int(max_value_3_9_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_3_9_3, desired_value_3_9_3)
    btn_3_9_next = browser.find_element(By.ID, 'btn_3_9_next')
    btn_3_9_next.click()


# ПЕРЕЛИСТЫВАНИЯ НАЗАД

    time.sleep(0.8)
    end_test_3_prev = browser.find_element(By.ID, 'end_test_3_prev')
    end_test_3_prev.click()

    time.sleep(0.8)
    btn_3_9_prev = browser.find_element(By.ID, 'btn_3_9_prev')
    btn_3_9_prev.click()

    time.sleep(0.8)
    btn_3_8_prev = browser.find_element(By.ID, 'btn_3_8_prev')
    btn_3_8_prev.click()

    time.sleep(0.8)
    btn_3_7_prev = browser.find_element(By.ID, 'btn_3_7_prev')
    btn_3_7_prev.click()

    time.sleep(0.8)
    btn_3_6_prev = browser.find_element(By.ID, 'btn_3_6_prev')
    btn_3_6_prev.click()

    time.sleep(0.8)
    btn_3_5_prev = browser.find_element(By.ID, 'btn_3_5_prev')
    btn_3_5_prev.click()

    time.sleep(0.8)
    btn_3_4_prev = browser.find_element(By.ID, 'btn_3_4_prev')
    btn_3_4_prev.click()

    time.sleep(0.8)
    btn_3_3_prev = browser.find_element(By.ID, 'btn_3_3_prev')
    btn_3_3_prev.click()

    time.sleep(0.8)
    btn_3_2_prev = browser.find_element(By.ID, 'btn_3_2_prev')
    btn_3_2_prev.click()

    time.sleep(0.8)
    btn_3_1_prev = browser.find_element(By.ID, 'btn_3_1_prev')
    btn_3_1_prev.click()

except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    # Ожидание ввода от пользователя, чтобы браузер не закрылся
    input("Нажмите Enter, чтобы закрыть браузер...")
    browser.quit()