from selenium.webdriver.common.by import By
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
from page.base_page import BasePage
import time
from dotenv import load_dotenv

from page.home_page import HomePage

load_dotenv()

REGISTRATION_DATA = load_test_data("test_data.json")["registration"]
DEVICE = load_test_data("test_data.json")["device"]
APP_URL = "APP_URL"
WAIT_TIME = 20
CONTACT_US_ID = "contact-link"
EMAIL_BOX_NAME = "email"
SUSCRIBE_BUTTON_XPATH = "//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/div/div[1]/input[1]"
SUSCRIBE_BUTTON_NAME= "submitNewsletter"
MESSAGE_ID = "blockEmailSubscription_displayFooterBefore"
#MESSAGE_XPATH = "//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form"
#MESSAGE_XPATH = "//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/div/div[2]/p[2]"
#//*[@id="blockEmailSubscription_displayFooterBefore"]/div/div/form/div/div[2]/p[2]
#//*[@id="blockEmailSubscription_displayFooterBefore"]/div/div/form/p

def test_sign_up_newsletter(driver):
    driver, device = driver
    home_page = HomePage(driver)
    # base_page_obj = BasePage(driver)
    
    # Arrange
    home_page.configHome(url=APP_URL, device=DEVICE[device])

    # Act
    home_page.wait_for_element(By.ID, CONTACT_US_ID)
    home_page.sign_up_newsletter(REGISTRATION_DATA["email"])

    # Assert  
    time.sleep(2)
    #base_page_obj.wait_for_text_to_be_present_in_element(By.ID, MESSAGE_ID)
    success_message = driver.find_element(By.ID, MESSAGE_ID)
    assert "You have successfully subscribed to this newsletter." in success_message.text, \
        f"Expected success message not displayed. Actual message: {success_message.text}"
    
    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)

