import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
from utils.test_data_loader import load_test_data
from page.home_page import HomePage 
from utils.custom_assertion import assert_resolution

CHECKOUT_DATA = load_test_data("test_data.json")["checkout"]
DEVICE = load_test_data("test_data.json")["device"]
APP_URL = "APP_URL"
load_dotenv()

def test_main3(driver):
    driver, device = driver
    home_page = HomePage(driver)
    home_page.configHome(url=APP_URL, device=DEVICE[device])
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='content']/section[1]/div/div[1]/article/div/div[1]/a/picture/img")))
    product1 = driver.find_element(By.XPATH, "//*[@id='content']/section[1]/div/div[1]/article/div/div[1]/a/picture/img")
    product1.click()

    time.sleep(10)
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='quantity_wanted']")))
    quantityWanted = driver.find_element(By.XPATH, "//*[@id='quantity_wanted']")
    quantityWanted.send_keys("999")

    checkoutButton2 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-or-refresh']/div[1]")
    checkoutButton2.click()
    time.sleep(3)
    # The available purchase order quantity for this product is 300.
    expectedMessage = "There are not enough products in stock"
    userData = driver.find_element(By.XPATH, "//*[@id='product-availability']")
    f"Expected success message not displayed. Actual message: {userData.text}"