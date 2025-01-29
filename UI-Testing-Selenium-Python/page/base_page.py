from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils import config
import os
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, *locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, *locator):
        element = self.find_element(*locator)
        element.click()

    def enter_text(self, text, *locator):
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def go_to_home(self):    
        # Lista de posibles localizadores del botón Home
        home_button_selectors = [
            (By.XPATH, "//*[@id='_desktop_logo']/a/img"),
            (By.XPATH, "//*[@id='_desktop_logo']/h1/a/img"),
            (By.ID, "_desktop_logo"),
            (By.CSS_SELECTOR, "#_desktop_logo > a > img"),
            (By.CLASS_NAME, "logo img-fluid"),
        ]
        
        # Intentar localizar el botón Home con los distintos selectores
        for selector_type, selector_value in home_button_selectors:
            try:
                home_button = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((selector_type, selector_value))
                )
                home_button.click()
                print(f"Botón Home encontrado y clickeado con selector: {selector_type} = {selector_value}")
                break  # Salir del bucle si se encuentra y hace clic
            except Exception as e:
                print(f"No se pudo encontrar el botón con el selector ({selector_type}, {selector_value}): {e}")
                continue  # Intentar con el siguiente selector
        
        else:
            # Si no se encuentra ningún botón
            raise Exception("No se pudo encontrar el botón Home usando los selectores disponibles.")

    # WAITS    
    # def wait_for_element(driver, by, value, timeout=10):
    #     return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

    # def wait_for_element_to_be_visible_and_clickable(driver, by, value, timeout=10):
    #     return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))

    # def click_element(driver, by, value, timeout=10):
    #     element = wait_for_element_to_be_visible_and_clickable(driver, by, value, timeout)
    #     element.click()
    
    def wait_for_element(self, by, value):
        return WebDriverWait(self.driver, config.WAIT_TIME).until(
            EC.presence_of_element_located((by, value))
    )

    def wait_for_element_to_be_visible_and_clickable(self, by, value):
        WebDriverWait(self.driver, config.WAIT_TIME).until(
            EC.visibility_of_element_located((by, value))
        )
        return WebDriverWait(self.driver,config.WAIT_TIME).until(
            EC.element_to_be_clickable((by, value))
    )

    def wait_for_element_to_be_visible(self, by, value):
        return WebDriverWait(self.driver, config.WAIT_TIME).until(
            EC.visibility_of_element_located((by, value))
    )   
    
    def wait_for_alert(self, by, value):
        return WebDriverWait(self.driver, config.WAIT_TIME).until(
            EC.alert_is_present((by, value))
    )

    def wait_for_text_to_be_present_in_element(self, by, value, text):
        return WebDriverWait(self.driver, config.WAIT_TIME).until(
            EC.text_to_be_present_in_element((by, value), text)
    )

    def wait_element_visible_and_click(self, by, value):
        self.wait_for_element_to_be_visible_and_clickable(by,value)
        element = self.find_element(by, value)
        time.sleep(5)
        element.click()

    def wait_element_and_click(self, by, value):
        self.wait_for_element(by,value)
        element = self.find_element(by,value)
        time.sleep(5)
        element.click()
    
    #CONFIG HOME
    def configHome(self,url, device):
        
        self.driver.get(os.getenv(url))

        WebDriverWait(self.driver, 50).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='framelive']")))

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

    #HOVER AND ADD TO CART
    # def hover_and_add_to_cart(self, product_xpath, add_to_cart_xpath, timeout=10):
    #     product_element = wait_for_element(self, By.XPATH, product_xpath)
    #     add_to_cart_element = wait_for_element_to_be_visible_and_clickable(self, By.XPATH, add_to_cart_xpath, timeout)
    #     actions = ActionChains(self)
    #     actions.move_to_element(product_element).click(add_to_cart_element).perform() 