from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_presence_button_cart(browser):
    browser.get(link)
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@class='col-sm-6 product_main']")
                                       ))
    try:
        browser.find_element_by_xpath("//*[@class='btn btn-lg btn-primary btn-add-to-basket']")
        result = True

    except:
        result = False
    assert result == True, "The add to basket button not found"
