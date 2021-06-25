from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Utils:
    MAXIMUM_WAIT_DUR_SECONDS = 7

    @staticmethod
    def go_to_page(browser, page):
        return browser.get(page)

    def hover_and_click_link(self, browser, hover_element, link):
        actions = ActionChains(browser)
        actions.move_to_element(hover_element).perform()

        link_element = self.get_element_by_link_text(browser, link)
        link_element.click()

    def get_visible_element_by(self, browser, element_locator):
        if self.is_visible(browser, element_locator):
            return browser.find_element(*element_locator)
        else:
            return None

    def get_clickable_element_by(self, browser, element_locator):
        if self.is_clickable(browser, element_locator):
            return browser.find_element(*element_locator)
        else:
            return None

    def get_element_by_class(self, browser, _class):
        element_locator = (By.CLASS_NAME, _class)
        if self.is_visible(browser, element_locator):
            return browser.find_element(*element_locator)
        else:
            print("No element found matching the class: %s" % _class)
            return None

    def get_element_by_id(self, browser, _id):
        element_locator = (By.ID, _id)
        if self.is_visible(browser, element_locator):
            return browser.find_element(*element_locator)
        else:
            print("No element found matching the id: %s" % _id)
            return None

    def get_element_by_link_text(self, browser, link_text):
        element_locator = (By.LINK_TEXT, link_text)
        if self.is_visible(browser, element_locator):
            return browser.find_element(*element_locator)
        else:
            print("No element found matching the link text: %s" % link_text)
            return None

    def get_element_by_text(self, browser, text):
        element_locator = (By.XPATH, "//*[text()='%s']" % text)
        if self.is_visible(browser, element_locator):
            return browser.find_element(*element_locator)
        else:
            print("No element found matching the text: %s" % text)
            return None

    @staticmethod
    def send_keyboard_command(browser, key):
        actions = ActionChains(browser)
        actions.send_keys(getattr(Keys, key))
        actions.perform()

    def is_visible(self, browser, element_locator):
        try:
            WebDriverWait(browser, self.MAXIMUM_WAIT_DUR_SECONDS).until(
                EC.visibility_of_element_located(element_locator)
            )
            return True
        except TimeoutException:
            return False

    def is_clickable(self, browser, element_locator):
        try:
            WebDriverWait(browser, self.MAXIMUM_WAIT_DUR_SECONDS).until(
                EC.element_to_be_clickable(element_locator)
            )
            return True
        except TimeoutException:
            return False

    def is_alert_present(self, browser):
        try:
            WebDriverWait(browser, self.MAXIMUM_WAIT_DUR_SECONDS).until(
                EC.alert_is_present()
            )
            return True
        except TimeoutException:
            return False
