import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())
time.sleep(2)
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/")
time.sleep(2)
chrome.find_element(By.PARTIAL_LINK_TEXT, "Authentication").click()
chrome.quit()
