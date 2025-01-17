import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from dotenv import load_dotenv
from utils.test_data_loader import load_test_data
from page.home import configHome

CHECKOUT_DATA = load_test_data("test_data.json")["checkout"]
DEVICE = load_test_data("test_data.json")["device"]
load_dotenv()

def test_main3(driver):
    configHome(driver,url="APP_URL", device = DEVICE["tabletV"])
    product1 = driver.find_element(By.XPATH, "//*[@id='content']/section[1]/div/div[1]/article/div/div[1]/a/picture/img")
    product1.click()

    time.sleep(3)
    addtocartButton = driver.find_element(By.XPATH, "//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button")
    addtocartButton.click()

    time.sleep(3)
    checkoutButton = driver.find_element(By.XPATH, "//*[@id='blockcart-modal']/div/div/div[2]/div/div[2]/div/div/a")
    checkoutButton.click()
    time.sleep(3)
    checkoutButton2 = driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div[1]/div[2]/div/a")
    checkoutButton2.click()

    time.sleep(3)
    addressBox = driver.find_element(By.ID, "field-address1")
    postcodeBox = driver.find_element(By.ID, "field-postcode")
    cityBox = driver.find_element(By.ID, "field-city")

    addressBox.send_keys(CHECKOUT_DATA["address"])
    postcodeBox.send_keys(CHECKOUT_DATA["postcode"])
    cityBox.send_keys(CHECKOUT_DATA["city"])

    time.sleep(1)
    stateBox = driver.find_element(By.ID, "field-id_state")
    select = Select(stateBox)
    select.select_by_value(CHECKOUT_DATA["state_value"])
    time.sleep(1)

    deliveryButton = driver.find_element(By.XPATH, "//*[@id='delivery-address']/div/footer/button")
    deliveryButton.click()
    time.sleep(1)
    #DELIVERY
    continueButton2 = driver.find_element(By.XPATH, "//*[@id='js-delivery']/button")
    continueButton2.click()
    time.sleep(1)
    # payment1Button = driver.find_element(By.ID, "payment-option-1")
    # payment1Button.click()

    #CONDITIONS
    payment1Button = driver.find_element(By.XPATH, "//*[@id='conditions_to_approve[terms-and-conditions]']")
    payment1Button.click() #//*[@id="conditions_to_approve[terms-and-conditions]"]
    time.sleep(3)
    #REVISAR!    
    # placeorderButton = driver.find_element(By.XPATH, "//*[@id='payment-confirmation']/div[1]/button")
    # placeorderButton.click()
    # time.sleep(6)

    # homeButton =driver.find_element(By.XPATH, "//*[@id='_desktop_logo']/a/img")
    # homeButton.click()
    # time.sleep(3)