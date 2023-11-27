import allure
from base.base_test import BaseTest
import pytest

@allure.feature("Meet Functionality")
class TestBlockingMeet(BaseTest):


    @allure.title("Blocked room")
    @allure.severity("Normal")
    def test_blocking_meet(self, setup_1, setup_2):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_planning_meet_button()
        self.planning_meet_page.is_opened()
        self.planning_meet_page.add_topic_for_block()
        self.planning_meet_page.click_user_tab_button()
        self.planning_meet_page.select_user()
        self.planning_meet_page.save_schedule()
        self.planning_meet_page.click_on_close_schedule_meeting_button()
        self.main_page.is_opened()
        self.main_page.click_on_meet_for_block_button()
        self.main_page.click_on_connect_to_meet_button()
        # self.meet_page.click_on_dismiss_alert_button() # Нужен для локального запуска
        self.meet_page.click_on_enter_without_cheking_button()
        self.meet_page.click_on_more_button()
        self.meet_page.click_on_managment_button()
        self.meet_page.switch_blocking_room_on()
        # second user script
        self.login_page_2.open()
        self.login_page_2.is_opened()
        self.login_page_2.enter_login(self.data.LOGIN2)
        self.login_page_2.enter_password(self.data.PASSWORD2)
        self.login_page_2.click_submit_button()
        self.main_page_2.is_opened()
        self.main_page_2.click_on_meet_for_block_button()
        self.main_page_2.meet_is_blocked()
        self.meet_page_2.make_screenshot("meet_is_blocked")
        self.main_page.open()
        self.main_page.is_opened()
        self.main_page.click_on_meet_for_block_button()
        self.main_page.click_on_delete_meet_button()
        self.main_page.click_on_confirm_action_button()