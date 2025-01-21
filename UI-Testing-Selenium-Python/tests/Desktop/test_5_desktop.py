from selenium.webdriver.common.by import By
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
from utils.product_interactions import wait_for_element_to_be_visible_and_clickable
from utils.product_interactions import hover_and_add_to_cart, wait_for_element
from page.home import configHome
from dotenv import load_dotenv

load_dotenv()

DEVICE = load_test_data("test_data.json")["device"]
APP_URL = "APP_URL"
CONFIRM_ADDRESS_NAME = "confirm-addresses"
CONDITIONS_TO_APPROVE_ID = "conditions_to_approve[terms-and-conditions]"
CONFIRM_DELIVERY_NAME = "confirmDeliveryOption"
WAIT_TIME = 20
PRODUCT_A_XPATH = "//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img"
QUICK_VIEW_A = "//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/div/a"

PRODUCT_B_XPATH ="//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/a/picture/img"
QUICK_VIEW_B ="//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/div/a"

PRODUCT_C_XPATH ="//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/a/picture/img"
QUICK_VIEW_C ="//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/div/a"

CART_CSS = "#_desktop_cart > div > div > a > span.hidden-sm-down"
CHECKOUT_BUTTON_XPATH = "//*[@id='main']/div/div[2]/div[1]/div[2]/div/a"

def test_modify_shopping_cart(driver):
    configHome(driver,url=APP_URL, device = DEVICE["desktop"])
    
    # Arrange
    wait_for_element(driver, By.XPATH, PRODUCT_A_XPATH, WAIT_TIME)   
    
    # Act
    hover_and_add_to_cart(driver, PRODUCT_A_XPATH, QUICK_VIEW_A)
    hover_and_add_to_cart(driver, PRODUCT_B_XPATH, QUICK_VIEW_B)
    hover_and_add_to_cart(driver, PRODUCT_C_XPATH, QUICK_VIEW_C)   

    wait_for_element_to_be_visible_and_clickable(driver, By.CSS_SELECTOR, CART_CSS, WAIT_TIME)
    gotoCart = driver.find_element(By.CSS_SELECTOR, CART_CSS)
    gotoCart.click()

    # Increase quantity of product A
    increaseButton = driver.find_element(By.XPATH, "//*[@id='main']/div/div[1]/div/div[2]/ul/li[2]/div/div[3]/div/div[2]/div/div[1]/div/span[3]/button[1]")
    increaseButton.click()

    # Delete Product C
    deleteButton = driver.find_element(By.XPATH, "//*[@id='main']/div/div[1]/div/div[2]/ul/li[4]/div/div[3]/div/div[3]/div/a/i")
    deleteButton.click()

    # Proceed to checkout
    continueA = driver.find_element(By.XPATH, CHECKOUT_BUTTON_XPATH)
    continueA.click()

    wait_for_element_to_be_visible_and_clickable(driver, By.NAME, CONFIRM_ADDRESS_NAME, WAIT_TIME)
    deliveryButton = driver.find_element(By.NAME, CONFIRM_ADDRESS_NAME)
    deliveryButton.click()

    wait_for_element_to_be_visible_and_clickable(driver, By.NAME, CONFIRM_DELIVERY_NAME, WAIT_TIME)
    continueButton2 = driver.find_element(By.NAME, CONFIRM_DELIVERY_NAME)
    continueButton2.click()

    wait_for_element_to_be_visible_and_clickable(driver, By.ID, "conditions-to-approve", WAIT_TIME)
    cond_checkbox = driver.find_element(By.ID, CONDITIONS_TO_APPROVE_ID)
    cond_checkbox.click()

    # Assert
    assert cond_checkbox.is_selected(), "El botón no se seleccionó después del clic."
    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)
