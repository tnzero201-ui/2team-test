from selenium.webdriver.common.by import By


class LoginLocators:
    # 이메일 입력창
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")

    # 비밀번호 입력창
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")

    # 로그인 버튼
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    # 에러 메시지
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div[data-testid='error-message']")