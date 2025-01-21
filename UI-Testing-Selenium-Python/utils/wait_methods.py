from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

def wait_for_element_to_be_visible_and_clickable(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))

def click_element(driver, by, value, timeout=10):
    element = wait_for_element_to_be_visible_and_clickable(driver, by, value, timeout)
    element.click()

def hover_and_add_to_cart(driver, product_xpath, add_to_cart_xpath, timeout=10):
    product_element = wait_for_element(driver, By.XPATH, product_xpath, timeout)
    add_to_cart_element = wait_for_element_to_be_visible_and_clickable(driver, By.XPATH, add_to_cart_xpath, timeout)
    actions = ActionChains(driver)
    actions.move_to_element(product_element).click(add_to_cart_element).perform()