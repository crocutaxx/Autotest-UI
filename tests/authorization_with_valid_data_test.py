import allure
from base.base_test import BaseTest

@allure.feature("Authorization Functionality")
class TestValidAuthorization(BaseTest):
    @allure.title("Valid authorization")
    @allure.severity("Critical")
    def test_create_room_in_meet(self, setup_1):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.planning_meet_page.make_screenshot("test_valid_authorization")