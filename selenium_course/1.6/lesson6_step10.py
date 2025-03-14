from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elements1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group:nth-child(1) input").send_keys('а')
    elements2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group:nth-child(2) input").send_keys('а')
    elements3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group:nth-child(3) input").send_keys('а')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()