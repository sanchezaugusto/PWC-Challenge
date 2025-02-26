import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
from dotenv import load_dotenv
from page.account_page import AccountPage
from page.home_page import HomePage 

load_dotenv()

REGISTRATION_DATA = load_test_data("test_data.json")["registration"]
DEVICE = load_test_data("test_data.json")["device"]

def test_user_registration(driver):
    # Arrange   
    driver, device = driver
    home_page = HomePage(driver)
    account_page = AccountPage(driver)
    home_page.configHome(DEVICE[device])

    # Act
    home_page.click_on_sign_in()
    home_page.click_on_register()
    account_page.create_account(REGISTRATION_DATA["firstname"],
                                REGISTRATION_DATA["lastname"],
                                REGISTRATION_DATA["wrong_email"], 
                                REGISTRATION_DATA["password"])
    

    WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='customer-form']/div/div[4]/div[1]/div/ul/li")))
    # Invalid format.

    expectedMessage = "Invalid format."
    userData = driver.find_element(By.XPATH, "//*[@id='customer-form']/div/div[4]/div[1]/div/ul/li")
    assert userData.text == expectedMessage, \
    f"Expected success message not displayed. Actual message: {userData.text}"

