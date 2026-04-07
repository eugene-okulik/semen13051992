from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

firstname = 'Ivan'
lastname = 'Smit'
email = 'IvanSmith@mail.ru'
mobile = '375257359284'
subjects = 'qa-practice'

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

months = driver.find_elements(By.CLASS_NAME, 'react-datepicker__month-select')
for month in months:
    if month.text == 'April':
        month.click()

years = driver.find_elements(By.CLASS_NAME, 'react-datepicker__year-select')
for year in years:
    if year.text == '2026':
        year.click()

days = driver.find_elements(By.CLASS_NAME, 'react-datepicker__day')
for day in days:
    if day.text == 5:
        day.click()

subject = driver.find_element(By.ID, 'subjectsInput')
subject.send_keys(subjects)


hobbi1 = driver.find_element(By.ID, 'hobbies-checkbox-1')
hobbi1.click()

hobbi3 = driver.find_element(By.ID, 'hobbies-checkbox-3')
hobbi3.click()

driver.execute_script("window.scrollBy(0,10000)")

adsress = driver.find_element(By.ID, 'currentAddress')
adsress.send_keys('belarus')

state = driver.find_element(By.ID, 'react-select-3-input')
state.click()
state.send_keys(Keys.ARROW_DOWN)
state.send_keys(Keys.ARROW_DOWN)
state.send_keys(Keys.ENTER)

city = driver.find_element(By.ID, 'react-select-4-input')
city.click()
state.send_keys(Keys.ARROW_DOWN)
state.send_keys(Keys.ENTER)

submit = driver.find_element(By.ID, 'submit')
submit.click()

text = driver.find_element(By.CLASS_NAME, 'modal-body')
print(text.text)
