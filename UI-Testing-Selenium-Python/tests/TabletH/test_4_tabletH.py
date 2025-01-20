import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.product_interactions import funcionTest
import time
import os
from dotenv import load_dotenv

load_dotenv()

def test_main4(driver):
    driver.get(os.getenv("APP_URL"))
    time.sleep(20)
    driver.switch_to.frame(driver.find_element(By.ID, "framelive"))
    # productA
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img")))
    
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
    #HASTA ACA CONTROLE
    continueA = driver.find_element(By.XPATH, "//*[@id='checkout-addresses-step']/div/div/form/div[2]/button")
    continueA.click()
    continueB = driver.find_element(By.XPATH, "//*[@id='js-delivery']/button")
    continueB.click()
    conditionsA = driver.find_element(By.XPATH, "//*[@id='conditions_to_approve[terms-and-conditions]']")
    conditionsA.click()    
    time.sleep(3)
    # homeButton =driver.find_element(By.XPATH, "//*[@id='_desktop_logo']/a/img")
    # homeButton.click()
    # time.sleep(10)
