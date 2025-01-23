from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
from page.base_page import BasePage
import time
from dotenv import load_dotenv

from page.home_page import HomePage
from page.contact_page import ContactPage

load_dotenv()

CONTACTFORM_DATA = load_test_data("test_data.json")["contact_form"]
DEVICE = load_test_data("test_data.json")["device"]
APP_URL = "APP_URL"
WAIT_TIME = 20
CONTACT_US_ID = "contact-link"
FILE_UPLOAD_ID = "file-upload"
EMAIL_ID = "email"
MESSAGE_BOX_ID = "contactform-message"
SEND_BUTTON_NAME = "submitMessage"
SUCCESS_MESSAGE_XPATH = "//*[@id='content']/section/form/div/ul/li"

def test_main2(driver):
    driver, device = driver
    contact_page = ContactPage(driver)
    home_page = HomePage(driver)

    home_page.configHome(url=APP_URL, device=DEVICE[device])
    # Arrange
    home_page.wait_for_element( By.ID, CONTACT_US_ID)

    # Act
    login_button = driver.find_element(By.ID, CONTACT_US_ID)
    login_button.click()

    # home_page.wait_for_element(By.ID, FILE_UPLOAD_ID)
    # #contact_page.fill_contact_form(CONTACTFORM_DATA["email"], CONTACTFORM_DATA["attachment_path"], CONTACTFORM_DATA["message"])
    contact_page.fill_contact_form(CONTACTFORM_DATA["email"], CONTACTFORM_DATA["message"])
    
    # Assert
    home_page.wait_for_element(By.XPATH, SUCCESS_MESSAGE_XPATH)
    success_message = driver.find_element(By.XPATH, SUCCESS_MESSAGE_XPATH)

    assert success_message.text == "Your message has been successfully sent to our team.", \
    f"Expected success message not displayed. Actual message: {success_message.text}"

    expected_resolution = 'desktop'
    assert_resolution(driver,expected_resolution)