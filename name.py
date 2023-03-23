import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())
chrome.get("https://www.seleniumframework.com/Practiceform/")
chrome.find_element(By.NAME,"name").send_keys("Alexandra")
chrome.find_element(By.NAME,"email").send_keys("alexandra.iuganu@gmail.com")
chrome.find_element(By.NAME,"country").send_keys("Romania")
chrome.find_element(By.NAME,"company").send_keys("itfactory")
