import allure
from base.base_test import BaseTest

@allure.feature("Setting functionality")
class TestSettings(BaseTest):

    @allure.title("Logout")
    @allure.severity("Normal")
    def test_logout(self, user_1):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_user_avatar_button()
        self.main_page.click_on_logout_button()
        self.login_page.open()
        self.login_page.make_screenshot("logout successful")