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
    PRODUCT_XPATH = (By.XPATH,"//*[@id='content']/section[1]/div/div[1]/article/div/div[1]/a")


    PRODUCT_A_XPATH = (By.XPATH,"//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img")
    QUICK_VIEW_A=(By.XPATH,"//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/div/a")
    PRODUCT_B_XPATH=(By.XPATH,"//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/a/picture/img")
    QUICK_VIEW_B=(By.XPATH,"//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/div/a")
    PRODUCT_C_XPATH=(By.XPATH,"//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/a/picture/img")
    QUICK_VIEW_C=(By.XPATH,"//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/div/a")

    CONDITIONS_TO_APPROVE_ID =(By.ID,"conditions_to_approve[terms-and-conditions]")
    

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
    CONDITIONS_TO_APPROVE_ID_TERMS =(By.ID,"conditions_to_approve[terms-and-conditions]") 

    ADD_TO_CART_XPATH =(By.XPATH,"//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button") 
    CHECKOUT_BUTTON_MODAL_XPATH = (By.XPATH,"//*[@id='blockcart-modal']/div/div/div[2]/div/div[2]/div/div/a")
    CHECKOUT_BUTTON_CART_XPATH = (By.XPATH,"//*[@id='main']/div/div[2]/div[1]/div[2]/div/a")

    CART_CSS = (By.CSS_SELECTOR,"#_desktop_cart > div > div > a > span.hidden-sm-down")



    