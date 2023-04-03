import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

class Search(unittest.TestCase):

    Prestashop_search_our_catalog_button = (By.XPATH,'//input[@placeholder="Search our catalog" ] ')
    sorting_dropdown = (By.XPATH, '//*[@class="btn-unstyle select-title"]')
    Search_rezults = (By.XPATH,'//span[@class="price"]')
    dropdown_option = (By.XPATH,"// a[contains(text(), 'Price, low to high')]")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.chrome.maximize_window()
        self.chrome.get("https://prestashop-ta26.multibit.ro/en/")
        self.chrome.implicitly_wait(2)

    def tearDown(self) -> None:
        self.chrome.quit()



    def test_check_sort_by_price(self):
        self.chrome.find_element(*self.Prestashop_search_our_catalog_button).send_keys("fox")
        time.sleep(2)
        self.chrome.find_element(*self.Prestashop_search_our_catalog_button).send_keys(Keys.ENTER)
        time.sleep(2)
        self.chrome.find_element(*self.sorting_dropdown).click()
        self.chrome.find_element(*self.dropdown_option).click()
        time.sleep(1)
        price_list = self.chrome.find_elements(*self.Search_rezults)
        sorted = True
        for i in range (len(price_list)):
            for j in range(i + 1, len(price_list)):
                if float(price_list[i].text.replace("lei", "")) > float(price_list[j].text.replace("lei", "")):
                    sorted = False

        assert sorted == True, "Error sorting by price did not work"




