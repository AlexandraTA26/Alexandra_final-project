# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTotalcos():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_totalcos(self):
    # Test name: total_cos
    # Step # | name | target | value
    # 1 | open | /en/ | 
    self.driver.get("https://prestashop-ta26.multibit.ro/en/")
    # 2 | setWindowSize | 1070x824 | 
    self.driver.set_window_size(1070, 824)
    # 3 | click | css=.js-product:nth-child(2) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(2) img").click()
    # 4 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 5 | click | css=.cart-content-btn > .btn-secondary | 
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
    # 6 | click | css=.logo | 
    self.driver.find_element(By.CSS_SELECTOR, ".logo").click()
    # 7 | click | css=.js-product:nth-child(3) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(3) img").click()
    # 8 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 9 | click | css=.cart-content-btn > .btn-primary | 
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary").click()
  
