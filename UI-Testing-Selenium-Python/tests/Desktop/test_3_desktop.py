import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
from utils.test_data_loader import load_test_data
from page.home import configHome
from utils.custom_assertion import assert_resolution

CHECKOUT_DATA = load_test_data("test_data.json")["checkout"]
DEVICE = load_test_data("test_data.json")["device"]
load_dotenv()

def test_main3(driver):
    configHome(driver,url="APP_URL", device = DEVICE["desktop"])
    product1 = driver.find_element(By.XPATH, "//*[@id='content']/section[1]/div/div[1]/article/div/div[1]/a/picture/img")
    product1.click()

    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button")))
    addtocartButton = driver.find_element(By.XPATH, "//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button")
    addtocartButton.click()

    # WebDriverWait(driver, 30).until(
    # EC.presence_of_element_located((By.XPATH, "//*[@id='blockcart-modal']/div/div/div[2]/div/div[2]/div/div")))
    time.sleep(2)
    checkoutButton = driver.find_element(By.XPATH, "//*[@id='blockcart-modal']/div/div/div[2]/div/div[2]/div/div/a")
    checkoutButton.click()

    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div/div[2]/div[1]/div[2]/div/a")))
    checkoutButton2 = driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div[1]/div[2]/div/a")
    checkoutButton2.click()

    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "field-address1")))
    
    addressBox = driver.find_element(By.ID, "field-address1")
    postcodeBox = driver.find_element(By.ID, "field-postcode")
    cityBox = driver.find_element(By.ID, "field-city")

    addressBox.send_keys(CHECKOUT_DATA["address"])
    postcodeBox.send_keys(CHECKOUT_DATA["postcode"])
    cityBox.send_keys(CHECKOUT_DATA["city"])

    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "field-id_state")))
    stateBox = driver.find_element(By.ID, "field-id_state")
    select = Select(stateBox)
    select.select_by_value(CHECKOUT_DATA["state_value"])
    deliveryButton = driver.find_element(By.XPATH, "//*[@id='delivery-address']/div/footer/button")
    deliveryButton.click()

    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='js-delivery']/button")))
    #DELIVERY
    continueButton2 = driver.find_element(By.XPATH, "//*[@id='js-delivery']/button")
    continueButton2.click()
    # payment1Button = driver.find_element(By.ID, "payment-option-1")
    # payment1Button.click()

    #CONDITIONS
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='conditions_to_approve[terms-and-conditions]']")))
    payment1Button = driver.find_element(By.XPATH, "//*[@id='conditions_to_approve[terms-and-conditions]']")
    payment1Button.click() #//*[@id="conditions_to_approve[terms-and-conditions]"]

    # Verificar el estado después del clic
    assert payment1Button.is_selected(), "El botón no se seleccionó después del clic."
    
    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)

    #REVISAR!    
    # placeorderButton = driver.find_element(By.XPATH, "//*[@id='payment-confirmation']/div[1]/button")
    # placeorderButton.click()
    # time.sleep(6)
