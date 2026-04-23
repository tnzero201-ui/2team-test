def test_login_success(driver):
    # Arrange
    login_page = LoginPage(driver)

    # Act
    login_page.login("test@test.com", "1234")

    # Assert
    assert "dashboard" in driver.current_url