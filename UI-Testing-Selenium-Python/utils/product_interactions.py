# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# from utils import config

# def hover_and_add_to_cart(driver, productXPATH, quickViewXPATH):
#     product = driver.find_element(By.XPATH, productXPATH)
#     hover= ActionChains(driver).move_to_element(product)
#     hover.perform()

#     WebDriverWait(driver, 30).until(
#     EC.presence_of_element_located((By.XPATH, quickViewXPATH)))

#     quickView = driver.find_element(By.XPATH, quickViewXPATH)
#     hover= ActionChains(driver).move_to_element(quickView)
#     hover.perform()
#     quickView.click()
    
#     WebDriverWait(driver, 30).until(
#     EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button")))

#     addtocart2Button = driver.find_element(By.XPATH, "//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button")
#     addtocart2Button.click()

#     time.sleep(2) 
#     closeView = driver.find_element(By.XPATH, "//*[@id='blockcart-modal']/div/div/div[2]/div/div[2]/div/div/button")
#     closeView.click()

# def hover_and_add_to_cart_product_A(driver):
#     PRODUCT_A_XPATH="//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img"
#     QUICK_VIEW_A="//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/div/a"
#     hover_and_add_to_cart(driver, PRODUCT_A_XPATH, QUICK_VIEW_A)

# def hover_and_add_to_cart_product_B(driver):
#     PRODUCT_B_XPATH="//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/a/picture/img"
#     QUICK_VIEW_B="//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/div/a"
#     hover_and_add_to_cart(driver, PRODUCT_B_XPATH, QUICK_VIEW_B)

# def hover_and_add_to_cart_product_C(driver):
#     PRODUCT_C_XPATH="//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/a/picture/img"
#     QUICK_VIEW_C="//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/div/a"
#     hover_and_add_to_cart(driver, PRODUCT_C_XPATH, QUICK_VIEW_C)