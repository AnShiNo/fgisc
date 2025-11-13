import time

from selenium import webdriver
from selenium.webdriver.common.by import By

username = "team1"
password = "00000000"

driver = webdriver.Chrome()

driver.get("https://ckefgisc-rpg.vercel.app/login")

username_input = driver.find_element(By.XPATH, "//input[@placeholder='Name']")
password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
print(username_input.get_attribute('type'))
print(password_input.get_attribute('type'))

username_input.send_keys(username)
password_input.send_keys(password)

submit_button = driver.find_element(By.TAG_NAME, "button")
print(submit_button.text)

submit_button.click()

time.sleep(3)

driver.quit()