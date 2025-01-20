from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
from utils.product_interactions import wait_for_element
from page.home import configHome
from dotenv import load_dotenv

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
    configHome(driver,url=APP_URL, device = DEVICE["desktop"])

    wait_for_element(driver, By.ID, CONTACT_US_ID, WAIT_TIME)
    login_button = driver.find_element(By.ID, CONTACT_US_ID)
    login_button.click()

    wait_for_element(driver, By.ID, FILE_UPLOAD_ID, WAIT_TIME)

    email_box = driver.find_element(By.ID, EMAIL_ID)
    attachment_box = driver.find_element(By.ID, FILE_UPLOAD_ID)
    message_box = driver.find_element(By.ID, MESSAGE_BOX_ID)
    send_button = driver.find_element(By.NAME, SEND_BUTTON_NAME)

    attachment_box.send_keys(CONTACTFORM_DATA["attachment_path"])
    message_box.send_keys(CONTACTFORM_DATA["message"])
    email_box.clear()
    email_box.send_keys(CONTACTFORM_DATA["email"])
    send_button.click()

    wait_for_element(driver, By.XPATH, SUCCESS_MESSAGE_XPATH, WAIT_TIME)
    success_message = driver.find_element(By.XPATH, SUCCESS_MESSAGE_XPATH)

    assert success_message.text == "Your message has been successfully sent to our team.", \
    f"Expected success message not displayed. Actual message: {success_message.text}"

    expected_resolution = 'desktop'
    assert_resolution(driver,expected_resolution)