from selenium.webdriver.common.by import By


class Home:
    PROFILE_MENU = (By.CLASS_NAME, "hui-globaluseritem__display-name")
    FEED_TAB = (By.XPATH, "//*[text()='Feed']")
