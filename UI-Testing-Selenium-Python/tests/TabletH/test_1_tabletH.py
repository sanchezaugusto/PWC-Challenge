# test_user_registration.py
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.test_data_loader import load_test_data
from dotenv import load_dotenv
from page.home import configHome

load_dotenv()

REGISTRATION_DATA = load_test_data("test_data.json")["registration"]
DEVICE = load_test_data("test_data.json")["device"]

def test_user_registration(driver):
    # Arrange: Navegar a la página de registro
    # driver.get(os.getenv("APP_URL"))

    # WebDriverWait(driver, 50).until(
    # EC.presence_of_element_located((By.XPATH, "//*[@id='framelive']")))

    # iframe = driver.find_element(By.ID, "framelive")
    # WebDriverWait(driver, 10).until(
    #     lambda d: iframe.is_displayed() and iframe.is_enabled()
    # )
   
    # driver.switch_to.frame(driver.find_element(By.ID, "framelive"))
    configHome(driver,url="APP_URL", device = DEVICE["tabletH"])
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
    driver.find_element(By.NAME, "email").send_keys(REGISTRATION_DATA["email"])
    driver.find_element(By.NAME, "password").send_keys(REGISTRATION_DATA["password"])
    driver.find_element(By.NAME, "psgdpr").click()      #acepta condicion
    driver.find_element(By.NAME, "customer_privacy").click()    #acepta condicion
    driver.find_element(By.XPATH, "//*[@id='customer-form']/footer/button").click()  #envia formulario
    time.sleep(5)

   # Assert
    expectedText = "Sign In"
    logOut = driver.find_element(By.XPATH,"//*[@id='_desktop_user_info']/div/a[1]")
    assert expectedText != logOut.text, \
    f"Expected success message not displayed. Actual message: {logOut.text}"

    expectedName = f"{REGISTRATION_DATA['firstname']} {REGISTRATION_DATA['lastname']}"
    userData = driver.find_element(By.XPATH, "//*[@id='_desktop_user_info']/div/a[2]/span")
    assert userData.text == expectedName, \
    f"Expected success message not displayed. Actual message: {userData.text}"
