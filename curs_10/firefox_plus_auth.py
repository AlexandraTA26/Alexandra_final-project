import time
import unittest
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


class Authentication_in_firefox(unittest.TestCase):

    __USERNAME = 'admin'
    __PASSWORD = 'admin'

    def setUp(self) -> None:
        self.firefox = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.firefox.maximize_window()

        self.firefox.implicitly_wait(2)

    def tearDown(self) -> None:
        self.firefox.quit()

    def test_auth(self):
        print("test")
        self.firefox.get(f"https://{self.__USERNAME}:{self.__PASSWORD}@the-internet.herokuapp.com/basic_auth")


