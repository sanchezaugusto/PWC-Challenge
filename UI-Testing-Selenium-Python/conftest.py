import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests (chrome or firefox)")

@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Navegador '{browser}' no soportado")
    
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def cleanup_after_test(driver):
    yield
    
    # Lista de posibles localizadores del botón Home
    home_button_selectors = [
        (By.XPATH, "//*[@id='_desktop_logo']/a/img"),
        (By.XPATH, "//*[@id='_desktop_logo']/h1/a/img"),
        (By.ID, "_desktop_logo")
    ]
    
    # Intentar localizar el botón Home con los distintos selectores
    for selector_type, selector_value in home_button_selectors:
        try:
            home_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((selector_type, selector_value))
            )
            home_button.click()
            print(f"Botón Home encontrado y clickeado con selector: {selector_type} = {selector_value}")
            break  # Salir del bucle si se encuentra y hace clic
        except Exception as e:
            print(f"No se pudo encontrar el botón con el selector ({selector_type}, {selector_value}): {e}")
            continue  # Intentar con el siguiente selector
    
    else:
        # Si no se encuentra ningún botón
        raise Exception("No se pudo encontrar el botón Home usando los selectores disponibles.")
    
    # Volver al contenido principal (por si se cambió de frame)
    driver.switch_to.default_content()
