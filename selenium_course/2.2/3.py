from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    summ = num1 + num2

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(summ))

    browser.find_element(By.CLASS_NAME, "btn").click()
    
finally:
    time.sleep(5)
    browser.quit()    