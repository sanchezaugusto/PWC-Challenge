import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        service = Service(executable_path="../driver/chromedriver.exe")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        service = Service(executable_path="../driver/geckodriver.exe")
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Navegador '{browser}' no soportado")
    
    driver.maximize_window()
    yield driver
    driver.quit()
