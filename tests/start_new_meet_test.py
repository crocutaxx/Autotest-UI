import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Meet Functionality")
class TestNewMeet(BaseTest):

    @allure.title("Start new meet")
    @allure.severity("Normal")
    def test_start_new_meet(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_new_meet_button()
        # self.meet_page.is_opened() Разобраться с идентификатором комант
        # self.meet_page.click_on_dismiss_alert_button() Нужен для w10
        self.meet_page.click_on_enter_without_cheking_button()
        self.meet_page.check_enter_meet_push()
        self.meet_page.make_screenshot("start_new_meet")
