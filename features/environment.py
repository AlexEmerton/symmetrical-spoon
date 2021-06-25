import os

from selenium import webdriver
from behave import fixture, use_fixture
from steps.utils import Utils


@fixture
def browser_chrome(context):
    context.browser = webdriver.Chrome("drivers/chromedriver.exe")
    context.utils = Utils()
    get_user_credentials_from_env(context)


def get_user_credentials_from_env(context):
    if os.environ.get('LOGIN_PASSWORD') is not None:
        context.env_login_password = os.environ.get('LOGIN_PASSWORD')

    if os.environ.get('LOGIN_USERNAME') is not None:
        context.env_login_username = os.environ.get('LOGIN_USERNAME')


def before_scenario(context, scenario):
    use_fixture(browser_chrome, context)


def after_scenario(context, scenario):
    context.browser.quit()
