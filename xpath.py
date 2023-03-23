import time

import form as form
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")

#1. Cautare dupa atribut = valoare pentru un tag specific
chrome.find_element(By.XPATH,"//input[@placeholder='Enter first name']").send_keys("Alexandra")
# 1. Cautare dupa atribut = valoare indiferent de tag
chrome.find_element(By.XPATH,"//*[@placeholder='Enter last name']").send_keys("Voicu")
# 3. Cautare dupa copil prin navigare in jos
chrome.find_element(By.XPATH,"//div[@class='form-group']/div[3]/input").send_keys("Tester")
chrome.find_element(By.XPATH,"//div[@class='input-group'][2]/div[2]/input").click()
chrome.find_element(By.XPATH,"//input[@placeholder='Enter first name']").clear()
chrome.find_element(By.XPATH,"//*[@placeholder='Enter last name']").clear()

# 4. Cautare cu OR - Ambele conditii sunt adevarate
chrome.find_element(By.XPATH,"//input[@placeholder='Enter first name'] | //*[@placeholder='Enter last name']").send_keys("Cautare cu OR")

# 5. Cautare cu OR - Doar a doua conditie este adevarata
chrome.find_element(By.XPATH,"//input[@placeholder='Enter first name'] | //*[@placeholder='Enter last names']").send_keys("Cautare cu OR")

# 6. Cautare cu OR - Nici o conditie nu este adevarata
chrome.find_element(By.XPATH,"//input[@placeholder='Enter first names'] | //*[@placeholder='Enter last name']").send_keys("Cautare cu OR")

# 7. Tratare dropdown
years_of_experience= Select(chrome.find_element(By.XPATH,"//*[@id='select-menu']"))
time.sleep(2)
years_of_experience.select_by_visible_text("5-9")
time.sleep(2)
years_of_experience.select_by_visible_text("10+")
time.sleep(2)

"""
x y axis navigation
1. Navigare din parinte in copil se face cu caracterul /
2. Navigare catre un urmas care nu e urmas direct se face cu caracterul //
3. Navigarea in sus catre parent se poate face cu "/parent::tag"
4. Putem sa navigam la urmatorul frate cu "/following-sibling::tag"
5. Putem sa navigam la fratele anterior cu "/proceding-sibiling::tag"

# //@form/div/div/following-sibling::div[4]/proceding-sibiling::div[3]
# //a[text()='Submit']
# //a[@role='button'

"""

time.sleep(2)
chrome.quit()
# //div[@clasa='input-group'][2]/div[2]/input
# //*[@id='checkbox-1']
#//div[@class='input-group']/folowing-sibling::div/div[2]/input
