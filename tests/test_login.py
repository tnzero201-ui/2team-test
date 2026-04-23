from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage

def test_login_success(driver):
    # Arrange
    login_page = LoginPage(driver)

    # Act
    login_page.login("test@test.com", "1234")

    # Assert
    WebDriverWait(driver, 5).until(lambda d: "dashboard" in d.current_url)
    assert "dashboard" in driver.current_url
