import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())
chrome.implicitly_wait(2)

time.sleep(2)
chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/form") # putem deschide un site
chrome.find_element(By.ID,"first-name" ).send_keys("Alexandra")
chrome.find_element(By.ID,"last-name" ).send_keys("Voicu")
time.sleep(2)
chrome.quit() # inchide toata instanta browserului
