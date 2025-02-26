import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from utils.test_data_loader import load_test_data
from page.home_page import HomePage 
from page.contact_page import ContactPage
from utils.custom_assertion import assert_resolution

CONTACTFORM_DATA = load_test_data("test_data.json")["contact_form"]
DEVICE = load_test_data("test_data.json")["device"]
load_dotenv()

def test_main2(driver):
    # Arrange
    driver, device = driver
    contact_page = ContactPage(driver)
    home_page = HomePage(driver)
    home_page.configHome(DEVICE[device])

    # Act
    home_page.click_on_contact_us()
    time.sleep(2)
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='file-upload']")))

    emailBox = driver.find_element(By.ID, "email")
    emailBox.send_keys("Perez123@mail.com")
    time.sleep(2)

    sendButton =driver.find_element(By.XPATH, "//*[@id='content']/section/form/footer/input[3]")

    sendButton.click()
    time.sleep(2)
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='content']/section/form/div/ul/li")))


    expectedMessage = "The message cannot be blank."
    userData = driver.find_element(By.XPATH, "//*[@id='content']/section/form/div/ul/li")
    assert userData.text == expectedMessage, \
    f"Expected success message not displayed. Actual message: {userData.text}"
