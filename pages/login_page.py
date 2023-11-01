import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_FIELD = ("xpath", '//input[@id="login_email"]')
    PASSWORD_FIELD = ("xpath", '//input[@id="login_password"]')
    SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")
    ENTER_MEET_BUTTON = ("xpath", "//button[@type='button']")

    @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)
    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    @allure.step("Click enter meet button")
    def enter_meet_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ENTER_MEET_BUTTON)).click()