from .base_page import BasePage
from utils.locators import ContactPageLocators

class ContactPage(BasePage):
#    def fill_contact_form(self, email, message, attachment_path):
    def fill_contact_form(self, email, message):
        self.enter_text(email, *ContactPageLocators.EMAIL_FIELD)
        self.enter_text(message, *ContactPageLocators.MESSAGE_BOX)
        #self.find_element(*ContactPageLocators.FILE_UPLOAD).send_keys(attachment_path)
        self.click_element(*ContactPageLocators.SEND_BUTTON)