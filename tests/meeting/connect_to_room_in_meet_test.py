import allure
from base.base_test import BaseTest
import pytest


@allure.feature("Meet Functionality")
class TestConnecToRoomInMeet(BaseTest):


    @allure.title("Connect to room in meet")
    @allure.severity("Normal")
    def test_connect_to_room_in_meet(self, user_1, user_2):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_planning_meet_button()
        self.planning_meet_page.is_opened()
        self.planning_meet_page.add_topic_for_create_room()
        self.planning_meet_page.click_user_tab_button()
        self.planning_meet_page.select_user()
        self.planning_meet_page.save_schedule()
        self.planning_meet_page.click_on_close_schedule_meeting_button()
        self.main_page.is_opened()
        self.main_page.click_on_meet_for_create_room_button()
        self.main_page.click_on_connect_to_meet_button()
        # self.meet_page.is_opened() Разобраться с идентификатором комант
        # self.meet_page.click_on_dismiss_alert_button() # Нужен для локального запуска
        self.meet_page.click_on_enter_without_checking_button()
        self.meet_page.check_enter_meet_push()
        self.meet_page.click_on_more_button()
        self.meet_page.click_on_rooms_button()
        self.meet_page.click_on_create_room_button()
        self.meet_page.enter_room_name()
        self.meet_page.click_on_modal_create_room_button()
        self.meet_page.close_room_widget()
        # start second user case
        self.login_page_2.open()
        self.login_page_2.is_opened()
        self.login_page_2.enter_login(self.data.LOGIN2)
        self.login_page_2.enter_password(self.data.PASSWORD2)
        self.login_page_2.click_submit_button()
        self.main_page_2.is_opened()
        self.main_page_2.click_on_meet_for_create_room_button()
        self.main_page_2.click_on_connect_to_meet_button()
        self.meet_page_2.click_on_enter_without_checking_button()
        self.meet_page_2.check_enter_meet_push()
        self.meet_page_2.click_on_more_button()
        self.meet_page_2.click_on_rooms_button()
        self.meet_page_2.click_on_connect_to_room_button()
        # self.meet_page.click_on_dismiss_alert_button()  # Нужен для локального запуска
        self.meet_page_2.click_on_enter_without_checking_button()
        self.meet_page_2.check_enter_meet_push()
        self.meet_page_2.click_on_more_button()
        self.meet_page_2.click_on_rooms_button()
        self.meet_page_2.check_return_to_main_room_button()
        self.meet_page.click_on_participants_button()
        self.meet_page.check_count_of_participants()
        self.meet_page.make_screenshot("created_room")
        self.main_page.open()
        self.main_page.is_opened()
        self.main_page.click_on_meet_for_create_room_button()
        self.main_page.click_on_delete_meet_button()
        self.main_page.click_on_confirm_action_button()