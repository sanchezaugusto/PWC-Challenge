import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.add_product import wait_for_element
from utils.add_product import wait_for_element_to_be_visible_and_clickable
import time
from dotenv import load_dotenv
from utils.test_data_loader import load_test_data
from page.home import configHome
from utils.custom_assertion import assert_resolution

load_dotenv()

CHECKOUT_DATA = load_test_data("test_data.json")["checkout"]
DEVICE = load_test_data("test_data.json")["device"]
APP_URL = "APP_URL"
WAIT_TIME = 20
PRODUCT_XPATH = "//*[@id='content']/section[1]/div/div[1]/article/div/div[1]/a/picture/img"
ADD_TO_CART_XPATH = "//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button"
CHECKOUT_BUTTON_XPATH = "//*[@id='blockcart-modal']/div/div/div[2]/div/div[2]/div/div/a"
CHECKOUT_BUTTON2_XPATH = "//*[@id='main']/div/div[2]/div[1]/div[2]/div/a"
ADDRESS_ID = "field-address1"
FIELD_ID = "field-postcode"
CITY_ID = "field-city"
STATE_ID = "field-id_state"

def test_main3(driver):
    configHome(driver,url="APP_URL", device = DEVICE["desktop"])

    wait_for_element(driver, By.XPATH, PRODUCT_XPATH, WAIT_TIME)
    product1 = driver.find_element(By.XPATH, "//*[@id='content']/section[1]/div/div[1]/article/div/div[1]/a/picture/img")
    product1.click()

    wait_for_element_to_be_visible_and_clickable(driver, By.XPATH, ADD_TO_CART_XPATH, WAIT_TIME)
    addtocartButton = driver.find_element(By.XPATH, ADD_TO_CART_XPATH)
    addtocartButton.click()

    wait_for_element_to_be_visible_and_clickable(driver, By.XPATH, CHECKOUT_BUTTON_XPATH, WAIT_TIME)
    checkoutButton = driver.find_element(By.XPATH, "//*[@id='blockcart-modal']/div/div/div[2]/div/div[2]/div/div/a")
    checkoutButton.click()

    wait_for_element_to_be_visible_and_clickable(driver, By.XPATH, CHECKOUT_BUTTON2_XPATH, WAIT_TIME)
    checkoutButton2 = driver.find_element(By.XPATH, CHECKOUT_BUTTON2_XPATH)
    checkoutButton2.click()

    wait_for_element(driver, By.ID, ADDRESS_ID, WAIT_TIME)
    
    addressBox = driver.find_element(By.ID, ADDRESS_ID)
    postcodeBox = driver.find_element(By.ID, FIELD_ID)
    cityBox = driver.find_element(By.ID, CITY_ID)

    addressBox.send_keys(CHECKOUT_DATA["address"])
    postcodeBox.send_keys(CHECKOUT_DATA["postcode"])
    cityBox.send_keys(CHECKOUT_DATA["city"])

    wait_for_element(driver, By.ID, STATE_ID, WAIT_TIME)
    stateBox = driver.find_element(By.ID, STATE_ID)
    select = Select(stateBox)
    select.select_by_value(CHECKOUT_DATA["state_value"])
    deliveryButton = driver.find_element(By.XPATH, "//*[@id='delivery-address']/div/footer/button")
    deliveryButton.click()

    wait_for_element_to_be_visible_and_clickable(driver, By.XPATH, "//*[@id='js-delivery']/button", WAIT_TIME)

    continueButton2 = driver.find_element(By.XPATH, "//*[@id='js-delivery']/button")
    continueButton2.click()

    wait_for_element_to_be_visible_and_clickable(driver, By.ID, "conditions-to-approve", WAIT_TIME)
    payment1Button = driver.find_element(By.XPATH, "//*[@id='conditions_to_approve[terms-and-conditions]']")
    payment1Button.click() 

    assert payment1Button.is_selected(), "El botón no se seleccionó después del clic."
    
    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)

