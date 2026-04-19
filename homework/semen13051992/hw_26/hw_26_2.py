import pytest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver


def test_1(driver):
    driver.get('http://testshop.qa-practice.com/')
    product = driver.find_element(By.XPATH, "//*[@content='Customizable Desk']")
    product_name = driver.find_element(By.XPATH, "//*[@content='Customizable Desk']").text
    basket = driver.find_element(By.XPATH, "//*[@title='Shopping cart']")

    actions = ActionChains(driver)
    actions.move_to_element(product)
    actions.click(basket)
    actions.perform()

    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.modal-title')
        )
    )

    product_in_the_cart = driver.find_element(By.CSS_SELECTOR, ".in_cart .product_display_name").text
    assert product_name in product_in_the_cart
