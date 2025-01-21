from .base_page import BasePage
from utils.locators import AccountPageLocators

class AccountPage(BasePage):
    def create_account(self, firstname, lastname, email, password):
        self.enter_text(firstname, *AccountPageLocators.FIRSTNAME_FIELD)
        self.enter_text(lastname, *AccountPageLocators.LASTNAME_FIELD)
        self.enter_text(email, *AccountPageLocators.EMAIL_FIELD)
        self.enter_text(password, *AccountPageLocators.PASSWORD_FIELD)
        self.click_element(*AccountPageLocators.PSGDPR_CHECKBOX)
        self.click_element(*AccountPageLocators.CUSTOMER_PRIVACY_CHECKBOX)
        self.click_element(*AccountPageLocators.SUBMIT_BUTTON)