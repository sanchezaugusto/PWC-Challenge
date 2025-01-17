import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from utils.test_data_loader import load_test_data
from page.home import configHome


CONTACTFORM_DATA = load_test_data("test_data.json")["contact_form"]
DEVICE = load_test_data("test_data.json")["device"]
load_dotenv()

def test_main2(driver):
        # Arrange: Navegar a la página de registro
    configHome(driver,url="APP_URL", device = DEVICE["tabletH"])#llama a la funcion configHome el cual inicializa la pagina

    loginButton = driver.find_element(By.ID, "contact-link")
    loginButton.click()
    #time.sleep(3)
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='file-upload']")))

    # emailBox = driver.find_element(By.ID, "email")
    # emailBox.send_keys("Perez123@mail.com")

    attachmentBox = driver.find_element(By.XPATH, "//*[@id='file-upload']")
    messageBox = driver.find_element(By.ID, "contactform-message")
    sendButton =driver.find_element(By.XPATH, "//*[@id='content']/section/form/footer/input[3]")

    attachmentBox.send_keys(CONTACTFORM_DATA["attachment_path"])
    messageBox.send_keys(CONTACTFORM_DATA["message"])
    sendButton.click()
    #time.sleep(3)
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='content']/section/form/div/ul/li")))
    success_message = driver.find_element(By.XPATH, "//*[@id='content']/section/form/div/ul/li")

    assert success_message.text == "Your message has been successfully sent to our team.", \
    f"Expected success message not displayed. Actual message: {success_message.text}"

    # homeButton =driver.find_element(By.XPATH, "//*[@id='_desktop_logo']/a/img")
    # homeButton.click()
