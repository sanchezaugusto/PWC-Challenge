from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution

from dotenv import load_dotenv

from page.account_page import AccountPage
from page.home_page import HomePage

load_dotenv()

REGISTRATION_DATA = load_test_data("test_data.json")["registration"]
DEVICE = load_test_data("test_data.json")["device"]
APP_URL = "APP_URL"
REGISTER_LINK_TEXT = "No account? Create one here"
SEND_BUTTON_SELECTOR = "//*[@id='customer-form']/footer/button"
REG_DATA_XPATH = "//*[@id='_desktop_user_info']/div/a[2]/span"


def test_main1(driver):
    driver, device = driver
    home_page = HomePage(driver)
    account_page = AccountPage(driver)

    # Arrange   
    home_page.configHome(APP_URL, DEVICE[device])
    home_page.wait_for_element( By.PARTIAL_LINK_TEXT, "Sign in")
    driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in").click()

    # Act
    home_page.wait_for_element(By.LINK_TEXT, REGISTER_LINK_TEXT)
    driver.find_element(By.LINK_TEXT, REGISTER_LINK_TEXT).click()

    home_page.wait_for_element(By.XPATH, SEND_BUTTON_SELECTOR)
    account_page.create_account(REGISTRATION_DATA["firstname"], REGISTRATION_DATA["lastname"], REGISTRATION_DATA["email"], REGISTRATION_DATA["password"])
    
   # Asserts
    home_page.wait_for_element( By.XPATH, REG_DATA_XPATH)
    expectedText = "Sign In"
    logOut = driver.find_element(By.XPATH,"//*[@id='_desktop_user_info']/div/a[1]")
    assert expectedText != logOut.text, \
    f"Expected success message not displayed. Actual message: {logOut.text}"

    expectedName = f"{REGISTRATION_DATA['firstname']} {REGISTRATION_DATA['lastname']}"
    userData = driver.find_element(By.XPATH, REG_DATA_XPATH)
    assert userData.text == expectedName, \
    f"Expected success message not displayed. Actual message: {userData.text}"

    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)


