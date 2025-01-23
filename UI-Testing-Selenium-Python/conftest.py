import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.base_page import BasePage as BasePage

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests (chrome or firefox)")
    parser.addoption("--device", action="store", default="desktop", help="Device to run tests (desktop, tabletV, tabletH)")

@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption("--browser")
    device = request.config.getoption("--device")

    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Navegador '{browser}' no soportado")
    
    driver.maximize_window()
    yield driver, device
    driver.quit()

@pytest.fixture(autouse=True)
def cleanup_after_test(driver):
    driver, _ = driver
    yield
    base_page_obj = BasePage(driver)
    base_page_obj.go_to_home()
    
    driver.switch_to.default_content()
