from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import secret

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://dispace.edu.nstu.ru')
time.sleep(2)

btn = driver.find_element_by_css_selector('div.input-field>a')
btn.click()
time.sleep(2)

login = driver.find_element_by_css_selector('input[name="callback_0"]')
password = driver.find_element_by_css_selector('input[name="callback_1"]')
submit = driver.find_element_by_css_selector('input[name="callback_2"]')
login.send_keys(secret.login)
password.send_keys(secret.password)
submit.click()
time.sleep(2)
