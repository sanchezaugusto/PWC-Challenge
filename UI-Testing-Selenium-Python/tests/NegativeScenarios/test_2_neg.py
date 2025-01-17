import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from utils.test_data_loader import load_test_data
from page.home import configHome
from utils.custom_assertion import assert_resolution

CONTACTFORM_DATA = load_test_data("test_data.json")["contact_form"]
DEVICE = load_test_data("test_data.json")["device"]
load_dotenv()

def test_main2(driver):
    # Arrange: Navegar a la página de registro
    configHome(driver,url="APP_URL", device = DEVICE["desktop"])#llama a la funcion configHome el cual inicializa la pagina

    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "contact-link")))
    loginButton = driver.find_element(By.ID, "contact-link")
    loginButton.click()
    time.sleep(2)
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='file-upload']")))

    emailBox = driver.find_element(By.ID, "email")
    emailBox.send_keys("Perez123@mail.com")
    time.sleep(2)
    # attachmentBox = driver.find_element(By.XPATH, "//*[@id='file-upload']")
    # messageBox = driver.find_element(By.ID, "contactform-message")
    sendButton =driver.find_element(By.XPATH, "//*[@id='content']/section/form/footer/input[3]")

    # attachmentBox.send_keys(CONTACTFORM_DATA["attachment_path"])
    # messageBox.send_keys(CONTACTFORM_DATA["message"])
    sendButton.click()
    time.sleep(2)
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='content']/section/form/div/ul/li")))


    expectedMessage = "The message cannot be blank."
    userData = driver.find_element(By.XPATH, "//*[@id='content']/section/form/div/ul/li")
    assert userData.text == expectedMessage, \
    f"Expected success message not displayed. Actual message: {userData.text}"


    # success_message = driver.find_element(By.XPATH, "//*[@id='content']/section/form/div/ul/li")

    # assert success_message.text == "Your message has been successfully sent to our team.", \
    # f"Expected success message not displayed. Actual message: {success_message.text}"

    # expectedResolution = 'desktop'
    # assert_resolution(driver,expectedResolution)
