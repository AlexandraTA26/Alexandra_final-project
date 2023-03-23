import time
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")
"""
Cum sa gandim un selector?
1. # cautare dupa id
2. . cautare dupa class

"""

chrome.find_element(By.CSS_SELECTOR,"#first-name").send_keys("Alexandra")
# am facut cautare dupa id
chrome.find_element(By.CSS_SELECTOR,"#last-name").send_keys("Alexandra")
time.sleep(3)
chrome.find_element(By.CSS_SELECTOR,"#last-name").clear()
time.sleep(3)
# am facut cautare dupa atribut valoare
chrome.find_element(By.CSS_SELECTOR,"input[placeholder='Enter last name']").send_keys("Voicu")
time.sleep(2)
# am facut cautare dupa clasa
lista_elemente = chrome.find_elements(By.CSS_SELECTOR,".form-control")
lista_elemente[2].send_keys("Tester")
text_label_last_name = chrome.find_element(By.CSS_SELECTOR,"strong > label[for='last-name']").text
assert text_label_last_name == "Last name",f"Error, Expected - Last name - , Actual {text_label_last_name}"
chrome.find_element(By.CSS_SELECTOR,"div.input-group>div:nth-of-type(2) input").click()
chrome.find_element(By.CSS_SELECTOR,"div.input-group>div:last-of-type input").click()
education_label = chrome.find_element(By.CSS_SELECTOR,"div.input-group>div:first-of-type label").text
assert education_label == "Highest level of education",f"Error, Expected:Highest level of education, Actual {education_label}"
college_education = chrome.find_element(By.CSS_SELECTOR,"div.input-group>div:nth-of-type(3)").text
assert college_education == "College",f"Error: Expected: College, Actual {college_education}"
chrome.find_element(By.CSS_SELECTOR,"div.form-group > div:nth-of-type(2) > strong + input").send_keys("follwing sibling")
time.sleep(1)
chrome.quit()
