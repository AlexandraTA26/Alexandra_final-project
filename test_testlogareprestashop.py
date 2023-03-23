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

class TestTestlogareprestashop():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testlogareprestashop(self):
    # Test name: test_logare_prestashop
    # Step # | name | target | value
    # 1 | open | /en/ | 
    self.driver.get("https://prestashop-ta26.multibit.ro/en/")
    # 2 | setWindowSize | 1070x824 | 
    self.driver.set_window_size(1070, 824)
    # 3 | click | css=a > .hidden-sm-down | 
    self.driver.find_element(By.CSS_SELECTOR, "a > .hidden-sm-down").click()
    # 4 | type | id=field-email | alexandra.iuganu@gmail.com
    self.driver.find_element(By.ID, "field-email").send_keys("alexandra.iuganu@gmail.com")
    # 5 | type | id=field-password | ALEXANDRA.2023
    self.driver.find_element(By.ID, "field-password").send_keys("ALEXANDRA.2023")
    # 6 | click | id=field-email | 
    self.driver.find_element(By.ID, "field-email").click()
    # 7 | click | id=field-password | 
    self.driver.find_element(By.ID, "field-password").click()
    # 8 | click | id=submit-login | 
    self.driver.find_element(By.ID, "submit-login").click()
  
