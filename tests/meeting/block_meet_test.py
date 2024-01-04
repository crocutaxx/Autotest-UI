import allure
from base.base_test import BaseTest
import pytest

@allure.feature("Meet Functionality")
class TestBlockingMeet(BaseTest):


    @allure.title("Blocked room")
    @allure.severity("Normal")
    def test_blocking_meet(self, user_1, user_2):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_new_meet_button()
        # self.meet_page.is_opened() Разобраться с идентификатором комант
        # self.meet_page.click_on_dismiss_alert_button() # Нужен для локального запуска
        self.meet_page.click_on_enter_without_checking_button()
        self.meet_page.check_enter_meet_push()

        self.meet_page.click_on_more_button()
        self.meet_page.click_on_information_button()
        self.meet_page.get_identifier_from_information_window()
        self.meet_page.click_close_information_window_button()

        self.meet_page.click_on_more_button()
        self.meet_page.click_on_management_button()
        self.meet_page.switch_blocking_room_on()
        # second user script
        self.login_page_2.open()
        self.login_page_2.click_enter_meet_button()
        self.connect_to_meeting_page_2.is_opened()
        self.connect_to_meeting_page_2.enter_meet_identifier_from_json()
        self.connect_to_meeting_page_2.enter_user_name()
        self.connect_to_meeting_page_2.click_enter_button()
        # self.meet_page.click_on_dismiss_alert_button() # Нужен для локального запуска
        self.meet_page_2.click_on_enter_without_checking_button()
        # self.meet_page.click_on_dismiss_alert_button() #Нужен для локального запуска
        self.meet_page_2.click_on_enter_without_checking_button()

        self.meet_page_2.check_push_in_blocked_room()
        self.meet_page_2.make_screenshot("meet_is_blocked")