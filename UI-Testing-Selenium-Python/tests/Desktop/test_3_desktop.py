from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from page.base_page import BasePage
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
import time
from dotenv import load_dotenv

load_dotenv()

CHECKOUT_DATA = load_test_data("test_data.json")["checkout"]
DEVICE = load_test_data("test_data.json")["device"]
APP_URL = "APP_URL"
WAIT_TIME = 20
PRODUCT_XPATH = "//*[@id='content']/section[1]/div/div[1]/article/div/div[1]/a"
ADD_TO_CART_XPATH = "//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button"
CHECKOUT_BUTTON_LINK = "Proceed to checkout" 
CHECKOUT_BUTTON_XPATH = "//*[@id='blockcart-modal']/div/div/div[2]/div/div[2]/div/div/a"
CHECKOUT_BUTTON2_XPATH = "//*[@id='main']/div/div[2]/div[1]/div[2]/div/a"
ADDRESS_ID = "field-address1"
FIELD_ID = "field-postcode"
CITY_ID = "field-city"
COUNTRY_ID = "field-id_country" 
STATE_ID = "field-id_state" 
#STATE_ID = "field-id_state" 21EEUU chrome   21EEUU firefox
CONFIRM_DELIVERY_NAME = "confirmDeliveryOption"
CONFIRM_ADDRESS_NAME = "confirm-addresses"
CONDITIONS_TO_APPROVE_ID = "conditions_to_approve[terms-and-conditions]"

def test_main3(driver):
    base_page_obj = BasePage(driver)
    
    base_page_obj.configHome(url=APP_URL, device = DEVICE["desktop"])
    # Arrange
    base_page_obj.wait_for_element(By.XPATH, PRODUCT_XPATH)

    # Act
    product1 = driver.find_element(By.XPATH, PRODUCT_XPATH)
    product1.click()

    base_page_obj.wait_for_element_to_be_visible_and_clickable(By.XPATH, ADD_TO_CART_XPATH)
    addtocartButton = driver.find_element(By.XPATH, ADD_TO_CART_XPATH)
    addtocartButton.click()

    base_page_obj.wait_for_element_to_be_visible_and_clickable(By.XPATH, CHECKOUT_BUTTON_XPATH)
    checkoutButton = driver.find_element(By.XPATH, CHECKOUT_BUTTON_XPATH)
    checkoutButton.click()

    base_page_obj.wait_for_element_to_be_visible_and_clickable(By.XPATH, CHECKOUT_BUTTON2_XPATH)
    checkoutButton2 = driver.find_element(By.XPATH, CHECKOUT_BUTTON2_XPATH)
    checkoutButton2.click()

    base_page_obj.wait_for_element(By.ID, ADDRESS_ID)
    
    addressBox = driver.find_element(By.ID, ADDRESS_ID)
    postcodeBox = driver.find_element(By.ID, FIELD_ID)
    cityBox = driver.find_element(By.ID, CITY_ID)

    addressBox.send_keys(CHECKOUT_DATA["address"])
    postcodeBox.send_keys(CHECKOUT_DATA["postcode"])
    cityBox.send_keys(CHECKOUT_DATA["city"])
    

    base_page_obj.wait_for_element(By.ID, COUNTRY_ID)
    countryBox = driver.find_element(By.ID, COUNTRY_ID)
    select_country = Select(countryBox)
    select_country.select_by_value(CHECKOUT_DATA["country_value"])

    base_page_obj.wait_for_element(By.ID, STATE_ID)
    stateBox = driver.find_element(By.ID, STATE_ID)
    select = Select(stateBox)
    select.select_by_value(CHECKOUT_DATA["state_value"])
    #time.sleep(300)
    deliveryButton = driver.find_element(By.NAME, CONFIRM_ADDRESS_NAME)
    deliveryButton.click()

    base_page_obj.wait_for_element_to_be_visible_and_clickable(By.NAME, CONFIRM_DELIVERY_NAME)
    continueButton2 = driver.find_element(By.NAME, CONFIRM_DELIVERY_NAME)
    continueButton2.click()

    base_page_obj.wait_for_element_to_be_visible_and_clickable(By.ID, "conditions-to-approve")
    payment1Button = driver.find_element(By.ID, CONDITIONS_TO_APPROVE_ID)
    payment1Button.click()

    # Assert
    assert payment1Button.is_selected(), "El botón no se seleccionó después del clic."
    
    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)

