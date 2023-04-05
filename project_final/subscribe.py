import random
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time


class Subscribe(unittest.TestCase):

    Subscribe_email_input = (By.XPATH, '//input[@placeholder="Your email address" ] ')
    Prestashop_subscribe_buttom = (By.XPATH, '//input[@class="btn btn-primary float-xs-right hidden-xs-down"]')
    Alert_response_error_message = (By.XPATH, '//p[@class="alert alert-danger block_newsletter_alert"]')
    Alert_response_succes_message = (By.XPATH, '//p[@class ="alert alert-success block_newsletter_alert"]')


    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.chrome.maximize_window()
        self.chrome.get("https://prestashop-ta26.multibit.ro/en/")
        self.chrome.implicitly_wait(5)

    def tearDown(self) -> None:
        self.chrome.quit()



    def test_prestashop_subscribe_email_exist(self):
        self.chrome.find_element(*self.Subscribe_email_input).send_keys("alexandra.iuganu@gmail.com")
        self.chrome.find_element(*self.Prestashop_subscribe_buttom).click()

        prestashop_alert_text = self.chrome.find_element(*self.Alert_response_error_message).text
        expected_text = "This email address is already registered."
        assert prestashop_alert_text == expected_text

    def test_prestashop_subscribe_email_is_not_subscribe(self):
        nr = random.randint(0,9999999)
        self.chrome.find_element(*self.Subscribe_email_input).send_keys(f"alexandra.iuganu{nr}@gmail.com")
        self.chrome.find_element(*self.Prestashop_subscribe_buttom).click()

        prestashop_alert_text = self.chrome.find_element(*self.Alert_response_succes_message).text
        expected_text = "You have successfully subscribed to this newsletter."
        assert prestashop_alert_text == expected_text


