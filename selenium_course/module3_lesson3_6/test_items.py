import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_the_basket_btn(browser):
    browser.get(link)
    time.sleep(5)
    is_basket_btn_presented = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(is_basket_btn_presented) > 0, "No 'add to basket' button"