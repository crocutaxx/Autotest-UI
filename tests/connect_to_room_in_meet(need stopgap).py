import allure
from base.base_test import BaseTest
import pytest


@allure.feature("Meet Functionality")
class TestConnecToRoomInMeet(BaseTest):


    @allure.title("Connect to room in meet")
    @allure.severity("Normal")
    def test_connect_to_room_in_meet(self, setup_1, setup_2):
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
        self.planning_meet_page.click_on_close_schedule_meeting_button()
        self.main_page.click_on_planned_name_meet()
        # непонятно как передать идентификатор комнаты между двумя драйверами ???????????????


        self.main_page.click_on_new_meet_button()
        # self.meet_page.is_opened() Разобраться с идентификатором комант
        self.meet_page.click_on_dismiss_alert_button() # Нужен для локального запуска
        self.meet_page.click_on_enter_without_cheking_button()
        self.meet_page.check_enter_meet_push()



        self.meet_page.click_on_more_button()
        self.meet_page.make_screenshot("created_room")
        self.meet_page.click_on_rooms_button()
        self.meet_page.click_on_create_room_button()
        self.meet_page.enter_room_name()
        self.meet_page.click_on_modal_create_room_button()
        self.meet_page.close_room_vidget()
        self.meet_page.click_on_more_button()
        self.meet_page.click_on_information_button()
        self.meet_page.get_identificator_from_information_window()
        self.meet_page.click_close_information_window_button()
        # start second user case
        self.login_page_2.open()
        self.login_page_2.click_enter_meet_button()
        self.connect_to_meeting_page_2.enter_meet_identificator_from_information()
        self.meet_page_2.make_screenshot("created_room1")
        # self.connect_to_meeting_page_2.enter_user_name()
        # self.connect_to_meeting_page_2.click_enter_button()
        # self.meet_page_2.make_screenshot("created_room")
        # self.meet_page_2.click_on_enter_without_cheking_button() #1
        # self.meet_page_2.click_on_dismiss_alert_button() # Нужен для локального запуска
        # self.meet_page_2.click_on_enter_without_cheking_button()#3
        # self.meet_page_2.check_enter_meet_push()
        # # end second user test
        # self.meet_page.click_on_connect_to_toom_button()
        # self.meet_page.click_on_dismiss_alert_button()  # Нужен для локального запуска
        # self.meet_page.click_on_enter_without_cheking_button()
        # self.meet_page.check_enter_meet_push()
        # self.meet_page.click_on_more_button()
        # self.meet_page.click_on_rooms_button()
        # self.meet_page.check_return_to_main_room_button()
        # self.meet_page_2.click_on_participans_button()
        #
        # self.meet_page.make_screenshot("created_room")