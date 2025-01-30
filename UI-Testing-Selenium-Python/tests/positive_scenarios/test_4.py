from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from page.home_page import HomePage
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.checkout_page import CheckoutPage
from dotenv import load_dotenv
import time
from utils.locators import CheckoutPageLocators

load_dotenv()

DEVICE = load_test_data("test_data.json")["device"]


def test_main4(driver):
    driver, device = driver
    #CHECKOUT_BUTTON_XPATH = "//*[@id='main']/div/div[2]/div[1]/div[2]/div/a"
    PRODUCT_XPATH = "//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img"
    #CART_CSS = "#_desktop_cart > div > div > a > span.hidden-sm-down"

    #locators=CheckoutPageLocators()
    checkout_page=CheckoutPage(driver)
    home_page = HomePage(driver)

    home_page.configHome(DEVICE[device])
    # Arrange
    time.sleep(5)

    home_page.wait_for_element(By.XPATH, PRODUCT_XPATH)
    
    # Act    
    home_page.hover_and_add_to_cart_product_A()
    home_page.hover_and_add_to_cart_product_B()
    home_page.hover_and_add_to_cart_product_C()

    # home_page.wait_for_element_to_be_visible_and_clickable(By.CSS_SELECTOR, CART_CSS)
    # gotoCart = driver.find_element(By.CSS_SELECTOR, CART_CSS)
    # gotoCart.click()
    checkout_page.wait_element_and_click_goToCart()

    #crear una funcion para esto en checkout
    checkout_page.wait_element_and_click_checkCart()
    checkout_page.confirm_address()
    checkout_page.confirm_delivery()
    checkout_page.accept_terms()
    
    # Assert
    assert checkout_page.cond_checkbox().is_selected(), "El botón no se seleccionó después del clic."
    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)
