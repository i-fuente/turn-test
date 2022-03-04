from selenium import webdriver



def get_driver(browser):
    if browser == 'chrome':
        driver_path = './drivers/chromedriver'
        driver = webdriver.Chrome(executable_path=driver_path)
    elif browser == 'firefox':
        driver_path = './drivers/geckodriver'
        driver = webdriver.Firefox(executable_path=driver_path)  
    else: 
        raise RuntimeError ('No existe el driver del navegador indicado')
    return driver