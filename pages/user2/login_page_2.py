import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE
    # Buttons
    USERNAME_FIELD = ("xpath", '//input[@id="login_email"]')
    PASSWORD_FIELD = ("xpath", '//input[@id="login_password"]')
    SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")
    ENTER_MEET_BUTTON = ("xpath", "//button[@type='button']")
    # Push notification
    INCORECT_DATA = ("xpath", "//div[contains(@class, 'ant-notification-notice-closable')]")

    @pytest.mark.parametrize("login", [("login")])
    def enter_login(self, login):
        with allure.step("Enter login"):
            self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @pytest.mark.parametrize("password", [("password")])
    def enter_password(self, password):
        with allure.step("Enter password"):
            self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Confir login and pass - Click submit button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    @allure.step("Click enter meet button")
    def click_enter_meet_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ENTER_MEET_BUTTON)).click()

    @allure.step("Check push incorect data")
    def check_push_incorect_data(self):
        self.wait.until(EC.visibility_of_element_located(self.INCORECT_DATA))
        self.wait.until(EC.text_to_be_present_in_element(self.INCORECT_DATA, "EMAIL_OR_PASSWORD_INCORRECT"))

    @allure.step("Clear login")
    def clear_login(self):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).clear()

    @allure.step("Clear password")
    def clear_password(self):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).clear()

