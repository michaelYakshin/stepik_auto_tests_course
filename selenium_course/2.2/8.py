from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    firstname.send_keys("Ivan")
    lastname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    lastname.send_keys("Ivanov")
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("ivanov@yandex.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")

    upload_file = browser.find_element(By.ID, "file")
    upload_file.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()