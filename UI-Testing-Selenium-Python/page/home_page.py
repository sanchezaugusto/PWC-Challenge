import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from .base_page import BasePage
from utils.locators import HomePageLocators
from utils import config

class HomePage(BasePage):
    def config_home(self, url, device):
        self.driver.get(os.getenv(url))

        WebDriverWait(self.driver, config.WAIT_TIME).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='framelive']"))
        )

        iframe = self.driver.find_element(By.ID, "framelive")
        WebDriverWait(self.driver, config.WAIT_TIME).until(
            lambda d: iframe.is_displayed() and iframe.is_enabled()
        )
        myDevice = self.driver.find_element(By.XPATH, device)
        WebDriverWait(self.driver, config.WAIT_TIME).until(
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

    def wait_for_produc_A(self):
        self.wait_for_element(*HomePageLocators.PRODUCT_A_XPATH)

    def hover_and_add_to_cart(self, by_produc, value_produc, byquick, quick_view):
        product = self.driver.find_element(by_produc, value_produc)
        hover= ActionChains(self.driver).move_to_element(product)
        hover.perform()

        WebDriverWait(self.driver, config.WAIT_TIME).until(
        EC.presence_of_element_located((byquick, quick_view)))

        quickView = self.driver.find_element(byquick, quick_view)
        hover= ActionChains(self.driver).move_to_element(quickView)
        hover.perform()
        quickView.click()
        
        WebDriverWait(self.driver, config.WAIT_TIME).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button")))

        addtocart2Button = self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button")
        addtocart2Button.click()

        time.sleep(2) 
        closeView = self.driver.find_element(By.XPATH, "//*[@id='blockcart-modal']/div/div/div[2]/div/div[2]/div/div/button")
        closeView.click()

    def hover_and_add_to_cart_product_A(self):
        self.hover_and_add_to_cart(*HomePageLocators.PRODUCT_A_XPATH, *HomePageLocators.QUICK_VIEW_A)

    def hover_and_add_to_cart_product_B(self):
        self.hover_and_add_to_cart(*HomePageLocators.PRODUCT_B_XPATH, *HomePageLocators.QUICK_VIEW_B)

    def hover_and_add_to_cart_product_C(self):
        self.hover_and_add_to_cart(*HomePageLocators.PRODUCT_C_XPATH, *HomePageLocators.QUICK_VIEW_C)
        
    def product_click(self):
        self.wait_element_and_click(*HomePageLocators.PRODUCT_XPATH)
    
    def smooth_scroll(self, start, end, step, delay=0.1):
        if end is None:
            end = self.driver.execute_script("return document.body.scrollHeight")
        
        for position in range(start, end, step):
            self.driver.execute_script(f"window.scrollTo(0, {position});")
            time.sleep(delay)

    def navigate_and_scroll(self, by_element, value_element, scroll_end=None, scroll_delay=0.2):
        element = WebDriverWait(self.driver, config.WAIT_TIME).until(
            EC.presence_of_element_located((by_element, value_element))
        )
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        element.click()
        time.sleep(5)
        self.smooth_scroll(start=0, step=50, end=scroll_end, delay=scroll_delay)

    def navigate_to_first_element(self):
         # Navegar al primer elemento
         # self.navigate_and_scroll(By.XPATH, "//*[@id='category-3']/a")
        self.navigate_and_scroll(*HomePageLocators.ELEMENT_PAGE_FIRST_XPATH)

    def navigate_to_second_element(self):
        page_height = self.driver.execute_script("return document.body.scrollHeight")
        halfway_point = page_height // 2
        #self.navigate_and_scroll(By.XPATH, "//*[@id='link-cms-page-1-2']", scroll_end=halfway_point)
        self.navigate_and_scroll(*HomePageLocators.ELEMENT_PAGE_SECOND_XPATH, scroll_end=halfway_point)

    def navigate_to_third_element(self):
         page_height = self.driver.execute_script("return document.body.scrollHeight")
         halfway_point = page_height // 2
         self.go_to_home()
         time.sleep(10)
         # Navegar al tercer elemento
         self.navigate_and_scroll(*HomePageLocators.ELEMENT_PAGE_THIRD_XPATH, scroll_end=halfway_point)
         #self.navigate_and_scroll(By.XPATH, "//*[@id='category-6']/a", scroll_end=halfway_point)

    def navigate_to_fourth_element(self):
         page_height = self.driver.execute_script("return document.body.scrollHeight")
         halfway_point = page_height // 2
         #self.navigate_and_scroll(By.XPATH, "//*[@id='js-product-list']/div[1]/div[7]/article/div/div[1]/a/picture/img", scroll_end=halfway_point)
         self.navigate_and_scroll(*HomePageLocators.ELEMENT_PAGE_FOURTH_XPATH, scroll_end=halfway_point)
         # Volver a la página de inicio
         self.go_to_home()

