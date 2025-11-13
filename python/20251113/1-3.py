from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://suzy12121.github.io/webscrape-sample/")

elements = driver.find_elements(By.TAG_NAME, 'p')

for paragraph, e in enumerate(elements):
    print(f"In paragraph {paragraph}:")
    print(e.text)
    
images = driver.find_elements(By.TAG_NAME, 'img')

for i, image in enumerate(images):
    print(f"Image {i} at {image.get_attribute('src')}")

driver.quit()

