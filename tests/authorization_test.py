import allure
from base.base_test import BaseTest

@allure.feature("Authorization functionality")
class TestAuthorization(BaseTest):

    @allure.title("Invalid authorization")
    @allure.severity("Normal")
    def test_invalid_authorization(self, user_1):
        self.login_page.open()
        self.login_page.enter_login("mail@mail.com")
        self.login_page.enter_password("PASSWORD")
        self.login_page.click_submit_button()
        self.login_page.check_push_incorrect_data()
        self.login_page.is_opened()
        self.planning_meet_page.make_screenshot("The user is not logged in")


    @allure.title("Valid authorization")
    @allure.severity("Critical")
    def test_valid_auth(self, user_1):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.planning_meet_page.make_screenshot("The user has been successfully logged in")
