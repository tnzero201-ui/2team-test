from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.login_locators import LoginLocators


class LoginPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def login(self, email, password):
        email_input = self.wait.until(
            EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)
        )
        password_input = self.wait.until(
            EC.visibility_of_element_located(LoginLocators.PASSWORD_INPUT)
        )
        login_button = self.wait.until(
            EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON)
        )

        email_input.clear()
        email_input.send_keys(email)
        password_input.clear()
        password_input.send_keys(password)
        login_button.click()
