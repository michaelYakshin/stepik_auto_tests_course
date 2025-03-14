from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.ID, "input_value").text
    x = calc(x_element)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(x)
    submit = browser.find_element(By.CLASS_NAME, "btn")
    submit.click()
    alert = browser.switch_to.alert
    alert_text = alert.text

    split_alert = alert_text.split(": ")
    number = split_alert[-1]
    print(number)


finally:
   browser.quit()