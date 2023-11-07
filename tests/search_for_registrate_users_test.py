import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Messages Functionality")
class TestSearchUsers(BaseTest):
    @allure.title("Search users")
    @allure.severity("Normal")
    def test_search_users(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_messages_button()
        self.messages_page.is_opened()
        self.messages_page.enter_user_name_in_field()
        self.messages_page.check_result_of_search()
        self.messages_page.make_screenshot("result_of_search_user")
