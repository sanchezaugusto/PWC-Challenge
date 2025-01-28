from selenium.webdriver.common.by import By
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
from page.home_page import HomePage
from page.checkout_page import CheckoutPage
from utils.product_interactions import hover_and_add_to_cart
from dotenv import load_dotenv

load_dotenv()

DEVICE = load_test_data("test_data.json")["device"]
APP_URL = "APP_URL"
CONFIRM_ADDRESS_NAME = "confirm-addresses"
CONDITIONS_TO_APPROVE_ID = "conditions_to_approve[terms-and-conditions]"
CONFIRM_DELIVERY_NAME = "confirmDeliveryOption"
#WAIT_TIME = 20
PRODUCT_A_XPATH = "//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img"
QUICK_VIEW_A = "//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/div/a"

PRODUCT_B_XPATH ="//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/a/picture/img"
QUICK_VIEW_B ="//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/div/a"

PRODUCT_C_XPATH ="//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/a/picture/img"
QUICK_VIEW_C ="//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/div/a"

CART_CSS = "#_desktop_cart > div > div > a > span.hidden-sm-down"
CHECKOUT_BUTTON_XPATH = "//*[@id='main']/div/div[2]/div[1]/div[2]/div/a"

def test_modify_shopping_cart(driver):
    driver, device = driver
    home_page = HomePage(driver)
    checkout_page = CheckoutPage(driver)

    home_page.configHome(url=APP_URL, device = DEVICE[device])
    # Arrange
    home_page.wait_for_element(By.XPATH, PRODUCT_A_XPATH)   
    
    # Act
    hover_and_add_to_cart(driver, PRODUCT_A_XPATH, QUICK_VIEW_A)
    hover_and_add_to_cart(driver, PRODUCT_B_XPATH, QUICK_VIEW_B)
    hover_and_add_to_cart(driver, PRODUCT_C_XPATH, QUICK_VIEW_C)   

    home_page.wait_for_element_to_be_visible_and_clickable( By.CSS_SELECTOR, CART_CSS)
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

    # home_page.wait_for_element_to_be_visible_and_clickable(By.NAME, CONFIRM_ADDRESS_NAME)
    # deliveryButton = driver.find_element(By.NAME, CONFIRM_ADDRESS_NAME)
    # deliveryButton.click()

    # home_page.wait_for_element_to_be_visible_and_clickable(By.NAME, CONFIRM_DELIVERY_NAME)
    # continueButton2 = driver.find_element(By.NAME, CONFIRM_DELIVERY_NAME)
    # continueButton2.click()

    # home_page.wait_for_element_to_be_visible_and_clickable(By.ID, "conditions-to-approve")
    # cond_checkbox = driver.find_element(By.ID, CONDITIONS_TO_APPROVE_ID)
    # cond_checkbox.click()
    checkout_page.confirm_address()
    checkout_page.confirm_delivery()
    checkout_page.accept_terms()

    # Assert
    cond_checkbox = driver.find_element(By.ID, CONDITIONS_TO_APPROVE_ID)
    assert cond_checkbox.is_selected(), "El botón no se seleccionó después del clic."
    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)
