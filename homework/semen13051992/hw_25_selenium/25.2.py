from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

firstname = 'Ivan'
lastname = 'Smit'
email = 'IvanSmith@mail.ru'
mobile = '375257359284'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://demoqa.com/automation-practice-form')

firstname_input = driver.find_element(By.ID, 'firstName')
firstname_input.send_keys(firstname)

lastname_input = driver.find_element(By.ID, 'lastName')
lastname_input.send_keys(lastname)

email_input = driver.find_element(By.ID, 'userEmail')
email_input.send_keys(email)

gender_input = driver.find_element(By.ID, 'gender-radio-1')
gender_input.click()

mobile_input = driver.find_element(By.ID, 'userNumber')
mobile_input.send_keys(mobile)

data_input = driver.find_element(By.ID, 'dateOfBirthInput')
data_input.click()

months = driver.find_elements(By.TAG_NAME, 'option')
for month in months:
    if month.text == "January":
        month.click()

years = driver.find_elements(By.TAG_NAME, 'option')
for year in years:
    if year.text == "2020":
        year.click()

days = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__day.react-datepicker__day--013')
days.click()

subject_input = driver.find_element(By.ID, 'subjectsInput')
subject_input.click()
subject_input.send_keys('a')
subject_input.send_keys(Keys.ARROW_DOWN)
subject_input.send_keys(Keys.ENTER)
subject_input.send_keys('c')
subject_input.send_keys(Keys.ARROW_DOWN)
subject_input.send_keys(Keys.ENTER)

hobbi1 = driver.find_element(By.ID, 'hobbies-checkbox-1')
hobbi1.click()

hobbi3 = driver.find_element(By.ID, 'hobbies-checkbox-3')
hobbi3.click()

driver.find_element(By.ID, 'submit').send_keys(Keys.TAB)
driver.find_element(By.ID, 'submit').send_keys(Keys.TAB)

adsress = driver.find_element(By.ID, 'currentAddress')
adsress.send_keys('belarus')

state = driver.find_element(By.ID, 'react-select-3-input')
state.send_keys(Keys.ARROW_DOWN)
state.send_keys(Keys.ENTER)

city = driver.find_element(By.ID, 'react-select-4-live-region')
state.send_keys('Noida')

submit = driver.find_element(By.ID, 'submit')
submit.click()

text = driver.find_element(By.CLASS_NAME, 'modal-body')
print(text.text)
