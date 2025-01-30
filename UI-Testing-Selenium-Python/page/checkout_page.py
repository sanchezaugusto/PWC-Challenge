from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.locators import CheckoutPageLocators
from page.base_page import BasePage
import utils.config as config
import time
class CheckoutPage(BasePage):

    def fill_address(self, address, postcode, city, country_value, state_value):
        time.sleep(5)
        #self.wait_for_element(*CheckoutPageLocators.ADDRESS_ID)
        self.enter_text(address, *CheckoutPageLocators.ADDRESS_ID)
        self.enter_text(postcode, *CheckoutPageLocators.POSTCODE_ID)
        self.enter_text(city, *CheckoutPageLocators.CITY_ID)

        self.wait_for_element(*CheckoutPageLocators.COUNTRY_ID)
        countryBox = self.find_element(*CheckoutPageLocators.COUNTRY_ID)
        select_country = Select(countryBox)
        select_country.select_by_value(country_value)
        
        self.wait_for_element(*CheckoutPageLocators.STATE_ID)
        stateBox = self.find_element(*CheckoutPageLocators.STATE_ID)
        select_country = Select(stateBox)
        select_country.select_by_value(state_value)
        #self.click_element(By.NAME, self.CONFIRM_ADDRESS)

    def confirm_address(self):
        # self.click_element(By.NAME, self.CONFIRM_ADDRESS_NAME)
        self.click_element(*CheckoutPageLocators.CONFIRM_ADDRESS_NAME)


    def is_terms_accepted(self):
        return self.find_element(*CheckoutPageLocators.CONDITIONS_TO_APPROVE_ID).is_selected()

    def confirm_delivery(self):
        self.wait_for_element_to_be_visible_and_clickable(*CheckoutPageLocators.CONFIRM_DELIVERY_NAME).click()

    def accept_terms(self):
        self.wait_for_element_to_be_visible_and_clickable(*CheckoutPageLocators.CONDITIONS_TO_APPROVE_ID).click()
    
    def cond_checkbox(self):
        return self.find_element(*CheckoutPageLocators.CONDITIONS_TO_APPROVE_ID_TERMS)
    
    def wait_element_visible_and_click_add_to_cart(self):
        self.wait_element_visible_and_click(*CheckoutPageLocators.ADD_TO_CART_XPATH)

    def wait_element_visible_and_click_check_from_modal(self):
        self.wait_element_visible_and_click(*CheckoutPageLocators.CHECKOUT_BUTTON_MODAL_XPATH)

    def wait_element_visible_and_click_check_from_cart(self):
        self.wait_element_visible_and_click(*CheckoutPageLocators.CHECKOUT_BUTTON_CART_XPATH)
   
    def wait_element_and_click_goToCart(self):
        self.wait_element_visible_and_click(*CheckoutPageLocators.CART_CSS)

    def wait_element_and_click_checkCart(self):
        self.wait_element_and_click(*CheckoutPageLocators.CHECKOUT_BUTTON_CART_XPATH)

    def increase_button(self):
        self.wait_element_visible_and_click(*CheckoutPageLocators.INCREASE_XPATH)

    def delete_button(self):
        self.wait_element_visible_and_click(*CheckoutPageLocators.DELETE_XPATH)
    
