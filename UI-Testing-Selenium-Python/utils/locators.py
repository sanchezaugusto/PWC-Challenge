from selenium.webdriver.common.by import By

class HomePageLocators:
    SIGN_IN_BUTTON = (By.ID, '_desktop_user_info')
    CONTACT_US_BUTTON = (By.ID, 'contact-link')
    NEWSLETTER_EMAIL_BOX = (By.NAME, 'email')
    NEWSLETTER_SUBSCRIBE_BUTTON = (By.NAME, 'submitNewsletter')
    NEWSLETTER_SUCCESS_MESSAGE = (By.XPATH, "//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/div/div[2]/p[2]")
    # Add more locators as needed

class AccountPageLocators:
    FIRSTNAME_FIELD = (By.NAME, 'firstname')
    LASTNAME_FIELD = (By.NAME, 'lastname')
    EMAIL_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.NAME, 'password')
    PSGDPR_CHECKBOX = (By.NAME, 'psgdpr')
    CUSTOMER_PRIVACY_CHECKBOX = (By.NAME, 'customer_privacy')
    SUBMIT_BUTTON = (By.XPATH, "//*[@id='customer-form']/footer/button")
    # Add more locators as needed

class ContactPageLocators:
    EMAIL_FIELD = (By.ID, 'email')
    MESSAGE_BOX = (By.ID, 'contactform-message')
    FILE_UPLOAD = (By.ID, 'file-upload')
    SEND_BUTTON = (By.NAME, 'submitMessage')
    # Add more locators as needed

class CheckoutPageLocators:
    WAIT_TIME = 25
    CONFIRM_DELIVERY_NAME = (By.NAME, 'confirmDeliveryOption')
    CONFIRM_ADDRESS_NAME = (By.NAME, 'confirm-addresses')
    #CONDITIONS_TO_APPROVE_ID = (By.NAME, 'conditions_to_approve[terms-and-conditions]')
    CONDITIONS_TO_APPROVE_ID = (By.ID, 'conditions-to-approve')    