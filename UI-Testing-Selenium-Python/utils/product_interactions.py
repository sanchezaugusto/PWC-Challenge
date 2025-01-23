import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils import config

def hover_and_add_to_cart(driver, productXPATH, quickViewXPATH):
    product = driver.find_element(By.XPATH, productXPATH)
    hover= ActionChains(driver).move_to_element(product)
    hover.perform()

    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, quickViewXPATH)))

    quickView = driver.find_element(By.XPATH, quickViewXPATH)
    hover= ActionChains(driver).move_to_element(quickView)
    hover.perform()
    quickView.click()
    
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button")))

    addtocart2Button = driver.find_element(By.XPATH, "//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button")
    addtocart2Button.click()

    time.sleep(2) 
    closeView = driver.find_element(By.XPATH, "//*[@id='blockcart-modal']/div/div/div[2]/div/div[2]/div/div/button")
    closeView.click()

# def wait_for_element(driver, by, value):
#     return WebDriverWait(driver, config.WAIT_TIME).until(
#         EC.presence_of_element_located((by, value))
#     )

# def wait_for_element_to_be_visible_and_clickable(driver, by, value):
#     WebDriverWait(driver, config.WAIT_TIME).until(
#         EC.visibility_of_element_located((by, value))
#     )
#     return WebDriverWait(driver,config.WAIT_TIME).until(
#         EC.element_to_be_clickable((by, value))
# )

# def click_element(driver, by, value):
#     element = wait_for_element(driver, by, value, 20)
#     element.click()