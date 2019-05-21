from time import sleep
from splinter.browser import Browser
from splinter.driver.flaskclient import FlaskClient
from flask import Flask
import sys
sys.path.append('./')
from main import *

def test_home_page_header():

    browser = Browser('flask', app=app)

    browser.visit('http://127.0.0.1:5000/')
    assert browser.is_text_present("AJAK's first Flask app")

    browser.quit()

# def test_click_predict():
#
#     browser = Browser('flask', app=app)
#
#     browser.visit('http://localhost:5000/')
#     # browser.execute_script("document.getElementById('predictButton').click()")
#     browser.find_by_id('predictButton').click()
#     assert browser.is_text_present("Predicted Output")
#     browser.quit()
