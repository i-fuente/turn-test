import selenium_driver
import time
import data_handler
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


def setup():
    global driver
    driver = selenium_driver.get_driver(data_handler.browser)
    return driver

def test_candidate_search():
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


    #search by name
    candidate_name : WebElement = driver.find_element(By.ID, 'candidateSearch_candidateName')
    candidate_name.send_keys(data_handler.first_name,' ',data_handler.last_name) 
    search_button : WebElement = driver.find_element(By.ID, 'btnSrch')
    search_button.click()
    download_file : WebElement = driver.find_element_by_partial_link_text('Download')
    download_file.click()

    time.sleep(6)

def teardown():
    driver.quit()


