import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestAddtocart():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_addtocart(self):
        # Test name: add_to_cart
        # Step # | name | target | value
        # 1 | open | /en/ |
        self.driver.get("https://prestashop-ta26.multibit.ro/en/")
        # time.sleep(5)
        # 2 | setWindowSize | 1920x1080 |
        self.driver.set_window_size(1920, 1080)
        # time.sleep(5)
        # 3 | click | css=.js-product:nth-child(1) img |
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(1) img").click()
        # time.sleep(5)
        product_container = self.driver.find_element(By.CLASS_NAME, 'h1')
        product_name = product_container.get_attribute('innerText')

        # 4 | click | css=.add-to-cart |
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        # time.sleep(5)
        # 5 | click | css=.cart-content-btn > .btn-primary |
        element = WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary"))
        element.click()
        # time.sleep(5)
        assert product_name.lower() in self.driver.page_source.lower()
