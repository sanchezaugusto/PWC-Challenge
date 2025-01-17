import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from dotenv import load_dotenv
from utils.test_data_loader import load_test_data
import time
import os

load_dotenv()
LANGUAGE_DATA = load_test_data("test_data.json")["language"]

def test_main6(driver):
    driver.get(os.getenv("APP_URL"))
    time.sleep(3)
    driver.switch_to.frame(driver.find_element(By.ID, "framelive"))
    langSelector = driver.find_element(By.XPATH,"//*[@id='_desktop_language_selector']/div/div/ul")
    # langSelector.click()
    # stateBox = driver.find_element(By.ID, "field-id_state")
    select = Select(langSelector)
    select.select_by_visible_text(LANGUAGE_DATA["language1"])

    time.sleep(5)
