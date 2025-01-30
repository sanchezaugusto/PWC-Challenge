from selenium.webdriver.common.by import By
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
from dotenv import load_dotenv
from page.account_page import AccountPage
from page.home_page import HomePage

load_dotenv()

REGISTRATION_DATA = load_test_data("test_data.json")["registration"]
DEVICE = load_test_data("test_data.json")["device"]
REG_DATA_XPATH = "//*[@id='_desktop_user_info']/div/a[2]/span"

def test_main1(driver):
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
                                REGISTRATION_DATA["email"], 
                                REGISTRATION_DATA["password"])
    
   # Asserts
    home_page.wait_for_user_info()
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


