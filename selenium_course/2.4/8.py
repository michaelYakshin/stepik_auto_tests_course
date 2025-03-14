from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    wait = WebDriverWait(browser, 12)
    is_price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book_btn = browser.find_element(By.ID, "book")

    while True:
        if is_price:
            book_btn.click()
            break

    x_element = browser.find_element(By.ID, "input_value").text
    x = calc(x_element)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(x)

    submit_btn = browser.find_element(By.ID, "solve")
    submit_btn.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    substr = alert_text.split(": ")
    number = substr[-1]
    print(number)
    

finally:
    browser.quit()