import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from page.home import configHome
from utils.product_interactions import funcionTest
from utils.test_data_loader import load_test_data
import time
from utils.custom_assertion import assert_resolution

DEVICE = load_test_data("test_data.json")["device"]
load_dotenv()

def test_main4(driver):
    configHome(driver,url="APP_URL", device = DEVICE["desktop"])
    time.sleep(20)
    # productA
    # WebDriverWait(driver, 15).until(
    # EC.presence_of_element_located((By.XPATH, "//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img")))
    
    funcionTest(driver,"//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/div/a")

    #productB
    funcionTest(driver,"//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/div/a")
 
    #productC
    funcionTest(driver,"//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/div/a")   
    time.sleep(3)

    gotoCartA = driver.find_element(By.XPATH, "//*[@id='_desktop_cart']/div/div/a/span[1]")
    gotoCartA.click()
    time.sleep(2) 
    checkCartA = driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div[1]/div[2]/div/a")
    checkCartA.click()


    # WebDriverWait(driver, 30).until(
    # EC.presence_of_element_located((By.XPATH, "//*[@id='checkout-addresses-step']/div/div/form/div[2]/button")))

    time.sleep(2)
    firstNameBox = driver.find_element(By.ID, "field-firstname")
    lastNameBox = driver.find_element(By.ID, "field-lastname")
    emailBox = driver.find_element(By.ID, "field-email")

    firstNameBox.send_keys("999999")
    time.sleep(2)
    lastNameBox.send_keys("999999")
    time.sleep(2)
    emailBox.send_keys("wrong@mail")
    time.sleep(2)
    driver.find_element(By.NAME, "psgdpr").click()      #acepta condicion
    driver.find_element(By.NAME, "customer_privacy").click()    #acepta condicion
    
    continueA = driver.find_element(By.XPATH, "//*[@id='customer-form']/footer/button")
    continueA.click()

    time.sleep(2)

    expectedMessage = "Invalid format."
    userData1 = driver.find_element(By.XPATH, "//*[@id='customer-form']/div/div[2]/div[1]/div/ul/li")
    assert userData1.text == expectedMessage, \
    f"Expected success message not displayed. Actual message: {userData1.text}"

    userData2 = driver.find_element(By.XPATH, "//*[@id='customer-form']/div/div[3]/div[1]/div/ul/li")
    assert userData2.text == expectedMessage, \
    f"Expected success message not displayed. Actual message: {userData2.text}"

    userData3 = driver.find_element(By.XPATH, "//*[@id='customer-form']/div/div[4]/div[1]/div/ul/li")
    assert userData3.text == expectedMessage, \
    f"Expected success message not displayed. Actual message: {userData3.text}"

    time.sleep(2)

    # WebDriverWait(driver, 30).until(
    # EC.presence_of_element_located((By.XPATH, "//*[@id='js-delivery']/button")))
    # continueB = driver.find_element(By.XPATH, "//*[@id='js-delivery']/button")
    # continueB.click()
    
    # WebDriverWait(driver, 30).until(
    # EC.presence_of_element_located((By.XPATH, "//*[@id='conditions_to_approve[terms-and-conditions]']")))
    # conditionsA = driver.find_element(By.XPATH, "//*[@id='conditions_to_approve[terms-and-conditions]']")
    # # conditionsA.click()

    # assert conditionsA.is_selected(), "El botón no se seleccionó después del clic."
    # expectedResolution = 'desktop'
    # assert_resolution(driver,expectedResolution)
