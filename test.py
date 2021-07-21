
from selenium import webdriver
import time
"""

def test_lambdatest_todo_app():
    chrome_driver = webdriver.Chrome()

    chrome_driver.get('https://to-3d.com/')

    chrome_driver.find_element_by_css_selector(".wp-block-button__link").click()

    title = "3D Models - Download 3D models free"
    assert title == chrome_driver.title

    chrome_driver.close()
    
    """


def test_lambdatest_todo_app():
    chrome_driver = webdriver.Chrome()

    chrome_driver.get('https://to-3d.com/')

    input_element = chrome_driver.find_element_by_css_selector('#subscribe-email input')
    input_element.send_keys("golub.togo@gmail.com")

    chrome_driver.find_element_by_css_selector("#subscribe-submit button").click()
    subscribed_text = chrome_driver.find_element_by_css_selector(".jetpack_subscription_widget p").text

    assert "You subscribed" in subscribed_text

    chrome_driver.close()

