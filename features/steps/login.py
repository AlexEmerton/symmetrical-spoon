from behave import *
from pages.landing import Landing
from pages.home import Home
from pages.login import Login
from pages.sign_up import SignUp


@given('the Hudl homepage is opened')
def hudl_homepage_open(context):
    context.utils.go_to_page(context.browser, "https://www.hudl.com")
    big_text = context.utils.get_visible_element_by(context.browser, Landing.WE_POWER_SPORTS_BANNER)

    assert big_text is not None


@given('the user login is in "{casing}" case')
def apply_user_name_casing(context, casing):
    if casing == "upper":
        context.env_login_username = context.env_login_username.upper()
    elif casing == "lower":
        context.env_login_username = context.env_login_username.lower()
    elif casing == "capitalized":
        context.env_login_username = context.env_login_username.capitalize()


@given('the user password is in "{casing}" case')
def apply_user_name_casing(context, casing):
    if casing == "upper":
        context.env_login_password = context.env_login_password.upper()
    elif casing == "lower":
        context.env_login_password = context.env_login_password.lower()
    elif casing == "capitalized":
        context.env_login_password = context.env_login_password.capitalize()


@when('I go to the logged-in dashboard')
def go_to_logged_in_dashboard_url(context):
    context.utils.go_to_page(context.browser, "https://www.hudl.com/home")


@when('I go to the login page')
def go_to_login_page(context):
    login_button = context.utils.get_visible_element_by(context.browser, Landing.LOGIN_BUTTON)
    login_button.click()

    email_field = context.utils.get_visible_element_by(context.browser, Login.EMAIL_FIELD)
    assert email_field is not None


@when('I enter the following credentials')
def enter_login_creds(context):
    email_field = context.utils.get_visible_element_by(context.browser, Login.EMAIL_FIELD)
    passw_field = context.utils.get_visible_element_by(context.browser, Login.PASSW_FIELD)

    for row in context.table:
        if row['username'] != "null":
            if row['username'] == "env_user_name":
                email_field.send_keys(context.env_login_username)
            else:
                email_field.send_keys(row['username'])

        if row['password'] != "null":
            if row['password'] == "env_user_pass":
                passw_field.send_keys(context.env_login_password)
            else:
                passw_field.send_keys(row['password'])

    context.browser.implicitly_wait(2)


@when('I click on \'log in\'')
def click_log_in(context):
    log_in_button = context.utils.get_visible_element_by(context.browser, Login.LOGIN_BUTTON)
    log_in_button.click()


@when('I click on \'Need help?\'')
def click_need_help(context):
    need_help_link = context.utils.get_visible_element_by(context.browser, Login.NEED_HELP_LINK)
    need_help_link.click()


@when('I click on \'Sign up\'')
def click_sign_up(context):
    sign_up_button = context.utils.get_visible_element_by(context.browser, Login.SIGN_UP_LINK)
    sign_up_button.click()


@then('the login should fail with the following message \'{text}\'')
def should_show_login_error(context, text):
    log_in_error_msg = context.utils.get_visible_element_by(context.browser, Login.LOGIN_ERROR_MSG)
    assert log_in_error_msg.text == text


@then('the \'log in\' button is disabled')
def should_show_login_error(context):
    log_in_button = context.utils.get_visible_element_by(context.browser, Login.LOGIN_BUTTON)
    assert not log_in_button.is_enabled()


@when('I hit "{key}" on the keyboard')
def click_log_in(context, key):
    context.utils.send_keyboard_command(context.browser, key)


@when('I log out')
def log_out(context):
    profile_menu = context.utils.get_visible_element_by(context.browser, Home.PROFILE_MENU)
    context.utils.hover_and_click_link(context.browser, profile_menu, "Log Out")


@then('I should see the logged-in dashboard')
def should_see_logged_in_page(context):
    feed = context.utils.get_visible_element_by(context.browser, Home.FEED_TAB)
    assert feed is not None


@then('I should see the landing page')
def should_see_login_page(context):
    big_text = context.utils.get_visible_element_by(context.browser, Landing.WE_POWER_SPORTS_BANNER)
    assert big_text is not None


@then('I should see the login page')
def should_see_login_page(context):
    email_field = context.utils.get_visible_element_by(context.browser, Login.EMAIL_FIELD)
    assert email_field is not None


@then('I should see the sign up page')
def should_see_sign_up_page(context):
    request_demo_banner = context.utils.get_visible_element_by(context.browser, SignUp.REQUEST_DEMO_BANNER)
    assert request_demo_banner is not None


@then('the \'Remember me\' checkbox is clickable')
def remember_me_should_be_clickable(context):
    remember_me_checkbox = context.utils.get_clickable_element_by(context.browser, Login.REMEMBER_ME_CHECKBOX)
    assert remember_me_checkbox is not None


@then('the \'Remember me\' checkbox is not enabled')
def remember_me_should_be_clickable(context):
    remember_me_checkbox = context.utils.get_clickable_element_by(context.browser, Login.REMEMBER_ME_CHECKBOX)
    assert not remember_me_checkbox.is_selected()


@then('Login help is displayed')
def should_display_login_help(context):
    login_help_heading = context.utils.get_visible_element_by(context.browser, Login.LOGIN_HELP_HEADING)
    assert login_help_heading is not None


@then('the \'send password reset\' button is shown')
def should_show_password_reset_btn(context):
    password_reset_button = context.utils.get_visible_element_by(context.browser, Login.RESET_PASSWORD_BUTTON)
    assert password_reset_button is not None


@then('no alert box should be displayed')
def should_not_display_alert_box(context):
    alert_present = context.utils.is_alert_present(context.browser)

    assert not alert_present
