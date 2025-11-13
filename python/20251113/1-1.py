from selenium import webdriver
import time

driver = webdriver.Chrome()

# 打開網頁
driver.get("https://youtu.be/OzOrqWGurlI?si=LzR4LY8TdXyQ3kdg")

# 等待 30 秒
time.sleep(30)

# 關閉瀏覽器
driver.quit()