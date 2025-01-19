from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
from utils.add_product import wait_for_element
from dotenv import load_dotenv
from page.home import configHome

load_dotenv()

REGISTRATION_DATA = load_test_data("test_data.json")["registration"]
DEVICE = load_test_data("test_data.json")["device"]
APP_URL = "APP_URL"

WAIT_TIME = 20
LOGIN_SELECTOR = "_desktop_user_info"
CONTENT_SELECTOR = "#content > div > a"
SEND_BUTTON_SELECTOR = "//*[@id='customer-form']/footer/button"
REG_DATA_SELECTOR = "//*[@id='_desktop_user_info']/div/a[2]/span"


def test_main1(driver):

    configHome(driver, url=APP_URL, device=DEVICE["desktop"])
    
    wait_for_element(driver, By.ID, LOGIN_SELECTOR, WAIT_TIME)
    driver.find_element(By.ID, LOGIN_SELECTOR).click()
    
    wait_for_element(driver, By.CSS_SELECTOR, CONTENT_SELECTOR, WAIT_TIME)
    driver.find_element(By.CSS_SELECTOR, CONTENT_SELECTOR).click()

    wait_for_element(driver, By.XPATH, SEND_BUTTON_SELECTOR, WAIT_TIME)

    # Act: Completar el formulario de registro
    driver.find_element(By.NAME, "firstname").send_keys(REGISTRATION_DATA["firstname"])
    driver.find_element(By.NAME, "lastname").send_keys(REGISTRATION_DATA["lastname"])
    driver.find_element(By.NAME, "email").send_keys(REGISTRATION_DATA["email"])
    driver.find_element(By.NAME, "password").send_keys(REGISTRATION_DATA["password"])
    driver.find_element(By.NAME, "psgdpr").click()
    driver.find_element(By.NAME, "customer_privacy").click()
    driver.find_element(By.XPATH, SEND_BUTTON_SELECTOR).click()
    
    wait_for_element(driver, By.XPATH, REG_DATA_SELECTOR, WAIT_TIME)

   # Asserts
    expectedText = "Sign In"
    logOut = driver.find_element(By.XPATH,"//*[@id='_desktop_user_info']/div/a[1]")
    assert expectedText != logOut.text, \
    f"Expected success message not displayed. Actual message: {logOut.text}"

    expectedName = f"{REGISTRATION_DATA['firstname']} {REGISTRATION_DATA['lastname']}"
    userData = driver.find_element(By.XPATH, REG_DATA_SELECTOR)
    assert userData.text == expectedName, \
    f"Expected success message not displayed. Actual message: {userData.text}"

    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)


