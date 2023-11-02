import random
import allure
import time
import pytest
from base.base_test import BaseTest

@allure.feature("Schedule Functionality")
class TestScheduleFeature(BaseTest):

    @allure.title("Create schedule")
    @allure.severity("Critical")
    def test_create_schedule(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_planning_meet_button()
        self.planning_meet_page.is_opened()
        self.planning_meet_page.add_topic(f"Test {random.randint(1, 100)}")
        self.planning_meet_page.add_meet_password(f"password {random.randint(1, 100)}")
        self.planning_meet_page.add_meet_description("Hello world!")
        self.planning_meet_page.save_schedule()
        self.planning_meet_page.topic_name_is_saved()
        self.planning_meet_page.meet_password_is_saved()
        self.planning_meet_page.meet_description_is_saved()
        self.planning_meet_page.make_screenshot("Success")

