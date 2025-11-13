import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title
print("title =", title)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

time.sleep(3)

text_box.send_keys("Selenium")

time.sleep(3)

submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text
print("text =", text)
#等三秒
time.sleep(3)
#退出
driver.quit()