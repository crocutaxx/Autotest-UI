import allure
from base.base_test import BaseTest

@allure.feature("Authorization Functionality")
class TestInvalidAuthorization(BaseTest):
    @allure.title("Invalid authorization")
    @allure.severity("Normal")
    def test_invalid_authorization(self, setup_1):
        self.login_page.open()
        self.login_page.enter_login("mail@mail.com")
        self.login_page.enter_password("PASSWORD")
        self.login_page.click_submit_button()
        self.login_page.check_push_incorect_data()
        self.login_page.is_opened()
        self.planning_meet_page.make_screenshot("test_invalid_authorization")