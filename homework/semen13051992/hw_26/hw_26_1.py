import pytest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver


def test_1_1(driver):
    driver.get('http://testshop.qa-practice.com/')

    product_name = driver.find_element(By.LINK_TEXT, 'Customizable Desk').text

    tabs = driver.window_handles
    driver.switch_to.new_window('tab')
    driver.get("http://testshop.qa-practice.com/shop/customizable-desk-9#attr=1,3")

    add_to_cart = driver.find_element(By.ID, 'add_to_cart')
    add_to_cart.click()

    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.btn.btn-secondary')
        )
    )

    button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-secondary')
    button.click()
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(concat(' ', @class, ' '), 'rounded-pill')]")
        )
    )

    driver.close()

    driver.switch_to.window(tabs[0])
    driver.refresh()

    basket = driver.find_element(By.XPATH, "//*[contains(concat(' ', @class, ' '), 'rounded-pill')]").text
    baskets = driver.find_element(By.CSS_SELECTOR, '.o_wsale_my_cart')
    baskets.click()

    product_in_the_cart = driver.find_element(By.CSS_SELECTOR, '.d-inline').text

    assert basket == '1'
    assert product_name in product_in_the_cart


def test_1_2(driver):
    driver.get('http://testshop.qa-practice.com/')

    product = driver.find_element(By.LINK_TEXT, 'Customizable Desk')
    product_name = driver.find_element(By.LINK_TEXT, 'Customizable Desk').text

    ActionChains(driver).key_down(Keys.CONTROL).click(product).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    add_to_cart = driver.find_element(By.ID, 'add_to_cart')
    add_to_cart.click()

    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.btn.btn-secondary')
        )
    )

    button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-secondary')
    button.click()

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(concat(' ', @class, ' '), 'rounded-pill')]")
        )
    )

    driver.close()

    driver.switch_to.window(tabs[0])
    driver.refresh()

    basket = driver.find_element(By.XPATH, "//*[contains(concat(' ', @class, ' '), 'rounded-pill')]").text
    baskets = driver.find_element(By.CSS_SELECTOR, '.o_wsale_my_cart')
    baskets.click()

    product_in_the_cart = driver.find_element(By.CSS_SELECTOR, '.d-inline').text

    assert basket == '1'
    assert product_name in product_in_the_cart
