import page.home_page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from page.base_page import BasePage
from utils.product_interactions import hover_and_add_to_cart
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
APP_URL = "APP_URL"


def test_main4(driver):
    driver, device = driver
    CHECKOUT_BUTTON_XPATH = "//*[@id='main']/div/div[2]/div[1]/div[2]/div/a"
    #WAIT_TIME = 25
    PRODUCT_XPATH = "//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img"
    CART_CSS = "#_desktop_cart > div > div > a > span.hidden-sm-down"

    locators=CheckoutPageLocators()
    checkout_obj=CheckoutPage(driver)
    base_page_obj = BasePage(driver)

    base_page_obj.configHome(url=APP_URL, device=DEVICE[device])
    # Arrange
    time.sleep(50)

    # WebDriverWait(driver, 30).until(
    #     EC.presence_of_all_elements_located((By.CLASS_NAME, "product-miniature js-product-miniature"))
    # )
    # WebDriverWait(driver, 30).until(
    #     EC.presence_of_all_elements_located((By.CLASS_NAME, "quick-view js-quick-view"))
    # )
    base_page_obj.wait_for_element(By.XPATH, PRODUCT_XPATH)
    
    # Act
    #content > section:nth-child(2) > div > div:nth-child(5) > article > div > div.thumbnail-top > a > picture > img
    #content > section:nth-child(2) > div > div:nth-child(5) > article > div > div.thumbnail-top > div > a
    #div.js-product:nth-child(5) > article:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > picture:nth-child(1) > img:nth-child(1)
    #div.js-product:nth-child(5) > article:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)
    #/html/body/main/section/div/div/div/section/section/section[1]/div/div[5]/article/div/div[1]/a/picture/img
    #/html/body/main/section/div/div/div/section/section/section[1]/div/div[5]/article/div/div[1]/div/a
    # elements = driver.find_elements(By.CLASS_NAME,"product-miniature js-product-miniature")
    # quickviews = driver.find_elements(By.CLASS_NAME,"quick-view js-quick-view")
    # productA = elements[3]
    # quickviewA = quickviews[3]
    # productB = elements[4]
    # quickviewB = quickviews[4]
    # productC = elements[5]
    # quickviewC = quickviews[5]

    #productA.click()

    #time.sleep(50)
    # hover_and_add_to_cart(driver,productA,quickviewA)
    # hover_and_add_to_cart(driver,productB,quickviewB)
    # hover_and_add_to_cart(driver,productC,quickviewC)  
    hover_and_add_to_cart(driver,"//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/div/a")
    hover_and_add_to_cart(driver,"//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/div/a")
    hover_and_add_to_cart(driver,"//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/div/a")   
    
    base_page_obj.wait_for_element_to_be_visible_and_clickable(By.CSS_SELECTOR, CART_CSS)
    gotoCart = driver.find_element(By.CSS_SELECTOR, CART_CSS)
    gotoCart.click()

    base_page_obj.wait_for_element(By.XPATH, CHECKOUT_BUTTON_XPATH)
    checkCartA = driver.find_element(By.XPATH, CHECKOUT_BUTTON_XPATH)
    checkCartA.click()
    
    checkout_obj.acc(*locators.CONFIRM_ADDRESS_NAME)
    checkout_obj.acc(*locators.CONFIRM_DELIVERY_NAME)
    checkout_obj.acc(*locators.CONDITIONS_TO_APPROVE_ID)

    
    # Assert
    cond_checkbox = driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]")
    assert cond_checkbox.is_selected(), "El botón no se seleccionó después del clic."
    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)
