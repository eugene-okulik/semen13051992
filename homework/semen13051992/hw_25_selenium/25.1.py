from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

text = 'cats'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.qa-practice.com/elements/input/simple')
search_input = driver.find_element(By.NAME, 'text_string')
search_input.send_keys(text)
search_input.send_keys(Keys.ENTER)
result = driver.find_element(By.ID, 'result-text').text
print(result)
