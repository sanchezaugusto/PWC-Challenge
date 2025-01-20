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

def test_main5(driver):
    configHome(driver,url="APP_URL", device = DEVICE["desktop"])
    time.sleep(15)
    #productA
    #WebDriverWait(driver, 20).until(
    #EC.presence_of_element_located((By.XPATH, "//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img")))
    
    funcionTest(driver,"//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/div/a")

    #productB
    funcionTest(driver,"//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/div/a")

    #productC
    funcionTest(driver,"//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/div/a")   
    time.sleep(4)

    gotoCartA = driver.find_element(By.XPATH, "//*[@id='_desktop_cart']/div/div/a/span[1]")
    gotoCartA.click()
    time.sleep(3)

    #ProductoA boton para aumentar numero de productos //*[@id="main"]/div/div[1]/div/div[2]/ul/li[2]/div/div[3]/div/div[2]/div/div[1]/div/span[3]/button[1]
    increaseButton = driver.find_element(By.XPATH, "//*[@id='main']/div/div[1]/div/div[2]/ul/li[1]/div/div[3]/div/div[2]/div/div[1]/div/span[3]/button[1]/i")
    increaseButton.click()
    
    #ProductoB boton para disminuir numero de productos //*[@id="main"]/div/div[1]/div/div[2]/ul/li[2]/div/div[3]/div/div[2]/div/div[1]/div/span[3]/button[1]

    #ProductoC Eliminar //*[@id="main"]/div/div[1]/div/div[2]/ul/li[4]/div/div[3]/div/div[3]/div/a/i
    deleteButton = driver.find_element(By.XPATH, "//*[@id='main']/div/div[1]/div/div[2]/ul/li[3]/div/div[3]/div/div[3]/div/a/i")
    deleteButton.click()

    #Proceed to chekout button //*[@id="main"]/div/div[2]/div[1]/div[2]/div/a
    # continueA = driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div[1]/div[2]/div/a")
    # continueA.click()
    time.sleep(3)
    #//*[@id="main"]/div/div[1]/div/div[2]/ul/li/div/div[3]/div/div[2]/div/div[1]/div/input     
    driver.find_element(By.XPATH, "//*[@id='main']/div/div[1]/div/div[2]/ul/li[2]/div/div[3]/div/div[2]/div/div[1]/div/input").send_keys("999")


    # WebDriverWait(driver, 30).until(
    # EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div/div[2]/div[1]/div[2]/div/a")))   //*[@id="main"]/div/div[1]/div/div[2]/ul/li[2]/div/div[2]
    checkoutButton2 = driver.find_element(By.XPATH, "//*[@id='main']/div/div[1]/div/div[2]/ul/li[2]/div/div[2]")
    checkoutButton2.click()
    time.sleep(15)
    # //*[@id="notifications"]/div/article/ul/li
    # The available purchase order quantity for this product is 300.
    expectedMessage = "The available purchase order quantity for this product is 300."
    userData = driver.find_element(By.XPATH, "//*[@id='notifications']/div/article/ul/li")
    assert userData.text == expectedMessage, \
    f"Expected success message not displayed. Actual message: {userData.text}"
