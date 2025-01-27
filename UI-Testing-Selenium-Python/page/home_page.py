import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from utils.locators import HomePageLocators

class HomePage(BasePage):
    def config_home(self, url, device):
        self.driver.get(os.getenv(url))

        WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='framelive']"))
        )

        iframe = self.driver.find_element(By.ID, "framelive")
        WebDriverWait(self.driver, 10).until(
            lambda d: iframe.is_displayed() and iframe.is_enabled()
        )
        myDevice = self.driver.find_element(By.XPATH, device)
        WebDriverWait(self.driver, 10).until(
            lambda d: iframe.is_displayed() and iframe.is_enabled()
        )

        myDevice.click()
        self.driver.switch_to.frame(self.driver.find_element(By.ID, "framelive"))

    def click_sign_in(self):
        self.click_element(*HomePageLocators.SIGN_IN_BUTTON)

    def sign_up_newsletter(self, email):
        self.wait_for_element(*HomePageLocators.NEWSLETTER_EMAIL_BOX)
        self.enter_text(email, *HomePageLocators.NEWSLETTER_EMAIL_BOX)
        self.click_element(*HomePageLocators.NEWSLETTER_SUBSCRIBE_BUTTON)

    def click_on_sign_in(self):
        self.wait_for_element(*HomePageLocators.SIGN_IN_LINK_TEXT)
        self.click_element(*HomePageLocators.SIGN_IN_LINK_TEXT)

    def click_on_register(self):
        self.wait_for_element(*HomePageLocators.REGISTER_LINK_TEXT)
        self.click_element(*HomePageLocators.REGISTER_LINK_TEXT)

    def wait_for_user_info(self):
        self.wait_for_element(*HomePageLocators.REG_DATA_XPATH)

    def click_on_contact_us(self):
        self.wait_for_element(*HomePageLocators.CONTACT_US_ID)
        self.click_element(*HomePageLocators.CONTACT_US_ID)

    def wait_for_newsletter_message(self):
        self.wait_for_element(*HomePageLocators.MESSAGE_CSS)