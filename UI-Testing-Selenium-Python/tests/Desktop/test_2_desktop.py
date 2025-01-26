from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
from dotenv import load_dotenv
from page.home_page import HomePage
from page.contact_page import ContactPage

load_dotenv()

CONTACTFORM_DATA = load_test_data("test_data.json")["contact_form"]
DEVICE = load_test_data("test_data.json")["device"]
APP_URL = "APP_URL"
SUCCESS_MESSAGE_XPATH = "//*[@id='content']/section/form/div/ul/li"

def test_main2(driver):
    # Arrange
    driver, device = driver
    contact_page = ContactPage(driver)
    home_page = HomePage(driver)
    home_page.configHome(url=APP_URL, device=DEVICE[device])

    # Act
    home_page.click_on_contact_us()
    contact_page.fill_contact_form(CONTACTFORM_DATA["email"],
                                    CONTACTFORM_DATA["message"])
    
    # Assert
    contact_page.wait_for_message()
    success_message = driver.find_element(By.XPATH, SUCCESS_MESSAGE_XPATH)

    assert success_message.text == "Your message has been successfully sent to our team.", \
    f"Expected success message not displayed. Actual message: {success_message.text}"

    expected_resolution = 'desktop'
    assert_resolution(driver,expected_resolution)