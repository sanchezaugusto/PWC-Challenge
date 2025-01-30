from page.home_page import HomePage
from page.checkout_page import CheckoutPage
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
from dotenv import load_dotenv
import time
load_dotenv()

CHECKOUT_DATA = load_test_data("test_data.json")["checkout"]
DEVICE = load_test_data("test_data.json")["device"]

def test_main3(driver):
    # Arrange
    driver, device = driver
    home_page = HomePage(driver)
    checkout_page = CheckoutPage(driver)
    home_page.configHome(DEVICE[device])
    
    # Act
    home_page.product_click()

    checkout_page.wait_element_visible_and_click_add_to_cart()
    checkout_page.wait_element_visible_and_click_check_from_modal()
    checkout_page.wait_element_visible_and_click_check_from_cart()

    checkout_page.fill_address( CHECKOUT_DATA["address"], 
                                CHECKOUT_DATA["postcode"],
                                CHECKOUT_DATA["city"],
                                CHECKOUT_DATA["country_value"],
                                CHECKOUT_DATA["state_value"])
    
    checkout_page.confirm_address()
    checkout_page.confirm_delivery()
    checkout_page.accept_terms()

    # Assert
    assert checkout_page.cond_checkbox().is_selected(), "El botón no se seleccionó después del clic."
    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)

