from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
from page.home_page import HomePage
from page.checkout_page import CheckoutPage
from dotenv import load_dotenv
import time

load_dotenv()

DEVICE = load_test_data("test_data.json")["device"]

def test_modify_shopping_cart(driver):
    driver, device = driver
    home_page = HomePage(driver)
    checkout_page = CheckoutPage(driver)

    home_page.configHome(DEVICE[device])
    # Arrange
    home_page.wait_for_produc_A()   
    
    # Act
    home_page.hover_and_add_to_cart_product_A()
    home_page.hover_and_add_to_cart_product_B()
    home_page.hover_and_add_to_cart_product_C() 

    # home_page.wait_for_element_to_be_visible_and_clickable( By.CSS_SELECTOR, CART_CSS)
    # gotoCart = driver.find_element(By.CSS_SELECTOR, CART_CSS)
    # gotoCart.click()
    checkout_page.wait_element_and_click_goToCart()

    # Increase quantity of product A
    checkout_page.increase_button()

    # Delete Product C
    checkout_page.delete_button()

    # Proceed to checkout
    # continueA = driver.find_element(By.XPATH, CHECKOUT_BUTTON_XPATH)
    # continueA.click()
    checkout_page.wait_element_visible_and_click_check_from_cart() 
    checkout_page.confirm_address()
    checkout_page.confirm_delivery()
    checkout_page.accept_terms()

    # Assert
    assert checkout_page.cond_checkbox().is_selected(), "El botón no se seleccionó después del clic."
    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)
