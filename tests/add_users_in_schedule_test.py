import allure
import pytest
from base.base_test import BaseTest

@allure.feature("Schedule Functionality")
class TestAddUserInSchedule(BaseTest):

    @allure.title("Create schedule")
    @allure.severity("Critical")
    def test_add_user_in_schedule(self, setup_1):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_planning_meet_button()
        self.planning_meet_page.is_opened()
        self.planning_meet_page.add_topic()
        self.planning_meet_page.click_user_tab_button()
        self.planning_meet_page.select_user()
        self.planning_meet_page.save_schedule()
        self.planning_meet_page.click_on_user_avatar_button()
        self.planning_meet_page.click_on_log_out_button()
        self.login_page.is_opened()
        self.login_page.clear_login()
        self.login_page.enter_login(self.data.LOGIN2)
        self.login_page.clear_password()
        self.login_page.enter_password(self.data.PASSWORD2)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.planning_meet_page.check_planned_meet()
        self.planning_meet_page.make_screenshot("test_create_schedule")


