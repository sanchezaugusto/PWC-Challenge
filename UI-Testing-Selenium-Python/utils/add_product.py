import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def funcionTest(driver, productXPATH, quickViewXPATH):
    product = driver.find_element(By.XPATH, productXPATH)
    hover= ActionChains(driver).move_to_element(product)
    hover.perform()

    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, quickViewXPATH)))
    #time.sleep(1)
    quickView = driver.find_element(By.XPATH, quickViewXPATH)
    hover= ActionChains(driver).move_to_element(quickView)
    hover.perform()
    quickView.click()
    
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button")))
    #time.sleep(2)
    addtocart2Button = driver.find_element(By.XPATH, "//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button")
    addtocart2Button.click()
    # WebDriverWait(driver, 30).until(
    # EC.presence_of_element_located((By.XPATH, "//*[@id='conditions_to_approve[terms-and-conditions]']")))
    time.sleep(2) 
    closeView = driver.find_element(By.XPATH, "//*[@id='blockcart-modal']/div/div/div[2]/div/div[2]/div/div/button")
    closeView.click()