from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://vrconcept.net"

browser = webdriver.Chrome()
browser.get(link)

time.sleep(3)

# Найдите элемент и выполните на нем операцию click
demo_button = browser.find_element(By.XPATH, "//a[contains(text(),'ПОЛУЧИТЬ ДЕМО')]")
demo_button.click()

time.sleep(3)

# Найдите другой элемент и выполните на нем операцию send_keys
input_field_FIO = browser.find_element(By.XPATH, "(//input[@id='nm-1531306243545'])[2]")
input_field_FIO.send_keys("Селениум Автоматизатор Автоматизаторович")
time.sleep(2)
input_field_FIO_test = "Селениум Автоматизатор Автоматизаторович"
#Тест приняло ли поле ввод корректно
if input_field_FIO.get_attribute('value') == input_field_FIO_test:
    print("Тест ФИО - Ok")
else:
    print("Тест ФИО - Failed")
time.sleep(2)
input_field_org = browser.find_element(By.XPATH, "(//input[@id='in-1531306540094'])[2]") #
input_field_org.send_keys("Auto_Testing_QA_Team")
time.sleep(2)
#Тест приняло ли поле ввод корректно
input_field_org_test = "Auto_Testing_QA_Team"
if input_field_org.get_attribute('value') == input_field_org_test:
    print("Тест Организация - Ok")
else:
    print("Тест Организация - Failed")
time.sleep(2)

input_field_email = browser.find_element(By.XPATH, "(//input[@id='em-1677589849544'])")
input_field_email.send_keys("sgresko@vrconcept.net")
time.sleep(1)
#Тест приняло ли поле ввод корректно
input_field_email_test = "sgresko@vrconcept.net"
if input_field_email.get_attribute('value') == input_field_email_test:
    print("Тест e-mail - Ok")
else:
    print("Тест e-mail - Failed")

input_field_phone = browser.find_element(By.XPATH, "(//input[@id='input_1702560936705'])")
input_field_phone.send_keys("9112080503")
time.sleep(2)
input_field_phone_test = "+9112080503"
if input_field_phone.get_attribute('value') == input_field_phone_test:
    print("Тест Телефон - Ok")
else:
    print("Тест Телефон - Failed")

#demo_button = browser.find_element(By.XPATH, "//button[contains(text(),'ОТПРАВИТЬ ФОРМУ')]")
#demo_button.click()
# Дополнительная пауза для просмотра результатов
time.sleep(200)

