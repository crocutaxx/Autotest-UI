import allure
from base.base_test import BaseTest


@allure.feature("Log out Functionality")
class TestLogOut(BaseTest):

    @allure.title("Log Out")
    @allure.severity("Normal")
    def test_log_out(self, setup_1):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_user_avatar_button()
        self.main_page.click_on_log_out_button()
        self.login_page.open()
        self.login_page.make_screenshot("log_out_sucsessful")