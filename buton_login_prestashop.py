import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())
chrome.get("https://prestashop-ta26.multibit.ro/en/login?back=my-account")

chrome.find_element(By.XPATH,'//button[@class="btn btn-primary" and @data-link-action="sign-in"]').click()
time.sleep(2)
chrome.quit()