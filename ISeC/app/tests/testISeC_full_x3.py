from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os


# Инициализация веб-драйвера
browser = webdriver.Chrome()

try:
    browser.get('http://127.0.0.1:5000/')

# ВВОД КОДА
    time.sleep(1.5)
    inputCode = browser.find_element(By.ID, 'inp_code') # ОКНО ВВОДА КОДА
    inputCode.send_keys("111")
    time.sleep(0.8)
    btn_main_start = browser.find_element(By.ID, 'startTest') # КНОПКА "ПРОЙТИ ТЕСТ"
    btn_main_start.click()


# ВВОД ДАННЫХ ПОЛЬЗОВАТЕЛЯ
    time.sleep(1.5)
    btn_UDI_next = browser.find_element(By.ID, 'btn_UDI_next') # КНОПКА "ПРОДОЛЖИТЬ"
    closeBtn_UDI = browser.find_element(By.ID, 'closeBtn_UDI') # ЗАКРЫТИЕ ВСПЛЫВАЮЩЕГО ОКНА
    inputName = browser.find_element(By.ID, 'user_name') # ИМЯ
    inputSurname = browser.find_element(By.ID, 'user_surname') # ФАМИЛИЯ
    inputSexFemale = browser.find_element(By.ID, 'user_sex_female') # ПОЛ
    inputBirthyear = browser.find_element(By.ID, 'user_birthyear') # ДАТА РОЖДЕНИЯ
    inputCategory = Select(browser.find_element(By.ID, 'user_category')) # КАТЕГОРИЯ
    inputEmail = browser.find_element(By.ID, 'user_email') # ЭЛ.ПОЧТА
    inputAgreement = browser.find_element(By.ID, 'user_confirmation') # СОГЛАСИЕ НА ОБРАБОТКУ ДАННЫХ

# ВВЕДЕНЫ ВЕРНЫЕ ДАННЫЕ
    inputName.send_keys("Анна-Мария")
    time.sleep(0.1)
    inputSurname.send_keys("Мамина-Алексеева")
    time.sleep(0.1)
    inputSexFemale.click()
    time.sleep(0.1)
    inputBirthyear.send_keys("1900")
    time.sleep(0.1)
    inputCategory.select_by_value("Собственник малого бизнеса")
    time.sleep(0.1)
    inputEmail.send_keys("-")
    time.sleep(0.1)
    inputAgreement.click()
    time.sleep(0.8)
    btn_UDI_next.click()


# СТАРТ БЛОКА 1
    time.sleep(1.5)
    btn_1_start = browser.find_element(By.ID, 'test_1_start')
    btn_1_start.click()

# ВОПРОС 1_1
    # Ожидание 0,1 секунды
    time.sleep(0.8)
    # Выбор отвера на вопрос 1
    ans_1_1 = browser.find_element(By.ID, '1_1_top_2')
    ans_1_1.click()
    # Нажатие на кнопку "Далее" вопроса 1
    btn_1_1_next = browser.find_element(By.ID, 'btn_1_1_next')
    btn_1_1_next.click()

# ВОПРОС 1_2
    time.sleep(0.8)
    ans_1_2 = browser.find_element(By.ID, '1_2_top_2')
    ans_1_2.click()
    btn_1_2_next = browser.find_element(By.ID, 'btn_1_2_next')
    btn_1_2_next.click()

# ВОПРОС 1_3
    time.sleep(0.8)
    ans_1_3 = browser.find_element(By.ID, '1_3_top_2')
    ans_1_3.click()
    btn_1_3_next = browser.find_element(By.ID, 'btn_1_3_next')
    btn_1_3_next.click()

# ВОПРОС 1_4
    time.sleep(0.8)
    ans_1_4 = browser.find_element(By.ID, '1_4_top_2')
    ans_1_4.click()
    btn_1_4_next = browser.find_element(By.ID, 'btn_1_4_next')
    btn_1_4_next.click()

# ВОПРОС 1_5
    time.sleep(0.8)
    ans_1_5 = browser.find_element(By.ID, '1_5_top_2')
    ans_1_5.click()
    btn_1_5_next = browser.find_element(By.ID, 'btn_1_5_next')
    btn_1_5_next.click()

# ВОПРОС 1_6
    time.sleep(0.8)
    ans_1_6 = browser.find_element(By.ID, '1_6_top_2')
    ans_1_6.click()
    btn_1_6_next = browser.find_element(By.ID, 'btn_1_6_next')
    btn_1_6_next.click()

# ВОПРОС 1_7
    time.sleep(0.8)
    ans_1_7 = browser.find_element(By.ID, '1_7_top_2')
    ans_1_7.click()
    btn_1_7_next = browser.find_element(By.ID, 'btn_1_7_next')
    btn_1_7_next.click()

# ВОПРОС 1_8
    time.sleep(0.8)
    ans_1_8 = browser.find_element(By.ID, '1_8_top_2')
    ans_1_8.click()
    btn_1_8_next = browser.find_element(By.ID, 'btn_1_8_next')
    btn_1_8_next.click()

# ВОПРОС 1_9
    time.sleep(0.8)
    ans_1_9 = browser.find_element(By.ID, '1_9_top_2')
    ans_1_9.click()
    btn_1_9_next = browser.find_element(By.ID, 'btn_1_9_next')
    btn_1_9_next.click()

# ВОПРОС 1_10
    time.sleep(0.8)
    ans_1_10 = browser.find_element(By.ID, '1_10_top_2')
    ans_1_10.click()
    btn_1_10_next = browser.find_element(By.ID, 'btn_1_10_next')
    btn_1_10_next.click()

# ВОПРОС 1_11
    time.sleep(0.8)
    ans_1_11 = browser.find_element(By.ID, '1_11_top_2')
    ans_1_11.click()
    btn_1_11_next = browser.find_element(By.ID, 'btn_1_11_next')
    btn_1_11_next.click()

# ВОПРОС 1_12
    time.sleep(0.8)
    ans_1_12 = browser.find_element(By.ID, '1_12_top_2')
    ans_1_12.click()
    btn_1_12_next = browser.find_element(By.ID, 'btn_1_12_next')
    btn_1_12_next.click()

# ВОПРОС 1_13
    time.sleep(0.8)
    ans_1_13 = browser.find_element(By.ID, '1_13_top_2')
    ans_1_13.click()
    btn_1_13_next = browser.find_element(By.ID, 'btn_1_13_next')
    btn_1_13_next.click()

# ВОПРОС 1_14
    time.sleep(0.8)
    ans_1_14 = browser.find_element(By.ID, '1_14_top_2')
    ans_1_14.click()
    btn_1_14_next = browser.find_element(By.ID, 'btn_1_14_next')
    btn_1_14_next.click()

# ВОПРОС 1_15
    time.sleep(0.8)
    ans_1_15 = browser.find_element(By.ID, '1_15_top_2')
    ans_1_15.click()
    btn_1_15_next = browser.find_element(By.ID, 'btn_1_15_next')
    btn_1_15_next.click()

# КОНЕЦ БЛОКА 1
    time.sleep(0.8)
    ans_1_end = browser.find_element(By.ID, 'confirm_1_end')
    ans_1_end.click()
    btn_1_end_next = browser.find_element(By.ID, 'end_test_next_1')
    btn_1_end_next.click()


# СТАРТ БЛОКА 2
    time.sleep(1.5)
    btn_2_start = browser.find_element(By.ID, 'test_2_start')
    btn_2_start.click()

# ВОПРОС 2_1
    time.sleep(0.8)
    ans_2_1 = browser.find_element(By.ID, '2_1_top_2')
    ans_2_1.click()
    btn_2_1_next = browser.find_element(By.ID, 'btn_2_1_next')
    btn_2_1_next.click()

# ВОПРОС 2_2
    time.sleep(0.8)
    ans_2_2 = browser.find_element(By.ID, '2_2_top_2')
    ans_2_2.click()
    btn_2_2_next = browser.find_element(By.ID, 'btn_2_2_next')
    btn_2_2_next.click()

# ВОПРОС 2_3
    time.sleep(0.8)
    ans_2_3 = browser.find_element(By.ID, '2_3_top_2')
    ans_2_3.click()
    btn_2_3_next = browser.find_element(By.ID, 'btn_2_3_next')
    btn_2_3_next.click()

# ВОПРОС 2_4
    time.sleep(0.8)
    ans_2_4 = browser.find_element(By.ID, '2_4_top_2')
    ans_2_4.click()
    btn_2_4_next = browser.find_element(By.ID, 'btn_2_4_next')
    btn_2_4_next.click()

# ВОПРОС 2_5
    time.sleep(0.8)
    ans_2_5 = browser.find_element(By.ID, '2_5_top_2')
    ans_2_5.click()
    btn_2_5_next = browser.find_element(By.ID, 'btn_2_5_next')
    btn_2_5_next.click()

# ВОПРОС 2_6
    time.sleep(0.8)
    ans_2_6 = browser.find_element(By.ID, '2_6_top_2')
    ans_2_6.click()
    btn_2_6_next = browser.find_element(By.ID, 'btn_2_6_next')
    btn_2_6_next.click()

# ВОПРОС 2_7
    time.sleep(0.8)
    ans_2_7 = browser.find_element(By.ID, '2_7_top_2')
    ans_2_7.click()
    btn_2_7_next = browser.find_element(By.ID, 'btn_2_7_next')
    btn_2_7_next.click()

# ВОПРОС 2_8
    time.sleep(0.8)
    ans_2_8 = browser.find_element(By.ID, '2_8_top_2')
    ans_2_8.click()
    btn_2_8_next = browser.find_element(By.ID, 'btn_2_8_next')
    btn_2_8_next.click()

# ВОПРОС 2_9
    time.sleep(0.8)
    ans_2_9 = browser.find_element(By.ID, '2_9_top_2')
    ans_2_9.click()
    btn_2_9_next = browser.find_element(By.ID, 'btn_2_9_next')
    btn_2_9_next.click()

# ВОПРОС 2_10
    time.sleep(0.8)
    ans_2_10 = browser.find_element(By.ID, '2_10_top_2')
    ans_2_10.click()
    btn_2_10_next = browser.find_element(By.ID, 'btn_2_10_next')
    btn_2_10_next.click()

# ВОПРОС 2_11
    time.sleep(0.8)
    ans_2_11 = browser.find_element(By.ID, '2_11_top_2')
    ans_2_11.click()
    btn_2_11_next = browser.find_element(By.ID, 'btn_2_11_next')
    btn_2_11_next.click()

# ВОПРОС 2_12
    time.sleep(0.8)
    ans_2_12 = browser.find_element(By.ID, '2_12_top_2')
    ans_2_12.click()
    btn_2_12_next = browser.find_element(By.ID, 'btn_2_12_next')
    btn_2_12_next.click()

# ВОПРОС 2_13
    time.sleep(0.8)
    ans_2_13 = browser.find_element(By.ID, '2_13_top_2')
    ans_2_13.click()
    btn_2_13_next = browser.find_element(By.ID, 'btn_2_13_next')
    btn_2_13_next.click()

# ВОПРОС 2_14
    time.sleep(0.8)
    ans_2_14 = browser.find_element(By.ID, '2_14_top_2')
    ans_2_14.click()
    btn_2_14_next = browser.find_element(By.ID, 'btn_2_14_next')
    btn_2_14_next.click()

# ВОПРОС 2_15
    time.sleep(0.8)
    ans_2_15 = browser.find_element(By.ID, '2_15_top_2')
    ans_2_15.click()
    btn_2_15_next = browser.find_element(By.ID, 'btn_2_15_next')
    btn_2_15_next.click()

# ВОПРОС 2_16
    time.sleep(0.8)
    ans_2_16 = browser.find_element(By.ID, '2_16_top_2')
    ans_2_16.click()
    btn_2_16_next = browser.find_element(By.ID, 'btn_2_16_next')
    btn_2_16_next.click()

# ВОПРОС 2_17
    time.sleep(0.8)
    ans_2_17 = browser.find_element(By.ID, '2_17_top_2')
    ans_2_17.click()
    btn_2_17_next = browser.find_element(By.ID, 'btn_2_17_next')
    btn_2_17_next.click()

# ВОПРОС 2_18
    time.sleep(0.8)
    ans_2_18 = browser.find_element(By.ID, '2_18_top_2')
    ans_2_18.click()
    btn_2_18_next = browser.find_element(By.ID, 'btn_2_18_next')
    btn_2_18_next.click()

# ВОПРОС 2_19
    time.sleep(0.8)
    ans_2_19 = browser.find_element(By.ID, '2_19_top_2')
    ans_2_19.click()
    btn_2_19_next = browser.find_element(By.ID, 'btn_2_19_next')
    btn_2_19_next.click()

# ВОПРОС 2_20
    time.sleep(0.8)
    ans_2_20 = browser.find_element(By.ID, '2_20_top_2')
    ans_2_20.click()
    btn_2_20_next = browser.find_element(By.ID, 'btn_2_20_next')
    btn_2_20_next.click()

# ВОПРОС 2_21
    time.sleep(0.8)
    ans_2_21 = browser.find_element(By.ID, '2_21_top_2')
    ans_2_21.click()
    btn_2_21_next = browser.find_element(By.ID, 'btn_2_21_next')
    btn_2_21_next.click()

# ВОПРОС 2_22
    time.sleep(0.8)
    ans_2_22 = browser.find_element(By.ID, '2_22_top_2')
    ans_2_22.click()
    btn_2_22_next = browser.find_element(By.ID, 'btn_2_22_next')
    btn_2_22_next.click()

# ВОПРОС 2_23
    time.sleep(0.8)
    ans_2_23 = browser.find_element(By.ID, '2_23_top_2')
    ans_2_23.click()
    btn_2_23_next = browser.find_element(By.ID, 'btn_2_23_next')
    btn_2_23_next.click()

# ВОПРОС 2_24
    time.sleep(0.8)
    ans_2_24 = browser.find_element(By.ID, '2_24_top_2')
    ans_2_24.click()
    btn_2_24_next = browser.find_element(By.ID, 'btn_2_24_next')
    btn_2_24_next.click()

# ВОПРОС 2_25
    time.sleep(0.8)
    ans_2_25 = browser.find_element(By.ID, '2_25_top_2')
    ans_2_25.click()
    btn_2_25_next = browser.find_element(By.ID, 'btn_2_25_next')
    btn_2_25_next.click()

# ВОПРОС 2_26
    time.sleep(0.8)
    ans_2_26 = browser.find_element(By.ID, '2_26_top_2')
    ans_2_26.click()
    btn_2_26_next = browser.find_element(By.ID, 'btn_2_26_next')
    btn_2_26_next.click()

# ВОПРОС 2_27
    time.sleep(0.8)
    ans_2_27 = browser.find_element(By.ID, '2_27_top_2')
    ans_2_27.click()
    btn_2_27_next = browser.find_element(By.ID, 'btn_2_27_next')
    btn_2_27_next.click()

# ВОПРОС 2_28
    time.sleep(0.8)
    ans_2_28 = browser.find_element(By.ID, '2_28_top_2')
    ans_2_28.click()
    btn_2_28_next = browser.find_element(By.ID, 'btn_2_28_next')
    btn_2_28_next.click()

# ВОПРОС 2_29
    time.sleep(0.8)
    ans_2_29 = browser.find_element(By.ID, '2_29_top_2')
    ans_2_29.click()
    btn_2_29_next = browser.find_element(By.ID, 'btn_2_29_next')
    btn_2_29_next.click()

# ВОПРОС 2_30
    time.sleep(0.8)
    ans_2_30 = browser.find_element(By.ID, '2_30_top_2')
    ans_2_30.click()
    btn_2_30_next = browser.find_element(By.ID, 'btn_2_30_next')
    btn_2_30_next.click()

# КОНЕЦ БЛОКА 2
    time.sleep(0.8)
    ans_2_end = browser.find_element(By.ID, 'confirm_2_end')
    ans_2_end.click()
    btn_2_end_next = browser.find_element(By.ID, 'end_test_next_2')
    btn_2_end_next.click()


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

# КОНЕЦ БЛОКА 3
    time.sleep(0.8)
    ans_3_end = browser.find_element(By.ID, 'confirm_3_end')
    ans_3_end.click()
    btn_3_end_next = browser.find_element(By.ID, 'end_test_next_3')
    btn_3_end_next.click()


# СТАРТ БЛОКА 4
    time.sleep(1.5)
    btn_4_start = browser.find_element(By.ID, 'test_4_start')
    btn_4_start.click()

# ВОПРОС 4_1
    time.sleep(0.8)
    ans_4_1 = browser.find_element(By.ID, '4_1_1')
    ans_4_1.click()
    btn_4_1_next = browser.find_element(By.ID, 'btn_4_1_next')
    btn_4_1_next.click()

# ВОПРОС 4_2
    time.sleep(0.8)
    ans_4_2 = browser.find_element(By.ID, '4_2_1')
    ans_4_2.click()
    btn_4_2_next = browser.find_element(By.ID, 'btn_4_2_next')
    btn_4_2_next.click()

# ВОПРОС 4_3
    time.sleep(0.8)
    ans_4_3 = browser.find_element(By.ID, '4_3_1')
    ans_4_3.click()
    btn_4_3_next = browser.find_element(By.ID, 'btn_4_3_next')
    btn_4_3_next.click()

# ВОПРОС 4_4
    time.sleep(0.8)
    ans_4_4 = browser.find_element(By.ID, '4_4_1')
    ans_4_4.click()
    btn_4_4_next = browser.find_element(By.ID, 'btn_4_4_next')
    btn_4_4_next.click()

# ВОПРОС 4_5
    time.sleep(0.8)
    ans_4_5 = browser.find_element(By.ID, '4_5_1')
    ans_4_5.click()
    btn_4_5_next = browser.find_element(By.ID, 'btn_4_5_next')
    btn_4_5_next.click()

# ВОПРОС 4_6
    time.sleep(0.8)
    ans_4_6 = browser.find_element(By.ID, '4_6_1')
    ans_4_6.click()
    btn_4_6_next = browser.find_element(By.ID, 'btn_4_6_next')
    btn_4_6_next.click()

# ВОПРОС 4_7
    time.sleep(0.8)
    ans_4_7 = browser.find_element(By.ID, '4_7_1')
    ans_4_7.click()
    btn_4_7_next = browser.find_element(By.ID, 'btn_4_7_next')
    btn_4_7_next.click()

# ВОПРОС 4_8
    time.sleep(0.8)
    ans_4_8 = browser.find_element(By.ID, '4_8_1')
    ans_4_8.click()
    btn_4_8_next = browser.find_element(By.ID, 'btn_4_8_next')
    btn_4_8_next.click()

# ВОПРОС 4_9
    time.sleep(0.8)
    ans_4_9 = browser.find_element(By.ID, '4_9_1')
    ans_4_9.click()
    btn_4_9_next = browser.find_element(By.ID, 'btn_4_9_next')
    btn_4_9_next.click()

# ВОПРОС 4_10
    time.sleep(0.8)
    ans_4_10 = browser.find_element(By.ID, '4_10_1')
    ans_4_10.click()
    btn_4_10_next = browser.find_element(By.ID, 'btn_4_10_next')
    btn_4_10_next.click()

# ВОПРОС 4_11
    time.sleep(0.8)
    ans_4_11 = browser.find_element(By.ID, '4_11_1')
    ans_4_11.click()
    btn_4_11_next = browser.find_element(By.ID, 'btn_4_11_next')
    btn_4_11_next.click()

# ВОПРОС 4_12
    time.sleep(0.8)
    ans_4_12 = browser.find_element(By.ID, '4_12_1')
    ans_4_12.click()
    btn_4_12_next = browser.find_element(By.ID, 'btn_4_12_next')
    btn_4_12_next.click()

# ВОПРОС 4_13
    time.sleep(0.8)
    ans_4_13 = browser.find_element(By.ID, '4_13_1')
    ans_4_13.click()
    btn_4_13_next = browser.find_element(By.ID, 'btn_4_13_next')
    btn_4_13_next.click()

# ВОПРОС 4_14
    time.sleep(0.8)
    ans_4_14 = browser.find_element(By.ID, '4_14_1')
    ans_4_14.click()
    btn_4_14_next = browser.find_element(By.ID, 'btn_4_14_next')
    btn_4_14_next.click()

# ВОПРОС 4_15
    time.sleep(0.8)
    ans_4_15 = browser.find_element(By.ID, '4_15_1')
    ans_4_15.click()
    btn_4_15_next = browser.find_element(By.ID, 'btn_4_15_next')
    btn_4_15_next.click()

# ВОПРОС 4_16
    time.sleep(0.8)
    ans_4_16 = browser.find_element(By.ID, '4_16_1')
    ans_4_16.click()
    btn_4_16_next = browser.find_element(By.ID, 'btn_4_16_next')
    btn_4_16_next.click()

# КОНЕЦ БЛОКА 4
    time.sleep(0.8)
    ans_4_end = browser.find_element(By.ID, 'confirm_4_end')
    ans_4_end.click()
    btn_4_end_next = browser.find_element(By.ID, 'end_test_next_4')
    btn_4_end_next.click()


# СТАРТ БЛОКА 5
    time.sleep(1.5)
    btn_5_start = browser.find_element(By.ID, 'test_5_start')
    btn_5_start.click()

# ВОПРОС 5_1
    time.sleep(0.8)

    # Находим элементы input type="range" для каждого ползунка
    range_input_5_1_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_1_1 input[type="range"]')
    range_input_5_1_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_1_2 input[type="range"]')
    range_input_5_1_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_1_3 input[type="range"]')

    # Устанавливаем значение для ползунка range_input_5_1_1
    desired_value_5_1_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_1_1 = range_input_5_1_1.get_attribute(
        'max')  # Получаем максимальное значение ползунка
    # Устанавливаем значение на ползунок, если оно меньше или равно максимальному значению ползунка
    if desired_value_5_1_1 <= int(max_value_5_1_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_1_1, desired_value_5_1_1)

    # Устанавливаем значение для ползунка range_input_5_1_2
    desired_value_5_1_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_1_2 = range_input_5_1_2.get_attribute(
        'max')  # Получаем максимальное значение ползунка
    # Устанавливаем значение на ползунок, если оно меньше или равно максимальному значению ползунка
    if desired_value_5_1_2 <= int(max_value_5_1_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_1_2, desired_value_5_1_2)

    # Устанавливаем значение для ползунка range_input_5_1_3
    desired_value_5_1_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_1_3 = range_input_5_1_3.get_attribute(
        'max')  # Получаем максимальное значение ползунка
    # Устанавливаем значение на ползунок, если оно меньше или равно максимальному значению ползунка
    if desired_value_5_1_3 <= int(max_value_5_1_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_1_3, desired_value_5_1_3)

    # Нажимаем кнопку "Далее"
    btn_5_1_next = browser.find_element(By.ID, 'btn_5_1_next')
    btn_5_1_next.click()

# ВОПРОС 5_2
    time.sleep(0.8)
    range_input_5_2_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_2_1 input[type="range"]')
    range_input_5_2_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_2_2 input[type="range"]')
    range_input_5_2_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_2_3 input[type="range"]')
    desired_value_5_2_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_2_1 = range_input_5_2_1.get_attribute('max')
    if desired_value_5_2_1 <= int(max_value_5_2_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_2_1, desired_value_5_2_1)
    desired_value_5_2_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_2_2 = range_input_5_2_2.get_attribute('max')
    if desired_value_5_2_2 <= int(max_value_5_2_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_2_2, desired_value_5_2_2)
    desired_value_5_2_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_2_3 = range_input_5_2_3.get_attribute('max')
    if desired_value_5_2_3 <= int(max_value_5_2_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_2_3, desired_value_5_2_3)
    btn_5_2_next = browser.find_element(By.ID, 'btn_5_2_next')
    btn_5_2_next.click()

# ВОПРОС 5_3
    time.sleep(0.8)
    range_input_5_3_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_3_1 input[type="range"]')
    range_input_5_3_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_3_2 input[type="range"]')
    range_input_5_3_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_3_3 input[type="range"]')
    desired_value_5_3_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_3_1 = range_input_5_3_1.get_attribute('max')
    if desired_value_5_3_1 <= int(max_value_5_3_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_3_1, desired_value_5_3_1)
    desired_value_5_3_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_3_2 = range_input_5_3_2.get_attribute('max')
    if desired_value_5_3_2 <= int(max_value_5_3_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_3_2, desired_value_5_3_2)
    desired_value_5_3_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_3_3 = range_input_5_3_3.get_attribute('max')
    if desired_value_5_3_3 <= int(max_value_5_3_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_3_3, desired_value_5_3_3)
    btn_5_3_next = browser.find_element(By.ID, 'btn_5_3_next')
    btn_5_3_next.click()

# ВОПРОС 5_4
    time.sleep(0.8)
    range_input_5_4_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_4_1 input[type="range"]')
    range_input_5_4_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_4_2 input[type="range"]')
    range_input_5_4_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_4_3 input[type="range"]')
    desired_value_5_4_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_4_1 = range_input_5_4_1.get_attribute('max')
    if desired_value_5_4_1 <= int(max_value_5_4_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_4_1, desired_value_5_4_1)
    desired_value_5_4_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_4_2 = range_input_5_4_2.get_attribute('max')
    if desired_value_5_4_2 <= int(max_value_5_4_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_4_2, desired_value_5_4_2)
    desired_value_5_4_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_4_3 = range_input_5_4_3.get_attribute('max')
    if desired_value_5_4_3 <= int(max_value_5_4_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_4_3, desired_value_5_4_3)
    btn_5_4_next = browser.find_element(By.ID, 'btn_5_4_next')
    btn_5_4_next.click()

# ВОПРОС 5_5
    time.sleep(0.8)
    range_input_5_5_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_5_1 input[type="range"]')
    range_input_5_5_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_5_2 input[type="range"]')
    range_input_5_5_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_5_3 input[type="range"]')
    desired_value_5_5_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_5_1 = range_input_5_5_1.get_attribute('max')
    if desired_value_5_5_1 <= int(max_value_5_5_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_5_1, desired_value_5_5_1)
    desired_value_5_5_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_5_2 = range_input_5_5_2.get_attribute('max')
    if desired_value_5_5_2 <= int(max_value_5_5_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_5_2, desired_value_5_5_2)
    desired_value_5_5_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_5_3 = range_input_5_5_3.get_attribute('max')
    if desired_value_5_5_3 <= int(max_value_5_5_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_5_3, desired_value_5_5_3)
    btn_5_5_next = browser.find_element(By.ID, 'btn_5_5_next')
    btn_5_5_next.click()

# ВОПРОС 5_6
    time.sleep(0.8)
    range_input_5_6_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_6_1 input[type="range"]')
    range_input_5_6_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_6_2 input[type="range"]')
    range_input_5_6_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_6_3 input[type="range"]')
    desired_value_5_6_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_6_1 = range_input_5_6_1.get_attribute('max')
    if desired_value_5_6_1 <= int(max_value_5_6_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_6_1, desired_value_5_6_1)
    desired_value_5_6_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_6_2 = range_input_5_6_2.get_attribute('max')
    if desired_value_5_6_2 <= int(max_value_5_6_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_6_2, desired_value_5_6_2)
    desired_value_5_6_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_6_3 = range_input_5_6_3.get_attribute('max')
    if desired_value_5_6_3 <= int(max_value_5_6_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_6_3, desired_value_5_6_3)
    btn_5_6_next = browser.find_element(By.ID, 'btn_5_6_next')
    btn_5_6_next.click()

# ВОПРОС 5_7
    time.sleep(0.8)
    range_input_5_7_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_7_1 input[type="range"]')
    range_input_5_7_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_7_2 input[type="range"]')
    range_input_5_7_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_7_3 input[type="range"]')
    desired_value_5_7_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_7_1 = range_input_5_7_1.get_attribute('max')
    if desired_value_5_7_1 <= int(max_value_5_7_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_7_1, desired_value_5_7_1)
    desired_value_5_7_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_7_2 = range_input_5_7_2.get_attribute('max')
    if desired_value_5_7_2 <= int(max_value_5_7_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_7_2, desired_value_5_7_2)
    desired_value_5_7_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_7_3 = range_input_5_7_3.get_attribute('max')
    if desired_value_5_7_3 <= int(max_value_5_7_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_7_3, desired_value_5_7_3)
    btn_5_7_next = browser.find_element(By.ID, 'btn_5_7_next')
    btn_5_7_next.click()

# ВОПРОС 5_8
    time.sleep(0.8)
    range_input_5_8_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_8_1 input[type="range"]')
    range_input_5_8_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_8_2 input[type="range"]')
    range_input_5_8_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_8_3 input[type="range"]')
    desired_value_5_8_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_8_1 = range_input_5_8_1.get_attribute('max')
    if desired_value_5_8_1 <= int(max_value_5_8_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_8_1, desired_value_5_8_1)
    desired_value_5_8_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_8_2 = range_input_5_8_2.get_attribute('max')
    if desired_value_5_8_2 <= int(max_value_5_8_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_8_2, desired_value_5_8_2)
    desired_value_5_8_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_8_3 = range_input_5_8_3.get_attribute('max')
    if desired_value_5_8_3 <= int(max_value_5_8_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_8_3, desired_value_5_8_3)
    btn_5_8_next = browser.find_element(By.ID, 'btn_5_8_next')
    btn_5_8_next.click()

# ВОПРОС 5_9
    time.sleep(0.8)
    range_input_5_9_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_9_1 input[type="range"]')
    range_input_5_9_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_9_2 input[type="range"]')
    range_input_5_9_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_9_3 input[type="range"]')
    desired_value_5_9_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_9_1 = range_input_5_9_1.get_attribute('max')
    if desired_value_5_9_1 <= int(max_value_5_9_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_9_1, desired_value_5_9_1)
    desired_value_5_9_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_9_2 = range_input_5_9_2.get_attribute('max')
    if desired_value_5_9_2 <= int(max_value_5_9_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_9_2, desired_value_5_9_2)
    desired_value_5_9_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_9_3 = range_input_5_9_3.get_attribute('max')
    if desired_value_5_9_3 <= int(max_value_5_9_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_9_3, desired_value_5_9_3)
    btn_5_9_next = browser.find_element(By.ID, 'btn_5_9_next')
    btn_5_9_next.click()

# ВОПРОС 5_10
    time.sleep(0.8)
    range_input_5_10_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_10_1 input[type="range"]')
    range_input_5_10_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_10_2 input[type="range"]')
    range_input_5_10_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_10_3 input[type="range"]')
    desired_value_5_10_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_10_1 = range_input_5_10_1.get_attribute('max')
    if desired_value_5_10_1 <= int(max_value_5_10_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_10_1, desired_value_5_10_1)
    desired_value_5_10_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_10_2 = range_input_5_10_2.get_attribute('max')
    if desired_value_5_10_2 <= int(max_value_5_10_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_10_2, desired_value_5_10_2)
    desired_value_5_10_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_10_3 = range_input_5_10_3.get_attribute('max')
    if desired_value_5_10_3 <= int(max_value_5_10_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_10_3, desired_value_5_10_3)
    btn_5_10_next = browser.find_element(By.ID, 'btn_5_10_next')
    btn_5_10_next.click()

# ВОПРОС 5_11
    time.sleep(0.8)
    range_input_5_11_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_11_1 input[type="range"]')
    range_input_5_11_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_11_2 input[type="range"]')
    range_input_5_11_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_11_3 input[type="range"]')
    desired_value_5_11_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_11_1 = range_input_5_11_1.get_attribute('max')
    if desired_value_5_11_1 <= int(max_value_5_11_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_11_1, desired_value_5_11_1)
    desired_value_5_11_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_11_2 = range_input_5_11_2.get_attribute('max')
    if desired_value_5_11_2 <= int(max_value_5_11_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_11_2, desired_value_5_11_2)
    desired_value_5_11_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_11_3 = range_input_5_11_3.get_attribute('max')
    if desired_value_5_11_3 <= int(max_value_5_11_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_11_3, desired_value_5_11_3)
    btn_5_11_next = browser.find_element(By.ID, 'btn_5_11_next')
    btn_5_11_next.click()

# ВОПРОС 5_12
    time.sleep(0.8)
    range_input_5_12_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_12_1 input[type="range"]')
    range_input_5_12_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_12_2 input[type="range"]')
    range_input_5_12_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_12_3 input[type="range"]')
    desired_value_5_12_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_12_1 = range_input_5_12_1.get_attribute('max')
    if desired_value_5_12_1 <= int(max_value_5_12_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_12_1, desired_value_5_12_1)
    desired_value_5_12_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_12_2 = range_input_5_12_2.get_attribute('max')
    if desired_value_5_12_2 <= int(max_value_5_12_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_12_2, desired_value_5_12_2)
    desired_value_5_12_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_12_3 = range_input_5_12_3.get_attribute('max')
    if desired_value_5_12_3 <= int(max_value_5_12_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_12_3, desired_value_5_12_3)
    btn_5_12_next = browser.find_element(By.ID, 'btn_5_12_next')
    btn_5_12_next.click()

# КОНЕЦ БЛОКА 5
    time.sleep(0.8)
    ans_5_end = browser.find_element(By.ID, 'confirm_5_end')
    ans_5_end.click()
    btn_5_end_next = browser.find_element(By.ID, 'end_test_next_5')
    btn_5_end_next.click()


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


# КОНЕЦ БЛОКА 6
    time.sleep(0.8)
    ans_6_end = browser.find_element(By.ID, 'confirm_6_end')
    ans_6_end.click()
    btn_6_end_next = browser.find_element(By.ID, 'end_test_next_6')
    btn_6_end_next.click()


# ВЫБОР ВАРИАНТА ПОЛУЧЕНИЯ ИКС-ФАЙЛА
    time.sleep(0.8)

    btn_PDF_dwnl = browser.find_element(By.ID, 'PDF_dwnl')
    btn_PDF_dwnl.click()

    # btn_PDF_send = browser.find_element(By.ID, 'PDF_send')
    # btn_PDF_send.click()
    # time.sleep(0.8)
    # inputEmail = browser.find_element(By.ID, 'user_email') # ЭЛ.ПОЧТА
    # time.sleep(0.1)
    # inputEmail.send_keys("apakufai@gmail.com")
    # time.sleep(0.8)
    # btnConfirm = browser.find_element(By.ID, 'btn_confirm') # КНОПКА ПОДТВЕРЖДЕНИЯ
    # btnConfirm.click()
    
    # btn_PDF_dwnl_and_send = browser.find_element(By.ID, 'PDF_dwnl_and_send')
    # btn_PDF_dwnl_and_send.click()
    # time.sleep(0.8)
    # inputEmail = browser.find_element(By.ID, 'user_email') # ЭЛ.ПОЧТА
    # time.sleep(0.1)
    # inputEmail.send_keys("apakufai@gmail.com")
    # time.sleep(0.8)
    # btnConfirm = browser.find_element(By.ID, 'btn_confirm') # КНОПКА ПОДТВЕРЖДЕНИЯ
    # btnConfirm.click()

    time.sleep(30)
    # Обновляем страницу
    browser.refresh()



# ВВОД КОДА
    time.sleep(1.5)
    inputCode = browser.find_element(By.ID, 'inp_code') # ОКНО ВВОДА КОДА
    inputCode.send_keys("111")
    time.sleep(0.8)
    btn_main_start = browser.find_element(By.ID, 'startTest') # КНОПКА "ПРОЙТИ ТЕСТ"
    btn_main_start.click()


# ВВОД ДАННЫХ ПОЛЬЗОВАТЕЛЯ
    time.sleep(1.5)
    btn_UDI_next = browser.find_element(By.ID, 'btn_UDI_next') # КНОПКА "ПРОДОЛЖИТЬ"
    closeBtn_UDI = browser.find_element(By.ID, 'closeBtn_UDI') # ЗАКРЫТИЕ ВСПЛЫВАЮЩЕГО ОКНА
    inputName = browser.find_element(By.ID, 'user_name') # ИМЯ
    inputSurname = browser.find_element(By.ID, 'user_surname') # ФАМИЛИЯ
    inputSexFemale = browser.find_element(By.ID, 'user_sex_female') # ПОЛ
    inputBirthyear = browser.find_element(By.ID, 'user_birthyear') # ДАТА РОЖДЕНИЯ
    inputCategory = Select(browser.find_element(By.ID, 'user_category')) # КАТЕГОРИЯ
    inputEmail = browser.find_element(By.ID, 'user_email') # ЭЛ.ПОЧТА
    inputAgreement = browser.find_element(By.ID, 'user_confirmation') # СОГЛАСИЕ НА ОБРАБОТКУ ДАННЫХ

# ВВЕДЕНЫ ВЕРНЫЕ ДАННЫЕ
    inputName.send_keys("Анна-Мария")
    time.sleep(0.1)
    inputSurname.send_keys("Мамина-Алексеева")
    time.sleep(0.1)
    inputSexFemale.click()
    time.sleep(0.1)
    inputBirthyear.send_keys("1900")
    time.sleep(0.1)
    inputCategory.select_by_value("Собственник малого бизнеса")
    time.sleep(0.1)
    inputEmail.send_keys("-")
    time.sleep(0.1)
    inputAgreement.click()
    time.sleep(0.8)
    btn_UDI_next.click()


# СТАРТ БЛОКА 1
    time.sleep(1.5)
    btn_1_start = browser.find_element(By.ID, 'test_1_start')
    btn_1_start.click()

# ВОПРОС 1_1
    # Ожидание 0,1 секунды
    time.sleep(0.8)
    # Выбор отвера на вопрос 1
    ans_1_1 = browser.find_element(By.ID, '1_1_top_2')
    ans_1_1.click()
    # Нажатие на кнопку "Далее" вопроса 1
    btn_1_1_next = browser.find_element(By.ID, 'btn_1_1_next')
    btn_1_1_next.click()

# ВОПРОС 1_2
    time.sleep(0.8)
    ans_1_2 = browser.find_element(By.ID, '1_2_top_2')
    ans_1_2.click()
    btn_1_2_next = browser.find_element(By.ID, 'btn_1_2_next')
    btn_1_2_next.click()

# ВОПРОС 1_3
    time.sleep(0.8)
    ans_1_3 = browser.find_element(By.ID, '1_3_top_2')
    ans_1_3.click()
    btn_1_3_next = browser.find_element(By.ID, 'btn_1_3_next')
    btn_1_3_next.click()

# ВОПРОС 1_4
    time.sleep(0.8)
    ans_1_4 = browser.find_element(By.ID, '1_4_top_2')
    ans_1_4.click()
    btn_1_4_next = browser.find_element(By.ID, 'btn_1_4_next')
    btn_1_4_next.click()

# ВОПРОС 1_5
    time.sleep(0.8)
    ans_1_5 = browser.find_element(By.ID, '1_5_top_2')
    ans_1_5.click()
    btn_1_5_next = browser.find_element(By.ID, 'btn_1_5_next')
    btn_1_5_next.click()

# ВОПРОС 1_6
    time.sleep(0.8)
    ans_1_6 = browser.find_element(By.ID, '1_6_top_2')
    ans_1_6.click()
    btn_1_6_next = browser.find_element(By.ID, 'btn_1_6_next')
    btn_1_6_next.click()

# ВОПРОС 1_7
    time.sleep(0.8)
    ans_1_7 = browser.find_element(By.ID, '1_7_top_2')
    ans_1_7.click()
    btn_1_7_next = browser.find_element(By.ID, 'btn_1_7_next')
    btn_1_7_next.click()

# ВОПРОС 1_8
    time.sleep(0.8)
    ans_1_8 = browser.find_element(By.ID, '1_8_top_2')
    ans_1_8.click()
    btn_1_8_next = browser.find_element(By.ID, 'btn_1_8_next')
    btn_1_8_next.click()

# ВОПРОС 1_9
    time.sleep(0.8)
    ans_1_9 = browser.find_element(By.ID, '1_9_top_2')
    ans_1_9.click()
    btn_1_9_next = browser.find_element(By.ID, 'btn_1_9_next')
    btn_1_9_next.click()

# ВОПРОС 1_10
    time.sleep(0.8)
    ans_1_10 = browser.find_element(By.ID, '1_10_top_2')
    ans_1_10.click()
    btn_1_10_next = browser.find_element(By.ID, 'btn_1_10_next')
    btn_1_10_next.click()

# ВОПРОС 1_11
    time.sleep(0.8)
    ans_1_11 = browser.find_element(By.ID, '1_11_top_2')
    ans_1_11.click()
    btn_1_11_next = browser.find_element(By.ID, 'btn_1_11_next')
    btn_1_11_next.click()

# ВОПРОС 1_12
    time.sleep(0.8)
    ans_1_12 = browser.find_element(By.ID, '1_12_top_2')
    ans_1_12.click()
    btn_1_12_next = browser.find_element(By.ID, 'btn_1_12_next')
    btn_1_12_next.click()

# ВОПРОС 1_13
    time.sleep(0.8)
    ans_1_13 = browser.find_element(By.ID, '1_13_top_2')
    ans_1_13.click()
    btn_1_13_next = browser.find_element(By.ID, 'btn_1_13_next')
    btn_1_13_next.click()

# ВОПРОС 1_14
    time.sleep(0.8)
    ans_1_14 = browser.find_element(By.ID, '1_14_top_2')
    ans_1_14.click()
    btn_1_14_next = browser.find_element(By.ID, 'btn_1_14_next')
    btn_1_14_next.click()

# ВОПРОС 1_15
    time.sleep(0.8)
    ans_1_15 = browser.find_element(By.ID, '1_15_top_2')
    ans_1_15.click()
    btn_1_15_next = browser.find_element(By.ID, 'btn_1_15_next')
    btn_1_15_next.click()

# КОНЕЦ БЛОКА 1
    time.sleep(0.8)
    ans_1_end = browser.find_element(By.ID, 'confirm_1_end')
    ans_1_end.click()
    btn_1_end_next = browser.find_element(By.ID, 'end_test_next_1')
    btn_1_end_next.click()


# СТАРТ БЛОКА 2
    time.sleep(1.5)
    btn_2_start = browser.find_element(By.ID, 'test_2_start')
    btn_2_start.click()

# ВОПРОС 2_1
    time.sleep(0.8)
    ans_2_1 = browser.find_element(By.ID, '2_1_top_2')
    ans_2_1.click()
    btn_2_1_next = browser.find_element(By.ID, 'btn_2_1_next')
    btn_2_1_next.click()

# ВОПРОС 2_2
    time.sleep(0.8)
    ans_2_2 = browser.find_element(By.ID, '2_2_top_2')
    ans_2_2.click()
    btn_2_2_next = browser.find_element(By.ID, 'btn_2_2_next')
    btn_2_2_next.click()

# ВОПРОС 2_3
    time.sleep(0.8)
    ans_2_3 = browser.find_element(By.ID, '2_3_top_2')
    ans_2_3.click()
    btn_2_3_next = browser.find_element(By.ID, 'btn_2_3_next')
    btn_2_3_next.click()

# ВОПРОС 2_4
    time.sleep(0.8)
    ans_2_4 = browser.find_element(By.ID, '2_4_top_2')
    ans_2_4.click()
    btn_2_4_next = browser.find_element(By.ID, 'btn_2_4_next')
    btn_2_4_next.click()

# ВОПРОС 2_5
    time.sleep(0.8)
    ans_2_5 = browser.find_element(By.ID, '2_5_top_2')
    ans_2_5.click()
    btn_2_5_next = browser.find_element(By.ID, 'btn_2_5_next')
    btn_2_5_next.click()

# ВОПРОС 2_6
    time.sleep(0.8)
    ans_2_6 = browser.find_element(By.ID, '2_6_top_2')
    ans_2_6.click()
    btn_2_6_next = browser.find_element(By.ID, 'btn_2_6_next')
    btn_2_6_next.click()

# ВОПРОС 2_7
    time.sleep(0.8)
    ans_2_7 = browser.find_element(By.ID, '2_7_top_2')
    ans_2_7.click()
    btn_2_7_next = browser.find_element(By.ID, 'btn_2_7_next')
    btn_2_7_next.click()

# ВОПРОС 2_8
    time.sleep(0.8)
    ans_2_8 = browser.find_element(By.ID, '2_8_top_2')
    ans_2_8.click()
    btn_2_8_next = browser.find_element(By.ID, 'btn_2_8_next')
    btn_2_8_next.click()

# ВОПРОС 2_9
    time.sleep(0.8)
    ans_2_9 = browser.find_element(By.ID, '2_9_top_2')
    ans_2_9.click()
    btn_2_9_next = browser.find_element(By.ID, 'btn_2_9_next')
    btn_2_9_next.click()

# ВОПРОС 2_10
    time.sleep(0.8)
    ans_2_10 = browser.find_element(By.ID, '2_10_top_2')
    ans_2_10.click()
    btn_2_10_next = browser.find_element(By.ID, 'btn_2_10_next')
    btn_2_10_next.click()

# ВОПРОС 2_11
    time.sleep(0.8)
    ans_2_11 = browser.find_element(By.ID, '2_11_top_2')
    ans_2_11.click()
    btn_2_11_next = browser.find_element(By.ID, 'btn_2_11_next')
    btn_2_11_next.click()

# ВОПРОС 2_12
    time.sleep(0.8)
    ans_2_12 = browser.find_element(By.ID, '2_12_top_2')
    ans_2_12.click()
    btn_2_12_next = browser.find_element(By.ID, 'btn_2_12_next')
    btn_2_12_next.click()

# ВОПРОС 2_13
    time.sleep(0.8)
    ans_2_13 = browser.find_element(By.ID, '2_13_top_2')
    ans_2_13.click()
    btn_2_13_next = browser.find_element(By.ID, 'btn_2_13_next')
    btn_2_13_next.click()

# ВОПРОС 2_14
    time.sleep(0.8)
    ans_2_14 = browser.find_element(By.ID, '2_14_top_2')
    ans_2_14.click()
    btn_2_14_next = browser.find_element(By.ID, 'btn_2_14_next')
    btn_2_14_next.click()

# ВОПРОС 2_15
    time.sleep(0.8)
    ans_2_15 = browser.find_element(By.ID, '2_15_top_2')
    ans_2_15.click()
    btn_2_15_next = browser.find_element(By.ID, 'btn_2_15_next')
    btn_2_15_next.click()

# ВОПРОС 2_16
    time.sleep(0.8)
    ans_2_16 = browser.find_element(By.ID, '2_16_top_2')
    ans_2_16.click()
    btn_2_16_next = browser.find_element(By.ID, 'btn_2_16_next')
    btn_2_16_next.click()

# ВОПРОС 2_17
    time.sleep(0.8)
    ans_2_17 = browser.find_element(By.ID, '2_17_top_2')
    ans_2_17.click()
    btn_2_17_next = browser.find_element(By.ID, 'btn_2_17_next')
    btn_2_17_next.click()

# ВОПРОС 2_18
    time.sleep(0.8)
    ans_2_18 = browser.find_element(By.ID, '2_18_top_2')
    ans_2_18.click()
    btn_2_18_next = browser.find_element(By.ID, 'btn_2_18_next')
    btn_2_18_next.click()

# ВОПРОС 2_19
    time.sleep(0.8)
    ans_2_19 = browser.find_element(By.ID, '2_19_top_2')
    ans_2_19.click()
    btn_2_19_next = browser.find_element(By.ID, 'btn_2_19_next')
    btn_2_19_next.click()

# ВОПРОС 2_20
    time.sleep(0.8)
    ans_2_20 = browser.find_element(By.ID, '2_20_top_2')
    ans_2_20.click()
    btn_2_20_next = browser.find_element(By.ID, 'btn_2_20_next')
    btn_2_20_next.click()

# ВОПРОС 2_21
    time.sleep(0.8)
    ans_2_21 = browser.find_element(By.ID, '2_21_top_2')
    ans_2_21.click()
    btn_2_21_next = browser.find_element(By.ID, 'btn_2_21_next')
    btn_2_21_next.click()

# ВОПРОС 2_22
    time.sleep(0.8)
    ans_2_22 = browser.find_element(By.ID, '2_22_top_2')
    ans_2_22.click()
    btn_2_22_next = browser.find_element(By.ID, 'btn_2_22_next')
    btn_2_22_next.click()

# ВОПРОС 2_23
    time.sleep(0.8)
    ans_2_23 = browser.find_element(By.ID, '2_23_top_2')
    ans_2_23.click()
    btn_2_23_next = browser.find_element(By.ID, 'btn_2_23_next')
    btn_2_23_next.click()

# ВОПРОС 2_24
    time.sleep(0.8)
    ans_2_24 = browser.find_element(By.ID, '2_24_top_2')
    ans_2_24.click()
    btn_2_24_next = browser.find_element(By.ID, 'btn_2_24_next')
    btn_2_24_next.click()

# ВОПРОС 2_25
    time.sleep(0.8)
    ans_2_25 = browser.find_element(By.ID, '2_25_top_2')
    ans_2_25.click()
    btn_2_25_next = browser.find_element(By.ID, 'btn_2_25_next')
    btn_2_25_next.click()

# ВОПРОС 2_26
    time.sleep(0.8)
    ans_2_26 = browser.find_element(By.ID, '2_26_top_2')
    ans_2_26.click()
    btn_2_26_next = browser.find_element(By.ID, 'btn_2_26_next')
    btn_2_26_next.click()

# ВОПРОС 2_27
    time.sleep(0.8)
    ans_2_27 = browser.find_element(By.ID, '2_27_top_2')
    ans_2_27.click()
    btn_2_27_next = browser.find_element(By.ID, 'btn_2_27_next')
    btn_2_27_next.click()

# ВОПРОС 2_28
    time.sleep(0.8)
    ans_2_28 = browser.find_element(By.ID, '2_28_top_2')
    ans_2_28.click()
    btn_2_28_next = browser.find_element(By.ID, 'btn_2_28_next')
    btn_2_28_next.click()

# ВОПРОС 2_29
    time.sleep(0.8)
    ans_2_29 = browser.find_element(By.ID, '2_29_top_2')
    ans_2_29.click()
    btn_2_29_next = browser.find_element(By.ID, 'btn_2_29_next')
    btn_2_29_next.click()

# ВОПРОС 2_30
    time.sleep(0.8)
    ans_2_30 = browser.find_element(By.ID, '2_30_top_2')
    ans_2_30.click()
    btn_2_30_next = browser.find_element(By.ID, 'btn_2_30_next')
    btn_2_30_next.click()

# КОНЕЦ БЛОКА 2
    time.sleep(0.8)
    ans_2_end = browser.find_element(By.ID, 'confirm_2_end')
    ans_2_end.click()
    btn_2_end_next = browser.find_element(By.ID, 'end_test_next_2')
    btn_2_end_next.click()


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

# КОНЕЦ БЛОКА 3
    time.sleep(0.8)
    ans_3_end = browser.find_element(By.ID, 'confirm_3_end')
    ans_3_end.click()
    btn_3_end_next = browser.find_element(By.ID, 'end_test_next_3')
    btn_3_end_next.click()


# СТАРТ БЛОКА 4
    time.sleep(1.5)
    btn_4_start = browser.find_element(By.ID, 'test_4_start')
    btn_4_start.click()

# ВОПРОС 4_1
    time.sleep(0.8)
    ans_4_1 = browser.find_element(By.ID, '4_1_1')
    ans_4_1.click()
    btn_4_1_next = browser.find_element(By.ID, 'btn_4_1_next')
    btn_4_1_next.click()

# ВОПРОС 4_2
    time.sleep(0.8)
    ans_4_2 = browser.find_element(By.ID, '4_2_1')
    ans_4_2.click()
    btn_4_2_next = browser.find_element(By.ID, 'btn_4_2_next')
    btn_4_2_next.click()

# ВОПРОС 4_3
    time.sleep(0.8)
    ans_4_3 = browser.find_element(By.ID, '4_3_1')
    ans_4_3.click()
    btn_4_3_next = browser.find_element(By.ID, 'btn_4_3_next')
    btn_4_3_next.click()

# ВОПРОС 4_4
    time.sleep(0.8)
    ans_4_4 = browser.find_element(By.ID, '4_4_1')
    ans_4_4.click()
    btn_4_4_next = browser.find_element(By.ID, 'btn_4_4_next')
    btn_4_4_next.click()

# ВОПРОС 4_5
    time.sleep(0.8)
    ans_4_5 = browser.find_element(By.ID, '4_5_1')
    ans_4_5.click()
    btn_4_5_next = browser.find_element(By.ID, 'btn_4_5_next')
    btn_4_5_next.click()

# ВОПРОС 4_6
    time.sleep(0.8)
    ans_4_6 = browser.find_element(By.ID, '4_6_1')
    ans_4_6.click()
    btn_4_6_next = browser.find_element(By.ID, 'btn_4_6_next')
    btn_4_6_next.click()

# ВОПРОС 4_7
    time.sleep(0.8)
    ans_4_7 = browser.find_element(By.ID, '4_7_1')
    ans_4_7.click()
    btn_4_7_next = browser.find_element(By.ID, 'btn_4_7_next')
    btn_4_7_next.click()

# ВОПРОС 4_8
    time.sleep(0.8)
    ans_4_8 = browser.find_element(By.ID, '4_8_1')
    ans_4_8.click()
    btn_4_8_next = browser.find_element(By.ID, 'btn_4_8_next')
    btn_4_8_next.click()

# ВОПРОС 4_9
    time.sleep(0.8)
    ans_4_9 = browser.find_element(By.ID, '4_9_1')
    ans_4_9.click()
    btn_4_9_next = browser.find_element(By.ID, 'btn_4_9_next')
    btn_4_9_next.click()

# ВОПРОС 4_10
    time.sleep(0.8)
    ans_4_10 = browser.find_element(By.ID, '4_10_1')
    ans_4_10.click()
    btn_4_10_next = browser.find_element(By.ID, 'btn_4_10_next')
    btn_4_10_next.click()

# ВОПРОС 4_11
    time.sleep(0.8)
    ans_4_11 = browser.find_element(By.ID, '4_11_1')
    ans_4_11.click()
    btn_4_11_next = browser.find_element(By.ID, 'btn_4_11_next')
    btn_4_11_next.click()

# ВОПРОС 4_12
    time.sleep(0.8)
    ans_4_12 = browser.find_element(By.ID, '4_12_1')
    ans_4_12.click()
    btn_4_12_next = browser.find_element(By.ID, 'btn_4_12_next')
    btn_4_12_next.click()

# ВОПРОС 4_13
    time.sleep(0.8)
    ans_4_13 = browser.find_element(By.ID, '4_13_1')
    ans_4_13.click()
    btn_4_13_next = browser.find_element(By.ID, 'btn_4_13_next')
    btn_4_13_next.click()

# ВОПРОС 4_14
    time.sleep(0.8)
    ans_4_14 = browser.find_element(By.ID, '4_14_1')
    ans_4_14.click()
    btn_4_14_next = browser.find_element(By.ID, 'btn_4_14_next')
    btn_4_14_next.click()

# ВОПРОС 4_15
    time.sleep(0.8)
    ans_4_15 = browser.find_element(By.ID, '4_15_1')
    ans_4_15.click()
    btn_4_15_next = browser.find_element(By.ID, 'btn_4_15_next')
    btn_4_15_next.click()

# ВОПРОС 4_16
    time.sleep(0.8)
    ans_4_16 = browser.find_element(By.ID, '4_16_1')
    ans_4_16.click()
    btn_4_16_next = browser.find_element(By.ID, 'btn_4_16_next')
    btn_4_16_next.click()

# КОНЕЦ БЛОКА 4
    time.sleep(0.8)
    ans_4_end = browser.find_element(By.ID, 'confirm_4_end')
    ans_4_end.click()
    btn_4_end_next = browser.find_element(By.ID, 'end_test_next_4')
    btn_4_end_next.click()


# СТАРТ БЛОКА 5
    time.sleep(1.5)
    btn_5_start = browser.find_element(By.ID, 'test_5_start')
    btn_5_start.click()

# ВОПРОС 5_1
    time.sleep(0.8)

    # Находим элементы input type="range" для каждого ползунка
    range_input_5_1_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_1_1 input[type="range"]')
    range_input_5_1_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_1_2 input[type="range"]')
    range_input_5_1_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_1_3 input[type="range"]')

    # Устанавливаем значение для ползунка range_input_5_1_1
    desired_value_5_1_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_1_1 = range_input_5_1_1.get_attribute(
        'max')  # Получаем максимальное значение ползунка
    # Устанавливаем значение на ползунок, если оно меньше или равно максимальному значению ползунка
    if desired_value_5_1_1 <= int(max_value_5_1_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_1_1, desired_value_5_1_1)

    # Устанавливаем значение для ползунка range_input_5_1_2
    desired_value_5_1_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_1_2 = range_input_5_1_2.get_attribute(
        'max')  # Получаем максимальное значение ползунка
    # Устанавливаем значение на ползунок, если оно меньше или равно максимальному значению ползунка
    if desired_value_5_1_2 <= int(max_value_5_1_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_1_2, desired_value_5_1_2)

    # Устанавливаем значение для ползунка range_input_5_1_3
    desired_value_5_1_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_1_3 = range_input_5_1_3.get_attribute(
        'max')  # Получаем максимальное значение ползунка
    # Устанавливаем значение на ползунок, если оно меньше или равно максимальному значению ползунка
    if desired_value_5_1_3 <= int(max_value_5_1_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_1_3, desired_value_5_1_3)

    # Нажимаем кнопку "Далее"
    btn_5_1_next = browser.find_element(By.ID, 'btn_5_1_next')
    btn_5_1_next.click()

# ВОПРОС 5_2
    time.sleep(0.8)
    range_input_5_2_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_2_1 input[type="range"]')
    range_input_5_2_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_2_2 input[type="range"]')
    range_input_5_2_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_2_3 input[type="range"]')
    desired_value_5_2_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_2_1 = range_input_5_2_1.get_attribute('max')
    if desired_value_5_2_1 <= int(max_value_5_2_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_2_1, desired_value_5_2_1)
    desired_value_5_2_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_2_2 = range_input_5_2_2.get_attribute('max')
    if desired_value_5_2_2 <= int(max_value_5_2_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_2_2, desired_value_5_2_2)
    desired_value_5_2_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_2_3 = range_input_5_2_3.get_attribute('max')
    if desired_value_5_2_3 <= int(max_value_5_2_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_2_3, desired_value_5_2_3)
    btn_5_2_next = browser.find_element(By.ID, 'btn_5_2_next')
    btn_5_2_next.click()

# ВОПРОС 5_3
    time.sleep(0.8)
    range_input_5_3_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_3_1 input[type="range"]')
    range_input_5_3_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_3_2 input[type="range"]')
    range_input_5_3_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_3_3 input[type="range"]')
    desired_value_5_3_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_3_1 = range_input_5_3_1.get_attribute('max')
    if desired_value_5_3_1 <= int(max_value_5_3_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_3_1, desired_value_5_3_1)
    desired_value_5_3_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_3_2 = range_input_5_3_2.get_attribute('max')
    if desired_value_5_3_2 <= int(max_value_5_3_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_3_2, desired_value_5_3_2)
    desired_value_5_3_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_3_3 = range_input_5_3_3.get_attribute('max')
    if desired_value_5_3_3 <= int(max_value_5_3_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_3_3, desired_value_5_3_3)
    btn_5_3_next = browser.find_element(By.ID, 'btn_5_3_next')
    btn_5_3_next.click()

# ВОПРОС 5_4
    time.sleep(0.8)
    range_input_5_4_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_4_1 input[type="range"]')
    range_input_5_4_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_4_2 input[type="range"]')
    range_input_5_4_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_4_3 input[type="range"]')
    desired_value_5_4_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_4_1 = range_input_5_4_1.get_attribute('max')
    if desired_value_5_4_1 <= int(max_value_5_4_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_4_1, desired_value_5_4_1)
    desired_value_5_4_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_4_2 = range_input_5_4_2.get_attribute('max')
    if desired_value_5_4_2 <= int(max_value_5_4_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_4_2, desired_value_5_4_2)
    desired_value_5_4_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_4_3 = range_input_5_4_3.get_attribute('max')
    if desired_value_5_4_3 <= int(max_value_5_4_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_4_3, desired_value_5_4_3)
    btn_5_4_next = browser.find_element(By.ID, 'btn_5_4_next')
    btn_5_4_next.click()

# ВОПРОС 5_5
    time.sleep(0.8)
    range_input_5_5_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_5_1 input[type="range"]')
    range_input_5_5_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_5_2 input[type="range"]')
    range_input_5_5_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_5_3 input[type="range"]')
    desired_value_5_5_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_5_1 = range_input_5_5_1.get_attribute('max')
    if desired_value_5_5_1 <= int(max_value_5_5_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_5_1, desired_value_5_5_1)
    desired_value_5_5_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_5_2 = range_input_5_5_2.get_attribute('max')
    if desired_value_5_5_2 <= int(max_value_5_5_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_5_2, desired_value_5_5_2)
    desired_value_5_5_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_5_3 = range_input_5_5_3.get_attribute('max')
    if desired_value_5_5_3 <= int(max_value_5_5_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_5_3, desired_value_5_5_3)
    btn_5_5_next = browser.find_element(By.ID, 'btn_5_5_next')
    btn_5_5_next.click()

# ВОПРОС 5_6
    time.sleep(0.8)
    range_input_5_6_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_6_1 input[type="range"]')
    range_input_5_6_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_6_2 input[type="range"]')
    range_input_5_6_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_6_3 input[type="range"]')
    desired_value_5_6_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_6_1 = range_input_5_6_1.get_attribute('max')
    if desired_value_5_6_1 <= int(max_value_5_6_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_6_1, desired_value_5_6_1)
    desired_value_5_6_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_6_2 = range_input_5_6_2.get_attribute('max')
    if desired_value_5_6_2 <= int(max_value_5_6_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_6_2, desired_value_5_6_2)
    desired_value_5_6_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_6_3 = range_input_5_6_3.get_attribute('max')
    if desired_value_5_6_3 <= int(max_value_5_6_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_6_3, desired_value_5_6_3)
    btn_5_6_next = browser.find_element(By.ID, 'btn_5_6_next')
    btn_5_6_next.click()

# ВОПРОС 5_7
    time.sleep(0.8)
    range_input_5_7_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_7_1 input[type="range"]')
    range_input_5_7_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_7_2 input[type="range"]')
    range_input_5_7_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_7_3 input[type="range"]')
    desired_value_5_7_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_7_1 = range_input_5_7_1.get_attribute('max')
    if desired_value_5_7_1 <= int(max_value_5_7_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_7_1, desired_value_5_7_1)
    desired_value_5_7_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_7_2 = range_input_5_7_2.get_attribute('max')
    if desired_value_5_7_2 <= int(max_value_5_7_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_7_2, desired_value_5_7_2)
    desired_value_5_7_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_7_3 = range_input_5_7_3.get_attribute('max')
    if desired_value_5_7_3 <= int(max_value_5_7_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_7_3, desired_value_5_7_3)
    btn_5_7_next = browser.find_element(By.ID, 'btn_5_7_next')
    btn_5_7_next.click()

# ВОПРОС 5_8
    time.sleep(0.8)
    range_input_5_8_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_8_1 input[type="range"]')
    range_input_5_8_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_8_2 input[type="range"]')
    range_input_5_8_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_8_3 input[type="range"]')
    desired_value_5_8_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_8_1 = range_input_5_8_1.get_attribute('max')
    if desired_value_5_8_1 <= int(max_value_5_8_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_8_1, desired_value_5_8_1)
    desired_value_5_8_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_8_2 = range_input_5_8_2.get_attribute('max')
    if desired_value_5_8_2 <= int(max_value_5_8_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_8_2, desired_value_5_8_2)
    desired_value_5_8_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_8_3 = range_input_5_8_3.get_attribute('max')
    if desired_value_5_8_3 <= int(max_value_5_8_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_8_3, desired_value_5_8_3)
    btn_5_8_next = browser.find_element(By.ID, 'btn_5_8_next')
    btn_5_8_next.click()

# ВОПРОС 5_9
    time.sleep(0.8)
    range_input_5_9_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_9_1 input[type="range"]')
    range_input_5_9_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_9_2 input[type="range"]')
    range_input_5_9_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_9_3 input[type="range"]')
    desired_value_5_9_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_9_1 = range_input_5_9_1.get_attribute('max')
    if desired_value_5_9_1 <= int(max_value_5_9_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_9_1, desired_value_5_9_1)
    desired_value_5_9_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_9_2 = range_input_5_9_2.get_attribute('max')
    if desired_value_5_9_2 <= int(max_value_5_9_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_9_2, desired_value_5_9_2)
    desired_value_5_9_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_9_3 = range_input_5_9_3.get_attribute('max')
    if desired_value_5_9_3 <= int(max_value_5_9_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_9_3, desired_value_5_9_3)
    btn_5_9_next = browser.find_element(By.ID, 'btn_5_9_next')
    btn_5_9_next.click()

# ВОПРОС 5_10
    time.sleep(0.8)
    range_input_5_10_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_10_1 input[type="range"]')
    range_input_5_10_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_10_2 input[type="range"]')
    range_input_5_10_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_10_3 input[type="range"]')
    desired_value_5_10_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_10_1 = range_input_5_10_1.get_attribute('max')
    if desired_value_5_10_1 <= int(max_value_5_10_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_10_1, desired_value_5_10_1)
    desired_value_5_10_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_10_2 = range_input_5_10_2.get_attribute('max')
    if desired_value_5_10_2 <= int(max_value_5_10_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_10_2, desired_value_5_10_2)
    desired_value_5_10_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_10_3 = range_input_5_10_3.get_attribute('max')
    if desired_value_5_10_3 <= int(max_value_5_10_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_10_3, desired_value_5_10_3)
    btn_5_10_next = browser.find_element(By.ID, 'btn_5_10_next')
    btn_5_10_next.click()

# ВОПРОС 5_11
    time.sleep(0.8)
    range_input_5_11_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_11_1 input[type="range"]')
    range_input_5_11_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_11_2 input[type="range"]')
    range_input_5_11_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_11_3 input[type="range"]')
    desired_value_5_11_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_11_1 = range_input_5_11_1.get_attribute('max')
    if desired_value_5_11_1 <= int(max_value_5_11_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_11_1, desired_value_5_11_1)
    desired_value_5_11_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_11_2 = range_input_5_11_2.get_attribute('max')
    if desired_value_5_11_2 <= int(max_value_5_11_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_11_2, desired_value_5_11_2)
    desired_value_5_11_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_11_3 = range_input_5_11_3.get_attribute('max')
    if desired_value_5_11_3 <= int(max_value_5_11_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_11_3, desired_value_5_11_3)
    btn_5_11_next = browser.find_element(By.ID, 'btn_5_11_next')
    btn_5_11_next.click()

# ВОПРОС 5_12
    time.sleep(0.8)
    range_input_5_12_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_12_1 input[type="range"]')
    range_input_5_12_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_12_2 input[type="range"]')
    range_input_5_12_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_12_3 input[type="range"]')
    desired_value_5_12_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_12_1 = range_input_5_12_1.get_attribute('max')
    if desired_value_5_12_1 <= int(max_value_5_12_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_12_1, desired_value_5_12_1)
    desired_value_5_12_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_12_2 = range_input_5_12_2.get_attribute('max')
    if desired_value_5_12_2 <= int(max_value_5_12_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_12_2, desired_value_5_12_2)
    desired_value_5_12_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_12_3 = range_input_5_12_3.get_attribute('max')
    if desired_value_5_12_3 <= int(max_value_5_12_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_12_3, desired_value_5_12_3)
    btn_5_12_next = browser.find_element(By.ID, 'btn_5_12_next')
    btn_5_12_next.click()

# КОНЕЦ БЛОКА 5
    time.sleep(0.8)
    ans_5_end = browser.find_element(By.ID, 'confirm_5_end')
    ans_5_end.click()
    btn_5_end_next = browser.find_element(By.ID, 'end_test_next_5')
    btn_5_end_next.click()


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


# КОНЕЦ БЛОКА 6
    time.sleep(0.8)
    ans_6_end = browser.find_element(By.ID, 'confirm_6_end')
    ans_6_end.click()
    btn_6_end_next = browser.find_element(By.ID, 'end_test_next_6')
    btn_6_end_next.click()


# ВЫБОР ВАРИАНТА ПОЛУЧЕНИЯ ИКС-ФАЙЛА
    time.sleep(0.8)

    # btn_PDF_dwnl = browser.find_element(By.ID, 'PDF_dwnl')
    # btn_PDF_dwnl.click()

    btn_PDF_send = browser.find_element(By.ID, 'PDF_send')
    btn_PDF_send.click()
    time.sleep(0.8)
    inputEmail = browser.find_element(By.ID, 'user_email') # ЭЛ.ПОЧТА
    time.sleep(0.1)
    inputEmail.send_keys("apakufai@gmail.com")
    time.sleep(0.8)
    btnConfirm = browser.find_element(By.ID, 'btn_confirm') # КНОПКА ПОДТВЕРЖДЕНИЯ
    btnConfirm.click()
    
    # btn_PDF_dwnl_and_send = browser.find_element(By.ID, 'PDF_dwnl_and_send')
    # btn_PDF_dwnl_and_send.click()
    # time.sleep(0.8)
    # inputEmail = browser.find_element(By.ID, 'user_email') # ЭЛ.ПОЧТА
    # time.sleep(0.1)
    # inputEmail.send_keys("apakufai@gmail.com")
    # time.sleep(0.8)
    # btnConfirm = browser.find_element(By.ID, 'btn_confirm') # КНОПКА ПОДТВЕРЖДЕНИЯ
    # btnConfirm.click()

    time.sleep(30)
    # Обновляем страницу
    browser.refresh()



# ВВОД КОДА
    time.sleep(1.5)
    inputCode = browser.find_element(By.ID, 'inp_code') # ОКНО ВВОДА КОДА
    inputCode.send_keys("111")
    time.sleep(0.8)
    btn_main_start = browser.find_element(By.ID, 'startTest') # КНОПКА "ПРОЙТИ ТЕСТ"
    btn_main_start.click()


# ВВОД ДАННЫХ ПОЛЬЗОВАТЕЛЯ
    time.sleep(1.5)
    btn_UDI_next = browser.find_element(By.ID, 'btn_UDI_next') # КНОПКА "ПРОДОЛЖИТЬ"
    closeBtn_UDI = browser.find_element(By.ID, 'closeBtn_UDI') # ЗАКРЫТИЕ ВСПЛЫВАЮЩЕГО ОКНА
    inputName = browser.find_element(By.ID, 'user_name') # ИМЯ
    inputSurname = browser.find_element(By.ID, 'user_surname') # ФАМИЛИЯ
    inputSexFemale = browser.find_element(By.ID, 'user_sex_female') # ПОЛ
    inputBirthyear = browser.find_element(By.ID, 'user_birthyear') # ДАТА РОЖДЕНИЯ
    inputCategory = Select(browser.find_element(By.ID, 'user_category')) # КАТЕГОРИЯ
    inputEmail = browser.find_element(By.ID, 'user_email') # ЭЛ.ПОЧТА
    inputAgreement = browser.find_element(By.ID, 'user_confirmation') # СОГЛАСИЕ НА ОБРАБОТКУ ДАННЫХ

# ВВЕДЕНЫ ВЕРНЫЕ ДАННЫЕ
    inputName.send_keys("Анна-Мария")
    time.sleep(0.1)
    inputSurname.send_keys("Мамина-Алексеева")
    time.sleep(0.1)
    inputSexFemale.click()
    time.sleep(0.1)
    inputBirthyear.send_keys("1900")
    time.sleep(0.1)
    inputCategory.select_by_value("Собственник малого бизнеса")
    time.sleep(0.1)
    inputEmail.send_keys("-")
    time.sleep(0.1)
    inputAgreement.click()
    time.sleep(0.8)
    btn_UDI_next.click()


# СТАРТ БЛОКА 1
    time.sleep(1.5)
    btn_1_start = browser.find_element(By.ID, 'test_1_start')
    btn_1_start.click()

# ВОПРОС 1_1
    # Ожидание 0,1 секунды
    time.sleep(0.8)
    # Выбор отвера на вопрос 1
    ans_1_1 = browser.find_element(By.ID, '1_1_top_2')
    ans_1_1.click()
    # Нажатие на кнопку "Далее" вопроса 1
    btn_1_1_next = browser.find_element(By.ID, 'btn_1_1_next')
    btn_1_1_next.click()

# ВОПРОС 1_2
    time.sleep(0.8)
    ans_1_2 = browser.find_element(By.ID, '1_2_top_2')
    ans_1_2.click()
    btn_1_2_next = browser.find_element(By.ID, 'btn_1_2_next')
    btn_1_2_next.click()

# ВОПРОС 1_3
    time.sleep(0.8)
    ans_1_3 = browser.find_element(By.ID, '1_3_top_2')
    ans_1_3.click()
    btn_1_3_next = browser.find_element(By.ID, 'btn_1_3_next')
    btn_1_3_next.click()

# ВОПРОС 1_4
    time.sleep(0.8)
    ans_1_4 = browser.find_element(By.ID, '1_4_top_2')
    ans_1_4.click()
    btn_1_4_next = browser.find_element(By.ID, 'btn_1_4_next')
    btn_1_4_next.click()

# ВОПРОС 1_5
    time.sleep(0.8)
    ans_1_5 = browser.find_element(By.ID, '1_5_top_2')
    ans_1_5.click()
    btn_1_5_next = browser.find_element(By.ID, 'btn_1_5_next')
    btn_1_5_next.click()

# ВОПРОС 1_6
    time.sleep(0.8)
    ans_1_6 = browser.find_element(By.ID, '1_6_top_2')
    ans_1_6.click()
    btn_1_6_next = browser.find_element(By.ID, 'btn_1_6_next')
    btn_1_6_next.click()

# ВОПРОС 1_7
    time.sleep(0.8)
    ans_1_7 = browser.find_element(By.ID, '1_7_top_2')
    ans_1_7.click()
    btn_1_7_next = browser.find_element(By.ID, 'btn_1_7_next')
    btn_1_7_next.click()

# ВОПРОС 1_8
    time.sleep(0.8)
    ans_1_8 = browser.find_element(By.ID, '1_8_top_2')
    ans_1_8.click()
    btn_1_8_next = browser.find_element(By.ID, 'btn_1_8_next')
    btn_1_8_next.click()

# ВОПРОС 1_9
    time.sleep(0.8)
    ans_1_9 = browser.find_element(By.ID, '1_9_top_2')
    ans_1_9.click()
    btn_1_9_next = browser.find_element(By.ID, 'btn_1_9_next')
    btn_1_9_next.click()

# ВОПРОС 1_10
    time.sleep(0.8)
    ans_1_10 = browser.find_element(By.ID, '1_10_top_2')
    ans_1_10.click()
    btn_1_10_next = browser.find_element(By.ID, 'btn_1_10_next')
    btn_1_10_next.click()

# ВОПРОС 1_11
    time.sleep(0.8)
    ans_1_11 = browser.find_element(By.ID, '1_11_top_2')
    ans_1_11.click()
    btn_1_11_next = browser.find_element(By.ID, 'btn_1_11_next')
    btn_1_11_next.click()

# ВОПРОС 1_12
    time.sleep(0.8)
    ans_1_12 = browser.find_element(By.ID, '1_12_top_2')
    ans_1_12.click()
    btn_1_12_next = browser.find_element(By.ID, 'btn_1_12_next')
    btn_1_12_next.click()

# ВОПРОС 1_13
    time.sleep(0.8)
    ans_1_13 = browser.find_element(By.ID, '1_13_top_2')
    ans_1_13.click()
    btn_1_13_next = browser.find_element(By.ID, 'btn_1_13_next')
    btn_1_13_next.click()

# ВОПРОС 1_14
    time.sleep(0.8)
    ans_1_14 = browser.find_element(By.ID, '1_14_top_2')
    ans_1_14.click()
    btn_1_14_next = browser.find_element(By.ID, 'btn_1_14_next')
    btn_1_14_next.click()

# ВОПРОС 1_15
    time.sleep(0.8)
    ans_1_15 = browser.find_element(By.ID, '1_15_top_2')
    ans_1_15.click()
    btn_1_15_next = browser.find_element(By.ID, 'btn_1_15_next')
    btn_1_15_next.click()

# КОНЕЦ БЛОКА 1
    time.sleep(0.8)
    ans_1_end = browser.find_element(By.ID, 'confirm_1_end')
    ans_1_end.click()
    btn_1_end_next = browser.find_element(By.ID, 'end_test_next_1')
    btn_1_end_next.click()


# СТАРТ БЛОКА 2
    time.sleep(1.5)
    btn_2_start = browser.find_element(By.ID, 'test_2_start')
    btn_2_start.click()

# ВОПРОС 2_1
    time.sleep(0.8)
    ans_2_1 = browser.find_element(By.ID, '2_1_top_2')
    ans_2_1.click()
    btn_2_1_next = browser.find_element(By.ID, 'btn_2_1_next')
    btn_2_1_next.click()

# ВОПРОС 2_2
    time.sleep(0.8)
    ans_2_2 = browser.find_element(By.ID, '2_2_top_2')
    ans_2_2.click()
    btn_2_2_next = browser.find_element(By.ID, 'btn_2_2_next')
    btn_2_2_next.click()

# ВОПРОС 2_3
    time.sleep(0.8)
    ans_2_3 = browser.find_element(By.ID, '2_3_top_2')
    ans_2_3.click()
    btn_2_3_next = browser.find_element(By.ID, 'btn_2_3_next')
    btn_2_3_next.click()

# ВОПРОС 2_4
    time.sleep(0.8)
    ans_2_4 = browser.find_element(By.ID, '2_4_top_2')
    ans_2_4.click()
    btn_2_4_next = browser.find_element(By.ID, 'btn_2_4_next')
    btn_2_4_next.click()

# ВОПРОС 2_5
    time.sleep(0.8)
    ans_2_5 = browser.find_element(By.ID, '2_5_top_2')
    ans_2_5.click()
    btn_2_5_next = browser.find_element(By.ID, 'btn_2_5_next')
    btn_2_5_next.click()

# ВОПРОС 2_6
    time.sleep(0.8)
    ans_2_6 = browser.find_element(By.ID, '2_6_top_2')
    ans_2_6.click()
    btn_2_6_next = browser.find_element(By.ID, 'btn_2_6_next')
    btn_2_6_next.click()

# ВОПРОС 2_7
    time.sleep(0.8)
    ans_2_7 = browser.find_element(By.ID, '2_7_top_2')
    ans_2_7.click()
    btn_2_7_next = browser.find_element(By.ID, 'btn_2_7_next')
    btn_2_7_next.click()

# ВОПРОС 2_8
    time.sleep(0.8)
    ans_2_8 = browser.find_element(By.ID, '2_8_top_2')
    ans_2_8.click()
    btn_2_8_next = browser.find_element(By.ID, 'btn_2_8_next')
    btn_2_8_next.click()

# ВОПРОС 2_9
    time.sleep(0.8)
    ans_2_9 = browser.find_element(By.ID, '2_9_top_2')
    ans_2_9.click()
    btn_2_9_next = browser.find_element(By.ID, 'btn_2_9_next')
    btn_2_9_next.click()

# ВОПРОС 2_10
    time.sleep(0.8)
    ans_2_10 = browser.find_element(By.ID, '2_10_top_2')
    ans_2_10.click()
    btn_2_10_next = browser.find_element(By.ID, 'btn_2_10_next')
    btn_2_10_next.click()

# ВОПРОС 2_11
    time.sleep(0.8)
    ans_2_11 = browser.find_element(By.ID, '2_11_top_2')
    ans_2_11.click()
    btn_2_11_next = browser.find_element(By.ID, 'btn_2_11_next')
    btn_2_11_next.click()

# ВОПРОС 2_12
    time.sleep(0.8)
    ans_2_12 = browser.find_element(By.ID, '2_12_top_2')
    ans_2_12.click()
    btn_2_12_next = browser.find_element(By.ID, 'btn_2_12_next')
    btn_2_12_next.click()

# ВОПРОС 2_13
    time.sleep(0.8)
    ans_2_13 = browser.find_element(By.ID, '2_13_top_2')
    ans_2_13.click()
    btn_2_13_next = browser.find_element(By.ID, 'btn_2_13_next')
    btn_2_13_next.click()

# ВОПРОС 2_14
    time.sleep(0.8)
    ans_2_14 = browser.find_element(By.ID, '2_14_top_2')
    ans_2_14.click()
    btn_2_14_next = browser.find_element(By.ID, 'btn_2_14_next')
    btn_2_14_next.click()

# ВОПРОС 2_15
    time.sleep(0.8)
    ans_2_15 = browser.find_element(By.ID, '2_15_top_2')
    ans_2_15.click()
    btn_2_15_next = browser.find_element(By.ID, 'btn_2_15_next')
    btn_2_15_next.click()

# ВОПРОС 2_16
    time.sleep(0.8)
    ans_2_16 = browser.find_element(By.ID, '2_16_top_2')
    ans_2_16.click()
    btn_2_16_next = browser.find_element(By.ID, 'btn_2_16_next')
    btn_2_16_next.click()

# ВОПРОС 2_17
    time.sleep(0.8)
    ans_2_17 = browser.find_element(By.ID, '2_17_top_2')
    ans_2_17.click()
    btn_2_17_next = browser.find_element(By.ID, 'btn_2_17_next')
    btn_2_17_next.click()

# ВОПРОС 2_18
    time.sleep(0.8)
    ans_2_18 = browser.find_element(By.ID, '2_18_top_2')
    ans_2_18.click()
    btn_2_18_next = browser.find_element(By.ID, 'btn_2_18_next')
    btn_2_18_next.click()

# ВОПРОС 2_19
    time.sleep(0.8)
    ans_2_19 = browser.find_element(By.ID, '2_19_top_2')
    ans_2_19.click()
    btn_2_19_next = browser.find_element(By.ID, 'btn_2_19_next')
    btn_2_19_next.click()

# ВОПРОС 2_20
    time.sleep(0.8)
    ans_2_20 = browser.find_element(By.ID, '2_20_top_2')
    ans_2_20.click()
    btn_2_20_next = browser.find_element(By.ID, 'btn_2_20_next')
    btn_2_20_next.click()

# ВОПРОС 2_21
    time.sleep(0.8)
    ans_2_21 = browser.find_element(By.ID, '2_21_top_2')
    ans_2_21.click()
    btn_2_21_next = browser.find_element(By.ID, 'btn_2_21_next')
    btn_2_21_next.click()

# ВОПРОС 2_22
    time.sleep(0.8)
    ans_2_22 = browser.find_element(By.ID, '2_22_top_2')
    ans_2_22.click()
    btn_2_22_next = browser.find_element(By.ID, 'btn_2_22_next')
    btn_2_22_next.click()

# ВОПРОС 2_23
    time.sleep(0.8)
    ans_2_23 = browser.find_element(By.ID, '2_23_top_2')
    ans_2_23.click()
    btn_2_23_next = browser.find_element(By.ID, 'btn_2_23_next')
    btn_2_23_next.click()

# ВОПРОС 2_24
    time.sleep(0.8)
    ans_2_24 = browser.find_element(By.ID, '2_24_top_2')
    ans_2_24.click()
    btn_2_24_next = browser.find_element(By.ID, 'btn_2_24_next')
    btn_2_24_next.click()

# ВОПРОС 2_25
    time.sleep(0.8)
    ans_2_25 = browser.find_element(By.ID, '2_25_top_2')
    ans_2_25.click()
    btn_2_25_next = browser.find_element(By.ID, 'btn_2_25_next')
    btn_2_25_next.click()

# ВОПРОС 2_26
    time.sleep(0.8)
    ans_2_26 = browser.find_element(By.ID, '2_26_top_2')
    ans_2_26.click()
    btn_2_26_next = browser.find_element(By.ID, 'btn_2_26_next')
    btn_2_26_next.click()

# ВОПРОС 2_27
    time.sleep(0.8)
    ans_2_27 = browser.find_element(By.ID, '2_27_top_2')
    ans_2_27.click()
    btn_2_27_next = browser.find_element(By.ID, 'btn_2_27_next')
    btn_2_27_next.click()

# ВОПРОС 2_28
    time.sleep(0.8)
    ans_2_28 = browser.find_element(By.ID, '2_28_top_2')
    ans_2_28.click()
    btn_2_28_next = browser.find_element(By.ID, 'btn_2_28_next')
    btn_2_28_next.click()

# ВОПРОС 2_29
    time.sleep(0.8)
    ans_2_29 = browser.find_element(By.ID, '2_29_top_2')
    ans_2_29.click()
    btn_2_29_next = browser.find_element(By.ID, 'btn_2_29_next')
    btn_2_29_next.click()

# ВОПРОС 2_30
    time.sleep(0.8)
    ans_2_30 = browser.find_element(By.ID, '2_30_top_2')
    ans_2_30.click()
    btn_2_30_next = browser.find_element(By.ID, 'btn_2_30_next')
    btn_2_30_next.click()

# КОНЕЦ БЛОКА 2
    time.sleep(0.8)
    ans_2_end = browser.find_element(By.ID, 'confirm_2_end')
    ans_2_end.click()
    btn_2_end_next = browser.find_element(By.ID, 'end_test_next_2')
    btn_2_end_next.click()


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

# КОНЕЦ БЛОКА 3
    time.sleep(0.8)
    ans_3_end = browser.find_element(By.ID, 'confirm_3_end')
    ans_3_end.click()
    btn_3_end_next = browser.find_element(By.ID, 'end_test_next_3')
    btn_3_end_next.click()


# СТАРТ БЛОКА 4
    time.sleep(1.5)
    btn_4_start = browser.find_element(By.ID, 'test_4_start')
    btn_4_start.click()

# ВОПРОС 4_1
    time.sleep(0.8)
    ans_4_1 = browser.find_element(By.ID, '4_1_1')
    ans_4_1.click()
    btn_4_1_next = browser.find_element(By.ID, 'btn_4_1_next')
    btn_4_1_next.click()

# ВОПРОС 4_2
    time.sleep(0.8)
    ans_4_2 = browser.find_element(By.ID, '4_2_1')
    ans_4_2.click()
    btn_4_2_next = browser.find_element(By.ID, 'btn_4_2_next')
    btn_4_2_next.click()

# ВОПРОС 4_3
    time.sleep(0.8)
    ans_4_3 = browser.find_element(By.ID, '4_3_1')
    ans_4_3.click()
    btn_4_3_next = browser.find_element(By.ID, 'btn_4_3_next')
    btn_4_3_next.click()

# ВОПРОС 4_4
    time.sleep(0.8)
    ans_4_4 = browser.find_element(By.ID, '4_4_1')
    ans_4_4.click()
    btn_4_4_next = browser.find_element(By.ID, 'btn_4_4_next')
    btn_4_4_next.click()

# ВОПРОС 4_5
    time.sleep(0.8)
    ans_4_5 = browser.find_element(By.ID, '4_5_1')
    ans_4_5.click()
    btn_4_5_next = browser.find_element(By.ID, 'btn_4_5_next')
    btn_4_5_next.click()

# ВОПРОС 4_6
    time.sleep(0.8)
    ans_4_6 = browser.find_element(By.ID, '4_6_1')
    ans_4_6.click()
    btn_4_6_next = browser.find_element(By.ID, 'btn_4_6_next')
    btn_4_6_next.click()

# ВОПРОС 4_7
    time.sleep(0.8)
    ans_4_7 = browser.find_element(By.ID, '4_7_1')
    ans_4_7.click()
    btn_4_7_next = browser.find_element(By.ID, 'btn_4_7_next')
    btn_4_7_next.click()

# ВОПРОС 4_8
    time.sleep(0.8)
    ans_4_8 = browser.find_element(By.ID, '4_8_1')
    ans_4_8.click()
    btn_4_8_next = browser.find_element(By.ID, 'btn_4_8_next')
    btn_4_8_next.click()

# ВОПРОС 4_9
    time.sleep(0.8)
    ans_4_9 = browser.find_element(By.ID, '4_9_1')
    ans_4_9.click()
    btn_4_9_next = browser.find_element(By.ID, 'btn_4_9_next')
    btn_4_9_next.click()

# ВОПРОС 4_10
    time.sleep(0.8)
    ans_4_10 = browser.find_element(By.ID, '4_10_1')
    ans_4_10.click()
    btn_4_10_next = browser.find_element(By.ID, 'btn_4_10_next')
    btn_4_10_next.click()

# ВОПРОС 4_11
    time.sleep(0.8)
    ans_4_11 = browser.find_element(By.ID, '4_11_1')
    ans_4_11.click()
    btn_4_11_next = browser.find_element(By.ID, 'btn_4_11_next')
    btn_4_11_next.click()

# ВОПРОС 4_12
    time.sleep(0.8)
    ans_4_12 = browser.find_element(By.ID, '4_12_1')
    ans_4_12.click()
    btn_4_12_next = browser.find_element(By.ID, 'btn_4_12_next')
    btn_4_12_next.click()

# ВОПРОС 4_13
    time.sleep(0.8)
    ans_4_13 = browser.find_element(By.ID, '4_13_1')
    ans_4_13.click()
    btn_4_13_next = browser.find_element(By.ID, 'btn_4_13_next')
    btn_4_13_next.click()

# ВОПРОС 4_14
    time.sleep(0.8)
    ans_4_14 = browser.find_element(By.ID, '4_14_1')
    ans_4_14.click()
    btn_4_14_next = browser.find_element(By.ID, 'btn_4_14_next')
    btn_4_14_next.click()

# ВОПРОС 4_15
    time.sleep(0.8)
    ans_4_15 = browser.find_element(By.ID, '4_15_1')
    ans_4_15.click()
    btn_4_15_next = browser.find_element(By.ID, 'btn_4_15_next')
    btn_4_15_next.click()

# ВОПРОС 4_16
    time.sleep(0.8)
    ans_4_16 = browser.find_element(By.ID, '4_16_1')
    ans_4_16.click()
    btn_4_16_next = browser.find_element(By.ID, 'btn_4_16_next')
    btn_4_16_next.click()

# КОНЕЦ БЛОКА 4
    time.sleep(0.8)
    ans_4_end = browser.find_element(By.ID, 'confirm_4_end')
    ans_4_end.click()
    btn_4_end_next = browser.find_element(By.ID, 'end_test_next_4')
    btn_4_end_next.click()


# СТАРТ БЛОКА 5
    time.sleep(1.5)
    btn_5_start = browser.find_element(By.ID, 'test_5_start')
    btn_5_start.click()

# ВОПРОС 5_1
    time.sleep(0.8)

    # Находим элементы input type="range" для каждого ползунка
    range_input_5_1_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_1_1 input[type="range"]')
    range_input_5_1_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_1_2 input[type="range"]')
    range_input_5_1_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_1_3 input[type="range"]')

    # Устанавливаем значение для ползунка range_input_5_1_1
    desired_value_5_1_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_1_1 = range_input_5_1_1.get_attribute(
        'max')  # Получаем максимальное значение ползунка
    # Устанавливаем значение на ползунок, если оно меньше или равно максимальному значению ползунка
    if desired_value_5_1_1 <= int(max_value_5_1_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_1_1, desired_value_5_1_1)

    # Устанавливаем значение для ползунка range_input_5_1_2
    desired_value_5_1_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_1_2 = range_input_5_1_2.get_attribute(
        'max')  # Получаем максимальное значение ползунка
    # Устанавливаем значение на ползунок, если оно меньше или равно максимальному значению ползунка
    if desired_value_5_1_2 <= int(max_value_5_1_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_1_2, desired_value_5_1_2)

    # Устанавливаем значение для ползунка range_input_5_1_3
    desired_value_5_1_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_1_3 = range_input_5_1_3.get_attribute(
        'max')  # Получаем максимальное значение ползунка
    # Устанавливаем значение на ползунок, если оно меньше или равно максимальному значению ползунка
    if desired_value_5_1_3 <= int(max_value_5_1_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_1_3, desired_value_5_1_3)

    # Нажимаем кнопку "Далее"
    btn_5_1_next = browser.find_element(By.ID, 'btn_5_1_next')
    btn_5_1_next.click()

# ВОПРОС 5_2
    time.sleep(0.8)
    range_input_5_2_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_2_1 input[type="range"]')
    range_input_5_2_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_2_2 input[type="range"]')
    range_input_5_2_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_2_3 input[type="range"]')
    desired_value_5_2_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_2_1 = range_input_5_2_1.get_attribute('max')
    if desired_value_5_2_1 <= int(max_value_5_2_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_2_1, desired_value_5_2_1)
    desired_value_5_2_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_2_2 = range_input_5_2_2.get_attribute('max')
    if desired_value_5_2_2 <= int(max_value_5_2_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_2_2, desired_value_5_2_2)
    desired_value_5_2_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_2_3 = range_input_5_2_3.get_attribute('max')
    if desired_value_5_2_3 <= int(max_value_5_2_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_2_3, desired_value_5_2_3)
    btn_5_2_next = browser.find_element(By.ID, 'btn_5_2_next')
    btn_5_2_next.click()

# ВОПРОС 5_3
    time.sleep(0.8)
    range_input_5_3_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_3_1 input[type="range"]')
    range_input_5_3_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_3_2 input[type="range"]')
    range_input_5_3_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_3_3 input[type="range"]')
    desired_value_5_3_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_3_1 = range_input_5_3_1.get_attribute('max')
    if desired_value_5_3_1 <= int(max_value_5_3_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_3_1, desired_value_5_3_1)
    desired_value_5_3_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_3_2 = range_input_5_3_2.get_attribute('max')
    if desired_value_5_3_2 <= int(max_value_5_3_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_3_2, desired_value_5_3_2)
    desired_value_5_3_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_3_3 = range_input_5_3_3.get_attribute('max')
    if desired_value_5_3_3 <= int(max_value_5_3_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_3_3, desired_value_5_3_3)
    btn_5_3_next = browser.find_element(By.ID, 'btn_5_3_next')
    btn_5_3_next.click()

# ВОПРОС 5_4
    time.sleep(0.8)
    range_input_5_4_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_4_1 input[type="range"]')
    range_input_5_4_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_4_2 input[type="range"]')
    range_input_5_4_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_4_3 input[type="range"]')
    desired_value_5_4_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_4_1 = range_input_5_4_1.get_attribute('max')
    if desired_value_5_4_1 <= int(max_value_5_4_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_4_1, desired_value_5_4_1)
    desired_value_5_4_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_4_2 = range_input_5_4_2.get_attribute('max')
    if desired_value_5_4_2 <= int(max_value_5_4_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_4_2, desired_value_5_4_2)
    desired_value_5_4_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_4_3 = range_input_5_4_3.get_attribute('max')
    if desired_value_5_4_3 <= int(max_value_5_4_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_4_3, desired_value_5_4_3)
    btn_5_4_next = browser.find_element(By.ID, 'btn_5_4_next')
    btn_5_4_next.click()

# ВОПРОС 5_5
    time.sleep(0.8)
    range_input_5_5_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_5_1 input[type="range"]')
    range_input_5_5_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_5_2 input[type="range"]')
    range_input_5_5_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_5_3 input[type="range"]')
    desired_value_5_5_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_5_1 = range_input_5_5_1.get_attribute('max')
    if desired_value_5_5_1 <= int(max_value_5_5_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_5_1, desired_value_5_5_1)
    desired_value_5_5_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_5_2 = range_input_5_5_2.get_attribute('max')
    if desired_value_5_5_2 <= int(max_value_5_5_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_5_2, desired_value_5_5_2)
    desired_value_5_5_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_5_3 = range_input_5_5_3.get_attribute('max')
    if desired_value_5_5_3 <= int(max_value_5_5_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_5_3, desired_value_5_5_3)
    btn_5_5_next = browser.find_element(By.ID, 'btn_5_5_next')
    btn_5_5_next.click()

# ВОПРОС 5_6
    time.sleep(0.8)
    range_input_5_6_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_6_1 input[type="range"]')
    range_input_5_6_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_6_2 input[type="range"]')
    range_input_5_6_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_6_3 input[type="range"]')
    desired_value_5_6_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_6_1 = range_input_5_6_1.get_attribute('max')
    if desired_value_5_6_1 <= int(max_value_5_6_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_6_1, desired_value_5_6_1)
    desired_value_5_6_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_6_2 = range_input_5_6_2.get_attribute('max')
    if desired_value_5_6_2 <= int(max_value_5_6_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_6_2, desired_value_5_6_2)
    desired_value_5_6_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_6_3 = range_input_5_6_3.get_attribute('max')
    if desired_value_5_6_3 <= int(max_value_5_6_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_6_3, desired_value_5_6_3)
    btn_5_6_next = browser.find_element(By.ID, 'btn_5_6_next')
    btn_5_6_next.click()

# ВОПРОС 5_7
    time.sleep(0.8)
    range_input_5_7_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_7_1 input[type="range"]')
    range_input_5_7_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_7_2 input[type="range"]')
    range_input_5_7_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_7_3 input[type="range"]')
    desired_value_5_7_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_7_1 = range_input_5_7_1.get_attribute('max')
    if desired_value_5_7_1 <= int(max_value_5_7_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_7_1, desired_value_5_7_1)
    desired_value_5_7_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_7_2 = range_input_5_7_2.get_attribute('max')
    if desired_value_5_7_2 <= int(max_value_5_7_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_7_2, desired_value_5_7_2)
    desired_value_5_7_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_7_3 = range_input_5_7_3.get_attribute('max')
    if desired_value_5_7_3 <= int(max_value_5_7_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_7_3, desired_value_5_7_3)
    btn_5_7_next = browser.find_element(By.ID, 'btn_5_7_next')
    btn_5_7_next.click()

# ВОПРОС 5_8
    time.sleep(0.8)
    range_input_5_8_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_8_1 input[type="range"]')
    range_input_5_8_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_8_2 input[type="range"]')
    range_input_5_8_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_8_3 input[type="range"]')
    desired_value_5_8_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_8_1 = range_input_5_8_1.get_attribute('max')
    if desired_value_5_8_1 <= int(max_value_5_8_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_8_1, desired_value_5_8_1)
    desired_value_5_8_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_8_2 = range_input_5_8_2.get_attribute('max')
    if desired_value_5_8_2 <= int(max_value_5_8_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_8_2, desired_value_5_8_2)
    desired_value_5_8_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_8_3 = range_input_5_8_3.get_attribute('max')
    if desired_value_5_8_3 <= int(max_value_5_8_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_8_3, desired_value_5_8_3)
    btn_5_8_next = browser.find_element(By.ID, 'btn_5_8_next')
    btn_5_8_next.click()

# ВОПРОС 5_9
    time.sleep(0.8)
    range_input_5_9_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_9_1 input[type="range"]')
    range_input_5_9_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_9_2 input[type="range"]')
    range_input_5_9_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_9_3 input[type="range"]')
    desired_value_5_9_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_9_1 = range_input_5_9_1.get_attribute('max')
    if desired_value_5_9_1 <= int(max_value_5_9_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_9_1, desired_value_5_9_1)
    desired_value_5_9_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_9_2 = range_input_5_9_2.get_attribute('max')
    if desired_value_5_9_2 <= int(max_value_5_9_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_9_2, desired_value_5_9_2)
    desired_value_5_9_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_9_3 = range_input_5_9_3.get_attribute('max')
    if desired_value_5_9_3 <= int(max_value_5_9_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_9_3, desired_value_5_9_3)
    btn_5_9_next = browser.find_element(By.ID, 'btn_5_9_next')
    btn_5_9_next.click()

# ВОПРОС 5_10
    time.sleep(0.8)
    range_input_5_10_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_10_1 input[type="range"]')
    range_input_5_10_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_10_2 input[type="range"]')
    range_input_5_10_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_10_3 input[type="range"]')
    desired_value_5_10_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_10_1 = range_input_5_10_1.get_attribute('max')
    if desired_value_5_10_1 <= int(max_value_5_10_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_10_1, desired_value_5_10_1)
    desired_value_5_10_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_10_2 = range_input_5_10_2.get_attribute('max')
    if desired_value_5_10_2 <= int(max_value_5_10_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_10_2, desired_value_5_10_2)
    desired_value_5_10_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_10_3 = range_input_5_10_3.get_attribute('max')
    if desired_value_5_10_3 <= int(max_value_5_10_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_10_3, desired_value_5_10_3)
    btn_5_10_next = browser.find_element(By.ID, 'btn_5_10_next')
    btn_5_10_next.click()

# ВОПРОС 5_11
    time.sleep(0.8)
    range_input_5_11_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_11_1 input[type="range"]')
    range_input_5_11_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_11_2 input[type="range"]')
    range_input_5_11_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_11_3 input[type="range"]')
    desired_value_5_11_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_11_1 = range_input_5_11_1.get_attribute('max')
    if desired_value_5_11_1 <= int(max_value_5_11_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_11_1, desired_value_5_11_1)
    desired_value_5_11_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_11_2 = range_input_5_11_2.get_attribute('max')
    if desired_value_5_11_2 <= int(max_value_5_11_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_11_2, desired_value_5_11_2)
    desired_value_5_11_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_11_3 = range_input_5_11_3.get_attribute('max')
    if desired_value_5_11_3 <= int(max_value_5_11_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_11_3, desired_value_5_11_3)
    btn_5_11_next = browser.find_element(By.ID, 'btn_5_11_next')
    btn_5_11_next.click()

# ВОПРОС 5_12
    time.sleep(0.8)
    range_input_5_12_1 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_12_1 input[type="range"]')
    range_input_5_12_2 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_12_2 input[type="range"]')
    range_input_5_12_3 = browser.find_element(
        By.CSS_SELECTOR, '#inp_count_5_12_3 input[type="range"]')
    desired_value_5_12_1 = 1  # Значение, которое нужно установить на ползунке 1
    max_value_5_12_1 = range_input_5_12_1.get_attribute('max')
    if desired_value_5_12_1 <= int(max_value_5_12_1):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_12_1, desired_value_5_12_1)
    desired_value_5_12_2 = 2  # Значение, которое нужно установить на ползунке 2
    max_value_5_12_2 = range_input_5_12_2.get_attribute('max')
    if desired_value_5_12_2 <= int(max_value_5_12_2):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_12_2, desired_value_5_12_2)
    desired_value_5_12_3 = 3  # Значение, которое нужно установить на ползунке 3
    max_value_5_12_3 = range_input_5_12_3.get_attribute('max')
    if desired_value_5_12_3 <= int(max_value_5_12_3):
        browser.execute_script(
            "arguments[0].value = arguments[1];", range_input_5_12_3, desired_value_5_12_3)
    btn_5_12_next = browser.find_element(By.ID, 'btn_5_12_next')
    btn_5_12_next.click()

# КОНЕЦ БЛОКА 5
    time.sleep(0.8)
    ans_5_end = browser.find_element(By.ID, 'confirm_5_end')
    ans_5_end.click()
    btn_5_end_next = browser.find_element(By.ID, 'end_test_next_5')
    btn_5_end_next.click()


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


# КОНЕЦ БЛОКА 6
    time.sleep(0.8)
    ans_6_end = browser.find_element(By.ID, 'confirm_6_end')
    ans_6_end.click()
    btn_6_end_next = browser.find_element(By.ID, 'end_test_next_6')
    btn_6_end_next.click()


# ВЫБОР ВАРИАНТА ПОЛУЧЕНИЯ ИКС-ФАЙЛА
    time.sleep(0.8)

    # btn_PDF_dwnl = browser.find_element(By.ID, 'PDF_dwnl')
    # btn_PDF_dwnl.click()

    # btn_PDF_send = browser.find_element(By.ID, 'PDF_send')
    # btn_PDF_send.click()
    # time.sleep(0.8)
    # inputEmail = browser.find_element(By.ID, 'user_email') # ЭЛ.ПОЧТА
    # time.sleep(0.1)
    # inputEmail.send_keys("apakufai@gmail.com")
    # time.sleep(0.8)
    # btnConfirm = browser.find_element(By.ID, 'btn_confirm') # КНОПКА ПОДТВЕРЖДЕНИЯ
    # btnConfirm.click()
    
    btn_PDF_dwnl_and_send = browser.find_element(By.ID, 'PDF_dwnl_and_send')
    btn_PDF_dwnl_and_send.click()
    time.sleep(0.8)
    inputEmail = browser.find_element(By.ID, 'user_email') # ЭЛ.ПОЧТА
    time.sleep(0.1)
    inputEmail.send_keys("apakufai@gmail.com")
    time.sleep(0.8)
    btnConfirm = browser.find_element(By.ID, 'btn_confirm') # КНОПКА ПОДТВЕРЖДЕНИЯ
    btnConfirm.click()

    time.sleep(30)
    # Обновляем страницу
    browser.refresh()



except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    # Ожидание ввода от пользователя, чтобы браузер не закрылся
    input("Нажмите Enter, чтобы закрыть браузер...")
    browser.quit()