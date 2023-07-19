from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from extracting_data import get_data
import pandas as pd
from time import sleep
import logging

option = Options()
option.add_argument("--disable-notifications")

logging.basicConfig(filename='bot_file.txt', filemode='w',level=logging.INFO, format= '%(asctime)s - %(levelname)s - %(message)s - %(lineno)d')

def webdriver_connection():
    try:
        service =   Service(executable_path = "/chromedriver")
        driver = webdriver.Chrome(options=option,service=service)
    except Exception as e:
        logging.critical(e)
    else:
        driver.maximize_window()
        return driver
    
def open_page(driver):
    website = "https://www.facebook.com/"
    try:
        driver.set_page_load_timeout(100)
        driver.implicitly_wait(50)
        driver.get(website)
    except Exception as e:
        logging.error(e)

def login():
    driver = webdriver_connection()
    open_page(driver)
    try:
        driver.implicitly_wait(20)
        email = driver.find_element(by='xpath',value='//*[@id="email"]')
        email.send_keys("muhammadtalhaasif5@gmail.com")
    except NoSuchElementException as e:
        logging.error(e)

    try:
        driver.implicitly_wait(20)
        password = driver.find_element(by='xpath',value='//*[@id="pass"]')
        password.send_keys("03204878756talha")
    except NoSuchElementException as e:
        logging.error(e)
        
    try:
        driver.implicitly_wait(20)
        login = driver.find_element(by='xpath',value='//button[@value = "1"]')
        login.click()
    except NoSuchElementException as e:
        logging.error(e)
    sleep(10)
    website = "https://www.facebook.com/groups/353719791773684/members"
    try:
        driver.set_page_load_timeout(100)
        driver.implicitly_wait(20)
        driver.get(website)
    except Exception as e:
        logging.error(e)

    
def saving_in_excel():
    df = get_data()
    df.to_excel('Profiles_Data.xlsx',index=False)

if __name__ == "__main__":
    login()
    saving_in_excel()