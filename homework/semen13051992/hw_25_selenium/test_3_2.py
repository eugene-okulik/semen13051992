import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield  driver


def test_text_1(driver):
    driver.implicitly_wait(10)
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start = driver.find_element(By.XPATH, '//*[@id="start"]/button')
    start.click()
    finish = driver.find_element(By.ID, 'finish')
    assert finish.is_displayed()


def test_text_2(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start = driver.find_element(By.XPATH, '//*[@id="start"]/button')
    start.click()
    wait = WebDriverWait(driver, 5)
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, 'finish')
        )
    )
    finish = driver.find_element(By.ID, 'finish')
    assert finish.text == 'Hello World!'
    assert finish.is_displayed()
