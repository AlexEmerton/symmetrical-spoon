from selenium.webdriver.common.by import By


class Login:
    EMAIL_FIELD = (By.ID, "email")
    PASSW_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "logIn")
    LOGIN_ERROR_MSG = (By.CLASS_NAME, "login-error-container")
    REMEMBER_ME_CHECKBOX = (By.ID, "remember-me")
    SIGN_UP_LINK = (By.LINK_TEXT, "Sign up")
    NEED_HELP_LINK = (By.LINK_TEXT, "Need help?")
    RESET_PASSWORD_BUTTON = (By.ID, "resetBtn")
    LOGIN_HELP_HEADING = (By.XPATH, "//*[text()='Login Help']")
