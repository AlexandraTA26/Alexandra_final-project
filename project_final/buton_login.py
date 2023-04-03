import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

class Login(unittest.TestCase):

    prestashop_buttom_sign_in = (By.XPATH,'//button[@class="btn btn-primary" and @data-link-action="sign-in"]')
    prestashop_my_store = (By.XPATH)
    username = (By.ID, "field-email")
    parola =(By.ID, "field-password")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.chrome.maximize_window()
        self.chrome.get("https://prestashop-ta26.multibit.ro/en/login?back=my-account")
        self.chrome.implicitly_wait(2)

    def tearDown(self) -> None:
        self.chrome.quit()
    #@unittest.skip
    def test_prestashop_buttom_sign_in(self):
        self.chrome.find_element(*self.username).send_keys("alexandra.iuganu@gmail.com")
        self.chrome.find_element(*self.parola).send_keys("ALEXANDRA.2023")
        self.chrome.find_element(*self.prestashop_buttom_sign_in).click()
        curent_url = self.chrome.current_url
        expected_text = "https://prestashop-ta26.multibit.ro/en/my-account"
        assert curent_url == expected_text

    def test_prestashop_invalid_username(self):
        self.chrome.find_element(*self.username).send_keys("voicu.alexandra")
        time.sleep(2)
        self.chrome.find_element(*self.parola).send_keys("ALEXANDRA.2023")
        self.chrome.find_element(*self.prestashop_buttom_sign_in).click()
        curent_url = self.chrome.current_url
        expected_text = "https://prestashop-ta26.multibit.ro/en/login?back=my-account"
        assert curent_url == expected_text

    def test_prestashop_invalid_password(self):
        self.chrome.find_element(*self.username).send_keys("alexandra.iuganu@gmail.com")
        self.chrome.find_element(*self.parola).send_keys("ALEXANDRAa.2023")
        self.chrome.find_element(*self.prestashop_buttom_sign_in).click()
        curent_url = self.chrome.current_url
        expected_text = "https://prestashop-ta26.multibit.ro/en/login?back=my-account"
        assert curent_url == expected_text

    def test_prestashop_missing_username(self):
        self.chrome.find_element(*self.parola).send_keys("ALEXANDRA.2023")
        self.chrome.find_element(*self.prestashop_buttom_sign_in).click()
        curent_url = self.chrome.current_url
        expected_text = "https://prestashop-ta26.multibit.ro/en/login?back=my-account"
        assert curent_url == expected_text

    def test_prestashop_missing_password(self):
        self.chrome.find_element(*self.username).send_keys("alexandra.iuganu@gmail.com")
        self.chrome.find_element(*self.prestashop_buttom_sign_in).click()
        curent_url = self.chrome.current_url
        expected_text = "https://prestashop-ta26.multibit.ro/en/login?back=my-account"
        assert curent_url == expected_text






















