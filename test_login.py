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
import data_handler

driver : WebDriver = None

def setup():
    global driver
    browser = 'chrome'
    driver = selenium_driver.get_driver(browser)
    return driver

#def path():
#    path = "src/test/resources/testData/twt_Pic.jpg";
#    file = new File(new File(path).getAbsolutePath());

def test_login():
    #login
    driver.get(data_handler.url) 
    driver.maximize_window()
    user_name : WebElement = driver.find_element(By.ID, 'txtUsername')
    user_name.send_keys(data_handler.user_name)
    user_pass : WebElement = driver.find_element(By.ID, 'txtPassword')
    user_pass.send_keys(data_handler.user_pass)
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
    first_name.send_keys(data_handler.first_name)
    last_name : WebElement = driver.find_element(By.ID, 'addCandidate_lastName')
    last_name.send_keys(data_handler.last_name)
    e_mail : WebElement = driver.find_element(By.ID, 'addCandidate_email')
    e_mail.send_keys(data_handler.email)
    contact_number : WebElement = driver.find_element(By.ID, 'addCandidate_contactNo')
    contact_number.send_keys(data_handler.phone)
    candidate_vacancy = Select(driver.find_element(By.ID, 'addCandidate_vacancy'))
    candidate_vacancy.select_by_visible_text(data_handler.vacancy)
    candidate_resume : WebElement = driver.find_element(By.ID,'addCandidate_resume')
    candidate_resume.send_keys(data_handler.file_path)
    candidate_keyWords : WebElement = driver.find_element(By.ID, 'addCandidate_keyWords')
    candidate_keyWords.send_keys(data_handler.keywords)
    candidate_comment : WebElement = driver.find_element(By.ID, 'addCandidate_comment')
    candidate_comment.send_keys(data_handler.comments)
    candidate_appliedDate : WebElement = driver.find_element(By.ID, 'addCandidate_appliedDate')
    candidate_appliedDate.click()
    candidate_appliedDate.send_keys(Keys.COMMAND, "a")
    candidate_appliedDate.send_keys(Keys.BACKSPACE)
    candidate_appliedDate.send_keys(data_handler.date)
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