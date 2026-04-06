import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield  driver


def test_text(driver):
    text = 'Python'
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    languages = driver.find_element(By.ID, 'id_choose_language')
    languages.click()
    languages.send_keys(Keys.ARROW_DOWN)
    languages.send_keys(Keys.ENTER)
    submit = driver.find_element(By.ID, 'submit-id-submit')
    submit.click()
    driver.execute_script("window.scrollBy(0,10000)")
    result = driver.find_element(By.ID, 'result-text')
    assert result.text == text
