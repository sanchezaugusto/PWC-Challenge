from selenium.webdriver.common.by import By

class HomePageLocators:
    SIGN_IN_BUTTON = (By.ID, '_desktop_user_info')
    SIGN_IN_LINK_TEXT = (By.PARTIAL_LINK_TEXT, 'Sign in')
    REGISTER_LINK_TEXT = (By.PARTIAL_LINK_TEXT, 'No account? Create one here')
    REG_DATA_XPATH = (By.XPATH, "//*[@id='_desktop_user_info']/div/a[2]/span")
    CONTACT_US_ID = (By.ID, 'contact-link')
    NEWSLETTER_EMAIL_BOX = (By.NAME, 'email')
    NEWSLETTER_SUBSCRIBE_BUTTON = (By.NAME, 'submitNewsletter')
    NEWSLETTER_SUCCESS_MESSAGE = (By.XPATH, "//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/div/div[2]/p[2]")
    MESSAGE_ID = "blockEmailSubscription_displayFooterBefore"
    MESSAGE_CSS = (By.CSS_SELECTOR,"p.alert.alert-success")

class AccountPageLocators:
    FIRSTNAME_FIELD = (By.NAME, 'firstname')
    LASTNAME_FIELD = (By.NAME, 'lastname')
    EMAIL_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.NAME, 'password')
    PSGDPR_CHECKBOX = (By.NAME, 'psgdpr')
    CUSTOMER_PRIVACY_CHECKBOX = (By.NAME, 'customer_privacy')
    SUBMIT_BUTTON = (By.XPATH, "//*[@id='customer-form']/footer/button")


class ContactPageLocators:
    EMAIL_FIELD = (By.ID, 'email')
    MESSAGE_BOX = (By.ID, 'contactform-message')
    FILE_UPLOAD = (By.ID, 'file-upload')
    SEND_BUTTON = (By.NAME, 'submitMessage')
    SUCCESS_MESSAGE_XPATH = (By.XPATH, "//*[@id='content']/section/form/div/ul/li")

class CheckoutPageLocators:
    WAIT_TIME = 25
    ADDRESS_ID = (By.ID,'field-address1')
    POSTCODE_ID = (By.ID,"field-postcode")
    CITY_ID = (By.ID,"field-city")
    COUNTRY_ID = (By.ID,"field-id_country") 
    STATE_ID = (By.ID,"field-id_state")
    CONFIRM_DELIVERY_NAME = (By.NAME, 'confirmDeliveryOption')
    CONFIRM_ADDRESS_NAME = (By.NAME, 'confirm-addresses')
    #CONDITIONS_TO_APPROVE_ID = (By.NAME, 'conditions_to_approve[terms-and-conditions]')
    CONDITIONS_TO_APPROVE_ID = (By.ID, 'conditions-to-approve')    