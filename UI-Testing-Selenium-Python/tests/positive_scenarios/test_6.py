import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from utils.test_data_loader import load_test_data
import time
from selenium.webdriver.common.action_chains import ActionChains

from page.home_page import HomePage 

# Cargar variables de entorno
load_dotenv()

# Cargar los datos de prueba
LANGUAGE_DATA = list(load_test_data("test_data.json")["language"].values())
DEVICE = load_test_data("test_data.json")["device"]


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
    home_page.configHome(DEVICE[device])

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

def navigate_through_sections(driver):
    home_page = HomePage(driver)
    home_page.navigate_to_first_element()
    home_page.navigate_to_second_element()
    home_page.navigate_to_third_element()
    home_page.navigate_to_fourth_element()
    