import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from utils.test_data_loader import load_test_data
import time
import os
from selenium.webdriver.common.action_chains import ActionChains

from page.home_page import HomePage 

# Cargar variables de entorno
load_dotenv()

# Cargar los datos de prueba
LANGUAGE_DATA = list(load_test_data("test_data.json")["language"].values())
DEVICE = load_test_data("test_data.json")["device"]

APP_URL = "APP_URL"

@pytest.fixture(scope="function", autouse=True)
def reset_language_to_english(driver):
    driver, device = driver
    yield
    # Cambiar el idioma a inglés después de cada prueba
    change_language(driver, "English")

@pytest.mark.parametrize("language", LANGUAGE_DATA)
def test_main6(language, driver):
    driver, device = driver
    home_page = HomePage(driver)
    home_page.configHome(url=APP_URL, device=DEVICE[device])

    time.sleep(20)
    try:    
        # Cambiar el idioma
        change_language(driver, language)
        time.sleep(10)
        # Ejecutar pruebas en diferentes páginas
        navigate_through_sections(driver)
        time.sleep(10)
    except Exception as e:
        print(f"Error: {e}")

# Función para cambiar el idioma de la página
def change_language(driver, language):
    quickView = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "_desktop_language_selector"))
    )
    hover = ActionChains(driver).move_to_element(quickView)
    hover.perform()
    quickView.click()

    quickView2 = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.LINK_TEXT, language))
    )
    hover2 = ActionChains(driver).move_to_element(quickView2)
    hover2.perform()
    quickView2.click()

# Desplazamiento suave hacia abajo en la página.
def smooth_scroll(driver, start, end, step, delay=0.1):
    if end is None:
        end = driver.execute_script("return document.body.scrollHeight")
    
    for position in range(start, end, step):
        driver.execute_script(f"window.scrollTo(0, {position});")
        time.sleep(delay)

def navigate_through_sections(driver):
    home_page = HomePage(driver)
    # Navegar al primer elemento
    quickView = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='category-3']/a"))
    )
    hover = ActionChains(driver).move_to_element(quickView)
    hover.perform()
    quickView.click()
   
    # Desplazar hacia abajo en la página
    smooth_scroll(driver, start=0, step=50, end=None, delay=0.2)
    time.sleep(2)
    
    # Navegar al segundo elemento
    quickView2 = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='link-cms-page-1-2']"))
    )
    hover2 = ActionChains(driver).move_to_element(quickView2)
    hover2.perform()
    quickView2.click()
    time.sleep(5)
    
    # Desplazar hacia abajo en la página
    page_height = driver.execute_script("return document.body.scrollHeight")
    halfway_point = page_height // 2
    smooth_scroll(driver, start=0, step=50, end=halfway_point, delay=0.2)
    time.sleep(5)
    
    # Volver a la página de inicio
    home_page.go_to_home()
    time.sleep(10)
    # Navegar al tercer elemento
    quickView3 = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='category-6']/a"))
    )
    hover3 = ActionChains(driver).move_to_element(quickView3)
    hover3.perform()
    quickView3.click()

    # Desplazar hacia abajo en la página
    time.sleep(5)
    page_height = driver.execute_script("return document.body.scrollHeight")
    halfway_point = page_height // 2
    smooth_scroll(driver, start=0, step=50, end=halfway_point, delay=0.2)
    time.sleep(2)
    
    # Navegar al cuarto elemento
    quickView4 = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='js-product-list']/div[1]/div[7]/article/div/div[1]/a/picture/img"))
    )
    hover4 = ActionChains(driver).move_to_element(quickView4)
    hover4.perform()
    quickView4.click()
    
    # Desplazar hacia abajo en la página
    smooth_scroll(driver, start=0, step=50, end=halfway_point, delay=0.2)
    time.sleep(10)
    
    # Volver a la página de inicio
    home_page.go_to_home()