import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utils.product_interactions import funcionTest
import time

def test_main5(driver):
    time.sleep(3)
    driver.switch_to.frame(driver.find_element(By.ID, "framelive"))
    #productA
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img")))
    funcionTest(driver,"//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/div/a")

    #productB
    funcionTest(driver,"//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/div/a")

    #productC
    funcionTest(driver,"//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/div/a")   
    time.sleep(4)

    # driver.quit()
    # time.sleep(10)
    # homeButton =driver.find_element(By.XPATH, "//*[@id='_desktop_logo']/h1/a/img")
    # homeButton.click()

    # time.sleep(6)//*[@id="_desktop_logo"]/h1/a/img    //*[@id="_desktop_logo"]   #_desktop_logo > h1 > a > img    //*[@id="_desktop_logo"]          //*[@id="_desktop_logo"]/h1/a/img