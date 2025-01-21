from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.locators import CheckoutPageLocators
from utils.product_interactions import wait_for_element_to_be_visible_and_clickable

class CheckoutPage(BasePage):
    ADDRESS_ID = "field-address1"
    FIELD_ID = "field-postcode"
    CITY_ID = "field-city"
    STATE_ID = "field-id_state"
    CONFIRM_DELIVERY_NAME = "confirmDeliveryOption"
    CONFIRM_ADDRESS_NAME = "confirm-addresses"
    CONDITIONS_TO_APPROVE_ID = "conditions_to_approve[terms-and-conditions]"

    def fill_address(self, address, postcode, city, state_value):
        self.enter_text(address, By.ID, self.ADDRESS_ID)
        self.enter_text(postcode, By.ID, self.FIELD_ID)
        self.enter_text(city, By.ID, self.CITY_ID)
        stateBox = self.find_element(By.ID, self.STATE_ID)
        select = Select(stateBox)
        select.select_by_value(state_value)

    def confirm_address(self):
        self.click_element(By.NAME, self.CONFIRM_ADDRESS_NAME)

    def confirm_delivery(self):
        self.click_element(By.NAME, self.CONFIRM_DELIVERY_NAME)

    def accept_terms(self):
        self.click_element(By.ID, self.CONDITIONS_TO_APPROVE_ID)

    def is_terms_accepted(self):
        return self.find_element(By.ID, self.CONDITIONS_TO_APPROVE_ID).is_selected()
    
    def acc(self,*locator,wait_time):
        wait_for_element_to_be_visible_and_clickable(self.driver,locator[0] ,locator[1],wait_time)
        return self.find_element(*locator).click()
        #obj (la instancia) se pasa automáticamente como el primer argumento.
        