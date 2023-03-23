from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())
