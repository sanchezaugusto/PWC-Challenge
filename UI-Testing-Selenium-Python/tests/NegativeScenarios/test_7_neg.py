import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.test_data_loader import load_test_data
from page.home_page import HomePage 
import time
from dotenv import load_dotenv
from utils.custom_assertion import assert_resolution

load_dotenv()

DEVICE = load_test_data("test_data.json")["device"]
APP_URL = "APP_URL"

def test_main7(driver):
    driver, device = driver
    home_page = HomePage(driver)
    home_page.configHome(url=APP_URL, device=DEVICE[device])

    WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "contact-link")))
    contactUs = driver.find_element(By.ID, "contact-link")
    contactUs.click()

    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/div/div[1]/div[1]/input")))
    emailboxA = driver.find_element(By.XPATH,"//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/div/div[1]/div[1]/input")
    emailboxA.send_keys("wrong@mail")
    suscribeButton = driver.find_element(By.XPATH,"//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/div/div[1]/input[1]")
    suscribeButton.click()

    WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/p")))
    
    # Invalid format.

    expectedMessage = "Invalid email address."
    userData = driver.find_element(By.XPATH, "//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/p")
    assert userData.text == expectedMessage, \
    f"Expected success message not displayed. Actual message: {userData.text}"

