# # test_user_registration.py
# import os
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from utils.test_data_loader import load_test_data
# from dotenv import load_dotenv
# from page.base_page import BasePage

# def configHome(driver,url, device):
#     BasePage_obj=BasePage(driver)
#     driver.get(os.getenv(url))

#     BasePage_obj.wait_for_element(By.XPATH, "//*[@id='framelive']") 
#     WebDriverWait(driver, 50).until(
#         EC.presence_of_element_located((By.XPATH, "//*[@id='framelive']")))

#     iframe = driver.find_element(By.ID, "framelive")
#     WebDriverWait(driver, 10).until(
#             lambda d: iframe.is_displayed() and iframe.is_enabled()
#         )
#     myDevice = driver.find_element(By.XPATH, device)
#     WebDriverWait(driver, 10).until(
#             lambda d: iframe.is_displayed() and iframe.is_enabled()
#         )
    
#     myDevice.click()
#     driver.switch_to.frame(driver.find_element(By.ID, "framelive"))
    
   