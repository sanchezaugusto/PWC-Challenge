from selenium.webdriver.common.by import By
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
import time
from dotenv import load_dotenv
from page.home_page import HomePage

load_dotenv()

REGISTRATION_DATA = load_test_data("test_data.json")["registration"]
DEVICE = load_test_data("test_data.json")["device"]
APP_URL = "APP_URL"
MESSAGE_ID = "blockEmailSubscription_displayFooterBefore"
MESSAGE_CSS = "p.alert.alert-success"

def test_main7(driver):
    # Arrange
    driver, device = driver
    home_page = HomePage(driver)
    home_page.configHome(url=APP_URL, device=DEVICE[device])

    # Act
    home_page.sign_up_newsletter(REGISTRATION_DATA["email"])

    # Assert  
    home_page.wait_for_newsletter_message()
    success_message = driver.find_element(By.ID, MESSAGE_ID)
    assert "You have successfully subscribed to this newsletter." in success_message.text, \
        f"Expected success message not displayed. Actual message: {success_message.text}"
    
    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)

