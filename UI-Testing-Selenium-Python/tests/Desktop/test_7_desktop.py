import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.test_data_loader import load_test_data
from page.home import configHome
import time
from dotenv import load_dotenv
from utils.custom_assertion import assert_resolution
from utils.add_product import wait_for_element
from utils.add_product import click_element

load_dotenv()

REGISTRATION_DATA = load_test_data("test_data.json")["registration"]
DEVICE = load_test_data("test_data.json")["device"]
APP_URL = "APP_URL"
WAIT_TIME = 20
CONTACT_US_ID = "contact-link"
EMAIL_BOX_XPATH = "//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/div/div[1]/div[1]/input"
SUSCRIBE_BUTTON_XPATH = "//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/div/div[1]/input[1]"

def test_main7(driver):
    configHome(driver,url="APP_URL", device = DEVICE["desktop"])

    # WebDriverWait(driver, 20).until(
    # EC.presence_of_element_located((By.ID, "contact-link")))
    wait_for_element(driver, By.ID, CONTACT_US_ID, WAIT_TIME)
    contactUs = driver.find_element(By.ID, CONTACT_US_ID)
    contactUs.click()

    wait_for_element(driver, By.XPATH, EMAIL_BOX_XPATH, WAIT_TIME)
    emailboxA = driver.find_element(By.XPATH, EMAIL_BOX_XPATH)
    emailboxA.send_keys(REGISTRATION_DATA["email"])
    click_element(driver, By.XPATH, SUSCRIBE_BUTTON_XPATH)
    # suscribeButton = driver.find_element(By.XPATH,"//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/div/div[1]/input[1]")
    # suscribeButton.click()


    # WebDriverWait(driver, 10).until(
    # EC.presence_of_element_located((By.XPATH, "//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/p")))
    wait_for_element(driver, By.XPATH, "//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/p", WAIT_TIME)
    success_message = driver.find_element(By.XPATH, "//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/p")
    assert success_message.text == "You have successfully subscribed to this newsletter.", \
        f"Expected success message not displayed. Actual message: {success_message.text}"
    
    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)

    
    time.sleep(5)
    driver.quit()

