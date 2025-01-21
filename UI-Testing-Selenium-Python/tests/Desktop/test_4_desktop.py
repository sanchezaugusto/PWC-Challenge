import page.home_page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.product_interactions import wait_for_element_to_be_visible_and_clickable
from utils.product_interactions import wait_for_element
from utils.product_interactions import hover_and_add_to_cart
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
from page.home import configHome
from page.checkout_page import CheckoutPage
from dotenv import load_dotenv

from utils.locators import CheckoutPageLocators

load_dotenv()

DEVICE = load_test_data("test_data.json")["device"]
CONFIRM_DELIVERY_NAME = "confirmDeliveryOption"
APP_URL = "APP_URL"
CONFIRM_ADDRESS_XPATH = "//*[@id='checkout-addresses-step']/div/div/form/div[2]/button"
CONFIRM_ADDRESS_NAME = "confirm-addresses"
CONDITIONS_TO_APPROVE_ID = "conditions_to_approve[terms-and-conditions]"
CHECKOUT_BUTTON_XPATH = "//*[@id='main']/div/div[2]/div[1]/div[2]/div/a"
WAIT_TIME = 25
PRODUCT_XPATH = "//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img"
CART_CSS = "#_desktop_cart > div > div > a > span.hidden-sm-down"

def test_main4(driver):
    configHome(driver, url=APP_URL, device=DEVICE["desktop"])
    #locators=CheckoutPageLocators()
    checkout_obj=CheckoutPage(driver)
    
   
    # Arrange
    wait_for_element(driver, By.XPATH, PRODUCT_XPATH, WAIT_TIME)
    
    # Act
    hover_and_add_to_cart(driver,"//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/div/a")
    hover_and_add_to_cart(driver,"//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/div/a")
    hover_and_add_to_cart(driver,"//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/div/a")   
    
    wait_for_element_to_be_visible_and_clickable(driver, By.CSS_SELECTOR, CART_CSS, WAIT_TIME)
    gotoCart = driver.find_element(By.CSS_SELECTOR, CART_CSS)
    gotoCart.click()

    wait_for_element(driver, By.XPATH, CHECKOUT_BUTTON_XPATH, WAIT_TIME)
    checkCartA = driver.find_element(By.XPATH, CHECKOUT_BUTTON_XPATH)
    checkCartA.click()

    # wait_for_element_to_be_visible_and_clickable(driver, By.NAME, CONFIRM_ADDRESS_NAME, WAIT_TIME)
    # continueA = driver.find_element(By.NAME, CONFIRM_ADDRESS_NAME)
    # continueA.click()

    # wait_for_element_to_be_visible_and_clickable(driver, By.NAME, CONFIRM_DELIVERY_NAME, WAIT_TIME)
    # continueButton2 = driver.find_element(By.NAME, CONFIRM_DELIVERY_NAME)
    # continueButton2.click()

    # wait_for_element_to_be_visible_and_clickable(driver, By.ID, "conditions-to-approve", WAIT_TIME)
    # cond_checkbox = driver.find_element(By.ID, CONDITIONS_TO_APPROVE_ID)
    # cond_checkbox.click()
    
    checkout_obj.acc(*CheckoutPageLocators.CONFIRM_ADDRESS_NAME, wait_time = CheckoutPageLocators.WAIT_TIME)
    checkout_obj.acc(*CheckoutPageLocators.CONFIRM_DELIVERY_NAME, wait_time = CheckoutPageLocators.WAIT_TIME)
    checkout_obj.acc(*CheckoutPageLocators.CONDITIONS_TO_APPROVE_ID, wait_time = CheckoutPageLocators.WAIT_TIME)

    
    # Assert
    cond_checkbox = driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]")
    assert cond_checkbox.is_selected(), "El botón no se seleccionó después del clic."
    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)
