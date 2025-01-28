from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.locators import CheckoutPageLocators
from page.base_page import BasePage
import utils.config as config
class CheckoutPage(BasePage):
    ADDRESS_ID = "field-address1"
    FIELD_ID = "field-postcode"
    CITY_ID = "field-city"
    STATE_ID = "field-id_state"
    CONFIRM_DELIVERY_NAME = "confirmDeliveryOption"
    CONFIRM_ADDRESS_NAME = "confirm-addresses"
    CONDITIONS_TO_APPROVE_ID = "conditions_to_approve[terms-and-conditions]"

    def fill_address(self, address, postcode, city, country_value, state_value):
        self.wait_for_element(*CheckoutPageLocators.ADDRESS_ID)
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
        self.click_element(By.NAME, self.CONFIRM_ADDRESS_NAME)

    # def confirm_delivery(self):
    #     self.click_element(By.NAME, self.CONFIRM_DELIVERY_NAME)

    # def accept_terms(self):
    #     self.click_element(By.ID, self.CONDITIONS_TO_APPROVE_ID)

    def is_terms_accepted(self):
        return self.find_element(By.ID, self.CONDITIONS_TO_APPROVE_ID).is_selected()
    
    def acc(self,*locator):
        BasePage_obj=BasePage(self.driver)
        BasePage_obj.wait_for_element_to_be_visible_and_clickable(locator[0] ,locator[1])
        return self.find_element(*locator).click()
        #obj (la instancia) se pasa automáticamente como el primer argumento.

    def confirm_delivery(self):
        self.wait_for_element_to_be_visible_and_clickable(*CheckoutPageLocators.CONFIRM_DELIVERY_NAME).click()

    def accept_terms(self):
        self.wait_for_element_to_be_visible_and_clickable(*CheckoutPageLocators.CONDITIONS_TO_APPROVE_ID).click()
        