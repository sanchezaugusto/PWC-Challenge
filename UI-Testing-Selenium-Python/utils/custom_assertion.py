from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def assert_resolution(driver, expected_resolution):
    """
    Verifica que la resolución de la ventana del navegador coincida con la resolución esperada.
    
    :param driver: Instancia del WebDriver.
    :param expected_resolution: Resolución esperada ('desktop', 'tabletH', 'tabletV', 'phone').
    """
    # Obtener el tamaño de la ventana
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']

    # Definir las resoluciones esperadas
    resolutions = {
        'desktop': (width > 1024),  # Ancho mayor que 1024px
        'tabletH': (768 <= width <= 1024 and height < 768),  # Rango de tablet horizontal
        'tabletV': (width <= 768 and height >= 768),  # Rango de tablet vertical
        'phone': (width <= 480),  # Ancho menor o igual a 480px
    }

    # Verificar si la resolución actual coincide con la esperada
    if not resolutions.get(expected_resolution, False):
        raise AssertionError(f"Se esperaba una resolución '{expected_resolution}' pero la resolución actual es {width}x{height}.")
    
    print(f"Resolución correcta: {expected_resolution} ({width}x{height})")