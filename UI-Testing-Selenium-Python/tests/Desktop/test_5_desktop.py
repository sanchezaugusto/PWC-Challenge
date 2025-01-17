import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from page.home import configHome
from utils.add_product import funcionTest
from utils.test_data_loader import load_test_data
import time
from utils.custom_assertion import assert_resolution

DEVICE = load_test_data("test_data.json")["device"]
load_dotenv()

def test_main5(driver):
    configHome(driver,url="APP_URL", device = DEVICE["desktop"])
    #productA
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img")))
    funcionTest(driver,"//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/div/a")

    #productB
    funcionTest(driver,"//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/div/a")

    #productC
    funcionTest(driver,"//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/div/a")   
    time.sleep(4)

    gotoCartA = driver.find_element(By.XPATH, "//*[@id='_desktop_cart']/div/div/a/span[1]")
    gotoCartA.click()
    time.sleep(2)

    #ProductoA boton para aumentar numero de productos //*[@id="main"]/div/div[1]/div/div[2]/ul/li[2]/div/div[3]/div/div[2]/div/div[1]/div/span[3]/button[1]
    increaseButton = driver.find_element(By.XPATH, "//*[@id='main']/div/div[1]/div/div[2]/ul/li[2]/div/div[3]/div/div[2]/div/div[1]/div/span[3]/button[1]")
    increaseButton.click()
    
    #ProductoB boton para disminuir numero de productos //*[@id="main"]/div/div[1]/div/div[2]/ul/li[2]/div/div[3]/div/div[2]/div/div[1]/div/span[3]/button[1]

    #ProductoC Eliminar //*[@id="main"]/div/div[1]/div/div[2]/ul/li[4]/div/div[3]/div/div[3]/div/a/i
    deleteButton = driver.find_element(By.XPATH, "//*[@id='main']/div/div[1]/div/div[2]/ul/li[4]/div/div[3]/div/div[3]/div/a/i")
    deleteButton.click()

    #Proceed to chekout button //*[@id="main"]/div/div[2]/div[1]/div[2]/div/a
    continueA = driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div[1]/div[2]/div/a")
    continueA.click()

    #Continue Addresses //*[@id="checkout-addresses-step"]/div/div/form/div[2]/button
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='checkout-addresses-step']/div/div/form/div[2]/button")))
    continueA = driver.find_element(By.XPATH, "//*[@id='checkout-addresses-step']/div/div/form/div[2]/button")
    continueA.click()

    #Continue Shipping     //*[@id="js-delivery"]/button
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='js-delivery']/button")))
    continueB = driver.find_element(By.XPATH, "//*[@id='js-delivery']/button")
    continueB.click()

    # I agree checkbox //*[@id="conditions_to_approve[terms-and-conditions]"]
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='conditions_to_approve[terms-and-conditions]']")))
    conditionsA = driver.find_element(By.XPATH, "//*[@id='conditions_to_approve[terms-and-conditions]']")
    conditionsA.click()

    assert conditionsA.is_selected(), "El botón no se seleccionó después del clic."
    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)
