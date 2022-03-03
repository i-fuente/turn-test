from typing import ItemsView
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import selenium_driver
import time

driver : WebDriver = None

def setup():
    global driver
    browser = 'chrome'
    driver = selenium_driver.get_driver(browser)
    return driver

def test_login():
    url = 'https://opensource-demo.orangehrmlive.com'
    driver.get(url) 
    driver.maximize_window()
    time.sleep(6)
    


def teardown():
    driver.quit()