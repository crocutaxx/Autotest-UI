import allure
from base.base_test import BaseTest
import pytest

@allure.feature("Viewing a scheduled meeting Functionality")
class TestViewingAScheduledMeeting(BaseTest):

    @allure.title("Deleting meeting")
    @allure.severity("Normal")
    def test_deleting_meeting(self, user_1):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_planning_meet_button()
        self.planning_meet_page.is_opened()
        self.planning_meet_page.add_topic_for_deleting_meeting()
        self.planning_meet_page.save_schedule()
        self.main_page.open()
        self.main_page.click_on_meet_for_delete_button()
        self.main_page.click_on_delete_meet_button()
        self.main_page.click_on_confirm_action_button()
        self.main_page.check_push_meet_deleted()
        self.main_page.meet_is_deleted()
        self.main_page.make_screenshot("the meeting has been deleted")

    @allure.title("Canceling meeting")
    @allure.severity("Normal")
    def test_canceling_meeting(self, user_1):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_planning_meet_button()
        self.planning_meet_page.is_opened()
        self.planning_meet_page.add_topic()
        self.planning_meet_page.save_schedule()
        self.main_page.open()
        self.main_page.click_on_planned_name_meet()
        self.main_page.click_on_cancell_meet_button()
        self.main_page.click_on_confirm_action_button()
        self.main_page.check_push_meet_cancel()
        self.main_page.click_on_canceled_name_meet()
        self.main_page.meet_is_canceled()
        self.main_page.make_screenshot("the meeting has been canceled")
        self.main_page.click_on_delete_meet_button()
        self.main_page.click_on_confirm_action_button()
