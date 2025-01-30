# test_user_registration.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
from dotenv import load_dotenv
#from page.home import configHome

from page.home_page import HomePage 

load_dotenv()

REGISTRATION_DATA = load_test_data("test_data.json")["registration"]
DEVICE = load_test_data("test_data.json")["device"]
APP_URL = "APP_URL"

def test_user_registration(driver):
    driver, device = driver
    home_page = HomePage(driver)
    home_page.configHome(url=APP_URL, device=DEVICE[device])
    
    WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.ID, "_desktop_user_info")))

    driver.find_element(By.ID, "_desktop_user_info").click()
    
    WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#content > div > a")))
    driver.find_element(By.CSS_SELECTOR, "#content > div > a").click()

    WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='customer-form']/footer/button")))

    # Act: Completar el formulario de registro
    driver.find_element(By.NAME, "firstname").send_keys(REGISTRATION_DATA["firstname"])
    driver.find_element(By.NAME, "lastname").send_keys(REGISTRATION_DATA["lastname"])
    driver.find_element(By.NAME, "email").send_keys("wrong@mail")
    driver.find_element(By.NAME, "password").send_keys(REGISTRATION_DATA["password"])
    driver.find_element(By.NAME, "psgdpr").click()      #acepta condicion
    driver.find_element(By.NAME, "customer_privacy").click()    #acepta condicion
    driver.find_element(By.XPATH, "//*[@id='customer-form']/footer/button").click()  #envia formulario
    

    WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='customer-form']/div/div[4]/div[1]/div/ul/li")))
    # Invalid format.

    expectedMessage = "Invalid format."
    userData = driver.find_element(By.XPATH, "//*[@id='customer-form']/div/div[4]/div[1]/div/ul/li")
    assert userData.text == expectedMessage, \
    f"Expected success message not displayed. Actual message: {userData.text}"

