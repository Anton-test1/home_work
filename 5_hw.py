from selenium.webdriver.common.by import By
from selenium import webdriver

def check_web_elements():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')

    elements = [driver.find_element(By.ID, 'user-name'),
                driver.find_element(By.ID, 'password'),
                driver.find_element(By.ID, 'login-button')]

    if all(elements):
        print('элементы найдены')
    else:
        print('не все элементы найдены')

check_web_elements()
