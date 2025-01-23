from utils.test_data_loader import load_test_data
from dotenv import load_dotenv
import os

load_dotenv()

# Datos de registro
REGISTRATION_DATA = load_test_data("test_data.json")["registration"]

# Datos de contacto
CONTACTFORM_DATA = load_test_data("test_data.json")["contact_form"]

# Datos del dispositivo
DEVICE = load_test_data("test_data.json")["device"]

# URL de la aplicación
APP_URL = os.getenv("APP_URL")

# Tiempo de espera
WAIT_TIME = 25