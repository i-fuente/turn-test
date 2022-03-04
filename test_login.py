from turtle import clear
from typing import ItemsView
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
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
    #login
    url = 'https://opensource-demo.orangehrmlive.com'
    driver.get(url) 
    driver.maximize_window()
    user_name : WebElement = driver.find_element(By.ID, 'txtUsername')
    user_name.send_keys('Admin')
    user_pass : WebElement = driver.find_element(By.ID, 'txtPassword')
    user_pass.send_keys('admin123')
    login_button : WebElement = driver.find_element(By.ID, 'btnLogin')
    login_button.click()
    
    #recrutement menu
    action = ActionChains(driver)

    firstLevelMenu = driver.find_element_by_id("mainMenuFirstLevelUnorderedList")
    action.move_to_element(firstLevelMenu).perform()
    secondLevelMenu = driver.find_element_by_id("menu_recruitment_viewRecruitmentModule")
    action.move_to_element(secondLevelMenu).perform()
    secondLevelMenu.click()

    #new candidate
    add_button : WebElement = driver.find_element(By.ID, 'btnAdd')
    add_button.click()
    first_name : WebElement = driver.find_element(By.ID, 'addCandidate_firstName')
    first_name.send_keys('Ivan')
    last_name : WebElement = driver.find_element(By.ID, 'addCandidate_lastName')
    last_name.send_keys('de la fuente')
    e_mail : WebElement = driver.find_element(By.ID, 'addCandidate_email')
    e_mail.send_keys('ivan.test@test.com')
    contact_number : WebElement = driver.find_element(By.ID, 'addCandidate_contactNo')
    contact_number.send_keys('3322556677')
    candidate_vacancy = Select(driver.find_element(By.ID, 'addCandidate_vacancy'))
    candidate_vacancy.select_by_visible_text('Senior QA Lead')
    candidate_resume : WebElement = driver.find_element(By.ID, 'addCandidate_resume')
    #candidate_resume.send_keys('3322556677')
    candidate_keyWords : WebElement = driver.find_element(By.ID, 'addCandidate_keyWords')
    candidate_keyWords.send_keys('Jira, python, SQL')
    candidate_comment : WebElement = driver.find_element(By.ID, 'addCandidate_comment')
    candidate_comment.send_keys('Comment 1')
    candidate_appliedDate : WebElement = driver.find_element(By.ID, 'addCandidate_appliedDate')
    candidate_appliedDate.click()
    candidate_appliedDate.send_keys(Keys.COMMAND, "a")
    candidate_appliedDate.send_keys(Keys.BACKSPACE)
    candidate_appliedDate.send_keys('2022-03-02')
    candidate_appliedDate.send_keys(Keys.RETURN)
    candidate_consent : WebElement = driver.find_element(By.ID, 'addCandidate_consentToKeepData')
    candidate_consent.click()
    save_button : WebElement = driver.find_element(By.ID, 'btnSave')
    save_button.click()
    form_addcandidate : WebElement = driver.find_element(By.ID, 'frmAddCandidate')
    assert form_addcandidate.is_displayed() , 'Successfully Saved'




    
    time.sleep(6)

def teardown():
    driver.quit()