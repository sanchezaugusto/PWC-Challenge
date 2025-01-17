import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_main7(driver):
    driver.switch_to.frame(driver.find_element(By.ID, "framelive"))
    loginButton = driver.find_element(By.ID, "contact-link")
    loginButton.click()

    emailboxA = driver.find_element(By.XPATH,"//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/div/div[1]/div[1]/input")
    emailboxA.send_keys("person123@mail.com")
    suscribeButton = driver.find_element(By.XPATH,"//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/div/div[1]/input[1]")
    suscribeButton.click()


    success_message = driver.find_element(By.XPATH, "//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/p")
    assert success_message.text == "You have successfully subscribed to this newsletter.", \
        f"Expected success message not displayed. Actual message: {success_message.text}"
    time.sleep(10)
