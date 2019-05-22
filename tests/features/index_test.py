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

def test_views_predict_button():

    browser = Browser('flask', app=app)

    browser.visit('http://127.0.0.1:5000/')
    assert browser.is_element_present_by_id("predictButton")

    browser.quit()

def test_views_clear_button():

    browser = Browser('flask', app=app)

    browser.visit('http://127.0.0.1:5000/')
    assert browser.is_element_present_by_id("clear-canvas")

    browser.quit()

def test_views_timer_present():

    browser = Browser('flask', app=app)

    browser.visit('http://127.0.0.1:5000/')
    assert browser.is_element_present_by_id("timer")
    assert browser.is_text_present("20")

    browser.quit()

def test_views_span_for_result_present():

    browser = Browser('flask', app=app)

    browser.visit('http://127.0.0.1:5000/')
    assert browser.is_element_present_by_id("result")

    browser.quit()
