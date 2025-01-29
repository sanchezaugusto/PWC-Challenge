from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from page.home_page import HomePage
from page.checkout_page import CheckoutPage
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
from dotenv import load_dotenv
import time
load_dotenv()

CHECKOUT_DATA = load_test_data("test_data.json")["checkout"]
DEVICE = load_test_data("test_data.json")["device"]
APP_URL = "APP_URL"
PRODUCT_XPATH = "//*[@id='content']/section[1]/div/div[1]/article/div/div[1]/a"
ADD_TO_CART_XPATH = "//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button"
CHECKOUT_BUTTON_XPATH = "//*[@id='blockcart-modal']/div/div/div[2]/div/div[2]/div/div/a"
CHECKOUT_BUTTON2_XPATH = "//*[@id='main']/div/div[2]/div[1]/div[2]/div/a"
CONDITIONS_TO_APPROVE_ID = "conditions_to_approve[terms-and-conditions]"

def test_main3(driver):
    # Arrange
    driver, device = driver
    home_page = HomePage(driver)
    checkout_page = CheckoutPage(driver)
    home_page.configHome(url=APP_URL, device = DEVICE[device])
    
    # Act
    #home_page.product_click() ver si puedo poner esta funcion nomas 
    home_page.wait_for_element(By.XPATH, PRODUCT_XPATH)
    product1 = driver.find_element(By.XPATH, PRODUCT_XPATH)
    product1.click()
    
    checkout_page.wait_element_visible_and_click_add_to_cart()
    checkout_page.wait_element_visible_and_click_check_from_modal()
    checkout_page.wait_element_visible_and_click_check_from_cart()
    # home_page.wait_for_element_to_be_visible_and_clickable(By.XPATH, ADD_TO_CART_XPATH)
    # addtocartButton = driver.find_element(By.XPATH, ADD_TO_CART_XPATH)
    # time.sleep(5)
    # addtocartButton.click()

    # home_page.wait_for_element_to_be_visible_and_clickable(By.XPATH, CHECKOUT_BUTTON_XPATH)
    # checkoutButton = driver.find_element(By.XPATH, CHECKOUT_BUTTON_XPATH)
    # time.sleep(5)
    # checkoutButton.click()

    # home_page.wait_for_element_to_be_visible_and_clickable(By.XPATH, CHECKOUT_BUTTON2_XPATH)
    # checkoutButton2 = driver.find_element(By.XPATH, CHECKOUT_BUTTON2_XPATH)
    # time.sleep(5)
    # checkoutButton2.click()

    checkout_page.fill_address( CHECKOUT_DATA["address"], 
                                CHECKOUT_DATA["postcode"],
                                CHECKOUT_DATA["city"],
                                CHECKOUT_DATA["country_value"],
                                CHECKOUT_DATA["state_value"])
    
    checkout_page.confirm_address()
    checkout_page.confirm_delivery()
    checkout_page.accept_terms()

    # Assert
    # payment1Button = driver.find_element(By.ID, CONDITIONS_TO_APPROVE_ID)
    assert checkout_page.cond_checkbox().is_selected(), "El botón no se seleccionó después del clic."
    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)

